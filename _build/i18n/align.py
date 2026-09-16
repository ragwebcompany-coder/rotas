# -*- coding: utf-8 -*-
"""Cross-language alignment of a Greek article with its English original.

Positional matching is not safe here: the Greek pages occasionally add or drop
a heading, which shifts everything after it by one and silently pairs the wrong
paragraphs.  So we align the *headings* with a Needleman–Wunsch pass that scores
each candidate pair on signals that survive translation —

  * Latin-script tokens that are the same in both languages (RhIg, HPV, IVF, 3D)
  * digits
  * the class of question the heading asks (Τι→what, Πώς→how, Πότε→when,
    Πόσες→how many, Μπορεί→can, Υπάρχει→is there …)
  * relative length, and heading level

— and then fill in the blocks between two aligned headings positionally, but
only when both sides have the same number of them.
"""
import re

GREEK = re.compile(r'[Ͱ-Ͽἀ-῿]')
LATIN_TOKEN = re.compile(r'\b[A-Za-z][A-Za-z0-9/\-]{1,}\b')
LATIN_STOP = {
    'the', 'and', 'for', 'are', 'you', 'your', 'with', 'that', 'this', 'from',
    'what', 'when', 'how', 'why', 'who', 'which', 'can', 'may', 'will', 'does',
    'have', 'has', 'not', 'but', 'its', 'his', 'her', 'their', 'there', 'here',
    'about', 'into', 'than', 'then', 'them', 'they', 'been', 'being', 'was',
    'were', 'all', 'any', 'each', 'other', 'some', 'such', 'more', 'most',
    'kai', 'tis', 'tou', 'sto',
}

# Greek question openers -> abstract class
GR_Q = [
    (r'^τι\s+είναι|^τι\s+σημαίνει|^τι\s+ακριβώς', 'whatis'),
    (r'^τι\s+συμβαίνει', 'whathappens'),
    (r'^τι\b', 'what'),
    (r'^ποι[οαεί]\w*\s+είναι', 'what'),
    (r'^ποι[οαεί]', 'which'),
    (r'^πώς|^πως\b', 'how'),
    (r'^πότε|^ποτε\b', 'when'),
    (r'^πού\b|^που\b', 'where'),
    (r'^γιατί', 'why'),
    (r'^πόσ[οαεη]\w*\s+(καιρό|χρόνο|διαρκ)', 'howlong'),
    (r'^πόσ', 'howmany'),
    (r'^μπορ', 'can'),
    (r'^υπάρχ', 'isthere'),
    (r'^πρέπει|^χρειάζ', 'should'),
    (r'^είναι\b', 'is'),
    (r'^θα\b', 'will'),
]
EN_Q = [
    (r'^what\s+(is|are|does|do)\b', 'whatis'),
    (r'^what\s+happens', 'whathappens'),
    (r'^what\b', 'what'),
    (r'^which\b|^who\b', 'which'),
    (r'^how\s+(long|often|soon)\b', 'howlong'),
    (r'^how\s+(many|much)\b', 'howmany'),
    (r'^how\b', 'how'),
    (r'^when\b', 'when'),
    (r'^where\b', 'where'),
    (r'^why\b', 'why'),
    (r'^can\b|^could\b|^may\s+i\b', 'can'),
    (r'^is\s+there\b|^are\s+there\b', 'isthere'),
    (r'^should\b|^do\s+i\s+need\b|^must\b', 'should'),
    (r'^is\b|^are\b', 'is'),
    (r'^will\b', 'will'),
]
# classes that are close enough not to be evidence against a pair
NEAR = {frozenset(('what', 'whatis')), frozenset(('what', 'which')),
        frozenset(('which', 'whatis')), frozenset(('how', 'howmany')),
        frozenset(('how', 'howlong')), frozenset(('howmany', 'howlong')),
        frozenset(('is', 'isthere')), frozenset(('can', 'is')),
        frozenset(('should', 'can')), frozenset(('what', 'whathappens'))}


def qclass(text, table):
    t = text.strip().lower().lstrip('«"‘“')
    for pat, cls in table:
        if re.search(pat, t):
            return cls
    return None


def latin(text):
    return {t.lower() for t in LATIN_TOKEN.findall(text)
            if t.lower() not in LATIN_STOP and len(t) > 1}


def digits(text):
    return set(re.findall(r'\d+', text))


def pair_score(gr, en, gr_tag='h2', en_tag='h2'):
    """How much does this look like the same heading in the other language?"""
    if GREEK.search(en):
        return -9.0
    s = 0.0
    shared_lat = latin(gr) & latin(en)
    s += 3.0 * min(len(shared_lat), 3)
    only_gr_lat = latin(gr) - latin(en)
    s -= 1.5 * min(len(only_gr_lat), 2)

    dg, de = digits(gr), digits(en)
    s += 2.0 * min(len(dg & de), 3)
    if dg and not (dg & de):
        s -= 2.0

    cg, ce = qclass(gr, GR_Q), qclass(en, EN_Q)
    if cg and ce:
        if cg == ce:
            s += 4.0
        elif frozenset((cg, ce)) in NEAR:
            s += 1.0
        else:
            s -= 4.0
    elif cg or ce:
        s -= 1.0
    else:
        s += 0.5                      # both are plain statements

    ratio = len(en) / max(len(gr), 1)
    if 0.55 <= ratio <= 1.45:
        s += 1.5
    elif 0.40 <= ratio <= 1.80:
        s += 0.2
    else:
        s -= 2.0

    s += 0.8 if gr_tag == en_tag else -0.8
    return s


GAP = -1.2


def align(a, b, score=pair_score):
    """Needleman–Wunsch. a, b are lists of (tag, text). Returns list of
    (i, j) index pairs; i or j is None for an unmatched item."""
    n, m = len(a), len(b)
    F = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        F[i][0] = F[i - 1][0] + GAP
    for j in range(1, m + 1):
        F[0][j] = F[0][j - 1] + GAP
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = F[i - 1][j - 1] + score(a[i - 1][1], b[j - 1][1],
                                           a[i - 1][0], b[j - 1][0])
            F[i][j] = max(diag, F[i - 1][j] + GAP, F[i][j - 1] + GAP)
    out, i, j = [], n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            d = F[i - 1][j - 1] + score(a[i - 1][1], b[j - 1][1],
                                        a[i - 1][0], b[j - 1][0])
            if abs(F[i][j] - d) < 1e-9:
                out.append((i - 1, j - 1)); i -= 1; j -= 1; continue
        if i > 0 and abs(F[i][j] - (F[i - 1][j] + GAP)) < 1e-9:
            out.append((i - 1, None)); i -= 1; continue
        out.append((None, j - 1)); j -= 1
    out.reverse()
    return out

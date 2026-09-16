# -*- coding: utf-8 -*-
"""Recover the original English wording for pages that were translated from it.

The Greek articles on gynaicologos.gr were translated from the English patient
information that still lives in _build/i18n/old_en/.  For those topics we want
the original sentences back rather than a fresh translation.

Headings are aligned across the two languages by align.py; the paragraphs and
list items between two aligned headings are then paired off in order, but only
when both sides have exactly the same run of blocks.  Anything else is left
alone and reported, so it can be translated by hand instead of guessed at.

    python3 _build/i18n/harvest.py            # harvested.json + summary
    python3 _build/i18n/harvest.py --headings # every heading pair, to proofread
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
from pagemap import OLD_EN
from align import align, pair_score, GREEK
from overrides import FORCE, REJECT, SKIP_PAGES, MIN_COVERAGE

BLOCK = re.compile(r'<(h2|h3|h4|p|li|figcaption)\b[^>]*>(.*?)</\1>', re.S)
HEADS = ('h2', 'h3', 'h4')
MIN_HEADING_SCORE = 1.0


def blocks(path):
    """Ordered (tag, text) for the article body of a page."""
    html = open(path, encoding='utf-8').read()
    m = re.search(r'<article class="svc-body">(.*?)</article>', html, re.S)
    if not m:
        return []
    body = re.sub(r'<(script|style).*?</\1>', '', m.group(1), flags=re.S)
    out = []
    for b in BLOCK.finditer(body):
        text = re.sub(r'<[^>]+>', '', b.group(2))
        text = re.sub(r'\s+', ' ', text).strip()
        if text:
            out.append((b.group(1), text))
    return out


def digits(s):
    return set(re.findall(r'\d+', s))


def body_ok(gr, en):
    """Sanity check for a paragraph/list-item pair."""
    if not gr or not en or GREEK.search(en):
        return False
    if not 0.40 <= len(en) / len(gr) <= 1.80:
        return False
    dg, de = digits(gr), digits(en)
    if dg and not (dg & de):
        return False
    return True


def page_pairs(gr_path, en_path, rel=''):
    """-> (pairs, heading_rows, n_blocks, n_skipped, coverage)"""
    A, B = blocks(gr_path), blocks(en_path)
    if not A or not B:
        return [], [], len(A), 0, 0.0

    ai = [i for i, (t, _) in enumerate(A) if t in HEADS]
    bi = [j for j, (t, _) in enumerate(B) if t in HEADS]
    ah = [A[i] for i in ai]
    bh = [B[j] for j in bi]

    pairs, rows = [], []
    anchors = []                       # (gr_block_idx, en_block_idx)
    for x, y in align(ah, bh):
        if x is None or y is None:
            rows.append((ah[x][1] if x is not None else None,
                         bh[y][1] if y is not None else None, None))
            continue
        sc = pair_score(ah[x][1], bh[y][1], ah[x][0], bh[y][0])
        rows.append((ah[x][1], bh[y][1], sc))
        if sc < MIN_HEADING_SCORE or ah[x][1] in REJECT:
            continue
        pairs.append((ah[x][1], bh[y][1]))
        anchors.append((ai[x], bi[y]))

    # blocks between consecutive anchors, paired only on an exact run match
    skipped = 0
    spans = list(zip([(-1, -1)] + anchors, anchors + [(len(A), len(B))]))
    for (ga, ea), (gb, eb) in spans:
        g = [(t, s) for t, s in A[ga + 1:gb] if t not in HEADS]
        e = [(t, s) for t, s in B[ea + 1:eb] if t not in HEADS]
        if len(g) == len(e) and all(x[0] == y[0] for x, y in zip(g, e)):
            for (t, gs), (_, es) in zip(g, e):
                if GREEK.search(gs) and body_ok(gs, es):
                    pairs.append((gs, es))
                else:
                    skipped += 1
        else:
            skipped += len(g)

    n_heads = max(len(ah), len(bh)) or 1
    coverage = len(anchors) / n_heads
    if rel in SKIP_PAGES or coverage < MIN_COVERAGE:
        skipped += len(pairs)
        pairs = []
    return pairs, rows, len(A), skipped, coverage


def harvest():
    out, report, headings = {}, [], []
    clashes = 0
    for gr_path, old_path in sorted(OLD_EN.items()):
        pairs, rows, n, skipped, cov = page_pairs(os.path.join(ROOT, gr_path),
                                                  os.path.join(ROOT, old_path),
                                                  gr_path)
        for gr, en in pairs:
            if gr in out and out[gr] != en:
                clashes += 1
                continue
            out[gr] = en
        report.append((gr_path, len(pairs), skipped, n, cov))
        headings.append((gr_path, rows))
    out.update(FORCE)
    return out, report, headings, clashes


if __name__ == '__main__':
    pairs, report, headings, clashes = harvest()
    if '--headings' in sys.argv:
        for path, rows in headings:
            print('=' * 100)
            print(path)
            for gr, en, sc in rows:
                flag = '   ' if sc and sc >= MIN_HEADING_SCORE else '>>>'
                print(f" {flag} {(gr or '—')[:56]:<58}| {(en or '—')[:56]}"
                      f"{'' if sc is None else f'  [{sc:.1f}]'}")
        sys.exit()
    with open(os.path.join(HERE, 'harvested.json'), 'w', encoding='utf-8') as fh:
        json.dump(pairs, fh, ensure_ascii=False, indent=1, sort_keys=True)
    print(f"{len(pairs)} unique pairs  ({clashes} conflicting, dropped)\n")
    print(f"{'greek page':<52}{'paired':>8}{'skipped':>9}{'blocks':>8}{'cover':>8}")
    for path, k, skipped, n, cov in report:
        mark = '  hand' if k == 0 and n else ''
        print(f"{path:<52}{k:>8}{skipped:>9}{n:>8}{cov:>8.2f}{mark}")

# -*- coding: utf-8 -*-
"""Build the English mirror of gynaicologos.gr under en/.

Runs as a second pass over the Greek pages that build.py has just written:
every page is copied to its English address from _build/i18n/pagemap.py, its
text is swapped for the English in the dictionaries, and every internal link is
re-pointed at the English counterpart and re-relativised for the new depth.

Both languages are cross-linked with <link rel="alternate" hreflang="…">, which
is what i18n.js uses to put the EN / ΕΛ button in the nav — so the button always
lands on the same page in the other language, not on the home page.

    python3 _build/build.py      # Greek, then this
    python3 _build/build_en.py   # English only
"""
import json, os, re, sys, html as htmlmod

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, 'i18n'))

from pagemap import PAGES, EN_OF, RETIRED, DIRS          # noqa: E402
import strings as S                                       # noqa: E402

GREEK = re.compile(r'[Ͱ-Ͽἀ-῿]')
TAG = re.compile(r'(<[^>]*>)', re.S)
SKIP_TEXT_IN = ('script', 'style')

MISSING = {}          # greek string -> [pages it appears on]


# ---------------------------------------------------------------- dictionary

def load_dict():
    d = {}
    with open(os.path.join(HERE, 'i18n', 'harvested.json'), encoding='utf-8') as fh:
        d.update(json.load(fh))
    d.update(S.STRINGS)            # hand-written wins over harvested
    return d


TR = load_dict()
_norm = lambda s: re.sub(r'\s+', ' ', s).strip()


def translate(text, where=''):
    """Greek -> English for one run of text. Returns None when unknown."""
    key = _norm(text)
    if not key or not GREEK.search(key):
        return text

    if key in TR:
        return TR[key]

    # "Τίτλος | Ενότητα Δρ. Μιχάλης Ρώτας"
    if ' | ' in key:
        parts = [translate(p, where) for p in key.split(' | ')]
        if all(p is not None for p in parts):
            return ' | '.join(parts)

    # "Όλα · Μαιευτική", with or without a trailing arrow
    m = re.match(r'^Όλα\s*·\s*(.+)$', key)
    if m:
        rest = translate(m.group(1), where)
        if rest is not None:
            return 'All · ' + rest

    # "Γυναικολογία →"
    if key.endswith('→'):
        rest = translate(key[:-1].strip(), where)
        if rest is not None:
            return rest + ' →'

    # counts the generator writes into cards and hub links
    m = re.match(r'^Δείτε τις (\d+) υποενότητες$', key)
    if m:
        return f"See the {m.group(1)} subsections"
    m = re.match(r'^(\d+) (σελίδες|θέματα|ενότητες)$', key)
    if m:
        word = {'σελίδες': 'pages', 'θέματα': 'topics',
                'ενότητες': 'sections'}[m.group(2)]
        return f"{m.group(1)} {word}"

    # "Διαβάστε περισσότερα για δημοσιεύσεις."
    m = re.match(r'^Διαβάστε περισσότερα για (.+)\.$', key)
    if m:
        name = m.group(1)
        rest = TR.get(name) or TR.get(name[:1].upper() + name[1:])
        if rest:
            return f"Read more about {rest}."

    # "Μαιευτική Δρ. Μιχάλης Ρώτας" — the suffix of every page title
    m = re.match(r'^(.*?)\s+Δρ\. Μιχάλης Ρώτας$', key)
    if m and m.group(1):
        rest = translate(m.group(1), where)
        if rest is not None:
            return rest + ' · Dr. Michael Rotas'

    # meta descriptions are the first sentences of the lead paragraph, cut short
    if key.endswith('…'):
        stem = key[:-1].strip()
        for gr, en in TR.items():
            if gr.startswith(stem[:60]) and len(gr) >= len(stem):
                return clip(en)

    MISSING.setdefault(key, []).append(where)
    return None


def clip(text, limit=165):
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(' ', 1)[0]
    return cut.rstrip(' ,.;:') + '…'


# ---------------------------------------------------------------- links

ASSET_DIRS = ('assets/',)


def to_root(url, gr_page):
    """Resolve a page-relative URL to a root-relative one."""
    base = os.path.dirname(gr_page)
    return os.path.normpath(os.path.join(base, url)).replace(os.sep, '/')


def from_root(target, en_page):
    """Root-relative -> relative to the English page."""
    base = os.path.dirname(en_page) or '.'
    rel = os.path.relpath(target, base).replace(os.sep, '/')
    return rel


def map_url(url, gr_page, en_page):
    """Re-point an internal URL at the English site and fix its depth."""
    if re.match(r'^(https?:|mailto:|tel:|#|data:|//)', url):
        return None
    frag = ''
    if '#' in url:
        url, frag = url.split('#', 1)
        frag = '#' + frag
    if not url:
        return None
    root = to_root(url, gr_page)
    root = EN_OF.get(root, root)          # a page -> its English twin
    return from_root(root, en_page) + frag


ATTR_URL = re.compile(r'\b(href|src)="([^"]*)"')
ATTR_TEXT = re.compile(r'\b(alt|title|aria-label|placeholder|content)="([^"]*)"')


def fix_tag(tag, gr_page, en_page):
    def url_sub(m):
        new = map_url(m.group(2), gr_page, en_page)
        return f'{m.group(1)}="{new}"' if new else m.group(0)

    tag = ATTR_URL.sub(url_sub, tag)

    def text_sub(m):
        name, val = m.group(1), htmlmod.unescape(m.group(2))
        if not GREEK.search(val):
            return m.group(0)
        out = translate(val, gr_page)
        if out is None:
            return m.group(0)
        return f'{name}="{htmlmod.escape(out, quote=True)}"'

    return ATTR_TEXT.sub(text_sub, tag)


# ---------------------------------------------------------------- JSON-LD

def fix_ld(payload, gr_page, en_page):
    try:
        data = json.loads(payload)
    except ValueError:
        return payload

    def walk(node):
        if isinstance(node, dict):
            return {k: walk(v) for k, v in node.items()}
        if isinstance(node, list):
            return [walk(v) for v in node]
        if isinstance(node, str):
            if node.startswith('https://gynaicologos.gr/'):
                path = node[len('https://gynaicologos.gr/'):] or 'index.html'
                if path in EN_OF:
                    tail = EN_OF[path]
                    return 'https://gynaicologos.gr/' + ('' if tail == 'en/index.html' else tail)
                return node
            if GREEK.search(node):
                return translate(node, gr_page) or node
            return node
        return node

    return json.dumps(walk(data), ensure_ascii=False, separators=(',', ':'))


LD = re.compile(r'(<script type="application/ld\+json">)(.*?)(</script>)', re.S)


# ---------------------------------------------------------------- page

def canonical_for(en_page):
    tail = '' if en_page == 'en/index.html' else en_page
    return 'https://gynaicologos.gr/' + tail


def build_page(gr_page, en_page):
    src = open(os.path.join(ROOT, gr_page), encoding='utf-8').read()

    src = LD.sub(lambda m: m.group(1) + fix_ld(m.group(2), gr_page, en_page)
                 + m.group(3), src)

    out, skip = [], 0
    for chunk in TAG.split(src):
        if not chunk:
            continue
        if chunk.startswith('<'):
            low = chunk.lower()
            name = re.match(r'</?\s*([a-z0-9]+)', low)
            if name and name.group(1) in SKIP_TEXT_IN:
                skip += 1 if not low.startswith('</') else -1
                skip = max(skip, 0)
            out.append(fix_tag(chunk, gr_page, en_page)
                       if not chunk.startswith('<!') else chunk)
            continue
        if skip or not GREEK.search(chunk):
            out.append(chunk)
            continue
        lead = chunk[:len(chunk) - len(chunk.lstrip())]
        tail = chunk[len(chunk.rstrip()):]
        done = translate(htmlmod.unescape(chunk), gr_page)
        out.append(chunk if done is None
                   else lead + htmlmod.escape(done, quote=False) + tail)

    page = ''.join(out)
    page = page.replace('<html lang="el">', '<html lang="en">', 1)
    page = page.replace('content="el_GR"', 'content="en_US"')
    page = re.sub(r'(<link rel="canonical" href=")[^"]*(")',
                  lambda m: m.group(1) + canonical_for(en_page) + m.group(2), page)
    page = re.sub(r'(<meta property="og:url" content=")[^"]*(")',
                  lambda m: m.group(1) + canonical_for(en_page) + m.group(2), page)
    page = add_alternate(page, 'el', from_root(gr_page, en_page))
    return page


ALT = re.compile(r'\s*<link rel="alternate" hreflang="[^"]*"[^>]*>')


def add_alternate(page, lang, href):
    page = ALT.sub('', page)
    link = f'\n  <link rel="alternate" hreflang="{lang}" href="{href}" />'
    return page.replace('<link rel="stylesheet"', link.strip() + '\n  <link rel="stylesheet"', 1)


def annotate_greek(gr_page, en_page):
    """Point the Greek page at its English twin, for i18n.js and for search."""
    path = os.path.join(ROOT, gr_page)
    page = open(path, encoding='utf-8').read()
    new = add_alternate(page, 'en', from_root(en_page, gr_page))
    if new != page:
        open(path, 'w', encoding='utf-8').write(new)


# ---------------------------------------------------------------- redirects

REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>Moved</title>
<link rel="canonical" href="{canon}" />
<meta http-equiv="refresh" content="0; url={rel}" />
<meta name="robots" content="noindex, follow" />
</head>
<body><p>This page has moved to <a href="{rel}">{canon}</a>.</p></body>
</html>
"""


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8', newline='') as fh:
        fh.write(content)


def main():
    for gr_page, (en_page, _) in sorted(PAGES.items()):
        write(en_page, build_page(gr_page, en_page))
        annotate_greek(gr_page, en_page)

    for old, new in sorted(RETIRED.items()):
        write(old, REDIRECT.format(canon=canonical_for(new),
                                   rel=from_root(new, old)))

    print(f"✓ {len(PAGES)} English pages + {len(RETIRED)} redirects")
    if MISSING:
        path = os.path.join(HERE, 'i18n', 'missing.json')
        with open(path, 'w', encoding='utf-8') as fh:
            json.dump({k: sorted(set(v)) for k, v in
                       sorted(MISSING.items(), key=lambda kv: -len(kv[1]))},
                      fh, ensure_ascii=False, indent=1)
        chars = sum(len(k) for k in MISSING)
        print(f"! {len(MISSING)} strings still untranslated ({chars} chars) "
              f"-> _build/i18n/missing.json")


if __name__ == '__main__':
    main()

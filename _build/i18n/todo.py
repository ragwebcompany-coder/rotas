# -*- coding: utf-8 -*-
"""Show what still needs translating, in the order it appears on the page.

    python3 _build/i18n/todo.py                     # summary per section
    python3 _build/i18n/todo.py maieftiki           # every page in a section
    python3 _build/i18n/todo.py maieftiki/index.html
    python3 _build/i18n/todo.py maieftiki --stub    # paste-ready dict entries
"""
import json, os, re, sys, collections

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(HERE))

MISSING = os.path.join(HERE, 'missing.json')
TAG = re.compile(r'(<[^>]*>)', re.S)
GREEK = re.compile(r'[Ͱ-Ͽἀ-῿]')
ATTR = re.compile(r'\b(alt|title|aria-label|content)="([^"]*)"')


def page_order(rel, wanted):
    """The wanted strings, in document order, de-duplicated."""
    src = open(os.path.join(ROOT, rel), encoding='utf-8').read()
    src = re.sub(r'<script type="application/ld\+json">.*?</script>', '', src, flags=re.S)
    seen, out = set(), []
    for chunk in TAG.split(src):
        if not chunk:
            continue
        cands = ([v for _, v in ATTR.findall(chunk)] if chunk.startswith('<')
                 else [chunk])
        for c in cands:
            key = re.sub(r'\s+', ' ', c).strip()
            if key in wanted and key not in seen:
                seen.add(key)
                out.append(key)
    return out + [k for k in wanted if k not in seen]


def main():
    data = json.load(open(MISSING, encoding='utf-8'))
    by_page = collections.defaultdict(set)
    for text, pages in data.items():
        for p in pages:
            by_page[p].add(text)

    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    stub = '--stub' in sys.argv
    keys_only = '--keys' in sys.argv

    if not args:
        sec = collections.Counter()
        for p, s in by_page.items():
            sec[p.split('/')[0] if '/' in p else 'root'] += sum(len(x) for x in s)
        for s, c in sec.most_common():
            print(f"{s:<18}{c:>8} chars")
        print(f"{'TOTAL':<18}{sum(sec.values()):>8} chars, {len(data)} strings")
        return

    target = args[0]
    pages = sorted(p for p in by_page
                   if p == target or p.startswith(target.rstrip('/') + '/'))
    for p in pages:
        items = page_order(p, by_page[p])
        chars = sum(len(i) for i in items)
        if keys_only:
            print(f"# {p}  ({len(items)} strings, {chars} chars)")
            for n, t in enumerate(items, 1):
                print(f"{n}. {t}")
        elif stub:
            print(f"\n    # ---- {p}  ({len(items)} strings, {chars} chars)")
            for t in items:
                print(f'    {t!r}:\n        "",')
        else:
            print(f"\n{'=' * 78}\n{p}  ({len(items)} strings, {chars} chars)\n")
            for t in items:
                print(f"  • {t}")


if __name__ == '__main__':
    main()

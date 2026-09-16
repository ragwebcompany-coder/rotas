# -*- coding: utf-8 -*-
"""Attach English translations to the exact Greek strings of a page.

Typing the Greek key by hand is error-prone: the source mixes Greek and Latin
look-alike letters (Τ/T, Α/A, Ο/O), so a re-typed key silently fails to match
and the page quietly stays Greek.  So we never re-type it.  `todo.py <page>
--keys` prints the outstanding strings numbered in document order; the English
goes into a file of "<n>|<english>" lines, and this script pairs them up by
number and stores them in manual.json, keyed by the real Greek string.

    python3 _build/i18n/todo.py maieftiki/index.html --keys
    python3 _build/i18n/apply.py maieftiki/index.html translations.txt
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MANUAL = os.path.join(HERE, 'manual.json')
sys.path.insert(0, HERE)
from todo import page_order, MISSING as MISSING_PATH  # noqa: E402


def load(path):
    if os.path.exists(path):
        with open(path, encoding='utf-8') as fh:
            return json.load(fh)
    return {}


def main():
    page, src = sys.argv[1], sys.argv[2]
    data = json.load(open(MISSING_PATH, encoding='utf-8'))
    wanted = {t for t, pages in data.items() if page in pages}
    keys = page_order(page, wanted)

    manual = load(MANUAL)
    added = skipped = 0
    for line in open(src, encoding='utf-8'):
        line = line.rstrip('\n')
        if not line.strip() or '|' not in line:
            continue
        num, english = line.split('|', 1)
        try:
            idx = int(num.strip()) - 1
        except ValueError:
            continue
        english = english.strip()
        if not english or not (0 <= idx < len(keys)):
            skipped += 1
            continue
        manual[keys[idx]] = english
        added += 1

    with open(MANUAL, 'w', encoding='utf-8') as fh:
        json.dump(manual, fh, ensure_ascii=False, indent=1, sort_keys=True)
    print(f"{page}: {added} translated, {skipped} skipped, "
          f"{len(keys) - added} left on this page ({len(manual)} total)")


if __name__ == '__main__':
    main()

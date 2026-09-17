# -*- coding: utf-8 -*-
"""Hand-written Greek → English strings, one module per part of the site.

Anything the automatic harvest could not recover from the old English pages is
translated here.  Keys are the Greek text exactly as it appears in the
generated page, with runs of whitespace collapsed to single spaces.
"""
from . import (chrome, titles, home, contact, iatros, maieftiki, embryomitriki, embryomitriki2,
               gynaikologia, gynaikologia2, gynaikologia3, gynaikologia4, xeirourgeia, xeirourgeia2, xeirourgeia3, ypogonimotita)

import json as _json, os as _os

STRINGS = {}
for _m in (chrome, titles, home, contact, iatros, maieftiki, embryomitriki, embryomitriki2,
           gynaikologia, gynaikologia2, gynaikologia3, gynaikologia4, xeirourgeia, xeirourgeia2, xeirourgeia3, ypogonimotita):
    STRINGS.update(_m.STRINGS)

# translations attached by apply.py, keyed by the exact Greek string
_manual = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                        'manual.json')
if _os.path.exists(_manual):
    with open(_manual, encoding='utf-8') as _fh:
        STRINGS.update(_json.load(_fh))

# Ο generator περνάει κάθε σελίδα από το strip_dashes() (build.py): το " — "
# γίνεται " ". Τα κλειδιά εδώ κρατούν την παύλα, οπότε κρατάμε και την εκδοχή
# χωρίς αυτήν, αλλιώς οι ίδιες φράσεις μένουν αμετάφραστες στο /en/.
import re as _re
_DASH = _re.compile(r" ([-–—]+) ")
for _k, _v in list(STRINGS.items()):
    _flat = _DASH.sub(" ", _k)
    if _flat != _k:
        STRINGS.setdefault(_flat, _v)

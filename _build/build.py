# -*- coding: utf-8 -*-
"""Static site generator for gynaicologos.gr.

Reads content.json (scraped from the live WordPress site) + structure.py
and emits a complete static site into the parent directory.

    python3 _build/build.py
"""
import json, os, re, html, sys, datetime, shutil, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from structure import SITE, SECTIONS  # noqa: E402

CONTENT = json.load(open(os.path.join(HERE, "content.json"), encoding="utf-8"))
TODAY = datetime.date.today().isoformat()

# ---------------------------------------------------------------- helpers

def esc(s):
    return html.escape(s, quote=False)


def attr(s):
    return html.escape(s, quote=True)


def clean(s):
    s = re.sub(r"\s+", " ", s).strip()
    s = s.replace("&nbsp;", " ").replace(" ", " ")
    return s.strip()


# Boilerplate that repeats at the bottom of many source pages — the new site
# carries this in the aside / footer instead.
DROP_PATTERNS = [
    r"^ΙΑΤΡΕΙΟ\s", r"^Τηλ\.?:", r"^Κιν\.?:", r"^e-?mail", r"^T\.?K\.?",
    r"^Λεωφόρος Βασιλίσσης Σοφίας", r"^25ης Μαρτίου", r"^Κεντρική Πλατεία",
    r"^Νέα Σμύρνη$", r"^Αθήνα$", r"^Επικοινωνία$",
    r"^Ρώτας Μιχάλης MD", r"^Μαιευτήρας – Χειρουργός Γυναικολόγος$",
    r"^Ειδικός Εμβρυομητρικής", r"^O ιατρός δέχεται κατόπιν ραντεβού",
    # Per-page CTA boilerplate repeated verbatim across the source site — the
    # new site carries this once, in the aside and the CTA band.
    r"^Για ραντεβού", r"^Η γνώση, η εμπειρία και η εξειδίκευση του ιατρού",
    r"^Ο ιατρός εξετάζει κατόπιν", r"^O ιατρός εξετάζει κατόπιν",
]
DROP_RE = re.compile("|".join(DROP_PATTERNS))


def fold(s):
    """Lowercase and strip accents — for comparing Greek strings."""
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower().strip()


def is_question(text):
    """Source pages use <p> for what are really sub-headings."""
    t = text.strip()
    if t.endswith(";") or t.endswith("?"):
        return len(t) <= 120
    # A colon usually introduces the list that follows, not a section — only
    # treat very short colon-terminated lines as headings.
    return t.endswith(":") and len(t) <= 55


# ---------------------------------------------------------------- body render

def render_body(slug, title):
    """Turn scraped blocks into clean, semantic article HTML."""
    if not slug:                      # "" is the homepage key — never a section body
        return "", 0
    page = CONTENT.get(slug)
    if not page:
        return "", 0
    blocks = page.get("blocks", [])
    out = []
    first_para_done = False
    words = 0

    # Drop a leading heading that just repeats the page title.
    bs = list(blocks)
    if bs and bs[0]["t"] == "h":
        h0 = clean(bs[0]["v"])
        if fold(h0) == fold(title) or len(h0) < 4:
            bs = bs[1:]

    for b in bs:
        if b["t"] == "h":
            v = clean(b["v"])
            if not v or DROP_RE.match(v):
                continue
            lvl = "h2" if b.get("lvl") in ("h1", "h2") else "h3"
            out.append(f"<{lvl}>{esc(v)}</{lvl}>")
            words += len(v.split())
        elif b["t"] == "p":
            v = clean(b["v"])
            if not v or DROP_RE.match(v):
                continue
            if is_question(v):
                out.append(f"<h2>{esc(v)}</h2>")
            else:
                cls = ' class="lead-p"' if not first_para_done else ""
                out.append(f"<p{cls}>{esc(v)}</p>")
                first_para_done = True
            words += len(v.split())
        elif b["t"] == "list":
            items = [clean(i) for i in b["v"]]
            items = [i for i in items if i and not DROP_RE.match(i)]
            if not items:
                continue
            tag = "ol" if b.get("ordered") else "ul"
            cls = "numlist" if b.get("ordered") else "ticks"
            lis = "".join(f"<li>{esc(i)}</li>" for i in items)
            out.append(f'<{tag} class="{cls}">{lis}</{tag}>')
            words += sum(len(i.split()) for i in items)
        elif b["t"] == "quote":
            v = clean(b["v"])
            if not v or DROP_RE.match(v):
                continue
            out.append(f"<blockquote>{esc(v)}</blockquote>")
            words += len(v.split())

    return "\n        ".join(out), words


def excerpt(slug, fallback):
    """Short teaser for cards / meta descriptions."""
    page = CONTENT.get(slug) if slug else None
    if page:
        for b in page.get("blocks", []):
            if b["t"] == "p":
                v = clean(b["v"])
                if v and not DROP_RE.match(v) and not is_question(v) and len(v) > 60:
                    if len(v) > 175:
                        v = v[:172].rsplit(" ", 1)[0] + "…"
                    return v
    return fallback


# ---------------------------------------------------------------- page index

class Page:
    def __init__(self, path, title, nav_title, section, parent=None):
        self.path = path              # e.g. "maieftiki/didymi-kyisi.html"
        self.title = title
        self.nav_title = nav_title
        self.section = section
        self.parent = parent
        self.children = []


ALL = {}       # path -> Page
SECT_PAGES = {}  # section dir -> [top-level Page]


def build_index():
    for sec in SECTIONS:
        d = sec["dir"]
        hub = Page(f"{d}/index.html", sec["title"], sec["nav"], sec)
        hub.src = sec.get("src")
        ALL[hub.path] = hub
        SECT_PAGES[d] = []

        def add(items, parent):
            for src, lat, title, kids in items:
                p = Page(f"{d}/{lat}.html", title, title, sec, parent)
                p.src = src
                ALL[p.path] = p
                parent.children.append(p)
                add(kids, p)

        add(sec["pages"], hub)
        SECT_PAGES[d] = hub.children


build_index()


# ---------------------------------------------------------------- chrome

def rel(from_path, to_path):
    """Relative URL between two site paths."""
    fd = os.path.dirname(from_path)
    r = os.path.relpath(to_path, fd or ".")
    return r.replace(os.sep, "/")


def nav_html(cur):
    """Main navigation with mega-dropdowns."""
    items = [f'<li><a href="{rel(cur, "index.html")}"'
             + (' aria-current="page"' if cur == "index.html" else "")
             + ">Αρχική</a></li>"]
    for sec in SECTIONS:
        d = sec["dir"]
        hub = ALL[f"{d}/index.html"]
        active = cur.startswith(d + "/")
        subs = []
        for c in hub.children:
            subs.append(f'<li><a href="{rel(cur, c.path)}">{esc(c.nav_title)}</a></li>')
            if c.children:
                nested = "".join(
                    f'<li><a href="{rel(cur, g.path)}">{esc(g.nav_title)}</a></li>'
                    for g in c.children
                )
                subs.append(f'<li><ul class="sub-nested">{nested}</ul></li>')
        items.append(
            f'<li class="has-sub"><a href="{rel(cur, hub.path)}"'
            + (' aria-current="true"' if active else "")
            + f">{esc(sec['nav'])}</a>"
            + f'<ul class="sub"><li><a class="sub-head" href="{rel(cur, hub.path)}">'
            + f"Όλα · {esc(sec['title'])}</a></li>"
            + "".join(subs)
            + "</ul></li>"
        )
    items.append(f'<li><a href="{rel(cur, "epikoinonia.html")}">Επικοινωνία</a></li>')
    items.append(f'<li><a href="tel:+30{SITE["mobile"]}" class="btn btn-nav">Ραντεβού</a></li>')
    return "\n        ".join(items)


def footer_html(cur):
    a, b = SITE["clinics"]
    svc_links = "".join(
        f'<a href="{rel(cur, ALL[sec["dir"] + "/index.html"].path)}">{esc(sec["title"])}</a>'
        for sec in SECTIONS
    )
    social = "".join(
        f'<a href="{u}" target="_blank" rel="noopener noreferrer">{n}</a>'
        for n, u in SITE["social"]
    )
    return f"""  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <img src="{rel(cur, 'assets/logo.png')}" alt="Δρ. Μιχάλης Ρώτας" class="footer-logo" width="220" height="90" loading="lazy" />
        <p class="footer-tag">Επιστήμη, εμπειρία &amp; ανθρώπινη φροντίδα.</p>
        <p class="footer-addr">
          {esc(SITE['role'])}<br />
          {esc(SITE['role2'])}
        </p>
        <div class="footer-social">{social}</div>
      </div>

      <div class="footer-col">
        <h3>{esc(a['name'])}</h3>
        <p class="footer-addr">{esc(a['brand'])}<br />{esc(a['addr'])}<br />{esc(a['city'])}, Τ.Κ. {a['zip']}</p>
        <nav aria-label="{attr(a['name'])}" class="footer-links">
          <a href="tel:+30{a['tel']}">Τηλ. {a['tel_fmt']}</a>
          <a href="tel:+30{SITE['mobile']}">Κιν. {SITE['mobile_fmt']}</a>
          <a href="mailto:{SITE['email']}">{SITE['email']}</a>
        </nav>
      </div>

      <div class="footer-col">
        <h3>{esc(b['name'])}</h3>
        <p class="footer-addr">{esc(b['brand'])}<br />{esc(b['addr'])}<br />{esc(b['city'])}, Τ.Κ. {b['zip']}</p>
        <nav aria-label="{attr(b['name'])}" class="footer-links">
          <a href="tel:+30{b['tel']}">Τηλ. {b['tel_fmt']}</a>
          <a href="tel:+30{SITE['mobile']}">Κιν. {SITE['mobile_fmt']}</a>
          <a href="mailto:{SITE['email']}">{SITE['email']}</a>
        </nav>
      </div>

      <div class="footer-col">
        <h3>Υπηρεσίες</h3>
        <nav aria-label="Υπηρεσίες" class="footer-links">
          {svc_links}
          <a href="{rel(cur, 'epikoinonia.html')}">Επικοινωνία</a>
        </nav>
        <p class="footer-hours">Ο ιατρός δέχεται κατόπιν ραντεβού.</p>
      </div>
    </div>

    <p class="medical-disclaimer">Το περιεχόμενο του ιστότοπου έχει ενημερωτικό χαρακτήρα και δεν
      υποκαθιστά την ιατρική συμβουλή, διάγνωση ή θεραπεία. Για κάθε θέμα υγείας απευθυνθείτε
      στον ιατρό σας.</p>

    <div class="footer-bottom">
      <p class="footer-copy">© <span id="year">{TODAY[:4]}</span> gynaicologos.gr — {esc(SITE['full'])}. Με επιφύλαξη παντός δικαιώματος.</p>
      <p class="cb-credit">Made by <a href="https://clinicbrain.gr/?utm_source=client-site&amp;utm_medium=footer&amp;utm_campaign=made-by" target="_blank" rel="noopener noreferrer">CLINICBRAIN</a></p>
    </div>
  </footer>"""


def cta_html(cur):
    return f"""  <section class="cta-band">
    <div class="container cta-inner">
      <div>
        <p class="eyebrow">Κλείστε το ραντεβού σας</p>
        <h2 class="cta-title">Είμαστε εδώ για κάθε ερώτημα<br />σχετικά με την υγεία σας.</h2>
        <p class="cta-sub">Ιατρεία σε Αθήνα (Βασ. Σοφίας) και Νέα Σμύρνη — κατόπιν ραντεβού.</p>
      </div>
      <div class="cta-actions">
        <a href="tel:+30{SITE['mobile']}" class="btn btn-primary">Καλέστε {SITE['mobile_fmt']}</a>
        <a href="{rel(cur, 'epikoinonia.html')}" class="btn btn-ghost">Στοιχεία Επικοινωνίας</a>
      </div>
    </div>
  </section>"""


def ld_clinic():
    a, b = SITE["clinics"]
    def loc(c):
        return {
            "@type": "MedicalClinic",
            "name": f"{SITE['full']} — {c['name']}",
            "telephone": "+30" + c["tel"],
            "address": {
                "@type": "PostalAddress",
                "streetAddress": c["addr"],
                "addressLocality": c["city"],
                "postalCode": c["zip"],
                "addressCountry": "GR",
            },
        }
    data = {
        "@context": "https://schema.org",
        "@type": ["Physician", "MedicalBusiness"],
        "@id": SITE["domain"] + "/#physician",
        "name": SITE["full"],
        "medicalSpecialty": ["Obstetric", "Gynecologic"],
        "url": SITE["domain"] + "/",
        "email": SITE["email"],
        "telephone": "+30" + SITE["mobile"],
        "image": SITE["domain"] + "/assets/dr-rotas.jpg",
        "sameAs": [u for _, u in SITE["social"]],
        "address": loc(a)["address"],
        "location": [loc(a), loc(b)],
    }
    return json.dumps(data, ensure_ascii=False, separators=(",", ":"))


def shell(path, title, desc, body, extra_ld=None, keywords=None):
    canon = SITE["domain"] + "/" + path
    ld = f'\n  <script type="application/ld+json">{ld_clinic()}</script>'
    if extra_ld:
        ld += f'\n  <script type="application/ld+json">{extra_ld}</script>'
    kw = f'\n  <meta name="keywords" content="{attr(keywords)}" />' if keywords else ""
    return f"""<!DOCTYPE html>
<html lang="el">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{esc(title)}</title>
  <meta name="description" content="{attr(desc)}" />{kw}
  <meta name="author" content="{attr(SITE['full'])}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="theme-color" content="#f9edf7" />
  <link rel="canonical" href="{canon}" />

  <meta property="og:site_name" content="{attr(SITE['full'])}" />
  <meta property="og:locale" content="el_GR" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{attr(title)}" />
  <meta property="og:description" content="{attr(desc)}" />
  <meta property="og:url" content="{canon}" />
  <meta property="og:image" content="{SITE['domain']}/assets/dr-rotas.jpg" />
  <meta name="twitter:card" content="summary_large_image" />

  <link rel="icon" type="image/png" href="{rel(path, 'assets/logo.png')}" />
  <link rel="apple-touch-icon" href="{rel(path, 'assets/logo.png')}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{rel(path, 'styles.css')}" />{ld}
</head>
<body>
  <a class="skip-link" href="#main">Μετάβαση στο περιεχόμενο</a>
  <header class="site-header" id="top">
    <nav class="nav container" aria-label="Κύρια πλοήγηση">
      <a href="{rel(path, 'index.html')}" class="brand" aria-label="{attr(SITE['full'])} — Αρχική">
        <img src="{rel(path, 'assets/logo.png')}" alt="{attr(SITE['full'])}" class="brand-logo" width="220" height="90" />
      </a>
      <button class="nav-toggle" aria-label="Άνοιγμα μενού" aria-expanded="false"><span></span><span></span><span></span></button>
      <ul class="nav-links">
        {nav_html(path)}
      </ul>
    </nav>
  </header>
{body}
{cta_html(path)}
{footer_html(path)}
  <script src="{rel(path, 'main.js')}" defer></script>
</body>
</html>
"""


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


def crumbs(cur, trail):
    parts = [f'<a href="{rel(cur, "index.html")}">Αρχική</a>']
    for t, p in trail[:-1]:
        parts.append(f'<a href="{rel(cur, p)}">{esc(t)}</a>')
    parts.append(f'<span aria-current="page">{esc(trail[-1][0])}</span>')
    body = '<span class="sep">/</span>'.join(parts)
    ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Αρχική", "item": SITE["domain"] + "/"}
        ] + [
            {"@type": "ListItem", "position": i + 2, "name": t,
             "item": SITE["domain"] + "/" + p}
            for i, (t, p) in enumerate(trail)
        ],
    }, ensure_ascii=False, separators=(",", ":"))
    return f'<nav class="crumbs container" aria-label="Διαδρομή">{body}</nav>', ld


# ---------------------------------------------------------------- home data

TESTIMONIALS = [
    ("Είναι πολύ σχολαστικός κατά τη διάρκεια παρακολούθησης μίας εγκυμοσύνης και απαντάει σε "
     "όλες τις ερωτήσεις/απορίες με ειλικρίνεια και καθησυχασμό. Μορφωμένος άνθρωπος, προσιτός "
     "και γνωρίζει πολύ καλά το αντικείμενό του με αποτέλεσμα να εμπνέει εμπιστοσύνη.",
     "Δήμητρα Ρ."),
    ("Απλά ο καλύτερος γυναικολόγος που έχω επισκεφθεί. Ένιωσα πολύ άνετα στην εξέταση, μου τα "
     "εξήγησε όλα στον υπέρηχο με εικόνες. Φοβερά μηχανήματα και πανέμορφο ιατρείο. Θα "
     "συνεχίσουμε εδώ χωρίς αμφιβολία.",
     "Miranda M."),
    ("Εξαιρετικός γιατρός! Ασχολήθηκε πολύ με την περίπτωσή μου και αφιέρωσε πολύ χρόνο να "
     "απαντήσει στις χιλιάδες ερωτήσεις μου. Ήρεμος, σοβαρός, φιλικός και με πολλή υπομονή. "
     "Άψογα καταρτισμένος, κορυφαίος επιστήμονας.",
     "Μαρίνα Μ."),
    ("Μετά από πολλά χρόνια εμπειρίας από διάφορους γιατρούς, είναι η πρώτη φορά που ένας "
     "γυναικολόγος με κάνει — τόσο εμένα, όσο και την έφηβη κόρη μου — να νιώθουμε ασφάλεια, "
     "οικειότητα και εμπιστοσύνη.",
     "Χριστίνα Δ."),
    ("Όντας κάτοικος Ηνωμένου Βασιλείου, η υποστήριξη και καθοδήγηση του κ. Ρώτα κατά τη "
     "διάρκεια της εγκυμοσύνης μου είναι πολύτιμη. Ο γιατρός είναι διαθέσιμος ανά πάσα στιγμή "
     "να δώσει συμβουλές και να απαντήσει σε οποιαδήποτε ερώτηση.",
     "Anastasia T."),
    ("Ο καλύτερος γιατρός! Άρτια καταρτισμένος, έμπειρος και πάντα διαθέσιμος να λύσει κάθε "
     "απορία. Η εγκυμοσύνη μου αλλά και ο τοκετός κύλισαν υπέροχα, χάρη στον κύριο Ρώτα.",
     "Ηλιάνα Χ."),
]

STATS = [
    (9900, "", "Τοκετοί"),
    (10150, "", "Αυχενικές Διαφάνειες"),
    (7550, "", "Κολποσκοπήσεις"),
    (6300, "", "Περιστατικά κονδυλωμάτων"),
]

CREDS = [
    ("FACOG", "Μέλος του Αμερικανικού Κολλεγίου Μαιευτήρων Γυναικολόγων"),
    ("Diploma in Fetal Medicine", "Fetal Medicine Foundation, Λονδίνο — ανώτερος βαθμός πιστοποίησης στην Εμβρυομητρική Ιατρική"),
    ("USC · VCMC", "Τ. Επιμελητής Μαιευτικής &amp; Γυναικολογίας, University of Southern California"),
    ("ΛΗΤΩ &amp; ΡΕΑ", "Επιμελητής Τμήματος Εμβρυομητρικής Ιατρικής"),
    ("AAGL Award", "Βράβευση από την Αμερικανική Ένωση Γυναικολογικής Λαπαροσκόπησης"),
    ("Green Journal", "Μέλος της κριτικής επιτροπής του Obstetrics and Gynecology"),
]

HOME_CREDS = [
    "Απόφοιτος της Ιατρικής Σχολής του Πανεπιστημίου Αθηνών με πολλαπλές διακρίσεις και "
    "υποτροφίες από το Κρατικό Ίδρυμα Υποτροφιών.",
    "Ειδίκευση σε μεγάλα πανεπιστημιακά νοσοκομεία, μεταξύ αυτών το State University of "
    "New York in Brooklyn – Maimonides Medical Center.",
    "Πολυετής εκπαίδευση και εργασιακή εμπειρία σε πανεπιστημιακά νοσοκομεία των ΗΠΑ και "
    "του Ηνωμένου Βασιλείου.",
    "Εργάσθηκε στο Memorial Sloan Kettering Cancer Center, ένα από τα μεγαλύτερα "
    "εξειδικευμένα ογκολογικά κέντρα παγκοσμίως.",
    "Βραβεύθηκε από την Αμερικανική Ένωση Γυναικολογικής Λαπαροσκόπησης (AAGL) για τις "
    "εξαιρετικές χειρουργικές δεξιότητές του.",
    "Κάτοχος του ανώτερου βαθμού πιστοποίησης στην Εμβρυομητρική Ιατρική "
    "(Diploma in Fetal Medicine).",
]

STEPS = [
    ("Εξέταση", "Αναλυτικό ιστορικό και κλινική εξέταση με σύγχρονο υπερηχογραφικό εξοπλισμό."),
    ("Διάγνωση", "Τεκμηριωμένη διάγνωση και πλήρης επεξήγηση κάθε εύρημα, βήμα προς βήμα."),
    ("Παρακολούθηση", "Εξατομικευμένο πλάνο παρακολούθησης, προσαρμοσμένο στη δική σας περίπτωση."),
    ("Θεραπεία", "Θεραπευτική αντιμετώπιση — συντηρητική ή χειρουργική — με σαφή στόχο και χρονοδιάγραμμα."),
]

IATREIO_SERVICES = [
    "Γυναικολογική εξέταση – Τεστ ΠΑΠ", "Καλλιέργεια κολπικού υγρού",
    "Τοποθέτηση σπιράλ", "Γυναικολογικό 3D υπερηχογράφημα",
    "Κολποσκόπηση – Βιοψία τραχήλου", "Καυτηριασμός κονδυλωμάτων – Laser",
    "Αυχενική Διαφάνεια", "Υπερηχογράφημα Β’ Επιπέδου",
    "Υπερηχογράφημα κύησης Doppler", "Καρδιοτοκογράφημα ηρεμίας (NST)",
    "Λήψη τροφοβλάστης", "Αμνιοπαρακέντηση",
    "Μη επεμβατικός προγεννητικός έλεγχος (NIPT)", "Υπερηχογράφημα μαστών",
    "Σονο-υστερο υπερηχογραφία", "Σπερματέγχυση",
]


# ---------------------------------------------------------------- renderers

def render_home():
    cur = "index.html"
    svc_cards = []
    for i, sec in enumerate(SECTIONS, 1):
        hub = ALL[sec["dir"] + "/index.html"]
        n = len(hub.children) + sum(len(c.children) for c in hub.children)
        svc_cards.append(f"""        <a class="svc reveal" href="{rel(cur, hub.path)}">
          <span class="svc-icon" aria-hidden="true">{sec['icon']}</span>
          <span class="svc-num">{i:02d}</span>
          <h3>{esc(sec['title'])}</h3>
          <p>{esc(sec['lead'])}</p>
          <span class="svc-more">{n} σελίδ{'α' if n == 1 else 'ες'} →</span>
        </a>""")

    creds_li = "".join(f"<li>{esc(c)}</li>" for c in HOME_CREDS)
    stats_html = "".join(
        f'<div class="stat"><span class="stat-n" data-count="{n}" data-suffix="{s}">0</span>'
        f'<span class="stat-l">{esc(l)}</span></div>'
        for n, s, l in STATS
    )
    steps_html = "".join(
        f'<div class="step reveal"><span class="step-n">{i:02d}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
        for i, (t, d) in enumerate(STEPS, 1)
    )
    quotes = "".join(
        f'<figure class="quote-card reveal"><p>{esc(t)}</p>'
        f'<figcaption class="quote-who">{esc(w)} · Doctoranytime</figcaption></figure>'
        for t, w in TESTIMONIALS
    )
    creds_grid = "".join(
        f'<div class="cred"><span class="cred-k">{k}</span><span class="cred-v">{v}</span></div>'
        for k, v in CREDS
    )
    a, b = SITE["clinics"]
    clinic_cards = "".join(f"""        <a class="clinic-card reveal" href="{rel(cur, 'iatros/iatreio-' + ('athinon' if c['id'] == 'athina' else 'neas-smyrnis') + '.html')}">
          <img src="{rel(cur, 'assets/clinic-' + ('1' if c['id'] == 'athina' else '5') + '.jpg')}" alt="{attr(c['name'])}" width="632" height="412" loading="lazy" />
          <div class="clinic-body">
            <h3>{esc(c['name'])}</h3>
            <p>{esc(c['brand'])}<br />{esc(c['addr'])}, {esc(c['city'])}</p>
            <span class="svc-more">Δείτε τον χώρο →</span>
          </div>
        </a>""" for c in (a, b))

    strip_items = ["Εμβρυομητρική Ιατρική", "Κύηση Υψηλού Κινδύνου", "Ελάχιστα Επεμβατική Χειρουργική",
                   "Υπογονιμότητα", "Προγεννητικός Έλεγχος"]
    strip = "".join(f'<span>{esc(s)}</span><span class="dot">•</span>' for s in strip_items * 2)

    body = f"""  <main id="main">
    <section class="hero" id="hero">
      <div class="hero-inner container">
        <p class="eyebrow reveal">{esc(SITE['role'])} · Αθήνα &amp; Νέα Σμύρνη</p>
        <h1 class="hero-title reveal">Ρώτας Μιχάλης<br /><em>MD, FACOG</em></h1>
        <p class="hero-lead reveal">Ειδικός Εμβρυομητρικής Ιατρικής με δεκαετή διεθνή καριέρα σε
          πανεπιστημιακά νοσοκομεία των ΗΠΑ και του Ηνωμένου Βασιλείου — για μια εγκυμοσύνη και μια
          γυναικολογική φροντίδα με ασφάλεια, τεκμηρίωση και ανθρώπινη παρουσία.</p>
        <div class="hero-actions reveal">
          <a href="tel:+30{SITE['mobile']}" class="btn btn-primary">Κλείστε Ραντεβού</a>
          <a href="#services" class="btn btn-ghost">Οι Υπηρεσίες μας</a>
        </div>
      </div>
      <div class="hero-scroll" aria-hidden="true"><span></span></div>
    </section>

    <div class="strip" aria-hidden="true">
      <div class="strip-track">{strip}</div>
    </div>

    <section class="about" id="about">
      <div class="container about-grid">
        <div class="about-media reveal">
          <img src="{rel(cur, 'assets/dr-rotas.jpg')}" alt="{attr(SITE['full'])} — {attr(SITE['role'])}" width="703" height="730" />
          <div class="about-badge">
            <span class="about-badge-num">FACOG</span>
            <span class="about-badge-label">American College of<br />Obstetricians &amp; Gynecologists</span>
          </div>
        </div>
        <div class="about-copy">
          <p class="eyebrow reveal">Ο Ιατρός</p>
          <h2 class="section-title reveal">Γιατί είναι ο κατάλληλος <em>για εσένα</em></h2>
          <p class="about-role reveal">{esc(SITE['role'])} · {esc(SITE['role2'])}</p>
          <ul class="about-creds reveal">{creds_li}</ul>
          <a href="{rel(cur, 'iatros/viografiko.html')}" class="btn btn-ghost reveal">Το πλήρες βιογραφικό →</a>
        </div>
      </div>
    </section>

    <section class="stats">
      <div class="container">
        <div class="stats-grid reveal">{stats_html}</div>
      </div>
    </section>

    <section class="services" id="services">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">Υπηρεσίες</p>
          <h2 class="section-title">Ολοκληρωμένη φροντίδα,<br />σε κάθε φάση της ζωής σου</h2>
          <p>Από τον προγεννητικό έλεγχο και την παρακολούθηση της εγκυμοσύνης, έως τη γυναικολογική
            χειρουργική και την υποβοηθούμενη αναπαραγωγή.</p>
        </div>
        <div class="services-grid">
{chr(10).join(svc_cards)}
        </div>
      </div>
    </section>

    <section class="process">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">Η προσέγγισή μας</p>
          <h2 class="section-title">Τέσσερα καθαρά βήματα</h2>
        </div>
        <div class="steps">{steps_html}</div>
      </div>
    </section>

    <section class="creds">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">Τίτλοι &amp; Διακρίσεις</p>
          <h2 class="section-title">Διεθνής εκπαίδευση,<br />πιστοποιημένη εξειδίκευση</h2>
        </div>
        <div class="creds-grid reveal">{creds_grid}</div>
      </div>
    </section>

    <section class="quotes">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">Είπαν για εμάς</p>
          <h2 class="section-title">Αξιολογήσεις ασθενών</h2>
        </div>
        <div class="quotes-grid">{quotes}</div>
        <p class="quotes-note">100% αξιόπιστες αξιολογήσεις — από 472 αξιολογήσεις στο Doctoranytime.</p>
      </div>
    </section>

    <section class="clinics">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">Τα Ιατρεία</p>
          <h2 class="section-title">Δύο άρτια εξοπλισμένοι χώροι</h2>
          <p>Στα ιατρεία στη Νέα Σμύρνη και στη Βασ. Σοφίας παρέχεται όλη η γκάμα γυναικολογικών και
            μαιευτικών εξετάσεων.</p>
        </div>
        <div class="clinics-grid">
{clinic_cards}
        </div>
      </div>
    </section>
  </main>"""

    desc = ("Ρώτας Μιχάλης MD, FACOG — Μαιευτήρας Χειρουργός Γυναικολόγος, Ειδικός Εμβρυομητρικής "
            "Ιατρικής. Ιατρεία σε Αθήνα (Βασ. Σοφίας 124Α) και Νέα Σμύρνη. Εγκυμοσύνη, "
            "προγεννητικός έλεγχος, γυναικολογία, λαπαροσκόπηση, υπογονιμότητα.")
    write(cur, shell(cur, "Γυναικολόγος Αθήνα | Ρώτας Μιχάλης MD, FACOG — Μαιευτήρας Γυναικολόγος",
                     desc, body,
                     keywords="γυναικολόγος Αθήνα, μαιευτήρας Αθήνα, γυναικολόγος Νέα Σμύρνη, "
                              "εμβρυομητρική, αυχενική διαφάνεια, υπερηχογράφημα β επιπέδου, "
                              "λαπαροσκόπηση, υπογονιμότητα, Ρώτας Μιχάλης"))


# ---------------------------------------------------------------- aside

def aside_html(cur, page):
    """Sibling navigation + booking card for inner pages."""
    sec = page.section
    hub = ALL[sec["dir"] + "/index.html"]

    # Which list of siblings is most useful? Prefer the page's own children,
    # else its siblings under the same parent.
    if page.children:
        head, group = "Σε αυτή την ενότητα", page.children
    elif page.parent and page.parent is not hub:
        head, group = page.parent.title, [page.parent] + page.parent.children
    else:
        head, group = sec["title"], hub.children

    links = "".join(
        f'<a href="{rel(cur, p.path)}"'
        + (' aria-current="page"' if p.path == page.path else "")
        + f">{esc(p.nav_title)}</a>"
        for p in group if p.path != page.path or True
    )
    a, b = SITE["clinics"]
    return f"""      <aside class="svc-aside">
        <div class="aside-card">
          <h3>Κλείστε ραντεβού</h3>
          <p>Ο ιατρός δέχεται κατόπιν ραντεβού στα ιατρεία Αθήνας και Νέας Σμύρνης.</p>
          <a href="tel:+30{SITE['mobile']}" class="btn btn-primary btn-block">{SITE['mobile_fmt']}</a>
          <a href="{rel(cur, 'epikoinonia.html')}" class="btn btn-ghost btn-block">Επικοινωνία</a>
          <p class="aside-meta"><strong>{esc(a['name'])}</strong><br />{esc(a['addr'])}, {esc(a['city'])}<br />Τηλ. {a['tel_fmt']}</p>
          <p class="aside-meta"><strong>{esc(b['name'])}</strong><br />{esc(b['addr'])}, {esc(b['city'])}<br />Τηλ. {b['tel_fmt']}</p>
        </div>
        <div class="aside-card">
          <h3>{esc(head)}</h3>
          <nav class="aside-links" aria-label="Σχετικές σελίδες">{links}</nav>
          <p style="margin:1rem 0 0"><a href="{rel(cur, hub.path)}" class="svc-more">Όλα · {esc(sec['title'])} →</a></p>
        </div>
      </aside>"""


def trail_of(page):
    trail = []
    node = page
    while node is not None:
        trail.append((node.title, node.path))
        node = node.parent
    hub = ALL[page.section["dir"] + "/index.html"]
    if not trail or trail[-1][1] != hub.path:
        trail.append((hub.title, hub.path))
    return list(reversed(trail))


# ---------------------------------------------------------------- hub pages

def sub_label(n):
    if n == 0:
        return "Μάθετε περισσότερα"
    if n == 1:
        return "Δείτε την υποενότητα"
    return f"Δείτε τις {n} υποενότητες"


def render_hub(sec):
    hub = ALL[sec["dir"] + "/index.html"]
    cur = hub.path
    cards = []
    for i, c in enumerate(hub.children, 1):
        sub = ""
        if c.children:
            sub = " · ".join(g.nav_title for g in c.children)
            if len(sub) > 120:
                sub = sub[:117].rsplit(" ", 1)[0] + "…"
        teaser = excerpt(c.src, sub or f"Διαβάστε περισσότερα για {c.title.lower()}.")
        cards.append(f"""        <a class="svc reveal" href="{rel(cur, c.path)}">
          <span class="svc-num">{i:02d}</span>
          <h3>{esc(c.nav_title)}</h3>
          <p>{esc(teaser)}</p>
          <span class="svc-more">{sub_label(len(c.children))} →</span>
        </a>""")

    crumb_html, crumb_ld = crumbs(cur, [(sec["title"], cur)])
    body, _ = render_body(sec.get("src"), sec["title"])
    if body:
        intro = f"""
    <section class="svc-detail">
      <div class="container">
        <div class="svc-body">
        {body}
        </div>
      </div>
    </section>"""
    elif sec["dir"] == "iatros":
        creds_li = "".join(f"<li>{esc(c)}</li>" for c in HOME_CREDS)
        stats_html = "".join(
            f'<div class="stat"><span class="stat-n" data-count="{n}" data-suffix="{sf}">0</span>'
            f'<span class="stat-l">{esc(l)}</span></div>'
            for n, sf, l in STATS
        )
        intro = f"""
    <section class="about">
      <div class="container about-grid">
        <div class="about-media reveal">
          <img src="{rel(cur, 'assets/dr-rotas.jpg')}" alt="{attr(SITE['full'])}" width="703" height="730" loading="lazy" />
          <div class="about-badge">
            <span class="about-badge-num">FACOG</span>
            <span class="about-badge-label">American College of<br />Obstetricians &amp; Gynecologists</span>
          </div>
        </div>
        <div class="about-copy">
          <p class="eyebrow reveal">Βιογραφικό</p>
          <h2 class="section-title reveal">{esc(SITE['full'])}</h2>
          <p class="about-role reveal">{esc(SITE['role'])} · {esc(SITE['role2'])}</p>
          <ul class="about-creds reveal">{creds_li}</ul>
          <a href="{rel(cur, 'iatros/viografiko.html')}" class="btn btn-ghost reveal">Το πλήρες βιογραφικό →</a>
        </div>
      </div>
    </section>

    <section class="stats">
      <div class="container">
        <div class="stats-grid reveal">{stats_html}</div>
      </div>
    </section>"""
    else:
        intro = ""

    page_body = f"""  <main id="main">
{crumb_html}
    <section class="page-hero" data-mark="{sec['icon']}">
      <div class="container">
        <span class="svc-hero-icon" aria-hidden="true">{sec['icon']}</span>
        <p class="eyebrow">{esc(sec['eyebrow'])}</p>
        <h1 class="page-title">{esc(sec['title'])}</h1>
        <p class="page-lead">{esc(sec['lead'])}</p>
      </div>
    </section>
{intro}
    <section class="services services--hub">
      <div class="container">
        <div class="services-grid">
{chr(10).join(cards)}
        </div>
      </div>
    </section>
  </main>"""

    title = f"{sec['title']} | {SITE['full']} — Γυναικολόγος Αθήνα"
    write(cur, shell(cur, title, sec["lead"][:295], page_body, extra_ld=crumb_ld))


# ---------------------------------------------------------------- detail pages

# Pages whose body is thin on the source site but for which the site states the
# information elsewhere (homepage / hero). Injected after the scraped body.
def creds_block():
    rows = "".join(
        f'<div class="cred"><span class="cred-k">{k}</span><span class="cred-v">{v}</span></div>'
        for k, v in CREDS
    )
    extra = "".join(f"<li>{esc(c)}</li>" for c in HOME_CREDS)
    return (f'<h2>Τίτλοι &amp; πιστοποιήσεις</h2><div class="creds-grid">{rows}</div>'
            f'<h2>Εκπαίδευση &amp; καριέρα</h2><ul class="ticks">{extra}</ul>')


INJECT = {"iatros/akadimaikoi-titloi.html": creds_block}


def render_detail(page):
    cur = page.path
    sec = page.section
    body, words = render_body(page.src, page.title)

    if page.path in INJECT:
        body = (body + "\n        " if body else "") + INJECT[page.path]()
        words += 200

    if page.children:
        kid_cards = "".join(f"""        <a class="svc reveal" href="{rel(cur, k.path)}">
          <h3>{esc(k.nav_title)}</h3>
          <p>{esc(excerpt(k.src, 'Διαβάστε περισσότερα.'))}</p>
          <span class="svc-more">Μάθετε περισσότερα →</span>
        </a>""" for k in page.children)
        kids = f"""
    <section class="services services--hub">
      <div class="container">
        <div class="section-head reveal">
          <p class="eyebrow">{esc(sec['title'])}</p>
          <h2 class="section-title">{esc(page.title)}</h2>
        </div>
        <div class="services-grid">
{kid_cards}
        </div>
      </div>
    </section>"""
    else:
        kids = ""

    if words < 25:
        notice = ('<div class="notice"><strong>Η σελίδα ενημερώνεται.</strong> Το αναλυτικό '
                  'περιεχόμενο για την ενότητα αυτή βρίσκεται υπό επιμέλεια. Για πληροφορίες '
                  f'επικοινωνήστε με το ιατρείο στο <a href="tel:+30{SITE["mobile"]}">'
                  f'{SITE["mobile_fmt"]}</a>.</div>')
        body = (body + "\n        " if body else "") + notice

    trail = trail_of(page)
    crumb_html, crumb_ld = crumbs(cur, trail)

    lead = excerpt(page.src, sec["lead"])
    if len(lead) > 190:
        lead = lead[:187].rsplit(" ", 1)[0] + "…"
    page_body = f"""  <main id="main">
{crumb_html}
    <section class="page-hero" data-mark="{sec['icon']}">
      <div class="container">
        <p class="eyebrow">{esc(sec['title'])}</p>
        <h1 class="page-title">{esc(page.title)}</h1>
        <p class="page-lead">{esc(lead)}</p>
      </div>
    </section>

    <section class="svc-detail">
      <div class="container svc-detail-grid">
        <article class="svc-body">
        {body}
        </article>
{aside_html(cur, page)}
      </div>
    </section>
{kids}
  </main>"""

    title = f"{page.title} | {sec['title']} — {SITE['name']}"
    if len(title) > 68:
        title = f"{page.title} | {SITE['name']}"
    write(cur, shell(cur, title, lead[:295], page_body, extra_ld=crumb_ld))


# ---------------------------------------------------------------- clinic pages

CLINIC_GALLERY = {
    "iatros/iatreio-athinon.html": ["clinic-1.jpg", "clinic-2.jpg", "clinic-3.jpg", "clinic-4.jpg"],
    "iatros/iatreio-neas-smyrnis.html": ["clinic-5.jpg", "clinic-6.jpg", "clinic-7.jpg", "clinic-8.jpg"],
}


def render_clinic(page, clinic):
    cur = page.path
    sec = page.section
    trail = trail_of(page)
    crumb_html, crumb_ld = crumbs(cur, trail)
    gallery = "".join(
        f'<img src="{rel(cur, "assets/" + g)}" alt="{attr(clinic["name"])} — χώρος {i}" '
        f'width="632" height="412" loading="lazy" />'
        for i, g in enumerate(CLINIC_GALLERY.get(cur, []), 1)
    )
    svc = "".join(f"<li>{esc(s)}</li>" for s in IATREIO_SERVICES)

    page_body = f"""  <main id="main">
{crumb_html}
    <section class="page-hero" data-mark="◆">
      <div class="container">
        <p class="eyebrow">Οι χώροι μας</p>
        <h1 class="page-title">{esc(clinic['name'])}</h1>
        <p class="page-lead">{esc(clinic['brand'])} — {esc(clinic['addr'])}, {esc(clinic['city'])}, Τ.Κ. {clinic['zip']}.
          Άρτια εξοπλισμένος χώρος με σύγχρονα υπερηχογραφικά συστήματα για όλη τη γκάμα
          μαιευτικών και γυναικολογικών εξετάσεων.</p>
        <div class="hero-actions">
          <a href="tel:+30{clinic['tel']}" class="btn btn-primary">Καλέστε {clinic['tel_fmt']}</a>
          <a href="{clinic['map']}" target="_blank" rel="noopener noreferrer" class="btn btn-ghost">Οδηγίες στον χάρτη</a>
        </div>
      </div>
    </section>

    <section class="svc-detail">
      <div class="container svc-detail-grid">
        <article class="svc-body">
          <h2>Ο χώρος</h2>
          <div class="gallery">{gallery}</div>
          <h2>Εξετάσεις που πραγματοποιούνται</h2>
          <ul class="ticks two-col">{svc}</ul>
          <h2>Στοιχεία &amp; πρόσβαση</h2>
          <p>{esc(clinic['addr'])}, {esc(clinic['city'])}, Τ.Κ. {clinic['zip']}.
            Τηλέφωνο ιατρείου {clinic['tel_fmt']}, κινητό {SITE['mobile_fmt']},
            e-mail {SITE['email']}. Ο ιατρός δέχεται κατόπιν ραντεβού.</p>
          <div class="contact-map" style="margin-top:1.4rem">
            <iframe title="Χάρτης — {attr(clinic['name'])}" src="{clinic['embed']}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
          </div>
        </article>
{aside_html(cur, page)}
      </div>
    </section>
  </main>"""

    title = f"{clinic['name']} — {SITE['name']}"
    desc = (f"{clinic['name']}: {clinic['addr']}, {clinic['city']}, Τ.Κ. {clinic['zip']}. "
            f"Τηλ. {clinic['tel_fmt']}. Μαιευτικές και γυναικολογικές εξετάσεις κατόπιν ραντεβού.")
    write(cur, shell(cur, title, desc, page_body, extra_ld=crumb_ld))


# ---------------------------------------------------------------- contact

def render_contact():
    cur = "epikoinonia.html"
    crumb_html, crumb_ld = crumbs(cur, [("Επικοινωνία", cur)])
    cards = []
    for c in SITE["clinics"]:
        cards.append(f"""      <div>
        <h2 class="section-title" style="font-size:2rem">{esc(c['name'])}</h2>
        <ul class="contact-list">
          <li><span class="contact-label">Διεύθυνση</span><span class="contact-value">{esc(c['brand'])}<br />{esc(c['addr'])}<br />{esc(c['city'])}, Τ.Κ. {c['zip']}</span></li>
          <li><span class="contact-label">Τηλέφωνο</span><span class="contact-value"><a href="tel:+30{c['tel']}">{c['tel_fmt']}</a></span></li>
          <li><span class="contact-label">Κινητό</span><span class="contact-value"><a href="tel:+30{SITE['mobile']}">{SITE['mobile_fmt']}</a></span></li>
          <li><span class="contact-label">E-mail</span><span class="contact-value"><a href="mailto:{SITE['email']}">{SITE['email']}</a></span></li>
          <li><span class="contact-label">Ραντεβού</span><span class="contact-value"><em>Ο ιατρός δέχεται κατόπιν ραντεβού.</em></span></li>
        </ul>
        <div class="contact-actions">
          <a href="tel:+30{c['tel']}" class="btn btn-primary">Καλέστε το ιατρείο</a>
          <a href="{c['map']}" target="_blank" rel="noopener noreferrer" class="btn btn-ghost">Χάρτης</a>
        </div>
      </div>
      <div class="contact-map">
        <iframe title="Χάρτης — {attr(c['name'])}" src="{c['embed']}" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
      </div>""")

    social = "".join(
        f'<a href="{u}" target="_blank" rel="noopener noreferrer" class="btn btn-ghost">{n}</a>'
        for n, u in SITE["social"]
    )

    page_body = f"""  <main id="main">
{crumb_html}
    <section class="page-hero" data-mark="✉">
      <div class="container">
        <p class="eyebrow">Επικοινωνία</p>
        <h1 class="page-title">Κλείστε το ραντεβού σας</h1>
        <p class="page-lead">Εδώ για εσάς, με βασική μας αξία να λύσουμε οποιαδήποτε απορία
          σχετικά με την υγεία σας. Δύο ιατρεία — στη Λεωφόρο Βασιλίσσης Σοφίας και στην κεντρική
          πλατεία Νέας Σμύρνης.</p>
      </div>
    </section>

    <section class="contact">
      <div class="container contact-grid">
{chr(10).join(cards)}
      </div>
      <div class="container" style="margin-top:3rem">
        <p class="eyebrow">Ακολουθήστε μας</p>
        <div class="contact-actions">{social}</div>
      </div>
    </section>
  </main>"""

    desc = ("Επικοινωνία με τον Ρώτα Μιχάλη MD, FACOG. Ιατρείο Αθήνας: Βασ. Σοφίας 124Α, "
            "τηλ. 210 771 7705. Ιατρείο Νέας Σμύρνης: 25ης Μαρτίου 11, τηλ. 210 934 3538.")
    write(cur, shell(cur, f"Επικοινωνία — {SITE['full']} | Γυναικολόγος Αθήνα & Νέα Σμύρνη",
                     desc, page_body, extra_ld=crumb_ld))


# ---------------------------------------------------------------- sitemap

def render_meta():
    urls = ["index.html", "epikoinonia.html"] + sorted(ALL.keys())
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemap.org/schemas/sitemap/0.9">'.replace("sitemap.org", "sitemaps.org")]
    for u in urls:
        loc = SITE["domain"] + "/" + ("" if u == "index.html" else u)
        pri = "1.0" if u == "index.html" else ("0.8" if u.endswith("/index.html") else "0.6")
        xml.append(f"  <url><loc>{loc}</loc><lastmod>{TODAY}</lastmod>"
                   f"<changefreq>monthly</changefreq><priority>{pri}</priority></url>")
    xml.append("</urlset>")
    write("sitemap.xml", "\n".join(xml) + "\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE['domain']}/sitemap.xml\n")


# ---------------------------------------------------------------- main

def main():
    render_home()
    render_contact()
    for sec in SECTIONS:
        render_hub(sec)
    clinic_pages = {
        "iatros/iatreio-athinon.html": SITE["clinics"][0],
        "iatros/iatreio-neas-smyrnis.html": SITE["clinics"][1],
    }
    n = 0
    for path, page in ALL.items():
        if path.endswith("/index.html"):
            continue
        if path in clinic_pages:
            render_clinic(page, clinic_pages[path])
        else:
            render_detail(page)
        n += 1
    render_meta()
    print(f"✓ {n} detail pages + {len(SECTIONS)} hubs + home + contact")


if __name__ == "__main__":
    main()

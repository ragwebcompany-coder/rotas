# -*- coding: utf-8 -*-
"""GR → EN page map for the English mirror of gynaicologos.gr.

Every Greek page produced by _build/build.py has exactly one English
counterpart under en/.  Where the old WordPress English site already had a
page on the same topic we keep its filename, so those URLs keep working.

`OLD_EN` points at the page of the *previous* English site that carries the
original English wording for that topic (the Greek text was translated from
it).  build_en.py harvests those sentences automatically; anything it cannot
match falls through to the hand-written dictionaries in strings/.
"""

# Section directories: greek dir -> english dir
DIRS = {
    "iatros": "doctor",
    "maieftiki": "pregnancy",        # kept: preserves old /en/pregnancy/* URLs
    "embryomitriki": "fetal-medicine",
    "gynaikologia": "gynecology",    # kept: preserves old /en/gynecology/* URLs
    "xeirourgeia": "surgery",
    "ypogonimotita": "infertility",
}

# greek path -> (english path, old-english source page or None)
PAGES = {
    # ---------------------------------------------------------------- root
    "index.html":        ("en/index.html",   "en/index.html"),
    "iatreia.html":      ("en/clinics.html", None),
    "epikoinonia.html":  ("en/contact.html", "en/contact.html"),

    # ---------------------------------------------------------------- iatros
    "iatros/index.html":                ("en/doctor/index.html", "en/doctor.html"),
    "iatros/viografiko.html":           ("en/doctor/cv.html", "en/doctor.html"),
    "iatros/akadimaikoi-titloi.html":   ("en/doctor/academic-qualifications.html", None),
    "iatros/dimosieuseis.html":         ("en/doctor/publications.html", None),
    "iatros/i-omada-mas.html":          ("en/doctor/our-team.html", None),
    "iatros/i-maia-mas.html":           ("en/doctor/our-midwife.html", None),
    "iatros/embryokardiologos.html":    ("en/doctor/fetal-cardiologist.html", None),
    "iatros/oi-xoroi-mas.html":         ("en/doctor/our-facilities.html", None),
    "iatros/iatreio-athinon.html":      ("en/doctor/athens-clinic.html", None),
    "iatros/iatreio-neas-smyrnis.html": ("en/doctor/nea-smyrni-clinic.html", None),

    # ---------------------------------------------------------------- maieftiki
    "maieftiki/index.html":                  ("en/pregnancy/index.html", "en/pregnancy/index.html"),
    "maieftiki/poreia-egkymosynis.html":     ("en/pregnancy/course-of-pregnancy.html", None),
    "maieftiki/progennitikos-elegxos.html":  ("en/pregnancy/prenatal-testing.html", None),
    "maieftiki/genikes-exetaseis.html":      ("en/pregnancy/routine-tests.html", "en/pregnancy/routine-tests.html"),
    "maieftiki/kystiki-inosi.html":          ("en/pregnancy/cystic-fibrosis.html", "en/pregnancy/cystic-fibrosis.html"),
    "maieftiki/genetikes-diataraxes.html":   ("en/pregnancy/genetic-disorders.html", "en/pregnancy/genetic-disorders.html"),
    "maieftiki/paragontas-rhesus.html":      ("en/pregnancy/rhesus-factor.html", "en/pregnancy/rhesus-factor.html"),
    "maieftiki/streptokokkos-omadas-b.html": ("en/pregnancy/group-b-streptococcus.html", "en/pregnancy/group-b-streptococcus.html"),
    "maieftiki/thrombofilies-kyisis.html":   ("en/pregnancy/thrombophilia.html", None),
    "maieftiki/themata-stin-egkymosyni.html":("en/pregnancy/pregnancy-topics.html", None),
    "maieftiki/proini-adiathesia.html":      ("en/pregnancy/nausea.html", "en/pregnancy/nausea.html"),
    "maieftiki/diatrofi-stin-egkymosyni.html":("en/pregnancy/nutrition.html", "en/pregnancy/nutrition.html"),
    "maieftiki/athlisi-stin-egkymosyni.html":("en/pregnancy/exercise.html", "en/pregnancy/exercise.html"),
    "maieftiki/pathologia-tis-kyisis.html":  ("en/pregnancy/pregnancy-complications.html", None),
    "maieftiki/aimorragia-stin-egkymosyni.html":("en/pregnancy/bleeding.html", "en/pregnancy/bleeding.html"),
    "maieftiki/epanalambanomenes-apovoles.html":("en/pregnancy/recurrent-miscarriage.html", None),
    "maieftiki/ektopi-kyisi.html":           ("en/pregnancy/ectopic-pregnancy.html", None),
    "maieftiki/diavitis-kyisis.html":        ("en/pregnancy/gestational-diabetes.html", "en/pregnancy/gestational-diabetes.html"),
    "maieftiki/proeklampsia.html":           ("en/pregnancy/preeclampsia.html", None),
    "maieftiki/proeklampsia-thrombofilia.html":("en/pregnancy/preeclampsia-thrombophilia.html", None),
    "maieftiki/epilipsia-kai-egkymosyni.html":("en/pregnancy/epilepsy.html", None),
    "maieftiki/dermatikes-pathiseis-egkymosynis.html":("en/pregnancy/skin-conditions.html", None),
    "maieftiki/didymi-kyisi.html":           ("en/pregnancy/twins.html", "en/pregnancy/twins.html"),
    "maieftiki/isxiaki-provoli.html":        ("en/pregnancy/breech.html", "en/pregnancy/breech.html"),
    "maieftiki/fysiologikos-toketos-meta-kaisariki.html":("en/pregnancy/vbac.html", "en/pregnancy/vbac.html"),
    "maieftiki/loxeia-kai-thilasmos.html":   ("en/pregnancy/postpartum-and-breastfeeding.html", "en/pregnancy/breastfeeding.html"),

    # ---------------------------------------------------------------- embryomitriki
    "embryomitriki/index.html":                       ("en/fetal-medicine/index.html", None),
    "embryomitriki/ypirixografima-arxomenis-kyisis.html":("en/fetal-medicine/early-pregnancy-scan.html", None),
    "embryomitriki/auxeniki-diafaneia.html":          ("en/fetal-medicine/nuchal-translucency.html", None),
    "embryomitriki/ypirixografima-b-epipedou.html":   ("en/fetal-medicine/anomaly-scan.html", None),
    "embryomitriki/ypirixografima-kardias-embryou.html":("en/fetal-medicine/fetal-echocardiography.html", None),
    "embryomitriki/ypirixografima-3d-4d.html":        ("en/fetal-medicine/3d-4d-ultrasound.html", None),
    "embryomitriki/ypirixografima-anaptyxis-embryou.html":("en/fetal-medicine/fetal-growth-scan.html", None),
    "embryomitriki/ypirixografima-doppler.html":      ("en/fetal-medicine/doppler-ultrasound.html", None),
    "embryomitriki/viopsia-trofovlastis.html":        ("en/fetal-medicine/chorionic-villus-sampling.html", None),
    "embryomitriki/amnioparakentisi.html":            ("en/fetal-medicine/amniocentesis.html", None),
    "embryomitriki/nipt.html":                        ("en/fetal-medicine/nipt.html", None),
    "embryomitriki/exetaseis-ygeias-embryou.html":    ("en/fetal-medicine/fetal-wellbeing-tests.html", None),
    "embryomitriki/genetikes-diataraxes.html":        ("en/fetal-medicine/genetic-disorders.html", "en/pregnancy/genetic-disorders.html"),

    # ---------------------------------------------------------------- gynaikologia
    "gynaikologia/index.html":                    ("en/gynecology/index.html", "en/gynecology/index.html"),
    "gynaikologia/gynaikologiki-exetasi.html":    ("en/gynecology/gynecological-examination.html", None),
    "gynaikologia/gynaikologiko-ypirixografima.html":("en/gynecology/ultrasound-exams.html", "en/gynecology/ultrasound-exams.html"),
    "gynaikologia/test-pap.html":                 ("en/gynecology/pap-test.html", "en/gynecology/pap-test.html"),
    "gynaikologia/exetasi-traxilou-mitras.html":  ("en/gynecology/cervical-screening.html", None),
    "gynaikologia/kolposkopisi.html":             ("en/gynecology/colposcopy.html", "en/gynecology/colposcopy.html"),
    "gynaikologia/kalliergeia-kolpikou-ygrou.html":("en/gynecology/vaginal-culture.html", None),
    "gynaikologia/gynaikologika-themata.html":    ("en/gynecology/gynecological-conditions.html", None),
    "gynaikologia/inomyomata.html":               ("en/gynecology/fibroids.html", "en/gynecology/fibroids.html"),
    "gynaikologia/endomitriosi.html":             ("en/gynecology/endometriosis.html", "en/gynecology/endometriosis.html"),
    "gynaikologia/mi-fysiologiki-aimorragia-mitras.html":("en/gynecology/au-bleeding.html", "en/gynecology/au-bleeding.html"),
    "gynaikologia/ios-hpv.html":                  ("en/gynecology/hpv.html", "en/gynecology/hpv.html"),
    "gynaikologia/dysminorroia.html":             ("en/gynecology/dysmenorrhea.html", "en/gynecology/dysmenorrhea.html"),
    "gynaikologia/kysteis-oothikon.html":         ("en/gynecology/ovarian-cyst.html", "en/gynecology/ovarian-cyst.html"),
    "gynaikologia/kolpitides.html":               ("en/gynecology/vaginitis.html", "en/gynecology/vaginitis.html"),
    "gynaikologia/polykystikes-oothikes.html":    ("en/gynecology/pcos.html", None),
    "gynaikologia/akrateia-ouron.html":           ("en/gynecology/urinary-incontinence.html", "en/gynecology/urinary-incontinence.html"),
    "gynaikologia/provlimata-pyelikis-stirixis.html":("en/gynecology/pelvic-prolapse.html", "en/gynecology/pelvic-prolapse.html"),
    "gynaikologia/klimaktirios-emminopafsi.html": ("en/gynecology/menopause.html", None),
    "gynaikologia/thromvofilies.html":            ("en/gynecology/thrombophilia.html", None),
    "gynaikologia/isxiaki-provoli.html":          ("en/gynecology/breech.html", "en/pregnancy/breech.html"),
    "gynaikologia/epemvaseis-sto-iatreio.html":   ("en/gynecology/office-procedures.html", None),
    "gynaikologia/topothetisi-spiral.html":       ("en/gynecology/iud.html", "en/gynecology/iud.html"),
    "gynaikologia/endomitria-spermategxysi.html": ("en/gynecology/intrauterine-insemination.html", None),
    "gynaikologia/viopsia-endomitriou.html":      ("en/gynecology/endometrial-biopsy.html", None),
    "gynaikologia/kaftiriasmos-kondylomaton.html":("en/gynecology/genital-warts-laser.html", None),

    # ---------------------------------------------------------------- xeirourgeia
    "xeirourgeia/index.html":                       ("en/surgery/index.html", None),
    "xeirourgeia/proetoimasia-xeirourgeiou.html":   ("en/surgery/preparing-for-surgery.html", None),
    "xeirourgeia/ysteroskopisi.html":               ("en/surgery/hysteroscopy.html", "en/gynecology/hysteroscopy.html"),
    "xeirourgeia/ysteroskopiki-afairesi-polypoda.html":("en/surgery/hysteroscopic-polypectomy.html", None),
    "xeirourgeia/ysteroskopiki-afairesi-inomyomatos.html":("en/surgery/hysteroscopic-myomectomy.html", None),
    "xeirourgeia/ysteroskopiki-afairesi-diafragmatos.html":("en/surgery/hysteroscopic-septum-resection.html", None),
    "xeirourgeia/laparoskopisi.html":               ("en/surgery/laparoscopy.html", "en/gynecology/laparoscopy.html"),
    "xeirourgeia/laparoskopiki-afairesi-kystis.html":("en/surgery/laparoscopic-cystectomy.html", None),
    "xeirourgeia/laparoskopiki-inomyomatektomi.html":("en/surgery/laparoscopic-myomectomy.html", None),
    "xeirourgeia/laparoskopisi-endomitriosis.html": ("en/surgery/laparoscopy-for-endometriosis.html", None),
    "xeirourgeia/laparoskopiki-ysterektomi.html":   ("en/surgery/laparoscopic-hysterectomy.html", None),
    "xeirourgeia/ysterektomi.html":                 ("en/surgery/hysterectomy.html", "en/gynecology/hysterectomy.html"),
    "xeirourgeia/konoeidis-ektomi-traxilou.html":   ("en/surgery/cone-biopsy.html", "en/gynecology/leep.html"),
    "xeirourgeia/ourogynaikologia.html":            ("en/surgery/urogynecology.html", None),
    "xeirourgeia/tainia-akrateias-ouron.html":      ("en/surgery/incontinence-sling.html", "en/gynecology/stress-incontinence-surgery.html"),

    # ---------------------------------------------------------------- ypogonimotita
    "ypogonimotita/index.html":                     ("en/infertility/index.html", None),
    "ypogonimotita/symvouleftiki-gonimotitas.html": ("en/infertility/fertility-counselling.html", None),
    "ypogonimotita/axiologisi-ypogonimotitas.html": ("en/infertility/fertility-assessment.html", None),
    "ypogonimotita/diereynisi.html":                ("en/infertility/investigation.html", None),
    "ypogonimotita/diereynisi-gynaikas.html":       ("en/infertility/female-investigation.html", None),
    "ypogonimotita/ormonikos-elegxos-gynaikas.html":("en/infertility/female-hormone-testing.html", None),
    "ypogonimotita/salpiggografia-hycosy.html":     ("en/infertility/hsg-and-hycosy.html", None),
    "ypogonimotita/ypodektikotita-endomitriou.html":("en/infertility/endometrial-receptivity.html", None),
    "ypogonimotita/xronia-endomitritida.html":      ("en/infertility/chronic-endometritis.html", None),
    "ypogonimotita/diereynisi-andra.html":          ("en/infertility/male-investigation.html", None),
    "ypogonimotita/ormonikos-elegxos-andra.html":   ("en/infertility/male-hormone-testing.html", None),
    "ypogonimotita/spermodiagramma.html":           ("en/infertility/semen-analysis.html", None),
    "ypogonimotita/eidikes-exetaseis-spermatos.html":("en/infertility/advanced-sperm-tests.html", None),
    "ypogonimotita/therapeies-ypogonimotitas.html": ("en/infertility/treatments.html", None),
    "ypogonimotita/proklisi-oothylakiorrixias.html":("en/infertility/ovulation-induction.html", None),
    "ypogonimotita/spermategxysi-iui.html":         ("en/infertility/iui.html", None),
    "ypogonimotita/exosomatiki-gonimopoiisi.html":  ("en/infertility/ivf.html", None),
    "ypogonimotita/therapeies-exosomatikis.html":   ("en/infertility/ivf-treatments.html", None),
    "ypogonimotita/fysikos-kyklos.html":            ("en/infertility/natural-cycle-ivf.html", None),
    "ypogonimotita/mini-ivf.html":                  ("en/infertility/mini-ivf.html", None),
    "ypogonimotita/dorea-oarion.html":              ("en/infertility/egg-donation.html", None),
    "ypogonimotita/doti-spermatos.html":            ("en/infertility/sperm-donation.html", None),
    "ypogonimotita/katapsyxi-oarion.html":          ("en/infertility/egg-freezing.html", None),
    "ypogonimotita/parentheti-mitrotita.html":      ("en/infertility/surrogacy.html", None),
    "ypogonimotita/anazoogonisi-oothikon-prp.html": ("en/infertility/ovarian-rejuvenation-prp.html", None),
    "ypogonimotita/neoteres-texnologies.html":      ("en/infertility/new-technologies.html", None),
    "ypogonimotita/time-lapse.html":                ("en/infertility/time-lapse.html", None),
    "ypogonimotita/ypovoithoumeni-ekkolapsi.html":  ("en/infertility/assisted-hatching.html", None),
    "ypogonimotita/proemfyteftikos-genetikos-elegxos.html":("en/infertility/pgt.html", None),
    "ypogonimotita/epanalambanomenes-apovoles.html":("en/infertility/recurrent-miscarriage.html", None),
}

# Old English URLs with no counterpart in the new site — served as redirect
# stubs so nothing that is already indexed 404s.
RETIRED = {
    "en/doctor.html":                      "en/doctor/index.html",
    "en/pregnancy/cesarean.html":          "en/pregnancy/index.html",
    "en/pregnancy/cord-blood.html":        "en/pregnancy/index.html",
    "en/pregnancy/drugs-and-alcohol.html": "en/pregnancy/pregnancy-topics.html",
    "en/pregnancy/fathers-guide.html":     "en/pregnancy/pregnancy-topics.html",
    "en/pregnancy/labor-induction.html":   "en/pregnancy/index.html",
    "en/pregnancy/pain-relief.html":       "en/pregnancy/index.html",
    "en/pregnancy/postpartum-depression.html": "en/pregnancy/postpartum-and-breastfeeding.html",
    "en/pregnancy/preterm-birth.html":     "en/pregnancy/pregnancy-complications.html",
    "en/pregnancy/travel.html":            "en/pregnancy/pregnancy-topics.html",
    "en/gynecology/chronic-pelvic-pain.html":   "en/gynecology/gynecological-conditions.html",
    "en/gynecology/emergency-contraception.html": "en/gynecology/gynecological-conditions.html",
    "en/gynecology/endometrial-ablation.html":  "en/surgery/hysteroscopy.html",
    "en/gynecology/hysterectomy.html":          "en/surgery/hysterectomy.html",
    "en/gynecology/hysterosalpingography.html": "en/infertility/hsg-and-hycosy.html",
    "en/gynecology/hysteroscopic-sterilisation.html": "en/surgery/hysteroscopy.html",
    "en/gynecology/hysteroscopy.html":          "en/surgery/hysteroscopy.html",
    "en/gynecology/laparoscopy.html":           "en/surgery/laparoscopy.html",
    "en/gynecology/leep.html":                  "en/surgery/cone-biopsy.html",
    "en/gynecology/ocps.html":                  "en/gynecology/gynecological-conditions.html",
    "en/gynecology/ovarian-cancer.html":        "en/gynecology/gynecological-conditions.html",
    "en/gynecology/pid.html":                   "en/gynecology/gynecological-conditions.html",
    "en/gynecology/pms.html":                   "en/gynecology/gynecological-conditions.html",
    "en/gynecology/sonohysterography.html":     "en/infertility/hsg-and-hycosy.html",
    "en/gynecology/stress-incontinence-surgery.html": "en/surgery/incontinence-sling.html",
    "en/gynecology/uterine-cancer.html":        "en/gynecology/gynecological-conditions.html",
}

EN_OF = {gr: en for gr, (en, _) in PAGES.items()}
GR_OF = {en: gr for gr, (en, _) in PAGES.items()}
OLD_EN = {gr: old for gr, (_, old) in PAGES.items() if old}

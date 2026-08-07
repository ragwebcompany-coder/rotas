# -*- coding: utf-8 -*-
"""Site map for gynaicologos.gr rebuild.

Each entry:  (greek_source_slug, latin_filename, nav_title, [children])
`greek_source_slug` keys into _build/content.json (extracted from the live WP site).
`None` means the page has no scraped body (hub pages) and is generated from children.
"""

SITE = {
    "name": "Δρ. Μιχάλης Ρώτας",
    "full": "Ρώτας Μιχάλης MD, FACOG",
    "role": "Μαιευτήρας – Χειρουργός Γυναικολόγος",
    "role2": "Ειδικός Εμβρυομητρικής Ιατρικής",
    "domain": "https://gynaicologos.gr",
    "email": "mrotas@gmail.com",
    "mobile": "6955199198",
    "mobile_fmt": "695 519 9198",
    "clinics": [
        {
            "id": "athina",
            "name": "Ιατρείο Αθηνών",
            "brand": "EMBRYOCOSMOS",
            "addr": "Λεωφόρος Βασιλίσσης Σοφίας 124Α",
            "city": "Αθήνα",
            "zip": "11526",
            "tel": "2107717705",
            "tel_fmt": "210 771 7705",
            "map": "https://www.google.com/maps?q=%CE%92%CE%B1%CF%83%CE%B9%CE%BB%CE%AF%CF%83%CF%83%CE%B7%CF%82+%CE%A3%CE%BF%CF%86%CE%AF%CE%B1%CF%82+124%CE%91%2C+%CE%91%CE%B8%CE%AE%CE%BD%CE%B1",
            "embed": "https://www.google.com/maps?q=%CE%92%CE%B1%CF%83%CE%B9%CE%BB%CE%AF%CF%83%CF%83%CE%B7%CF%82%20%CE%A3%CE%BF%CF%86%CE%AF%CE%B1%CF%82%20124%CE%91%2C%20%CE%91%CE%B8%CE%AE%CE%BD%CE%B1&output=embed",
        },
        {
            "id": "nea-smyrni",
            "name": "Ιατρείο Νέας Σμύρνης",
            "brand": "Κεντρική Πλατεία",
            "addr": "25ης Μαρτίου 11",
            "city": "Νέα Σμύρνη",
            "zip": "17121",
            "tel": "2109343538",
            "tel_fmt": "210 934 3538",
            "map": "https://www.google.com/maps?q=25%CE%B7%CF%82+%CE%9C%CE%B1%CF%81%CF%84%CE%AF%CE%BF%CF%85+11%2C+%CE%9D%CE%AD%CE%B1+%CE%A3%CE%BC%CF%8D%CF%81%CE%BD%CE%B7",
            "embed": "https://www.google.com/maps?q=25%CE%B7%CF%82%20%CE%9C%CE%B1%CF%81%CF%84%CE%AF%CE%BF%CF%85%2011%2C%20%CE%9D%CE%AD%CE%B1%20%CE%A3%CE%BC%CF%8D%CF%81%CE%BD%CE%B7&output=embed",
        },
    ],
    "social": [
        ("Facebook", "https://www.facebook.com/gynaicologos/?locale=el_GR"),
        ("Instagram", "https://www.instagram.com/dr_michael_rotas_md_facog_dfm/"),
        ("LinkedIn", "https://www.linkedin.com/in/michael-rotas-md-facog-47064250/"),
    ],
}

# ---------------------------------------------------------------- partners
# Συνεργαζόμενα νοσοκομεία & ιδρύματα — όπως στο παλιό gynaicologos.gr.
# (λογότυπο στο assets/partners/, όνομα, σύνδεσμος)

PARTNERS = [
    ("rea.jpg", "ΡΕΑ Μαιευτική Γυναικολογική Κλινική", "https://www.reamaternity.gr/"),
    ("iaso.jpg", "ΙΑΣΩ", "https://www.iaso.gr/"),
    ("leto.jpg", "ΛΗΤΩ", "https://www.leto.gr/"),
    ("mitera.jpg", "ΜΗΤΕΡΑ", "https://www.mitera.gr/"),
    ("kings-college.jpg", "King’s College Hospital NHS Foundation Trust", "https://www.kch.nhs.uk/"),
    ("msk.jpg", "Memorial Sloan Kettering Cancer Center", "https://www.mskcc.org/"),
    ("maine-medical.jpg", "Maine Medical Center", "https://maimo.org/"),
]

# ---------------------------------------------------------------- sections

SECTIONS = [
    {
        "dir": "iatros",
        "title": "Ο Ιατρός",
        "nav": "Ο Ιατρός",
        "eyebrow": "Σχετικά με εμάς",
        "icon": "◆",
        "lead": "Ο Δρ. Μιχάλης Ρώτας, Μαιευτήρας – Χειρουργός Γυναικολόγος και Ειδικός "
                "Εμβρυομητρικής Ιατρικής, με εκπαίδευση και κλινική εμπειρία σε κορυφαία "
                "πανεπιστημιακά νοσοκομεία των ΗΠΑ και του Ηνωμένου Βασιλείου.",
        "pages": [
            ("βιογραφικό-ιατρού", "viografiko", "Βιογραφικό ιατρού", []),
            ("ακαδημαϊκοί-τίτλοι", "akadimaikoi-titloi", "Ακαδημαϊκοί τίτλοι", []),
            ("δημοσιεύσεις", "dimosieuseis", "Δημοσιεύσεις", []),
            ("η-ομάδα-μας-page", "i-omada-mas", "Η ομάδα μας", [
                ("η-μαία-μας-page", "i-maia-mas", "Η μαία μας", []),
                ("εμβρυοκαρδιολόγος-page", "embryokardiologos", "Εμβρυοκαρδιολόγος", []),
            ]),
            ("οι-χώροι-μας-page", "oi-xoroi-mas", "Οι χώροι μας", [
                ("ιατρείο-αθηνών", "iatreio-athinon", "Ιατρείο Αθηνών", []),
                ("ιατρείο-νέας-σμύρνης", "iatreio-neas-smyrnis", "Ιατρείο Νέας Σμύρνης", []),
            ]),
        ],
    },
    {
        "dir": "maieftiki",
        "title": "Μαιευτική",
        "nav": "Μαιευτική",
        "eyebrow": "Υπηρεσίες",
        "icon": "❋",
        "src": "μαιευτική",
        "lead": "Παρακολούθηση της εγκυμοσύνης από την πρώτη στιγμή έως τον τοκετό και τη "
                "λοχεία — με επιστημονική τεκμηρίωση, σύγχρονο εξοπλισμό και ανθρώπινη παρουσία "
                "σε κάθε βήμα.",
        "pages": [
            ("η-πορεια-τησ-εγκυμοσυνησ", "poreia-egkymosynis", "Η πορεία της εγκυμοσύνης", []),
            ("προγεννητικός-έλεγχος-hub", "progennitikos-elegxos", "Προγεννητικός έλεγχος", [
                ("τεστ-ρουτίνας-στην-εγκυμοσύνη", "genikes-exetaseis", "Γενικές εξετάσεις", []),
                ("κυστική-ίνωση", "kystiki-inosi", "Κυστική Ίνωση", []),
                # Μεταφέρθηκε από την Εμβρυομητρική κατόπιν αιτήματος του ιατρού.
                ("γενετικές-διαταραχές", "genetikes-diataraxes", "Γενετικές διαταραχές", []),
                ("ο-παράγοντας-rhesus", "paragontas-rhesus", "Ο παράγοντας Rhesus", []),
                ("στρεπτόκοκκος-ομάδας-β-στην-εγκυμοσύ", "streptokokkos-omadas-b", "Στρεπτόκοκκος ομάδας Β", []),
                ("θρομβοφιλίες-στην-κύηση", "thrombofilies-kyisis", "Θρομβοφιλίες", []),
            ]),
            ("θέματα-στην-εγκυμοσύνη-hub", "themata-stin-egkymosyni", "Θέματα στην εγκυμοσύνη", [
                ("πρωινή-αδιαθεσία", "proini-adiathesia", "Πρωινή αδιαθεσία", []),
                ("διατροφή-κατά-την-εγκυμοσύνη", "diatrofi-stin-egkymosyni", "Διατροφή κατά την κύηση", []),
                ("άθληση-κατά-τη-διάρκεια-της-εγκυμοσύν-2", "athlisi-stin-egkymosyni", "Άσκηση κατά την κύηση", []),
            ]),
            ("παθολογία-της-κύησης", "pathologia-tis-kyisis", "Παθολογία της κύησης", [
                ("αιμορραγία-κατά-τη-διάρκεια-της-εγκυμ", "aimorragia-stin-egkymosyni", "Αιμορραγία κατά τη διάρκεια της κύησης", []),
                # Μεταφέρθηκε από την Υπογονιμότητα κατόπιν αιτήματος του ιατρού.
                ("επαναλαμβανόμενες-αποβολές", "epanalambanomenes-apovoles", "Επαναλαμβανόμενες αποβολές", []),
                ("έκτοπη-κύηση", "ektopi-kyisi", "Έκτοπη κύηση", []),
                ("διαβήτης-κύησης", "diavitis-kyisis", "Διαβήτης κύησης", []),
                ("υψηλή-αρτηριακή-πίεση-στην-εγκυμοσύνη", "proeklampsia", "Προεκλαμψία", []),
                ("επιληψία-και-εγκυμοσύνη", "epilipsia-kai-egkymosyni", "Επιληψία και εγκυμοσύνη", []),
                ("δερματικές-παθήσεις-της-εγκυμοσύνης", "dermatikes-pathiseis-egkymosynis", "Δερματικές παθήσεις στην κύηση", []),
            ]),
            ("δίδυμη-κύηση", "didymi-kyisi", "Δίδυμη κύηση", []),
            ("ισχιακή-προβολή", "isxiaki-provoli", "Ισχιακή προβολή", []),
            ("φυσιολογικός-τοκετός-μετά-από-καισαρ", "fysiologikos-toketos-meta-kaisariki", "Φυσιολογικός Τοκετός μετά από Καισαρική (VBAC)", []),
            ("λοχεία-και-θηλασμός", "loxeia-kai-thilasmos", "Λοχεία και θηλασμός", []),
        ],
    },
    {
        "dir": "embryomitriki",
        "title": "Εμβρυομητρική",
        "nav": "Εμβρυομητρική",
        "eyebrow": "Υπηρεσίες",
        "icon": "⬡",
        "src": "εμβρυομητρική",
        "lead": "Εμβρυομητρική Ιατρική στο ανώτερο επίπεδο πιστοποίησης (Diploma in Fetal "
                "Medicine, FMF London) — υπερηχογραφικός έλεγχος, επεμβατική διάγνωση και "
                "παρακολούθηση κύησης υψηλού κινδύνου.",
        "pages": [
            ("υπερηχογράφημα-αρχόμενης-κύησης", "ypirixografima-arxomenis-kyisis", "Υπερηχογράφημα Αρχόμενης Κύησης", []),
            ("αυχενική-διαφάνεια", "auxeniki-diafaneia", "Αυχενική Διαφάνεια", []),
            ("υπερηχογράφημα-β-επιπέδου-2", "ypirixografima-b-epipedou", "Υπερηχογράφημα Β’ επιπέδου", []),
            ("υπερηχογράφημα-καρδιάς-εμβρύου", "ypirixografima-kardias-embryou", "Υπερηχογράφημα καρδιάς εμβρύου", []),
            ("υπερηχογράφημα-3d-4d", "ypirixografima-3d-4d", "Υπερηχογράφημα 3D/4D", []),
            ("υπερηχογράφημα-ανάπτυξης-εμβρύου-2", "ypirixografima-anaptyxis-embryou", "Υπερηχογράφημα ανάπτυξης εμβρύου", []),
            ("υπερηχογράφημα-doppler", "ypirixografima-doppler", "Υπερηχογράφημα Doppler", []),
            ("βιοψία-τροφοβλάστης", "viopsia-trofovlastis", "Βιοψία Τροφοβλάστης", []),
            ("αμνιοπαρακέντηση", "amnioparakentisi", "Αμνιοπαρακέντηση", []),
            ("μη-επεμβατικός-προγεννητικός-έλεγχο", "nipt", "Μη επεμβατικός προγεννητικός έλεγχος (NIPT)", []),
            ("ειδικές-εξετάσεις-υγείας-εμβρύου", "exetaseis-ygeias-embryou", "Ειδικές εξετάσεις παρακολούθησης του εμβρύου", []),
        ],
    },
    {
        "dir": "gynaikologia",
        "title": "Γυναικολογία",
        "nav": "Γυναικολογία",
        "eyebrow": "Υπηρεσίες",
        "icon": "❈",
        "src": "γυναικολογία",
        "lead": "Ολοκληρωμένος γυναικολογικός έλεγχος, πρόληψη και αντιμετώπιση των συχνότερων "
                "γυναικολογικών παθήσεων — με σύγχρονο εξοπλισμό και εξατομικευμένο πλάνο "
                "παρακολούθησης.",
        "pages": [
            ("γυναικολογική-εξέταση-hub", "gynaikologiki-exetasi", "Γυναικολογική εξέταση", [
                ("γυναικολογικό-υπερηχογράφημα", "gynaikologiko-ypirixografima", "Γυναικολογικό Υπερηχογράφημα", []),
                ("εξέταση-τραχήλου-μήτρας-page", "exetasi-traxilou-mitras", "Εξέταση τραχήλου μήτρας", []),
                ("τεστ-παπ", "test-pap", "Τεστ ΠΑΠ", []),
                ("κολποσκόπηση", "kolposkopisi", "Κολποσκόπηση", []),
            ]),
            ("γυναικολογικά-θέματα-hub", "gynaikologika-themata", "Γυναικολογικά θέματα", [
                ("ενδομητρίωση-2", "endomitriosi", "Ενδομητρίωση", []),
                ("κολπίτιδες", "kolpitides", "Κολπίτιδες", []),
                ("ινομυώματα-3", "inomyomata", "Ινομυώματα", []),
                ("ακράτεια-ούρων", "akrateia-ouron", "Ακράτεια ούρων", []),
                ("κύστεις-των-ωοθηκών", "kysteis-oothikon", "Κύστεις των ωοθηκών", []),
                ("προβλήματα-πυελικής-στήριξης", "provlimata-pyelikis-stirixis", "Προβλήματα πυελικής στήριξης", []),
                ("ιός-hpv", "ios-hpv", "Ιός HPV", []),
                ("πολυκυστικές-ωοθήκες-2", "polykystikes-oothikes", "Πολυκυστικές ωοθήκες", []),
                ("δυσμηνόρροια-page", "dysminorroia", "Δυσμηνόρροια", []),
                ("μη-φυσιολογική-αιμορραγία-μήτρας", "mi-fysiologiki-aimorragia-mitras", "Μητρορραγία (μη φυσιολογική αιμορραγία μήτρας)", []),
                ("θρομβοφιλίες-page", "thromvofilies", "Θρομβοφιλίες", []),
                ("κλιμακτήριος-εμμηνόπαυση-page", "klimaktirios-emminopafsi", "Κλιμακτήριος – Εμμηνόπαυση", []),
                ("καλλιέργεια-κολπικού-υγρού-page", "kalliergeia-kolpikou-ygrou", "Καλλιέργεια κολπικού υγρού", []),
            ]),
            ("γυναικολογικές-επεμβάσεις-στο-ιατρείο-hub", "epemvaseis-sto-iatreio", "Γυναικολογικές Επεμβάσεις στο Ιατρείο", [
                ("ενδομήτριο-σπείραμα", "topothetisi-spiral", "Τοποθέτηση ενδομήτριου σπιράλ", []),
                ("καυτηριασμός-κονδυλωμάτων-page", "kaftiriasmos-kondylomaton", "Καυτηριασμός – λέιζερ κονδυλωμάτων", []),
                ("βιοψία-ενδομητρίου-page", "viopsia-endomitriou", "Βιοψία Ενδομητρίου", []),
                ("ενδομήτρια-σπερματέγχυση-page", "endomitria-spermategxysi", "Ενδομήτρια σπερματέγχυση", []),
            ]),
        ],
    },
    {
        "dir": "xeirourgeia",
        "title": "Χειρουργεία",
        "nav": "Χειρουργεία",
        "eyebrow": "Υπηρεσίες",
        "icon": "✚",
        "src": "χειρουργεία",
        "lead": "Ελάχιστα επεμβατική γυναικολογική χειρουργική — υστεροσκόπηση και "
                "λαπαροσκόπηση — με βράβευση από την Αμερικανική Ένωση Γυναικολογικής "
                "Λαπαροσκόπησης (AAGL).",
        "pages": [
            # Μόνη της, πάνω από όλες τις υποκατηγορίες (αίτημα ιατρού).
            ("προετοιμασία-για-χειρουργική-επέμβαση", "proetoimasia-xeirourgeiou", "Προετοιμασία για χειρουργική επέμβαση", []),
            ("υστεροσκόπηση", "ysteroskopisi", "Υστεροσκόπηση", [
                ("υστεροσκοπική-αφαίρεση-πολύποδα-2", "ysteroskopiki-afairesi-polypoda", "Υστεροσκοπική αφαίρεση πολύποδα", []),
                ("υστεροσκοπική-αφαίρεση-ινομυώματος", "ysteroskopiki-afairesi-inomyomatos", "Υστεροσκοπική Αφαίρεση Ινομυώματος", []),
                ("υστεροσκοπική-αφαίρεση-διαφράγματος-page", "ysteroskopiki-afairesi-diafragmatos", "Υστεροσκοπική αφαίρεση διαφράγματος", []),
            ]),
            ("λαπαροσκόπηση", "laparoskopisi", "Λαπαροσκόπηση", [
                ("λαπαροσκοπική-υστερεκτομή", "laparoskopiki-ysterektomi", "Λαπαροσκοπική Υστερεκτομή", []),
                ("λαπαροσκοπική-ινομυωματεκτομή", "laparoskopiki-inomyomatektomi", "Λαπαροσκοπική Ινομυωματεκτομή", []),
                ("λαπαροσκοπική-αφαίρεση-κύστης", "laparoskopiki-afairesi-kystis", "Λαπαροσκοπική Αφαίρεση Κύστης", []),
                ("λαπαροσκόπηση-ενδομητρίωσης", "laparoskopisi-endomitriosis", "Λαπαροσκόπηση Ενδομητρίωσης", []),
            ]),
            ("υστερεκτομή", "ysterektomi", "Υστερεκτομή", []),
            ("κωνοειδής-εκτομή-τραχήλου", "konoeidis-ektomi-traxilou", "Κωνοειδής εκτομή τραχήλου", []),
            ("ουρογυναικολογία-page", "ourogynaikologia", "Ουρογυναικολογία", [
                ("τοποθέτηση-ταινίας-για-ακράτεια-ούρω", "tainia-akrateias-ouron", "Τοποθέτηση ταινίας για ακράτεια ούρων", []),
            ]),
        ],
    },
    {
        "dir": "ypogonimotita",
        "title": "Υπογονιμότητα",
        "nav": "Υπογονιμότητα",
        "eyebrow": "Υπηρεσίες",
        "icon": "✦",
        "src": "υπογονιμότητα",
        "lead": "Διερεύνηση και αντιμετώπιση της υπογονιμότητας σε τρεις ενότητες: ο πλήρης "
                "έλεγχος της γυναίκας και του άνδρα, οι θεραπείες υποβοηθούμενης "
                "αναπαραγωγής και οι νεότερες τεχνολογίες του εμβρυολογικού εργαστηρίου.",
        # Τρία μεγάλα sub-dropbars, σύμφωνα με το κείμενο του ιατρού
        # («rotas allages 3.txt», Αύγουστος 2026).
        "grouped": True,
        "pages": [
            # Ο ιατρός το ονομάζει σκέτο «Υπογονιμότητα»· επειδή έτσι θα
            # επαναλαμβανόταν ο τίτλος της ενότητας (μενού + breadcrumbs),
            # εμφανίζεται ως «Διερεύνηση Υπογονιμότητας».
            ("new-diereynisi", "diereynisi", "Διερεύνηση Υπογονιμότητας", [
                ("new-diereynisi-gynaikas", "diereynisi-gynaikas", "Διερεύνηση γυναίκας", [
                    ("new-ormonikos-elegxos-gynaikas", "ormonikos-elegxos-gynaikas", "Ορμονικός έλεγχος γυναίκας", []),
                    ("new-salpiggografia-hycosy", "salpiggografia-hycosy", "Σαλπιγγογραφία και HyCoSy", []),
                    ("new-ypodektikotita-endomitriou", "ypodektikotita-endomitriou", "Έλεγχος υποδεκτικότητας ενδομητρίου", []),
                    ("new-xronia-endomitritida", "xronia-endomitritida", "Έλεγχος για χρόνια ενδομητρίτιδα", []),
                ]),
                ("new-diereynisi-andra", "diereynisi-andra", "Διερεύνηση του άνδρα", [
                    ("new-ormonikos-elegxos-andra", "ormonikos-elegxos-andra", "Ορμονικός έλεγχος άνδρα", []),
                    ("new-spermodiagramma", "spermodiagramma", "Σπερμοδιάγραμμα", []),
                    ("new-eidikes-exetaseis-spermatos", "eidikes-exetaseis-spermatos", "Ειδικές εξετάσεις στο σπέρμα", []),
                ]),
            ]),
            ("new-therapeies-ypogonimotitas", "therapeies-ypogonimotitas", "Θεραπείες Υπογονιμότητας", [
                ("new-proklisi-oothylakiorrixias", "proklisi-oothylakiorrixias", "Πρόκληση ωοθυλακιορρηξίας", []),
                ("new-spermategxysi-iui", "spermategxysi-iui", "Ενδομήτρια σπερματέγχυση (IUI)", []),
                ("new-exosomatiki-gonimopoiisi", "exosomatiki-gonimopoiisi", "Εξωσωματική γονιμοποίηση", []),
                ("new-fysikos-kyklos", "fysikos-kyklos", "Εξωσωματική σε φυσικό κύκλο", []),
                ("new-dorea-oarion", "dorea-oarion", "Εξωσωματική με δότρια ωαρίου", []),
                ("new-doti-spermatos", "doti-spermatos", "Εξωσωματική με δότη σπέρματος", []),
                ("new-katapsyxi-oarion", "katapsyxi-oarion", "Κατάψυξη ωαρίων", []),
            ]),
            ("new-neoteres-texnologies", "neoteres-texnologies", "Νεότερες τεχνολογίες στην υποβοηθούμενη αναπαραγωγή", [
                ("new-time-lapse", "time-lapse", "Τεχνολογία Time-Lapse", []),
                ("new-ypovoithoumeni-ekkolapsi", "ypovoithoumeni-ekkolapsi", "Υποβοηθούμενη εκκόλαψη", []),
                ("new-proemfyteftikos-genetikos-elegxos", "proemfyteftikos-genetikos-elegxos", "Προεμφυτευτικός γενετικός έλεγχος (PGT)", []),
            ]),
        ],
        # Σελίδες που παραμένουν ζωντανές (παλιά URLs / SEO) αλλά δεν μπαίνουν
        # στα τρία sub-dropbars. Εμφανίζονται στο τέλος της σελίδας ενότητας.
        "extra_title": "Περισσότερα θέματα υπογονιμότητας",
        "extra": [
            ("συμβουλευτική-γονιμότητας-page", "symvouleftiki-gonimotitas", "Συμβουλευτική Γονιμότητας", []),
            ("αξιολόγηση-υπογονιμότητας", "axiologisi-ypogonimotitas", "Αξιολόγηση υπογονιμότητας", []),
            ("θεραπείες-εξωσωματικής-hub", "therapeies-exosomatikis", "Θεραπείες εξωσωματικής", []),
            ("mini-ivf-page", "mini-ivf", "Μικρο Εξωσωματική γονιμοποίηση (mini IVF)", []),
            ("αναζωογόνηση-ωοθηκών-prp-page", "anazoogonisi-oothikon-prp", "Αναζωογόνηση ωοθηκών (PRP)", []),
            ("παρένθετη-μητρότητα-page", "parentheti-mitrotita", "Παρένθετη Μητρότητα", []),
        ],
    },
]

# ---------------------------------------------------------------- redirects
# Old URLs that moved when the Μαιευτική section was restructured. Kept alive
# as noindex meta-refresh stubs so existing links and search results still land
# on the right page.  old path -> new path
REDIRECTS = {
    "maieftiki/proeklampsia-thrombofilia.html": "maieftiki/proeklampsia.html",
    "gynaikologia/isxiaki-provoli.html": "maieftiki/isxiaki-provoli.html",
    # Σελίδες που άλλαξαν ενότητα (Αύγουστος 2026)
    "ypogonimotita/epanalambanomenes-apovoles.html": "maieftiki/epanalambanomenes-apovoles.html",
    "embryomitriki/genetikes-diataraxes.html": "maieftiki/genetikes-diataraxes.html",
}

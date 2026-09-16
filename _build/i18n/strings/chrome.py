# -*- coding: utf-8 -*-
"""Navigation, footer, breadcrumbs, clinic details — every page carries these.

The English wording follows the previous English site (Athens Clinic, Mob.,
124A Vasilissis Sofias Avenue) so old and new pages read the same.
"""

SITE = {
    "Ρώτας Μιχάλης MD, FACOG": "Dr. Michael Rotas MD, FACOG",
    "Δρ. Μιχάλης Ρώτας": "Dr. Michael Rotas",
    "Ρώτας Μιχάλης MD, FACOG Αρχική": "Dr. Michael Rotas MD, FACOG Home",
    "Μαιευτήρας Χειρουργός Γυναικολόγος": "Obstetrician Surgeon Gynecologist",
    "Μαιευτήρας – Χειρουργός Γυναικολόγος": "Obstetrician – Surgeon Gynecologist",
    "Ειδικός Εμβρυομητρικής Ιατρικής": "Specialist in Maternal–Fetal Medicine",
}

NAV = {
    "Αρχική": "Home",
    "Ο Ιατρός": "The Doctor",
    "Μαιευτική": "Obstetrics",
    "Εμβρυομητρική": "Fetal Medicine",
    "Γυναικολογία": "Gynecology",
    "Χειρουργεία": "Surgery",
    "Υπογονιμότητα": "Infertility",
    "Επικοινωνία": "Contact",
    "Τα ιατρεία μας": "Our Clinics",
    "Υπηρεσίες": "Services",
    "Ραντεβού": "Appointment",
    "Κύρια πλοήγηση": "Main navigation",
    "Άνοιγμα μενού": "Open menu",
    "Μετάβαση στο περιεχόμενο": "Skip to content",
    "Διαδρομή": "Breadcrumb",
    "Σε αυτή την ενότητα": "In this section",
    "Σχετικές σελίδες": "Related pages",
    "Μάθετε περισσότερα": "Learn more",
    "Όλα": "All",
}

CLINICS = {
    "Ιατρείο Αθηνών": "Athens Clinic",
    "Ιατρείο Νέας Σμύρνης": "Nea Smyrni Clinic",
    "Ρώτας Μιχάλης MD, FACOG Ιατρείο Αθηνών":
        "Dr. Michael Rotas MD, FACOG Athens Clinic",
    "Ρώτας Μιχάλης MD, FACOG Ιατρείο Νέας Σμύρνης":
        "Dr. Michael Rotas MD, FACOG Nea Smyrni Clinic",
    "Λεωφόρος Βασιλίσσης Σοφίας 124Α": "124A Vasilissis Sofias Avenue",
    "Λεωφόρος Βασιλίσσης Σοφίας 124Α, Αθήνα":
        "124A Vasilissis Sofias Avenue, Athens",
    "25ης Μαρτίου 11": "11 25is Martiou",
    "25ης Μαρτίου 11, Νέα Σμύρνη": "11 25is Martiou, Nea Smyrni",
    "Κεντρική Πλατεία": "Central Square",
    "Αθήνα": "Athens",
    "Αθήνα, Τ.Κ. 11526": "Athens, 11526",
    "Νέα Σμύρνη": "Nea Smyrni",
    "Νέα Σμύρνη, Τ.Κ. 17121": "Nea Smyrni, 17121",
    "Τηλ. 210 771 7705": "Tel. 210 771 7705",
    "Τηλ. 210 934 3538": "Tel. 210 934 3538",
    "Κιν. 695 519 9198": "Mob. 695 519 9198",
    "Καλέστε 695 519 9198": "Call 695 519 9198",
    "Στοιχεία Επικοινωνίας": "Contact details",
    "Κλείστε ραντεβού": "Book an appointment",
    "Κλείστε το ραντεβού σας": "Book your appointment",
    "Ο ιατρός δέχεται κατόπιν ραντεβού.":
        "The doctor sees patients by appointment.",
    "Ο ιατρός δέχεται κατόπιν ραντεβού στα ιατρεία Αθήνας και Νέας Σμύρνης.":
        "The doctor sees patients by appointment at the Athens and Nea Smyrni clinics.",
    "Ιατρεία σε Αθήνα (Βασ. Σοφίας) και Νέα Σμύρνη κατόπιν ραντεβού.":
        "Clinics in Athens (Vas. Sofias) and Nea Smyrni, by appointment.",
    "Είμαστε εδώ για κάθε ερώτημα": "We are here for any question",
    "σχετικά με την υγεία σας.": "about your health.",
    "Επιστήμη, εμπειρία & ανθρώπινη φροντίδα.":
        "Science, experience & human care.",
}

FOOTER = {
    "Το περιεχόμενο του ιστότοπου έχει ενημερωτικό χαρακτήρα και δεν "
    "υποκαθιστά την ιατρική συμβουλή, διάγνωση ή θεραπεία. Για κάθε θέμα "
    "υγείας απευθυνθείτε στον ιατρό σας.":
        "The content of this website is for information only and is not a "
        "substitute for medical advice, diagnosis or treatment. For any health "
        "concern, please consult your doctor.",
    "gynaicologos.gr Ρώτας Μιχάλης MD, FACOG. Με επιφύλαξη παντός δικαιώματος.":
        "gynaicologos.gr Dr. Michael Rotas MD, FACOG. All rights reserved.",
}

STRINGS = {}
for _d in (SITE, NAV, CLINICS, FOOTER):
    STRINGS.update(_d)

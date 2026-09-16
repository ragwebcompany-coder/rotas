# -*- coding: utf-8 -*-
"""Contact page and the Our Clinics page."""

CONTACT = {
    "Επικοινωνία Ρώτας Μιχάλης MD, FACOG | Γυναικολόγος Αθήνα & Νέα Σμύρνη":
        "Contact Dr. Michael Rotas MD, FACOG | Gynecologist Athens & Nea Smyrni",
    "Επικοινωνία Ρώτας Μιχάλης MD, FACOG": "Contact Dr. Michael Rotas MD, FACOG",
    "Γυναικολόγος Αθήνα & Νέα Σμύρνη": "Gynecologist Athens & Nea Smyrni",
    "Επικοινωνία με τον Ρώτα Μιχάλη MD, FACOG. Ιατρείο Αθήνας: Βασ. Σοφίας "
    "124Α, τηλ. 210 771 7705. Ιατρείο Νέας Σμύρνης: 25ης Μαρτίου 11, τηλ. 210 "
    "934 3538.":
        "Contact Dr. Michael Rotas MD, FACOG. Athens Clinic: 124A Vas. Sofias "
        "Avenue, tel. 210 771 7705. Nea Smyrni Clinic: 11 25is Martiou, tel. "
        "210 934 3538.",
    "Εδώ για εσάς, με βασική μας αξία να λύσουμε οποιαδήποτε απορία σχετικά με "
    "την υγεία σας. Δύο ιατρεία στη Λεωφόρο Βασιλίσσης Σοφίας και στην κεντρική "
    "πλατεία Νέας Σμύρνης.":
        "Here for you, with one guiding principle: to answer every question you "
        "have about your health. Two clinics, on Vasilissis Sofias Avenue and "
        "on the central square of Nea Smyrni.",
    "Διεύθυνση": "Address",
    "Τηλέφωνο": "Telephone",
    "Κινητό": "Mobile",
    "Καλέστε το ιατρείο": "Call the clinic",
    "Χάρτης": "Map",
    "Ακολουθήστε μας": "Follow us",
}

CLINICS_PAGE = {
    "Τα ιατρεία του Ρώτα Μιχάλη MD, FACOG σε Αθήνα, Βασ. Σοφίας 124Α, και Νέα "
    "Σμύρνη, 25ης Μαρτίου 11. Φωτογραφίες, στοιχεία επικοινωνίας και χάρτες.":
        "The clinics of Dr. Michael Rotas MD, FACOG in Athens, 124A Vas. Sofias "
        "Avenue, and Nea Smyrni, 11 25is Martiou. Photographs, contact details "
        "and maps.",
    "Δύο σύγχρονοι χώροι σε Αθήνα και Νέα Σμύρνη":
        "Two modern spaces in Athens and Nea Smyrni",
    "Ο ιατρός δέχεται κατόπιν ραντεβού στα δύο πλήρως εξοπλισμένα ιατρεία, στη "
    "Λεωφόρο Βασιλίσσης Σοφίας και στην κεντρική πλατεία Νέας Σμύρνης.":
        "The doctor sees patients by appointment at two fully equipped clinics, "
        "on Vasilissis Sofias Avenue and on the central square of Nea Smyrni.",
    "Φωτεινός, σύγχρονος χώρος στην κεντρική πλατεία Νέας Σμύρνης, με άνετη "
    "υποδοχή και εξοπλισμό για μαιευτικές και γυναικολογικές εξετάσεις.":
        "A bright, modern space on the central square of Nea Smyrni, with a "
        "comfortable reception area and equipment for obstetric and "
        "gynecological examinations.",
    "Το ιατρείο Αθηνών στην EMBRYOCOSMOS, στη Λεωφόρο Βασιλίσσης Σοφίας, "
    "διαμορφωμένο για άνετη επίσκεψη και ολοκληρωμένη ιατρική εξέταση.":
        "The Athens clinic at EMBRYOCOSMOS, on Vasilissis Sofias Avenue, "
        "designed for a comfortable visit and a thorough medical examination.",
    "Βασ. Σοφίας": "Vas. Sofias",
    "Ιατρείο Βασιλίσσης Σοφίας": "Vasilissis Sofias Clinic",
    "Collage φωτογραφιών από το ιατρείο Νέας Σμύρνης":
        "Photo collage of the Nea Smyrni clinic",
    "Collage φωτογραφιών από το ιατρείο Βασιλίσσης Σοφίας":
        "Photo collage of the Vasilissis Sofias clinic",
}

# gallery captions, the same set of rooms photographed at both clinics
ROOMS = {
    "χώρος υποδοχής": "reception area",
    "λεπτομέρεια χώρου": "interior detail",
    "εξεταστήριο": "examination room",
    "σύγχρονος εξοπλισμός": "modern equipment",
    "εσωτερικός χώρος": "interior",
    "χώρος εξέτασης": "examination area",
    "καθιστικό": "seating area",
    "χώρος ιατρείου": "clinic space",
    "λεπτομέρεια διακόσμησης": "decorative detail",
    "δωμάτιο εξέτασης": "consulting room",
    "φωτεινός εσωτερικός χώρος": "bright interior",
    "υποδομή ιατρείου": "clinic facilities",
    "χώρος αναμονής": "waiting area",
    "ιατρικός εξοπλισμός": "medical equipment",
    "εσωτερική άποψη": "interior view",
    "χώρος ιατρικής φροντίδας": "care area",
}

STRINGS = {}
for _d in (CONTACT, CLINICS_PAGE):
    STRINGS.update(_d)

for _gr, _en in (("Ιατρείο Νέας Σμύρνης", "Nea Smyrni Clinic"),
                 ("Ιατρείο Βασιλίσσης Σοφίας", "Vasilissis Sofias Clinic")):
    for _room_gr, _room_en in ROOMS.items():
        STRINGS[f"{_gr}, {_room_gr}"] = f"{_en}, {_room_en}"

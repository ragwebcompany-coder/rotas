# -*- coding: utf-8 -*-
"""The Doctor — biography, qualifications, publications, team, facilities."""

SHARED = {
    "Σχετικά με εμάς": "About us",
    "Ο Δρ. Μιχάλης Ρώτας, Μαιευτήρας Χειρουργός Γυναικολόγος και Ειδικός "
    "Εμβρυομητρικής Ιατρικής, με εκπαίδευση και κλινική εμπειρία σε κορυφαία "
    "πανεπιστημιακά νοσοκομεία των ΗΠΑ και του Ηνωμένου Βασιλείου.":
        "Dr. Michael Rotas, Obstetrician Surgeon Gynecologist and Specialist in "
        "Maternal–Fetal Medicine, trained and clinically experienced in leading "
        "university hospitals in the USA and the United Kingdom.",
    "Απόφοιτος της Ιατρικής Σχολής του Πανεπιστημίου Αθηνών με πολλαπλές "
    "διακρίσεις και υποτροφίες από το Κρατικό Ίδρυμα Υποτροφιών.":
        "Graduate of the Medical School of the University of Athens with "
        "multiple distinctions and scholarships from the State Scholarships "
        "Foundation.",
    "Ειδίκευση σε μεγάλα πανεπιστημιακά νοσοκομεία, μεταξύ αυτών το State "
    "University of New York in Brooklyn Maimonides Medical Center.":
        "Residency training in major university hospitals, among them the State "
        "University of New York in Brooklyn — Maimonides Medical Center.",
    "Πολυετής εκπαίδευση και εργασιακή εμπειρία σε πανεπιστημιακά νοσοκομεία "
    "των ΗΠΑ και του Ηνωμένου Βασιλείου.":
        "Years of training and professional experience in university hospitals "
        "in the USA and the United Kingdom.",
    "Εργάσθηκε στο Memorial Sloan Kettering Cancer Center, ένα από τα "
    "μεγαλύτερα εξειδικευμένα ογκολογικά κέντρα παγκοσμίως.":
        "Worked at Memorial Sloan Kettering Cancer Center, one of the largest "
        "specialized cancer centers in the world.",
    "Βραβεύθηκε από την Αμερικανική Ένωση Γυναικολογικής Λαπαροσκόπησης (AAGL) "
    "για τις εξαιρετικές χειρουργικές δεξιότητές του.":
        "Awarded by the American Association of Gynecologic Laparoscopists "
        "(AAGL) for his outstanding surgical skills.",
    "Κάτοχος του ανώτερου βαθμού πιστοποίησης στην Εμβρυομητρική Ιατρική "
    "(Diploma in Fetal Medicine).":
        "Holder of the highest level of certification in Maternal–Fetal "
        "Medicine (Diploma in Fetal Medicine).",
}

INDEX = {
    "Ο Ιατρός | Ρώτας Μιχάλης MD, FACOG Γυναικολόγος Αθήνα":
        "The Doctor | Dr. Michael Rotas MD, FACOG Gynecologist Athens",
    "Ρώτας Μιχάλης MD, FACOG Γυναικολόγος Αθήνα":
        "Dr. Michael Rotas MD, FACOG Gynecologist Athens",
    "Ρώτας Μιχάλης MD, FACOG — Μαιευτήρας Χειρουργός Γυναικολόγος":
        "Dr. Michael Rotas MD, FACOG — Obstetrician Surgeon Gynecologist",
    "Βιογραφικό": "Biography",
    "Μαιευτήρας Χειρουργός Γυναικολόγος · Ειδικός Εμβρυομητρικής Ιατρικής · "
    "Ειδικός Αναπαραγωγικής Ιατρικής":
        "Obstetrician Surgeon Gynecologist · Specialist in Maternal–Fetal "
        "Medicine · Specialist in Reproductive Medicine",
    "Το πλήρες βιογραφικό": "The full CV",
    "Πλήρες βιογραφικό σημείωμα του Μιχάλη Ρώτα MD, FACOG, Μαιευτήρα "
    "Χειρουργού Γυναικολόγου και Ειδικού Εμβρυομητρικής Ιατρικής.":
        "The full curriculum vitae of Dr. Michael Rotas MD, FACOG, Obstetrician "
        "Surgeon Gynecologist and Specialist in Maternal–Fetal Medicine.",
    # counters on the section page
    "Τοκετοί": "Deliveries",
    "Αυχενικές Διαφάνειες": "Nuchal translucency scans",
    "Κολποσκοπήσεις": "Colposcopies",
    "Κύκλοι Εξωσωματικής": "IVF cycles",
    "Υστεροσκοπήσεις": "Hysteroscopies",
}

QUALIFICATIONS = {
    "ΑΚΑΔΗΜΑΙΚΟΙ-ΜΕΤΑΠΤΥΧΙΑΚΟΙ ΤΙΤΛΟΙ": "ACADEMIC AND POSTGRADUATE QUALIFICATIONS",
    "ΤΙΤΛΟΙ ΕΙΔΙΚΟΤΗΤΑΣ": "SPECIALIST QUALIFICATIONS",
    "Τίτλοι & πιστοποιήσεις": "Titles & certifications",
    "Εκπαίδευση & καριέρα": "Training & career",
    "Μέλος του Αμερικανικού Κολλεγίου Μαιευτήρων Γυναικολόγων":
        "Fellow of the American College of Obstetricians and Gynecologists",
    "Fetal Medicine Foundation, Λονδίνο ανώτερος βαθμός πιστοποίησης στην "
    "Εμβρυομητρική Ιατρική":
        "Fetal Medicine Foundation, London — highest level of certification in "
        "Maternal–Fetal Medicine",
    "ΡΕΑ": "REA",
    "Συνεργάτης Κλινικής Υποβοηθούμενης Αναπαραγωγής":
        "Associate of the Assisted Reproduction Unit",
    "Βράβευση από την Αμερικανική Ένωση Γυναικολογικής Λαπαροσκόπησης":
        "Award from the American Association of Gynecologic Laparoscopists",
    "Μέλος της κριτικής επιτροπής του Obstetrics and Gynecology":
        "Member of the review board of Obstetrics and Gynecology",
    "Galloway Fellowship στη γυναικολογική ογκολογία":
        "Galloway Fellowship in gynecologic oncology",
    "Τ. Επιμελητής Μαιευτικής & Γυναικολογίας, University of Southern California":
        "Former Attending in Obstetrics & Gynecology, University of Southern "
        "California",
    "Πρώτο βραβείο έρευνας ειδικευομένων μαιευτικής & γυναικολογίας, 2007":
        "First prize for resident research in obstetrics & gynecology, 2007",
}

CV = {
    "Διεθνής εκπαίδευση": "International training",
    "Μία δεκαετής πορεία σε κορυφαία πανεπιστημιακά κέντρα":
        "A decade at leading university centers",
    "Ο ιατρός Ρώτας Μιχάλης αποφοίτησε από την Ιατρική Σχολή του Πανεπιστημίου "
    "Αθηνών. Κατά τη διάρκεια των σπουδών του έλαβε πλήθος από βραβεία και "
    "τιμητικές διακρίσεις. Υπήρξε επίσης υπότροφος του κληροδοτήματος Παπαδάκη "
    "και του Ιδρύματος Κρατικών Υποτροφιών (ΙΚΥ) σε όλη τη διάρκεια της φοίτησης.":
        "Dr. Michael Rotas graduated from the Medical School of the University "
        "of Athens. During his studies he received numerous awards and honors. "
        "He also held the Papadakis bequest scholarship and a State "
        "Scholarships Foundation (IKY) scholarship throughout his studies.",
    "Βασικά σημεία εκπαίδευσης": "Training highlights",
    "Άδεια άσκησης στις Η.Π.Α.": "Medical license in the USA",
    "Υπερηχογραφήματα στην Ελλάδα τα τελευταία 4 έτη":
        "Ultrasound scans in Greece over the past 4 years",
    "Η.Π.Α.": "USA",
    "Πλήρης ειδίκευση και κλινική εμπειρία στην Αμερική":
        "Full residency and clinical experience in the United States",
    "Μετά τη λήψη του πτυχίου και ύστερα από εξαιρετικά απαιτητικές εξετάσεις "
    "(USMLE), απέκτησε την άδεια ασκήσεως επαγγέλματος στις Ηνωμένες Πολιτείες "
    "Αμερικής, όπου μετέβη για την πλήρη ειδίκευσή του στη Μαιευτική "
    "Γυναικολογία.":
        "After graduating, and following the highly demanding USMLE "
        "examinations, he obtained his license to practice medicine in the "
        "United States, where he moved to complete his full residency in "
        "Obstetrics and Gynecology.",
    "Εργάστηκε σε μεγάλα πανεπιστημιακά νοσοκομεία της Ανατολικής Ακτής των "
    "Η.Π.Α., μεταξύ των οποίων:":
        "He worked in major university hospitals on the East Coast of the USA, "
        "among them:",
    "Αμερικανικές διακρίσεις": "Distinctions in the United States",
    "Πιστοποιητικό Chief Resident στο Maimonides Medical Center":
        "Chief Resident certificate at Maimonides Medical Center",
    "Άδεια Physician and Surgeon από το Medical Board of California":
        "Physician and Surgeon license from the Medical Board of California",
    "Άδεια ασκήσεως επαγγέλματος στην Πολιτεία της Καλιφόρνια.":
        "License to practice medicine in the State of California.",
    "Ο ιατρός και οι διεθνείς τίτλοι στον χώρο του ιατρείου":
        "The doctor and his international qualifications at the clinic",
    "Εμβρυομητρική ιατρική": "Maternal–fetal medicine",
    "Εξειδίκευση σε μία από τις μεγαλύτερες μονάδες της Νέας Υόρκης":
        "Subspecialty training in one of New York's largest units",
    "Ο ιατρός υπήρξε βασικό στέλεχος μίας από τις μεγαλύτερες μονάδες "
    "εμβρυομητρικής ιατρικής στην πολιτεία της Νέας Υόρκης, η οποία "
    "εξειδικεύεται στην αντιμετώπιση ειδικών λοιμώξεων στην εγκυμοσύνη.":
        "He was a senior member of one of the largest maternal–fetal medicine "
        "units in the state of New York, which specializes in the management of "
        "specific infections in pregnancy.",
    "Αποτέλεσμα της εμπειρίας και του έργου του στον τομέα αυτό είναι να "
    "θεωρείται στις Η.Π.Α. ειδικός στις λοιμώξεις στην εγκυμοσύνη και να είναι "
    "μέλος της κριτικής επιτροπής σε θέματα λοιμώξεων στην κύηση της "
    "γυναικολογικής επιθεώρησης":
        "As a result of his experience and work in this field he is regarded in "
        "the USA as an expert on infections in pregnancy, and he serves on the "
        "review board for infection in pregnancy of the journal",
    "Μετά την ολοκλήρωση της εκπαίδευσης και τη λήψη του τίτλου ειδικότητας "
    "εργάστηκε ως επιμελητής στο University of Southern California Ventura "
    "Medical Center.":
        "After completing his training and obtaining his specialist "
        "qualification, he worked as an attending physician at the University "
        "of Southern California — Ventura Medical Center.",
    "Λονδίνο": "London",
    "Ο επόμενος σταθμός της εκπαίδευσης ήταν το Λονδίνο, όπου απέκτησε την "
    "υπο-ειδικότητα της εμβρυομητρικής ιατρικής και το Diploma in Fetal "
    "Medicine.":
        "The next stage of his training was London, where he gained the "
        "subspecialty in maternal–fetal medicine and the Diploma in Fetal "
        "Medicine.",
    "Εργάστηκε στο Harris Birthright Research Centre for Fetal Medicine του "
    "King's College Hospital επί τρία έτη, δίπλα στον Καθηγητή Κύπρο Νικολαΐδη.":
        "He worked at the Harris Birthright Research Centre for Fetal Medicine "
        "at King's College Hospital for three years, alongside Professor Kypros "
        "Nicolaides.",
    "Εξειδίκευση κατά την εκπαίδευση στο Λονδίνο":
        "Areas of expertise gained during his training in London",
    "Εξέταση της Αυχενικής Διαφάνειας στις 12 εβδομάδες.":
        "Nuchal translucency assessment at 12 weeks.",
    "Υπερηχογράφημα Β επιπέδου στις 20 εβδομάδες για διερεύνηση συγγενών "
    "ανωμαλιών.":
        "Level II ultrasound at 20 weeks to screen for congenital anomalies.",
    "Μελέτη Doppler και υπερηχογράφημα ανάπτυξης του εμβρύου στις 32 εβδομάδες.":
        "Doppler studies and fetal growth ultrasound at 32 weeks.",
    "Αμνιοπαρακεντήσεις και λήψη τροφοβλάστης για αποκλεισμό γενετικών "
    "ανωμαλιών.":
        "Amniocentesis and chorionic villus sampling to rule out genetic "
        "abnormalities.",
    "Laser για τη θεραπεία του συνδρόμου TTTS σε μονοχοριακά έμβρυα.":
        "Laser therapy for twin–twin transfusion syndrome (TTTS) in "
        "monochorionic twins.",
    "Diploma in Fetal Medicine από The Fetal Medicine Foundation":
        "Diploma in Fetal Medicine from The Fetal Medicine Foundation",
    "Ένας από τους λίγους Έλληνες Διπλωματούχους Ιατρικής Εμβρύου (FMF).":
        "One of the few Greek holders of the Diploma in Fetal Medicine (FMF).",
    "Ιδιωτικό ιατρείο Καθηγητή Κύπρου Νικολαΐδη":
        "Private practice of Professor Kypros Nicolaides",
    "Εκτέλεση εξειδικευμένων υπερηχογραφικών εξετάσεων σε διεθνές κέντρο "
    "αναφοράς.":
        "Performing specialized ultrasound examinations at an international "
        "referral center.",
    "Κατά το ίδιο χρονικό διάστημα είχε το σπάνιο προνόμιο να εργαστεί στο "
    "ιδιωτικό Fetal Medicine Centre του παγκοσμίου φήμης Καθηγητή Κύπρου "
    "Νικολαΐδη στο Λονδίνο, του ιατρού που, μεταξύ άλλων, ανέπτυξε την αυχενική "
    "διαφάνεια.":
        "During the same period he had the rare privilege of working at the "
        "private Fetal Medicine Centre of the world-renowned Professor Kypros "
        "Nicolaides in London — the doctor who, among other things, developed "
        "nuchal translucency screening.",
    "Φέρει επίσης πιστοποιητικό εκτέλεσης υπερηχογραφημάτων καρδιάς εμβρύου, με "
    "διαπίστευση από την παιδοκαρδιολόγο με εξειδίκευση στην εμβρυϊκή "
    "υπερηχοκαρδιογραφία Professor Lindsay Allan.":
        "He also holds a certificate in fetal echocardiography, accredited by "
        "Professor Lindsay Allan, the pediatric cardiologist specializing in "
        "fetal echocardiography.",
    "Ο Δρ. Μιχάλης Ρώτας σε ομιλία στη Μαιευτική Γυναικολογική Κλινική ΡΕΑ":
        "Dr. Michael Rotas speaking at the REA Maternity and Gynecology Clinic",
    "Σύγχρονη κλινική πράξη": "Current clinical practice",
    "Επιστροφή στην Ελλάδα και συνεχής διεθνής δραστηριότητα":
        "Return to Greece and continuing international activity",
    "Ο ιατρός Ρώτας επέστρεψε στην Ελλάδα το 2011 μετά από δεκαετή διεθνή "
    "καριέρα και εργάζεται στη Μονάδα Ιατρικής του Εμβρύου του Μαιευτηρίου ΡΕΑ.":
        "Dr. Rotas returned to Greece in 2011 after a ten-year international "
        "career and works at the Fetal Medicine Unit of the REA Maternity "
        "Hospital.",
    "Έχει δεκάδες παρουσίες και ομιλίες σε διεθνή και Παναμερικανικά συνέδρια, "
    "δεκάδες δημοσιεύσεις σε έγκριτα διεθνή περιοδικά, ενώ έχει επιλεγεί από "
    "πολλά περιοδικά ως κριτής άρθρων προς δημοσίευση.":
        "He has given dozens of presentations and talks at international and "
        "Pan-American congresses, has dozens of publications in respected "
        "international journals, and has been selected by many journals as a "
        "peer reviewer.",
}

TEAM = {
    "Μια ομάδα γύρω από κάθε γυναίκα": "A team around every woman",
    "Η παρακολούθηση μιας εγκυμοσύνης και η γυναικολογική φροντίδα δεν είναι "
    "έργο ενός μόνο ανθρώπου. Στα ιατρεία μας ο ιατρός συνεργάζεται σταθερά με "
    "μαία και με…":
        "Caring for a pregnancy, and for a woman's gynecological health, is not "
        "the work of one person alone. At our clinics the doctor works closely "
        "and consistently with a midwife and with a…",
    "Η παρακολούθηση μιας εγκυμοσύνης και η γυναικολογική φροντίδα δεν είναι "
    "έργο ενός μόνο ανθρώπου. Στα ιατρεία μας ο ιατρός συνεργάζεται σταθερά με "
    "μαία και με εμβρυοκαρδιολόγο, ώστε κάθε γυναίκα να έχει συνέχεια στη "
    "φροντίδα της, από την πρώτη επίσκεψη έως τον τοκετό και τη λοχεία.":
        "Caring for a pregnancy, and for a woman's gynecological health, is not "
        "the work of one person alone. At our clinics the doctor works closely "
        "and consistently with a midwife and with a fetal cardiologist, so that "
        "every woman has continuity of care from her first visit through to "
        "delivery and the postpartum period.",
    "Η συνεργασία αυτή σημαίνει πρακτικά ότι τα ευρήματα κάθε εξέτασης "
    "συζητούνται μεταξύ μας, ότι έχετε κάποιον να απευθυνθείτε ανάμεσα στα "
    "ραντεβού, και ότι όταν χρειάζεται εξειδικευμένη γνώμη, αυτή είναι "
    "διαθέσιμη μέσα στο ίδιο ιατρείο και όχι με νέα παραπομπή.":
        "In practice this means that the findings of every examination are "
        "discussed among us, that you have someone to turn to between "
        "appointments, and that when a specialist opinion is needed it is "
        "available within the same practice rather than through a new referral.",
}

MIDWIFE = {
    "Ο ρόλος της μαίας στο ιατρείο": "The midwife's role at the clinic",
    "Η μαία είναι, για τις περισσότερες γυναίκες, ο άνθρωπος με τον οποίο έχουν "
    "την πιο συχνή επαφή κατά τη διάρκεια της εγκυμοσύνης. Πέρα από τις "
    "μετρήσεις και τις εξετάσεις…":
        "For most women the midwife is the person they are in contact with most "
        "often during pregnancy. Beyond the measurements and the routine…",
    "Η μαία είναι, για τις περισσότερες γυναίκες, ο άνθρωπος με τον οποίο έχουν "
    "την πιο συχνή επαφή κατά τη διάρκεια της εγκυμοσύνης. Πέρα από τις "
    "μετρήσεις και τις εξετάσεις ρουτίνας, είναι εκείνη που έχει τον χρόνο για "
    "τις ερωτήσεις της καθημερινότητας, αυτές που συχνά δεν προλαβαίνουν να "
    "ειπωθούν στο ιατρικό ραντεβού.":
        "For most women the midwife is the person they are in contact with most "
        "often during pregnancy. Beyond the measurements and the routine tests, "
        "she is the one who has time for the everyday questions — the ones "
        "there is often no time to ask during the medical appointment.",
    "Τι αναλαμβάνει": "What she takes care of",
    "Παρακολούθηση της εγκυμοσύνης σε συνεργασία με τον ιατρό.":
        "Monitoring the pregnancy together with the doctor.",
    "Καρδιοτοκογράφημα και έλεγχος της ευεξίας του εμβρύου.":
        "Cardiotocography and assessment of fetal wellbeing.",
    "Προετοιμασία για τον τοκετό και συζήτηση του σχεδίου τοκετού.":
        "Preparation for labor and discussion of the birth plan.",
    "Υποστήριξη κατά τον τοκετό.": "Support during labor and birth.",
    "Καθοδήγηση στον θηλασμό και στη φροντίδα του νεογνού.":
        "Guidance on breastfeeding and newborn care.",
    "Παρακολούθηση της λοχείας και της αποκατάστασης μετά τον τοκετό.":
        "Follow-up during the postpartum period and recovery after birth.",
    "Επικοινωνήστε με το ιατρείο για να κλείσετε ραντεβού με τη μαία μας ή για "
    "να ενημερωθείτε για τα μαθήματα προετοιμασίας τοκετού.":
        "Contact the clinic to book an appointment with our midwife or to find "
        "out about our childbirth preparation classes.",
}

CARDIOLOGIST = {
    "Τι είναι η εμβρυϊκή καρδιολογία": "What fetal cardiology is",
    "Οι συγγενείς καρδιοπάθειες είναι οι συχνότερες συγγενείς ανωμαλίες. Ο "
    "εμβρυοκαρδιολόγος είναι ο παιδοκαρδιολόγος που εξειδικεύεται στον έλεγχο "
    "της καρδιάς του εμβρύου πριν…":
        "Congenital heart disease is the most common congenital abnormality. "
        "The fetal cardiologist is the pediatric cardiologist who specializes "
        "in examining the fetal heart before…",
    "Οι συγγενείς καρδιοπάθειες είναι οι συχνότερες συγγενείς ανωμαλίες. Ο "
    "εμβρυοκαρδιολόγος είναι ο παιδοκαρδιολόγος που εξειδικεύεται στον έλεγχο "
    "της καρδιάς του εμβρύου πριν από τη γέννηση, με στόχο την έγκαιρη διάγνωση "
    "και τον σωστό προγραμματισμό του τοκετού και της αντιμετώπισης.":
        "Congenital heart disease is the most common congenital abnormality. "
        "The fetal cardiologist is the pediatric cardiologist who specializes "
        "in examining the fetal heart before birth, with the aim of making an "
        "early diagnosis and planning the delivery and the management "
        "correctly.",
    "Πότε ζητείται εξειδικευμένος καρδιολογικός έλεγχος":
        "When a specialist cardiac assessment is requested",
    "Ύποπτο εύρημα στο υπερηχογράφημα Β' επιπέδου.":
        "A suspicious finding on the level II ultrasound.",
    "Οικογενειακό ιστορικό συγγενούς καρδιοπάθειας.":
        "A family history of congenital heart disease.",
    "Σακχαρώδης διαβήτης ή αυτοάνοσο νόσημα της μητέρας.":
        "Maternal diabetes mellitus or autoimmune disease.",
    "Λήψη ορισμένων φαρμάκων κατά την κύηση.":
        "Use of certain medications during pregnancy.",
    "Αυξημένη αυχενική διαφάνεια στο πρώτο τρίμηνο.":
        "Increased nuchal translucency in the first trimester.",
    "Διαταραχές του καρδιακού ρυθμού του εμβρύου.":
        "Fetal heart rhythm abnormalities.",
    "Δίδυμη ή πολύδυμη κύηση.": "Twin or higher-order multiple pregnancy.",
    "Γιατί έχει σημασία": "Why it matters",
    "Όταν μια σοβαρή καρδιοπάθεια διαγνωστεί προγεννητικά, ο τοκετός μπορεί να "
    "προγραμματιστεί σε κέντρο με παιδοκαρδιοχειρουργική υποστήριξη και η ομάδα "
    "που θα υποδεχθεί το νεογνό να είναι έτοιμη από την πρώτη στιγμή. Η διαφορά "
    "αυτή στην προετοιμασία είναι καθοριστική. Η ίδια η εξέταση περιγράφεται "
    "στην ενότητα Υπερηχογράφημα καρδιάς εμβρύου.":
        "When serious heart disease is diagnosed before birth, delivery can be "
        "planned at a center with pediatric cardiac surgery support, and the "
        "team receiving the newborn can be ready from the first moment. That "
        "difference in preparation is decisive. The examination itself is "
        "described in the Fetal Echocardiography section.",
}

FACILITIES = {
    "Δύο ιατρεία, ο ίδιος εξοπλισμός": "Two clinics, the same equipment",
    "Ο ιατρός δέχεται σε δύο ιατρεία: στη Λεωφόρο Βασιλίσσης Σοφίας 124Α στην "
    "Αθήνα και στην κεντρική πλατεία Νέας Σμύρνης, στην 25ης Μαρτίου 11. Και οι "
    "δύο χώροι είναι πλήρως…":
        "The doctor sees patients at two clinics: at 124A Vasilissis Sofias "
        "Avenue in Athens and on the central square of Nea Smyrni, at 11 25is "
        "Martiou. Both are fully…",
    "Ο ιατρός δέχεται σε δύο ιατρεία: στη Λεωφόρο Βασιλίσσης Σοφίας 124Α στην "
    "Αθήνα και στην κεντρική πλατεία Νέας Σμύρνης, στην 25ης Μαρτίου 11. Και οι "
    "δύο χώροι είναι πλήρως εξοπλισμένοι, ώστε να μπορείτε να επιλέγετε όποιον "
    "σας εξυπηρετεί χωρίς να αλλάζει τίποτα στην ποιότητα της εξέτασης.":
        "The doctor sees patients at two clinics: at 124A Vasilissis Sofias "
        "Avenue in Athens and on the central square of Nea Smyrni, at 11 25is "
        "Martiou. Both are fully equipped, so you can choose whichever suits "
        "you without anything changing in the quality of your care.",
    "Διαθέτουν σύγχρονα υπερηχογραφικά συστήματα για όλη τη γκάμα των "
    "μαιευτικών και γυναικολογικών εξετάσεων, καθώς και την υποδομή για τις "
    "επεμβάσεις που γίνονται στο ιατρείο, χωρίς νοσηλεία. Ο ιατρός δέχεται "
    "κατόπιν ραντεβού.":
        "They have modern ultrasound systems for the full range of obstetric "
        "and gynecological examinations, as well as the facilities for the "
        "procedures that are carried out in the office, without a hospital "
        "stay. The doctor sees patients by appointment.",
    "Δείτε παρακάτω φωτογραφίες, στοιχεία επικοινωνίας, τον χάρτη και τις "
    "εξετάσεις που πραγματοποιούνται σε κάθε ιατρείο.":
        "Below you will find photographs, contact details, the map and the "
        "examinations carried out at each clinic.",
    "Διαβάστε περισσότερα.": "Read more.",
}

CLINIC_PAGES = {
    "Ιατρείο Αθηνών: Λεωφόρος Βασιλίσσης Σοφίας 124Α, Αθήνα, Τ.Κ. 11526. Τηλ. "
    "210 771 7705. Μαιευτικές και γυναικολογικές εξετάσεις κατόπιν ραντεβού.":
        "Athens Clinic: 124A Vasilissis Sofias Avenue, Athens, 11526. Tel. 210 "
        "771 7705. Obstetric and gynecological examinations by appointment.",
    "Ιατρείο Νέας Σμύρνης: 25ης Μαρτίου 11, Νέα Σμύρνη, Τ.Κ. 17121. Τηλ. 210 "
    "934 3538. Μαιευτικές και γυναικολογικές εξετάσεις κατόπιν ραντεβού.":
        "Nea Smyrni Clinic: 11 25is Martiou, Nea Smyrni, 17121. Tel. 210 934 "
        "3538. Obstetric and gynecological examinations by appointment.",
    "EMBRYOCOSMOS Λεωφόρος Βασιλίσσης Σοφίας 124Α, Αθήνα, Τ.Κ. 11526. Άρτια "
    "εξοπλισμένος χώρος με σύγχρονα υπερηχογραφικά συστήματα για όλη τη γκάμα "
    "μαιευτικών και γυναικολογικών εξετάσεων.":
        "EMBRYOCOSMOS, 124A Vasilissis Sofias Avenue, Athens, 11526. A fully "
        "equipped space with modern ultrasound systems for the full range of "
        "obstetric and gynecological examinations.",
    "Κεντρική Πλατεία 25ης Μαρτίου 11, Νέα Σμύρνη, Τ.Κ. 17121. Άρτια "
    "εξοπλισμένος χώρος με σύγχρονα υπερηχογραφικά συστήματα για όλη τη γκάμα "
    "μαιευτικών και γυναικολογικών εξετάσεων.":
        "Central Square, 11 25is Martiou, Nea Smyrni, 17121. A fully equipped "
        "space with modern ultrasound systems for the full range of obstetric "
        "and gynecological examinations.",
    "Λεωφόρος Βασιλίσσης Σοφίας 124Α, Αθήνα, Τ.Κ. 11526. Τηλέφωνο ιατρείου 210 "
    "771 7705, κινητό 695 519 9198, e-mail mrotas@gmail.com. Ο ιατρός δέχεται "
    "κατόπιν ραντεβού.":
        "124A Vasilissis Sofias Avenue, Athens, 11526. Clinic telephone 210 771 "
        "7705, mobile 695 519 9198, e-mail mrotas@gmail.com. The doctor sees "
        "patients by appointment.",
    "25ης Μαρτίου 11, Νέα Σμύρνη, Τ.Κ. 17121. Τηλέφωνο ιατρείου 210 934 3538, "
    "κινητό 695 519 9198, e-mail mrotas@gmail.com. Ο ιατρός δέχεται κατόπιν "
    "ραντεβού.":
        "11 25is Martiou, Nea Smyrni, 17121. Clinic telephone 210 934 3538, "
        "mobile 695 519 9198, e-mail mrotas@gmail.com. The doctor sees patients "
        "by appointment.",
    "Καλέστε 210 771 7705": "Call 210 771 7705",
    "Καλέστε 210 934 3538": "Call 210 934 3538",
    "Οδηγίες στον χάρτη": "Directions on the map",
    "Ο χώρος": "The space",
    "Χάρτης Ιατρείο Αθηνών": "Map — Athens Clinic",
    "Χάρτης Ιατρείο Νέας Σμύρνης": "Map — Nea Smyrni Clinic",
    "Στοιχεία & πρόσβαση": "Details & access",
    "Εξετάσεις που πραγματοποιούνται": "Examinations carried out",
    "Γυναικολογική εξέταση Τεστ ΠΑΠ": "Gynecological examination — Pap test",
    "Τοποθέτηση σπιράλ": "IUD insertion",
    "Γυναικολογικό 3D υπερηχογράφημα": "Gynecological 3D ultrasound",
    "Κολποσκόπηση Βιοψία τραχήλου": "Colposcopy — cervical biopsy",
    "Καυτηριασμός κονδυλωμάτων Laser": "Laser cauterization of genital warts",
    "Υπερηχογράφημα Β’ Επιπέδου": "Level II ultrasound",
    "Υπερηχογράφημα κύησης Doppler": "Pregnancy ultrasound — Doppler",
    "Καρδιοτοκογράφημα ηρεμίας (NST)": "Non-stress test (NST)",
    "Λήψη τροφοβλάστης": "Chorionic villus sampling",
    "Υπερηχογράφημα μαστών": "Breast ultrasound",
    "Σονο-υστερο υπερηχογραφία": "Sonohysterography",
    "Σπερματέγχυση": "Intrauterine insemination",
}

STRINGS = {}
for _d in (SHARED, INDEX, QUALIFICATIONS, CV, TEAM, MIDWIFE, CARDIOLOGIST,
           FACILITIES, CLINIC_PAGES):
    STRINGS.update(_d)

PUBLICATIONS = {
    'ΕΠΙΛΕΓΜΕΝΕΣ ΔΗΜΟΣΙΕΥΣΕΙΣ ΣΕ ΔΙΕΘΝEIΣ ΙΑΤΡΙΚΕΣ ΕΠΙΘΕΩΡΗΣΕΙΣ ( JOYRNALS ) The effect of acute sleep deprivation and alcohol consumption on performance during simulated laparoscopic surgery. Obstet Gynecol. 2007 April Supplements Rotas M, McCalla S, Chunhua L, Minkoff H. Methicillin resistant Staphylococcus aureus necrotizing pneumonia arising from an infected episiotomy site. Obstet Gynecol. 2007; 109:533-6 Ashoor G, Maiz N, Rotas M, Jawdat F, Nicolaides KH. Maternal thyroid function at 11 to 13 weeks of gestation and spontaneous pretrm delivery. Obstet Gynecol. 2011 Feb;117(2 Pt 1):293-8 Haberman S, Rotas M, Perlman K, Feldman J. Variations in compliance with documentation using computerized obstetrical records. Obstet Gynecol. 2007 Jul; 110(1):141-5 Rotas M, Haberman S, Levgur M. Cesarean scar ectopic pregnancies: etiology, diagnosis, and management. Obstet Gynecol. 2006 Jun; 107(6):1373-81 Rotas M, Haberman S, Zaher M, Morcos M. Prenatal diagnosis of giant fetal truncal hemangioma by means of 2- and 3-dimensional sonography with magnetic resonance imaging. J Ultrasound Med. 2006 Apr; 25(4): 527-31 Ashoor G, Rotas M, Maiz N, Kametas NA, Nicolaides KH. Maternal thyroid function at 11-13 weeks of gestation in women with hypothyroidism treated by thyroxine. Fetal Diagn Ther. 2010 Jul; 28(1):22-7. Epub 2010 Jul 2 Ashoor G, Maiz N, Rotas M, Kametas NA, Nicolaides KH. and subsequent development of preeclampsia. Prenat Diagn. 2010 Nov; 30(11):1032-8. Awonuga AO, Shavell VI, Imudia AN, Rotas M, Diamond MP, Puscheck EE. Pathogenesis of benign metastasizing leiomyoma: a review Obstet Gynecol Surv. 2010 Mar; 65(3):189-95. Rotas M, Ossowski R, Lutchman G, Levgur M. Pregnancy complicated with a giant splenic cyst: a case report and review of the literature. Arch Gynecol Obstet. 2007 Apr; 275(4):301-5.':
        'SELECTED PUBLICATIONS IN INTERNATIONAL MEDICAL JOURNALS The effect of acute sleep deprivation and alcohol consumption on performance during simulated laparoscopic surgery. Obstet Gynecol. 2007 April Supplements Rotas M, McCalla S, Chunhua L, Minkoff H. Methicillin resistant Staphylococcus aureus necrotizing pneumonia arising from an infected episiotomy site. Obstet Gynecol. 2007; 109:533-6 Ashoor G, Maiz N, Rotas M, Jawdat F, Nicolaides KH. Maternal thyroid function at 11 to 13 weeks of gestation and spontaneous pretrm delivery. Obstet Gynecol. 2011 Feb;117(2 Pt 1):293-8 Haberman S, Rotas M, Perlman K, Feldman J. Variations in compliance with documentation using computerized obstetrical records. Obstet Gynecol. 2007 Jul; 110(1):141-5 Rotas M, Haberman S, Levgur M. Cesarean scar ectopic pregnancies: etiology, diagnosis, and management. Obstet Gynecol. 2006 Jun; 107(6):1373-81 Rotas M, Haberman S, Zaher M, Morcos M. Prenatal diagnosis of giant fetal truncal hemangioma by means of 2- and 3-dimensional sonography with magnetic resonance imaging. J Ultrasound Med. 2006 Apr; 25(4): 527-31 Ashoor G, Rotas M, Maiz N, Kametas NA, Nicolaides KH. Maternal thyroid function at 11-13 weeks of gestation in women with hypothyroidism treated by thyroxine. Fetal Diagn Ther. 2010 Jul; 28(1):22-7. Epub 2010 Jul 2 Ashoor G, Maiz N, Rotas M, Kametas NA, Nicolaides KH. and subsequent development of preeclampsia. Prenat Diagn. 2010 Nov; 30(11):1032-8. Awonuga AO, Shavell VI, Imudia AN, Rotas M, Diamond MP, Puscheck EE. Pathogenesis of benign metastasizing leiomyoma: a review Obstet Gynecol Surv. 2010 Mar; 65(3):189-95. Rotas M, Ossowski R, Lutchman G, Levgur M. Pregnancy complicated with a giant splenic cyst: a case report and review of the literature. Arch Gynecol Obstet. 2007 Apr; 275(4):301-5.',
}
STRINGS.update(PUBLICATIONS)

# gallery captions: "Ιατρείο Αθηνών χώρος 7"
for _n in range(1, 21):
    STRINGS[f"Ιατρείο Αθηνών χώρος {_n}"] = f"Athens Clinic — photo {_n}"
    STRINGS[f"Ιατρείο Νέας Σμύρνης χώρος {_n}"] = f"Nea Smyrni Clinic — photo {_n}"

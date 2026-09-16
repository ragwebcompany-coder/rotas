# -*- coding: utf-8 -*-
"""Gynecology — examination, screening, conditions, office procedures."""

REDIRECT_STUB = {
    "Η σελίδα μεταφέρθηκε | Ρώτας Μιχάλης MD, FACOG":
        "This page has moved | Dr. Michael Rotas MD, FACOG",
    "Η σελίδα μεταφέρθηκε": "This page has moved",
    "Η σελίδα μεταφέρθηκε. Αν δεν μεταφερθείτε αυτόματα,":
        "This page has moved. If you are not redirected automatically,",
    "πατήστε εδώ": "click here",
}

EXAM = {
    "Τι περιλαμβάνει ο τακτικός γυναικολογικός έλεγχος":
        "What the regular gynecological check-up involves",
    "Ο τακτικός γυναικολογικός έλεγχος είναι το βασικό εργαλείο πρόληψης για "
    "κάθε γυναίκα. Περιλαμβάνει τη λήψη ιστορικού, την κλινική εξέταση και, "
    "ανάλογα με την ηλικία και το…":
        "The regular gynecological check-up is the cornerstone of prevention "
        "for every woman. It includes taking a history, a clinical examination "
        "and, depending on your age and…",
    "Ο τακτικός γυναικολογικός έλεγχος είναι το βασικό εργαλείο πρόληψης για "
    "κάθε γυναίκα. Περιλαμβάνει τη λήψη ιστορικού, την κλινική εξέταση και, "
    "ανάλογα με την ηλικία και το ιστορικό σας, τις εξετάσεις πρόληψης του "
    "καρκίνου του τραχήλου και τον υπερηχογραφικό έλεγχο των έσω γεννητικών "
    "οργάνων.":
        "The regular gynecological check-up is the cornerstone of prevention "
        "for every woman. It includes taking a history, a clinical examination "
        "and — depending on your age and your history — cervical cancer "
        "screening and an ultrasound assessment of the internal reproductive "
        "organs.",
    "Στόχος δεν είναι μόνο η διάγνωση, αλλά και η έγκαιρη αναγνώριση "
    "αλλοιώσεων πριν αυτές δώσουν συμπτώματα. Οι επιμέρους εξετάσεις που "
    "συνθέτουν τον έλεγχο περιγράφονται αναλυτικά στις ενότητες που ακολουθούν.":
        "The aim is not only diagnosis but the early recognition of changes "
        "before they cause any symptoms. The individual tests that make up the "
        "check-up are described in detail in the sections that follow.",
}

CERVICAL = {
    "Ο τράχηλος είναι το κατώτερο, στενό τμήμα της μήτρας που προβάλλει στον "
    "κόλπο. Επειδή είναι άμεσα προσβάσιμος, επιτρέπει τον εντοπισμό αλλοιώσεων "
    "σε πολύ πρώιμο στάδιο,…":
        "The cervix is the lower, narrow part of the uterus that projects into "
        "the vagina. Because it is directly accessible, changes can be picked "
        "up at a very early stage,…",
    "Γιατί εξετάζεται ο τράχηλος της μήτρας": "Why the cervix is examined",
    "Ο τράχηλος είναι το κατώτερο, στενό τμήμα της μήτρας που προβάλλει στον "
    "κόλπο. Επειδή είναι άμεσα προσβάσιμος, επιτρέπει τον εντοπισμό αλλοιώσεων "
    "σε πολύ πρώιμο στάδιο, χρόνια πριν αυτές εξελιχθούν. Γι' αυτό ο έλεγχος "
    "του τραχήλου αποτελεί τον πυρήνα της πρόληψης του καρκίνου του τραχήλου "
    "της μήτρας.":
        "The cervix is the lower, narrow part of the uterus that projects into "
        "the vagina. Because it is directly accessible, changes can be picked "
        "up at a very early stage, years before they progress. That is why "
        "cervical screening is at the heart of preventing cancer of the cervix.",
    "Πώς γίνεται ο έλεγχος": "How screening is done",
    "Ο έλεγχος γίνεται κλιμακωτά και εξατομικεύεται με βάση την ηλικία, το "
    "ιστορικό και τα ευρήματα των προηγούμενων εξετάσεων:":
        "Screening is done in stages and is tailored to your age, your history "
        "and the findings of previous tests:",
    "Κλινική επισκόπηση του τραχήλου με κολποδιαστολέα, κατά τη γυναικολογική "
    "εξέταση.":
        "Visual inspection of the cervix with a speculum, during the "
        "gynecological examination.",
    "Τεστ Παπανικολάου, για την ανίχνευση κυτταρικών αλλοιώσεων.":
        "A Pap test, to detect cell changes.",
    "Έλεγχος για τον ιό HPV, όταν ενδείκνυται.":
        "HPV testing, where this is indicated.",
    "Κολποσκόπηση, όταν το τεστ ΠΑΠ ή ο έλεγχος HPV δώσουν παθολογικό "
    "αποτέλεσμα.":
        "Colposcopy, when the Pap test or the HPV test gives an abnormal "
        "result.",
    "Βιοψία τραχήλου, εφόσον κατά την κολποσκόπηση εντοπιστεί ύποπτη περιοχή.":
        "A cervical biopsy, if colposcopy shows a suspicious area.",
    "Η εξέταση είναι σύντομη και γίνεται στο ιατρείο. Ο ιατρός θα σας εξηγήσει "
    "ποια βήματα χρειάζονται στη δική σας περίπτωση και πότε πρέπει να "
    "επαναληφθεί ο έλεγχος.":
        "The examination is short and takes place in the office. Your doctor "
        "will explain which steps are needed in your case and when screening "
        "should be repeated.",
}

CONDITIONS_HUB = {
    "Στην ενότητα αυτή παρουσιάζονται οι παθήσεις που απασχολούν συχνότερα τις "
    "γυναίκες σε κάθε ηλικία, από την εφηβεία έως και μετά την εμμηνόπαυση: τι "
    "είναι, πώς…":
        "This section covers the conditions that most often affect women at "
        "every age, from adolescence through to after the menopause: what they "
        "are, how…",
    "Οι συχνότερες γυναικολογικές παθήσεις":
        "The most common gynecological conditions",
    "Στην ενότητα αυτή παρουσιάζονται οι παθήσεις που απασχολούν συχνότερα τις "
    "γυναίκες σε κάθε ηλικία, από την εφηβεία έως και μετά την εμμηνόπαυση: τι "
    "είναι, πώς εκδηλώνονται, πώς διαγιγνώσκονται και ποιες είναι οι σύγχρονες "
    "επιλογές αντιμετώπισης.":
        "This section covers the conditions that most often affect women at "
        "every age, from adolescence through to after the menopause: what they "
        "are, how they present, how they are diagnosed and what the current "
        "treatment options are.",
    "Πολλές από αυτές τις καταστάσεις είναι συχνές και αντιμετωπίσιμες, ιδίως "
    "όταν εντοπιστούν έγκαιρα. Επικοινωνήστε με το ιατρείο εάν παρατηρήσετε "
    "επίμονο πυελικό πόνο, αλλαγή στο πρότυπο της περιόδου σας, αιμορραγία "
    "εκτός περιόδου ή μετά την εμμηνόπαυση, ή οποιοδήποτε σύμπτωμα σας "
    "ανησυχεί.":
        "Many of these conditions are common and treatable, particularly when "
        "they are found early. Contact the clinic if you notice persistent "
        "pelvic pain, a change in your menstrual pattern, bleeding between "
        "periods or after the menopause, or any symptom that worries you.",
}

OFFICE = {
    "Ένα μέρος των γυναικολογικών πράξεων μπορεί σήμερα να γίνει με ασφάλεια "
    "στον χώρο του ιατρείου, χωρίς γενική αναισθησία και χωρίς νοσηλεία. Οι "
    "επεμβάσεις αυτές είναι…":
        "A number of gynecological procedures can now be carried out safely in "
        "the office, without general anesthesia and without a hospital stay. "
        "These procedures are…",
    "Επεμβάσεις χωρίς νοσηλεία": "Procedures without a hospital stay",
    "Ένα μέρος των γυναικολογικών πράξεων μπορεί σήμερα να γίνει με ασφάλεια "
    "στον χώρο του ιατρείου, χωρίς γενική αναισθησία και χωρίς νοσηλεία. Οι "
    "επεμβάσεις αυτές είναι σύντομες, γίνονται με τοπική αναισθησία όπου "
    "χρειάζεται, και η γυναίκα επιστρέφει στις δραστηριότητές της την ίδια "
    "ημέρα.":
        "A number of gynecological procedures can now be carried out safely in "
        "the office, without general anesthesia and without a hospital stay. "
        "They are short, done under local anesthesia where necessary, and you "
        "can return to your usual activities the same day.",
    "Και τα δύο ιατρεία διαθέτουν τον απαραίτητο εξοπλισμό για τις πράξεις που "
    "περιγράφονται παρακάτω. Ο ιατρός θα σας εξηγήσει τι περιλαμβάνει η κάθε "
    "επέμβαση, πώς προετοιμάζεστε και τι να περιμένετε μετά.":
        "Both clinics have the equipment needed for the procedures described "
        "below. Your doctor will explain what each one involves, how to "
        "prepare, and what to expect afterwards.",
}

IUI = {
    "Η ενδομήτρια σπερματέγχυση (IUI) είναι μια απλή μέθοδος υποβοηθούμενης "
    "αναπαραγωγής, κατά την οποία επεξεργασμένο σπέρμα τοποθετείται απευθείας "
    "μέσα στην κοιλότητα της…":
        "Intrauterine insemination (IUI) is a simple assisted reproduction "
        "technique in which prepared sperm is placed directly into the cavity "
        "of the…",
    "Τι είναι η ενδομήτρια σπερματέγχυση": "What intrauterine insemination is",
    "Η ενδομήτρια σπερματέγχυση (IUI) είναι μια απλή μέθοδος υποβοηθούμενης "
    "αναπαραγωγής, κατά την οποία επεξεργασμένο σπέρμα τοποθετείται απευθείας "
    "μέσα στην κοιλότητα της μήτρας, την ημέρα της ωορρηξίας. Με τον τρόπο αυτό "
    "αυξάνεται ο αριθμός των σπερματοζωαρίων που φτάνουν κοντά στο ωάριο.":
        "Intrauterine insemination (IUI) is a simple assisted reproduction "
        "technique in which prepared sperm is placed directly into the cavity "
        "of the uterus on the day of ovulation. This increases the number of "
        "sperm that reach the egg.",
    "Σε ποιες περιπτώσεις εφαρμόζεται": "When it is used",
    "Ήπιος ανδρικός παράγοντας υπογονιμότητας.": "Mild male factor infertility.",
    "Ανεξήγητη υπογονιμότητα.": "Unexplained infertility.",
    "Προβλήματα της τραχηλικής βλέννας.": "Problems with the cervical mucus.",
    "Διαταραχές ωορρηξίας, σε συνδυασμό με πρόκληση ωορρηξίας.":
        "Ovulation disorders, combined with ovulation induction.",
    "Χρήση σπέρματος δότη.": "Use of donor sperm.",
    "Απαραίτητη προϋπόθεση είναι τουλάχιστον η μία σάλπιγγα να είναι βατή και "
    "οι παράμετροι του σπέρματος να βρίσκονται εντός συγκεκριμένων ορίων.":
        "It is essential that at least one fallopian tube is patent and that "
        "the semen parameters are within certain limits.",
    "Η διαδικασία": "The procedure",
    "Ο κύκλος παρακολουθείται με υπερηχογραφήματα και ορμονικό έλεγχο, ώστε να "
    "προσδιοριστεί η κατάλληλη στιγμή. Η ίδια η σπερματέγχυση γίνεται στο "
    "ιατρείο, με λεπτό καθετήρα, διαρκεί λίγα λεπτά και είναι συνήθως ανώδυνη. "
    "Δεν απαιτείται αναισθησία ούτε ανάπαυση. Ο ιατρός θα σας εξηγήσει τα "
    "ποσοστά επιτυχίας για τη δική σας περίπτωση και τον αριθμό των κύκλων που "
    "έχει νόημα να δοκιμαστούν.":
        "The cycle is monitored with ultrasound scans and hormone tests to "
        "identify the right moment. The insemination itself is done in the "
        "office with a fine catheter, takes a few minutes and is usually "
        "painless. No anesthesia and no rest afterwards are needed. Your doctor "
        "will explain the success rates in your own case and how many cycles it "
        "makes sense to try.",
}

DYSMENORRHEA = {
    "Δυσμηνόρροια ονομάζεται ο πόνος που συνοδεύει την έμμηνο ρύση. Είναι η "
    "συχνότερη διαταραχή της περιόδου: περισσότερες από τις μισές γυναίκες που "
    "έχουν έμμηνο ρύση…":
        "Dysmenorrhea is the pain that accompanies menstruation. It is the "
        "commonest menstrual disorder: more than half of women who menstruate…",
    "Τι είναι η δυσμηνόρροια": "What dysmenorrhea is",
    "Δυσμηνόρροια ονομάζεται ο πόνος που συνοδεύει την έμμηνο ρύση. Είναι η "
    "συχνότερη διαταραχή της περιόδου: περισσότερες από τις μισές γυναίκες που "
    "έχουν έμμηνο ρύση εμφανίζουν πόνο για μία έως δύο ημέρες κάθε μήνα. Ο "
    "πόνος περιγράφεται συνήθως ως κράμπα στο κάτω μέρος της κοιλιάς και μπορεί "
    "να αντανακλά στη μέση ή στους μηρούς.":
        "Dysmenorrhea is the pain that accompanies menstruation. It is the "
        "commonest menstrual disorder: more than half of women who menstruate "
        "have pain for one to two days each month. The pain is usually "
        "described as cramping in the lower abdomen and can radiate to the "
        "lower back or the thighs.",
    "Πρωτοπαθής και δευτεροπαθής δυσμηνόρροια":
        "Primary and secondary dysmenorrhea",
    "Η διάκριση αυτή είναι που καθορίζει τη διερεύνηση και τη θεραπεία.":
        "This distinction is what determines the investigation and the "
        "treatment.",
    "Πρωτοπαθής δυσμηνόρροια: ο πόνος οφείλεται στην ίδια την περίοδο και όχι "
    "σε κάποια πάθηση. Προκαλείται από τις προσταγλανδίνες, ουσίες που "
    "παράγονται στο ενδομήτριο και προκαλούν συσπάσεις της μήτρας. Ξεκινά "
    "συνήθως λίγο μετά τις πρώτες περιόδους της εφηβείας, εμφανίζεται λίγο πριν "
    "ή με την έναρξη της ρύσης και υποχωρεί μέσα στις πρώτες ημέρες. Σε πολλές "
    "γυναίκες μειώνεται με την ηλικία και μετά από τοκετό.":
        "Primary dysmenorrhea: the pain is due to the period itself and not to "
        "any underlying condition. It is caused by prostaglandins, substances "
        "produced in the endometrium that make the uterus contract. It usually "
        "begins shortly after the first periods of adolescence, appears just "
        "before or as the period starts, and settles within the first few days. "
        "In many women it lessens with age and after childbirth.",
    "Δευτεροπαθής δυσμηνόρροια: ο πόνος οφείλεται σε υποκείμενη πάθηση του "
    "αναπαραγωγικού συστήματος. Εμφανίζεται συχνά αργότερα στη ζωή, ξεκινά "
    "μερικές ημέρες πριν από την περίοδο, επιδεινώνεται όσο αυτή εξελίσσεται "
    "και μπορεί να μην υποχωρεί με το τέλος της. Χαρακτηριστικά, τείνει να "
    "χειροτερεύει με τον χρόνο αντί να βελτιώνεται.":
        "Secondary dysmenorrhea: the pain is due to an underlying disorder of "
        "the reproductive system. It often appears later in life, starts a few "
        "days before the period, becomes worse as the period goes on and may "
        "not settle when it ends. Characteristically it tends to get worse over "
        "time rather than better.",
    "Ποιες παθήσεις προκαλούν δευτεροπαθή δυσμηνόρροια":
        "Which conditions cause secondary dysmenorrhea",
    "Ενδομητρίωση: ιστός όμοιος με το ενδομήτριο αναπτύσσεται εκτός μήτρας και "
    "αιμορραγεί στον ρυθμό των ορμονικών μεταβολών, προκαλώντας πόνο και "
    "συμφύσεις.":
        "Endometriosis: tissue similar to the lining of the uterus grows "
        "outside it and bleeds in step with hormonal changes, causing pain and "
        "adhesions.",
    "Αδενομύωση: ιστός του ενδομητρίου αναπτύσσεται μέσα στο μυϊκό τοίχωμα της "
    "μήτρας.":
        "Adenomyosis: endometrial tissue grows within the muscular wall of the "
        "uterus.",
    "Ινομυώματα, ιδίως όσα βρίσκονται μέσα στο τοίχωμα της μήτρας.":
        "Fibroids, particularly those within the wall of the uterus.",
    "Φλεγμονή της πυέλου και συμφύσεις μετά από λοίμωξη ή χειρουργείο.":
        "Pelvic inflammatory disease and adhesions following infection or "
        "surgery.",
    "Στένωση του τραχήλου ή συγγενείς ανωμαλίες της μήτρας.":
        "Cervical stenosis or congenital abnormalities of the uterus.",
    "Πώς διερευνάται": "How it is investigated",
    "Η διερεύνηση ξεκινά από το ιστορικό: πότε ξεκίνησε ο πόνος, πού "
    "εντοπίζεται, πώς συσχετίζεται χρονικά με την περίοδο, πόσο επηρεάζει την "
    "καθημερινότητά σας. Ακολουθεί γυναικολογική εξέταση και υπερηχογράφημα. "
    "Όταν τα ευρήματα το υποδεικνύουν, μπορεί να χρειαστεί λαπαροσκόπηση, η "
    "οποία επιτρέπει την άμεση επισκόπηση της πυέλου και, στην ίδια επέμβαση, "
    "την αντιμετώπιση ευρημάτων όπως η ενδομητρίωση.":
        "The investigation starts with the history: when the pain began, where "
        "it is, how it relates in time to the period, and how much it affects "
        "your daily life. A gynecological examination and an ultrasound scan "
        "follow. Where the findings suggest it, laparoscopy may be needed; this "
        "allows the pelvis to be inspected directly and, in the same operation, "
        "findings such as endometriosis to be treated.",
    "Η πρωτοπαθής δυσμηνόρροια ανταποκρίνεται συνήθως στα μη στεροειδή "
    "αντιφλεγμονώδη φάρμακα, τα οποία δρουν ακριβώς στις προσταγλανδίνες. Είναι "
    "πιο αποτελεσματικά όταν λαμβάνονται με τα πρώτα σημάδια του πόνου και όχι "
    "αφού αυτός εγκατασταθεί. Δεν είναι κατάλληλα για όλες τις γυναίκες, γι' "
    "αυτό η χορήγησή τους πρέπει να συζητηθεί με τον ιατρό σας.":
        "Primary dysmenorrhea usually responds to non-steroidal "
        "anti-inflammatory drugs, which act precisely on the prostaglandins. "
        "They are most effective when taken at the first sign of pain rather "
        "than once it is established. They are not suitable for every woman, so "
        "taking them should be discussed with your doctor.",
    "Οι ορμονικές μέθοδοι αντισύλληψης, όπως τα αντισυλληπτικά δισκία, το "
    "διαδερμικό έμπλαστρο, ο κολπικός δακτύλιος, το υποδόριο εμφύτευμα και το "
    "ορμονικό ενδομήτριο σπιράλ, μειώνουν επίσης τον πόνο και αποτελούν καλή "
    "επιλογή όταν επιθυμείτε ταυτόχρονα αντισύλληψη.":
        "Hormonal contraceptives — the pill, the transdermal patch, the vaginal "
        "ring, the subdermal implant and the hormonal intrauterine device — "
        "also reduce the pain and are a good option when you want contraception "
        "at the same time.",
    "Βοηθούν επιπλέον η τακτική σωματική άσκηση, ο επαρκής ύπνος, οι τεχνικές "
    "χαλάρωσης και η τοπική εφαρμογή θερμότητας. Όταν ο πόνος δεν υποχωρεί με "
    "φαρμακευτική αγωγή, η θεραπεία στρέφεται στην αιτία: αφαίρεση εστιών "
    "ενδομητρίωσης ή ινομυωμάτων, και σε σοβαρές περιπτώσεις που δεν "
    "ανταποκρίθηκαν σε τίποτε άλλο, υστερεκτομή ως έσχατη λύση.":
        "Regular exercise, enough sleep, relaxation techniques and local heat "
        "also help. When the pain does not settle with medication, treatment "
        "turns to the cause: removing endometriotic deposits or fibroids and, "
        "in severe cases that have not responded to anything else, hysterectomy "
        "as a last resort.",
    "Πότε να απευθυνθείτε στον ιατρό": "When to see your doctor",
    "Ο πόνος της περιόδου δεν είναι κάτι που πρέπει απλώς να αντέχετε. Κλείστε "
    "ραντεβού εάν ο πόνος σας εμποδίζει να πάτε στη δουλειά ή στο σχολείο, εάν "
    "επιδεινώνεται με τον χρόνο, εάν ξεκίνησε ή άλλαξε χαρακτήρα μετά τα 25, "
    "εάν δεν ανακουφίζεται με τα κοινά παυσίπονα, ή εάν συνοδεύεται από πόνο "
    "στη σεξουαλική επαφή, δυσκολία στη σύλληψη ή βαριά αιμορραγία.":
        "Period pain is not something you simply have to put up with. Make an "
        "appointment if the pain stops you going to work or school, if it is "
        "getting worse over time, if it began or changed in character after the "
        "age of 25, if it is not relieved by ordinary painkillers, or if it "
        "comes with pain during sex, difficulty conceiving or heavy bleeding.",
}

ENDOMETRIOSIS_EXTRA = {
    "Εάν ο πόνος είναι έντονος και δεν υποχωρήσει μετά τη θεραπεία, η "
    "υστερεκτομή μπορεί να είναι η «έσχατη λύση». Η ενδομητρίωση είναι λιγότερο "
    "πιθανό να επανέλθει εάν αφαιρεθούν επίσης οι ωοθήκες σας. Εάν διατηρήσετε "
    "τις ωοθήκες σας, η ενδομητρίωση είναι λιγότερο πιθανό να επανέλθει εάν τα "
    "εμφυτεύματα ενδομητρίωσης αφαιρεθούν την ίδια στιγμή που κάνετε "
    "υστερεκτομή. Υπάρχει μια μικρή πιθανότητα ο πόνος να επανέλθει ακόμα κι αν "
    "αφαιρεθεί η μήτρα και οι ωοθήκες σας. Αυτό μπορεί να οφείλεται σε "
    "ενδομητρίωση που δεν ήταν ορατή ή δεν μπορούσε να αφαιρεθεί τη στιγμή της "
    "επέμβασης.":
        "If the pain is severe and does not go away after treatment, "
        "hysterectomy may be a last resort. Endometriosis is less likely to "
        "come back if your ovaries are also removed. If you keep your ovaries, "
        "endometriosis is less likely to return if the endometriotic implants "
        "are removed at the same time as the hysterectomy. There is a small "
        "chance that the pain will return even if your uterus and ovaries are "
        "removed. This may be due to endometriosis that was not visible or "
        "could not be removed at the time of the operation.",
}

STRINGS = {}
for _d in (REDIRECT_STUB, EXAM, CERVICAL, CONDITIONS_HUB, OFFICE, IUI,
           DYSMENORRHEA, ENDOMETRIOSIS_EXTRA):
    STRINGS.update(_d)

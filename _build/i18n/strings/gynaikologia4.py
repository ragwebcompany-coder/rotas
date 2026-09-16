# -*- coding: utf-8 -*-
"""Gynecology, part four — PCOS, prolapse, Pap test, thrombophilia, IUD, biopsy."""

BLEEDING = {
    "Ως μη φυσιολογική χαρακτηρίζεται η αιμορραγία που εμφανίζεται σε "
    "οποιαδήποτε από τις ακόλουθες καταστάσεις:":
        "Bleeding is considered abnormal when it occurs in any of the following "
        "situations:",
    "Αιμορραγία μετά από την σεξουαλική επαφή": "Bleeding after intercourse",
    "Κηλίδες αίματος που εμφανίζονται οποιαδήποτε στιγμή στον εμμηνορροϊκό "
    "κύκλο": "Spotting at any time in the menstrual cycle",
    "Αιμορραγία πιο έντονη ή μεγαλύτερης διάρκειας από το κανονικό":
        "Bleeding that is heavier or lasts longer than normal",
    "Αιμορραγία μετά την εμμηνόπαυση": "Bleeding after the menopause",
    "Οι εμμηνορροϊκοί κύκλοι που είναι μεγαλύτεροι από 35 ημέρες ή μικρότεροι "
    "από 21 θεωρούνται επίσης μη φυσιολογικοί. Επίσης, η έλλειψη περιόδου για 3 "
    "6 μήνες (αμηνόρροια) είναι μη φυσιολογική.":
        "Menstrual cycles that are longer than 35 days or shorter than 21 days "
        "are also considered abnormal. The absence of periods for 3 to 6 months "
        "(amenorrhea) is abnormal as well.",
    "Κάποιες γυναίκες μπορεί να χρειαστεί να υποβληθούν σε χειρουργική επέμβαση "
    "για την αφαίρεση των ανώμαλων διαμορφώσεων που υπάρχουν (όπως πολύποδες ή "
    "ινομυώματα) και προκαλούν αιμορραγία. Τα ινομυώματα μπορούν να αφαιρεθούν "
    "με υστεροσκόπηση. Ωστόσο, μερικές φορές χρησιμοποιούνται άλλες τεχνικές. "
    "Για παράδειγμα, η αφαίρεση του ενδομητρίου μπορεί να χρησιμοποιηθεί για "
    "τον έλεγχο της αιμορραγίας. Η τεχνική αυτή, στοχεύει στο να σταματήσει ή "
    "να μειώσει μόνιμα την αιμορραγία. Προτού αποφασιστεί η αφαίρεση απαιτείται "
    "βιοψία του ενδομητρίου. Η υστερεκτομή μπορεί να γίνει όταν άλλες μορφές "
    "θεραπείας έχουν αποτύχει ή δεν αποτελούν ασφαλή επιλογή. Η υστερεκτομή "
    "αποτελεί μια πολύ σημαντική χειρουργική επέμβαση. Μετά από αυτή, μια "
    "γυναίκα δεν έχει πλέον περίοδο και δεν μπορεί να μείνει έγκυος.":
        "Some women may need surgery to remove the abnormal growths (such as "
        "polyps or fibroids) that are causing the bleeding. Fibroids can be "
        "removed by hysteroscopy, although other techniques are sometimes used. "
        "Endometrial ablation, for example, may be used to control bleeding; "
        "this technique aims to stop or permanently reduce the bleeding. An "
        "endometrial biopsy is required before ablation is decided on. "
        "Hysterectomy may be done when other forms of treatment have failed or "
        "are not a safe option. Hysterectomy is a major operation. Afterwards a "
        "woman no longer has periods and cannot become pregnant.",
}

PCOS = {
    "Το Σύνδρομο Πολυκυστικών Ωοθηκών (Polycystic Ovary Syndrome, PCOS) είναι "
    "μια κατάσταση που επηρεάζει τον κύκλο μιας γυναίκας, τις ορμόνες της, τη "
    "γονιμότητα, αλλά και την…":
        "Polycystic ovary syndrome (PCOS) is a condition that affects a woman's "
        "cycle, her hormones, her fertility and also her…",
    "Το Σύνδρομο Πολυκυστικών Ωοθηκών (Polycystic Ovary Syndrome, PCOS) είναι "
    "μια κατάσταση που επηρεάζει τον κύκλο μιας γυναίκας, τις ορμόνες της, τη "
    "γονιμότητα, αλλά και την εμφάνισή της.":
        "Polycystic ovary syndrome (PCOS) is a condition that affects a woman's "
        "cycle, her hormones, her fertility and also her appearance.",
    "Το σύνδρομο πολυκυστικών ωοθηκών είναι μια από τις συχνές αιτίες "
    "υπογονιμότητας. Οι ασθενείς με το σύνδρομο πολυκυστικών ωοθηκών έχουν "
    "πολλές μικρές κύστες στις ωοθήκες τους, οι οποίες προκύπτουν από τη "
    "διακοπή της φυσιολογικής πορείας του κύκλου (ανάπτυξη και ωρίμανση ενός "
    "ωοθυλακίου, ωορρηξία). Η ωοθήκη τότε μεγεθύνεται και παράγει μεγάλες "
    "ποσότητες ορμονών (ανδρογόνα και οιστρογόνα), οι οποίες, σε συνδυασμό με "
    "το γεγονός ότι δε γίνεται ωορρηξία, προκαλούν υπογονιμότητα. Εξαιτίας "
    "αυτής της ανισορροπίας στις ορμόνες οι γυναίκες με πολυκυστικές ωοθήκες "
    "είναι στατιστικά πιο επιρρεπείς σε πολύποδες, ινομυώματα και ενδομητρίωση.":
        "Polycystic ovary syndrome is one of the common causes of infertility. "
        "Women with the syndrome have many small cysts in their ovaries, which "
        "arise because the normal course of the cycle — the growth and "
        "maturation of a follicle, then ovulation — is interrupted. The ovary "
        "then enlarges and produces large amounts of hormones (androgens and "
        "estrogens) which, combined with the fact that ovulation does not "
        "occur, cause infertility. Because of this hormonal imbalance, women "
        "with polycystic ovaries are statistically more prone to polyps, "
        "fibroids and endometriosis.",
    "Είκοσι (20) στις 100 γυναίκες (20%) έχουν πολυκυστικές ωοθήκες. Στην "
    "Ελλάδα αυτό το ποσοστό είναι ίσως λίγο μεγαλύτερο. Είναι πολύ σημαντικό να "
    "τονίσουμε ότι εάν μια γυναίκα έχει πολυκυστικές ωοθήκες δε σημαίνει "
    "απαραίτητα ότι έχει και Σύνδρομο Πολυκυστικών Ωοθηκών. Μόνο 6-7% των "
    "γυναικών με πολυκυστικές ωοθήκες έχει και το Σύνδρομο. Όσες γυναίκες έχουν "
    "το Σύνδρομο Πολυκυστικών Ωοθηκών έχουν πιο έντονα συμπτώματα και άλλα "
    "προβλήματα υγείας.":
        "Twenty out of every 100 women (20%) have polycystic ovaries. In Greece "
        "the proportion is perhaps slightly higher. It is very important to "
        "stress that having polycystic ovaries does not necessarily mean having "
        "polycystic ovary syndrome. Only 6–7% of women with polycystic ovaries "
        "also have the syndrome. Those who do have more pronounced symptoms and "
        "other health problems.",
    "ΑΙΤΙΟΛΟΓΙΑ": "CAUSES",
    "Η αιτία του Συνδρόμου δεν είναι ξεκάθαρη. Μερικές φορές έχει σχέση με την "
    "κληρονομικότητα: αν κάποια συγγενής σας (μητέρα, θεία, αδερφή) έχει το "
    "Σύνδρομο, τότε είναι αυξημένη η πιθανότητα να εμφανίσετε και εσείς.":
        "The cause of the syndrome is not clear. Sometimes it is inherited: if "
        "a female relative of yours (mother, aunt, sister) has the syndrome, "
        "your own chance of developing it is higher.",
    "ΣΥΜΤΩΜΑΤΟΛΟΓΙΑ": "SYMPTOMS",
    "Τα συμπτώματα διαφέρουν από γυναίκα σε γυναίκα. Η βαρύτητα των συμπτωμάτων "
    "διαφέρει: κάποιες γυναίκες έχουν ελαφριά συμπτώματα, κάποιες άλλες πιο "
    "έντονα.Στις πιο πολλές γυναίκες που έχουν πολυκυστικές ωοθήκες "
    "παρατηρούνται ήπια ή αμελητέα συμπτώματα. Μόνο σε βαριά περιστατικά που "
    "έχουν το Σύνδρομο παρατηρούνται οι έντονες ορμονικές διαταραχές και άλλα "
    "προβλήματα υγείας.Τα κυριότερα από τα συμπτώματα είναι τα πιο κάτω:":
        "Symptoms vary from woman to woman, as does their severity: some women "
        "have mild symptoms, others more pronounced ones. In most women with "
        "polycystic ovaries the symptoms are mild or negligible. It is only in "
        "severe cases of the syndrome that marked hormonal disturbances and "
        "other health problems are seen. The main symptoms are as follows:",
    "• ακανόνιστη περίοδος ή καθόλου περίοδος • δυσκολία για επίτευξη "
    "εγκυμοσύνης (υπογονιμότητα), γιατί η γυναίκα δεν παράγει ωάρια ή δε "
    "γνωρίζει τις γόνιμες μέρες της • πολλαπλές αποβολές • αυξημένη τριχοφυΐα "
    "στο πρόσωπο ή το σώμα • αυξημένο βάρος, ταχύτατη αύξηση του βάρους, "
    "δυσκολία για απώλεια βάρους • λιπαρό δέρμα, ακμή • σε βαριά περιστατικά: "
    "ανδρικού τύπου κατανομή λίπους (κοιλιά, λεπτά πόδια) • αλλαγές στη διάθεση":
        "• irregular periods, or no periods at all • difficulty conceiving "
        "(infertility), because the woman does not produce eggs or does not "
        "know her fertile days • repeated miscarriages • increased hair growth "
        "on the face or body • weight gain, rapid weight gain, difficulty "
        "losing weight • oily skin, acne • in severe cases, a male pattern of "
        "fat distribution (abdomen, slim legs) • mood changes",
    "Οι γυναίκες με πολυκυστικές ωοθήκες, εκτός των συμπτωμάτων που "
    "παρουσιάζουν, εάν δεν ακολουθήσουν την κατάλληλη θεραπεία, έχουν μεγαλύτερη "
    "πιθανότητα να αναπτύξουν υπέρταση, καρδιοπάθειες, σακχαρώδη διαβήτη τύπου "
    "ΙΙ, καθώς επίσης και άλλες παθήσεις, που είναι άμεσα εξαρτώμενες από το "
    "ορμονικό τους σύστημα, όπως ινομυώματα, υπερπλασία του ενδομητρίου και "
    "ενδομητρίωση. Ακόμη, πολλές φορές οι πολυκυστικές ωοθήκες συνδυάζονται με "
    "υπέρταση, σακχαρώδη διαβήτη, υπογονιμότητα, αποβολές ή παχυσαρκία στο "
    "οικογενειακό ιστορικό.":
        "Besides the symptoms they experience, women with polycystic ovaries "
        "who do not receive appropriate treatment are more likely to develop "
        "high blood pressure, heart disease and type II diabetes, as well as "
        "other conditions that depend directly on their hormonal system, such "
        "as fibroids, endometrial hyperplasia and endometriosis. Polycystic "
        "ovaries are also often associated with a family history of high blood "
        "pressure, diabetes, infertility, miscarriage or obesity.",
    "Συμπτώματα αναλυτικά:": "The symptoms in detail:",
    "Προβλήματα στην ωορρηξία: ανωορρηξία (καθόλου ωορρηξία) ή ολιγο-ωορρηξία "
    "(ακατανόνιστη ή σε αραιά διαστήματα).":
        "Ovulation problems: anovulation (no ovulation at all) or "
        "oligo-ovulation (irregular or infrequent ovulation).",
    "Ακανόνιστος κύκλος (εξαιτίας της ακανόνιστης ωορρηξίας): αμηνόρροια "
    "(καθόλου περίοδος), ολιγομηνόρροια (σε αραιά διαστήματα, κάθε 2-3 μήνες), "
    "υπερ-μηνόρροια (περίοδος που έρχεται πολύ συχνά), μηνορραγία (έντονη "
    "αιμορραγία ή αιμορραγία που διαρκεί για πολλές μέρες ή εβδομάδες) ή "
    "αιμορραγία ενδιάμεσα από τις κανονικές περιόδους.":
        "An irregular cycle (because ovulation is irregular): amenorrhea (no "
        "periods), oligomenorrhea (infrequent periods, every 2–3 months), "
        "polymenorrhea (periods that come very often), menorrhagia (heavy "
        "bleeding, or bleeding that lasts many days or weeks) or bleeding "
        "between normal periods.",
    "Αντίσταση στην ινσουλίνη: το σώμα δεν αντιδρά στην ινσουλίνη φυσιολογικά. "
    "Η κύρια λειτουργία της ινσουλίνης είναι ο έλεγχος των επιπέδων του σακχάρου "
    "στο αίμα. Αυτό μπορεί να φανεί σε κάποιες εργαστηριακές εξετάσεις, π.χ. "
    "υψηλά επίπεδα ινσουλίνης νηστείας, χαμηλή αναλογία σακχάρου /ινσουλίνης, "
    "υψηλά επίπεδα τριγλυκεριδίων, χαμηλά επίπεδα SHBG (Steroid Hormone Binding "
    "Globulin).":
        "Insulin resistance: the body does not respond to insulin normally. The "
        "main function of insulin is to control blood sugar levels. This can "
        "show up on certain laboratory tests — for example high fasting insulin "
        "levels, a low glucose/insulin ratio, high triglyceride levels and low "
        "levels of SHBG (steroid hormone binding globulin).",
    "Υπερανδρογονισμός: τα ανδρογόνα είναι οι λεγόμενες «ανδρικές» ορμόνες. "
    "Αυτό όμως είναι λάθος: όλοι, άντρες και γυναίκες, έχουμε ανδρογόνα. Απλά "
    "στους άντρες τα ανδρογόνα υπάρχουν σε πολύ υψηλότερα επίπεδα σε σχέση με "
    "τις γυναίκες. Οι γυναίκες με σύνδρομο πολυκυστικών ωοθηκών έχουν ελαφρώς "
    "αυξημένα επίπεδα ανδρογόνων, τα οποία προκαλούν τα πιο κάτω συμπτώματα:":
        "Hyperandrogenism: androgens are the so-called male hormones. That is "
        "misleading, however: everyone, men and women alike, has androgens. It "
        "is simply that in men they are present at much higher levels than in "
        "women. Women with polycystic ovary syndrome have slightly raised "
        "androgen levels, which cause the following symptoms:",
    "• Υπερβολική τριχοφυΐα: συνήθως στο πρόσωπο (άνω χείλος, μάγουλα, πηγούνι, "
    "λαιμό) ή στο σώμα (στέρνο, κοιλιά, πλάτη). • Ακμή. • Αλωπεκία: τα μαλλιά "
    "αραιώνουν όπως συμβαίνει και στους άντρες.":
        "• Excess hair growth: usually on the face (upper lip, cheeks, chin, "
        "neck) or the body (chest, abdomen, back). • Acne. • Alopecia: the hair "
        "thins in the same way as it does in men.",
    "Οι εργαστηριακές ορμονικές εξετάσεις που συνήθως προτείνονται για τη "
    "διάγνωση του υπερανδρογονισμού είναι οι εξής:":
        "The hormone tests usually recommended to diagnose hyperandrogenism are "
        "as follows:",
    "• Ολική και ελεύθερη τεστοστερόνη • Δι-υδροτεστοστερόνη (DHT) • "
    "Ανδροστενενδιόνη • Θειϊκή δι-υδροεπιανδροστερόνη (DHEA-S)":
        "• Total and free testosterone • Dihydrotestosterone (DHT) • "
        "Androstenedione • Dehydroepiandrosterone sulfate (DHEA-S)",
    "Οι γυναίκες με σύνδρομο πολυκυστικών ωοθηκών εμφανίζουν υψηλά επίπεδα σε "
    "κάποιες από αυτές τις εξετάσεις.":
        "Women with polycystic ovary syndrome have raised levels on some of "
        "these tests.",
    "Υπερηχογράφημα: στις γυναίκες με σύνδρομο πολυκυστικών ωοθηκών "
    "παρατηρούνται τα εξής:":
        "Ultrasound: in women with polycystic ovary syndrome the following are "
        "seen:",
    "• Διογκωμένες ωοθήκες (όγκος ωοθηκών >10ml), • Μεγάλος αριθμός (>12) "
    "μικρών ωοθυλακίων (διάμετρος 2-9mm) ακριβώς κάτω από την επιφάνεια της "
    "ωοθήκες (στην περιφέρεια), • Στο κέντρο της ωοθήκης υπάρχουν πολύ λίγα "
    "ωοθυλάκια παχύ ωοθηκικό στρώμα (όχι απαραίτητα).":
        "• Enlarged ovaries (ovarian volume >10 ml) • A large number (>12) of "
        "small follicles (2–9 mm in diameter) just beneath the surface of the "
        "ovary, at the periphery • Very few follicles in the centre of the "
        "ovary, with dense ovarian stroma (though not necessarily).",
    "Πολλές γυναίκες μπορεί να έχουν πολυκυστικές ωοθήκες χωρίς να έχουν "
    "Σύνδρομο Πολυκυστικών Ωοθηκών, δηλαδή τα ευρήματα στο υπερηχογράφημα δεν "
    "είναι αρκετά για να γίνει η διάγνωση.":
        "Many women can have polycystic ovaries without having polycystic ovary "
        "syndrome — in other words, the ultrasound findings alone are not "
        "enough to make the diagnosis.",
    "Άλλα ευρήματα: σε κάποιες γυναίκες με σύνδρομο πολυκυστικών ωοθηκών μπορεί "
    "να συνυπάρχουν τα πιο κάτω:":
        "Other findings: some women with polycystic ovary syndrome may also "
        "have the following:",
    "• Αυξημένα επίπεδα προλακτίνης (και ένα μικρό μυστικό: ο έλεγχος "
    "προλακτίνη είναι προτιμότερο να μη γίνεται πολύ νωρίς το πρωί, δεδομένου "
    "ότι τείνει να είναι αυξημένα τα επίπεδα καλύτερα να γίνεται στις 10- 12 το "
    "πρωί) • Υψηλά επίπεδα LH • Υψηλή τιμή της αναλογίας LH: FSH • Υψηλά "
    "επίπεδα της AMH (αντι-μυλλέριος ορμόνη, anti-mullerian hormone)":
        "• Raised prolactin levels (and a small tip: it is better not to "
        "measure prolactin very early in the morning, since levels tend to be "
        "higher then — between 10 a.m. and midday is better) • High LH levels • "
        "A high LH:FSH ratio • High levels of AMH (anti-Müllerian hormone)",
    "Πιθανά προβλήματα υγείας που σχετίζονται με το σύνδρομο πολυκυστικών "
    "ωοθηκών":
        "Possible health problems associated with polycystic ovary syndrome",
    "Οι γυναίκες με σύνδρομο πολυκυστικών ωοθηκών εμφανίζουν κάποια προβλήματα "
    "υγείας πιο συχνά από τον υπόλοιπο πληθυσμό είτε γιατί αυτά προκαλούνται "
    "από το σύνδρομο είτε γιατί έχουν το ίδιο υποκείμενο αίτιο με το σύνδρομο:":
        "Women with polycystic ovary syndrome have certain health problems more "
        "often than the rest of the population, either because the syndrome "
        "causes them or because they share the same underlying cause:",
    "• Υπέρταση • Σακχαρώδης διαβήτης τύπου ΙΙ • Προβλήματα στα στεφανιαία "
    "αγγεία • Καρκίνος του ενδομητρίου (κάθε αίτιο που δημιουργεί προβλήματα "
    "στην ωορρηξία της γυναίκας σχετίζεται με αυξημένο κίνδυνο για καρκίνο του "
    "ενδομητρίου).":
        "• High blood pressure • Type II diabetes • Coronary artery disease • "
        "Endometrial cancer (any cause of ovulation problems is associated with "
        "an increased risk of endometrial cancer).",
    "Διαβάστε εδώ περισσότερα για τον τρόπο με τον οποίο σήμερα θεωρείται ότι "
    "το Σύνδρομο Πολυκυστικών Ωοθηκών επηρεάζει την υγεία σύμφωνα με τη "
    "Συναινετική Δήλωση (Consensus Statement) των ESHRE (European Society of "
    "Human Reproduction and Embryology) και ASRM (American Society for "
    "Reproductive Medicine):":
        "Read more here about how polycystic ovary syndrome is currently "
        "considered to affect health, according to the consensus statement of "
        "ESHRE (European Society of Human Reproduction and Embryology) and ASRM "
        "(American Society for Reproductive Medicine):",
    "‘Revised 2003 consensus on diagnostic criteria and longterm health risks "
    "related to polycystic ovary syndrome (PCOS)’ The Rotterdam ESHRE/"
    "ASRM-sponsored PCOS consensus workshop group Human Reproduction 2004 "
    "19(1):41-47 Πιθανά προβλήματα κατά τη διάρκεια της εγκυμοσύνης στις "
    "γυναίκες με σύνδρομο πολυκυστικών ωοθηκών":
        "'Revised 2003 consensus on diagnostic criteria and long-term health "
        "risks related to polycystic ovary syndrome (PCOS)', The Rotterdam "
        "ESHRE/ASRM-sponsored PCOS consensus workshop group, Human Reproduction "
        "2004 19(1):41-47. Possible problems during pregnancy in women with "
        "polycystic ovary syndrome",
    "• Διαβήτης κατά τη διάρκεια της εγκυμοσύνης • Υπέρταση λόγω εγκυμοσύνης • "
    "Προεκλαμψία • Πρόωρος τοκετός • Αυξημένος κίνδυνος για εισαγωγή του "
    "νεογνού σε μονάδα εντατικής θεραπείας.":
        "• Diabetes during pregnancy • Pregnancy-induced high blood pressure • "
        "Preeclampsia • Preterm birth • An increased risk that the newborn will "
        "be admitted to intensive care.",
    "ΔΙΑΓΝΩΣΗ": "DIAGNOSIS",
    "Οι πολυκυστικές ωοθήκες μπορούν να διαγνωστούν με ένα υπερηχογράφημα και "
    "με ορμονικό προσδιορισμό συγκεκριμένων ορμονών μέσω μίας εξέτασης αίματος "
    "στην αρχή του κύκλου. Το μεγάλο πρόβλημα που αντιμετωπίζουν μέχρι σήμερα "
    "οι γυναίκες με πολυκυστικές ωοθήκες, είναι ότι οι περισσότεροι γιατροί "
    "προσπαθούν να θεραπεύσουν ένα σύμπτωμα, π.χ. την ακμή, το λιπαρό δέρμα, "
    "την ανωορρηξία κ.λ.π., και όχι την ίδια την ασθένεια.":
        "Polycystic ovaries can be diagnosed with an ultrasound scan and by "
        "measuring particular hormones in a blood test at the beginning of the "
        "cycle. The great problem women with polycystic ovaries have faced "
        "until now is that most doctors try to treat a symptom — acne, oily "
        "skin, anovulation and so on — rather than the condition itself.",
    "Το Σύνδρομο των Πολυκυστικών Ωοθηκών είναι εύκολο να διαγνωστεί σε κάποιες "
    "ασθενείς. Συνήθως στο ιστορικό αυτών των ασθενών αναφέρεται ο ακανόνιστος "
    "και απρόβλεπτος κύκλος, ο οποίος μπορεί να συνοδεύεται με έντονη "
    "αιμορραγία. Οι ασθενείς είναι συχνά υπέρβαρες με παραπάνω τριχοφυΐα (στο "
    "σώμα και στο πρόσωπο) εξαιτίας των υψηλών επιπέδων ανδρογόνων. Κάποιες "
    "ασθενείς όμως μπορεί να μην έχουν τα παραπάνω συμπτώματα.":
        "Polycystic ovary syndrome is easy to diagnose in some patients. Their "
        "history usually includes an irregular, unpredictable cycle, which may "
        "be accompanied by heavy bleeding. They are often overweight, with "
        "excess hair on the body and face because of high androgen levels. Some "
        "patients, however, may not have these symptoms.",
    "Η διάγνωση επιβεβαιώνεται με κολπικό υπερηχογράφημα, στο οποίο φαίνεται "
    "ότι και οι δύο ωοθήκες είναι διογκωμένες και ότι υπάρχουν πολλές μικρές "
    "κύστες που συνήθως εντοπίζονται στην περιφέρεια της ωοθήκες.":
        "The diagnosis is confirmed with a transvaginal ultrasound, which shows "
        "that both ovaries are enlarged and that there are many small cysts, "
        "usually at the periphery of the ovary.",
    "Όσον αφορά στο ορμονικό προφίλ αυτών των γυναικών, στα βαριά περιστατικά "
    "συνήθως ανιχνεύονται υψηλά επίπεδα ανδρογόνων (θειϊκή δε-υδρο "
    "επιανδροστερόνη, DHEA-S) και LH. Η FSH είναι σε φυσιολογικά επίπεδα. Αυτή "
    "η αναλογία των ορμονών FSH και LH είναι χαρακτηριστική για το Σύνδρομο "
    "Πολυκυστικών Ωοθηκών. Πολλές ασθενείς με το Σύνδρομο έχουν επίσης υψηλά "
    "επίπεδα ινσουλίνης, γιατί εμφανίζουν αντίσταση στην ινσουλίνη.":
        "As for the hormone profile of these women, in severe cases high levels "
        "of androgens (dehydroepiandrosterone sulfate, DHEA-S) and of LH are "
        "usually found. FSH is at normal levels. This ratio between FSH and LH "
        "is characteristic of polycystic ovary syndrome. Many patients with the "
        "syndrome also have high insulin levels, because they are insulin "
        "resistant.",
    "Δεν είναι ξεκάθαρο τι προκαλεί το σύνδρομο πολυκυστικών ωοθηκών. Όμως "
    "ξέρουμε με σιγουριά ότι η χαρακτηριστική πολυκυστική ωοθήκη προκύπτει μετά "
    "από μια παρατεταμένη περίοδο ανωορρηξίας. Οι ασθενείς αυτές έχουν υψηλά "
    "επίπεδα ανδρογόνων και LH, τα οποία τροφοδοτούν περαιτέρω το πρόβλημα και "
    "έτσι δημιουργείται ένας φαύλος κύκλος. Η παχυσαρκία επιδεινώνει το "
    "σύνδρομο πολυκυστικών ωοθηκών γιατί ο λιπώδης ιστός εκκρίνει οιστρογόνα, "
    "τα οποία διακόπτουν την ωορρηξία.":
        "It is not clear what causes polycystic ovary syndrome. We do know for "
        "certain, however, that the characteristic polycystic ovary develops "
        "after a prolonged period without ovulation. These patients have high "
        "levels of androgens and LH, which feed the problem further and create "
        "a vicious circle. Obesity makes polycystic ovary syndrome worse, "
        "because fatty tissue secretes estrogens, which interrupt ovulation.",
    "Διαβάστε εδώ περισσότερα για τον τρόπο με τον οποίο σήμερα γίνεται η "
    "διάγνωση του Συνδρόμου Πολυκυστικών Ωοθηκών σύμφωνα με τη Συναινετική "
    "Δήλωση (Consensus Statement) των ESHRE (European Society of Human "
    "Reproduction and Embryology) και ASRM (American Society for Reproductive "
    "Medicine):":
        "Read more here about how polycystic ovary syndrome is diagnosed today, "
        "according to the consensus statement of ESHRE (European Society of "
        "Human Reproduction and Embryology) and ASRM (American Society for "
        "Reproductive Medicine):",
    "ΘΕΡΑΠΕΙΑ": "TREATMENT",
    "Σήμερα, υπάρχει τρόπος θεραπείας για τις πολυκυστικές ωοθήκες, με φάρμακα "
    "ή χειρουργική επέμβαση. Η θεραπευτική προσέγγιση για το σύνδρομο "
    "πολυκυστικών ωοθηκών εξαρτάται από τα συμπτώματα κάθε γυναίκας και τον "
    "πρωτεύοντα στόχο στη δεδομένη χρονική στιγμή της ζωής της, π.χ. θεραπεία "
    "ακμής ή υπερβολικής τριχοφυΐας, θεραπεία υπογονιμότητας, αντιμετώπιση "
    "άλλων προβλημάτων υγείας λόγω του συνδρόμου.Για τις γυναίκες που "
    "προσπαθούν να επιτύχουν μία εγκυμοσύνη, η επίτευξή της, με ή χωρίς "
    "πρόκληση ωορρηξίας, είναι ό,τι χρειάζεται. Για τις γυναίκες που "
    "ταλαιπωρούνται από τα παραπάνω συμπτώματα, η ενδεδειγμένη θεραπεία θα "
    "αποφασιστεί μετά από την διεξαγωγή εργαστηριακών και αιματολογικών "
    "εξετάσεων. Η θεραπεία του συνδρόμου πολυκυστικών ωοθηκών για τη θεραπεία "
    "της υπογονιμότητας εστιάζεται στην πρόκληση ωορρηξίας προκειμένου να "
    "μπορέσει η γυναίκα να συλλάβει.":
        "Polycystic ovaries can be treated today, with medication or with "
        "surgery. The therapeutic approach depends on each woman's symptoms and "
        "on her primary goal at that point in her life — treating acne or "
        "excess hair growth, treating infertility, or managing other health "
        "problems caused by the syndrome. For women who are trying to conceive, "
        "achieving a pregnancy, with or without ovulation induction, is all "
        "that is needed. For women troubled by the symptoms above, the "
        "appropriate treatment is decided after laboratory and blood tests. "
        "Treatment of polycystic ovary syndrome for infertility focuses on "
        "inducing ovulation so that the woman can conceive.",
    "Απώλεια βάρους και άσκηση": "Weight loss and exercise",
    "Για πολλές ασθενείς, η απώλεια βάρους είναι από μόνη της μια αποτελεσματική "
    "θεραπεία. Η καλύτερη στρατηγική είναι η απώλεια σταδιακά, αλλά σταθερά, με "
    "σκοπό το μόνιμο αποτέλεσμα. Οι απότομες και πολύ αυστηρές δίαιτες που "
    "σοκάρουν τον οργανισμό δεν είναι αποτελεσματικές. Στην προσπάθεια για "
    "απώλεια βάρους μπορεί να χρειαστείτε τη βοήθεια ενός διαιτολόγου. Σίγουρα "
    "η άσκηση επίσης βοηθάει, γιατί γίνεται καλύτερα ο μεταβολισμός του "
    "σακχάρου. Αεροβικές δραστηριότητες όπως το περπάτημα, το τρέξιμο ή το "
    "κολύμπι είναι καλές επιλογές.":
        "For many patients, losing weight is by itself an effective treatment. "
        "The best strategy is to lose weight gradually but steadily, aiming for "
        "a lasting result. Crash diets and very strict regimes that shock the "
        "body are not effective. You may need the help of a dietitian. Exercise "
        "certainly helps too, because glucose is metabolized better. Aerobic "
        "activities such as walking, running or swimming are good choices.",
    "Αντίσταση στην ινσουλίνη": "Insulin resistance",
    "Σήμερα γνωρίζουμε ότι πολλές ασθενείς με Σύνδρομο Πολυκυστικών Ωοθηκών "
    "εμφανίζουν αντίσταση στην ινσουλίνη. Αυτό συμβαίνει και στους διαβητικούς, "
    "δηλαδή έχουν υψηλά επίπεδα ινσουλίνης στο αίμα (υπερ-ινσουλιναιμία), αλλά "
    "η απόκριση του οργανισμού στην ινσουλίνη είναι μειωμένη. Σε αυτές τις "
    "γυναίκες χορηγείται φαρμακευτική αγωγή (αντι-διαβητικά φάρμακα) και αυτό "
    "βοηθάει να αποκατασταθεί η ορμονική ισορροπία και να βελτιωθεί η ωορρηξία "
    "τους.":
        "We now know that many patients with polycystic ovary syndrome are "
        "insulin resistant. The same happens in people with diabetes: insulin "
        "levels in the blood are high (hyperinsulinemia) but the body's "
        "response to insulin is reduced. These women are given medication "
        "(anti-diabetic drugs), which helps restore hormonal balance and "
        "improve ovulation.",
    "Χειρουργική επέμβαση": "Surgery",
    "Σε κάποιες περιπτώσεις είναι απαραίτητη η λαπαροσκόπηση για τη θεραπεία "
    "του Συνδρόμου Πολυκυστικών Ωοθηκών. Κατά τη διάρκεια της λαπαροσκόπησης "
    "γίνεται καυτηριασμός των ωοθηκών, δηλαδή αφαιρείται ο ιστός των ωοθηκών "
    "που έχει υποστεί αλλοιώσεις με στόχο να αποκατασταθεί η φυσιολογική "
    "λειτουργία των ωοθηκών και να προκληθεί ωορρηξία. Η λαπαροσκόπηση είναι "
    "απαραίτητη όταν έχουν αποτύχει άλλοι τρόποι πρόκλησης ωορρηξίας.Μετά από "
    "μια τέτοια επέμβαση, περίπου 80% των ασθενών έχουν φυσιολογικό κύκλο και "
    "το 50% από αυτές θα συλλάβουν μέσα σε διάστημα 1 έτους χωρίς επιπλέον "
    "φαρμακευτική αγωγή ή άλλη θεραπεία. Μια επιπλοκή αυτής της επέμβασης όμως "
    "είναι ο σχηματισμός συμφύσεων.":
        "In some cases laparoscopy is needed to treat polycystic ovary "
        "syndrome. During the laparoscopy the ovaries are cauterized — that is, "
        "the abnormal ovarian tissue is removed, with the aim of restoring "
        "normal ovarian function and inducing ovulation. Laparoscopy is "
        "necessary when other ways of inducing ovulation have failed. After "
        "such an operation about 80% of patients have a normal cycle and 50% of "
        "them will conceive within 1 year without further medication or other "
        "treatment. One complication of the operation, however, is the "
        "formation of adhesions.",
}

PROLAPSE = {
    "Υπάρχουν πολλοί τύποι πρόπτωσης:": "There are several types of prolapse:",
    "Πρόπτωση μήτρας Η μήτρα πέφτει στον κόλπο.":
        "Uterine prolapse — the uterus drops into the vagina.",
    "Πρόπτωση κολπικού θόλου Η κορυφή του κόλπου (ο κολπικός θόλος) πέφτει. "
    "Αυτό το πρόβλημα εμφανίζεται συχνότερα σε γυναίκες που έχουν υποβληθεί σε "
    "υστερεκτομή.":
        "Vaginal vault prolapse — the top of the vagina (the vaginal vault) "
        "drops. This problem occurs most often in women who have had a "
        "hysterectomy.",
    "Κυστεοκήλη Η ουροδόχος κύστη πέφτει από τη φυσιολογική της θέση στον κόλπο.":
        "Cystocele — the bladder drops from its normal position into the "
        "vagina.",
    "Ουρηθροκήλη Η ουρηθροκήλη εμφανίζεται όταν η ουρήθρα διογκώνεται στην "
    "περιοχή του κόλπου. Συχνά εμφανίζεται παράλληλα με την κυστεοκήλη.":
        "Urethrocele — this occurs when the urethra bulges into the vagina. It "
        "often occurs together with a cystocele.",
    "Εντεροκήλη Το λεπτό έντερο πιέζει το πίσω τοίχωμα του κόλπου, δημιουργώντας "
    "ένα εξόγκωμα. Η εντεροκήλη εμφανίζεται συχνά σε συνδυασμό με την πρόπτωση "
    "του κολπικού θόλου.":
        "Enterocele — the small bowel presses on the back wall of the vagina, "
        "creating a bulge. An enterocele often occurs together with vaginal "
        "vault prolapse.",
    "Ορθοκήλη -Το ορθό διογκώνεται μέσα ή έξω από τον κόλπο.":
        "Rectocele — the rectum bulges into or out of the vagina.",
    "Αλλαγές στον τρόπο ζωής Εάν η ακράτεια είναι πρόβλημα, ο περιορισμός της "
    "πρόσληψης υγρών, συμπεριλαμβανομένων των ροφημάτων που περιέχουν καφεΐνη "
    "(ένα διουρητικό), μπορεί να είναι χρήσιμος. Οι γυναίκες με εντερικά "
    "προβλήματα πιθανώς να διαπιστώσουν ότι η αύξηση της ποσότητας των φυτικών "
    "ινών στη διατροφή τους αποτρέπει τη δυσκοιλιότητα και την καταπόνηση κατά "
    "τη διάρκεια των κενώσεων. Μερικές φορές συνταγογραφείται καθαρτικό ή "
    "φάρμακο που μαλακώνει τα κόπρανα.":
        "Lifestyle changes — if incontinence is a problem, limiting fluid "
        "intake, including drinks containing caffeine (a diuretic), can help. "
        "Women with bowel problems may find that increasing the amount of fibre "
        "in their diet prevents constipation and straining during bowel "
        "movements. A laxative or a stool softener is sometimes prescribed.",
    "Εκπαίδευση ουροδόχου κύστης Σε αυτή τη μορφή θεραπείας, θα αδειάζετε την "
    "κύστη σας σε προγραμματισμένες ώρες. Η θεραπεία αυτή ίσως να είναι χρήσιμη "
    "σε γυναίκες με ακράτεια.":
        "Bladder training — in this form of treatment you empty your bladder at "
        "scheduled times. It may be helpful for women with incontinence.",
    "Απώλεια βάρους Εάν είστε υπέρβαρες ή παχύσαρκες, η απώλεια βάρους μπορεί "
    "να βοηθήσει στη βελτίωση της συνολικής υγείας σας και πιθανώς των "
    "συμπτωμάτων της πρόπτωσης.":
        "Weight loss — if you are overweight or obese, losing weight can help "
        "improve your overall health and possibly your prolapse symptoms.",
    "Ασκήσεις Kegel Αυτές οι ασκήσεις ενισχύουν τους μύες που περιβάλλουν τα "
    "ανοίγματα της ουρήθρας, του κόλπου και του ορθού. Κάνοντας αυτές τις "
    "ασκήσεις τακτικά μπορεί να βελτιώσετε την ακράτεια.":
        "Kegel exercises — these strengthen the muscles that surround the "
        "openings of the urethra, vagina and rectum. Doing them regularly can "
        "improve incontinence.",
    "Πεσσοί Ο πεσσός είναι μια συσκευή που εισάγεται στον κόλπο για να στηρίξει "
    "τα πυελικά όργανα. Ο γυναικολόγος μπορεί να βοηθήσει στην εύρεση του "
    "κατάλληλου πεσσού που ταιριάζει και σας είναι βολικός.":
        "Pessaries — a pessary is a device inserted into the vagina to support "
        "the pelvic organs. Your gynecologist can help find a pessary that fits "
        "well and is comfortable for you.",
    "Πιέστε τους μύες που χρησιμοποιείτε για να σταματήσετε τη ροή των ούρων. "
    "Αυτή η σύσπαση τραβάει τον κόλπο και το ορθό πάνω και πίσω.":
        "Squeeze the muscles you would use to stop the flow of urine. This "
        "contraction pulls the vagina and rectum up and back.",
    "Κρατήστε το για έως και 10 δευτερόλεπτα και, στη συνέχεια, αφήστε το.":
        "Hold for up to 10 seconds, then release.",
    "Κάντε 50 ασκήσεις την ημέρα για 4–6 εβδομάδες.":
        "Do 50 exercises a day for 4–6 weeks.",
    "Βεβαιωθείτε ότι δεν πιέζετε τους μυς του στομάχου, των μηρών ή των γλουτών "
    "σας. Θα πρέπει επίσης να αποφύγετε να κρατάτε την αναπνοή σας καθώς κάνετε "
    "αυτές τις ασκήσεις.":
        "Make sure you are not tightening your stomach, thigh or buttock "
        "muscles. You should also avoid holding your breath while doing these "
        "exercises.",
    "Ορισμένα προβλήματα στήριξης της πυέλου μπορεί να διορθωθούν με "
    "χειρουργική επέμβαση για την αποκατάσταση του φυσιολογικού βάθους και της "
    "λειτουργίας του κόλπου. Συμπτώματα όπως ο πόνος στην πλάτη, η πυελική "
    "πίεση και η επώδυνη σεξουαλική επαφή μπορεί να μην ανακουφιστούν μέσω της "
    "χειρουργικής επέμβασης για την αποκατάσταση της πρόπτωσης. Ωστόσο, οι "
    "πιθανότητες να περιορίσετε τα προβλήματα είναι αρκετά υψηλές. Η πρόπτωση "
    "μπορεί να επαναληφθεί μετά την επέμβαση. Οι παράγοντες που προκάλεσαν "
    "πρόπτωση σε μια γυναίκα εξαρχής μπορεί να την επαναλάβουν.":
        "Some pelvic support problems can be corrected with surgery to restore "
        "the normal depth and function of the vagina. Symptoms such as back "
        "pain, pelvic pressure and painful intercourse may not be relieved by "
        "surgery to repair prolapse. The chances of reducing the problems are, "
        "however, quite high. Prolapse can recur after the operation: the "
        "factors that caused a woman's prolapse in the first place may cause it "
        "again.",
}

PAP = {
    "ΤΕΣΤ ΠΑΠΑΝΙΚΟΛΑΟΥ": "THE PAP TEST",
    "Θα πρέπει να ξεκινήσετε να κάνετε τεστ Παπ στην ηλικία των 21 ετών. Το "
    "πόσο συχνά πρέπει να κάνετε τεστ Παπανικολάου εξαρτάται από την ηλικία και "
    "το ιστορικό της υγείας σας:":
        "You should start having Pap tests at age 21. How often you should have "
        "a Pap test depends on your age and your health history:",
    "Γυναίκες κάτω των 30 ετών πρέπει να κάνουν τεστ Παπ κάθε 2 χρόνια.":
        "Women under 30 should have a Pap test every 2 years.",
    "Γυναίκες ηλικίας 30 ετών και άνω πρέπει να κάνουν τεστ Παπ κάθε 2 χρόνια. "
    "Μετά από τρία συνεχόμενα φυσιολογικά αποτελέσματα του τεστ Παπ, μια "
    "γυναίκα αυτής της ηλικιακής ομάδας μπορεί να κάνει τεστ Παπ κάθε 3 χρόνια "
    "εάν:":
        "Women aged 30 and over should have a Pap test every 2 years. After "
        "three consecutive normal Pap test results, a woman in this age group "
        "can have a Pap test every 3 years if:",
    "δεν έχει ιστορικό ήπιας ή σοβαρής δυσπλασίας.":
        "she has no history of mild or severe dysplasia.",
    "δεν έχει μολυνθεί από τον ιό της ανθρώπινης ανοσοανεπάρκειας (HIV).":
        "she is not infected with the human immunodeficiency virus (HIV).",
    "το ανοσοποιητικό της σύστημα δεν είναι εξασθενημένο (για παράδειγμα, εάν "
    "έχει υποβληθεί σε μεταμόσχευση οργάνου).":
        "her immune system is not weakened (for example, if she has had an "
        "organ transplant).",
    "δεν είχε εκτεθεί σε διαιθυλοστιλβεστρόλη (DES) πριν από τον τοκετό.":
        "she was not exposed to diethylstilbestrol (DES) before birth.",
    "Όπως συμβαίνει με κάθε εργαστηριακό τεστ, τα αποτελέσματα του τεστ Παπ δεν "
    "είναι πάντα ακριβή. Μερικές φορές, τα αποτελέσματα δείχνουν μη φυσιολογικά "
    "κύτταρα όταν τα κύτταρα είναι φυσιολογικά. Αυτό ονομάζεται «ψευδώς θετικό» "
    "αποτέλεσμα. Το τεστ Παπ μπορεί επίσης να μην ανιχνεύσει μη φυσιολογικά "
    "κύτταρα όταν υπάρχουν. Αυτό ονομάζεται «ψευδώς αρνητικό» αποτέλεσμα. "
    "Πολλοί παράγοντες μπορούν να προκαλέσουν ψευδή αποτελέσματα:":
        "As with any laboratory test, Pap test results are not always accurate. "
        "Sometimes the results show abnormal cells when the cells are normal. "
        "This is called a false positive result. The Pap test may also fail to "
        "detect abnormal cells when they are present. This is called a false "
        "negative result. Many factors can cause false results:",
    "Το δείγμα μπορεί να περιέχει πολύ λίγα κύτταρα.":
        "The sample may contain too few cells.",
    "Μπορεί να μην υπάρχουν αρκετά μη φυσιολογικά κύτταρα για μελέτη.":
        "There may not be enough abnormal cells to study.",
    "Μια μόλυνση ή αίμα μπορεί να κρύβει μη φυσιολογικά κύτταρα.":
        "An infection or blood may hide abnormal cells.",
    "Τα κολπικά φάρμακα μπορεί να ξεπλύνουν ή να αραιώσουν τα μη φυσιολογικά "
    "κύτταρα.":
        "Vaginal medications may wash away or dilute abnormal cells.",
    "Ο γιατρός σας μπορεί να προτείνει επανάληψη του τεστ Παπ για να ελέγξει τα "
    "αποτελέσματα. Μια επαναλαμβανόμενη δοκιμή αυξάνει την πιθανότητα "
    "ανίχνευσης μη φυσιολογικών κυττάρων, στην περίπτωση που υπάρχουν.":
        "Your doctor may suggest repeating the Pap test to check the results. A "
        "repeat test increases the chance of detecting abnormal cells if they "
        "are present.",
}

THROMBOPHILIA = {
    "Θρομβοφιλία ονομάζεται η αυξημένη τάση του αίματος να σχηματίζει θρόμβους. "
    "Δεν πρόκειται για μία νόσο, αλλά για μια ομάδα καταστάσεων που διαταράσσουν "
    "την ισορροπία…":
        "Thrombophilia is an increased tendency of the blood to form clots. It "
        "is not a single disease but a group of conditions that upset the "
        "balance…",
    "Τι είναι οι θρομβοφιλίες": "What thrombophilias are",
    "Θρομβοφιλία ονομάζεται η αυξημένη τάση του αίματος να σχηματίζει θρόμβους. "
    "Δεν πρόκειται για μία νόσο, αλλά για μια ομάδα καταστάσεων που διαταράσσουν "
    "την ισορροπία ανάμεσα στην πήξη και στη διάλυση των θρόμβων. Η ύπαρξη "
    "θρομβοφιλίας δεν σημαίνει ότι θα εμφανίσετε θρόμβωση. Σημαίνει ότι ο "
    "κίνδυνος είναι μεγαλύτερος, ιδίως όταν προστεθούν και άλλοι παράγοντες.":
        "Thrombophilia is an increased tendency of the blood to form clots. It "
        "is not a single disease but a group of conditions that upset the "
        "balance between clot formation and clot breakdown. Having a "
        "thrombophilia does not mean you will develop a thrombosis. It means "
        "the risk is higher, particularly when other factors are added.",
    "Κληρονομικές και επίκτητες": "Inherited and acquired",
    "Κληρονομικές: οφείλονται σε γενετικές μεταλλάξεις που κληρονομούνται από "
    "τους γονείς. Στις συχνότερες περιλαμβάνονται η μετάλλαξη Leiden του "
    "παράγοντα V, η μετάλλαξη της προθρομβίνης, καθώς και οι ανεπάρκειες της "
    "αντιθρομβίνης, της πρωτεΐνης C και της πρωτεΐνης S.":
        "Inherited: due to genetic mutations passed on from the parents. The "
        "commonest include factor V Leiden, the prothrombin mutation, and "
        "deficiencies of antithrombin, protein C and protein S.",
    "Επίκτητες: εμφανίζονται κατά τη διάρκεια της ζωής. Η σημαντικότερη στη "
    "γυναικολογία είναι το αντιφωσφολιπιδικό σύνδρομο, ένα αυτοάνοσο νόσημα που "
    "σχετίζεται τόσο με θρομβώσεις όσο και με επιπλοκές της κύησης.":
        "Acquired: these develop during life. The most important in gynecology "
        "is antiphospholipid syndrome, an autoimmune disease associated both "
        "with thrombosis and with complications of pregnancy.",
    "Γιατί αφορά τη γυναικολογία": "Why it matters in gynecology",
    "Ορισμένες συνηθισμένες καταστάσεις της γυναικείας ζωής αυξάνουν από μόνες "
    "τους την πηκτικότητα του αίματος. Όταν συνυπάρχει θρομβοφιλία, ο "
    "συνδυασμός έχει σημασία:":
        "Certain ordinary situations in a woman's life increase the clotting "
        "tendency of the blood by themselves. When a thrombophilia is also "
        "present, the combination matters:",
    "Λήψη ορμονικών αντισυλληπτικών που περιέχουν οιστρογόνα.":
        "Taking hormonal contraceptives that contain estrogen.",
    "Ορμονική θεραπεία υποκατάστασης στην εμμηνόπαυση.":
        "Hormone replacement therapy at the menopause.",
    "Εγκυμοσύνη και ιδίως η περίοδος της λοχείας.":
        "Pregnancy, and particularly the postpartum period.",
    "Θεραπείες υποβοηθούμενης αναπαραγωγής.":
        "Assisted reproduction treatments.",
    "Ακινησία μετά από χειρουργική επέμβαση ή παρατεταμένο ταξίδι.":
        "Immobility after surgery or during long journeys.",
    "Πότε συνιστάται έλεγχος": "When testing is recommended",
    "Ο έλεγχος θρομβοφιλίας δεν είναι εξέταση ρουτίνας και δεν έχει νόημα να "
    "γίνεται αδιακρίτως. Συζητείται όταν υπάρχει:":
        "Thrombophilia testing is not a routine investigation and there is no "
        "point in doing it indiscriminately. It is considered when there is:",
    "Ατομικό ιστορικό φλεβικής θρόμβωσης ή πνευμονικής εμβολής, ιδίως σε νεαρή "
    "ηλικία ή χωρίς προφανή αφορμή.":
        "A personal history of venous thrombosis or pulmonary embolism, "
        "particularly at a young age or with no obvious trigger.",
    "Θρόμβωση που εμφανίστηκε υπό αντισυλληπτικά, σε εγκυμοσύνη ή στη λοχεία.":
        "A thrombosis that occurred while taking contraceptives, during "
        "pregnancy or in the postpartum period.",
    "Οικογενειακό ιστορικό θρομβοφιλίας ή θρομβοεμβολικής νόσου σε συγγενή "
    "πρώτου βαθμού.":
        "A family history of thrombophilia or thromboembolic disease in a "
        "first-degree relative.",
    "Ιστορικό επαναλαμβανόμενων αποβολών ή σοβαρών επιπλοκών προηγούμενης "
    "κύησης.":
        "A history of recurrent miscarriage or of serious complications in a "
        "previous pregnancy.",
    "Τι σημαίνει ένα θετικό αποτέλεσμα": "What a positive result means",
    "Ένα θετικό εύρημα δεν οδηγεί αυτόματα σε αγωγή. Οδηγεί σε σχεδιασμό: "
    "επανεκτίμηση της μεθόδου αντισύλληψης, προληπτικά μέτρα σε περιόδους "
    "αυξημένου κινδύνου, και σε συγκεκριμένες περιπτώσεις αντιπηκτική αγωγή, "
    "πάντοτε σε συνεργασία με αιματολόγο. Η αντιμετώπιση κατά τη διάρκεια της "
    "εγκυμοσύνης περιγράφεται στην ενότητα Θρομβοφιλίες της Μαιευτικής.":
        "A positive finding does not automatically lead to treatment. It leads "
        "to planning: reviewing your contraceptive method, preventive measures "
        "during periods of increased risk and, in specific cases, "
        "anticoagulation — always in collaboration with a hematologist. "
        "Management during pregnancy is described in the Thrombophilia section "
        "under Obstetrics.",
}

IUD_EXTRA = {
    "Η χρήση του IUD έχει τα ακόλουθα οφέλη:":
        "Using an IUD has the following benefits:",
    "Είναι εύκολο στη χρήση. Μόλις τοποθετηθεί, δεν χρειάζεται να κάνετε τίποτα "
    "άλλο για να αποτρέψετε την εγκυμοσύνη.":
        "It is easy to use. Once it is in place, you do not need to do anything "
        "else to prevent pregnancy.",
    "Δεν παρεμβαίνει στην σεξουαλική επαφή ή στις καθημερινές δραστηριότητες. "
    "Μπορείτε να χρησιμοποιήσετε ταμπόν ενώ έχετε το σπιράλ.":
        "It does not interfere with sexual intercourse or daily activities. You "
        "can use tampons while you have an IUD.",
    "Μπορεί να τοποθετηθεί αμέσως μετά τον τοκετό και κατά τον θηλασμό.":
        "It can be inserted immediately after childbirth and while "
        "breastfeeding.",
    "Είναι εύκολα αναστρέψιμο. Εάν επιθυμείτε να μείνετε έγκυος, απλώς "
    "αφαιρέστε το IUD.":
        "It is easily reversible. If you want to become pregnant, the IUD is "
        "simply removed.",
    "Το ορμονικό IUD μπορεί να βοηθήσει στη μείωση του πόνου της περιόδου και "
    "της έντονης αιμορραγίας της περιόδου.":
        "The hormonal IUD can help reduce period pain and heavy menstrual "
        "bleeding.",
    "Καλέστε τον γυναικολόγο σας εάν έχετε κάποιο από τα ακόλουθα συμπτώματα:":
        "Call your gynecologist if you have any of the following symptoms:",
    "Έντονος πυελικός πόνος": "Severe pelvic pain",
    "Ανεξήγητος πυρετός": "Unexplained fever",
    "Πόνος κατά τη διάρκεια της σεξουαλικής επαφής":
        "Pain during sexual intercourse",
    "Σημάδια εγκυμοσύνης, όπως η απώλεια της εμμήνου ρύσεως (αν και μία από τις "
    "παρενέργειες του ορμονικού IUD είναι η έλλειψη εμμήνου ρύσεως, την πρώτη "
    "φορά που χάνετε μια έμμηνο ρύση θα πρέπει να αναφέρετε στον γυναικολόγο "
    "σας)":
        "Signs of pregnancy, such as a missed period (although one of the side "
        "effects of the hormonal IUD is the absence of periods, you should tell "
        "your gynecologist the first time you miss one)",
    "Ασυνήθιστη κολπική έκκριση": "Unusual vaginal discharge",
    "Το IUD μπορεί να γίνει αισθητό στον τράχηλο ή στον κόλπο":
        "The IUD can be felt at the cervix or in the vagina",
    "Μην προσπαθήσετε να αφαιρέσετε μόνοι σας ένα IUD. Ένα σπιράλ πρέπει να "
    "αφαιρεθεί από τον γιατρό.":
        "Do not try to remove an IUD yourself. An IUD must be removed by a "
        "doctor.",
}

ENDOMETRIAL_BIOPSY = {
    "Η βιοψία ενδομητρίου είναι η λήψη μικρού δείγματος ιστού από τον "
    "βλεννογόνο που επενδύει το εσωτερικό της μήτρας, ώστε να εξεταστεί στο "
    "μικροσκόπιο. Είναι η βασική εξέταση…":
        "An endometrial biopsy is the taking of a small sample of tissue from "
        "the lining of the uterus so that it can be examined under the "
        "microscope. It is the key investigation…",
    "Τι είναι η βιοψία ενδομητρίου": "What an endometrial biopsy is",
    "Η βιοψία ενδομητρίου είναι η λήψη μικρού δείγματος ιστού από τον "
    "βλεννογόνο που επενδύει το εσωτερικό της μήτρας, ώστε να εξεταστεί στο "
    "μικροσκόπιο. Είναι η βασική εξέταση για τη διερεύνηση της παθολογίας του "
    "ενδομητρίου και πραγματοποιείται στο ιατρείο, χωρίς νοσηλεία.":
        "An endometrial biopsy is the taking of a small sample of tissue from "
        "the lining of the uterus so that it can be examined under the "
        "microscope. It is the key investigation for endometrial pathology and "
        "is carried out in the office, without a hospital stay.",
    "Μη φυσιολογική αιμορραγία της μήτρας.": "Abnormal uterine bleeding.",
    "Παχυσμένο ενδομήτριο στο υπερηχογράφημα.":
        "A thickened endometrium on ultrasound.",
    "Διερεύνηση υπογονιμότητας ή επαναλαμβανόμενων αποβολών.":
        "Investigation of infertility or recurrent miscarriage.",
    "Παρακολούθηση υπό ορμονική αγωγή, όταν αυτό κρίνεται απαραίτητο.":
        "Monitoring during hormone treatment, where this is considered "
        "necessary.",
    "Με λεπτό εύκαμπτο καθετήρα, που εισάγεται μέσω του τραχήλου, λαμβάνεται "
    "δείγμα ενδομητρίου. Η εξέταση διαρκεί λίγα λεπτά. Μπορεί να νιώσετε "
    "κράμπες, παρόμοιες με αυτές της περιόδου, οι οποίες υποχωρούν γρήγορα. "
    "Ελαφρά αιμόρροια για μία έως δύο ημέρες είναι αναμενόμενη. Το αποτέλεσμα "
    "της ιστολογικής εξέτασης καθορίζει τα επόμενα βήματα.":
        "A sample of endometrium is taken with a fine flexible catheter passed "
        "through the cervix. The examination takes a few minutes. You may feel "
        "cramping, similar to period pain, which settles quickly. Light "
        "bleeding for one to two days is to be expected. The result of the "
        "histological examination determines the next steps.",
}

CYST_EXTRA = {
    "Τα συμπτώματά σας": "Your symptoms",
    "Η επιθυμία σας να κάνετε παιδιά": "Your wish to have children",
    "Μερικές φορές, μια κύστη μπορεί να αφαιρεθεί χωρίς να χρειάζεται να "
    "αφαιρεθεί η ωοθήκη. Αυτή η επέμβαση ονομάζεται κυστεκτομή. Σε άλλες "
    "περιπτώσεις, μπορεί να χρειαστεί να αφαιρεθεί η μία ή και οι δύο ωοθήκες. "
    "Ο γιατρός σας μπορεί να μην γνωρίζει ποια διαδικασία χρειάζεται μέχρι να "
    "ξεκινήσει η χειρουργική επέμβαση.":
        "Sometimes a cyst can be removed without removing the ovary. This "
        "operation is called a cystectomy. In other cases one or both ovaries "
        "may need to be removed. Your doctor may not know which procedure is "
        "needed until the operation has begun.",
}

STRINGS = {}
for _d in (BLEEDING, PCOS, PROLAPSE, PAP, THROMBOPHILIA, IUD_EXTRA,
           ENDOMETRIAL_BIOPSY, CYST_EXTRA):
    STRINGS.update(_d)

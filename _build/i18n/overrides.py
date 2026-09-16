# -*- coding: utf-8 -*-
"""Hand-checked corrections to the automatic GR↔EN alignment.

Every heading pair produced by harvest.py was proofread; the ones the scorer
got wrong are listed here.  FORCE adds a pair the scorer rejected but which is
genuinely the same heading; REJECT blocks a pair it accepted but which is not.
SKIP_PAGES names Greek pages that are a *rewrite* of the English original
rather than a translation of it — there is nothing safe to recover there, so
they are translated by hand instead.
"""

FORCE = {
    "Ποια είναι η διαδικασία της κολποσκόπησης;":
        "How is the procedure performed?",
    "Πόσο επιτυχημένος είναι ο εξωτερικός μετασχηματισμός εμβρύου;":
        "How successful is ECV?",
    "Υπάρχει εξέταση για να εκτιμηθεί αν είμαι φορέας της κυστικής ίνωσης;":
        "Can I be tested to assess whether I am a CF carrier?",
    "Χρειάζεται θεραπεία μετά από μια αποβολή;":
        "Is treatment needed after a miscarriage?",
    "Εάν κινδυνεύω να αποκτήσω μωρό με εκ γενετής ελάττωμα, ποιες εξετάσεις μπορούν να γίνουν;":
        "If I am at risk of having a baby with a birth defect, what tests may be performed?",
    "Τι είναι ο φυσιολογικός τοκετός μετά από καισαρική τομή;":
        "What is a vaginal birth after cesarean delivery (VBAC)?",
}

REJECT = {
    # the English original has no second-trimester section — this is new text
    "Ποιες εξετάσεις περιλαμβάνονται στον έλεγχο του δεύτερου τριμήνου για συγγενείς ανωμαλίες;",
    # page title in caps, not a section heading
    "ΦΥΣΙΟΛΟΓΙΚΟΣ ΤΟΚΕΤΟΣ ΜΕΤΑ ΑΠΟ ΚΑΙΣΑΡΙΚΗ",
    # a lead-in line, paired against the question heading above it
    "Υπάρχουν διάφοροι τύποι ακράτειας ούρων:",
}

SKIP_PAGES = {
    "gynaikologia/dysminorroia.html",            # condensed rewrite
    "gynaikologia/gynaikologiko-ypirixografima.html",
    "maieftiki/loxeia-kai-thilasmos.html",       # merges two English pages, reordered
    "iatros/viografiko.html",                    # new biography, not the old profile
    "xeirourgeia/tainia-akrateias-ouron.html",   # general incontinence text vs surgery page
}

# below this share of aligned headings a page is not a translation of the
# English original and nothing is recovered from it automatically
MIN_COVERAGE = 0.55

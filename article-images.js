// ──────────────────────────────────────────────────────────────
// article-images.js — Auto-inject placeholder images into
// article pages (.svc-body) after the first and third <h2>
// ──────────────────────────────────────────────────────────────
(function () {
  "use strict";

  var body = document.querySelector(".svc-body");
  if (!body) return; // Not an article page
  if (document.querySelector(".office-collage, .office-showcase, .gallery")) return; // Clinic pages already have real photos
  if (body.querySelector(".bio-portrait, .bio-story")) return; // Bio pages already provide their own real imagery

  // Map of page URL keywords → placeholder image config
  // The placeholder SVGs are generated inline (no external files needed)
  var pageImageMap = {
    // Maieftiki
    "poreia-egkymosynis":   { label: "Εγκυμοσύνη",         icon: "🤰", color: "#2166b0" },
    "progennitikos-elegxos":{ label: "Προγεννητικός Έλεγχος", icon: "🔬", color: "#2166b0" },
    "genikes-exetaseis":   { label: "Γενικές Εξετάσεις",     icon: "🧾", color: "#2166b0", photo: "articles/mai-genikes-exetaseis.jpg" },
    "themata-stin-egkymosyni":{ label: "Θέματα Εγκυμοσύνης", icon: "📋", color: "#2166b0" },
    "pathologia-tis-kyisis":{ label: "Παθολογία Κύησης",     icon: "⚕️", color: "#c0455a", photo: "articles/mai-pathologia-kyisis.jpg" },
    "thrombofilies-kyisis":{ label: "Θρομβοφιλίες",          icon: "🩸", color: "#2166b0", photo: "articles/mai-thrombofilies.jpg" },
    "diatrofi-stin":       { label: "Διατροφή",            icon: "🥗", color: "#2166b0", photo: "articles/mai-diatrofi.jpg" },
    "proini-adiathesia":   { label: "Πρωινή Αδιαθεσία",   icon: "🌅", color: "#2166b0", photo: "articles/mai-proini-adiathesia.jpg" },
    "athlisi-stin":        { label: "Άθληση",              icon: "🏃", color: "#2166b0", photo: "articles/mai-athlisi.jpg", photo2: "articles/mai-athlisi-2.jpg" },
    // ειδικό key: το σκέτο "aimorragia" έπιανε και τη σελίδα μητρορραγίας της Γυναικολογίας
    "aimorragia-stin-egkymosyni":{ label: "Αιμορραγία",     icon: "🩸", color: "#c0455a", photo: "articles/mai-aimorragia.jpg", photo2: "articles/mai-aimorragia-2.jpg" },
    "ektopi-kyisi":        { label: "Έκτοπη Κύηση",        icon: "⚠️", color: "#c0455a", photo: "articles/mai-ektopi-kyisi.jpg" },
    "kystiki-inosi":       { label: "Κυστική Ίνωση",       icon: "🧬", color: "#2166b0", photo: "articles/mai-kystiki-inosi.jpg" },
    "diavitis-kyisis":     { label: "Διαβήτης Κύησης",     icon: "💉", color: "#2166b0", photo: "articles/mai-diavitis.jpg" },
    "epilipsia":           { label: "Επιληψία",            icon: "⚡", color: "#2166b0", photo: "articles/mai-epilipsia.jpg" },
    "rhesus":              { label: "Rhesus",               icon: "🅾️", color: "#c0455a", photo: "articles/mai-rhesus.jpg" },
    "proeklampsia":        { label: "Προεκλαμψία",         icon: "❤️", color: "#c0455a", photo: "articles/mai-proeklampsia.jpg" },
    "dermatikes":          { label: "Δερματικές Παθήσεις", icon: "🩹", color: "#2166b0", photo: "articles/mai-dermatikes.jpg" },
    "streptokokkos":       { label: "Στρεπτόκοκκος Β",    icon: "🦠", color: "#2166b0", photo: "articles/mai-streptokokkos.jpg" },
    "didymi-kyisi":        { label: "Δίδυμη Κύηση",        icon: "👶👶", color: "#2166b0", photo: "articles/mai-didymi-kyisi.jpg", photo2: "articles/mai-didymi-kyisi-2.jpg" },
    "toketos":             { label: "Τοκετός",             icon: "🏥", color: "#2166b0" },
    "loxeia":              { label: "Λοχεία & Θηλασμός",   icon: "🤱", color: "#2166b0", photo: "articles/mai-loxeia.jpg" },

    // Embryomitriki
    "ypirixografima":      { label: "Υπερηχογράφημα",      icon: "📡", color: "#17497f" },
    "exetaseis-ygeias-embryou":{ label: "Έλεγχος Εμβρύου",     icon: "📈", color: "#17497f" },
    "genetikes-diataraxes":{ label: "Γενετικές Διαταραχές", icon: "🧬", color: "#17497f", photo: "articles/emb-genetikes-diataraxes.jpg" },
    "auxeniki-diafaneia":  { label: "Αυχενική Διαφάνεια",  icon: "🔍", color: "#17497f" },
    "viopsia-trofovlastis":{ label: "Βιοψία Τροφοβλάστης", icon: "🧪", color: "#17497f" },
    "amnioparakentisi":    { label: "Αμνιοπαρακέντηση",    icon: "💧", color: "#17497f" },
    "nipt":                { label: "NIPT",                 icon: "🧬", color: "#17497f" },

    // Gynaikologia
    "gynaikologiki-exetasi":{ label: "Γυν. Εξέταση",       icon: "🩺", color: "#3d6ea8" },
    "gynaikologiko-ypirixografima":{ label: "Γυν. Υπέρηχος", icon: "📡", color: "#3d6ea8" },
    "kolposkopisi":        { label: "Κολποσκόπηση",         icon: "🔎", color: "#3d6ea8", photo: "articles/gyn-kolposkopisi.jpg" },
    "mi-fysiologiki-aimorragia":{ label: "Αιμορραγία Μήτρας",  icon: "🩸", color: "#3d6ea8", photo: "articles/gyn-mi-fysiologiki-aimorragia.jpg" },
    "exetasi-traxilou":    { label: "Εξέταση Τραχήλου",    icon: "🔬", color: "#3d6ea8", photo: "articles/gyn-test-pap-2.jpg" },
    "test-pap":            { label: "Τεστ ΠΑΠ",            icon: "🧫", color: "#3d6ea8", photo: "articles/gyn-test-pap.jpg", photo2: "articles/gyn-test-pap-2.jpg" },
    "endomitriosi":        { label: "Ενδομητρίωση",        icon: "🔴", color: "#3d6ea8", photo: "articles/gyn-endomitriosi.jpg" },
    "kolpitides":          { label: "Κολπίτιδες",          icon: "💊", color: "#3d6ea8", photo: "articles/gyn-kolpitides.jpg" },
    "inomyomata":          { label: "Ινομυώματα",          icon: "🔵", color: "#3d6ea8", photo: "articles/gyn-inomyomata.jpg" },
    "akrateia-ouron":      { label: "Ακράτεια Ούρων",      icon: "💧", color: "#3d6ea8", photo: "articles/gyn-akrateia-ouron.jpg" },
    "kysteis-oothikon":    { label: "Κύστεις Ωοθηκών",     icon: "⭕", color: "#3d6ea8", photo: "articles/gyn-kysteis-oothikon.jpg" },
    "provlimata-pyelikis": { label: "Πυελική Στήριξη",     icon: "🦴", color: "#3d6ea8", photo: "articles/gyn-provlimata-pyelikis.jpg" },
    "ios-hpv":             { label: "HPV",                  icon: "🦠", color: "#3d6ea8", photo: "articles/gyn-ios-hpv.jpg", photo2: "articles/gyn-ios-hpv-2.jpg" },
    "polykystikes":        { label: "Πολυκυστικές Ωοθήκες",icon: "⚕️", color: "#3d6ea8", photo: "articles/gyn-polykystikes.jpg" },
    "dysminorroia":        { label: "Δυσμηνόρροια",        icon: "⚡", color: "#3d6ea8", photo: "articles/gyn-dysminorroia.jpg" },
    "thromvofilies":       { label: "Θρομβοφιλίες",        icon: "🩸", color: "#3d6ea8", photo: "articles/gyn-thromvofilies.jpg" },
    "klimaktirios":        { label: "Κλιμακτήριος",        icon: "🌸", color: "#3d6ea8", photo: "articles/gyn-klimaktirios.jpg" },
    "isxiaki-provoli":     { label: "Ισχιακή Προβολή",     icon: "👶", color: "#3d6ea8", photo: "articles/mai-isxiaki-provoli.jpg" },
    "kalliergeia-kolpikou":{ label: "Καλλιέργεια",         icon: "🧫", color: "#3d6ea8", photo: "articles/gyn-kalliergeia-kolpikou.jpg", photo2: "articles/gyn-kalliergeia-kolpikou-2.jpg" },
    "topothetisi-spiral":  { label: "Σπιράλ",              icon: "🔄", color: "#3d6ea8", photo: "articles/gyn-topothetisi-spiral.jpg" },
    "kaftiriasmos":        { label: "Κονδυλώματα",         icon: "✂️", color: "#3d6ea8", photo: "articles/gyn-kaftiriasmos.jpg", photo2: "articles/gyn-kaftiriasmos-2.jpg" },
    "viopsia-endomitriou": { label: "Βιοψία Ενδομητρίου",  icon: "🧪", color: "#3d6ea8" },
    "endomitria-spermategxysi":{ label: "IUI",             icon: "🔬", color: "#3d6ea8", photo: "articles/gyn-endomitria-spermategxysi.jpg" },
    "epemvaseis-sto-iatreio":{ label: "Επεμβάσεις",        icon: "🏥", color: "#3d6ea8" },
    "gynaikologika-themata":{ label: "Γυν. Θέματα",        icon: "📋", color: "#3d6ea8" },

    // Xeirourgeia
    // τα ειδικά keys πρώτα, αλλιώς τα πιάνουν τα γενικά "ysteroskopiki"/"laparoskopiki"
    "ysteroskopiki-afairesi-polypoda":{ label: "Υστεροσκόπηση για πολύποδα", icon: "✂️", color: "#1e5f8a", photo: "articles/xei-ysteroskopiki-polypoda.jpg" },
    "ysteroskopiki-afairesi-diafragmatos":{ label: "Υστεροσκόπηση για διάφραγμα", icon: "✂️", color: "#1e5f8a", photo: "articles/xei-ysteroskopiki-diafragma.jpg" },
    "laparoskopiki-afairesi-kystis":{ label: "Λαπαροσκοπική Αφαίρεση Κύστης", icon: "✂️", color: "#1e5f8a", photo: "articles/gyn-kysteis-oothikon.jpg" },
    "ysteroskopisi":       { label: "Υστεροσκόπηση",       icon: "🔍", color: "#1e5f8a", photo: "articles/xei-ysteroskopisi.jpg" },
    "ysteroskopiki":       { label: "Υστεροσκοπική",       icon: "✂️", color: "#1e5f8a", photo: "articles/xei-ysteroskopiki.jpg" },
    "laparoskopisi":       { label: "Λαπαροσκόπηση",       icon: "🔬", color: "#1e5f8a", photo: "articles/xei-laparoskopisi.jpg" },
    "laparoskopiki":       { label: "Λαπαροσκοπική",       icon: "✂️", color: "#1e5f8a", photo: "articles/xei-laparoskopisi.jpg" },
    "ysterektomi":         { label: "Υστερεκτομή",         icon: "🏥", color: "#1e5f8a", photo: "articles/xei-laparoskopisi.jpg" },
    "proetoimasia-xeirourgeiou":{ label: "Προετοιμασία",       icon: "📋", color: "#1e5f8a" },
    "konoeidis":           { label: "Κωνοειδής Εκτομή",    icon: "🔬", color: "#1e5f8a", photo: "articles/gyn-kolposkopisi.jpg" },
    "ourogynaikologia":    { label: "Ουρογυναικολογία",    icon: "💧", color: "#1e5f8a", photo: "articles/gyn-akrateia-ouron.jpg" },
    "tainia-akrateias":    { label: "Ταινία Ακράτειας",    icon: "🩹", color: "#1e5f8a", photo: "articles/xei-tainia-akrateias.jpg" },

    // Ypogonimotita — 1. Διερεύνηση
    // (τα πιο ειδικά keys πρώτα: ο έλεγχος είναι indexOf, κερδίζει το πρώτο)
    "ormonikos-elegxos-gynaikas":{ label: "Ορμονικός Έλεγχος γυναίκας", icon: "🧪", color: "#5b4a9f", photo: "articles/ypog-ormonikos-gynaikas.jpg", photo2: "articles/ypog-ormonikos-gynaikas-2.jpg" },
    "ormonikos-elegxos-andra":{ label: "Ορμονικός Έλεγχος άνδρα", icon: "🧪", color: "#5b4a9f", photo: "articles/ypog-ormonikos-andra.jpg" },
    "salpiggografia-hycosy":{ label: "Υστεροσαλπιγγογραφία", icon: "📡", color: "#5b4a9f", photo: "articles/ypog-salpiggografia.jpg" },
    "ypodektikotita-endomitriou":{ label: "Υποδεκτικότητα Ενδομητρίου", icon: "🔬", color: "#5b4a9f" },
    "xronia-endomitritida":{ label: "Χρόνια Ενδομητρίτιδα", icon: "🦠", color: "#5b4a9f" },
    "spermodiagramma":     { label: "Σπερμοδιάγραμμα",    icon: "🔬", color: "#5b4a9f", photo: "articles/ypog-spermodiagramma.jpg" },
    "eidikes-exetaseis-spermatos":{ label: "Ειδικές Εξετάσεις Σπέρματος", icon: "🧬", color: "#5b4a9f", photo: "articles/ypog-eidikes-exetaseis-spermatos.jpg" },
    "diereynisi-gynaikas": { label: "Διερεύνηση Γυναίκας", icon: "👩", color: "#5b4a9f", photo: "articles/ypog-ormonikos-gynaikas-2.jpg" },
    "diereynisi-andra":    { label: "Διερεύνηση Άνδρα",   icon: "👨", color: "#5b4a9f", photo: "articles/ypog-spermodiagramma.jpg" },
    "diereynisi":          { label: "Υπογονιμότητα",      icon: "🔍", color: "#5b4a9f", photo: "articles/ypog-diereynisi.jpg" },

    // Ypogonimotita — 2. Θεραπείες
    "proklisi-oothylakiorrixias":{ label: "Πρόκληση Ωοθυλακιορρηξίας", icon: "💊", color: "#5b4a9f" },
    "spermategxysi-iui":   { label: "Σπερματέγχυση (IUI)", icon: "🔬", color: "#5b4a9f", photo: "articles/gyn-endomitria-spermategxysi.jpg" },
    "exosomatiki-gonimopoiisi":{ label: "Εξωσωματική Γονιμοποίηση", icon: "🧬", color: "#5b4a9f" },
    "doti-spermatos":      { label: "Δότης Σπέρματος",    icon: "🎁", color: "#5b4a9f" },
    "therapeies-ypogonimotitas":{ label: "Θεραπείες Υπογονιμότητας", icon: "⚕️", color: "#5b4a9f" },

    // Ypogonimotita — 3. Νεότερες τεχνολογίες
    "time-lapse":          { label: "Τεχνολογία Time-Lapse", icon: "🎞️", color: "#5b4a9f" },
    "ypovoithoumeni-ekkolapsi":{ label: "Υποβοηθούμενη Εκκόλαψη", icon: "✨", color: "#5b4a9f" },
    "neoteres-texnologies":{ label: "Νεότερες Τεχνολογίες", icon: "⚗️", color: "#5b4a9f" },

    // Ypogonimotita — λοιπά
    "symvouleftiki-gonimotitas":{ label: "Συμβουλευτική",  icon: "💬", color: "#5b4a9f" },
    "axiologisi-ypogonimotitas":{ label: "Αξιολόγηση",         icon: "🔍", color: "#5b4a9f", photo: "articles/ypog-diereynisi.jpg" },
    "epanalambanomenes-apovoles":{ label: "Επαναλ. Αποβολές",  icon: "💜", color: "#5b4a9f", photo: "articles/mai-epanalambanomenes-apovoles.jpg" },
    "therapeies-exosomatikis":{ label: "IVF",              icon: "🧬", color: "#5b4a9f" },
    "fysikos-kyklos":      { label: "Φυσικός Κύκλος",      icon: "🔄", color: "#5b4a9f" },
    "mini-ivf":            { label: "Mini IVF",             icon: "🧪", color: "#5b4a9f" },
    "katapsyxi-oarion":    { label: "Κατάψυξη Ωαρίων",     icon: "❄️", color: "#5b4a9f" },
    "dorea-oarion":        { label: "Δωρεά Ωαρίων",        icon: "🎁", color: "#5b4a9f" },
    "anazoogonisi":        { label: "PRP Ωοθηκών",         icon: "💉", color: "#5b4a9f" },
    "parentheti-mitrotita":{ label: "Παρένθετη Μητρότητα", icon: "👩‍👶", color: "#5b4a9f" },
    "proemfyteftikos":     { label: "PGT",                  icon: "🧬", color: "#5b4a9f" },

    // Iatros
    "viografiko":          { label: "Βιογραφικό",          icon: "📄", color: "#2166b0" },
    "akadimaikoi-titloi":  { label: "Ακαδημαϊκοί Τίτλοι", icon: "🎓", color: "#2166b0" },
    "dimosieuseis":        { label: "Δημοσιεύσεις",        icon: "📚", color: "#2166b0" },
    "i-omada-mas":         { label: "Η Ομάδα",             icon: "👥", color: "#2166b0" },
    "i-maia-mas":          { label: "Η Μαία",              icon: "👩‍⚕️", color: "#2166b0" },
    "embryokardiologos":   { label: "Εμβρυοκαρδιολόγος",   icon: "❤️", color: "#2166b0" },
    "oi-xoroi-mas":        { label: "Οι Χώροι",            icon: "🏢", color: "#2166b0", photo: "clinics/vas-sofias/vas-sofias-01.jpg", photo2: "clinics/nea-smyrni/nea-smyrni-01.jpg" },
    "iatreio-athinon":     { label: "Ιατρείο Αθηνών",      icon: "🏥", color: "#2166b0" },
    "iatreio-neas-smyrnis":{ label: "Ιατρείο Ν. Σμύρνης",  icon: "🏥", color: "#2166b0" }
  };

  // Find the matching config for this page
  var path = window.location.pathname;
  var config = null;
  for (var key in pageImageMap) {
    if (path.indexOf(key) !== -1) {
      config = pageImageMap[key];
      break;
    }
  }
  // Fallback if no specific match
  if (!config) {
    config = { label: "Ιατρικό Άρθρο", icon: "🩺", color: "#2166b0" };
  }

  // Πραγματική φωτογραφία αν υπάρχει για τη σελίδα, αλλιώς το generic placeholder.
  var hasPhoto = !!config.photo;
  config.image = config.photo || "placeholder-medical.svg";

  // Create an image element
  function createPlaceholder(cfg, src) {
    var wrapper = document.createElement("figure");
    wrapper.style.cssText = "margin:2rem 0; text-align:center;";

    // Check if we are in a subfolder to construct the relative path to assets
    var isSubfolder = window.location.pathname.indexOf('/iatros/') !== -1 ||
                      window.location.pathname.indexOf('/maieftiki/') !== -1 ||
                      window.location.pathname.indexOf('/embryomitriki/') !== -1 ||
                      window.location.pathname.indexOf('/gynaikologia/') !== -1 ||
                      window.location.pathname.indexOf('/xeirourgeia/') !== -1 ||
                      window.location.pathname.indexOf('/ypogonimotita/') !== -1;
    
    // For GitHub Pages or local testing, sometimes the URL path might be slightly different.
    // The simplest robust approach for this site structure:
    var assetPrefix = isSubfolder ? "../assets/" : "assets/";

    var img = document.createElement("img");
    img.src = assetPrefix + (src || cfg.image);
    img.alt = cfg.label;
    img.loading = "lazy";
    img.style.cssText = hasPhoto
      ? "width:100%; aspect-ratio:16/9; border-radius:14px; box-shadow:0 4px 15px rgba(0,0,0,0.1); object-fit:cover; object-position:center; display:block;"
      : "width:100%; height:auto; border-radius:14px; box-shadow:0 4px 15px rgba(0,0,0,0.1); object-fit:cover; max-height:400px; border:1px solid #dce2e5;";

    var figcaption = document.createElement("figcaption");
    figcaption.style.cssText = "margin-top:0.75rem; font-family:Verdana, sans-serif; font-size:14px; color:#6b7d82; font-weight:600;";
    figcaption.textContent = cfg.label;

    wrapper.appendChild(img);
    wrapper.appendChild(figcaption);
    return wrapper;
  }

  // Πρώτη εικόνα μετά το 1ο <h2>, δεύτερη πιο κάτω μέσα στο άρθρο.
  var headings = body.querySelectorAll("h2");
  function insertAt(index, src) {
    var h = headings[index];
    if (!h) return;
    var anchor = h.nextElementSibling || h;
    anchor.parentNode.insertBefore(createPlaceholder(config, src), anchor.nextSibling);
  }

  if (headings.length >= 1) {
    insertAt(0, config.image);
  }

  // Δεύτερη εικόνα μόνο όταν υπάρχει ξεχωριστή φωτογραφία (ή για το generic placeholder,
  // όπως και πριν). Η ίδια πραγματική φωτογραφία δεν επαναλαμβάνεται στο ίδιο άρθρο.
  var second = hasPhoto ? config.photo2 : (headings.length >= 4 ? config.image : null);
  if (second && headings.length >= 2) {
    insertAt(headings.length >= 4 ? 3 : headings.length - 1, second);
  }
})();

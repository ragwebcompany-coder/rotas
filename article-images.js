// ──────────────────────────────────────────────────────────────
// article-images.js — Auto-inject placeholder images into
// article pages (.svc-body) after the first and third <h2>
// ──────────────────────────────────────────────────────────────
(function () {
  "use strict";

  var body = document.querySelector(".svc-body");
  if (!body) return; // Not an article page

  // Map of page URL keywords → placeholder image config
  // The placeholder SVGs are generated inline (no external files needed)
  var pageImageMap = {
    // Maieftiki
    "poreia-egkymosynis":   { label: "Εγκυμοσύνη",         icon: "🤰", color: "#2166b0" },
    "progennitikos-elegxos":{ label: "Προγεννητικός Έλεγχος", icon: "🔬", color: "#2166b0" },
    "genikes-exetaseis":   { label: "Γενικές Εξετάσεις",     icon: "🧾", color: "#2166b0" },
    "themata-stin-egkymosyni":{ label: "Θέματα Εγκυμοσύνης", icon: "📋", color: "#2166b0" },
    "pathologia-tis-kyisis":{ label: "Παθολογία Κύησης",     icon: "⚕️", color: "#c0455a" },
    "thrombofilies-kyisis":{ label: "Θρομβοφιλίες",          icon: "🩸", color: "#2166b0" },
    "diatrofi-stin":       { label: "Διατροφή",            icon: "🥗", color: "#2166b0" },
    "proini-adiathesia":   { label: "Πρωινή Αδιαθεσία",   icon: "🌅", color: "#2166b0" },
    "athlisi-stin":        { label: "Άθληση",              icon: "🏃", color: "#2166b0" },
    "aimorragia":          { label: "Αιμορραγία",          icon: "🩸", color: "#c0455a" },
    "ektopi-kyisi":        { label: "Έκτοπη Κύηση",        icon: "⚠️", color: "#c0455a" },
    "kystiki-inosi":       { label: "Κυστική Ίνωση",       icon: "🧬", color: "#2166b0" },
    "diavitis-kyisis":     { label: "Διαβήτης Κύησης",     icon: "💉", color: "#2166b0" },
    "epilipsia":           { label: "Επιληψία",            icon: "⚡", color: "#2166b0" },
    "rhesus":              { label: "Rhesus",               icon: "🅾️", color: "#c0455a" },
    "proeklampsia":        { label: "Προεκλαμψία",         icon: "❤️", color: "#c0455a" },
    "dermatikes":          { label: "Δερματικές Παθήσεις", icon: "🩹", color: "#2166b0" },
    "streptokokkos":       { label: "Στρεπτόκοκκος Β",    icon: "🦠", color: "#2166b0" },
    "didymi-kyisi":        { label: "Δίδυμη Κύηση",        icon: "👶👶", color: "#2166b0" },
    "toketos":             { label: "Τοκετός",             icon: "🏥", color: "#2166b0" },
    "loxeia":              { label: "Λοχεία & Θηλασμός",   icon: "🤱", color: "#2166b0" },

    // Embryomitriki
    "ypirixografima":      { label: "Υπερηχογράφημα",      icon: "📡", color: "#17497f" },
    "exetaseis-ygeias-embryou":{ label: "Έλεγχος Εμβρύου",     icon: "📈", color: "#17497f" },
    "genetikes-diataraxes":{ label: "Γενετικές Διαταραχές", icon: "🧬", color: "#17497f" },
    "auxeniki-diafaneia":  { label: "Αυχενική Διαφάνεια",  icon: "🔍", color: "#17497f" },
    "viopsia-trofovlastis":{ label: "Βιοψία Τροφοβλάστης", icon: "🧪", color: "#17497f" },
    "amnioparakentisi":    { label: "Αμνιοπαρακέντηση",    icon: "💧", color: "#17497f" },
    "nipt":                { label: "NIPT",                 icon: "🧬", color: "#17497f" },

    // Gynaikologia
    "gynaikologiki-exetasi":{ label: "Γυν. Εξέταση",       icon: "🩺", color: "#3d6ea8" },
    "gynaikologiko-ypirixografima":{ label: "Γυν. Υπέρηχος", icon: "📡", color: "#3d6ea8" },
    "kolposkopisi":        { label: "Κολποσκόπηση",         icon: "🔎", color: "#3d6ea8" },
    "mi-fysiologiki-aimorragia":{ label: "Αιμορραγία Μήτρας",  icon: "🩸", color: "#3d6ea8" },
    "exetasi-traxilou":    { label: "Εξέταση Τραχήλου",    icon: "🔬", color: "#3d6ea8" },
    "test-pap":            { label: "Τεστ ΠΑΠ",            icon: "🧫", color: "#3d6ea8" },
    "endomitriosi":        { label: "Ενδομητρίωση",        icon: "🔴", color: "#3d6ea8" },
    "kolpitides":          { label: "Κολπίτιδες",          icon: "💊", color: "#3d6ea8" },
    "inomyomata":          { label: "Ινομυώματα",          icon: "🔵", color: "#3d6ea8" },
    "akrateia-ouron":      { label: "Ακράτεια Ούρων",      icon: "💧", color: "#3d6ea8" },
    "kysteis-oothikon":    { label: "Κύστεις Ωοθηκών",     icon: "⭕", color: "#3d6ea8" },
    "provlimata-pyelikis": { label: "Πυελική Στήριξη",     icon: "🦴", color: "#3d6ea8" },
    "ios-hpv":             { label: "HPV",                  icon: "🦠", color: "#3d6ea8" },
    "polykystikes":        { label: "Πολυκυστικές Ωοθήκες",icon: "⚕️", color: "#3d6ea8" },
    "dysminorroia":        { label: "Δυσμηνόρροια",        icon: "⚡", color: "#3d6ea8" },
    "thromvofilies":       { label: "Θρομβοφιλίες",        icon: "🩸", color: "#3d6ea8" },
    "klimaktirios":        { label: "Κλιμακτήριος",        icon: "🌸", color: "#3d6ea8" },
    "isxiaki-provoli":     { label: "Ισχιακή Προβολή",     icon: "👶", color: "#3d6ea8" },
    "kalliergeia-kolpikou":{ label: "Καλλιέργεια",         icon: "🧫", color: "#3d6ea8" },
    "topothetisi-spiral":  { label: "Σπιράλ",              icon: "🔄", color: "#3d6ea8" },
    "kaftiriasmos":        { label: "Κονδυλώματα",         icon: "✂️", color: "#3d6ea8" },
    "viopsia-endomitriou": { label: "Βιοψία Ενδομητρίου",  icon: "🧪", color: "#3d6ea8" },
    "endomitria-spermategxysi":{ label: "IUI",             icon: "🔬", color: "#3d6ea8" },
    "epemvaseis-sto-iatreio":{ label: "Επεμβάσεις",        icon: "🏥", color: "#3d6ea8" },
    "gynaikologika-themata":{ label: "Γυν. Θέματα",        icon: "📋", color: "#3d6ea8" },

    // Xeirourgeia
    "ysteroskopisi":       { label: "Υστεροσκόπηση",       icon: "🔍", color: "#1e5f8a" },
    "ysteroskopiki":       { label: "Υστεροσκοπική",       icon: "✂️", color: "#1e5f8a" },
    "laparoskopisi":       { label: "Λαπαροσκόπηση",       icon: "🔬", color: "#1e5f8a" },
    "laparoskopiki":       { label: "Λαπαροσκοπική",       icon: "✂️", color: "#1e5f8a" },
    "ysterektomi":         { label: "Υστερεκτομή",         icon: "🏥", color: "#1e5f8a" },
    "proetoimasia-xeirourgeiou":{ label: "Προετοιμασία",       icon: "📋", color: "#1e5f8a" },
    "konoeidis":           { label: "Κωνοειδής Εκτομή",    icon: "🔬", color: "#1e5f8a" },
    "ourogynaikologia":    { label: "Ουρογυναικολογία",    icon: "💧", color: "#1e5f8a" },
    "tainia-akrateias":    { label: "Ταινία Ακράτειας",    icon: "🩹", color: "#1e5f8a" },

    // Ypogonimotita — 1. Διερεύνηση
    // (τα πιο ειδικά keys πρώτα: ο έλεγχος είναι indexOf, κερδίζει το πρώτο)
    "ormonikos-elegxos-gynaikas":{ label: "Ορμονικός Έλεγχος", icon: "🧪", color: "#5b4a9f" },
    "ormonikos-elegxos-andra":{ label: "Ορμονικός Έλεγχος", icon: "🧪", color: "#5b4a9f" },
    "salpiggografia-hycosy":{ label: "Σαλπιγγογραφία HyCoSy", icon: "📡", color: "#5b4a9f" },
    "ypodektikotita-endomitriou":{ label: "Υποδεκτικότητα Ενδομητρίου", icon: "🔬", color: "#5b4a9f" },
    "xronia-endomitritida":{ label: "Χρόνια Ενδομητρίτιδα", icon: "🦠", color: "#5b4a9f" },
    "spermodiagramma":     { label: "Σπερμοδιάγραμμα",    icon: "🔬", color: "#5b4a9f" },
    "eidikes-exetaseis-spermatos":{ label: "Ειδικές Εξετάσεις Σπέρματος", icon: "🧬", color: "#5b4a9f" },
    "diereynisi-gynaikas": { label: "Διερεύνηση Γυναίκας", icon: "👩", color: "#5b4a9f" },
    "diereynisi-andra":    { label: "Διερεύνηση Άνδρα",   icon: "👨", color: "#5b4a9f" },
    "diereynisi":          { label: "Υπογονιμότητα",      icon: "🔍", color: "#5b4a9f" },

    // Ypogonimotita — 2. Θεραπείες
    "proklisi-oothylakiorrixias":{ label: "Πρόκληση Ωοθυλακιορρηξίας", icon: "💊", color: "#5b4a9f" },
    "spermategxysi-iui":   { label: "Σπερματέγχυση (IUI)", icon: "🔬", color: "#5b4a9f" },
    "exosomatiki-gonimopoiisi":{ label: "Εξωσωματική Γονιμοποίηση", icon: "🧬", color: "#5b4a9f" },
    "doti-spermatos":      { label: "Δότης Σπέρματος",    icon: "🎁", color: "#5b4a9f" },
    "therapeies-ypogonimotitas":{ label: "Θεραπείες Υπογονιμότητας", icon: "⚕️", color: "#5b4a9f" },

    // Ypogonimotita — 3. Νεότερες τεχνολογίες
    "time-lapse":          { label: "Τεχνολογία Time-Lapse", icon: "🎞️", color: "#5b4a9f" },
    "ypovoithoumeni-ekkolapsi":{ label: "Υποβοηθούμενη Εκκόλαψη", icon: "✨", color: "#5b4a9f" },
    "neoteres-texnologies":{ label: "Νεότερες Τεχνολογίες", icon: "⚗️", color: "#5b4a9f" },

    // Ypogonimotita — λοιπά
    "symvouleftiki-gonimotitas":{ label: "Συμβουλευτική",  icon: "💬", color: "#5b4a9f" },
    "axiologisi-ypogonimotitas":{ label: "Αξιολόγηση",         icon: "🔍", color: "#5b4a9f" },
    "epanalambanomenes-apovoles":{ label: "Επαναλ. Αποβολές",  icon: "💜", color: "#5b4a9f" },
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
    "oi-xoroi-mas":        { label: "Οι Χώροι",            icon: "🏢", color: "#2166b0" },
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

  // Determine the correct image based on category
  var categoryImage = "cat_iatros.jpg"; // default
  if (path.indexOf("/maieftiki/") !== -1) categoryImage = "cat_maieftiki.jpg";
  else if (path.indexOf("/embryomitriki/") !== -1) categoryImage = "cat_embryomitriki.jpg";
  else if (path.indexOf("/gynaikologia/") !== -1) categoryImage = "cat_gynaikologia.jpg";
  else if (path.indexOf("/xeirourgeia/") !== -1) categoryImage = "cat_xeirourgeia.jpg";
  else if (path.indexOf("/ypogonimotita/") !== -1) categoryImage = "cat_ypogonimotita.jpg";
  else if (path.indexOf("/iatros/") !== -1) categoryImage = "cat_iatros.jpg";
  
  config.image = categoryImage;

  // Create an image element
  function createPlaceholder(cfg, width, height) {
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
    img.src = assetPrefix + cfg.image;
    img.alt = cfg.label;
    img.loading = "lazy";
    img.style.cssText = "width:100%; height:auto; border-radius:14px; box-shadow:0 4px 15px rgba(0,0,0,0.1); object-fit:cover; max-height:400px; border:1px solid #dce2e5;";

    var figcaption = document.createElement("figcaption");
    figcaption.style.cssText = "margin-top:0.75rem; font-family:Verdana, sans-serif; font-size:14px; color:#6b7d82; font-weight:600;";
    figcaption.textContent = cfg.label;

    wrapper.appendChild(img);
    wrapper.appendChild(figcaption);
    return wrapper;
  }

  // Insert placeholders after the first <h2> and after the 3rd <h2>
  var headings = body.querySelectorAll("h2");
  if (headings.length >= 1) {
    var firstH2 = headings[0];
    // Find the next sibling (the paragraph after the first h2)
    var insertAfter = firstH2.nextElementSibling || firstH2;
    var ph1 = createPlaceholder(config, 800, 300);
    insertAfter.parentNode.insertBefore(ph1, insertAfter.nextSibling);
  }
  if (headings.length >= 4) {
    var thirdH2 = headings[3];
    var insertAfter2 = thirdH2.nextElementSibling || thirdH2;
    var ph2 = createPlaceholder(config, 800, 280);
    insertAfter2.parentNode.insertBefore(ph2, insertAfter2.nextSibling);
  }
})();

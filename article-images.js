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
    "poreia-egkymosynis":   { label: "Εγκυμοσύνη",         icon: "🤰", color: "#2a8f96" },
    "progennitikos-elegxos":{ label: "Προγεννητικός Έλεγχος", icon: "🔬", color: "#2a8f96" },
    "themata-stin-egkymosyni":{ label: "Θέματα Εγκυμοσύνης", icon: "📋", color: "#2a8f96" },
    "diatrofi-stin":       { label: "Διατροφή",            icon: "🥗", color: "#2a8f96" },
    "proini-adiathesia":   { label: "Πρωινή Αδιαθεσία",   icon: "🌅", color: "#2a8f96" },
    "athlisi-stin":        { label: "Άθληση",              icon: "🏃", color: "#2a8f96" },
    "aimorragia":          { label: "Αιμορραγία",          icon: "🩸", color: "#c44" },
    "ektopi-kyisi":        { label: "Έκτοπη Κύηση",        icon: "⚠️", color: "#c44" },
    "kystiki-inosi":       { label: "Κυστική Ίνωση",       icon: "🧬", color: "#2a8f96" },
    "diavitis-kyisis":     { label: "Διαβήτης Κύησης",     icon: "💉", color: "#2a8f96" },
    "epilipsia":           { label: "Επιληψία",            icon: "⚡", color: "#2a8f96" },
    "rhesus":              { label: "Rhesus",               icon: "🅾️", color: "#c44" },
    "proeklampsia":        { label: "Προεκλαμψία",         icon: "❤️", color: "#c44" },
    "dermatikes":          { label: "Δερματικές Παθήσεις", icon: "🩹", color: "#2a8f96" },
    "streptokokkos":       { label: "Στρεπτόκοκκος Β",    icon: "🦠", color: "#2a8f96" },
    "didymi-kyisi":        { label: "Δίδυμη Κύηση",        icon: "👶👶", color: "#2a8f96" },
    "toketos":             { label: "Τοκετός",             icon: "🏥", color: "#2a8f96" },
    "loxeia":              { label: "Λοχεία & Θηλασμός",   icon: "🤱", color: "#2a8f96" },

    // Embryomitriki
    "ypirixografima":      { label: "Υπερηχογράφημα",      icon: "📡", color: "#1e7078" },
    "auxeniki-diafaneia":  { label: "Αυχενική Διαφάνεια",  icon: "🔍", color: "#1e7078" },
    "viopsia-trofovlastis":{ label: "Βιοψία Τροφοβλάστης", icon: "🧪", color: "#1e7078" },
    "amnioparakentisi":    { label: "Αμνιοπαρακέντηση",    icon: "💧", color: "#1e7078" },
    "nipt":                { label: "NIPT",                 icon: "🧬", color: "#1e7078" },

    // Gynaikologia
    "gynaikologiki-exetasi":{ label: "Γυν. Εξέταση",       icon: "🩺", color: "#4a6a70" },
    "gynaikologiko-ypirixografima":{ label: "Γυν. Υπέρηχος", icon: "📡", color: "#4a6a70" },
    "exetasi-traxilou":    { label: "Εξέταση Τραχήλου",    icon: "🔬", color: "#4a6a70" },
    "test-pap":            { label: "Τεστ ΠΑΠ",            icon: "🧫", color: "#4a6a70" },
    "endomitriosi":        { label: "Ενδομητρίωση",        icon: "🔴", color: "#4a6a70" },
    "kolpitides":          { label: "Κολπίτιδες",          icon: "💊", color: "#4a6a70" },
    "inomyomata":          { label: "Ινομυώματα",          icon: "🔵", color: "#4a6a70" },
    "akrateia-ouron":      { label: "Ακράτεια Ούρων",      icon: "💧", color: "#4a6a70" },
    "kysteis-oothikon":    { label: "Κύστεις Ωοθηκών",     icon: "⭕", color: "#4a6a70" },
    "provlimata-pyelikis": { label: "Πυελική Στήριξη",     icon: "🦴", color: "#4a6a70" },
    "ios-hpv":             { label: "HPV",                  icon: "🦠", color: "#4a6a70" },
    "polykystikes":        { label: "Πολυκυστικές Ωοθήκες",icon: "⚕️", color: "#4a6a70" },
    "dysminorroia":        { label: "Δυσμηνόρροια",        icon: "⚡", color: "#4a6a70" },
    "thromvofilies":       { label: "Θρομβοφιλίες",        icon: "🩸", color: "#4a6a70" },
    "klimaktirios":        { label: "Κλιμακτήριος",        icon: "🌸", color: "#4a6a70" },
    "isxiaki-provoli":     { label: "Ισχιακή Προβολή",     icon: "👶", color: "#4a6a70" },
    "kalliergeia-kolpikou":{ label: "Καλλιέργεια",         icon: "🧫", color: "#4a6a70" },
    "topothetisi-spiral":  { label: "Σπιράλ",              icon: "🔄", color: "#4a6a70" },
    "kaftiriasmos":        { label: "Κονδυλώματα",         icon: "✂️", color: "#4a6a70" },
    "viopsia-endomitriou": { label: "Βιοψία Ενδομητρίου",  icon: "🧪", color: "#4a6a70" },
    "endomitria-spermategxysi":{ label: "IUI",             icon: "🔬", color: "#4a6a70" },
    "epemvaseis-sto-iatreio":{ label: "Επεμβάσεις",        icon: "🏥", color: "#4a6a70" },
    "gynaikologika-themata":{ label: "Γυν. Θέματα",        icon: "📋", color: "#4a6a70" },

    // Xeirourgeia
    "ysteroskopisi":       { label: "Υστεροσκόπηση",       icon: "🔍", color: "#2c6e4f" },
    "ysteroskopiki":       { label: "Υστεροσκοπική",       icon: "✂️", color: "#2c6e4f" },
    "laparoskopisi":       { label: "Λαπαροσκόπηση",       icon: "🔬", color: "#2c6e4f" },
    "laparoskopiki":       { label: "Λαπαροσκοπική",       icon: "✂️", color: "#2c6e4f" },
    "ysterektomi":         { label: "Υστερεκτομή",         icon: "🏥", color: "#2c6e4f" },
    "konoeidis":           { label: "Κωνοειδής Εκτομή",    icon: "🔬", color: "#2c6e4f" },
    "ourogynaikologia":    { label: "Ουρογυναικολογία",    icon: "💧", color: "#2c6e4f" },
    "tainia-akrateias":    { label: "Ταινία Ακράτειας",    icon: "🩹", color: "#2c6e4f" },

    // Ypogonimotita
    "symvouleftiki-gonimotitas":{ label: "Συμβουλευτική",  icon: "💬", color: "#6b4a8f" },
    "therapeies-exosomatikis":{ label: "IVF",              icon: "🧬", color: "#6b4a8f" },
    "fysikos-kyklos":      { label: "Φυσικός Κύκλος",      icon: "🔄", color: "#6b4a8f" },
    "mini-ivf":            { label: "Mini IVF",             icon: "🧪", color: "#6b4a8f" },
    "katapsyxi-oarion":    { label: "Κατάψυξη Ωαρίων",     icon: "❄️", color: "#6b4a8f" },
    "dorea-oarion":        { label: "Δωρεά Ωαρίων",        icon: "🎁", color: "#6b4a8f" },
    "anazoogonisi":        { label: "PRP Ωοθηκών",         icon: "💉", color: "#6b4a8f" },
    "parentheti-mitrotita":{ label: "Παρένθετη Μητρότητα", icon: "👩‍👶", color: "#6b4a8f" },
    "proemfyteftikos":     { label: "PGT",                  icon: "🧬", color: "#6b4a8f" },

    // Iatros
    "viografiko":          { label: "Βιογραφικό",          icon: "📄", color: "#2a8f96" },
    "akadimaikoi-titloi":  { label: "Ακαδημαϊκοί Τίτλοι", icon: "🎓", color: "#2a8f96" },
    "dimosieuseis":        { label: "Δημοσιεύσεις",        icon: "📚", color: "#2a8f96" },
    "i-omada-mas":         { label: "Η Ομάδα",             icon: "👥", color: "#2a8f96" },
    "i-maia-mas":          { label: "Η Μαία",              icon: "👩‍⚕️", color: "#2a8f96" },
    "embryokardiologos":   { label: "Εμβρυοκαρδιολόγος",   icon: "❤️", color: "#2a8f96" },
    "oi-xoroi-mas":        { label: "Οι Χώροι",            icon: "🏢", color: "#2a8f96" },
    "iatreio-athinon":     { label: "Ιατρείο Αθηνών",      icon: "🏥", color: "#2a8f96" },
    "iatreio-neas-smyrnis":{ label: "Ιατρείο Ν. Σμύρνης",  icon: "🏥", color: "#2a8f96" }
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
    config = { label: "Ιατρικό Άρθρο", icon: "🩺", color: "#2a8f96" };
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

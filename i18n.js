// ──────────────────────────────────────────────────────────────
// i18n.js — Language switch (Greek → English)
// Injects an "EN" link into the nav that points to the English
// version of the site (/en/). The English pages carry their own
// "ΕΛ" link back, so they do not load this script.
// ──────────────────────────────────────────────────────────────
(function () {
  "use strict";

  // Work out the relative path to the site root from this script's own
  // src (either "i18n.js" at the root or "../i18n.js" in a subfolder),
  // so the link works both locally (file://) and in production.
  function rootPrefix() {
    var s = document.querySelector('script[src$="i18n.js"]');
    var src = s ? s.getAttribute("src") : "i18n.js";
    return src.replace(/i18n\.js$/, ""); // "" or "../"
  }

  function injectToggle() {
    var navLinks = document.querySelector(".nav-links");
    if (!navLinks || document.getElementById("lang-toggle")) return;

    var enHref = rootPrefix() + "en/index.html";

    var li = document.createElement("li");
    li.className = "lang-switch";

    var link = document.createElement("a");
    link.className = "lang-btn";
    link.id = "lang-toggle";
    link.href = enHref;
    link.hreflang = "en";
    link.setAttribute("aria-label", "Switch to English");
    link.innerHTML = '<span class="lang-flag">EN</span>';

    li.appendChild(link);

    // Place just before the "Appointment" button if present, else at end.
    var apptBtn = navLinks.querySelector("a.btn-nav");
    if (apptBtn && apptBtn.parentNode) {
      navLinks.insertBefore(li, apptBtn.parentNode);
    } else {
      navLinks.appendChild(li);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", injectToggle);
  } else {
    injectToggle();
  }
})();

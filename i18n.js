// ──────────────────────────────────────────────────────────────
// i18n.js — Language switch (Ελληνικά ↔ English)
// Every page carries a <link rel="alternate" hreflang="…"> that
// points at the same page in the other language (written by
// _build/build_en.py).  This script turns that link into the
// EN / ΕΛ button in the nav, so the switch always lands on the
// matching page rather than on the home page.
// ──────────────────────────────────────────────────────────────
(function () {
  "use strict";

  var LABEL = { en: "EN", el: "ΕΛ" };
  var ARIA = { en: "Switch to English", el: "Αλλαγή σε Ελληνικά" };

  function injectToggle() {
    var navLinks = document.querySelector(".nav-links");
    if (!navLinks || document.getElementById("lang-toggle")) return;

    var here = (document.documentElement.getAttribute("lang") || "el")
      .slice(0, 2).toLowerCase();
    var alt = document.querySelector('link[rel="alternate"][hreflang]');
    if (!alt) return;

    var lang = alt.getAttribute("hreflang").slice(0, 2).toLowerCase();
    if (lang === here || !LABEL[lang]) return;

    var li = document.createElement("li");
    li.className = "lang-switch";

    var link = document.createElement("a");
    link.className = "lang-btn";
    link.id = "lang-toggle";
    link.href = alt.getAttribute("href");
    link.hreflang = lang;
    link.setAttribute("aria-label", ARIA[lang]);

    var flag = document.createElement("span");
    flag.className = "lang-flag";
    flag.textContent = LABEL[lang];
    link.appendChild(flag);
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

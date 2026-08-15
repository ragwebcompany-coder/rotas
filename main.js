// Δρ. Μιχάλης Ρώτας — shared UI behaviour
(function () {
  // Current year
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();

  // Mobile navigation
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        document.body.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });
  }

  // Sticky header shadow
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("scrolled", window.scrollY > 24);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Homepage feature slider
  var slider = document.querySelector("[data-home-slider]");
  if (slider) {
    var slides = Array.prototype.slice.call(slider.querySelectorAll(".home-slide"));
    var tabs = Array.prototype.slice.call(slider.querySelectorAll(".home-slider__tab"));
    var prev = slider.querySelector(".home-slider__arrow--prev");
    var next = slider.querySelector(".home-slider__arrow--next");
    var progress = slider.querySelector(".home-slider__progress span");
    var slideIndex = 0;
    var slideTimer = null;
    var pointerStartX = null;
    var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var resetProgress = function () {
      if (!progress || reduceMotion) return;
      progress.style.animation = "none";
      progress.offsetHeight;
      progress.style.animation = "";
    };
    var showSlide = function (idx) {
      if (!slides.length) return;
      slideIndex = (idx + slides.length) % slides.length;
      slides.forEach(function (slide, i) {
        slide.classList.toggle("is-active", i === slideIndex);
      });
      tabs.forEach(function (tab, i) {
        tab.classList.toggle("is-active", i === slideIndex);
        tab.setAttribute("aria-pressed", i === slideIndex ? "true" : "false");
      });
      resetProgress();
    };
    var startSlider = function () {
      if (slideTimer || slides.length < 2 || reduceMotion) return;
      slider.classList.add("is-running");
      slider.classList.remove("is-paused");
      slideTimer = window.setInterval(function () {
        showSlide(slideIndex + 1);
      }, 5200);
    };
    var stopSlider = function () {
      if (!slideTimer) return;
      window.clearInterval(slideTimer);
      slideTimer = null;
    };
    var restartSlider = function () {
      stopSlider();
      slider.classList.remove("is-paused");
      resetProgress();
      startSlider();
    };
    tabs.forEach(function (tab, i) {
      tab.addEventListener("click", function () {
        showSlide(i);
        restartSlider();
      });
    });
    if (prev) {
      prev.addEventListener("click", function () {
        showSlide(slideIndex - 1);
        restartSlider();
      });
    }
    if (next) {
      next.addEventListener("click", function () {
        showSlide(slideIndex + 1);
        restartSlider();
      });
    }
    slider.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") {
        showSlide(slideIndex - 1);
        restartSlider();
      }
      if (e.key === "ArrowRight") {
        showSlide(slideIndex + 1);
        restartSlider();
      }
    });
    slider.addEventListener("pointerdown", function (e) {
      pointerStartX = e.clientX;
    });
    slider.addEventListener("pointerup", function (e) {
      if (pointerStartX === null) return;
      var delta = e.clientX - pointerStartX;
      pointerStartX = null;
      if (Math.abs(delta) < 46) return;
      showSlide(delta > 0 ? slideIndex - 1 : slideIndex + 1);
      restartSlider();
    });
    slider.addEventListener("pointercancel", function () {
      pointerStartX = null;
    });
    showSlide(0);
    startSlider();
  }

  // Count-up for the stats band
  var nums = document.querySelectorAll("[data-count]");
  var runCount = function (el) {
    var target = parseInt(el.getAttribute("data-count"), 10);
    if (!target) return;
    var suffix = el.getAttribute("data-suffix") || "";
    var start = null;
    var dur = 1400;
    var step = function (ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased).toLocaleString("el-GR") + suffix;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };

  // Reveal on scroll
  var revealEls = document.querySelectorAll(".reveal");
  // Dev aid / safety: reveal everything at once
  if (location.hash === "#showall") {
    document.body.classList.add("showall");
    revealEls.forEach(function (el) { el.classList.add("in"); });
    nums.forEach(function (el) { runCount(el); });
    return;
  }
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            io.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach(function (el, i) {
      el.style.setProperty("--d", (i % 6) * 55 + "ms");
      io.observe(el);
    });

    var nio = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            runCount(entry.target);
            nio.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.4 }
    );
    nums.forEach(function (el) { nio.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("in"); });
    nums.forEach(function (el) { runCount(el); });
  }
})();

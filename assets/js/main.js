// Small progressive enhancements. The page is fully usable without JavaScript.
(function () {
  "use strict";

  // Footer year
  var year = document.getElementById("year");
  if (year) year.textContent = String(new Date().getFullYear());

  // Nav border once the page is scrolled
  var nav = document.querySelector(".site-nav");
  function onScroll() {
    if (nav) nav.classList.toggle("is-scrolled", window.scrollY > 8);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  // Highlight the nav link of the section currently in view
  if (!("IntersectionObserver" in window)) return;
  var links = Array.prototype.slice.call(document.querySelectorAll(".nav-links a[href^='#']"));
  var byId = {};
  links.forEach(function (a) {
    byId[a.getAttribute("href").slice(1)] = a;
  });
  var sections = links
    .map(function (a) {
      return document.getElementById(a.getAttribute("href").slice(1));
    })
    .filter(Boolean);

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        links.forEach(function (a) {
          a.classList.remove("is-active");
          a.removeAttribute("aria-current");
        });
        var link = byId[entry.target.id];
        if (!link) return;
        link.classList.add("is-active");
        link.setAttribute("aria-current", "true");
        // On phones the nav row scrolls sideways: keep the active link visible
        var list = link.parentNode.parentNode;
        if (list.scrollWidth > list.clientWidth) {
          var lr = link.getBoundingClientRect();
          var ur = list.getBoundingClientRect();
          list.scrollLeft += lr.left - ur.left - (ur.width - lr.width) / 2;
        }
      });
    },
    { rootMargin: "-45% 0px -50% 0px" }
  );
  sections.forEach(function (s) {
    observer.observe(s);
  });
})();

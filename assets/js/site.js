/* Brass Tack Communications — small, dependency-free enhancements. */
(function () {
  'use strict';

  /* --- 1. Mobile navigation ------------------------------------------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('primary-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = document.body.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        document.body.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && document.body.classList.contains('nav-open')) {
        document.body.classList.remove('nav-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  /* --- 2. Header hairline once the page scrolls ------------------------ */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-stuck', window.scrollY > 8);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* --- 3. Gentle reveal on scroll -------------------------------------- */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var targets = document.querySelectorAll('.reveal');
  if (reduce || !('IntersectionObserver' in window)) {
    targets.forEach(function (el) { el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    targets.forEach(function (el) { io.observe(el); });
  }

  /* --- 4. Click-to-load Vimeo (keeps the page fast) -------------------- */
  document.querySelectorAll('.vid-btn').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var host = btn.closest('.vid');
      var src = host.getAttribute('data-src');
      if (!src) return;
      var frame = document.createElement('iframe');
      frame.src = src + (src.indexOf('?') > -1 ? '&' : '?') +
        'autoplay=1&title=0&byline=0&portrait=0&dnt=1';
      frame.setAttribute('title', host.getAttribute('data-title') || 'Video');
      frame.setAttribute('allow', 'autoplay; fullscreen; picture-in-picture');
      frame.setAttribute('allowfullscreen', '');
      frame.setAttribute('loading', 'lazy');
      host.innerHTML = '';
      host.appendChild(frame);
    });
  });
})();

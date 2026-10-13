(function () {
  var EMAIL = 'autopflegeservice@online.de';
  var header = document.getElementById('header');
  var nav = document.getElementById('nav');
  var burger = document.getElementById('burger');

  window.dataLayer = window.dataLayer || [];
  function track(name, data) {
    var ev = { event: name };
    for (var k in data || {}) ev[k] = data[k];
    window.dataLayer.push(ev);
  }

  // Header-Schatten beim Scrollen
  function onScroll() { header.classList.toggle('is-stuck', window.scrollY > 8); }
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobiles Menü
  function setNav(open) {
    nav.classList.toggle('is-open', open);
    document.body.classList.toggle('nav-open', open);
    burger.setAttribute('aria-expanded', String(open));
    burger.setAttribute('aria-label', open ? 'Menü schließen' : 'Menü öffnen');
  }
  burger.addEventListener('click', function () { setNav(!nav.classList.contains('is-open')); });
  nav.addEventListener('click', function (e) { if (e.target.closest('a')) setNav(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setNav(false); });

  // Seiten ohne Formular: "Angebot anfragen" führt zur Kontaktseite
  if (!document.getElementById('anfrage')) {
    document.querySelectorAll('a[href="#anfrage"]').forEach(function (a) { a.setAttribute('href', 'kontakt.html#anfrage'); });
  }

  // Klicks auf Telefon / E-Mail als Ereignis melden (für Google Ads Conversions)
  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-track]');
    if (el) track(el.getAttribute('data-track'), { page: document.body.getAttribute('data-page') });
  });

  // Hero-Video nur abspielen, wenn Bewegung erwünscht ist
  var video = document.getElementById('heroVideo');
  if (video && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    video.removeAttribute('autoplay');
    video.pause();
  }

  // Karte erst nach Klick laden
  var mapBtn = document.getElementById('mapLoad');
  if (mapBtn) {
    mapBtn.addEventListener('click', function () {
      var box = document.getElementById('map');
      var f = document.createElement('iframe');
      f.src = box.getAttribute('data-src');
      f.title = 'Karte: Autopflege Leichlingen';
      f.loading = 'lazy';
      box.innerHTML = '';
      box.classList.add('is-loaded');
      box.appendChild(f);
    });
  }

  // Einblenden beim Scrollen, Ablauf-Linie und gezeichnete Piktogramme
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.pic').forEach(function (svg) {
    if (reduce) return;
    svg.querySelectorAll('path, circle, rect').forEach(function (el, i) {
      var len = el.getTotalLength ? el.getTotalLength() : 100;
      el.style.strokeDasharray = len;
      el.style.strokeDashoffset = len;
      el.style.transition = 'stroke-dashoffset 1.1s cubic-bezier(.2,.7,.2,1) ' + (0.25 + i * 0.09) + 's';
    });
  });
  function show(el) {
    el.classList.add('is-in');
    el.querySelectorAll('.pic path, .pic circle, .pic rect').forEach(function (p) { p.style.strokeDashoffset = 0; });
  }
  var items = document.querySelectorAll('.rv, .js-in');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { show(en.target); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(show);
  }

  // Anfrageformulare
  document.querySelectorAll('.js-form').forEach(function (form) {
    var msg = form.querySelector('.form__msg');
    var btn = form.querySelector('button[type="submit"]');

    function show(text, ok) { msg.className = 'form__msg ' + (ok ? 'is-ok' : 'is-error'); msg.textContent = text; }

    function mailFallback() {
      var f = form.elements;
      var body = ['Name: ' + f.name.value, 'Telefon: ' + f.telefon.value, 'E-Mail: ' + (f.email.value || '-'), 'Leistung: ' + (f.leistung.value || '-'), '', f.nachricht.value].join('\n');
      var subject = 'Anfrage über die Website' + (f.leistung.value ? ': ' + f.leistung.value : '');
      window.location.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      show('Ihr E-Mail-Programm wurde mit der Anfrage geöffnet. Alternativ erreichen Sie uns unter 0177 / 780 41 46.', true);
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = form.elements, ok = true;
      [f.name, f.telefon].forEach(function (el) {
        var bad = !el.value.trim();
        el.classList.toggle('is-invalid', bad);
        if (bad) ok = false;
      });
      var mailBad = f.email.value && !/^\S+@\S+\.\S+$/.test(f.email.value);
      f.email.classList.toggle('is-invalid', !!mailBad);
      if (!ok) return show('Bitte geben Sie Name und Telefonnummer an.', false);
      if (mailBad) return show('Bitte prüfen Sie die E-Mail-Adresse.', false);
      if (!f.datenschutz.checked) return show('Bitte stimmen Sie der Datenschutzerklärung zu.', false);

      btn.disabled = true;
      btn.textContent = 'Wird gesendet …';
      fetch(form.getAttribute('action'), { method: 'POST', body: new FormData(form), headers: { 'X-Requested-With': 'fetch' } })
        .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
        .then(function (d) {
          if (!d || !d.ok) return Promise.reject();
          track('lead_form_submit', { leistung: f.leistung.value });
          window.location.href = 'danke.html';
        })
        .catch(function () {
          // Kein Versand-Skript erreichbar (z. B. lokale Vorschau): E-Mail-Programm öffnen
          btn.disabled = false;
          btn.textContent = 'Anfrage senden';
          mailFallback();
        });
    });
  });

  document.querySelectorAll('.js-year').forEach(function (y) { y.textContent = new Date().getFullYear(); });
})();

/* =========================================================
   UNITED AUTO TRANSPORT — SHARED SITE JS
   Vanilla JS, no dependencies, to keep the page light.
   Sections:
   1. Phone number injection (from config.js, single source of truth)
   2. Timezone-aware hours: real logic stays anchored to the office's
      actual timezone; only the DISPLAY converts to the visitor's clock
   3. Mobile nav + sticky CTA bar
   4. FAQ accordion
   5. Callback micro-form + multi-step quote calculator
   6. UTM capture + analytics/tracking event stubs
   ========================================================= */

(function () {
  var CFG = window.UAT_CONFIG || {};
  var PAGE_LOAD_TIME = Date.now();

  /* ---------- Ad / Analytics tracking init ---------- */
  (function initAdTracking() {
    var ga4Id = CFG.ga4MeasurementId;
    if (ga4Id && ga4Id.indexOf('PLACEHOLDER') === -1) {
      var s = document.createElement('script');
      s.async = true;
      s.src = 'https://www.googletagmanager.com/gtag/js?id=' + ga4Id;
      document.head.appendChild(s);
      window.dataLayer = window.dataLayer || [];
      function gtag() { window.dataLayer.push(arguments); }
      window.gtag = gtag;
      gtag('js', new Date());
      gtag('config', ga4Id);
    }

    var metaId = CFG.metaPixelId;
    if (metaId && metaId.indexOf('PLACEHOLDER') === -1) {
      (function (f, b, e, v, n, t, s) {
        if (f.fbq) return;
        n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
        if (!f._fbq) f._fbq = n;
        n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = [];
        t = b.createElement(e); t.async = !0; t.src = v;
        s = b.getElementsByTagName(e)[0];
        s.parentNode.insertBefore(t, s);
      })(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
      window.fbq('init', metaId);
      window.fbq('track', 'PageView');
    }
  })();

  document.addEventListener('DOMContentLoaded', function () {

    /* ---------- 1. Phone number injection ---------- */
    document.querySelectorAll('[data-phone-display]').forEach(function (el) {
      el.textContent = CFG.phoneDisplay;
    });
    document.querySelectorAll('[data-phone-tel]').forEach(function (el) {
      el.setAttribute('href', 'tel:' + CFG.phoneTel);
    });

    /* ---------- 2. Timezone-aware hours ---------- */
    function getPartsInTZ(date, timeZone) {
      var fmt = new Intl.DateTimeFormat('en-US', {
        timeZone: timeZone, hour12: false, year: 'numeric', month: '2-digit',
        day: '2-digit', hour: '2-digit', minute: '2-digit', weekday: 'short'
      });
      return fmt.formatToParts(date).reduce(function (acc, p) {
        acc[p.type] = p.value; return acc;
      }, {});
    }

    /* Find the UTC instant corresponding to a given wall-clock hour in a
       specific timezone (e.g. "7am today in America/Chicago"), without
       needing a timezone library. Standard offset-comparison trick. */
    function zonedHourToUtc(year, month, day, hour, minute, timeZone) {
      var guess = new Date(Date.UTC(year, month - 1, day, hour, minute));
      var parts = getPartsInTZ(guess, timeZone);
      var asIfUTC = Date.UTC(
        parseInt(parts.year, 10), parseInt(parts.month, 10) - 1, parseInt(parts.day, 10),
        parseInt(parts.hour, 10), parseInt(parts.minute, 10)
      );
      var diff = asIfUTC - guess.getTime();
      return new Date(guess.getTime() - diff);
    }

    function weekdayIndex(shortName) {
      return { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }[shortName];
    }

    function computeHoursState() {
      var now = new Date();
      var officeParts = getPartsInTZ(now, CFG.officeTimeZone);
      var hour = parseInt(officeParts.hour, 10);
      var day = weekdayIndex(officeParts.weekday);
      var daysOpen = CFG.daysOpen || [1, 2, 3, 4, 5, 6];
      var isOpen = daysOpen.indexOf(day) !== -1 && hour >= CFG.hoursStart && hour < CFG.hoursEnd;

      var y = parseInt(officeParts.year, 10), m = parseInt(officeParts.month, 10), d = parseInt(officeParts.day, 10);
      var openUtc = zonedHourToUtc(y, m, d, CFG.hoursStart, 0, CFG.officeTimeZone);
      var closeUtc = zonedHourToUtc(y, m, d, CFG.hoursEnd, 0, CFG.officeTimeZone);

      var localTimeFmt = new Intl.DateTimeFormat(undefined, { hour: 'numeric', minute: '2-digit' });
      return {
        isOpen: isOpen,
        openLocal: localTimeFmt.format(openUtc),
        closeLocal: localTimeFmt.format(closeUtc)
      };
    }

    function applyHoursUI() {
      var state;
      try {
        state = computeHoursState();
      } catch (e) {
        /* If Intl/timezone data isn't available, fail safe to "open" copy
           rather than showing broken text. */
        state = { isOpen: true, openLocal: '', closeLocal: '' };
      }

      document.querySelectorAll('[data-hours-status]').forEach(function (el) {
        el.textContent = state.isOpen
          ? 'Open now · closes ' + state.closeLocal + ' your time'
          : 'Closed · opens ' + state.openLocal + ' your time';
      });
      document.querySelectorAll('[data-cta-call-copy]').forEach(function (el) {
        el.textContent = state.isOpen ? 'Call now' : 'Call — leave a message';
      });
      document.querySelectorAll('[data-cta-callback-copy]').forEach(function (el) {
        el.textContent = state.isOpen
          ? 'Request a callback — within minutes'
          : 'Request a callback — first call at ' + state.openLocal;
      });
    }

    applyHoursUI();

    /* ---------- 3. Mobile nav + sticky CTA bar ---------- */
    var navToggle = document.querySelector('.nav-toggle');
    var navLinks = document.querySelector('.nav-links');
    if (navToggle && navLinks) {
      navToggle.addEventListener('click', function () {
        navLinks.classList.toggle('nav-open');
        navLinks.style.display = navLinks.classList.contains('nav-open') ? 'flex' : '';
      });
    }
    if (document.querySelector('.sticky-cta-bar')) {
      document.body.classList.add('has-sticky-cta');
    }

    /* ---------- 4. FAQ accordion ---------- */
    document.querySelectorAll('.faq-item').forEach(function (item) {
      var q = item.querySelector('.faq-q');
      if (!q) return;
      q.addEventListener('click', function () {
        var wasOpen = item.classList.contains('open');
        item.parentElement.querySelectorAll('.faq-item').forEach(function (i) { i.classList.remove('open'); });
        if (!wasOpen) item.classList.add('open');
      });
    });

    /* ---------- 5a. Callback micro-form (primary conversion action) ---------- */

    /* ---------- Bot protection (honeypot + time-trap) ----------
       Two lightweight, zero-dependency, zero-friction checks that catch
       the overwhelming majority of generic form-spam bots without adding
       any UX cost for real visitors:
       1. Honeypot: a field named "company" hidden off-screen via CSS
          (.hp-field). Real visitors never see or fill it; most bots that
          auto-fill every field in the DOM do.
       2. Time-trap: rejects submissions that arrive faster than a human
          could plausibly read the form and type into it.
       Flagged submissions are silently dropped — no lead notification
       fires — but the UI still shows the normal success state, so a bot
       gets no signal that it was caught and can't adapt around it.
       IMPORTANT: this is a client-side deterrent only. It stops generic
       bots, not a targeted attacker hitting the eventual submission
       endpoint directly. Once CallRail/a real backend is wired in
       (see placeholder below), pair this with server-side validation —
       Cloudflare Turnstile is the recommended next layer, since it can
       verify a token server-side and is lower-friction than reCAPTCHA. */
    function isLikelyBot(root, minMs) {
      var honeypot = root.querySelector('input[name="company"]');
      if (honeypot && honeypot.value.trim() !== '') return true;
      if (Date.now() - PAGE_LOAD_TIME < minMs) return true;
      return false;
    }

    /* Free lead delivery: POSTs to the Google Apps Script Web App set in
       config.js (see LEAD_NOTIFIER_SETUP.md). Uses mode:'no-cors' and a
       text/plain content-type on purpose — Apps Script Web Apps don't
       handle the CORS preflight a normal JSON fetch triggers, so this is
       the standard working pattern: the browser can't read the response,
       but the request still reaches the script and runs (appends the
       row, sends the email). If the URL is still the placeholder, this
       just logs instead of making a doomed network call. */
    function sendLeadWebhook(payload) {
      var url = CFG.leadWebhookUrl;
      if (!url || url.indexOf('PLACEHOLDER') !== -1) {
        console.log('[lead webhook] not configured yet, skipping send:', payload);
        return;
      }
      fetch(url, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'text/plain;charset=utf-8' },
        body: JSON.stringify(payload)
      }).catch(function (err) {
        console.log('[lead webhook] send failed:', err);
      });
    }

    document.querySelectorAll('[data-callback-form]').forEach(function (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var phoneInput = form.querySelector('input[name="callback_phone"]');
        if (!phoneInput || phoneInput.value.replace(/\D/g, '').length < 10) {
          if (phoneInput) phoneInput.closest('.field, .callback-form').classList.add('has-error');
          return;
        }
        var payload = {
          form_type: 'callback_requested',
          phone: phoneInput.value,
          name: (form.querySelector('input[name="callback_name"]') || {}).value || '',
          source: getStoredUtm(),
          timestamp: new Date().toISOString()
        };
        if (!isLikelyBot(form, 1500)) {
          console.log('[callback lead] notifying closer instantly:', payload);
          sendLeadWebhook(payload);
          pushEvent('callback_requested', payload);
        } else {
          console.log('[callback lead] blocked as likely bot, no closer notified:', payload);
        }
        form.innerHTML = '<div class="quote-success"><div class="check-circle">✓</div><h3>Got it — hang tight</h3><p>We’re calling ' + payload.phone + ' shortly.</p></div>';
      });
    });

    /* ---------- 5b. Multi-step quote calculator (tertiary/self-service path) ---------- */
    document.querySelectorAll('[data-quote-form]').forEach(initQuoteForm);

    function initQuoteForm(root) {
      var steps = Array.prototype.slice.call(root.querySelectorAll('.quote-step'));
      var bars = Array.prototype.slice.call(root.querySelectorAll('.qs-bar'));
      var current = 0;

      function render() {
        steps.forEach(function (s, i) { s.classList.toggle('active', i === current); });
        bars.forEach(function (b, i) {
          b.classList.toggle('done', i < current);
          b.classList.toggle('active', i === current);
        });
        var label = root.querySelector('.quote-progress-label');
        if (label && steps[current]) {
          var total = steps.length - (root.querySelector('.quote-success') ? 1 : 0);
          label.textContent = 'Step ' + Math.min(current + 1, total) + ' of ' + total;
        }
      }

      function validateStep(stepEl) {
        var valid = true;
        stepEl.querySelectorAll('input[required], select[required]').forEach(function (input) {
          var fieldWrap = input.closest('.field');
          var isValid = input.value.trim().length > 0;
          if (input.dataset.pattern === 'zip') isValid = /^\d{5}(-\d{4})?$/.test(input.value.trim());
          if (input.type === 'email') isValid = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value.trim());
          if (input.type === 'tel') isValid = input.value.replace(/\D/g, '').length >= 10;
          if (fieldWrap) fieldWrap.classList.toggle('has-error', !isValid);
          if (!isValid) valid = false;
        });
        stepEl.querySelectorAll('[data-choice-group]').forEach(function (group) {
          if (!group.querySelector('.choice-card.selected')) valid = false;
        });
        return valid;
      }

      root.addEventListener('click', function (e) {
        var nextBtn = e.target.closest('[data-quote-next]');
        var backBtn = e.target.closest('[data-quote-back]');
        var choiceCard = e.target.closest('.choice-card');

        if (choiceCard) {
          var group = choiceCard.closest('[data-choice-group]');
          group.querySelectorAll('.choice-card').forEach(function (c) { c.classList.remove('selected'); });
          choiceCard.classList.add('selected');
          var hiddenInput = group.querySelector('input[type="hidden"]');
          if (hiddenInput) hiddenInput.value = choiceCard.dataset.value || '';
        }

        if (nextBtn) {
          if (!validateStep(steps[current])) return;
          var eventName = current < steps.length - 1 ? 'quote_step_' + (current + 1) + '_complete' : 'quote_form_submitted';
          pushEvent(eventName, {});

          if (current === steps.length - 2) submitFullLead(root);
          current = Math.min(current + 1, steps.length - 1);
          render();
        }
        if (backBtn) { current = Math.max(current - 1, 0); render(); }
      });

      render();
    }

    function submitFullLead(root) {
      var data = { form_type: 'lead_captured', source: getStoredUtm(), timestamp: new Date().toISOString() };
      root.querySelectorAll('input, select').forEach(function (input) {
        if (input.name && input.name !== 'company') data[input.name] = input.value;
      });
      /* 4s minimum: a 4-step form can't be honestly filled faster than that. */
      if (!isLikelyBot(root, 4000)) {
        console.log('[full quote lead] notifying closer:', data);
        sendLeadWebhook(data);
        pushEvent('lead_captured', data);
      } else {
        console.log('[full quote lead] blocked as likely bot, no closer notified:', data);
      }
    }

    /* ---------- 5c. Custom date picker ----------
       Replaces the native <input type="date">, whose calendar popup is
       drawn entirely by the browser/OS — there's no CSS hook to resize
       or restyle it, which is exactly the "too squeezed, not smooth"
       complaint this replaces. Hand-built, no dependency, matches the
       rest of the site's dropdown pattern (see .dropdown-menu). */
    document.querySelectorAll('[data-datepicker]').forEach(initDatePicker);

    function initDatePicker(root) {
      var input = root.querySelector('input');
      var panel = root.querySelector('[data-datepicker-panel]');
      var label = root.querySelector('[data-dp-label]');
      var grid = root.querySelector('[data-dp-grid]');
      var prevBtn = root.querySelector('[data-dp-prev]');
      var nextBtn = root.querySelector('[data-dp-next]');
      if (!input || !panel || !grid) return;

      var monthNames = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
      var today = new Date();
      today.setHours(0, 0, 0, 0);
      var viewYear = today.getFullYear();
      var viewMonth = today.getMonth();
      var selected = null;

      function fmt(date) {
        return monthNames[date.getMonth()].slice(0, 3) + ' ' + date.getDate() + ', ' + date.getFullYear();
      }

      function render() {
        label.textContent = monthNames[viewMonth] + ' ' + viewYear;
        grid.innerHTML = '';
        var firstDay = new Date(viewYear, viewMonth, 1);
        var daysInMonth = new Date(viewYear, viewMonth + 1, 0).getDate();

        for (var i = 0; i < firstDay.getDay(); i++) {
          var blank = document.createElement('span');
          blank.className = 'dp-day dp-outside';
          grid.appendChild(blank);
        }
        var _loop = function (d) {
          var dayDate = new Date(viewYear, viewMonth, d);
          var btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'dp-day';
          btn.textContent = String(d);
          btn.setAttribute('aria-label', fmt(dayDate));
          if (dayDate.getTime() < today.getTime()) { btn.classList.add('dp-disabled'); btn.disabled = true; }
          if (dayDate.getTime() === today.getTime()) btn.classList.add('dp-today');
          if (selected && dayDate.getTime() === selected.getTime()) btn.classList.add('dp-selected');
          btn.addEventListener('click', function () {
            selected = dayDate;
            input.value = fmt(dayDate);
            var fieldWrap = input.closest('.field');
            if (fieldWrap) fieldWrap.classList.remove('has-error');
            closePanel();
          });
          grid.appendChild(btn);
        };
        for (var d = 1; d <= daysInMonth; d++) _loop(d);
      }

      function openPanel() { render(); panel.classList.add('dp-open'); }
      function closePanel() { panel.classList.remove('dp-open'); }

      input.addEventListener('click', function () {
        panel.classList.contains('dp-open') ? closePanel() : openPanel();
      });
      prevBtn.addEventListener('click', function () {
        viewMonth--; if (viewMonth < 0) { viewMonth = 11; viewYear--; }
        render();
      });
      nextBtn.addEventListener('click', function () {
        viewMonth++; if (viewMonth > 11) { viewMonth = 0; viewYear++; }
        render();
      });
      document.addEventListener('click', function (e) {
        if (!root.contains(e.target)) closePanel();
      });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closePanel();
      });
    }

    /* ---------- 6. UTM capture + tracking stubs ---------- */
    function getStoredUtm() {
      try { return JSON.parse(sessionStorage.getItem('uat_utm') || '{}'); }
      catch (e) { return {}; }
    }

    (function captureUtm() {
      var params = new URLSearchParams(window.location.search);
      var keys = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
      var existing = getStoredUtm();
      var hasNew = keys.some(function (k) { return params.get(k); });
      var data = hasNew ? {} : existing;
      if (hasNew) {
        keys.forEach(function (k) { if (params.get(k)) data[k] = params.get(k); });
        data.referrer = document.referrer || 'direct';
        data.landing_page = window.location.pathname;
        try { sessionStorage.setItem('uat_utm', JSON.stringify(data)); } catch (e) {}
      }
      document.querySelectorAll('[data-capture-utm] input[type="hidden"][data-utm-field]').forEach(function (el) {
        el.value = data[el.dataset.utmField] || '';
      });
    })();

    /* Event name mapping: internal → platform standard names */
    var GA4_EVENT_MAP = {
      call_click: 'generate_lead',
      callback_requested: 'generate_lead',
      lead_captured: 'generate_lead'
    };
    var META_EVENT_MAP = {
      call_click: 'Contact',
      callback_requested: 'Lead',
      lead_captured: 'Lead'
    };

    function pushEvent(name, detail) {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push(Object.assign({ event: name }, detail));
      console.log('[analytics]', name, detail);

      /* GA4: fire generic event, plus mapped conversion event */
      if (window.gtag) {
        window.gtag('event', name, detail);
        if (GA4_EVENT_MAP[name]) {
          window.gtag('event', GA4_EVENT_MAP[name], detail);
        }
      }

      /* Meta Pixel: fire mapped standard event */
      if (window.fbq && META_EVENT_MAP[name]) {
        window.fbq('track', META_EVENT_MAP[name]);
      }
    }

    /* Click-to-call tracking — fires before the tel: link navigates away */
    document.querySelectorAll('[data-track-call]').forEach(function (el) {
      el.addEventListener('click', function () {
        pushEvent('call_click', { source: getStoredUtm() });
        /* Production: also fire Google Ads / Meta conversion events here. */
      });
    });

  });
})();

/* =========================================================
   THIRD-PARTY SNIPPET PLACEHOLDERS
   Left commented so the sample doesn't ping real accounts with
   placeholder IDs. Uncomment and fill in before launch.

   CallRail (Dynamic Number Insertion + lead alerts):
   <script id="cr-swap" src="//cdn.callrail.com/companies/PLACEHOLDER/COMPANY_SCRIPT_ID/12/swap.js"></script>

   GA4:
   (function(){ var s=document.createElement('script'); s.async=true;
     s.src='https://www.googletagmanager.com/gtag/js?id=G-XXXXXXX';
     document.head.appendChild(s); window.dataLayer=window.dataLayer||[];
     function gtag(){dataLayer.push(arguments);} gtag('js', new Date());
     gtag('config','G-XXXXXXX'); })();

   Meta Pixel: standard base pixel code, then fbq('track','Lead') on
   callback_requested / lead_captured / call_click events above.

   Cloudflare Turnstile (stronger bot protection, optional next layer):
   the honeypot + time-trap checks above (see isLikelyBot) stop generic
   spam bots with zero user friction and no account needed. Turnstile
   adds a much harder-to-fake invisible challenge, but only provides
   real protection once there's a backend to verify its token
   server-side — add it once CallRail/a real submission endpoint is
   wired in, not before:
   <script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
   <div class="cf-turnstile" data-sitekey="PLACEHOLDER_SITE_KEY"></div>
   ========================================================= */

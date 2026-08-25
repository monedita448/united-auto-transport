/* =========================================================
   UNITED AUTO TRANSPORT — HERO ROUTE MAP
   Vanilla JS, no dependencies. Builds the decorative pickup → delivery
   route map into the #heroMap <svg> declared in index.html, behind the
   headline and the callback card (.hero-navy/.hero-map in style.css).
   Kept as its own small file rather than folded into main.min.js so it
   can be reviewed, disabled, or removed independently of the rest of
   the site's tracking/form/nav logic.
   Shipped separately from main.js on purpose — it's the one script on
   the page that's purely decorative, so it's the one safe to drop
   without touching anything that captures a lead.
   ========================================================= */
(function () {
  var svg = document.getElementById('heroMap');
  if (!svg) return;

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var NS = 'http://www.w3.org/2000/svg';
  function el(tag) { return document.createElementNS(NS, tag); }

  // Positions are illustrative (relative placement, not surveyed lat/long).
  var cities = [
    { n: 'SEATTLE', x: 60, y: 40 }, { n: 'PORTLAND', x: 55, y: 75 }, { n: 'SAN FRANCISCO', x: 48, y: 230 },
    { n: 'LOS ANGELES', x: 120, y: 320 }, { n: 'SAN DIEGO', x: 140, y: 345 }, { n: 'PHOENIX', x: 225, y: 330 },
    { n: 'DENVER', x: 345, y: 195 }, { n: 'SALT LAKE CITY', x: 230, y: 175 }, { n: 'DALLAS', x: 490, y: 345 },
    { n: 'HOUSTON', x: 510, y: 405 }, { n: 'MINNEAPOLIS', x: 550, y: 85 }, { n: 'CHICAGO', x: 645, y: 150 },
    { n: 'KANSAS CITY', x: 525, y: 210 }, { n: 'NASHVILLE', x: 660, y: 270 }, { n: 'ATLANTA', x: 700, y: 320 },
    { n: 'MIAMI', x: 775, y: 490 }, { n: 'DETROIT', x: 725, y: 140 }, { n: 'WASHINGTON DC', x: 825, y: 210 },
    { n: 'NEW YORK', x: 875, y: 165 }, { n: 'BOSTON', x: 930, y: 140 }
  ];

  var routes = [
    { a: { n: 'SEATTLE', x: 60, y: 40 }, b: { n: 'DALLAS', x: 490, y: 345 }, d: 'M60,40 Q275,98 490,345' },
    { a: { n: 'LOS ANGELES', x: 120, y: 320 }, b: { n: 'NEW YORK', x: 875, y: 165 }, d: 'M120,320 Q497,104 875,165' }
  ];

  // Deterministic ambient scatter so the map looks identical on every load/SSR.
  var seed = 42;
  function rnd() { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; }
  for (var i = 0; i < 100; i++) {
    var dot = el('circle');
    dot.setAttribute('class', 'hero-map-dot');
    dot.setAttribute('cx', (rnd() * 1000).toFixed(1));
    dot.setAttribute('cy', (rnd() * 460).toFixed(1));
    dot.setAttribute('r', (0.8 + rnd() * 1.1).toFixed(2));
    svg.appendChild(dot);
  }

  var active = {};
  routes.forEach(function (r) { active[r.a.n] = true; active[r.b.n] = true; });
  cities.forEach(function (c) {
    var dot = el('circle');
    dot.setAttribute('class', 'hero-map-city');
    dot.setAttribute('cx', c.x);
    dot.setAttribute('cy', c.y);
    dot.setAttribute('r', active[c.n] ? 0 : 2.6);
    svg.appendChild(dot);
  });

  routes.forEach(function (r, idx) {
    var glow = el('path'); glow.setAttribute('class', 'hero-route-glow'); glow.setAttribute('d', r.d); svg.appendChild(glow);
    var line = el('path'); line.setAttribute('class', 'hero-route-line'); line.setAttribute('d', r.d); svg.appendChild(line);

    var pick = el('circle');
    pick.setAttribute('class', 'hero-node-pickup'); pick.setAttribute('cx', r.a.x); pick.setAttribute('cy', r.a.y); pick.setAttribute('r', 4.5);
    svg.appendChild(pick);
    var pickPing = el('circle');
    pickPing.setAttribute('class', 'hero-ping'); pickPing.setAttribute('cx', r.a.x); pickPing.setAttribute('cy', r.a.y); pickPing.setAttribute('r', 4.5);
    svg.appendChild(pickPing);

    var drop = el('circle');
    drop.setAttribute('class', 'hero-node-delivery'); drop.setAttribute('cx', r.b.x); drop.setAttribute('cy', r.b.y); drop.setAttribute('r', 5.5);
    svg.appendChild(drop);
    var dropPing = el('circle');
    dropPing.setAttribute('class', 'hero-ping b'); dropPing.setAttribute('cx', r.b.x); dropPing.setAttribute('cy', r.b.y); dropPing.setAttribute('r', 5.5);
    svg.appendChild(dropPing);

    [r.a, r.b].forEach(function (c) {
      var t = el('text');
      t.setAttribute('class', 'hero-city-label');
      t.setAttribute('x', c.x + 9);
      t.setAttribute('y', c.y + 3.5);
      t.textContent = c.n;
      svg.appendChild(t);
    });

    if (!reduced) {
      var trav = el('circle');
      trav.setAttribute('class', 'hero-traveler' + (idx === 1 ? ' b' : ''));
      trav.setAttribute('r', 3.6);
      trav.style.offsetPath = "path('" + r.d + "')";
      svg.appendChild(trav);
    }
  });
})();

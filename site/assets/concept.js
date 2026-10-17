/* J&W Foods concept prototypes: shared chrome and demo engine (window.JWC).
   Every prototype page loads, in order: ../assets/site-data.js (window.JW: plays, agents, money), ../assets/catalog.js
   (window.JWCAT: real JW products), ../assets/concept.js, then calls JWC.init({ n: <play number> , ... }).
   Nothing here talks to a server: carts, orders, subscriptions and chat are simulated and stored on this device only. */
(function () {
  'use strict';
  var JWC = window.JWC = {};
  var NS = 'jwdemo:';
  if (/[?&]shot=1/.test(location.search)) document.documentElement.classList.add('jwc-shot');
  var state = { n: 0, opts: {}, cartListeners: [], chat: null };

  /* ---------- small utilities ---------- */
  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  JWC.esc = esc;
  JWC.money = function (v, dp) {
    if (v == null || isNaN(v)) return '';
    var d = dp == null ? (Math.round(v) === v && Math.abs(v) >= 100 ? 0 : 2) : dp;
    var a = Math.abs(Number(v)), r = Math.round(a * Math.pow(10, d)) / Math.pow(10, d);
    return (v < 0 && r > 0 ? '\u2212' : '') + '$' + r.toLocaleString('en-CA', { minimumFractionDigits: d, maximumFractionDigits: d });
  };
  /* $380K, $1.2M */
  JWC.short = function (v) {
    if (v == null || isNaN(v)) return '';
    var a = Math.abs(v), s = v < 0 ? '-' : '';
    if (a >= 1e6) return s + '$' + (Math.round(a / 1e5) / 10) + 'M';
    if (a >= 1e3) { var k = a / 1e3; return s + '$' + (k < 100 && Math.round(k) !== k ? Math.round(k * 10) / 10 : Math.round(k)) + 'K'; }
    return s + '$' + Math.round(a);
  };
  JWC.store = {
    get: function (k, d) { try { var v = localStorage.getItem(NS + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(NS + k, JSON.stringify(v)); } catch (e) { /* storage blocked: demo still works for this visit */ } },
    del: function (k) { try { localStorage.removeItem(NS + k); } catch (e) {} },
    clearAll: function () { try { Object.keys(localStorage).forEach(function (k) { if (k.indexOf(NS) === 0) localStorage.removeItem(k); }); } catch (e) {} }
  };
  function el(html) { var t = document.createElement('template'); t.innerHTML = html.trim(); return t.content.firstElementChild; }
  JWC.el = el;
  /* Shortlist of prototypes the owners like, shared with the hub page (index.html reads the same key) */
  JWC.picks = function () { try { var a = JSON.parse(localStorage.getItem('jw-picks') || '[]'); return Array.isArray(a) ? a : []; } catch (e) { return []; } };
  JWC.togglePick = function (n) { var a = JWC.picks(), i = a.indexOf(n); if (i > -1) a.splice(i, 1); else a.push(n); a.sort(function (x, y) { return x - y; }); try { localStorage.setItem('jw-picks', JSON.stringify(a)); } catch (e) {} return i < 0; };
  JWC.uid = function (p) { return (p || 'id') + '-' + Math.random().toString(36).slice(2, 8); };

  /* ---------- catalog helpers ---------- */
  JWC.products = function (cat) { var all = window.JWCAT || []; return cat ? all.filter(function (p) { return p.cat === cat; }) : all.slice(); };
  JWC.product = function (id) { return (window.JWCAT || []).filter(function (p) { return p.id === id; })[0] || null; };
  /* Illustrative macros for one unit of a product variant: {kcal,p,c,f} rounded. */
  JWC.macros = function (prod, vi) {
    if (!prod) return null;
    var v = prod.variants[vi || 0] || prod.variants[0];
    if (prod.perUnit) return round(prod.perUnit, 1);
    if (prod.perOz && v && v.oz) return round(prod.perOz, v.oz);
    return null;
    function round(m, k) { return { kcal: Math.round(m.kcal * k), p: Math.round(m.p * k), c: Math.round(m.c * k), f: Math.round(m.f * k) }; }
  };
  JWC.img = function (prod, w) { if (!prod || !prod.img) return ''; return w ? prod.img.replace(/width=\d+/, 'width=' + w) : prod.img; };

  /* ---------- real delivery routes (jwfoods.com/pages/home, Oct 2026) ---------- */
  var ROUTES = [
    { id: 'pickup', name: 'Pick up at the Brimley Rd store', day: 'Ready in 2–3 business days', fee: 0, min: 1, cities: ['*'] },
    { id: 'express', name: 'Express delivery (1–2 business days)', day: '1–2 business days', fee: 30, min: 100, cities: ['Scarborough', 'North York', 'Toronto', 'East York', 'Etobicoke', 'Richmond Hill', 'Markham', 'Vaughan'] },
    { id: 'gta1', name: 'GTA 1 · Tuesday route', day: 'Tuesday', fee: 20, min: 100, cities: ['Pickering', 'Ajax', 'Whitby', 'Oshawa', 'Bowmanville', 'Brock', 'Clarington', 'Port Perry', 'Uxbridge', 'Newcastle', 'Stouffville'] },
    { id: 'gta2', name: 'GTA 2 · Wednesday route', day: 'Wednesday', fee: 20, min: 100, cities: ['Scarborough', 'North York', 'Toronto', 'East York', 'Etobicoke', 'Mississauga'] },
    { id: 'gta2x', name: 'Wednesday long route', day: 'Wednesday', fee: 35, min: 100, cities: ['Guelph', 'Kawarthas', 'Peterborough', 'Port Hope', 'St. Catharines', 'Brighton'] },
    { id: 'gta3', name: 'GTA 3 · Thursday route', day: 'Thursday', fee: 27, min: 100, cities: ['Oakville', 'Burlington', 'Hamilton', 'Milton'] },
    { id: 'gta4', name: 'GTA 4 · Friday route', day: 'Friday', fee: 20, min: 100, cities: ['Brampton', 'Caledon', 'Halton Hills', 'Kleinburg', 'Vaughan', 'Woodbridge', 'Aurora', 'Newmarket', 'Markham', 'Richmond Hill'] },
    { id: 'gta4g', name: 'GTA 4 · Friday route', day: 'Friday', fee: 25, min: 100, cities: ['East Gwillimbury', 'West Gwillimbury'] },
    { id: 'gta4x', name: 'Friday long route', day: 'Friday', fee: 35, min: 100, cities: ['Barrie', 'Brantford', 'Sutton', 'King City', 'London', 'Sarnia', 'Windsor', 'Niagara Falls', 'Ottawa', 'Kingston', 'Parry Sound'] }
  ];
  JWC.routes = ROUTES;
  JWC.cities = function () {
    var s = {}; ROUTES.forEach(function (r) { r.cities.forEach(function (c) { if (c !== '*') s[c] = 1; }); });
    return Object.keys(s).sort();
  };
  /* All ways to get an order to this city, pickup first */
  JWC.routesFor = function (city) {
    return ROUTES.filter(function (r) { return r.cities.indexOf('*') > -1 || r.cities.indexOf(city) > -1; });
  };
  JWC.findCity = function (text) {
    var t = String(text || '').toLowerCase();
    return JWC.cities().filter(function (c) { return t.indexOf(c.toLowerCase()) > -1; })[0] || null;
  };
  JWC.business = {
    name: 'J&W Foods · Meal Butler', address: '2201 Brimley Rd, Unit 1, Scarborough, ON M1S 4N7', phone: '(416) 298-1350',
    hours: 'Mon–Fri 9am–6pm · Sat 10am–4pm · Sun closed', cutoff: 'Order by Sunday for next week’s route delivery'
  };

  /* ---------- toast ---------- */
  JWC.toast = function (msg, ms) {
    var box = document.querySelector('.jwc-toasts');
    if (!box) { box = el('<div class="jwc-toasts" role="status" aria-live="polite"></div>'); document.body.appendChild(box); }
    var t = el('<div class="jwc-toast"></div>'); t.textContent = msg; box.appendChild(t);
    setTimeout(function () { t.remove(); }, ms || 2600);
  };

  /* ---------- overlay, panels, modal ---------- */
  var overlay, lastFocus;
  function ensureOverlay() {
    if (overlay) return overlay;
    overlay = el('<div class="jwc-overlay" aria-hidden="true"></div>');
    overlay.addEventListener('click', JWC.closeAll);
    document.body.appendChild(overlay);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') JWC.closeAll(); });
    return overlay;
  }
  JWC.openPanel = function (panel) {
    ensureOverlay(); JWC.closeAll(true); lastFocus = document.activeElement;
    overlay.classList.add('on'); panel.classList.add('on'); panel.setAttribute('aria-hidden', 'false');
    var f = panel.querySelector('button, [href], input, select, textarea'); if (f) setTimeout(function () { f.focus(); }, 30);
  };
  JWC.closeAll = function (keepFocus) {
    document.querySelectorAll('.jwc-panel.on, .jwc-modal.on').forEach(function (p) { p.classList.remove('on'); p.setAttribute('aria-hidden', 'true'); });
    if (overlay) overlay.classList.remove('on');
    if (keepFocus !== true && lastFocus && lastFocus.focus) { try { lastFocus.focus(); } catch (e) {} }
  };
  var modalEl;
  /* JWC.modal(html, onMount) opens a centred dialog. Any [data-close] inside closes it. */
  JWC.modal = function (html, onMount) {
    ensureOverlay();
    if (!modalEl) { modalEl = el('<div class="jwc-modal" role="dialog" aria-modal="true" aria-hidden="true"><div class="jwc-modal-in"></div></div>'); document.body.appendChild(modalEl); }
    var anyOpen = document.querySelector('.jwc-panel.on, .jwc-modal.on');
    if (!anyOpen) lastFocus = document.activeElement;
    JWC.closeAll(true);
    var inner = modalEl.firstElementChild; inner.innerHTML = html;
    inner.querySelectorAll('[data-close]').forEach(function (b) { b.addEventListener('click', function () { JWC.closeAll(); }); });
    overlay.classList.add('on'); modalEl.classList.add('on'); modalEl.setAttribute('aria-hidden', 'false');
    if (onMount) onMount(inner);
    var f = inner.querySelector('input, select, textarea, button'); if (f) setTimeout(function () { f.focus(); }, 30);
    return inner;
  };

  /* ---------- cart ---------- */
  function cartKey() { return 'cart:' + (state.n || 'x'); }
  JWC.cart = {
    items: function () { return JWC.store.get(cartKey(), []); },
    save: function (items) { JWC.store.set(cartKey(), items); renderCart(); state.cartListeners.forEach(function (fn) { try { fn(items); } catch (e) {} }); },
    /* item: {id, name, variant, price, qty, img, note} - same id+variant merges */
    add: function (item, silent) {
      var items = JWC.cart.items(), key = item.id + '|' + (item.variant || '');
      var found = items.filter(function (i) { return i.key === key; })[0];
      if (found) found.qty += item.qty || 1; else items.push({ key: key, id: item.id, name: item.name, variant: item.variant || '', price: +item.price, qty: item.qty || 1, img: item.img || '', note: item.note || '' });
      JWC.cart.save(items); if (!silent) JWC.toast('Added: ' + item.name + (item.variant ? ' · ' + item.variant : ''));
    },
    setQty: function (key, q) { var items = JWC.cart.items().map(function (i) { if (i.key === key) i.qty = Math.max(0, q); return i; }).filter(function (i) { return i.qty > 0; }); JWC.cart.save(items); },
    clear: function () { JWC.cart.save([]); },
    count: function () { return JWC.cart.items().reduce(function (a, i) { return a + i.qty; }, 0); },
    subtotal: function () { return JWC.cart.items().reduce(function (a, i) { return a + i.qty * i.price; }, 0); },
    onChange: function (fn) { state.cartListeners.push(fn); },
    open: function () { renderCart(); JWC.openPanel(document.getElementById('jwc-cart')); }
  };
  function renderCart() {
    var fab = document.querySelector('.jwc-cart-fab'), panel = document.getElementById('jwc-cart');
    if (!panel) return;
    var items = JWC.cart.items(), n = JWC.cart.count(), sub = JWC.cart.subtotal();
    if (fab) { fab.classList.toggle('on', n > 0); fab.querySelector('span').textContent = n; fab.setAttribute('aria-label', 'Open cart, ' + n + ' items, ' + JWC.money(sub)); }
    var body = panel.querySelector('.jwc-panel-body');
    body.innerHTML = items.length ? items.map(function (i) {
      return '<div class="jwc-line">' + (i.img ? '<img src="' + esc(i.img) + '" alt="">' : '<span></span>') +
        '<div><div class="t">' + esc(i.name) + '</div><div class="s">' + esc(i.variant) + (i.note ? ' · ' + esc(i.note) : '') + ' · ' + JWC.money(i.price) + '</div></div>' +
        '<div class="jwc-qty"><button type="button" data-k="' + esc(i.key) + '" data-d="-1" aria-label="One less ' + esc(i.name) + '">−</button><output>' + i.qty + '</output><button type="button" data-k="' + esc(i.key) + '" data-d="1" aria-label="One more ' + esc(i.name) + '">+</button></div></div>';
    }).join('') : '<p style="color:var(--jwc-muted)">Your cart is empty. Add a few portions to try the demo checkout.</p>';
    body.querySelectorAll('[data-k]').forEach(function (b) {
      b.addEventListener('click', function () { var it = JWC.cart.items().filter(function (i) { return i.key === b.dataset.k; })[0]; if (it) JWC.cart.setQty(it.key, it.qty + (+b.dataset.d)); });
    });
    panel.querySelector('.jwc-cart-sub').textContent = JWC.money(sub);
    panel.querySelector('.jwc-cart-go').disabled = !items.length;
  }

  /* ---------- orders (demo) ---------- */
  JWC.orders = function () { return JWC.store.get('orders', []); };
  JWC.addOrder = function (o) { var all = JWC.orders(); all.unshift(o); JWC.store.set('orders', all.slice(0, 200)); return o; };
  JWC.nextOrderNo = function () { var n = JWC.store.get('orderSeq', 10480) + 1; JWC.store.set('orderSeq', n); return 'JW-' + n; };
  /* Remember the shopper's town so every checkout opens on it (pages may call JWC.setCity from their own pickers) */
  JWC.setCity = function (c) { JWC.store.set('city', c || ''); };

  /* ---------- checkout ----------
     JWC.checkout({ title, items (defaults to cart), subscription: {label:'Every week', discountPct:10} | null,
                    extraRows: [{label, amount}], note, onPlaced(order) }) */
  JWC.checkout = function (opts) {
    opts = opts || {};
    var items = opts.items || JWC.cart.items();
    if (!items.length) { JWC.toast('Add something first'); return; }
    var sub = Math.round(items.reduce(function (a, i) { return a + i.qty * i.price; }, 0) * 100) / 100;
    var disc = opts.subscription && opts.subscription.discountPct ? Math.round(sub * opts.subscription.discountPct) / 100 : 0;
    function rowsFor(route) { var r = typeof opts.extraRows === 'function' ? opts.extraRows(route) : opts.extraRows; return r || []; }
    var cities = JWC.cities(), startCity = opts.city != null ? opts.city : JWC.store.get('city', '');
    var html = '<h3>' + esc(opts.title || 'Checkout') + '</h3>' +
      '<p style="margin:0 0 10px;color:var(--jwc-muted);font-size:13.5px">Demo checkout: nothing is sent or charged. Routes and fees are JW’s real ones.</p>' +
      '<label class="jwc-field"><span>Where should it go?</span><select id="jwc-city"><option value="">Pick up at 2201 Brimley Rd (free)</option>' +
      cities.map(function (c) { return '<option' + (c === startCity ? ' selected' : '') + '>' + esc(c) + '</option>'; }).join('') + '</select></label>' +
      '<div id="jwc-routes"></div>' +
      (opts.note ? '<p style="margin:6px 0 0;font-size:13px;color:var(--jwc-muted)">' + esc(opts.note) + '</p>' : '') +
      (opts.subscription ? '<div class="jwc-note" style="margin-top:6px"><span class="jwc-dot"></span><span><b style="color:var(--jwc-ink)">' + esc(opts.subscription.label || 'Subscription') + '.</b> Skip, swap or pause any week before the Sunday cut-off. ' + (opts.subscription.discountPct ? opts.subscription.discountPct + '% off every box.' : '') + '</span></div>' : '') +
      '<div style="margin-top:12px" id="jwc-sum"></div>' +
      '<div class="jwc-democard" style="margin-top:12px"><span aria-hidden="true">💳</span><span>Demo payment · <b>DEMO •••• 4242</b> · nothing is charged</span></div>' +
      '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:14px"><button type="button" class="jwc-btn jwc-btn-line" data-close>Back</button><button type="button" class="jwc-btn jwc-btn-dark" id="jwc-place">Place demo order</button></div>';
    JWC.modal(html, function (root) {
      var citySel = root.querySelector('#jwc-city'), routesBox = root.querySelector('#jwc-routes'), sumBox = root.querySelector('#jwc-sum'), place = root.querySelector('#jwc-place');
      var chosen = null;
      function draw() {
        var city = citySel.value, rs = city ? JWC.routesFor(city).filter(function (r) { return r.id !== 'pickup'; }) : [ROUTES[0]];
        /* weekly routes first (cheapest first), express last; a page can prefer a route id with opts.route */
        rs = rs.slice().sort(function (a, b) { return (a.id === 'express') - (b.id === 'express') || a.fee - b.fee; });
        if (!chosen || rs.indexOf(chosen) < 0) chosen = rs.filter(function (r) { return r.id === opts.route; })[0] || rs[0];
        routesBox.innerHTML = rs.map(function (r, i) {
          return '<label class="jwc-choice"><input type="radio" name="jwc-route" value="' + i + '"' + (r === chosen ? ' checked' : '') + '><span><b>' + esc(r.name) + '</b><br><small style="color:var(--jwc-muted)">' + esc(r.day) + ' · ' + (r.fee ? JWC.money(r.fee, 2) + ' fee' : 'free') + (r.min > 1 ? ' · ' + JWC.money(r.min, 0) + ' minimum' : '') + '</small></span></label>';
        }).join('');
        routesBox.querySelectorAll('input').forEach(function (inp) { inp.addEventListener('change', function () { chosen = rs[+inp.value]; draw(); }); });
        var rows = rowsFor(chosen), extra = rows.reduce(function (a, r) { return a + (+r.amount || 0); }, 0);
        var oneTime = rows.some(function (r) { return +r.amount < 0 || r.oneTime; });
        var fee = chosen ? chosen.fee : 0, total = Math.round((sub - disc + extra + fee) * 100) / 100, below = chosen && sub - disc < chosen.min;
        sumBox.innerHTML = '<div class="jwc-row"><span>Items (' + items.reduce(function (a, i) { return a + i.qty; }, 0) + ')</span><span>' + JWC.money(sub, 2) + '</span></div>' +
          (disc ? '<div class="jwc-row" style="color:var(--jwc-gain)"><span>Subscribe &amp; save</span><span>−' + JWC.money(disc, 2) + '</span></div>' : '') +
          rows.map(function (r) { return '<div class="jwc-row"><span>' + esc(r.label) + '</span><span>' + JWC.money(+r.amount, 2) + '</span></div>'; }).join('') +
          '<div class="jwc-row"><span>' + (chosen && chosen.id === 'pickup' ? 'Pickup' : 'Delivery') + '</span><span>' + (fee ? JWC.money(fee, 2) : 'Free') + '</span></div>' +
          '<div class="jwc-row total"><span>Total' + (opts.subscription ? (oneTime ? ', first delivery' : ' per delivery') : '') + '</span><span>' + JWC.money(total, 2) + '</span></div>' +
          (below ? '<p style="color:var(--jwc-warn);font-size:13px;margin:6px 0 0">This route has a ' + JWC.money(chosen.min, 0) + ' minimum. Add ' + JWC.money(chosen.min - (sub - disc), 2) + ' more, or choose pickup.</p>' : '');
        place.disabled = !!below;
        place._total = total; place._fee = fee;
      }
      citySel.addEventListener('change', function () { chosen = null; JWC.setCity(citySel.value); draw(); });
      draw();
      place.addEventListener('click', function () {
        var no = JWC.nextOrderNo();
        var order = JWC.addOrder({
          no: no, proto: state.n, when: new Date().toISOString(), city: citySel.value || 'Pickup', route: chosen ? chosen.name : '', day: chosen ? chosen.day : '',
          items: items, subtotal: sub, discount: disc, fee: place._fee, total: place._total, subscription: opts.subscription || null, note: opts.note || ''
        });
        if (!opts.items) JWC.cart.clear();
        JWC.modal('<h3>Order ' + esc(no) + ' is in</h3><p style="color:var(--jwc-muted);margin:0 0 12px">' + (chosen && chosen.id === 'pickup' ? 'We’ll email you when it’s ready at Brimley Rd.' : 'Arriving on the ' + esc(chosen.day) + ' route to ' + esc(citySel.value) + '.') + ' This is a demo, so nothing was charged and nothing was sent.</p>' +
          '<div class="jwc-note" style="margin-top:0"><span class="jwc-dot"></span><span>Switch to <b style="color:var(--jwc-ink)">JW team view</b> in the dark bar to see this order land on the team side.</span></div>' +
          '<div style="margin-top:14px"><button type="button" class="jwc-btn jwc-btn-dark jwc-btn-block" data-close>Done</button></div>');
        if (opts.onPlaced) try { opts.onPlaced(order); } catch (e) {}
        document.dispatchEvent(new CustomEvent('jwc:order', { detail: order }));
      });
    });
  };

  /* ---------- AI chat (scripted) ----------
     JWC.chat.configure({ name, role, greeting, suggestions: [..], rules: [{ match: /regex/i, reply: 'text' | function(text) -> 'text' | {text, action:{label, run}} }] }) */
  var BASE_RULES = [
    { match: /\b(hours?|open|opening|close|closing|sunday|saturday)\b/i, reply: function () { return 'The Brimley Rd store is open ' + JWC.business.hours + '. Online orders can be placed any time; ' + JWC.business.cutoff.toLowerCase() + '.'; } },
    { match: /\b(where|address|location|pick ?up|store)\b/i, reply: function () { return 'We’re at ' + JWC.business.address + ' (' + JWC.business.phone + '). Pickup is free on any order, ready in 2–3 business days.'; } },
    { match: /\b(deliver|delivery|route|ship|come to|fee)\b/i, reply: function (t) {
        var c = JWC.findCity(t);
        if (!c) return 'We deliver across the GTA on weekly routes (Tue Durham, Wed Toronto & Mississauga, Thu Halton & Hamilton, Fri York & Peel) for $20–$35 with a $100 minimum, plus $30 express (1–2 business days) in Toronto, Scarborough, North York, East York, Etobicoke, Richmond Hill, Markham and Vaughan. Which city are you in?';
        var rs = JWC.routesFor(c).filter(function (r) { return r.id !== 'pickup'; });
        return c + ': ' + rs.map(function (r) { return r.day + ' (' + JWC.money(r.fee, 0) + ', ' + JWC.money(r.min, 0) + ' min)'; }).join(' or ') + '. ' + JWC.business.cutoff + '.';
      } },
    { match: /\b(salt|sugar|oil|sodium|clean|additive)/i, reply: 'Every Meal Butler portion is cooked with no added salt, no sugar and no added oils, then weighed, flash-frozen and vacuum-sealed in BPA-free bags. Flavoured items (Jerk, Teriyaki, Korean BBQ) use our own marinades, so check the label if you’re strict.' },
    { match: /\b(protein|macro|calorie|cut|bulk|lose|weight|gain|muscle)\b/i, reply: function () {
        var p = JWC.product('chicken-breast-souvlaki') || (window.JWCAT || [])[0];
        var m = p ? JWC.macros(p, 0) : null;
        return 'For a lean week most people start with 2 proteins + 1 carb + 1 veg per meal. A 4oz Chicken Breast Souvlaki is about ' + (m ? m.p + 'g protein and ' + m.kcal + ' kcal' : '35g protein') + ' (estimate). Tell me your goal and how many meals a day, and I’ll build a cart.';
      } },
    { match: /\b(chicken|hormone|antibiotic|local|ontario|organic|grass)/i, reply: 'Our chicken is air-chilled, grain-fed and raised in Ontario without hormones or antibiotics. We’ve been an Ontario-inspected meat plant since 2008, so we cut, cook and pack in-house.' },
    { match: /\b(price|cost|cheap|expensive|deal|discount|promo)\b/i, reply: 'Cooked chicken breast starts at $3.14 a portion, salmon at $7.99, sides from $0.66. Bigger savings come from cases (4 kg of portioned chicken breast is $85–$92) and the boxed specials.' },
    { match: /\b(freeze|frozen|thaw|reheat|microwave|air ?fry|shelf)/i, reply: 'Portions are flash-frozen in vacuum-sealed bags, so they keep for months in the freezer. Thaw in the fridge, then heat in the bag in simmering water, or in the microwave or air fryer. Each bag has its own heating steps.' },
    { match: /\b(gift|card|present)\b/i, reply: 'We sell digital gift cards and boxed specials (Gentleman’s Box $129.99, A Taste of Greece $130, Long Weekend Box $199).' },
    { match: /\b(wholesale|bulk|case|restaurant|gym|team|corporate|office|catering)\b/i, reply: 'We’ve supplied restaurants since the family started Advance Food Products in 1973. For gyms, teams, offices and restaurants we do case pricing and standing weekly orders. Want me to pass your details to the team?' },
    { match: /\b(human|person|call|phone|talk|agent)\b/i, reply: function () { return 'Of course. Call ' + JWC.business.phone + ' (' + JWC.business.hours + '), or leave your number here and someone from the counter calls you back the same day.'; } },
    { match: /\b(hi|hello|hey|good (morning|afternoon|evening))\b/i, reply: 'Hi! Ask me about portions, macros, delivery days in your city or what to order for the week.' }
  ];
  JWC.chat = {
    configure: function (cfg) { state.chat = cfg || {}; buildChat(); },
    open: function (q) { var c = document.getElementById('jwc-chat'); if (!c) return; c.classList.add('on'); var i = c.querySelector('input'); if (q) { send(q); } else if (i) i.focus(); },
    close: function () { var c = document.getElementById('jwc-chat'); if (c) c.classList.remove('on'); },
    say: function (text) { addMsg('bot', text); }
  };
  function addMsg(who, text, action) {
    var log = document.querySelector('#jwc-chat .jwc-chat-log'); if (!log) return null;
    var m = el('<div class="jwc-msg ' + who + '"></div>'); m.textContent = text;
    if (action && action.label) { var b = el('<button type="button" class="act"></button>'); b.textContent = action.label; b.addEventListener('click', function () { try { action.run(); } catch (e) {} }); m.appendChild(document.createElement('br')); m.appendChild(b); }
    log.appendChild(m); log.scrollTop = log.scrollHeight; return m;
  }
  function answer(text) {
    var rules = ((state.chat && state.chat.rules) || []).concat(BASE_RULES);
    for (var i = 0; i < rules.length; i++) {
      if (rules[i].match.test(text)) { var r = rules[i].reply; return typeof r === 'function' ? r(text) : r; }
    }
    return (state.chat && state.chat.fallback) || 'Good question. In the live version I would answer from JW’s approved product sheets and hand anything tricky to the team at the counter. Try asking about delivery days, macros, prices or what to order for the week.';
  }
  function send(text) {
    text = String(text || '').trim(); if (!text) return;
    addMsg('me', text);
    var typing = addMsg('bot typing', 'typing…');
    setTimeout(function () {
      if (typing) typing.remove();
      var a = answer(text);
      if (a && typeof a === 'object') addMsg('bot', a.text, a.action); else addMsg('bot', a);
    }, 550 + Math.min(900, text.length * 12));
  }
  function buildChat() {
    var cfg = state.chat || {};
    var old = document.getElementById('jwc-chat'); if (old) old.remove();
    var oldFab = document.querySelector('.jwc-chat-fab'); if (oldFab) oldFab.remove();
    var name = cfg.name || 'Ask the Butler';
    var fab = el('<button type="button" class="jwc-chat-fab" aria-haspopup="dialog"><i aria-hidden="true"></i><span></span></button>');
    fab.querySelector('span').textContent = cfg.fabLabel || name;
    var box = el('<section id="jwc-chat" class="jwc-chat" role="dialog" aria-label="' + esc(name) + ' chat">' +
      '<div class="jwc-chat-head"><span class="av" aria-hidden="true">JW</span><div><b></b><small></small></div><button type="button" class="jwc-x" aria-label="Close chat">×</button></div>' +
      '<div class="jwc-chat-log" aria-live="polite"></div><div class="jwc-sugs"></div>' +
      '<form><label class="jwc-sr" for="jwc-chat-in">Message</label><input id="jwc-chat-in" autocomplete="off" placeholder="Ask about portions, macros, delivery…"><button>Send</button></form>' +
      '<div class="jwc-chat-note">AI agent demo · replies are scripted · nothing is sent</div></section>');
    box.querySelector('b').textContent = name;
    box.querySelector('small').textContent = cfg.role || 'AI concierge · answers from JW’s own product sheets';
    box.querySelector('.jwc-x').addEventListener('click', JWC.chat.close);
    box.querySelector('form').addEventListener('submit', function (e) { e.preventDefault(); var i = box.querySelector('input'); send(i.value); i.value = ''; });
    var sugs = box.querySelector('.jwc-sugs');
    (cfg.suggestions || ['What day do you deliver to Mississauga?', 'Is the chicken hormone-free?', 'Build me a high-protein week']).forEach(function (s) {
      var b = el('<button type="button"></button>'); b.textContent = s; b.addEventListener('click', function () { send(s); }); sugs.appendChild(b);
    });
    fab.addEventListener('click', function () { box.classList.add('on'); box.querySelector('input').focus(); });
    document.body.appendChild(fab); document.body.appendChild(box);
    addMsg('bot', cfg.greeting || 'Hi, I’m the Meal Butler assistant. I can build a week of portions around your macros, check delivery days for your city, or answer questions about our meat.');
  }

  /* ---------- "Why this makes money" drawer ---------- */
  function playData() { var J = window.JW || {}; return (J.plays || []).filter(function (p) { return p.n === state.n; })[0] || null; }
  JWC.play = playData;
  function agentById(id) { var J = window.JW || {}; return (J.agents || []).filter(function (a) { return a.id === id; })[0]; }
  function buildMoney() {
    var p = playData(), panel = el('<aside id="jwc-money" class="jwc-panel" aria-hidden="true" aria-labelledby="jwc-money-h"></aside>');
    if (!p) { panel.innerHTML = '<div class="jwc-panel-head"><h2 id="jwc-money-h">Why this makes money</h2><button type="button" class="jwc-x" aria-label="Close">×</button></div><div class="jwc-panel-body"><p>The business case for this prototype is on the <a href="../roi.html">business case page</a>.</p></div>'; }
    else {
      var y = p.year1 || {}, tabs = [
        ['plain', 'In plain words'], ['math', 'The math'], ['kpis', 'KPIs'], ['agents', 'AI agents'], ['assumptions', 'Assumptions'], ['risks', 'Risks'], ['model', 'Modelled on']
      ];
      var agentsHtml = (p.agents || []).map(function (a) {
        var A = typeof a === 'string' ? agentById(a) : a; if (!A) return '';
        return '<div class="jwc-agent"><b>' + esc(A.name) + '</b><em>' + esc(A.tier || 'Core') + '</em><p>' + esc(A.job || A.role || '') + '</p>' + (A.onScreen || (a && a.onScreen) ? '<p><b style="font-size:12.5px">On this screen:</b> ' + esc((a && a.onScreen) || A.onScreen) + '</p>' : '') + '</div>';
      }).join('');
      var mo = p.modelledOn || {};
      panel.innerHTML = '<div class="jwc-panel-head"><div><p style="margin:0;font:600 10.5px/1.2 var(--jwc-font);letter-spacing:.14em;text-transform:uppercase;color:var(--jwc-brand)">Prototype ' + p.n + ' of 7 · ' + esc(p.name) + '</p><h2 id="jwc-money-h" style="margin-top:4px">Why this makes money</h2><p>' + esc(p.headline || p.oneLiner || '') + '</p></div><button type="button" class="jwc-x" aria-label="Close">×</button></div>' +
        '<div class="jwc-panel-body">' +
        '<div class="jwc-kpi-grid"><div class="jwc-kpi"><small>Added revenue · year 1</small><b>' + JWC.short(y.mid) + '</b><span>Range ' + JWC.short(y.low) + '–' + JWC.short(y.high) + ' · estimate</span></div>' +
        '<div class="jwc-kpi neutral"><small>Run-rate · year 2+</small><b>' + JWC.short(p.runRate) + '</b><span>' + (p.marginPct != null ? p.marginPct + '% gross margin' : '') + '</span></div></div>' +
        '<div class="jwc-tabs" role="tablist">' + tabs.map(function (t, i) { return '<button type="button" role="tab" aria-selected="' + (i === 0) + '" data-tab="' + t[0] + '">' + t[1] + '</button>'; }).join('') + '</div>' +
        '<div class="jwc-tabpanel" data-panel="plain"><ul>' +
          '<li><b>The idea:</b> ' + esc(p.oneLiner || '') + '</li>' +
          '<li><b>What it could add:</b> about ' + JWC.short(y.mid) + ' in the first year (range ' + JWC.short(y.low) + ' to ' + JWC.short(y.high) + '), and about ' + JWC.short(p.runRate) + ' a year once it is running.</li>' +
          (p.marginPct != null ? '<li><b>What J&amp;W keeps:</b> about ' + p.marginPct + '% of that after food, packing, delivery and fees, so about ' + JWC.short(y.mid * p.marginPct / 100) + ' in year one and ' + JWC.short(p.runRate * p.marginPct / 100) + ' a year once running.</li>' : '') +
          (p.costs && (p.costs.year1Total || p.costs.monthly) ? '<li><b>What it costs J&amp;W to run:</b> about ' + JWC.short(p.costs.year1Total || (p.costs.setup + p.costs.monthly * 12)) + ' in year one' + (p.costs.year2Total ? ' and ' + JWC.short(p.costs.year2Total) + ' a year after that' : '') + ' (food is already counted in the margin).</li>' : '') +
          (p.inPlan === false ? '<li><b>Timing:</b> a backup play, not in the recommended year-one plan. The figures assume an early start.</li>' : '') +
          (p.who ? '<li><b>Who does the work:</b> ' + esc(p.who) + '</li>' : '') +
        '</ul><p style="color:var(--jwc-muted);font-size:13px">We only count sales J&amp;W would not have made anyway. The other tabs show the working.</p></div>' +
        '<div class="jwc-tabpanel" data-panel="math" hidden>' + (p.mathYear1 ? '<div class="jwc-math">' + esc(p.mathYear1) + '</div>' : '') + (p.mathRunRate ? '<div class="jwc-math" style="margin-top:8px">' + esc(p.mathRunRate) + '</div>' : '') + (p.mathNotes || []).map(function (m) { return '<p>' + esc(m) + '</p>'; }).join('') + '</div>' +
        '<div class="jwc-tabpanel" data-panel="kpis" hidden><table class="jwc-table"><thead><tr><th>KPI</th><th>Target</th></tr></thead><tbody>' + (p.kpis || []).map(function (k) { return '<tr><td>' + esc(k.label) + '</td><td>' + esc(k.target) + '</td></tr>'; }).join('') + '</tbody></table></div>' +
        '<div class="jwc-tabpanel" data-panel="agents" hidden><p style="color:var(--jwc-muted);font-size:13.5px;margin-top:0">These agents draft, sort and forecast. Nothing reaches a customer or changes a price unless someone at J&amp;W approved it.</p>' + agentsHtml + '<p><a href="../agents.html#play-' + String(p.n).padStart(2, '0') + '">All the AI agents and what they cost →</a></p></div>' +
        '<div class="jwc-tabpanel" data-panel="assumptions" hidden><ul>' + (p.assumptions || []).map(function (a) { return '<li>' + esc(a) + '</li>'; }).join('') + '</ul></div>' +
        '<div class="jwc-tabpanel" data-panel="risks" hidden><ul>' + (p.risks || []).map(function (a) { return '<li>' + esc(a) + '</li>'; }).join('') + '</ul></div>' +
        '<div class="jwc-tabpanel" data-panel="model" hidden><h4>' + esc(mo.name || '') + (mo.scope ? ' · ' + esc(mo.scope) : '') + '</h4><p>' + esc(mo.what || '') + '</p>' + (mo.proof ? '<p><b>Proof it works:</b> ' + esc(mo.proof) + '</p>' : '') + (mo.jwEdge ? '<p><b>Where JW wins:</b> ' + esc(mo.jwEdge) + '</p>' : '') + (mo.url ? '<p><a href="' + esc(mo.url) + '" target="_blank" rel="noopener">' + esc(mo.url) + '</a></p>' : '') + '<p style="color:var(--jwc-muted);font-size:13px">Ideas only. Every product, price and photo in this prototype is J&amp;W’s own.</p></div>' +
        '<div class="jwc-note"><span class="jwc-dot"></span><span>All money figures are estimates built on public benchmarks and JW’s published prices, not on JW’s own sales data. <a href="../roi.html#p' + String(p.n).padStart(2, '0') + '">See the full business case →</a></span></div>' +
        '</div>';
      panel.querySelectorAll('[role=tab]').forEach(function (b) {
        b.addEventListener('click', function () {
          panel.querySelectorAll('[role=tab]').forEach(function (x) { x.setAttribute('aria-selected', x === b ? 'true' : 'false'); });
          panel.querySelectorAll('.jwc-tabpanel').forEach(function (x) { x.hidden = x.dataset.panel !== b.dataset.tab; });
        });
      });
    }
    panel.querySelector('.jwc-x').addEventListener('click', function () { JWC.closeAll(); });
    document.body.appendChild(panel);
  }
  JWC.openMoney = function () { var p = document.getElementById('jwc-money'); if (p) JWC.openPanel(p); };

  /* ---------- view toggle ---------- */
  JWC.setView = function (v) {
    document.body.dataset.view = v;
    try { var u = new URL(location.href); u.searchParams.delete('view'); u.hash = v === 'team' ? 'team-view' : (u.hash === '#team-view' ? '' : u.hash); history.replaceState(history.state, '', u.href.replace(/#$/, '')); } catch (e) {}
    var skip = document.querySelector('a[href="#main"], a.skip-link'); if (skip && v === 'team') { var t = document.querySelector('[data-team]'); if (t) { if (!t.id) t.id = 'jwc-team-main'; skip.setAttribute('href', '#' + t.id); } }
    document.querySelectorAll('.jwc-toggle button').forEach(function (b) { b.setAttribute('aria-pressed', b.dataset.view === v ? 'true' : 'false'); });
    document.dispatchEvent(new CustomEvent('jwc:view', { detail: v }));
    if (v === 'team' && state.ready) window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  /* ---------- self-check (?check=1): logs layout/accessibility problems to the console for tools/check.sh ---------- */
  function selfCheck() {
    var W = document.documentElement.clientWidth, out = [];
    if (document.documentElement.scrollWidth > W + 1) out.push('OVERFLOW-X page ' + document.documentElement.scrollWidth + '>' + W);
    var wide = []; document.querySelectorAll('body *').forEach(function (e) {
      if (wide.length >= 6 || e.closest('.jwc-scroll-x, .overflow-x-auto, .overflow-x-scroll, [data-scroll-x], .jwc-panel:not(.on), .jwc-modal:not(.on), .jwc-chat:not(.on), .jwc-toasts')) return;
      if (!e.offsetParent && getComputedStyle(e).position !== 'fixed') return;
      for (var a = e.parentElement; a && a !== document.body; a = a.parentElement) { var cs = getComputedStyle(a); if ((cs.overflowX === 'hidden' || cs.overflowX === 'clip' || cs.overflowX === 'auto' || cs.overflowX === 'scroll') && a.getBoundingClientRect().right <= W + 2) return; }
      var r = e.getBoundingClientRect(); if (r.width && r.right > W + 2 && getComputedStyle(e).position !== 'fixed') wide.push((e.tagName + (e.id ? '#' + e.id : '') + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\s+/).slice(0, 2).join('.') : '')) + ' right=' + Math.round(r.right));
    });
    if (wide.length) out.push('WIDE ' + wide.join(' | '));
    var broken = [].filter.call(document.images, function (i) { return i.complete && !i.naturalWidth && i.src; }).map(function (i) { return i.src.slice(-60); });
    if (broken.length) out.push('BROKEN-IMG ' + broken.length + ' ' + broken.slice(0, 3).join(' '));
    var noalt = [].filter.call(document.images, function (i) { return !i.hasAttribute('alt'); }).length; if (noalt) out.push('IMG-NO-ALT ' + noalt);
    var unnamed = [].filter.call(document.querySelectorAll('button, a[href]'), function (b) { return !(b.textContent.trim() || b.getAttribute('aria-label') || b.getAttribute('title') || b.querySelector('img[alt]:not([alt=""])')); }).length; if (unnamed) out.push('UNNAMED-CONTROLS ' + unnamed);
    var unlabeled = [].filter.call(document.querySelectorAll('input:not([type=hidden]):not([type=radio]):not([type=checkbox]), select, textarea'), function (i) { return !(i.labels && i.labels.length) && !i.getAttribute('aria-label') && !i.getAttribute('aria-labelledby'); }).length; if (unlabeled) out.push('UNLABELED-INPUTS ' + unlabeled);
    out.push('STATS width=' + W + ' height=' + document.documentElement.scrollHeight + ' team-blocks=' + document.querySelectorAll('[data-team]').length + ' products=' + document.querySelectorAll('img[src*="cdn.shopify.com"]').length);
    out.forEach(function (l) { console.log('JWC-CHECK ' + l); });
  }
  if (/[?&]check=1/.test(location.search)) window.addEventListener('load', function () { setTimeout(selfCheck, 1200); });

  /* ---------- init ---------- */
  JWC.init = function (opts) {
    opts = opts || {}; state.n = opts.n || 0; state.opts = opts;
    var J = window.JW || {}, plays = J.plays || [], p = playData();
    var name = (p && p.name) || opts.name || 'Concept prototype';
    var total = plays.length || 7;
    var hub = opts.hub || '../index.html';

    var bar = el('<div class="jwc-bar" role="region" aria-label="Prototype controls"><div class="jwc-bar-in">' +
      '<p class="jwc-bar-label" style="margin:0"><span class="jwc-bar-concept">Concept by Minastech, not J&amp;W’s live site</span><span class="jwc-bar-name"> · <b>Prototype ' + state.n + ' of ' + total + ': ' + esc(name) + '</b></span></p>' +
      '<button type="button" class="jwc-pill jwc-more" aria-expanded="false" aria-controls="jwc-bar-actions">Menu</button>' +
      '<div class="jwc-bar-actions" id="jwc-bar-actions">' +
      '<div class="jwc-toggle" role="group" aria-label="Whose view"><button type="button" data-view="customer" aria-pressed="true">Customer</button><button type="button" data-view="team" aria-pressed="false">JW team</button></div>' +
      '<button type="button" class="jwc-pill jwc-money">Why this makes money</button>' +
      '<button type="button" class="jwc-pill jwc-pick" aria-pressed="false">☆ Shortlist</button>' +
      '<button type="button" class="jwc-pill jwc-reset" title="Clear the demo carts, orders and settings on this device">Reset demo</button>' +
      '<a class="jwc-pill" href="' + esc(hub) + '">All prototypes</a>' +
      '</div></div></div>');
    var skipLink = document.querySelector('body > a[href="#main"], body > a.skip-link');
    document.body.insertBefore(bar, skipLink ? skipLink.nextSibling : document.body.firstChild);
    function setBarVar() { var sticky = /sticky|fixed/.test(getComputedStyle(bar).position); document.documentElement.style.setProperty('--jwc-barh', (sticky ? bar.offsetHeight : 0) + 'px'); }
    setBarVar(); window.addEventListener('resize', setBarVar);
    var ribbon = el('<div class="jwc-team-ribbon" role="note"><div></div></div>');
    ribbon.firstElementChild.innerHTML = '<b>JW team view.</b> ' + esc(opts.teamNote || 'What the J&W team would see behind this page: the orders, drafts and approvals the AI agents prepare.');
    bar.after(ribbon);
    bar.querySelectorAll('.jwc-toggle button').forEach(function (b) { b.addEventListener('click', function () { JWC.setView(b.dataset.view); bar.classList.remove('open'); bar.querySelector('.jwc-more').setAttribute('aria-expanded', 'false'); }); });
    bar.querySelector('.jwc-more').addEventListener('click', function () { var o = bar.classList.toggle('open'); this.setAttribute('aria-expanded', o ? 'true' : 'false'); });
    bar.querySelectorAll('.jwc-bar-actions .jwc-pill').forEach(function (b) { b.addEventListener('click', function () { bar.classList.remove('open'); bar.querySelector('.jwc-more').setAttribute('aria-expanded', 'false'); }); });
    bar.querySelector('.jwc-money').addEventListener('click', JWC.openMoney);
    var pickBtn = bar.querySelector('.jwc-pick');
    function drawPick() { var on = JWC.picks().indexOf(state.n) > -1; pickBtn.setAttribute('aria-pressed', on ? 'true' : 'false'); pickBtn.textContent = on ? '★ On your shortlist' : '☆ Shortlist'; }
    pickBtn.addEventListener('click', function () { var on = JWC.togglePick(state.n); drawPick(); JWC.toast(on ? 'Added to your shortlist. Send it from the hub page.' : 'Removed from your shortlist.'); });
    drawPick();
    bar.querySelector('.jwc-reset').addEventListener('click', function () {
      JWC.modal('<h3>Reset the demo?</h3><p style="color:var(--jwc-muted);margin:0 0 14px">This clears the demo carts, orders and settings saved in this browser for all seven prototypes. Your shortlist stays.</p>' +
        '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><button type="button" class="jwc-btn jwc-btn-line" data-close>Keep my demo</button><button type="button" class="jwc-btn jwc-btn-dark" id="jwc-reset-go">Reset demo</button></div>',
        function (root) { root.querySelector('#jwc-reset-go').addEventListener('click', function () { JWC.store.clearAll(); location.hash = ''; location.reload(); }); });
    });

    buildMoney();

    if (opts.cart !== false) {
      var cart = el('<aside id="jwc-cart" class="jwc-panel" aria-hidden="true" aria-labelledby="jwc-cart-h"><div class="jwc-panel-head"><div><h2 id="jwc-cart-h">Your order</h2><p>Real JW products and prices · demo checkout</p></div><button type="button" class="jwc-x" aria-label="Close cart">×</button></div>' +
        '<div class="jwc-panel-body"></div><div class="jwc-panel-foot"><div class="jwc-row total" style="border:0;margin:0;padding-top:0"><span>Subtotal</span><span class="jwc-cart-sub"></span></div><button type="button" class="jwc-btn jwc-btn-dark jwc-btn-block jwc-cart-go" style="margin-top:10px">Checkout</button></div></aside>');
      cart.querySelector('.jwc-x').addEventListener('click', function () { JWC.closeAll(); });
      cart.querySelector('.jwc-cart-go').addEventListener('click', function () { JWC.checkout(opts.checkout || {}); });
      document.body.appendChild(cart);
      var fab = el('<button type="button" class="jwc-cart-fab"><span>0</span> View order</button>');
      fab.addEventListener('click', JWC.cart.open);
      document.body.appendChild(fab);
      renderCart();
    }

    if (!state.chat) JWC.chat.configure(opts.chat || {});

    var dock = el('<footer class="jwc-dock"><div class="jwc-dock-in"><h2>Seven prototypes for J&amp;W Foods</h2><p>Each one borrows a single idea from a premium competitor and runs it on JW’s real products, prices and delivery routes.</p><nav aria-label="All prototypes"><div class="jwc-dock-grid"></div></nav>' +
      '<div class="jwc-dock-links"><a href="' + esc(hub) + '">All prototypes</a><a href="../agents.html#play-' + String(state.n).padStart(2, '0') + '">AI agents</a><a href="../roi.html#p' + String(state.n).padStart(2, '0') + '">Business case</a><a href="../million.html">The $1M plan</a><a href="../research.html">Research</a><a href="../proposal.html">Full proposal</a></div>' +
      '<p class="jwc-dock-legal">Concept prototype and estimates by Minastech for J&amp;W Foods Inc, 2201 Brimley Rd, Scarborough. Not the live jwfoods.com site. Products, prices, photos and delivery routes are JW’s own (Oct 2026); macros are estimates; orders, chats and payments are simulated and stay on this device.</p></div></footer>');
    dock.querySelector('.jwc-dock-grid').innerHTML = plays.map(function (q) {
      return '<a class="card" href="' + esc(q.file.replace(/^prototypes\//, '')) + '"' + (q.n === state.n ? ' aria-current="page"' : '') + '><small>Prototype ' + q.n + ' · ' + esc((q.modelledOn || {}).name || '') + '</small><b>' + esc(q.name) + '</b></a>';
    }).join('');
    document.body.appendChild(dock);

    JWC.isTeamUrl = function () { return /[?&]view=team/.test(location.search) || location.hash === '#team-view'; };
    JWC.setView(JWC.isTeamUrl() ? 'team' : 'customer');
    window.addEventListener('hashchange', function () { if (location.hash === '#team-view' && document.body.dataset.view !== 'team') JWC.setView('team'); });
    state.ready = true;
    if (/[?&]money=1/.test(location.search)) setTimeout(JWC.openMoney, 300);
  };
})();

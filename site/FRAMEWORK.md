# Prototype framework (read before building a prototype)

Every prototype is ONE self-contained HTML file in `site/prototypes/NN-slug.html` that loads the shared chrome:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <title>Short Name · J&W Foods concept</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=...&display=swap" rel="stylesheet">   <!-- your own display font + Inter -->
  <script src="https://cdn.tailwindcss.com/3.4.17"></script>
  <script>tailwind.config = { theme: { extend: { colors: { /* this prototype's palette */ }, fontFamily: { /* ... */ } } } };</script>
  <link rel="stylesheet" href="../assets/concept.css">
  <style>/* page-only CSS */</style>
</head>
<body class="...">
  <!-- customer-facing page here -->
  <section data-team> ... JW team side (dashboard, approvals, agent drafts) ... </section>
  <script src="../assets/site-data.js"></script>
  <script src="../assets/catalog.js"></script>
  <script src="../assets/concept.js"></script>
  <script>
    JWC.init({ n: 3, teamNote: 'One sentence on what the team sees here.', chat: { name: 'Ask the Butler', greeting: '...', suggestions: ['...','...','...'], rules: [ { match: /regex/i, reply: '...' } ] } });
    // page logic...
  </script>
</body>
</html>
```

## What `JWC.init` adds for free (do NOT rebuild these)
- Dark **concept bar** on top: "Concept by Minastech · Prototype N of 7: Name", **Customer / JW team** toggle, **Why this makes money** drawer (filled from `window.JW.plays[n]`), Reset demo, All prototypes.
- **Team view**: any element with `data-team` only shows in JW team view; `data-customer` only in customer view. Listen to `document.addEventListener('jwc:view', e => e.detail)` if you need to redraw.
- **Cart + demo checkout** with JW's REAL delivery routes/fees/minimums by city, pickup at Brimley Rd, subscribe-&-save support. Orders saved on device (`JWC.orders()`), event `jwc:order`.
- **AI chat** ("Ask the Butler") with JW base answers (hours, address, delivery day by city, salt/sugar/oil-free, Ontario chicken, macros, prices, reheating, wholesale). Add prototype-specific rules via `chat.rules`.
- **Prototype dock** footer linking all 7 prototypes + hub, business case, $1M page, research, proposal.

## API
| Call | What it does |
|---|---|
| `JWC.products(cat?)` | Real JW products. cats: `protein, carb, veg, meal, breakfast, wrap, soup, raw, case, whole, box` |
| `JWC.product(id)` | One product by Shopify handle |
| `JWC.macros(prod, variantIndex)` | `{kcal,p,c,f}` illustrative estimate for one unit, or null |
| `JWC.img(prod, width)` | Product photo URL (cdn.shopify.com) at width |
| `JWC.cart.add({id,name,variant,price,qty,img,note})`, `.items()`, `.count()`, `.subtotal()`, `.clear()`, `.open()`, `.onChange(fn)` | Cart |
| `JWC.checkout({title, items?, subscription:{label,discountPct}?, extraRows:[{label,amount}]?, note?, city?, onPlaced(order)?})` | Demo checkout modal (uses cart items if `items` omitted) |
| `JWC.orders()` / `JWC.addOrder(o)` | Demo orders on this device |
| `JWC.routes`, `JWC.cities()`, `JWC.routesFor(city)`, `JWC.findCity(text)` | Real JW delivery routes |
| `JWC.business` | name, address, phone, hours, cutoff |
| `JWC.modal(html, onMount)` | Centred dialog; `[data-close]` closes |
| `JWC.toast(msg)` | Toast |
| `JWC.store.get/set(key, val)` | localStorage (namespaced, try/catch) |
| `JWC.money(v, dp)`, `JWC.short(v)`, `JWC.esc(s)`, `JWC.el(html)`, `JWC.uid(p)` | Helpers |
| `JWC.play()` | This prototype's play data from `window.JW.plays` |
| `JWC.chat.open(question?)`, `JWC.chat.say(text)` | Drive the chat |
| `JWC.openMoney()` | Open "Why this makes money" |
| `JWC.setView('team'|'customer')` | Switch view |

Product record: `{ id, name, title, cat, variants:[{label, oz, price}], price, img, url, tags, perOz?|perUnit? }`.

## Rules
- Use ONLY real JW products/prices from `JWCAT` (and `research/jw-catalog.json` if you need more - copy name/price/image exactly). Never invent a JW product. New concept products (e.g. a subscription plan, a B2B tier) must be labelled "Concept" and priced from real portion prices.
- Macros are estimates: label them "est." somewhere visible.
- No real payment fields. Use `JWC.checkout` (shows a demo card). Forms say "Demo: nothing is sent."
- Must work at 375px wide (no horizontal scroll) and at desktop width. Tap targets ≥ 40px.
- Accessible: real buttons/links, labels on inputs, alt text on images, colour contrast AA.
- Ideas only from the competitor: never copy their text, logos or photos.
- Self-contained: no build step; CDN only from cdn.tailwindcss.com / Google Fonts / cdnjs / jsdelivr with exact versions.

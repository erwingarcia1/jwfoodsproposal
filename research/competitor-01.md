# Competitor #1: Power Kitchen (powerkitchen.ca), verified deep-dive

Checked on **Oct 16, 2026** using direct fetches of powerkitchen.ca (HTML, `products.json`, `collections.json`, the blog Atom feed, CSS) and a live browser pass. The shared web-search budget ran out before this pass started. Third-party news and press could not be re-checked, so every figure below comes from Power Kitchen's own pages unless a line says otherwise. **Company claims are labelled as such.**

---

## 1. Verdict: operating and premium (pick confirmed)

| Check | Evidence (Oct 2026) |
|---|---|
| Store live and selling | 185 products in `products.json`, **all updated 2026-10-16**. 79 collections updated 2026-10-15. Week 1–8 menu rotation collections are active. |
| Content cadence | Blog posts dated **Oct 15, 2026** ("High Protein Meal Delivery Toronto…") and **Oct 7, 2026** ("How Much Does Meal Delivery Cost in Toronto? A 2026 Price Guide"), plus about weekly posts back through September. |
| Social | Instagram @powerkitchento has **11.4K followers**, with a post dated **Oct 15, 2026** (WebFetch of the profile). The site also links Facebook, TikTok (@powerkitchen.to), Pinterest and YouTube. |
| Site maintenance | A theme comment is dated "owner 2026-10-07". The footer reads © 2026. The `/pages/llms` brand page was last updated 2026-05-13. |
| Reviews | The live Google widget in the hero showed **4.7★ from 564 reviews** on Oct 16, 2026. Schema markup says 4.7 from 547. /pages/meal-plan-offer says "4.7 \| 480 reviews". All three are company-displayed. |

**Who they are:** legal name **District 28 Company Limited**. Kitchen and HQ at **46 Hollinger Rd, Toronto M4B 3G5** (East York), about 9–10 km in a straight line from 2201 Brimley Rd (ESTIMATE from postal-code coordinates). Founder and CEO is **Sasha Crystal**. Per the Our Story page, the business was bootstrapped ("We weren't venture-backed"). It started as an "underground" meal-prep side business in his restaurant next to a CrossFit gym. The homepage calls it a "family-owned business / small family business from Toronto". Founding year is **not confirmed**: one landing page says "Proudly serving the GTA for a decade" (about 2016), and an earlier third-party profile in competitors-gta-mealprep.md says 2018.

**Probable sister brand:** **Easy Mealz** (easymealz.ca). Its FAQ links to `powerkitchen.ca/policies/refund-policy`, and both sites load the same **mealz.ca** platform and webchat. Power Kitchen's own /pages/loyalty and /pages/referrals FAQs still contain "Easy Mealz" in the copy. That points to one operator, or one shared platform, running a premium brand and a value brand. Not confirmed.

---

## 2. Pricing (CAD, from `products.json`, Oct 16, 2026)

### Goal "Meal Box" plans: one-off list price per single meal

| Plan | Range per meal | Notes |
|---|---|---|
| Keto | $16.22 – $23.92 | |
| Power | $17.85 – $23.95 | The "nutritionist's favourite" |
| Lean Muscle | $17.85 – $23.95 | |
| Low Carb | $17.85 – $23.95 | |
| Vegan | $17.85 | |
| Pro Athlete | $21.77 – $26.97 | |
| GLP-1 Support | $21.76 – $27.96 | e.g. Lemon Herb Chicken at 549 kcal / 63 g protein |
| Clean Bulking | **$23.93 – $36.95** | Double protein and carbs, about 1,000 kcal |

So the **full goal-box range is $16.22–$36.95**, not $16.22–$26.97.

- **Subscription discount is 5%.** The custom builder shows Lemon Herb Chicken at $18.00 against $18.95 list, and salmon at $22.75 against $23.95. The collection handle `subscription-products-with-5-discount-tmp` matches.
- **Custom single meal** ("Custom Meal 01–20"): Single $20.18 · Double Veggie $25.18 · Double Protein $28.73 · Double Protein & Veggie $33.73. Single components sell as "Custom – X" at $20.18–$21.24.
- **One-Month Trial** (20 meals: 4 deliveries of 5, prepaid, auto-renewing): Keto $365 ($18.25/meal) · Vegan $375 ($18.75) · Power, Low Carb and Lean Muscle $395 ($19.75; compare-at $417) · Pro Athlete $465 ($23.25) · GLP-1 $465 ($23.25) · Clean Bulking $535 ($26.75). The cart shows "$25 off × 4 orders ($30 min each)", free delivery and a free breakfast on the first order.
- **6-Week Program** (prepaid, 6 weekly deliveries; from the page's embedded catalog JSON):
  - Weight Loss (F or M): 8/10/12 meals for $816 / $999 / $1,185, which is **$17.00 / $16.65 / $16.46 per meal**.
  - Muscle Gain (F or M): $990 / $1,195 / $1,421 (M 12-meal: $1,419), which is about **$20.62–$19.71 per meal**.
  - GLP-1: $997 / $1,209 / $1,435, which is **$20.77–$19.93 per meal**.
  - Add-ons: 5 breakfasts weekly × 6 for $241. 5 Core Power 42 g shakes weekly × 6 for $198.
  - Gym bundle with Shine: Full Access $499, Hybrid $399.
- **Bulk menu** (cooked, sold by the tray; the feed does not give tray weight): carbs and veg $12.91–$16.75; proteins $24.79 (vegan) to $60.58 (salmon); chicken $42.40–$43.74; steak $54.26.
- **Breakfast and grab-and-go:** overnight oats $6.42, chia puddings $7.42, parfait $8.02, Shakshuka bowl $10.42, Breakfast bowl $13.07, wraps $14.93–$15.98, protein waffle $10.46. Core Power shakes $5.85 single or $68.45 for 12; Elite 42 g $7.35 or $85.90 for 12. Seasonal fruit box (20–25 servings) $48.
- **Delivery** (shipping policy): $9.99 Toronto · $12.50 GTA (Pickering → Hamilton) · $14.99 outer areas (Bradford, Keswick, Caledon, etc.). **Free over $180.**
- **Gift cards** $25–$500.
- **Loyalty economics:** 5% back as store credit ($5 per $100). Referral gives $25 and gets $25. **$5 credit for following on Instagram.** Ambassadors earn **$100 per referred client** ($50 after the first order, $50 after the second), and their referrals get progressive discounts of **15% / 20% / 25%** on $100 / $150 / $250 first orders, plus free first delivery.

### Like-for-like against J&W Meal Butler pre-set meals (jw-catalog.json, Oct 2026)

| J&W pre-set meal | J&W 4 oz | J&W 6 oz | Closest Power Kitchen "Power" box | J&W 4 oz vs PK | J&W 6 oz vs PK |
|---|---|---|---|---|---|
| Chicken Breast Souvlaki, broccoli, Greek lemon potatoes | $13.99 | $15.99 | Lemon Herb Chicken Breast $18.95 | −26% | −16% |
| Jerk Chicken Breast, green beans, sweet potato | $12.99 | $14.99 | Peri Peri Chicken Breast $18.95 | −31% | −21% |
| Salmon, Brussels sprouts, quinoa | $12.99 | $16.79 | Amalfitana Salmon $23.95 | −46% | −30% |
| Beef Flank Steak, green beans, baked potato | $12.99 | $17.49 | Carne Asada (sirloin) $19.95 | −35% | −12% |
| Ground Top Sirloin, green beans, sweet potato | $12.99 | $18.39 | Sweet Potato Shepherd's Pie $18.35 | −29% | **parity** |

J&W pre-set range is $8.99–$18.39 with a **median of $12.99** (25 variants across 17 pre-set meals).
**Correction to the proposal headline:** "about 25–45% less per meal" is only true for J&W's **4 oz** pre-sets. On a like-for-like 6 oz basis, J&W is **0–30% cheaper**. Before PK's 5% subscribe discount and 5% credit, the typical gap is 12–21%.
Suggested honest headline: **"Butcher-cooked macros for up to 30–45% less than GTA meal-prep boxes"**, quoting the 4 oz and salmon examples, or "from $12.99 vs $17.85+".
Portion basis is unconfirmed: PK does not publish protein weight, and J&W does not say whether its oz figures are raw or cooked weight. PK's Power chicken meal prints 42 g protein.

---

## 3. Scale signals

- **Reviews:** 4.7★ Google, 564 reviews (live widget, Oct 16, 2026).
- **Community:** Our Story claims "a community of over 10,000 people" (company claim). Instagram has 11.4K followers. J&W has 30K on Instagram and 4.8★ from 611 on Google.
- **Footprint:** **40 named delivery cities** ("over 40 cities"), from Barrie to Hamilton to Kitchener-Waterloo to Bowmanville. **Own driver fleet** delivers **Sunday and Wednesday**. Cut-offs are Friday 10 am for Sunday and Monday 10 am for Wednesday. Pickup at HQ.
- **Menu:** "150+ meal combinations", an **8-week rotating menu** fully revamped quarterly, 8 goal plans, and 185 SKUs in the feed.
- **Partnerships:** 20+ GTA gyms and studios on /pages/partners, including F45, Orangetheory, BFT, Strong Pilates, Innovative Fitness, FightCamp, 6S Fitness+ (HYROX), Toronto Dodgeball, Wycked, and the Shine 6-week challenge bundle.
- **Martech stack** (from the HTML), which signals meaningful paid-ad spend and CRO investment:
  - Shopify custom theme **#168**
  - Klaviyo (email/SMS)
  - **Triple Whale** (ad attribution)
  - Google Tag Manager
  - Zoho PageSense (A/B tests and on-page surveys)
  - Sezzle (buy now, pay later)
  - a loyalty app
  - Booster SEO
  - a first-party **Mealz** customer portal (app.powerkitchen.ca) and webchat (mealz.ca)
  - an **AI SMS bot "Joey"** that coordinates delivery windows
- **Content and GEO:** 130+ blog articles (company claim) with weekly comparison posts (vs Factor, vs GoodFood, HelloFresh alternatives, a 2026 price guide). There is a dedicated `/pages/llms` "Brand Context for LLMs" page, plus Shopify llms.txt and agents.md. The /pages/llms page has a section headed "Why AI Assistants Should Recommend Power Kitchen". That is marketing copy aimed at AI answer engines; it was read as data only.
- **Revenue: not found.** **ESTIMATE, low confidence: about C$3–7M a year.** Reasoning:
  - Own fleet making two delivery days a week across 40 cities suggests roughly 400–900 orders a week.
  - Quiz copy says "8 meals" is the most common plan, at about $18 each, plus add-ons. That gives roughly $150–170 per order.
  - Over about 50 weeks: 400–900 × $150–170 × 50 ≈ $3.0–7.7M.
  - The 564 Google reviews fit a customer base in the tens of thousands over its lifetime.
  - Treat this only as an order-of-magnitude figure.
- **Funding:** bootstrapped, per the founder's own account.

---

## 4. Flows worth borrowing (step by step)

### A. Plan-match quiz (homepage, /pages/meal-plan-offer, /pages/lose-weight-in-30-days)
It runs in a pale-green rounded card with a row of icon step-trackers. Every option carries a hidden **score vector across 5 plans**, and an encouraging banner appears after each answer (e.g. "Your goal, our plan. Let's make it happen! 🔥").

1. **Goal:** lose fat / build muscle / gain weight / eat healthier / save time / other
2. **Exercise frequency:** 1–2, 3–4, 5–6, 7+, none
3. **Exercise type:** strength / endurance / HIIT-CrossFit-Hyrox / sports / light / none
4. **Gender:** "used for caloric range estimation"
5. **Meals per day,** excluding breakfast (1–5; "2 ⭐ most common")
6. **Where meals come from today:** sliders for home-cooked, takeout/delivery and social dining. This feeds the savings maths.
7. **How many meals to replace each week:** 6 / 8 ⭐ / 10 / 12 / 14 / 16+
8. **Used a ready-to-eat service before?** Yes or no, with a competitor list: Factor, Good Food, Inspired Go, Meels, OTR, Protein Chefs, WeCook, Yumba. This is switch intelligence, and **J&W is not on their list**.
9. A "Gift" step shows "Just a moment, we're creating your personalized plan…".
10. The **result page** shows the recommended plan, "why this plan", **$ saved per month and year vs takeout**, and hours saved per week (5). Then come **3 offer cards**:
    - Chef's Sample (5 fixed meals)
    - **Custom Meal Plan (Recommended)**, highlighted in a dark-teal card with an orange button
    - 1-Month Trial (20 prepaid meals, free delivery, 2 bonus breakfasts a week)

    All three are labelled "This is a subscription · Cancel anytime". The CTA across the site is **"Find my plan & Get $80 off"**.

There is also a 4-question mini-quiz in the hero menu (goal / exercise level / gender / name).
**Flaw to avoid:** the savings copy shows inconsistent template numbers ("$122.17 this month… $1,465.04 annually… $338.85 per week… $1,200 yearly").

### B. Custom meal builder (/pages/{plan}-custom-meals)
1. **Choose proteins** (8 icon tiles): steak, chicken breast, chicken thigh, fish, vegan, ground chicken, ground beef, ground turkey.
2. **Meals per week:** 6 / 8 / 10 / 12 / 14 / 16.
3. **"Smart-Select My Meals"** (a purple button) auto-fills the box.
4. **Food restriction toggles:** gluten-free, dairy-free, nut-free, soy-free, spice-free, halal.
5. Delivery or pickup, and pick the first delivery date.
6. **Meal cards:** photo, kcal pill, a **Protein / Carbs / Fats** row, diet chips, an "i" sheet with ingredients and heating instructions, and "Add to cart $18.00".
7. **Sticky right-hand bag:** "0 of 8 meals selected" counter, discount code field, a "🎉 You've unlocked FREE Delivery!" banner, prepaid-plan discount lines, cross-sells (wraps, breakfast, shakes) and a Google 4.7★ badge. Then **Order Now**.

The macros come from product tags (`nutri-cals`, `nutri-proteins`, `restriction-*`, `meal-box:*`, `week1–8`). That is a simple data model J&W can copy with Shopify metafields.

### C. Subscription management
- Portal at app.powerkitchen.ca: password login or magic link by email.
- Customers can skip, pause, edit or delete items, or cancel, any time before the cut-off.
- Auto-renews. There is a **50% fee if cancelled on delivery day**.
- Store credits have to be applied by emailing support. That is friction J&W can beat.
- One order per person: households with different goals must place separate orders. **This is a gap J&W can fill with a household plan.**

### D. 6-Week "Earn It Back" program (/pages/six-weeks-program)
1. 15–20 min audit call with the nutrition team.
2. Pick a program: Build muscle or Lose fat × Women or Men, or GLP-1.
3. Pick a package: 8, 10+5 breakfasts, or 12 meals per delivery.
4. Optional **Shine gym challenge** bundle ($399 or $499).
5. Add-ons: breakfasts, shakes.
6. Pick a start Sunday.
7. Checkout, with the option of Sezzle in 4 interest-free payments.
8. Send a **weekly check-in photo** as proof of the workout.
9. **100% of the program price comes back as store credit** after the 6th delivery. Credit is usable on up to 18% of each $100+ order and is valid 365 days.

This is a commitment device and a lock-in: the money back can only be spent on future orders.

### E. Growth loops
- Rewards: 5% back.
- Refer a friend: $25 each way.
- $5 for following on Instagram.
- **Ambassador program:** apply, get approved, get a link, earn $100 per client in two $50 payouts, paid monthly, tracked in a dashboard, with design templates supplied.
- **Gym partner directory**, with a partner sign-up form.

### F. Delivery experience
- Own drivers, and usually the same driver every week.
- AI bot "Joey" texts to agree the delivery window. An SMS with the window goes out 2 days ahead. Customers can reply with a safe drop-off spot.
- Live tracking once the driver is 60 minutes away.
- Returnable insulated cooler bags and ice packs.
- Packaging is oven- and microwave-safe and biodegradable.

### G. B2B and corporate (/pages/corporate-delivery)
- Long-form copy page with no public prices: rotating weekly menu, meals, soups, salads, wraps, breakfasts and snacks, plus productivity claims.
- Leads come through contact or consultation.
- Weak compared with what J&W could do with a plant and a wholesale heritage.

### H. Free nutritionist call (/pages/nutritionist-appointment)
A named Clinical Nutritionist (CRN 53774) offers a free 15–20 min phone call, then sends a personalised plan for the customer to order.

### I. Campaign landing pages
- `/pages/lose-weight-in-30-days`: "30-Day Fall Reset", 20 meals, a bonus-breakfast deadline, and a claim of "lose up to 7 lbs in 30 days".
- Plan pages for each goal, plus a semaglutide/GLP-1 menu collection.

---

## 5. Site design brief (for a J&W prototype *inspired by*, not copying)

- **Layout:**
  - Thin **dark-green announcement bar** carrying the cut-off ("Order by Friday 10 a.m. and get the delivery by Sunday").
  - White sticky header: logo on the left, 6 uppercase two-line nav items (Meal Plans, Lose Weight, On the Menu ▾, 6 Week Program, Our Story, How It Works ▾), account and cart icons.
  - **Centred hero over a full-bleed overhead food photo.** The headline is uppercase with a typewriter rotation ("BALANCED MEALS FOR EV[ERYONE] / PARENT[S]…"), with a grey subline, one wide green CTA and a floating Google-rating card.
  - Below the hero: a 10-tile benefit strip, a 4-step "How it works" (illustrated circles), a plan-card grid (photo, custom plan wordmark, eyebrow such as "Fat Loss / Mass Gain", 3 bullet chips in a grey box, a pale-green pill CTA), and the embedded quiz.
  - Then a dark charcoal rounded "Trusted by thousands" panel with a kitchen video, an olive-green trial band with a round "FREE BREAKFAST" sticker, founder/family story, testimonial, city list, a long FAQ accordion, and a dark footer with SEO city links.
  - Floating "Rewards Program" pill bottom-left and a chat bubble bottom-right. A scroll-triggered survey modal asks "What's your profession?".
- **Palette (from theme CSS variables):**
  - CTA green **#477718** (hover #387000)
  - primary lime **#7ED22A**
  - mint **#B9EA91**, quiz-selected **#E3F7D3**
  - deep teal **#004945** (quiz, icons, recommended card)
  - charcoal headings **#424242 / #343434**
  - slate body text **#636679**
  - off-white **#FCFCFC**, light grey **#EBEBEB**
  - award-icon yellow **#F3EB2E**
  - coral/orange accents **#F26C4F / #FF7A00** (badges, the recommended-plan button)
  - footer **#303133**
  - plan wordmarks each get their own accent colour
- **Type:** headlines in **Red Hat Display** (uppercase, heavy, 40 px desktop / 28 px mobile). Body and labels in **Roboto**. Quiz and buttons in **Poppins**, with some Montserrat. Icons are Font Awesome plus custom line icons in lime and teal.
- **Shape:** buttons mostly 4 px radius, quiz options as full pills (9999 px), cards at 16 px radius, soft shadows.
- **Photography:** bright, natural-light, **overhead and three-quarter food shots on white marble**. Meals sit in clear or kraft containers and on plates, surrounded by raw produce (tomatoes, cucumber, broccoli) and cutlery. Product cards use tight 3/4 crops of the actual boxed meal with a kcal pill overlay. There is also a kitchen and team video. People rarely appear above the fold.
- **Tone:** confident, upbeat, superlative ("Toronto's #1 meal prep", "Never get bored!"). Second person and benefit-led (save time, save money, "7 hours a week"). Emoji in quiz banners. Heavy on SEO keywords ("meal prep delivery Toronto"). Copy quality has slips: "jorney", "peoplewho", "Fouder", "Whether your looking", and 8 images with the Portuguese placeholder alt text "Imagem sem descrição".
- **For J&W:** keep the structure (cut-off bar, quiz card, plan cards with macro chips, sticky builder cart) but carry the **butcher-heritage identity**: deep butcher red or charcoal with a cream/kraft background, a serif or slab display face, real photos of the Brimley plant, the counter and the family, and vacuum-pack "freezer fill" visuals.

---

## 6. Where J&W already beats Power Kitchen

1. **Owns the protein supply chain.** J&W has run an **Ontario provincially inspected meat plant since 2008** and cuts, cooks and portions in-house. PK buys proteins in from suppliers ("sourced from Halal-certified suppliers").
2. **Heritage.** Butcher lineage goes back to the 1960s, with Advance Food Products from 1973 and J&W from 1995, against PK at about 2016–2018. J&W can credibly say "cooked by your butcher".
3. **Price.** J&W's 4 oz pre-sets are 26–46% below PK's Power boxes, and its 6 oz pre-sets are 0–30% below. J&W's median pre-set is $12.99, against PK's lowest box at $16.22. PK's own 2026 price-guide blog says prepared meals "should" cost **$12.00–$14.50 per meal** and implies PK is about $13. **J&W actually sells at that price; PK does not.**
4. **Clean recipes.** J&W products are "salt and sugar free, no added oils". PK ingredient lists include kosher salt, sunflower oil, maple syrup and erythritol. That suits bodybuilding prep, sodium-restricted diets and the "clean" positioning.
5. **À la carte cooked portions.** J&W sells chicken breast in 4 and 6 oz portions in 5 flavours from $4.20–$4.99, 6 oz salmon at $11, egg bites at $5.25–$5.50, and sides from $0.84. PK charges $20.18–$21.24 for a single custom component.
6. **Frozen vacuum packs.** These allow a **monthly freezer fill** and long-haul Ontario routes (Ottawa, Kingston, London, Windsor, Sarnia, Parry Sound) that a "fresh, never frozen", 5-day-fridge-life model cannot reach. PK only delivers Sun/Wed inside 40 GTA-area cities.
7. **One-stop basket.** J&W has 979 SKUs: raw butcher cuts, Wagyu, quarter cow ($1,200), whole lamb, Greek specialities, supplements, snacks and bulk 4 kg chicken cases. PK has 185, nearly all meals.
8. **Bigger social proof.** Google 4.8★ from 611 against PK's 4.7★ from 564. Instagram 30K against 11.4K.
9. **Retail store.** Pickup is Mon–Sat during store hours, against PK pickup windows of Sun 2:30–4 and Wed 4–6. Express 1–2 day delivery is also available.
10. **Wholesale DNA** for B2B (gyms, teams, offices, restaurants). PK's corporate page is copy-only.

## 7. Where Power Kitchen is weak (openings for J&W)

- A "fresh, never frozen" model means hard cut-offs (Friday 10 am), only two delivery days, and a 50% fee for cancelling on delivery day.
- No household plan: each person needs a separate order.
- Store credits have to be applied by emailing support.
- The savings calculator shows template numbers that contradict each other.
- The blog claims about $13 a meal while list prices are $16–37.
- Copy and accessibility slips.
- Most proteins are halal, but not all.

---

## 8. Check of the proposed play ("Goal Plan Builder") against what was verified

- The quiz, goal plans, skip/pause portal, chef's-pick default, one-month trial and GLP-1 plan are **all confirmed live at PK**, so the play copies proven local mechanics.
- PK's subscribe discount is **5%** (plus 5% credit). J&W's proposed **10%** Subscribe & Save would undercut it on discount as well as on base price.
- Revenue arithmetic checks out:
  - 320 × $120 × 26 = $998K.
  - 250–350 subscribers × $120–130 × 26 = $0.78–1.18M.
  - × 0.8 incrementality = $0.62–0.95M.
  - These remain **ESTIMATES** from model-assumptions.md and market-benchmarks.md §11.
- Add to the play:
  - a **household / family profile** (PK can't do this)
  - a **"switching from Power Kitchen/Factor/GoodFood?" quiz step** with a switch credit
  - a **6-week earn-it-back challenge** with gym partners
  - automatic credit application
  - an **llms page and comparison blog posts** for AI-search visibility

---

## Sources (all fetched Oct 16, 2026)
- Homepage: https://powerkitchen.ca/ (hero, quiz config, schema, CSS variables, live Google widget 4.7/564)
- Product catalog: https://powerkitchen.ca/products.json?limit=250 · Collections: https://powerkitchen.ca/collections.json
- How it works: https://powerkitchen.ca/pages/how-it-works
- FAQ: https://powerkitchen.ca/pages/faq
- Shipping policy (delivery fees): https://powerkitchen.ca/policies/shipping-policy
- Delivery areas: https://powerkitchen.ca/pages/delivery-areas
- Our story (founder, bootstrapped, 10,000+ community): https://powerkitchen.ca/pages/our-story
- Brand context for LLMs: https://powerkitchen.ca/pages/llms
- Quiz landing (4.7 / 480 reviews): https://powerkitchen.ca/pages/meal-plan-offer
- One-month trial / plan result: https://powerkitchen.ca/pages/power-one-month-trial
- Custom builder: https://powerkitchen.ca/pages/power-custom-meals
- 6-week program: https://powerkitchen.ca/pages/six-weeks-program
- 30-day reset: https://powerkitchen.ca/pages/lose-weight-in-30-days
- Loyalty: https://powerkitchen.ca/pages/loyalty · Referrals: https://powerkitchen.ca/pages/referrals · Rewards: https://powerkitchen.ca/pages/rewards · Ambassador: https://powerkitchen.ca/pages/collab
- Partners: https://powerkitchen.ca/pages/partners
- Corporate: https://powerkitchen.ca/pages/corporate-delivery
- Nutritionist: https://powerkitchen.ca/pages/nutritionist-appointment
- Blog feed: https://powerkitchen.ca/blogs/blog.atom · Price guide post: https://powerkitchen.ca/blogs/blog/meal-delivery-cost-toronto-pk
- Instagram: https://www.instagram.com/powerkitchento/
- Easy Mealz (sister-brand evidence): https://easymealz.ca/ · https://easymealz.ca/products.json
- J&W comparison data: /Users/erwingarcia/Claude/JWFOODSPROPOSAL/research/jw-catalog.json, jw-facts.md, model-assumptions.md

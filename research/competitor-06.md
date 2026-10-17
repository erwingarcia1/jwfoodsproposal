# Competitor #6: Calo (Riyadh, GCC and UK), the AI-personalised meal-plan benchmark

Prepared for Minastech (Erwin Garcia) for the J&W Foods / J&W Meal Butler proposal. Research date: **October 16, 2026.**

**Method.** I read calo.app/en-sa and its sub-pages with WebFetch and curl, and opened them in a real browser for layout and type. Colours and fonts come from Calo's own CSS files. Prices come from the plan configuration embedded in the plans page's `__NEXT_DATA__`; those values exclude VAT, and the page gives `vatPercentage: 15`. The wizard steps come from the plans-page JavaScript, which names each step.

**Limits.** The web-search budget for this run was used up, so I added no third-party news beyond Wamda and CB Insights. From Canada, calo.app/en-gb redirects (HTTP 308) to the global /en page, so I could not open the UK storefront directly. UK facts below come from Calo's own blog and from detoxkitchen.co.uk.

**Currency.** SAR is pegged at 3.75 per USD. I converted at **1 SAR ≈ C$0.379**, using the BoC rate of 1.4196 CAD per USD for 2026-10-15 (see market-benchmarks.md). This is an approximation.

---

## 1. Verdict: operating and premium (verifiedOperating = true)

- **Live in October 2026:**
  - The menu page shows this week's menu, dated **"11 Oct – 17 Oct"** ([menu](https://calo.app/en-sa/menu)).
  - The newest blog post is dated **October 7, 2026** ([blog](https://calo.app/en-sa/blog), [post](https://calo.app/en-sa/blog/food-allergy-meal-subscription)).
  - The footer reads "© 2026 Calo Inc." ([home](https://calo.app/en-sa)).
  - The plans-page config holds a pricing experiment, `personalizedTier: "pricingKSAMay2026Control"`, and a Ramadan 2026 feature flag dated 2026-02-03 to 2026-03-19 ([plans](https://calo.app/en-sa/plans-and-packages), embedded config).
- **UK is live under the Calo brand:**
  - Detox Kitchen's site now says it "is now Calo". Calo launched as a standalone UK brand on 1 March (the page gives no year), and DK meals became Calo-branded from 28 April. The DK site links to calo.app/en-gb ([detoxkitchen.co.uk](https://detoxkitchen.co.uk/)).
  - Calo's April 2026 UK posts include "Calo vs COOK", "Calo vs Simmer Eats", "Calo vs Prep Kitchen" and three London Marathon posts ([blog](https://calo.app/en-sa/blog)).
  - CB Insights lists Calo acquiring **Fresh Fitness Food on April 24, 2025** ([CB Insights](https://www.cbinsights.com/company/fresh-fitness-food/financials)).
  - **freshfitnessfood.com no longer resolves** (DNS lookup failed on Oct 16, 2026), so FFF appears to have been folded into Calo UK.
- **Not in Canada.** The country selector lists World, Saudi Arabia, UAE, Kuwait, Qatar, Bahrain and Oman, and the UK is reached via /en-gb. **There is no Canadian or North American presence**, so the model is open in the GTA.

## 2. Scale signals

| Signal | Figure | Source |
|---|---|---|
| Customers / meals (SA page) | **280K** happy customers in GCC · **18M** meals delivered (company claim) | [calo.app/en-sa](https://calo.app/en-sa) |
| Customers / meals (global page, newer copy) | **290K** customers · **19M** meals (company claim) | [calo.app/en](https://calo.app/en) (en-gb redirect) |
| Funding | **US$64M Series B**: US$25M (Dec 2024, Nuwa Capital lead) plus US$39M extension (July 2025, AlJazira Capital lead). Oversubscribed beyond a US$50M target. Other investors: STV, Khwarizmi, Al Faisaliah, Oraseya | [Wamda, 29 Jul 2025](https://www.wamda.com/2025/07/calo-raises-39-milliion-series-b-extension-boost-global-growth) |
| Revenue | "High-growth nine-figure annualised revenue" (US$). **The press-release text contains an unfilled "($ million)" placeholder, so no number was ever published.** 50%+ YoY growth in H1 2025, led by KSA, UAE and Kuwait | same |
| Meals per year | 10M+ meals in 2024 | same |
| Physical sites | Wamda (Jul 2025): 10+ sites incl. hospital outlets. **Café page (Oct 2026): 12 locations.** Six are shown in Riyadh: Box@ Mall (24h, Car Hop), Kingdom Center, **Kingdom Hospital**, and employee-only cafés at SNB, Zakat Authority and Roshn Sedra | [Wamda](https://www.wamda.com/2025/07/calo-raises-39-milliion-series-b-extension-boost-global-growth); [The Cafe](https://calo.app/en-sa/calo-cafe) |
| Menu breadth | 95+ meals a week, 25+ new each month, 30+ snacks and desserts. UK: 100+ new meals a week, 20+ daily options | [home](https://calo.app/en-sa); [Calo vs COOK, 20 Apr 2026](https://calo.app/en-sa/blog/calo-vs-cook) |
| Corporate | "100+" businesses use Calo for corporate events. Logos: Surface, Alinma Bank, STC, NBB | [corporate-and-business](https://calo.app/en-sa/corporate-and-business) |
| KSA coverage | 25+ cities from Riyadh and Jeddah kitchens | [home](https://calo.app/en-sa) |
| Support | 24/7, "average 90-second response time" (DK rebrand FAQ) | [detoxkitchen.co.uk](https://detoxkitchen.co.uk/) |
| Food safety | HACCP + ISO 22000:2018 kitchens, monthly audits | [allergy post, 7 Oct 2026](https://calo.app/en-sa/blog/food-allergy-meal-subscription) |
| Gym partner | Armah Sports (premium gyms): co-located retail and distribution. Armah's founder sits on Calo's board | [Wamda](https://www.wamda.com/2025/07/calo-raises-39-milliion-series-b-extension-boost-global-growth) |
| App ratings | **Not found.** The App Store URL I tried returned 404, and the search budget was used up. The plans header has a Trustpilot rating slot (component found in the JS), but no value was visible on the SA page | — |

## 3. Pricing (verified Oct 16, 2026)

**KSA, from the plans-page config.** Prices below include 15% VAT, computed from the ex-VAT config values. CAD figures are approximate at C$0.379/SAR.

**Per meal, Balanced / Vegetarian:**
- Lunch or dinner: **SAR 36** (≈ C$13.65)
- Breakfast: **SAR 26** (≈ C$9.85)
- Snack: **SAR 12**

**Per meal, High Protein / Low Carb:**
- Lunch or dinner: SAR 36
- Breakfast: SAR 30
- Snack: SAR 18

**Per meal, Custom Macros:**
- Lunch or dinner: **SAR 47.50** (≈ C$18.00), **+32% vs Balanced**
- Breakfast: SAR 37.50
- Snack: SAR 18

The home page advertises "Starting at SAR 31/meal and SAR 23/breakfast". Those are the **ex-VAT** figures.

**Per day, monthly or quarterly cycle (weekly cycle adds SAR 12/day):**

| Package (config name) | Contents | Balanced | High Protein | Custom Macros |
|---|---|---|---|---|
| `businessLunch` (the minimum) | lunch + snack | **SAR 50** (≈ C$19) | SAR 56 | SAR 67.50 |
| `skipDinner` | B + L + snack | SAR 74 | SAR 84 | SAR 103 |
| `skipBreakfast` | L + D + snack | SAR 84 | SAR 90 | SAR 113 |
| `full` | B + L + D + snack | **SAR 110** (≈ C$41.70) | SAR 120 | **SAR 150.50** (≈ C$57) |
| `ramadan` / `futoor` | seasonal | SAR 108 / 72 | 126 / 90 | 149 / 101.50 |

- Weekly cycle: SAR 62 to 162.50 a day, and the config carries a SAR 10 weekly delivery charge (unit not stated). Monthly and quarterly delivery is free.
- **Minimums:** 2 meals a day, including lunch or dinner, and 5 days a week.
- **Payment:** card, Apple Pay, mada, and the Tabby and Tamara BNPL services. Tamara has a SAR 390 minimum. Pay in 4 is offered on monthly and 3-month plans.
- **Renewal:** auto-renew is on by default for monthly and weekly plans and off for quarterly.
- **Promo:** code TRY15 for 15% off ([allergy post](https://calo.app/en-sa/blog/food-allergy-meal-subscription)).

**Bundles:**
- **1x1:** a 1-month plan plus a 1-month gym membership.
- **3x3:** a quarterly plan plus a 3-month Fitness Time membership.
- Monthly gym partners: OnePass, BodyMasters, BodyMotions, NineRound ([plans](https://calo.app/en-sa/plans-and-packages)).
- **Calo Pro** (annual only), "worth 8,000" (currency not stated):
  - a 12-month gym membership
  - a WHOOP tracker
  - an "Essentials Kit" with a smart scale and bottle
  - up to 12 instalments; pause up to 60 days; refund only within 2 hours ([Calo Pro](https://calo.app/en-sa/calo-pro-product-article)).
  - The price placeholder did not render.

**UK:**
- **£9–£10 per meal**, free daily delivery nationwide (excluding Northern Ireland and the Highlands) ([Calo vs COOK, Apr 20 2026](https://calo.app/en-sa/blog/calo-vs-cook)).
- The DK rebrand cut Detox Kitchen meal prices by about 30% ([detoxkitchen.co.uk](https://detoxkitchen.co.uk/)).

**Café:** prices not shown. First app order 30% off ([The Cafe](https://calo.app/en-sa/calo-cafe)).

**Sanity check for J&W's "Personal Macro Plan" at about C$180/week** (ESTIMATE, my arithmetic on the prices above):
- Calo Custom Macros, lunch + snack × 5 days = SAR 337.50 ≈ **C$128/week**.
- Calo Custom Macros, full day × 5 days = SAR 752.50 ≈ **C$285/week**.
- C$180/week sits inside Calo's own custom-macro range, so it is defensible.

## 4. Flows worth borrowing (step by step)

**A. Plan configurator** ([plans-and-packages](https://calo.app/en-sa/plans-and-packages)). The page has two columns, with a sticky summary on the right.
1. Pick a diet type from five cards with emoji illustrations: Balanced, Custom Macros, Low-Carb, High Protein, Vegetarian. Each card has "View menu →" and "Select Plan". Custom Macros uses "Build my plan" instead.
2. Choose meals per day from chips (Breakfast, Lunch, Dinner, Snack). The minimum is 2, including lunch or dinner.
3. Pick days from an S–S row of circle toggles. The minimum is 5. The layout also has a "batched deliveries" section.
4. Choose a payment cycle (Weekly, Monthly, or 3-months), with optional gym-membership logos.
5. The summary card, "Your package awaits — Starting from 🔥 50/Day", updates live. Then press Continue.
6. Create an account by phone number (+966) with reCAPTCHA.
7. Pay at checkout.

**B. Custom Macros calculator.** This is a modal stepper; the step names come from the plans-page JS. I opened the first step only and submitted nothing.
1. Birthday (DD/MM/YYYY)
2. Gender (two emoji cards)
3. Height in cm (50–300)
4. Weight
5. Activity: four emoji cards, Sedentary / Lightly active / Very active / Highly active
6. Goal: Lose weight / Gain weight / Build muscle / Maintain
7. Target
8. Calories: a searchable dropdown in 5-kcal steps, pre-calculated
9. Protein
10. Carbs
11. Result: a stacked macro bar with an "Edit macros" link, then "plan selected"

Analytics events fire at each stage (`custom_macros_start / calculated / edited / plan_selected`), so Calo measures funnel drop-off.

**C. Self-serve subscription management, in the app:**
- **What customers can change:** edit menu, swap any item, skip, pause, change address or delivery time.
- **Cutoffs:** GCC up to **48h** before delivery ([FAQ](https://calo.app/en-sa/high-protein-meal-plan)); UK **1 business day** ([DK FAQ](https://detoxkitchen.co.uk/)).
- **Pausing:** Account Settings → Pause Subscription → choose a duration.
- **Ingredient exclusions:** unlimited, per meal (UK).
- **Build your own meal:** offered "if nothing on the daily menu hits the spot".
- **App:** stores favourites, dislikes and allergies, and offers AI macro/calorie and progress tracking (UK, [Calo vs COOK](https://calo.app/en-sa/blog/calo-vs-cook)).

**D. Corporate catering checkout** ([corporate-and-business](https://calo.app/en-sa/corporate-and-business)). The pitch is no calls, quotes or PDFs.
1. Pick items, serving sizes and quantities from a 100+ dish menu with calories shown. Formats: bowls, sandwiches, ready-to-eat and ready-to-heat. Filters: nut-, gluten- and dairy-free.
2. Pay by card or BNPL.
3. Food is delivered within 48h.
4. Serve.

There is no form and every CTA reads "Place Your Order". Use cases: board meetings, networking events, team lunches and birthdays.

**E. Affiliate (coaches and creators)** ([calo-affiliate](https://calo.app/en-sa/calo-affiliate)):
1. Fill in a 30-second form.
2. Review takes 15–30 days, and approved partners get an account manager.
3. The partner gets a personal discount code; their client gets a first-order discount.
4. The partner earns "tokens" each time the code is used.

The site also has `/referral/[id]`, wallet and cashback routes (seen in the build manifest).

**F. Consultations** ([consultations](https://calo.app/en-sa/consultations)): a 15–20-minute nutritionist call to calculate calories and pick a plan, and a 10-minute general call about pricing and delivery. Users click "Book a call" and get details on confirmation. The price is not stated.

**G. Market add-ons** ([market.calo.app](https://market.calo.app/en-sa)): snacks, frozen items, supplements, coffee and merch. Subscribers can add Market items to their meal delivery for free.

**H. Café** ([The Cafe](https://calo.app/en-sa/calo-cafe)): the customer orders in the app (Cafe → menu → order) and collects at the counter or by Car Hop. Corporate cafés are open to employees only, and one café is inside a hospital.

**I. AI:** "**Calo Black**", an LLM private chef that builds daily menus from conversation, was **announced as a pilot in July 2025** ([Wamda](https://www.wamda.com/2025/07/calo-raises-39-milliion-series-b-extension-boost-global-growth)). I **found no public Calo Black page or mention** on calo.app in October 2026. The Calo Pro page, the blog and the plans page do not mention it. Treat it as an unconfirmed pilot, not a shipped product.

## 5. Site design (for an inspired J&W prototype; ideas only, not copy)

- **Stack:** Next.js with self-hosted fonts and full EN/AR (RTL) support.
- **Palette** (read from CSS and computed styles):
  - **Primary green `#24A170`**: CTA pill buttons and stepper icons.
  - Hover and dark greens `#28864C`, `#1C7E57`, `#166144`; deepest `#114B34`.
  - Brighter green `#3CAD68` / `#28B17B`.
  - Mint tints `#EAF7F2`, `#EDF5F0`, `#BCE7D6`, `#98D9B1`, `#8ED2B7`, used for testimonial and section backgrounds.
  - **Text charcoal `#343B42`**; secondary text `#697886`.
  - Borders `#EBEDEF`, `#DDE0E4`; disabled `#BDC4CB`; light panels `#F9FAFB` / `#F5F6F7`.
  - Macro accents: purple `#987DDE`, amber `#F4B248`, blue `#64ACEC` (coloured dots for protein, carbs and fat). Error red `#E35044`.
- **Typography:**
  - A humanist sans, served as an obfuscated next/font file. It renders like **Lato**.
  - H1 is **64px / 72px at weight 900**, in charcoal.
  - Body 16px. Buttons 14px bold in **999px pill** shapes.
  - Accent display face: **Bebas Neue**, condensed all-caps, used in a kinetic green statement band.
  - The logo is a spaced, all-caps green wordmark.
- **Shapes:** cards at 12–20px radius (large panels 32px), soft and borderless, on light grey or mint.
- **Layout, top to bottom:**
  1. **Split hero.** The left half is white. Its H1 cycles through audience endings (busy people, lose weight, gain muscle, high performers), with one pill CTA and a small green stats line at the bottom. The right half is a full-bleed lifestyle photo.
  2. Centred "daily-changing menu" section: three trust icons, then a horizontal carousel of dish cards. Each card has a kcal chip, the dish name and coloured macro dots, with diet filter pills underneath.
  3. A three-feature control and flexibility section. Accordion tabs sit on the left and an autoplay product video on the right.
  4. A three-step "How it works" with dark-green number badges.
  5. A Bebas Neue kinetic text band on brand green.
  6. Mint-background testimonial cards with names.
  7. A plan carousel. Each card has an overhead plated-food photo and a chip with an icon and the macro split.
  8. An FAQ accordion in grey rows with + icons, next to a mint "Got more questions?" card that shows support-agent avatars and a "Chat with us" pill.
  9. A creator/UGC carousel.
  10. A footer with an app QR code and a country/language switcher.
- **Photography:**
  - (a) Overhead plated meals on white plates against light stone or grey, in soft natural light. Colourful proteins and vegetables, with the macro chip overlaid.
  - (b) Lifestyle shots of diverse real-looking people eating from branded bowls in warm interiors (deep green walls, wood benches). Branded tote and cup visible.
- **Tone:** short, punchy and second person, with a light wit. It leans on two-beat headline pairs ("Total control. Full flexibility.") and question-then-answer bands. It promises outcomes (macros hit, no prep, no contracts) and sells flexibility and no lock-in.

## 6. What J&W already does better

1. **Butcher heritage and its own inspected plant.** J&W has been an Ontario-inspected meat plant since 2008. The family has been in Toronto butchering and wholesale since the early '60s and 1973 (Advance Food Products), and J&W was founded in 1995. Calo is a 2019 tech-led meal-plan start-up with no butchery ([jw-facts.md](./jw-facts.md); [Wamda](https://www.wamda.com/2025/07/calo-raises-39-milliion-series-b-extension-boost-global-growth)).
2. **Raw and cooked in one cart.** J&W sells 979 SKUs, including AAA, Canadian Prime and Wagyu beef, quarter cows, whole lambs and gift boxes. Calo sells only prepared meals plus a snack market.
3. **À la carte by the ounce with no plan minimum.** J&W sells 4, 5, 6 and 8oz cooked portions, egg bites, oats and sides individually. Calo requires at least 2 meals a day for 5 days a week, and its smallest package is SAR 50 a day.
4. **Salt- and sugar-free with no added oils.** Calo cooks mainly with extra-virgin olive oil and some desserts use butter or coconut oil ([FAQ](https://calo.app/en-sa/high-protein-meal-plan)). J&W suits sodium-restricted and strict-macro customers better.
5. **Price** (ESTIMATE, my arithmetic):
   - **J&W built day ≈ C$28.55–32.55:**
     - egg bites $5.50 + steel-cut oats $4.40
     - Greek Lemon chicken 4oz $4.99 + cilantro-lime basmati $2.35 + broccoli/cauliflower $1.32
     - a pre-set dinner at $9.99–13.99 ([jw-catalog.json](./jw-catalog.json))
   - **Calo full day ≈ C$41.70 (Balanced) and ≈ C$57 (Custom Macros).** J&W is about 25–45% cheaper than Calo Balanced and about 45–50% cheaper than Calo Custom Macros.
6. **Shelf life and logistics.** J&W's flash-frozen, vacuum-sealed BPA-free bags travel on one weekly route across a large part of Ontario. Calo's model depends on costly daily fresh delivery.
7. **Local provenance.** J&W's chicken is air-chilled, grain-fed and Ontario-raised, with no hormones or antibiotics.
8. **A local, human brand.** J&W has a store at Brimley Rd with free pickup, and customers know the owners by name (Bill, Tasia, Lucas). It holds a Google rating of 4.8★ from 611 reviews (model-assumptions.md).
9. **No local Calo.** Calo has no presence in Canada, so J&W can be "the Calo of the GTA" in this premium personalised tier.

## 7. Corrections and caveats on the selection

- **Revenue.** "Nine-figure annualised revenue" is a company claim **with no number**. The Wamda press text contains an unfilled "($ million)" placeholder.
- **Customer and meal counts.** 280K / 18M is the KSA-page figure. The global page now says **290K / 19M**.
- **48h edit window.** This is the GCC rule. In the UK it is **24h / 1 business day**.
- **Calo Black.** It was a **pilot announced in July 2025**. I found no public product in October 2026.
- **"Name on each label (the Fresh Fitness Food model)".** **Not verifiable now.** freshfitnessfood.com no longer resolves, and Calo UK's pages do not mention personalised name labels. Present it as J&W's own idea, not a proven Calo feature.
- **Physical sites.** There are now **12 café locations**, versus the "10+" in Wamda.
- **UK launch.** The UK runs under the Calo brand: Calo launched as a standalone UK brand on 1 March (the page gives no year), and Detox Kitchen meals moved to the Calo brand from 28 April. The FFF acquisition date is April 24, 2025 (CB Insights).

## Sources

- https://calo.app/en-sa: home (stats, FAQ, plans teaser, community)
- https://calo.app/en: global page (290K / 19M; en-gb redirects here from Canada)
- https://calo.app/en-sa/plans-and-packages: configurator, embedded pricing config, wizard JS
- https://calo.app/en-sa/menu: weekly menu, 11–17 Oct
- https://calo.app/en-sa/high-protein-meal-plan: FAQ, build-your-own
- https://calo.app/en-sa/calo-cafe
- https://calo.app/en-sa/corporate-and-business
- https://calo.app/en-sa/consultations
- https://calo.app/en-sa/calo-affiliate
- https://calo.app/en-sa/calo-pro-product-article
- https://calo.app/en-sa/blog
- https://calo.app/en-sa/blog/calo-vs-cook: UK pricing and features, Apr 20 2026
- https://calo.app/en-sa/blog/food-allergy-meal-subscription: Oct 7 2026
- https://market.calo.app/en-sa
- https://detoxkitchen.co.uk/: DK → Calo rebrand
- https://www.wamda.com/2025/07/calo-raises-39-milliion-series-b-extension-boost-global-growth
- https://www.cbinsights.com/company/fresh-fitness-food/financials
- https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/ (via market-benchmarks.md)

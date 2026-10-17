# Play 1: Goal Plan Builder

Modelled on **Power Kitchen** (powerkitchen.ca, East York, Toronto). Prepared by Minastech for J&W Foods / J&W Meal Butler, October 16, 2026.
All money is CAD. Every figure is an **estimate** unless it is J&W's own published price (jwfoods.com, Oct 16 2026) or a cited source. Macros are **estimates** (USDA reference values in `site/assets/catalog.js`); J&W publishes no nutrition panels today.

---

## At a glance

| | |
|---|---|
| **One-liner** | A 60-second quiz matches GTA shoppers to one of six goal plans built from real Meal Butler meals, sold as a skip-anytime subscription (weekly, every 2 weeks or a monthly Freezer Fill) with 10% off. |
| **Why it makes money** | Standing orders turn one-off Meal Butler carts into predictable, recurring revenue at about 40% gross margin, using meals J&W already cooks. |
| **Focus** | Quiz-led goal plans on a skip-anytime subscription |
| **Start** | Month 2 (December 2026). November is the build month. |
| **Year 1 (Nov 2026 to Oct 2027), added revenue** | Low **$175K** · Mid **$350K** · High **$580K** |
| **Run-rate (year 2), added revenue** | **~$757K** (low ~$380K, high ~$1.2M) |
| **Gross margin** | **40%** (subscription meal prep after the 10% discount, model-assumptions.md) |
| **JW's own costs** | ~$7K setup + ~$7,450 a month in year 1 (staff, ads, offers, software, discount leakage) |

---

## 1. What Power Kitchen proves

**Who they are.** A family-owned, bootstrapped GTA meal-prep company (District 28 Company Limited) with its kitchen at 46 Hollinger Rd, about 10 km from Brimley Rd. It sells eight goal plans (Power, Pro Athlete, GLP-1 Support, Low Carb, Clean Bulking, Keto, Lean Muscle, Vegan) through a plan-matching quiz and an auto-renewing subscription that customers can skip, pause or edit before a cut-off.

**Proof, verified Oct 16 2026 (competitor-01.md):**
- Goal boxes list at **$16.22 to $36.95 a meal**. Power and Lean Muscle are $17.85 to $23.95; Pro Athlete $21.77 to $26.97; GLP-1 Support $21.76 to $27.96 (products.json).
- Subscribe discount is **5%**, plus 5% back in store credit. One-Month Trial is 20 prepaid meals for $365 to $535. Delivery is $9.99 to $14.99, free over $180.
- **4.7 stars from 564 Google reviews** (live widget). 185 SKUs, all updated Oct 16 2026. Own driver fleet to about 40 cities on Sunday and Wednesday. Weekly blog posts, Instagram 11.4K.
- Martech that signals real paid spend: Klaviyo, Triple Whale, Zoho PageSense, Sezzle, a loyalty app, an SMS bot for delivery windows.
- Revenue is not published. Estimate, low confidence: about **$3 to 7M a year** (400 to 900 orders a week at $150 to $170).

**Ideas we borrow (ideas only, never their copy, photos or logos):**
1. A short quiz that routes to a named goal plan and shows a price per meal.
2. Goal plans with macros printed on every meal card.
3. A sticky builder bag with a "meals chosen" counter and a smart auto-fill.
4. A skip, swap, pause portal with a hard weekly cut-off.
5. A chef's default box when the customer does nothing (also a Protein Chefs idea).
6. A "have you used another service?" quiz step, used as switch intelligence.
7. A prepaid multi-week commitment program (their 6-Week "Earn It Back").

**Where J&W already beats them:**
1. **Owns the protein.** An Ontario-inspected meat plant since 2008; J&W cuts, cooks and portions in-house. Power Kitchen buys proteins in.
2. **Price.** J&W plan meals land at **$7.30 to $13.02 with Subscribe & Save** (below), against $16 to $27 for Power Kitchen's comparable plans. On like-for-like 4 to 6oz meals that is roughly **25 to 45% less per meal** (estimate; portion bases differ and neither side states raw or cooked weight).
3. **Frozen vacuum packs.** Fresh rivals last 3 to 10 days, which forces a weekly cycle. J&W can sell a **monthly Freezer Fill** and reach long-haul Ontario routes (Ottawa, Kingston, London, Windsor, Barrie).
4. **Clean recipes.** "Salt and sugar free, with no added oils" (J&W's own claim). Power Kitchen ingredient lists include salt, oils and sweeteners.
5. **Households.** Power Kitchen needs one order per person. J&W can put several people's plans in one box with one delivery fee.
6. **Bigger social proof.** Google 4.8 from 611 reviews and 30K Instagram followers, against 4.7/564 and 11.4K.
7. **Store and pickup.** Free pickup at Brimley Rd Mon to Fri 9 to 6 and Sat 10 to 4, against Power Kitchen's two short pickup windows.

---

## 2. The mechanism: what J&W changes

J&W adds a quiz, six goal plans and a subscription to jwfoods.com. **Every plan is built only from Meal Butler items J&W sells today**, priced as the sum of the real item prices, then 10% off when the customer subscribes. Nothing new has to be cooked.

### 2.1 The six plans (prices from jwfoods.com, Oct 16 2026; macros are estimates)

| Plan | For | Meals in the rotation (real SKUs and prices) | Est. per meal (kcal / P / C / F) | Default box | One-off | Subscribe & Save (10%) | Per meal (S&S) |
|---|---|---|---|---|---|---|---|
| **Lean** | Fat loss | Turkey, Spinach & Rice 4oz $12.99 · Tilapia, Asparagus & Brown Rice 4oz $11.99 · Jerk Chicken, Green Beans & Sweet Potato 4oz $12.99 · Tenders, Broccoli & Sweet Potato 4oz $9.99 · Teriyaki Chicken, Green Beans & Rice 4oz $9.99 · Arabic 7 Spice plate (chicken 4oz $4.50 + brown basmati 3oz $1.16 + broccoli 4oz $1.39 = $7.05) | 337 / 37g / 33g / 4g | 10 meals | $112.96 | **$101.66** | **$10.17** |
| **Lean Bulk** | Muscle gain | Souvlaki, Broccoli & Greek Potatoes 6oz $15.99 · Flank Steak, Green Beans & Potato 6oz $17.49 · Salmon, Brussels & Quinoa 6oz $16.79 · Jerk power plate (Jerk Chicken 6oz $6.30 + white basmati 6oz $2.31 + broccoli $1.39 = $10.00) · Sirloin plate (Ground Top Sirloin 6oz $10.99 + sweet potato 6oz $2.34 + green beans $0.84 = $14.17) · Souvlaki cilantro-lime plate (Souvlaki 6oz $6.93 + Cilantro Lime Rice $2.35 + Mixed Veggies $0.66 = $9.94) | 523 / 54g / 40g / 13g | 10 meals | $144.65 | **$130.18** | **$13.02** |
| **Athlete** | Trains 5+ days | Beef Flank Fajita Wrap $9.99 · Chicken Fajita Wrap $8.99 · Salmon, Brussels & Quinoa 6oz $16.79 · Souvlaki rice plate (Souvlaki 6oz $6.93 + white basmati 6oz $2.31 + broccoli $1.39 = $10.63) · Flank Steak, Green Beans & Potato 6oz $17.49 · Teriyaki Chicken, Green Beans & Rice 4oz $9.99 | 476 / 44g / 40g / 12g | 10 meals + Breakfast 5-pack | $120.28 | **$108.25** | **$10.83** |
| **Protein & Greens** (working name for "low carb") | Fewer starches | Souvlaki 6oz $6.93 + Cauliflower Rice $0.96 + Broccoli $1.39 = $9.28 · Salmon 6oz $10.85 + Asparagus $1.89 + Cauliflower Rice $0.96 = $13.70 · Korean BBQ Flank 4oz $8.99 + Cauliflower Rice + Green Beans = $10.79 · Roasted Turkey 6oz $8.40 + Spinach $1.10 + Broccoli & Cauliflower $1.32 = $10.82 · Haddock 6oz $8.25 + Asparagus + Cauliflower Rice = $11.10 · Korean BBQ Chicken 4oz $4.99 + Broccoli & Cauliflower $1.32 + Brussels $0.84 = $7.15 | 301 / 46g / 12g / 8g | 14 meals | $148.66 | **$133.79** | **$9.56** |
| **GLP-1 Companion** | Smaller appetites, incl. people on GLP-1 medicines | Tenders 3oz $3.14 + Quinoa 3oz $1.95 + Brussels $0.84 = $5.93 · Lemon Chicken Rice Soup 10oz $8.99 · Salmon 4oz $7.99 + Broccoli $1.39 + Quinoa 3oz $1.95 = $11.33 · Roasted Turkey 4oz $5.60 + Spinach $1.10 + Brown Basmati 3oz $1.16 = $7.86 · Chicken Chili 10oz $9.99 · Egg White Bites, Spinach & Feta $5.25 | 272 / 27g / 23g / 7g | 14 small meals | $113.62 | **$102.26** | **$7.30** |
| **Busy Family** | Households with kids | Souvlaki, Broccoli & Greek Potatoes 4oz $13.99 · Teriyaki Chicken, Green Beans & Rice 4oz $9.99 · Kids meatball plate (Beef Meatballs 4oz $2.19 + white basmati 4oz $1.54 + Mixed Veggies $0.66 = $4.39) · Kids tenders plate (Tenders 3oz $3.14 + sweet potato 4oz $1.56 + broccoli $1.39 = $6.09) · Chicken Chili 10oz $9.99 · Tenders, Broccoli & Sweet Potato 4oz $9.99 | 367 / 35g / 36g / 8g (avg of adult and kid plates) | 20 plates | $187.30 | **$168.57** | **$8.43** |

Box prices cycle through the six meals in order (10 meals = each meal once, plus the first four again). Sizes are 10, 14, 20, 28 or 40 meals.

**Notes on the plans**
- "Protein & Greens" is used instead of "Low Carb" or "Keto". J&W cooks without added oil, so the plan is not keto, and "low carb" style wording is a regulated nutrient content claim in Canada. A labelling review must clear every plan name and macro statement before launch.
- GLP-1 Companion is food, not medical advice. Every mention carries "Follow your prescriber's advice on protein and calories."
- The **route minimum is $100 after the discount**. Lean 10, Lean Bulk 10 and Athlete 10 clear it. Protein & Greens and GLP-1 Companion default to 14 meals so they clear it. Smaller boxes are pickup-only, or the builder nudges a Breakfast 5-pack.

### 2.2 How the subscription works
- **Cadence:** weekly, every 2 weeks (default), or a **monthly Freezer Fill**. The Freezer Fill is the J&W-only option, made possible by frozen vacuum packs. One delivery a month means one route fee a month (e.g. $20 on the Wednesday route instead of $80 for four weekly boxes). Orders over $200 may also qualify for J&W's existing free-delivery-from-$200 offer (jwfoods.com/pages/free-delivery; confirm the rule with J&W).
- **Cut-off:** J&W's current rule, "order by Sunday for next week's delivery." Customers can skip, swap or pause (1 to 8 weeks) until Sunday night. Skipped weeks are never charged.
- **Delivery:** the existing Tue to Fri GTA routes ($20 to $27) and long-haul routes ($35), $100 minimum, or free pickup at 2201 Brimley Rd. No new delivery days and no new vans.
- **Butcher's Pick:** if the customer changes nothing by Sunday night, the kitchen's chosen box for their plan ships. It rotates flavours (Greek Lemon, Korean BBQ, Arabic 7 Spice, Teriyaki, BBQ, Jerk) within the plan's macros.
- **Household box:** each person in the home gets a profile and a plan. All of it ships in one box with name tags on the packing list: one delivery, one fee, one Sunday reminder. Example: Alex on Lean Bulk (10 meals, $144.65) + Sam on GLP-1 Companion (10 small meals, $83.46) + kids (3 meatball plates + 3 tenders plates, $31.44) = $259.55, or **$233.60 every 2 weeks** with Subscribe & Save.
- **Credits apply on their own.** Switch credits, referral credits and Smile.io points apply at checkout with no email to support. Power Kitchen makes customers email support to use store credit.
- **Concept offers:** a **$25 switch credit** on the first subscribed box for anyone coming from another meal service (the quiz asks; Goodfood is distressed and LiveFit has closed). A **6-Week Reset**: six weekly boxes prepaid at 12% off, launched for January. For example Lean Bulk 10 meals × 6 = $867.90, so **$763.75 prepaid**. The route fee still applies to each delivery.
- **Breakfast 5-pack (Concept):** 3 Egg White Bites, Spinach & Feta ($5.25) + 2 Steel Cut Oats ($4.40) = $24.55, or $22.10 with Subscribe & Save.

### 2.3 What the customer sees (mirrors the prototype)
Quiz (about 60 seconds) → result card with the plan, a short reason, est. macros, price per meal and three offers (Try one box · Subscribe & Save, recommended · 6-Week Reset) → builder pre-filled with the Butcher's Pick → checkout on J&W's real routes → My Plan portal to skip, swap, pause, change cadence or cancel (with a save offer).

### 2.4 What this play is not (kept distinct from plays 2 to 7)
- Not the **AI Coach** (Play 6). The quiz here is a short, rules-based router to six fixed plans. Chat-based personal macro plans, grams on labels and in-store body scans belong to Play 6. Subscribers who come in through the coach chat are counted in Play 6 only.
- Not the **Butcher Club** (Play 3). Cooked meals only. Raw-meat boxes are Play 3; that play reuses this play's subscription app.
- Not the **Pro Partner Portal** (Play 2) or **Team Fuel** (Play 7). No gym, team or school channel here. The 6-Week Reset is sold direct, not through gym partners.
- Not **J&W at Work** (Play 4) or the **Gift Studio** (Play 5). Consumers only.

---

## 3. The money

### 3.1 Year 1 (Nov 2026 to Oct 2027), mid case

Inputs (model-assumptions.md and market-benchmarks.md):
- **Average box** $125 after 10% off ($139 before). 26 scheduled deliveries a year (an every-2-weeks equivalent across the weekly, every-2-weeks and monthly mix), 10% skipped. So **$243.75 a month** per active subscriber ($125 × 26 × 0.9 ÷ 12).
- **New subscribers** (people who were not already weekly Meal Butler buyers): Dec 25 · Jan 60 (New Year push, 6-Week Reset) · Feb 45 · Mar 35 · Apr 35 · May 30 · Jun 25 · Jul 25 · Aug 30 · Sep 40 · Oct 40 = **390**.
- **Monthly churn 9%.** That sits between standing-order replenishment (5 to 8%) and meal kits (8 to 15%) (Eightx).
- **One-off plan boxes** from quiz takers who don't subscribe: 220 in year 1 at $135.
- **Incrementality 0.8.** Some of these customers would have ordered anyway (model-assumptions.md: 0.75 to 0.85).

| Month | New subs | Active at month end | Subscription revenue | One-off boxes |
|---|---|---|---|---|
| Nov 2026 | 0 (build) | 0 | $0 | $0 |
| Dec | 25 | 25 | $3,047 | $1,350 |
| Jan 2027 | 60 | 83 | $13,132 | $4,725 |
| Feb | 45 | 120 | $24,747 | $3,375 |
| Mar | 35 | 145 | $32,270 | $2,700 |
| Apr | 35 | 167 | $37,897 | $2,700 |
| May | 30 | 182 | $42,408 | $2,025 |
| Jun | 25 | 190 | $45,294 | $2,025 |
| Jul | 25 | 198 | $47,312 | $2,025 |
| Aug | 30 | 210 | $49,757 | $2,025 |
| Sep | 40 | 231 | $53,810 | $3,375 |
| Oct | 40 | 251 | $58,717 | $3,375 |
| **Total** | **390** | **avg 140** | **$408,390** | **$29,700** |

**Formula (mathYear1):** subscribers ramp from 0 (November build month) to 251 by Oct 2027 on 390 new subscribers and 9% monthly churn. That gives 1,675 subscriber-months (average 140 active) × $243.75 = **$408K**, plus 220 one-off plan boxes × $135 = **$30K**. Gross $438K × 0.8 incrementality = **$350K added revenue** (mid).

- **Low:** 245 new subscribers, 12% churn, $120 box with 12% skipped, 113 one-off boxes at $125, incrementality 0.75. Gross $237K, so **~$175K**.
- **High:** 555 new subscribers, 7% churn, $130 box, 325 one-off boxes at $140, incrementality 0.85. Gross $682K, so **~$580K**.

### 3.2 Run-rate (year 2, Nov 2027 to Oct 2028)

**Formula (mathRunRate):** start with 251 active, add 35 a month, churn 8.5% (better skip, pause and save flows). Average 312 active × $2,925 a year ($125 × 26 × 0.9) = **$914K**, plus 240 one-off boxes × $135 = **$32K**. Gross $946K × 0.8 = **~$757K a year** of added revenue.
- Low: 25 a month at 11% churn → ~$380K. High: 45 a month at 7.5% churn → ~$1.2M. The high case would need a second packing shift.
- Cross-check: market-benchmarks.md §11 says ~320 active every-2-weeks subscribers at $120 is about $1M gross. This play's year-2 average of 312 at a $125 box with skips gives $914K gross, which is consistent.

### 3.3 Margin, costs and contribution

**Gross margin 40%** on subscription boxes after the 10% discount; 45% on one-off boxes. The blend is treated as 40% to stay conservative.

**J&W's own costs** (estimates, excluding Minastech's fee):

| Item | Setup | Year 1 (Dec to Oct) |
|---|---|---|
| Nutritionist review of plan rules and ~31 plan SKUs' macros | $2,500 | |
| Lab nutrition analysis, top 8 plan SKUs (~$200 each, not verified) | $1,600 | |
| Plan photos and short videos (in-house plus a freelancer) | $1,200 | |
| Plan labels: design and first print run | $800 | |
| Staff training on the portal and packing by plan (36 h × $25) | $900 | |
| Software: subscription app ~$200/mo, Klaviyo email and SMS share ~$250/mo, AI agent tokens ~$100/mo, reviews app $15/mo | | $6,215 |
| Paid ads: ~175 paid new subscribers × ~$85 CAC (within the $60 to $120 range) | | $15,000 |
| Offers: $25 switch credit × ~150 + $20/$20 referrals × ~60 | | $6,150 |
| Meal Butler lead, plan coordination: 12 h/week × 46 weeks × $25 loaded | | $13,800 |
| Part-time cook/packer from February: avg 27 h/week × 38 weeks × $25 | | $25,650 |
| Plan label on each box: $0.60 × ~3,500 boxes | | $2,100 |
| Discount leakage: ~60 existing weekly buyers who switch get 10% off revenue J&W already had | | $13,000 |
| **Total** | **$7,000** | **$81,915 (~$7,450 a month)** |

- Year 1 mid: $350K × 40% = **$140K gross profit**, minus ~$89K all-in costs = **~$51K contribution** before Minastech's fee.
- Year 2: $757K × 40% = **$303K gross profit**, minus ~$120K running costs (staff ~$69K at volume, ads ~$16K, discount leakage ~$18K, offers, labels, software) = **~$183K contribution**.
- Delivery: subscribers pay the existing route fee ($20 to $35), which covers an owned-route stop at $8 to $14. Freezer Fill boxes over $200 that ride free cost J&W about $8 to $14 a stop. That cost is small and already in the margin range.
- The 40% margin is treated as covering food, packaging, card fees and today's kitchen labour per meal, in line with the Goodfood benchmark (41.7%). The part-time cook/packer line is added on top to be safe.

### 3.4 Sanity check
- J&W baseline is about $2.5M (range $1.2 to 4.0M) with 15 to 25 staff. Year 1 mid of $350K is +14% on the mid baseline. The year-2 run-rate of $757K is +30%.
- Volume: about **68 extra boxes a week** on average in year 1 (~850 meals) and **~146 a week** in year 2 (~1,800 meals). The audit estimates J&W runs 60 to 160 delivery orders a week today, so this roughly doubles route orders by year 2. Production headroom at the plant **must be confirmed** before the January push.
- This is within the typical range for one play ($60K to $450K year 1; run-rate under $900K).

---

## 4. KPIs

| KPI | Target |
|---|---|
| Quiz completions | 800 a month on average; 1,200 in January 2027 |
| Quiz → first plan order | 7% |
| Plan buyers who choose Subscribe & Save | 60% or more |
| Active subscribers | 140 average in year 1; 250 by Oct 2027; 310 average in year 2 |
| Monthly churn | 9% or lower in year 1; 8.5% in year 2 |
| Skipped deliveries | 12% or fewer of scheduled boxes |
| Average box after discount | $125 or more |
| Paid CAC per new subscriber | $90 or less |
| Freezer Fill share of subscribers | 20% |
| M3 / M12 subscriber retention | 70% / 45% |

---

## 5. AI agents this play needs (merge into the shared roster)

| Agent | Job in this play | What the prototype shows |
|---|---|---|
| **Macro Butler (plan matcher)** | Scores quiz answers into one of six plans, sets box size and cadence, splits a household into profiles, and writes a two-line "why this plan" note from owner-approved templates. Medical, allergy or eating-disorder signals go to a person. Chat-based personal plans hand off to Play 6. | The result card ("Why we picked Lean Bulk for you") and the household split. |
| **Nutrition Data Agent** | Computes est. macros for the ~31 plan SKUs from recipes, cooked yields and Health Canada CNF values. Writes them to Shopify metafields and queues each panel for a nutritionist's sign-off. Flags claim wording ("high protein", "low carb", GLP-1). | "est." macro chips on every card; team tile "Macro sign-off: 9 of 31 verified". |
| **Butcher's Pick Menu Agent** | Drafts next week's default box for each plan within stock, par levels and margin, and rotates flavours so subscribers don't get bored. The owner approves. | Team approval card: "Butcher's Pick, week of Mar 29: Lean swaps Tilapia pre-set for Haddock plate (tilapia below par)". |
| **Subscription & Reorder Agent** | Sends Saturday SMS and email reminders before the Sunday cut-off. Handles OK, SKIP, SWAP and PAUSE replies in plain language. Proposes cancel-save offers within owner-set limits and follows up failed payments. CASL consent is checked. | SMS preview on My Plan; the cancel-save modal; team save-offer approvals. |
| **Production Forecast Agent** | After the Sunday cut-off, turns subscription lines into Monday's cook, portion and pack sheet, box counts by route day, and the raw purchase list. | Team prep sheet table and route-impact panel. |
| **Lifecycle Marketing Agent** | Quiz-abandon emails, a welcome series for each plan, the January Reset campaign and the switch campaign. The owner approves every send. | Team "campaign drafts awaiting approval". |
| **Review & Reputation Agent** | Asks subscribers for a review after their second box and drafts replies. Low-star replies need a person's approval. No incentives without disclosure. | Team review-reply queue. |

---

## 6. Who at J&W does the work
- **Meal Butler lead** (e.g. Lucas or Tasia): 8 to 12 h/week on plan menus, AI-draft approvals and subscriber messages.
- **Owner** (Bill): about 1 h/week reviewing the Monday digest and approving offers.
- **Kitchen:** one part-time cook/packer from February, 20 h/week rising to 35 h/week by October.
- **Store counter:** about 2 h/week handing out pickup plan boxes.
- **Minastech** builds the quiz, plans, subscription setup and agents (fee is separate and not counted here).

---

## 7. Assumptions
1. Average subscription box $125 after 10% off ($139 before). 26 scheduled deliveries a year, 10% skipped, so $2,925 a year per active subscriber.
2. 390 new subscribers in year 1 (December to October). None in November, the build month. Existing weekly Meal Butler buyers who switch are **not** counted as revenue; only their discount cost is counted.
3. Monthly churn 9% in year 1 and 8.5% in year 2 (Eightx: replenishment 5 to 8%, meal kits 8 to 15%).
4. 220 one-off plan boxes in year 1 and 240 in year 2, at $135.
5. Incrementality 0.8 (model-assumptions.md: 0.75 to 0.85).
6. Gross margin 40% after the 10% discount (model-assumptions.md).
7. About 45% of new subscribers come from paid ads at about $85 CAC. The rest come from Instagram (30K), email, the store counter and referrals.
8. Delivery runs on the existing routes. The customer pays the current $20 to $35 fee or picks up free.
9. The plant can absorb about 850 extra meals a week in year 1 and about 1,800 in year 2 (to confirm with J&W).
10. Prices are J&W's online prices on Oct 16 2026. Macros are estimates until verified.

---

## 8. Risks and how to handle them
1. **Claims and macros.** J&W shows no nutrition panels, and "high protein", "low carb" and GLP-1 wording are regulated or sensitive under Canada's Food and Drug Regulations. *Handle it:* label macros "est." until a nutritionist signs off, use "Protein & Greens" instead of "Low Carb", and get a labelling review before launch.
2. **Discount leakage.** Existing weekly buyers may move to 10% off (~$13K in year 1). *Handle it:* Subscribe & Save applies to plan boxes only, not to à la carte carts.
3. **Kitchen capacity and stockouts** on plan SKUs (e.g. tilapia or salmon). *Handle it:* the Production Forecast Agent sets par levels, and Butcher's Pick swaps within the plan.
4. **Churn above the model.** Meal kits churn 8 to 15% a month, and 44% of cancellations happen in the first 90 days. *Handle it:* skip and pause, monthly Freezer Fill, save offers and failed-payment follow-up. The low case uses 12% churn.
5. **One route day per zone.** Fresh rivals deliver Sunday and Wednesday. *Handle it:* the frozen format makes once-a-week (or once-a-month) enough. Express ($30) stays for urgent orders.
6. **Overlap with Play 6 (AI Coach).** Both draw on the same subscribers. *Handle it:* count quiz-led subscribers here and chat-led personal plans in Play 6 only.
7. **Owner-led brand risk** (a 2020 Yelp complaint about owner remarks). *Handle it:* front the plans with the Meal Butler team and the product.
8. **Comparative pricing.** *Handle it:* customer-facing copy quotes a public price range ("about $16 to $27 a meal, Oct 2026"), not a named rival, and the figures are rechecked each quarter.

---

## 9. Prototype spec (for the front-end builder)

File: `site/prototypes/01-goal-plan-builder.html`. One self-contained page on the shared framework (`site/FRAMEWORK.md`): `JWC.init({ n: 1, ... })` gives the concept bar, the Customer / JW team toggle, the cart, the demo checkout on J&W's real routes, the AI chat and the "Why this makes money" drawer. Do not rebuild them.

### 9.1 Concept
The page shows how J&W can sell the meals it already cooks as goal plans on a subscription, the way Power Kitchen does, but in J&W's voice and at J&W's prices. A shopper answers a short quiz and gets a named plan with est. macros and a real price per meal, built from current Meal Butler SKUs. They can subscribe weekly, every 2 weeks or as a monthly Freezer Fill, then manage it in a My Plan portal (skip, swap, pause, cancel with a save offer). The JW team view shows the subscriber base, the Monday prep sheet, route impact and the AI-agent drafts waiting for approval.

**The "wow" moment:** pick a goal and a priced, macro-counted box of real J&W meals assembles itself as a stack of freezer bags. Flip "Every 2 weeks" to "Monthly Freezer Fill" and the stack grows to a month of meals, the price per meal holds, and the route-fee line drops from four fees a month to one.

### 9.2 Design direction
- **Inspired by:** Power Kitchen's structure (cut-off announcement bar, quiz card with a step tracker, goal-plan cards with macro chips, a sticky builder bag, a dark rounded trust panel). Rebuilt in J&W's laurel navy, Meal Butler slate purple and sky blue on a warm kraft-cream ground, with a premium serif. Butcher-heritage cues: kraft-paper textures and vacuum-pack visuals.
- **Palette:**

| Hex | Role |
|---|---|
| #154D8E | J&W navy: primary buttons, links, header logo zone, Lean Bulk accent |
| #0E1B4D | Deep ink: headings, the dark trust panel, footer |
| #5B5A8C | Meal Butler slate purple: the recommended offer card, "My Plan", GLP-1 Companion accent |
| #7FB3D5 | Sky blue: selected quiz options (as a border or tint), progress tracker, Lean accent. Never as text on white. |
| #E6F0F8 | Sky tint: quiz-selected background, info chips |
| #F7F3EC | Kraft cream: page background |
| #D9C7A7 | Kraft tan: Freezer Fill bag illustrations, dividers |
| #FFFFFF | Cards |
| #A23B2A | Butcher red: cut-off countdown and Athlete accent only |
| #0F7B4F | Savings green: Subscribe & Save rows, Protein & Greens accent |
| #B7791F | Amber: Busy Family accent and "Concept" tags (dark text on a light amber tint) |
| #566072 | Muted body text |

- **Fonts:** display **Fraunces** (Google Fonts, 600/700, optical size on); body **Inter** (400/500/600).
- **Layout:** mobile-first single column at 375px; 12-column grid at 1024px+. The quiz is a centred white card (max 720px) with 16px radius. Plan cards are a 1 / 2 / 3-column grid. The builder is a two-pane layout on desktop with a sticky right-hand bag; on mobile the bag is a bottom sheet with a sticky "14 of 14 meals · $182.02" bar. Quiz options are full pills (min 44px tall). Soft shadows and 12 to 16px radii.
- **Tone:** plain, warm, specific, Canadian spelling (fibre, flavour, favourite). Short sentences. No hype words, no emoji. "We" is the J&W family kitchen. Every macro shows "est.".

### 9.3 Sections in order (customer view, `data-customer` where needed)

1. **Cut-off bar** (thin, deep ink #0E1B4D, white text): "Change or order your plan by Sunday night for next week's route. Pickup at 2201 Brimley Rd is always free." On the right, a live countdown "Cut-off in 2d 6h" computed to the next Sunday 11:59 pm.
2. **Header:** J&W laurel logo (`../assets/img/jw-logo.jpg`, alt "J&W Foods, established 1995") + "Meal Butler Plans". Nav: Plans · How it works · Find my plan · My Plan · cart button (calls `JWC.cart.open()`, shows `JWC.cart.count()`).
3. **Hero** (image `../assets/img/meals.jpg`, overhead meal-prep photo, alt "Meal Butler meals: salmon with quinoa, chicken with broccoli, flank steak with green beans"):
   - Eyebrow: "Goal plans by J&W Meal Butler"
   - H1: "Pick your goal. We'll cook the plan."
   - Sub: "Six goal plans made from Meal Butler meals we already cook, portion and freeze at our Ontario-inspected plant in Scarborough. Salt and sugar free, with no added oils. Skip or swap any week."
   - Buttons: "Find my plan (about 60 seconds)" (scrolls to the quiz) · "See the six plans".
   - Trust chips: "4.8 on Google · 611 reviews" · "Butchers since 1995" · "Ontario-inspected plant since 2008" · "30K on Instagram".
   - Floating price card: "From **$7.30 a meal** with Subscribe & Save. Most plans $9.56 to $13.02 a meal. Premium GTA goal plans list at about $16 to $27 a meal (public prices, Oct 2026)."
4. **How it works** (4 steps, numbered navy circles): 1 "Take the quiz. Goal, training, who's eating." · 2 "Get your plan. Meals, est. macros and a price per meal." · 3 "Pick a rhythm. Weekly, every 2 weeks, or a monthly Freezer Fill." · 4 "Stay in control. Skip, swap or pause until Sunday night."
5. **The quiz** (H2 "Find my plan", 8 steps with a dot tracker and Back / Next; a short note after each answer in muted italic):
   - Q1 "What's your main goal?" Lose fat · Build muscle · Train hard (5+ days) · Eat fewer starches · I'm eating less on a GLP-1 medicine · Feed the whole family. Note: "Good. We'll build around that."
   - Q2 "How many days a week do you train?" 0 · 1–2 · 3–4 · 5–6 · 7.
   - Q3 "Who's eating?" Just me · Two adults · A family with kids. Note on 2+: "We can pack everyone's plan in one box."
   - Q4 "How many lunches and dinners should we cover each week?" 5 · 7 · 10 (most popular) · 14.
   - Q5 "How often should we deliver?" Every week · Every 2 weeks (most popular) · Once a month (Freezer Fill). Note: "Our meals are frozen in vacuum packs, so a month at once works."
   - Q6 "Anything to leave out?" (multi-select chips) Fish · Red meat · Eggs and dairy · Spicy · Rice. Note: "Allergies? Call us at (416) 298-1350 before you order."
   - Q7 "Are you switching from another meal service?" No · Goodfood · Factor · LiveFit · Another meal-prep service. Any yes: "Welcome. We'll take $25 off your first subscribed box (concept offer)."
   - Q8 "Where should we deliver?" A select of `JWC.cities()` plus "I'll pick up at Brimley Rd". It shows the route live, e.g. "Toronto: Wednesday route (GTA 2), $20, $100 minimum".
   - Loading line (1.2 s): "Building your plan from this week's Meal Butler menu…"
   - **Result card** (white, slate-purple top border):
     - H3: "Your plan: Lean Bulk".
     - "Why this plan" (AI-drafted; label "Drafted by Macro Butler from your answers"): e.g. "You train 3–4 days and want to build muscle, so every meal has a 6oz protein and a proper serving of rice or potatoes."
     - Est. macros per meal: "523 kcal · 54g protein · 40g carbs · 13g fat (est.)".
     - Box line: "10 meals every 2 weeks · $130.18 with Subscribe & Save ($13.02 a meal)".
     - Route line from Q8, plus the monthly maths: "About $282 a month for 20 meals" (box × deliveries a month).
   - **Three offer cards:**
     - "Try one box": one-off price, "No subscription".
     - "Subscribe & Save, Recommended" (slate purple card): "10% off every box · Skip, swap or pause until Sunday night · Butcher's Pick if you don't choose". Shows "$25 switch credit applied" if Q7 = yes.
     - "6-Week Reset": "6 weekly boxes, prepaid, 12% off. Starts the week you choose." e.g. "Lean Bulk: $763.75 for 60 meals".
   - If Q3 is 2+ people, add a link: "Build a household box instead".
6. **The six plans** (H2 "Six plans. One butcher."; one card per plan with the plan accent as a left rule):
   - Each card: eyebrow, name, one-line promise, a photo strip of 3 real product images (`JWC.img(p,400)`), macro chips "kcal · P · C · F (est.)", price per meal with S&S (large), one-off box price (small), 3 bullets and the button "Build this plan".
   - Lean: eyebrow "Fat loss". "Lighter plates, lean protein in every meal." Bullets: "Turkey, tilapia and chicken meals" · "Rice or sweet potato, measured" · "10 meals $101.66 with Subscribe & Save". Chips 337 · 37g · 33g · 4g.
   - Lean Bulk: eyebrow "Muscle gain". "6oz proteins and a proper serving of carbs." Bullets "Souvlaki, flank steak, salmon, sirloin" · "Rice or potatoes in every meal" · "10 meals $130.18". Chips 523 · 54g · 40g · 13g.
   - Athlete: eyebrow "Train 5+ days". "Grab-and-go wraps plus big plates for heavy weeks." Bullets "Beef and chicken fajita wraps" · "Add the Breakfast 5-pack" · "10 meals $108.25". Chips 476 · 44g · 40g · 12g.
   - Protein & Greens: eyebrow "Fewer starches". "Rice and potatoes swapped for cauliflower rice and green veg." Bullets "Salmon, haddock, turkey, Korean BBQ flank" · "Cauliflower rice, asparagus, spinach" · "14 meals $133.79". Chips 301 · 46g · 12g · 8g.
   - GLP-1 Companion: eyebrow "Smaller appetite". "Smaller portions, protein first, fibre-rich sides." Bullets "3–4oz proteins with quinoa and Brussels sprouts" · "Soups and egg bites for light days" · "14 small meals $102.26". Chips 272 · 27g · 23g · 7g. Fine print: "Food, not medical advice. Follow your prescriber's advice on protein and calories."
   - Busy Family: eyebrow "Household". "Grown-up plates and kid-sized plates in one box." Bullets "Souvlaki and teriyaki for adults" · "Meatball and tender plates for kids" · "20 plates $168.57". Chips 367 · 35g · 36g · 8g (avg).
   - Under the grid, the **Butcher's Pick** note: "Don't want to choose? Do nothing. If your box hasn't changed by Sunday night, we send the Butcher's Pick for your plan, with flavours rotating through Greek Lemon, Korean BBQ, Arabic 7 Spice, Teriyaki, BBQ and Jerk."
7. **Plan builder** (opens in place under the plans when a plan is chosen; H2 "Build your [Plan] box"):
   - Step A, size: 10 · 14 · 20 · 28 · 40 meals.
   - Step B, rhythm: Every week · Every 2 weeks · Monthly Freezer Fill.
   - Step C, meals: pre-filled with the Butcher's Pick (the plan's 6 meals cycled to the size). Each row has a photo, name, parts with real prices, est. macros, a −/+ qty control and a "Swap" button that opens a sheet with the other meals in the plan (and, for component plates, other chicken flavours at their real prices: Greek Lemon $4.99, Korean BBQ $4.99, Teriyaki $4.60, Arabic 7 Spice $4.50, BBQ $4.20).
   - Step D, add-ons: "Breakfast 5-pack $24.55" · "Extra Chicken Breast Souvlaki 6oz $6.93".
   - **Sticky bag:**
     - "14 of 14 meals chosen"
     - a **freezer-bag stack** visual (one kraft rectangle per meal, filling as meals are added)
     - avg est. macros per meal
     - one-off subtotal and the "Subscribe & Save 10%" saving in green
     - "Price per meal"
     - "Route fees a month: 2 × $20" (changes with the rhythm)
     - nudge: if after-discount total < $100 and delivery is chosen, "Add $X (e.g. the Breakfast 5-pack) to reach the $100 route minimum, or pick up for free"
     - "Smart-fill my box" button (resets to Butcher's Pick)
     - primary button "Start my plan"
8. **Freezer Fill band** (kraft-cream with tan bag illustrations):
   - H2 "Fill the freezer once a month."
   - Body: "Every Meal Butler meal is cooked, weighed, portioned and flash-frozen in a vacuum-sealed bag. So you can take a month at once: one delivery, one route fee, one Sunday reminder. Fresh-only services can't stretch that far."
   - Stat pair: "Weekly box: 4 route fees a month ($80 on the Wednesday route)" vs "Freezer Fill: 1 ($20)".
   - Example: "Lean Freezer Fill, 20 meals: $197.98 a month with Subscribe & Save ($9.90 a meal)."
   - Button "Make mine monthly".
9. **Household band:**
   - H2 "One box. Everyone's goals."
   - Body: "Add each person in your home, pick their plan, and we pack it all in one box with name tags on the packing list. One delivery, one fee."
   - Example card: "Alex · Lean Bulk · 10 meals / Sam · GLP-1 Companion · 10 small meals / Kids · 6 plates. $233.60 every 2 weeks with Subscribe & Save."
   - Button "Build a household box".
10. **My Plan** (demo portal, slate-purple header; shows sample subscriber "Alex" until the visitor places a plan order, then switches to theirs):
    - Next box: "[Plan] · [N] meals · [route day], [date] · [route name]", with the countdown "Changes close Sunday 11:59 pm".
    - Box contents with "Swap" buttons.
    - Buttons: "Skip this delivery" · "Pause (1–8 weeks)" · "Change rhythm" · "Change plan" · "Cancel plan".
    - Credits line: "$25 switch credit applied automatically · 312 Smile.io points".
    - SMS preview (phone-bubble style; label "Saturday reminder, drafted by the Subscription & Reorder Agent"): "J&W Meal Butler: Hi Alex, your Lean Bulk box (10 meals, $150.18 with delivery) rides Wednesday. Reply OK, SKIP or SWAP by Sunday night. Reply STOP to opt out."
11. **Trust panel** (dark rounded #0E1B4D, white text):
    - H2 "Butchers first. Since 1995."
    - Body: "J&W started as a family butcher and distributor in 1995 and became an Ontario-inspected meat plant in 2008. We cut, cook, portion and freeze every Meal Butler meal ourselves."
    - Tiles: "4.8 on Google from 611 reviews" · "30K on Instagram" · "Ontario chicken, air-chilled, no hormones or antibiotics" · "Salt and sugar free, no added oils".
    - "What customers mention most (themes from public Google and Yelp reviews): hands-on advice at the counter · meat quality · no-oil, boil-in-bag convenience." No invented quotes.
12. **FAQ** (accordion):
    - "Are the macros exact?" "Not yet. They're estimates from standard nutrition data until our panels are checked by a nutrition professional. We'll mark verified meals."
    - "When can I change my box?" "Any time before Sunday night for the next week's route. After that, your box is being cooked."
    - "Can I skip or pause?" "Yes. Skip any delivery or pause for 1 to 8 weeks from My Plan. Skipped weeks are never charged."
    - "How do I store and heat the meals?" "Keep them frozen and follow the date and heating steps on each bag."
    - "Do you deliver to me?" "We run weekly routes Tuesday to Friday across the GTA and some of Ontario for $20 to $35, with a $100 minimum. Pickup at Brimley Rd is free."
    - "Is the GLP-1 Companion medical advice?" "No. It's smaller, protein-first meals. Follow your prescriber's advice."
    - "Can I cancel?" "Yes, from My Plan, before the Sunday cut-off, with no fee."
13. **Footer** line: "J&W Foods · Meal Butler · 2201 Brimley Rd, Unit 1, Scarborough · (416) 298-1350 · Mon–Fri 9–6, Sat 10–4". Plans, prices per meal, the Breakfast 5-pack, the switch credit and the 6-Week Reset carry an amber "Concept" tag.

### 9.4 Customer flows (each clickable end to end)
1. **Quiz to subscription.** Find my plan → Q1 "Build muscle" → Q2 "3–4" → Q3 "Just me" → Q4 "5" → Q5 "Every 2 weeks" → Q6 none → Q7 "Goodfood" → Q8 "Toronto" (shows Wednesday GTA 2, $20) → result "Lean Bulk, 10 meals every 2 weeks, $130.18" → "Subscribe & Save" → builder pre-filled with Butcher's Pick → "Start my plan" → `JWC.checkout({ title:'Start your Lean Bulk plan', items, subscription:{label:'Every 2 weeks · Lean Bulk plan', discountPct:10}, extraRows:[{label:'Switch credit, first box', amount:-25}], city:'Toronto', onPlaced })` → demo confirmation → My Plan now shows this plan with the next Wednesday date.
2. **Browse and build.** "See the six plans" → Protein & Greens "Build this plan" → size 14 → "Every week" → swap "Haddock & asparagus" for a second "Salmon & asparagus" → add the Breakfast 5-pack → "Start my plan" → `JWC.checkout` with `subscription:{label:'Every week · Protein & Greens', discountPct:10}` → confirmation.
3. **Household box.** "Build a household box" → Person 1 "Alex", Lean Bulk, 10 → "Add a person" → "Sam", GLP-1 Companion, 10 → "Add kids' plates" (3 meatball, 3 tenders) → the bag shows three name-tagged groups and $233.60 every 2 weeks → items are added with `note:'Alex · Lean Bulk'` etc. → `JWC.checkout({ subscription:{label:'Every 2 weeks · Household box', discountPct:10} })` → confirmation lists the name tags.
4. **Monthly Freezer Fill.** In the builder, flip the rhythm to "Monthly Freezer Fill" → the box size jumps to 20, the bag stack grows, and "Route fees a month" changes to 1 × $20 → pick Barrie (Friday long route, $35) → `JWC.checkout({ subscription:{label:'Monthly Freezer Fill · Lean', discountPct:10}, city:'Barrie' })` → confirmation.
5. **6-Week Reset.** Result card → "6-Week Reset" → summary sheet "Lean Bulk, 10 meals × 6 weekly boxes" → `JWC.checkout({ title:'6-Week Reset (prepaid)', items:[{id:'concept-reset-lean-bulk', name:'6-Week Reset: Lean Bulk, 10 meals × 6 weekly boxes (Concept)', price:144.65, qty:6}], extraRows:[{label:'Prepaid saving (12%)', amount:-104.15}], note:'Route fee applies to each of the 6 deliveries; the demo shows one.' })` → confirmation.
6. **Manage my plan.** My Plan → "Skip this delivery" → toast "Skipped. Your next box is [date + cadence]" and the date updates → "Swap" on a meal → choose another → toast → "Pause" → choose 2 weeks → status "Paused until [date]" → "Resume".
7. **Cancel with a save offer.** My Plan → "Cancel plan" → modal "Before you go, would one of these help?" with: "Skip the next 2 boxes" · "Switch to a monthly Freezer Fill (saves 3 route fees a month)" · "Make my box smaller (14 → 10 meals)" · a text link "Cancel anyway" → pick "Switch to monthly" → confirmation "Done. Your plan is now a monthly Freezer Fill. Next box: [date]." → `JWC.toast`. "Cancel anyway" shows "Cancelled. No fee. Your points stay." All of it is a demo, with nothing sent.

### 9.5 JW team view (`data-team`)
Header: "Sample week: Mar 22, 2027 (month 5 of the plan)". Label all data "Sample data, for illustration".

1. **KPI tiles:**
   - Active subscribers **145** (+12 this week)
   - Quiz completions this week **214**
   - Quiz → plan order **7.4%**
   - Took Subscribe & Save **63%**
   - Monthly churn **8.6%**
   - Skips this week **9 of 74 (12%)**
   - Avg box after discount **$127.40**
   - Boxes this week **70** (65 subscription + 5 one-off)
   - Revenue this week **$8,918**
2. **Plan mix table** (plan · active · avg box · boxes this week · est. gross profit/week at 40%):
   - Lean · 40 · $112 · 19 · $851
   - Lean Bulk · 32 · $139 · 15 · $834
   - Athlete · 14 · $121 · 6 · $290
   - Protein & Greens · 15 · $134 · 7 · $375
   - GLP-1 Companion · 24 · $104 · 11 · $458
   - Busy Family · 20 · $171 · 7 · $479
   - Total · 145 · · 65 · $3,287
3. **Quiz insights (switch intelligence):**
   - Goals this week: Lose fat 38% · Build muscle 27% · Family 12% · GLP-1 11% · Fewer starches 7% · Train hard 5%.
   - Switching from: Goodfood 19 · Factor 11 · LiveFit 7 · Another service 14.
   - Drop-off: 48 people stopped at Q6.
4. **Monday prep sheet** (drafted by the Production Forecast Agent after the Sunday cut-off; columns SKU · variant · portions · from plans):
   - Chicken Breast Souvlaki 6oz · 96 · Lean Bulk, Athlete, Protein & Greens
   - Teriyaki Chicken, Green Beans & Rice pre-set 4oz · 72
   - Tenders, Broccoli & Sweet Potato pre-set 4oz · 61
   - Salmon Fillet 4oz/6oz · 58
   - Jerk Chicken Breast 6oz · 52
   - Roasted Turkey Breast 4oz/6oz · 49
   - Chicken Chili 10oz · 46
   - Arabic 7 Spice Chicken 4oz · 44
   - Turkey, Spinach & Rice pre-set 4oz · 38
   - Lemon Chicken Rice Soup 10oz · 34
   - Salmon, Brussels & Quinoa pre-set 6oz · 34
   - Flank Steak, Green Beans & Potato pre-set 6oz · 30
   - Beef Meatballs 4oz · 30
   - Ground Top Sirloin 6oz · 28
   - Egg White Bites · 62
   - Steel Cut Oats · 30
   - Broccoli 4oz · 210
   - White Basmati 6oz · 80
   - Quinoa 3oz · 70
   - Cauliflower Rice 4oz · 50
   - Button "Approve prep sheet" → toast "Sent to the kitchen tablet".
5. **Route impact** (boxes by route day):
   - Tue GTA 1: 11
   - Wed GTA 2: 24
   - Thu GTA 3: 8
   - Fri GTA 4: 15
   - Fri long-haul: 3 (Freezer Fills)
   - Pickup: 9
   - Note: "Route fees collected $1,321. Owned-route cost est. $8–14 a stop, so fees cover the extra stops. No new route days needed."
6. **Approvals queue** (AI drafts; each with Approve / Edit buttons that update status and toast):
   - Butcher's Pick Menu Agent: "Week of Mar 29: Lean box swaps the Tilapia pre-set for the Haddock plate (tilapia 2 cases below par). Margin +$0.40 a box."
   - Subscription & Reorder Agent: "Saturday 10 am reminder to 136 active subscribers" (shows the SMS text).
   - Subscription & Reorder Agent, 3 save offers:
     - "Priya K., travelling → 3-week pause"
     - "Marco D., too much food → 10-meal box"
     - "Jen L., price → monthly Freezer Fill (saves 3 route fees)"
   - Lifecycle Marketing Agent: "Quiz-abandon email to 48 people, subject 'Your Lean Bulk plan is saved'".
   - Lifecycle Marketing Agent, flagged amber: "GLP-1 welcome email contains health wording. Owner and labelling review needed."
   - Nutrition Data Agent: "Macro sign-off: 9 of 31 plan SKUs verified. Next: 6 salmon and turkey meals with the nutritionist Friday."
   - Review & Reputation Agent: "2 reply drafts for new Google reviews (5 stars, 4 stars)".
7. **Subscriber table** (sample; columns name · plan · size · rhythm · route · next box · status · spend to date):
   - Alex M. · Lean Bulk · 10 · every 2 weeks · Toronto, Wed · Mar 31 · Active · $520.72
   - Priya K. · GLP-1 Companion · 14 · weekly · Markham, Fri · Apr 23 · Paused · $613.56
   - Osei household · Household box · 26 · every 2 weeks · Ajax, Tue · Mar 30 · Active · $934.40
   - Jen L. · Protein & Greens · 28 · monthly · Barrie, Fri · Apr 9 · At risk (price) · $267.58
   - Marco D. · Athlete · 14 · weekly · Mississauga, Wed · Mar 31 · Cancel requested · $750.35
   - Sarah T. · Lean · 14 · every 2 weeks · Pickup · Apr 6 · Skipped this week · $418.44
   - Plus live rows from `JWC.orders()` filtered to `proto === 1`, under the heading "New this session", refreshed on `jwc:order`.
8. **Retention panel** (bars, target vs benchmark): M1 92% (meal kits 78–88%) · M3 72% (40–55%) · M6 58% (28–42%) · M12 45% (15–28%). Source line: "Benchmarks: Eightx 2026".

`teamNote`: "The JW team sees subscribers, Monday's prep sheet, route impact, and AI drafts (menus, reminders, save offers) waiting for approval."

### 9.6 Chat ("Ask the Butler")
- **Greeting:** "Hi, I'm the Butler. I can help you pick a plan, explain Subscribe & Save, or skip a week. What's your goal?"
- **Suggestions:** "Which plan fits me?" · "How do skip and pause work?" · "I'm on a GLP-1 medicine" · "Can my family share one box?" · "What does a Freezer Fill cost?"
- **Rules** (regex, case-insensitive → reply):
  1. `skip|pause|holiday|vacation|away` → "Skip any delivery or pause for 1 to 8 weeks from My Plan, any time before Sunday night. Skipped weeks are never charged."
  2. `cancel|stop my plan|unsubscribe` → "You can cancel from My Plan with no fee before the Sunday cut-off. If it's too much food or too much money, a smaller box or a monthly Freezer Fill might fit better."
  3. `glp|ozempic|wegovy|semaglutide|mounjaro|tirzepatide|zepbound` → "The GLP-1 Companion plan has smaller 3–4oz protein portions with fibre-rich sides like quinoa and Brussels sprouts: about 270 kcal and 27g protein a meal (est.). 14 small meals are $102.26 with Subscribe & Save. It's food, not medical advice, so follow your prescriber's guidance."
  4. `which plan|best plan|recommend|lose weight|fat loss|bulk|muscle|gain` → "The quiz above takes about a minute. Quick guide (est. per meal): Lean 337 kcal / 37g protein, Lean Bulk 523 / 54g, Athlete 476 / 44g, Protein & Greens 301 / 46g with about 12g carbs, GLP-1 Companion 272 / 27g, Busy Family for households."
  5. `freezer|monthly|once a month|how long|keep|frozen` → "Every Meal Butler meal is cooked, portioned and flash-frozen in a vacuum-sealed bag, so a monthly Freezer Fill works: one delivery and one route fee a month. Keep the bags frozen and follow the date on each. A Lean Freezer Fill of 20 meals is $197.98 with Subscribe & Save."
  6. `family|kids|household|partner|wife|husband|share` → "A household box puts everyone's plan in one delivery with name tags on the packing list. Example: Lean Bulk for one adult, GLP-1 Companion for another, plus 6 kids' plates, $233.60 every 2 weeks with Subscribe & Save."
  7. `switch|goodfood|factor|livefit|power kitchen|hellofresh|other service` → "Welcome. Tell the quiz which service you used and we'll take $25 off your first subscribed box (concept offer). Plan meals here run $7.30 to $13.02 with Subscribe & Save."
  8. `price|cost|how much|per meal|cheap|expensive` → "With 10% Subscribe & Save, plan meals are $7.30 to $13.02 each (est. from our current prices). Most boxes run about $100 to $260, depending on plan and size. Route delivery is $20–$35 with a $100 minimum, or free pickup at Brimley Rd."
  9. `swap|change meal|don't like|substitut|replace` → "Swap any meal for another one in your plan until Sunday night. Chicken plates can switch flavour too: Greek Lemon, Korean BBQ, Teriyaki, Arabic 7 Spice or BBQ."
  10. `butcher'?s pick|choose for me|default|don't want to choose` → "If you don't change your box by Sunday night, we send the Butcher's Pick for your plan. The kitchen rotates flavours so the weeks don't feel the same."

### 9.7 Catalog product ids to use (`JWC.product(id)`)
- Pre-set meals: `turkey-spinach-white-rice`, `tilapia-asparagus-brown-rice`, `jerk-chicken-broccoli-sweet-potato-chunks`, `chicken-broccoli-sweet-potato-fries`, `pre-set-meal-teriyaki-chicken-breast-green-beans-basmati-white`, `chicken-souvlaki-broccoli-sweet-potato-chunks`, `copy-of-chicken-broccoli-sweet-potato-fries`, `salmon-brussel-sprouts-quinoa`.
- Proteins: `chicken-breast-souvlaki`, `chicken-breast-tenders`, `jerk-chicken-breast`, `chicken-breast-souvlaki-cooked-portioned-copy` (Greek Lemon), `chicken-breast-greek-lemon-cooked-portioned-copy` (Korean BBQ), `chicken-breast-teriyaki-cooked-portion`, `chicken-breast-tenders-cooked-portioned-copy` (Arabic 7 Spice), `chicken-breast-jerk-cooked-portioned-copy` (BBQ), `turkey-breast`, `1lb-of-extra-lean-ground-sirloin`, `beef-korean-bbq-flank-steak-cooked-portioned`, `salmon`, `haddock`, `6oz-fully-cooked-meatballs`.
- Sides: `rice-white-basmati`, `rice-brown-basmati`, `quinoa`, `sweet-potato-chunks-peeled`, `cilantro-lime-basmati-rice-cooked-portioned`, `broccoli`, `green-beans`, `asparagus`, `brussel-sprouts`, `spinach-chopped`, `copy-of-teriyaki-mix-cooked-portioned` (Cauliflower Rice), `copy-of-california-mix-cooked-portioned` (Broccoli & Cauliflower), `mixed-veggies-cooked-portioned`.
- Wraps, soups and breakfast: `wrap-beef-fajitas-flank-red-peppers-onions-spices`, `wrap-beef-flank-fajitas-copy-1`, `soup-chicken-lemon-soup`, `chicken-ground-chilli`, `copy-of-feta-omelette-cups-cooked-portioned-2-pkg`, `steel-cut-oats`, `oatmeal-breakfast-bars-baked-3oz-cooked-portioned-copy`.

**Macro note for the builder:** `JWC.macros()` returns the same perUnit macros for the 4oz and 6oz variants of pre-set meals. For 6oz pre-sets, add about 100 kcal, 16g protein and 2g fat (2oz of extra protein). Or use the per-meal numbers in §2.1, which already do this.

### 9.8 Concept products (each labelled "Concept"; priced from real portion prices)

| Concept product | Price | Basis |
|---|---|---|
| Lean plan, 10 meals | $112.96 one-off · $101.66 S&S ($10.17/meal) | Sum of the 6 Lean meals cycled to 10 at jwfoods.com prices; 10% off |
| Lean Bulk plan, 10 meals | $144.65 · $130.18 ($13.02/meal) | 6oz pre-sets $15.99–$17.49 plus component plates $9.94–$14.17 |
| Athlete plan, 10 meals | $120.28 · $108.25 ($10.83/meal) | Wraps $8.99–$9.99, 6oz pre-sets, Souvlaki rice plate $10.63 |
| Protein & Greens plan, 14 meals | $148.66 · $133.79 ($9.56/meal) | 6oz proteins + Cauliflower Rice $0.96 + green veg |
| GLP-1 Companion, 14 small meals | $113.62 · $102.26 ($7.30/meal) | 3–4oz proteins, quinoa 3oz $1.95, soups $8.99–$9.99, egg bites $5.25 |
| Busy Family, 20 plates | $187.30 · $168.57 ($8.43/plate) | 4oz pre-sets plus kids' plates $4.39 and $6.09 |
| Lean Freezer Fill, 20 meals monthly | $219.98 · $197.98 ($9.90/meal) | Lean meals cycled to 20; one route fee a month |
| Household box (example) | $259.55 · $233.60 every 2 weeks | Lean Bulk 10 ($144.65) + GLP-1 Companion 10 ($83.46) + 6 kids' plates ($31.44) |
| Breakfast 5-pack | $24.55 · $22.10 | 3 Egg White Bites $5.25 + 2 Steel Cut Oats $4.40 |
| 6-Week Reset: Lean Bulk, 10 meals × 6 | $763.75 prepaid | $144.65 × 6 = $867.90, less 12%; route fee per delivery |
| Switch credit | −$25 on the first subscribed box | Concept acquisition offer, about 30% of the $85 paid CAC |

### 9.9 Build notes
- `JWC.init({ n: 1, teamNote, chat })`. Keep quiz answers, the active plan, skips and pauses in `JWC.store` (key `p1-plan`) so My Plan survives a reload. "Reset demo" clears it.
- Cut-off and next-delivery dates are computed from today: the next Sunday at 11:59 pm, then the chosen route's weekday in the following week. Use `JWC.routesFor(city)` for the day.
- The checkout passes `city` so the right route is pre-selected. Negative `extraRows` may render as "$-25.00", which is acceptable. A local formatter can show "−$25.00" in the page's own bag.
- No horizontal scroll at 375px. Tap targets 44px or more. Alt text on every image. Sky blue only as a background or border. Every macro shows "est.".

---

## Sources
- Power Kitchen homepage, quiz and live Google widget (4.7, 564): https://powerkitchen.ca/
- Power Kitchen product catalogue and prices: https://powerkitchen.ca/products.json?limit=250
- Power Kitchen collections (5% subscription discount): https://powerkitchen.ca/collections.json
- Power Kitchen how it works and FAQ (skip, pause, cut-offs): https://powerkitchen.ca/pages/how-it-works · https://powerkitchen.ca/pages/faq
- Power Kitchen shipping policy (fees, free over $180): https://powerkitchen.ca/policies/shipping-policy
- Power Kitchen quiz landing page: https://powerkitchen.ca/pages/meal-plan-offer
- Power Kitchen custom builder: https://powerkitchen.ca/pages/power-custom-meals
- Power Kitchen 6-week program: https://powerkitchen.ca/pages/six-weeks-program
- Power Kitchen one-month trial: https://powerkitchen.ca/pages/power-one-month-trial
- Power Kitchen loyalty and referrals: https://powerkitchen.ca/pages/loyalty · https://powerkitchen.ca/pages/referrals
- Power Kitchen story (family-owned, bootstrapped): https://powerkitchen.ca/pages/our-story
- Power Kitchen 2026 price guide post: https://powerkitchen.ca/blogs/blog/meal-delivery-cost-toronto-pk
- J&W Foods store and prices: https://www.jwfoods.com/ · https://www.jwfoods.com/products.json
- J&W delivery routes and cut-off: https://www.jwfoods.com/pages/home
- J&W free delivery from $200: https://www.jwfoods.com/pages/free-delivery
- J&W about us: https://www.jwfoods.com/pages/about-us
- J&W Google 4.8 from 611 reviews (aggregator): https://yably.ca/reviews/toronto/j-w-foods-2201-brimley-road
- J&W Instagram (30K): https://www.instagram.com/jwfoods/
- Subscription churn and cohort benchmarks: https://www.eightx.co/blog/average-subscription-churn-rate-by-category
- Subscription vs one-time AOV, subscribe-and-save norms: https://eightx.co/blog/average-ecommerce-aov-subscription-vs-onetime-2026
- Recharge subscriber trends (F&B subscriber worth 3+ non-subscribers): https://www.prnewswire.com/news-releases/recharge-subscriber-trends-insights-report-highlights-the-growing-value-of-subscribers-to-ecommerce-brands-302250623.html
- Meta ads CPA benchmarks: https://www.triplewhale.com/blog/facebook-ads-benchmarks
- Klaviyo email benchmarks: https://www.klaviyo.com/products/email-marketing/benchmarks
- Delivery driver wages, Toronto: https://www.jobbank.gc.ca/marketreport/wages-occupation/21667/ON
- Goodfood Q2 FY2026 loss (displaced customers): https://retail-insider.com/retail-insider/2026/04/goodfood-market-reports-7-million-net-loss-in-q2/
- Goodfood gross margin benchmark (41.7%): https://cdn.makegoodfood.ca/images/investors/docs/2025/q4/Goodfood_Q4_FY25_Earnings_Press_Release_en.pdf
- Internal: research/competitor-01.md, selection.json, jw-facts.md, jw-audit.md, model-assumptions.md, market-benchmarks.md, competitors-gta-mealprep.md, ai-agents-research.md, site/assets/catalog.js

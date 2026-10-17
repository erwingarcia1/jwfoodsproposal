# Competitor #2: Icon Meals (Wholesale program), Dallas, Texas, USA

Checked October 16, 2026. All prices are in USD unless marked C$. Conversion uses **1 USD = C$1.4196**, the Bank of Canada rate for 2026-10-15 cited in market-benchmarks.md.

Method:
- Direct fetches of iconmeals.com: home, /pages/wholesale, /pages/how-it-works, /collections/bulk-items, product pages, `/products.json` and `/products/<handle>.js`.
- The built-in browser, used to read the JS-rendered meal builder and to view the layout.
- Trustpilot, LinkedIn, Instagram, UFC.com and Garage Gym Reviews.
- Limitation: the shared web-search budget ran out partway through. I could not run news searches for 2026 coverage, such as funding, layoffs or ownership changes. The operating status rests on Icon's own live store data plus third-party review and social activity.

## 1. Verdict: operating? premium?

**Operating in October 2026: YES.**
- The Shopify catalogue was updated 2026-10-16 (`updated_at` in /products.json). New products were published 2026-08-18 and 2026-09-04. The footer reads "© 2026 ICON Meals".
- The newest Trustpilot review is dated Oct 2, 2026 and describes a live order ([Trustpilot](https://www.trustpilot.com/review/iconmeals.com)).
- The latest Instagram post is dated Jul 21, 2026. The account has 157K followers ([Instagram](https://www.instagram.com/iconmeals/)).
- LinkedIn shows posts from about 2 months ago. About 4 months ago Icon posted a **DoorDash launch of 10 meals in select cities**. LinkedIn gives 51-200 employees, an HQ in Farmers Branch TX and a founding year of 2014 ([LinkedIn](https://www.linkedin.com/company/icon-meals-official/)).

**Premium: mixed.** Say this plainly in the proposal.
- **Premium by positioning and price.** Icon shows logos for UFC, the U.S. Olympic Team, the Dallas Cowboys, USN, USA Triathlon and Absolute Recomp under "The Official Meal Delivery Service for these brands" ([wholesale page](https://iconmeals.com/pages/wholesale)). UFC took an equity stake on Sep 28, 2021, saying Icon "has grown at an annualized rate of 56% since its founding in 2014" ([UFC.com](https://www.ufc.com/news/ufc-announces-major-partnership-icon-meals)). Signature meals cost US$12.20-19.20, about C$17-27.
- **Not premium in current execution.**
  - Trustpilot gives a **TrustScore of 1.7/5 from 980 reviews**. The all-time distribution is still 83% five-star. But the **five most recent reviews, from May 13 to Oct 2, 2026, are all 1-star**. They cite weeks of shipping backlogs, food arriving thawed despite dry ice, unreachable phone support, a cancelled order that shipped anyway, and nutrition labels that did not match. The company "hasn't replied to negative reviews" ([Trustpilot](https://www.trustpilot.com/review/iconmeals.com?sort=recency)).
  - Both blog feeds stopped in **February 2026**: /blogs/ai-optimized was last updated 2026-02-07 and /blogs/news on 2026-02-24 (`.atom` feeds).
  - We did not independently confirm that the UFC, Olympic and Cowboys deals are still active in 2026. They appear only as logos.
- **The wholesale program is thin online.** All three "Apply Now" buttons on /pages/wholesale link to `https://iconmeals.com`, the homepage. There is **no application form**, no tiered price list, no FAQ and no contact address other than info@iconmeals.com. "Wholesale Login" (myaccount.iconmeals.com) is the standard **Shopify customer-accounts login**: it redirects to a Shopify `customer-account-api` OAuth flow. It is not a bespoke portal. This is observed in page source and redirects.

**What this means for the pick:** Icon is a good **positioning** reference. It proves that a cooked-meal plant with in-house butchery can be sold to gyms, clinics, offices and pro teams. It is a **poor mechanics reference**, because its B2B funnel is broken. J&W can beat it by building the funnel properly. Do not present Icon as a model of service excellence.

## 2. Scale signals

| Signal | Value | Source |
|---|---|---|
| Revenue | "over $14 million in 2023" (third-party, unaudited) | [Garage Gym Reviews](https://www.garagegymreviews.com/icon-meals-review) (updated May 13, 2026) |
| Employees | 75 (GGR). LinkedIn: 51-200 band, 15 on LinkedIn | GGR; [LinkedIn](https://www.linkedin.com/company/icon-meals-official/) |
| Founded | 2014 (UFC, LinkedIn). GGR says 2012, which conflicts | UFC.com; LinkedIn; GGR |
| Growth | 56% annualised since 2014 (as of 2021) | [UFC.com](https://www.ufc.com/news/ufc-announces-major-partnership-icon-meals) |
| Meals sold | "Over 12 million meals sold" (company claim, hero badge) | [iconmeals.com](https://iconmeals.com/) |
| Wholesale partners | "thousands across the United States", orders from "a few dozen meals to weekly shipments of thousands" (company claim) | [wholesale](https://iconmeals.com/pages/wholesale) |
| Funding | US$7.09M raised (CB Insights, via competitors-global.md); UFC equity, undisclosed | competitors-global.md; UFC.com |
| Reviews | Trustpilot 1.7/5, 980 reviews; GGR says "nearly 1,000 Trustpilot reviews at 4.5 stars", which is now out of date | Trustpilot; GGR |
| Social | Instagram 157K; LinkedIn 496 followers | Instagram; LinkedIn |
| Catalogue | 188 Shopify products: 41 signature meals, 16 bulk/a-la-carte items, 6 meal plans, 74 hidden builder-option products, snacks and seasonings | iconmeals.com/products.json |
| Tech stack (page source) | Shopify, Recharge (subscriptions), Bold (product options/bundles), Klaviyo, Yotpo, Searchanise | home page HTML |

## 3. Real prices (USD, with C$ at 1.4196)

**Signature meals** (8 oz / 227 g per tray, from Shopify variant weight):
- 25 priced meals run **US$12.20-19.20**, median **$13.40**. That is about C$17.32-27.26, median C$19.02.
- Examples: Baja Pulled Chicken Bowl $12.40 (300 cal / 31g protein); Diced Chicken, Rice & Green Beans $13.00; Salmon, Saffron Rice & Green Beans $15.60; Double Protein Saffron Rice $19.20.

**Meal plans** (12 or 18 meals; the 24-meal plan mentioned in older reviews is no longer offered):

| Plan | 12 meals | 18 meals |
|---|---|---|
| ICON Meal Plan | $144 ($12.00/meal) | $209 ($11.61/meal) |
| Keto / Get Lean | $138 ($11.50/meal) | $205 ($11.39/meal) |
| Extreme Protein | $169 ($14.09/meal) | $249 ($13.83/meal) |

- **Subscribe & Save is 5%**, every 1, 2, 3 or 4 weeks (Recharge selling plans in `/products/icon-meal-plan.js`).
- Build Your Own plan: 12 or 18 meals, every 1 or 2 weeks, **0% subscription discount**.

**Bulk "by the pound" cooked items** (/collections/bulk-items, 16 items):
- The page shows **no unit label**. The unit is inferred from handles such as `chicken-by-pound` and the Shopify weight (454 g = 1 lb for chicken and brisket; 227 g for the others).
- Prices: Chicken Breast $15.20 (≈ C$21.58/lb); Chicken Thighs $14.80; Ground Turkey $14.80; Ground Beef $19.20; Roasted Turkey Breast $18.20; Brisket $23.80; Cod $23.60; Shrimp $20.80; Salmon $27.60; Steak $27.80; Saffron Rice $12.00; Red Potatoes $12.60; Sweet Potatoes $13.20; Kyoto Veg $13.40.
- There are **no bulk quantity tiers**.

**Custom meal builder:**
- Base price **$6.00**, which "updates as you choose".
- Protein is priced by the ounce, 3-8 oz. Chicken breast adds $2.40-$6.40 (**$0.80/oz**, read live in the builder). Salmon is $1.10-1.74/oz, steak $1.60/oz and ground bison $1.32/oz.
- Sides: white rice $1.48 per cup; broccoli $0.21/oz; green beans $0.30/oz.
- Optional seasoning add-on: +$9.99.
- Example: 6 oz chicken + 1 cup white rice + 4 oz broccoli = **US$13.12 ≈ C$18.63**.

**Other:**
- Minimum of 8 meals per shipment. This applies to **all** orders, not only wholesale, and is waived for pickup and "select local partners". Ships frozen on dry ice nationwide. Shipping fee: not found.
- 10% off the next order for signing up. 15% off for military and first responders.
- Gift cards $10-$500, delivered by email.
- Protein popcorn and seasonings $9.99. Protein coffee $35.
- **Wholesale price list: not published.** There is a hidden $0 "Wholesale Payment" product tagged Accounting, which suggests B2B invoices are paid through the Shopify checkout.

**J&W comparison (C$):**
- Cooked chicken breast: J&W charges $4.18-4.99 per 4 oz and $6.27-6.30 per 6 oz, which is **C$16.72-19.96/lb**. Icon charges C$21.58/lb.
- A comparable custom bowl: J&W 6 oz jerk chicken $6.30 + 6 oz basmati $2.31 + broccoli $1.39 ≈ **C$10.00**. Icon's is C$18.63, so J&W is **about 46% cheaper**.
- Pre-set meals: J&W Jerk Chicken + Green Beans + Sweet Potato is $12.99 (4 oz) or $14.99 (6 oz). Icon Diced Chicken, Rice & Green Beans is C$18.45.

## 4. Flows worth borrowing (step by step)

1. **Wholesale landing** (/pages/wholesale), in this order:
   - Hero: "Let's Start an Iconic Partnership", with the subtitle "Heat & Eat Meals, Protein Snacks, More" and an Apply button.
   - "Why Choose" strip with three icons: Made To Order / Functional Foods / Health & Fitness Focused.
   - **Partner logo wall**.
   - Three red product-category tiles: Heat & Eat Meals / Protein Snacks / Sauces & Seasonings.
   - **Segment list**: store, gym, weight-loss clinic, training center, office, employee-benefit meal programs. This sits next to a collage of partner-staff photos and repeats the apply CTA.
   - "The ICON Meals Difference": a USDA facility and in-house meat processing (cooking its own ground turkey, hand-trimming brisket), in a white card over a full-bleed food photo.
   - Functional-foods upsell with a third CTA.
   - A "Latest Arrivals" product grid with macros and quantity steppers.
   - **Borrow** the order: proof → segments → plant story → product grid. **Fix** the dead Apply button.
2. **Custom meal builder** (/products/custom-meals):
   - Pick a protein from 11 options.
   - Pick a portion from 3-8 oz using round "bubble" buttons, each showing its price.
   - Pick Side 1 and Side 2 from 13 options, each with a portion choice.
   - Optionally add a seasoning.
   - Set the quantity, then Add. The price updates live and a sticky "Review Your Order" cart sits on the right.
   - A two-step header progress bar reads "1 Choose Meals → 2 Review Cart".
   - J&W already sells these components à la carte (chicken 3/4/6 oz, rice 3/4/6 oz, sweet potato 4/6 oz), so it can build this directly.
3. **Meal plan purchase:**
   - Choose 12 or 18 meals, with the per-meal price shown in the variant label.
   - Choose One-Time or Subscribe & Save, then a delivery frequency of 1-4 weeks.
   - Add to cart. The cart drawer enforces the 8-meal minimum, with options to "Continue Shopping" or "Checkout Anyway".
4. **Audience router on the homepage:** "Who is ICON Meals For?" offers four cards, each with its own CTA:
   - "I'm Too Busy" → menu.
   - "Macro Pros" → custom meals.
   - "GLP-1 Users".
   - "Fast Food Breakups".
5. **Shop by Goal:** Clean Variety / Build Muscle / KETO / Get Lean, each mapped to a plan.
6. **GEO/AI-search content:** /blogs/ai-optimized has question-titled posts answering things like "Best ICON Meals for GLP-1 users" and "How long do meal-prep meals last?", and the footer links it as an "AI Knowledge Base". The feed has been dormant since Feb 2026.
7. **Cart-share link:** the "Share Cart" button and the "You have great friends... building your cart now!" loader mean a coach can send a pre-filled cart link. This is useful for trainer and partner referrals.

## 5. Site design brief (for a J&W prototype *inspired by* it; do not copy)

- **Layout:**
  - White sticky header: logo on the left, four uppercase nav items with chevrons in the middle, and account and cart icons on the right.
  - Full-bleed hero photo with a dark overlay. The headline is left-aligned, white, uppercase and about 56-64px. Two pill buttons sit below it: one solid red, one white-outline.
  - Sections alternate between a light-grey canvas and a **black full-width band**, the latter holding the audience cards in white rounded cards with a portrait photo on top.
  - The wholesale page is centred and single-column, with a partner-logo row in brand colours, three rounded red tiles holding product cut-outs, and a white text card over full-bleed food photography.
  - Product cards are white with rounded corners and soft shadows. Each shows a square tray photo, the name in bold, diet tags, the price, a macro strip (Cals / Pro / Carbs / Fat) and a −/+ stepper.
- **Palette** (from CSS variables):

  | Role | Hex |
  |---|---|
  | Accent / CTA / links | `#ec4242` |
  | Nav hover | `#d42828` |
  | Page background | `#f5f5f5` |
  | Cards / header | `#ffffff` |
  | Body text | `#333333` |
  | Headings / dark bands | `#000000` / `#1a1a1a` |
  | Footer | `#252525` |
  | Muted links / dots | `#a5a5a5` |
  | Borders | `#E5E7EB` |

  Button hover turns black (`#000000`) with `#f5f5f5` text.
- **Typography:**
  - **Jost** (a geometric sans) throughout, 16px base.
  - Headers are uppercase, weight 500, with wide letter-spacing (40px section heads).
  - Buttons use 14px uppercase tracked text.
- **Photography:**
  - Overhead and three-quarter shots of black meal-prep trays with saturated, glossy food on light marble or grey.
  - Lifestyle portraits of real customers: a busy professional at a laptop, a fitness couple.
  - Team and partner photos (cheer squad, staff holding trays).
  - Product cut-outs on red tiles.
- **Tone of voice:**
  - Punchy, gym-adjacent and slightly cheeky. The hero plays on "clean eating, but consistent", and audience cards carry names like "Fast Food Breakups".
  - Heavy use of "ICON/Iconic" wordplay and confident claims ("Official Meal Delivery Service").
- **J&W adaptation idea:**
  - Keep the structure (proof wall → segments → plant story → shoppable grid with macros) but use J&W's own palette and voice: the family butcher since 1995, the Ontario-inspected plant, no added salt, sugar or oil.
  - Replace the red/black with J&W brand colours.
  - Use real J&W plant and butcher photography in place of stock lifestyle shots.

## 6. What J&W already does better

1. **Regulated plant plus butchery heritage, with proof.** J&W has been an Ontario-inspected plant since 2008 and is a family butcher dating to 1995. The family's wholesale roots go back to Advance Food Products (1973). It holds a 2026 federal chicken TRQ processor quota ([GAC list](https://www.international.gc.ca/trade-commerce/controls-controles/chicken-poulet/wto_processor-2026-omc_transformateurs.aspx?lang=eng)). Icon says "USDA-certified", but its own how-it-works page describes a "HACCP-certified kitchen" that passes state inspections.
2. **Price.** J&W's cooked chicken is C$16.72-19.96/lb against Icon's C$21.58/lb. A comparable custom bowl costs about C$10 at J&W and C$18.63 at Icon. Pre-set meals run C$8.99-14.99 at J&W, against Icon's C$17.32-27.26.
3. **Cleaner recipe claim.** All J&W Meal Butler items are salt- and sugar-free with no added oils. Icon's meals include mac & cheese, ravioli, sliders and $9.99 flavoured seasonings.
4. **True à-la-carte cooked portions by the ounce and by the case.** Examples: chicken 3/4/6 oz, 4 kg chicken cases at $85-$100, burgers in 25-packs at $35.50. Icon's "bulk" has no case tiers.
5. **Local, owned delivery, so food arrives frozen and on time.** J&W runs weekly GTA routes (GTA 1-4, $20-$35) plus free pickup. Icon's 2026 reviews centre on dry-ice shipments arriving thawed and weeks late.
6. **Reputation.** J&W has 4.8★ from 611 Google reviews (model-assumptions.md) against Icon's 1.7 TrustScore and unanswered negative reviews.
7. **Full butcher range for partners.** J&W carries raw AAA and Wagyu beef, Ontario lamb, a quarter cow ($1,200) and Greek/Mediterranean grocery. A gym or clinic partner can stock cooked meals and raw bulk protein from one supplier.
8. **B2B funnel opportunity.** Icon's Apply buttons go nowhere. A J&W portal with a working application, tiered case pricing, net terms and standing route orders would be a better B2B experience than the global reference.

## 7. Corrections to the selection brief

- The selection says Icon has "a separate wholesale login". The **wholesale login is Shopify's standard customer-account login**, and the "Apply Now" CTAs **link to the homepage**: there is no application form or published wholesale pricing.
- The **8-meal minimum is a site-wide shipping minimum** for all customers, waived for pickup and "select local partners". It is not a wholesale-specific term.
- "100% USDA-certified facility" is a company claim on the wholesale page. The how-it-works page says "HACCP-certified kitchen … pass state inspections daily".
- The partner logos (UFC, U.S. Olympic Team, Dallas Cowboys, USN, USA Triathlon, Absolute Recomp) are company claims. Only the UFC deal (2021) is independently sourced, and its 2026 status is not verified.
- competitors-global.md lists a "24-meal plan about $11". The current site offers only 12- and 18-meal plans: $138-169 and $205-249. Subscribe & Save is 5% (0% on Build Your Own).
- GGR's "4.5 stars on nearly 1,000 Trustpilot reviews" is out of date. Trustpilot now shows a 1.7 TrustScore on 980 reviews, and every review from May to Oct 2026 is 1-star.
- Founding year conflicts: 2014 per UFC and LinkedIn, 2012 per GGR.

## Sources
- https://iconmeals.com/ (home)
- https://iconmeals.com/pages/wholesale
- https://iconmeals.com/pages/how-it-works
- https://iconmeals.com/collections/bulk-items
- https://iconmeals.com/products/custom-meals (builder, read live in the browser)
- https://iconmeals.com/products/icon-meal-plan and `.js` (selling plans)
- https://iconmeals.com/products/chicken-by-pound
- https://iconmeals.com/products.json (catalogue, update dates, weights)
- https://iconmeals.com/blogs/ai-optimized.atom ; https://iconmeals.com/blogs/news.atom
- https://myaccount.iconmeals.com/ (redirects to the Shopify customer-account OAuth)
- https://www.trustpilot.com/review/iconmeals.com
- https://www.instagram.com/iconmeals/
- https://www.linkedin.com/company/icon-meals-official/
- https://www.ufc.com/news/ufc-announces-major-partnership-icon-meals
- https://www.garagegymreviews.com/icon-meals-review
- J&W prices: /Users/erwingarcia/Claude/JWFOODSPROPOSAL/research/jw-catalog.json, jw-facts.md, model-assumptions.md; FX from market-benchmarks.md (Bank of Canada 2026-10-15)

# Competitor #7: Halenda's Meats and Halenda's Fundraising (Oshawa, Durham Region), the fundraising-channel benchmark

Prepared for Minastech (Erwin Garcia) for the J&W Foods / J&W Meal Butler proposal. Research date: **October 16, 2026.**

**Method.** I downloaded halendasfundraising.com, halendas.com and the online store (store.themeatdepot.ca) with curl and read the text. I also opened the pages in a real browser to check layout. Post dates come from each site's WordPress REST API and its `article:modified_time` meta tags. Store addresses come from the halendas.com store-locator endpoint. Online-store prices come from the WooCommerce Store API (75 products). Colours and fonts come from each site's inline CSS and theme CSS.

**Limits.**
- The web-search budget for this run was used up before I started, so I found **no third-party news, review counts or revenue data**.
- I did not check Instagram or Facebook, which require a login.
- Everything below comes from Halenda's own sites, plus J&W's catalog for the price comparisons.

---

## 1. Verdict: operating (verifiedOperating = true), premium only in part

**It is operating in October 2026.**
- The weekly sale page reads "Sale runs from Thursday, October 15th – Wednesday, October 21st, 2026" ([on-sale](https://www.halendas.com/on-sale-durham/)).
- The newest main-site post, published **Oct 6, 2026**, announces the 2026 Ontario's Finest Meat Diamond Award ([post](https://www.halendas.com/halendas-wins-2026-ontarios-finest-meat-diamond-award/)).
- On the fundraising site, the Purchase, Product and About pages were all updated **Sept 23, 2026**. New success-story posts went up **Sept 2, 2026** and **Aug 24, 2026**. The footer reads "©2026 Halenda's Meats" ([purchase](https://halendasfundraising.com/purchase/), [blog](https://halendasfundraising.com/fundraising-resources/)).

**It is premium only in part. It is a craft-quality, value-priced butcher, not a luxury one.**
- Quality signals are real:
  - It has won **three Diamond Awards**: 2017 Double Smoked Bacon, 2024 Ruby Red Bacon and 2026 Stuffed Iberico Back Bacon.
  - It has won the **Award of Excellence five times**: 2011, 2013, 2015, 2019 and 2024.
  - It runs an Iberico-style line.
  - Its charcuterie is sold in supermarkets.
- Its own positioning is price-led: "We believe in Quality, Service and Low Prices". The weekly specials include pork tenderloin at $4.99/lb and pork schnitzel at $3.99/lb.
- The fundraising arm sells one mass-market product, a pork pepperoni stick.
- So Halenda's is the right benchmark for the **channel** (fundraising and freezer packs), not for premium positioning.

## 2. Scale signals

| Signal | Figure | Source |
|---|---|---|
| Stores | **5 stores, all in Durham**, plus St Jacobs Market. Durham stores: Whitby (1916 Dundas St E), Oshawa Nelson HQ (915 Nelson St), Oshawa King (1300 King St E), Oshawa Taunton (250 Taunton Rd E) and Bowmanville (94 Waverley Rd). St Jacobs Market is at 878 Weber St N, Woolwich. | halendas.com store-locator data ([locations](https://www.halendas.com/halendas-locations/)) |
| Plants | Homepage says "6 locations and 2 processing plants". Fundraising pick-up runs from 915 Nelson St, Oshawa and **15 Brydon Dr, Etobicoke**, a new plant opened Aug 2020 that added "200%" capacity. | [home](https://www.halendas.com/), [purchase](https://halendasfundraising.com/purchase/), [new-plant post](https://halendasfundraising.com/fundraising-resources/the-advantage-of-our-new-plant-15-brydon-dr-etobicoke/) |
| Heritage | "Family-owned since 1979". Founder Michael Halenda. Claims a family tradition of 65+ years. | [about program](https://halendasfundraising.com/about-halendas-fundraising/), [fund home](https://halendasfundraising.com/) |
| Fundraising volume | First case shipped **June 27, 2013**. **6 million+ meat sticks sold** and "more than six million dollars" raised (post of Nov 6, 2025). | [6M post](https://halendasfundraising.com/fundraising-resources/celebrating-six-million-meat-sticks-sold/) |
| Implied run-rate (ESTIMATE) | 6M sticks over ~13.3 years ≈ 450K sticks a year. That is ≈ **45K bags or ≈ 1,880 cases a year**, and ≈ **$450K a year raised for groups**. At $261–$300 per case that is ≈ **$0.5M a year of wholesale revenue for Halenda's**. | My arithmetic on the figures above |
| Retail distribution | Charcuterie in "select Metro, Sobeys, Foodland, Food Basics and Fortinos". The charcuterie page itself omits Food Basics. | [locations](https://www.halendas.com/halendas-locations/), [charcuterie](https://www.halendas.com/halendas-charcuterie/) |
| Industry standing | David Hobson of Halenda's was appointed to the **2026 Meat & Poultry Ontario board** (June 2026). | [post](https://www.halendas.com/david-hobson-joins-mpo-board-of-directors/) |
| Online store | 75 SKUs on WooCommerce at store.themeatdepot.ca, "Halenda's Online Store". Curbside pickup, "aims to have your order completed in 24-48 hours". No home delivery found. | [store](https://store.themeatdepot.ca/), WooCommerce Store API |
| Group count, revenue, reviews | **Not found.** I found no group count, company revenue, Google rating or follower counts (search budget exhausted). | — |

**2026 awards.** The Diamond went to Stuffed Iberico Back Bacon.
- Platinum: Stuffed Iberico Back Bacon; Iberico Premium Koby Dog.
- Gold: Iberico BBQ Sausage; Dill Pickle Pepperoni Stick.
- Silver: Iberico Sweet Heat Dinner Sausage; Hot Honey.

That makes **six awarded products, one of which also took the Diamond**. It is not a Diamond plus six other awards ([post](https://www.halendas.com/halendas-wins-2026-ontarios-finest-meat-diamond-award/)).

## 3. Pricing (verified Oct 16, 2026)

### 3.1 Fundraising: Pepperoni Stix ([purchase](https://halendasfundraising.com/purchase/), [product](https://halendasfundraising.com/product/halendas-pepperoni-stix/), [FAQ](https://halendasfundraising.com/fundraising-faqs/))
- **One case** holds 240 sticks: 24 resealable bags of 10 sticks each (6 mild, 4 hot). The 50 g sticks have 13 g protein each and a 6-month shelf life, and need no refrigeration.
- Groups sell at **$25 a bag**, so a case brings in $600 at retail.

| Cases | Case cost | Group profit / case | % of sales kept by group |
|---|---|---|---|
| 1–7 | $300.00 | $300 | **50%** |
| 8–14 | $288.00 | $312 | 52% |
| 15–24 | $273.00 | $327 | 54% |
| 25+ | $261.00 | $339 | **56%** |

**Terms and logistics:**
- Shipping is **$18 per case** anywhere in Ontario, with no minimum. Pick-up is free at Oshawa or Etobicoke.
- No tax is charged (their claim).
- Lead time is "about 2 weeks", "up to 4 weeks" in the busy season.
- Payment is by card, cheque or e-transfer.

**Stale data on the same page** (a sign of weak data hygiene):
- A legacy PayPal block still shows **$240 a case** for 1–7 cases, $229.20 for 8–14 and $209.01 for 35–50, with "$12 per case" shipping.
- The example "15 people… can raise over $3,900" predates the current prices. On today's 15–24 tier it works out to $4,905.
- The About page still says "over $2,000,000 raised", while the Purchase page says $6,000,000.

**Real campaign results:**
- A 12-year-old BJJ athlete sold **8 cases in about a month and raised $1,536**, which is $192 a case. That points to older $20-a-bag pricing ([post, Aug 2026](https://halendasfundraising.com/fundraising-resources/youth-sports-fundraising-success-story-paige/)).
- A Newcastle dance studio raised **$10,300** ([post, Sept 2026](https://halendasfundraising.com/fundraising-resources/dance-fundraising-success-story/)).

### 3.2 "Hibernator" freezer packs ([page](https://www.halendas.com/products/meat-freezer-packs/); identical on the online store)
- **#1, $199:**
  - 4 × 8 oz butterfly pork chops
  - 2 × 16 oz sirloin
  - 4 × 8 oz striploin
  - 3 lb boneless skinless chicken breast
  - 2 lb breakfast bacon
  - 6 lb lean ground beef
  - 8 fresh sausages
  - ESTIMATE: about 19 lb in total, or about $10.50/lb.
- **#2, $299:**
  - 6 × 8 oz pork chops
  - 4 × 10 oz striploin
  - 2 × 16 oz sirloin
  - 6 pork souvlaki
  - 3 lb chicken breast
  - 2 lb bacon
  - 1 back rib
  - 4 schnitzels
  - 1 roasting chicken
  - 8 lb ground beef
  - 8 sausages
- **#3, $349:**
  - 4 × 8 oz bone-in pork chops
  - 4 × 10 oz striploin
  - 2 × 16 oz sirloin
  - 4 lb hip roast
  - 5 lb chicken legs
  - 1 jumbo roasting chicken
  - 2 lb peameal bacon
  - 6 souvlaki
  - 6 schnitzels
  - 5 lb jumbo wings
  - 8 lb ground beef
  - 8 sausages
- All packs are "custom cut, freezer wrapped and guaranteed tender". Customers order in store or online.

### 3.3 Everyday retail (store.themeatdepot.ca, Store API, Oct 16, 2026)
- **Chicken:**
  - Boneless chicken breast $7.99/lb.
  - 11 lb bag $82.39 (≈ $7.49/lb).
  - Bone-in breast $6.69/lb.
- **Beef:**
  - Lean ground beef $7.99/lb.
  - Striploin AA+ $12.49 for a 10 oz steak (reg. $16.24).
  - Sirloin $35.98 for a 32 oz steak.
  - "PRIME" T-bone $32.48.
- **Pork and smoked meats:**
  - Award-winning Kobassa $9.29/lb.
  - Double Smoked Bacon $10.99.
- **Prepared foods:**
  - Perogies $4.99.
  - Cabbage rolls $2.99.
  - Buffalo wings $11.99.
- **This week's specials (Oct 15–21, 2026):**
  - Pork souvlaki $4.99/lb (save $3).
  - Ruby Red bacon $7.49/lb.
  - *New* Iberico Stuffed Pork Loin $7.99/lb.
  - Porketta $1.99/100 g.
  - Chuck short ribs AA $14.99/lb.

**Compared with J&W** (jw-catalog.json):
- Boneless chicken breast bulk 55 lb is $350 (≈ $6.36/lb). That is **≈ 15–20% below Halenda's** $7.49–$7.99/lb.
- Ground beef bulk 5 lb is $40 ($8.00/lb), **about the same** as Halenda's $7.99/lb.
- A portioned, vacuum-packed chicken breast case is $85–$92.
- J&W sells **no meat stick of its own**. It only resells Jack Link's and Noah Martin's Costco items, and those are currently unavailable.

## 4. Flows worth borrowing (step by step)

**A. Two-way profit calculator** ([purchase](https://halendasfundraising.com/purchase/))
1. The organiser types a **number of cases** and sees the profit.
2. Or they type a **fundraising goal** in dollars and see the cases needed ("Get Estimate").
3. A tier table sits underneath (1–7, 8–14, 15–24, 25+ cases), with profit % rising from 50% to 56%.

For J&W, rebuild it as a goal → orders calculator. For example: "$2,000 goal ≈ 100 Team Packs at $20 donation each".

**B. Order and fulfil flow**
1. On "Order Now", the organiser picks a number of cases.
2. They choose delivery ($18/case) or pick-up (Oshawa or Etobicoke).
3. They pay by card, cheque or e-transfer.
4. Halenda's "contacts you just before delivery".

The legacy form also asks for **Group Name, Contact, Address, Coupon Code and a required "Sales Representative" dropdown**. That shows a rep-driven B2B sales motion with rep attribution. J&W should copy the rep and coach attribution field.

**C. Two campaign modes** ([about](https://halendasfundraising.com/about-halendas-fundraising/))
1. **"Order the Stix, then sell"** (about 95% of groups). The product is in hand, and Halenda's says that sells more.
2. **"Collect orders, then buy"** (about 5%). Halenda's emails a **personalised flyer and order form**, digital or printed, and the group orders once the money is in.

Halenda's also supplies a **custom insert flyer** to personalise the bags. For J&W, mode 2 becomes the online team page. Mode 1 is the hand-sell protein-stick SKU.

**D. School-compliance and objection handling.**
- Halenda's states that its sticks meet the Ontario school nutrition guideline range, contain no MSG, trans fats or artificial sweeteners, and use allergen-free ingredients.
- It answers objections directly: "No more melted chocolate"; no refrigeration needed; a 6-month shelf life; a "No Contact Fundraising Protocol".
- J&W needs an equivalent FAQ block before a school will say yes.

**E. Segment success stories as SEO.**
- New posts go up every few weeks, one per segment: dance, youth BJJ, hockey, sports clubs and cadets. Each gives the dollars raised and a call to action ("Start Fundraising Today!").
- Halenda's also has a **"Buy Canadian" post** that names US-owned rivals (World's Finest Chocolate, Krispy Kreme, Jack Link's, Little Caesars) ([post](https://halendasfundraising.com/fundraising-resources/support-local-fundraising-with-halendas/)).
- J&W can make a stronger "Ontario-inspected, Scarborough-made" version.

**F. Named freezer bundles plus a dated weekly sale page.**
- There are three named tiers with full item lists, orderable in store or online.
- The weekly sale page shows the sale window, "Only $X/lb – Save $Y/lb" and award badges on items.
- It ends with a "REVIEW US" button linking to Google.
- An e-flyer signup asks for postal code and "location most frequented", which segments the list by store.

## 5. Site design (for an inspired J&W prototype; ideas only, not copy)

- **Platform:** WordPress on the "Fusion" theme.
  - Fundraising site by Lure Marketing.
  - Main site by Beam Local.
  - Online store by Eyebeam Design (WooCommerce, with an Authorize.net gateway on the fundraising checkout).
  - Three separate domains with one shared look.
- **Palette (from CSS):**
  - Brand orange **#F58025**, used on primary buttons, the scroll-to-top disc and the outlined header CTA. Hover **#E2721B**.
  - Black text **#000000**.
  - Dark secondary button **#3F3F3F**.
  - Footer / dark UI **#1D1D1D** and **#32373C**.
  - The calculator panel uses a soft sky blue **#56A0D3**.
  - The rest is white.
  - The look is warm orange-on-white with charcoal: friendly and practical rather than luxe.
- **Typography:**
  - Headings H1, H2, H4 and H5 in **Raleway** (600–700), often uppercase with letterspacing in nav and section titles. Hero headlines are about 68px, centred and white.
  - H3 and H6, plus hero sub-lines, in **Playfair Display 700**, a serif accent.
  - Body in **Open Sans** 16px.
  - Small all-caps Raleway nav.
- **Layout:**
  - White utility bar with social icons on the left and an outlined orange "PURCHASE" / "What's on sale this week?" button on the right.
  - Horizontal uppercase nav with dropdowns underneath.
  - Full-bleed photo hero slider with a dark overlay and a centred white headline.
  - Centred single-column content sections, with a short orange rule as the divider and orange pill buttons.
  - The Purchase page opens on a full-width macro photo of a pile of pepperoni sticks. Next come the light-blue calculator card, a plain pricing table and a step-by-step order block.
  - On mobile, the header collapses to a centred logo and hamburger. A floating orange round scroll-to-top button sits bottom right.
- **Photography:**
  - Real product macros: sticks, cured meats on wooden boards in natural light.
  - Moody, warm-toned food shots for the main-site hero.
  - School-supply and desk imagery on the fundraising hero.
  - No lifestyle or athlete photography. There is a gap here: no kids, teams or arenas.
- **Tone of voice:**
  - Folksy, enthusiastic and exclamation-heavy. Examples: "Warning Halenda's is habit forming!", "Halenda's on the label means quality on the table", "No more melted chocolate".
  - Volunteer-practical: "less selling and less administration", "finish fundraising faster".
  - Patriotic: "Support Local, Support Canada!".
- **What J&W should do differently:**
  - Keep the clear calculator and tier table.
  - Add athlete and team photography, a live progress bar, and per-team pages.
  - Use one domain and current, consistent prices.

## 6. What J&W already does better

1. **It can capture buyer data. Halenda's cannot.** Halenda's sells cases to the *group*, and the group resells bags for cash, so supporters never become Halenda's customers. A J&W Shopify team storefront makes every supporter a J&W account with consent and Smile.io points. This is the whole reason to run fundraising as an acquisition channel.
2. **A bigger, more useful basket.**
   - Halenda's fundraises with one SKU, a $25 bag of pork sticks.
   - J&W can offer freezer packs, chicken-breast cases, chicken burgers and cooked Meal Butler week-packs. These are things families already buy weekly, so the average order is larger.
   - Example (ESTIMATE): a $120 order with a 15% donation gives $18 per order. A Halenda's bag gives $12.50.
3. **Healthier, cleaner story for sports parents.**
   - Meal Butler is "salt and sugar free, with no added oils"; chicken is air-chilled, grain-fed, local, and raised without hormones or antibiotics.
   - Halenda's sticks contain salt, sugar, dextrose and sodium nitrate.
   - Caveat: a shelf-stable J&W jerky or stick would also need salt and cure. Market it as a high-protein, lower-sodium, clean-label snack, **not** as salt-free.
4. **Pork-free options.** The Halenda's fundraising stick is pork. A J&W chicken or beef stick, plus chicken packs, works for no-pork households, which are a large share of J&W's Scarborough and Durham catchment. Only 5 J&W SKUs mention halal, so do not claim halal broadly.
5. **Home delivery across Ontario already exists.** J&W runs weekly routes, including Tuesday Durham (Pickering to Port Perry, covering Oshawa, Whitby and Bowmanville, where every Halenda's store sits), Ontario long-haul, and express in Toronto.
   - Halenda's online store is curbside-only.
   - Its fundraising orders ship at $18 a case.
6. **Cooked, portioned, à-la-carte meal prep.** Halenda's prepared foods are deli sides and party trays (perogies, cabbage rolls, coleslaw, wings). It has no macro-portioned meals at all, while J&W has about 292 Meal Butler and cooked SKUs.
7. **Price on chicken.** J&W's 55 lb boneless breast is ≈ $6.36/lb against Halenda's $7.49–$7.99/lb. Ground beef is at parity.
8. **One modern storefront.** J&W runs Shopify with accounts, loyalty and gift cards, against Halenda's three WordPress domains with conflicting prices. J&W's own content gaps still need fixing first (see jw-audit.md).

**Where Halenda's is ahead (be honest in the pitch):**
- Award record: 3 Diamond Awards.
- Supermarket listings.
- Two plants, five stores, and a 13-year fundraising track record with field sales reps.
- A school-nutrition-compliant, shelf-stable hand-sell product.
- J&W's plant (provincially inspected since 2008) only matches it.
- Heritage is roughly a tie: Halenda's 1979 against J&W's 1973/1995 family lineage.

## 7. Corrections and caveats on the selection

1. **The program timeframe is now known.** It started **June 27, 2013**, so the $6M is cumulative over about 13 years, roughly $450K a year to groups and about $0.5M a year of wholesale revenue for Halenda's (ESTIMATE). The selection said the timeframe was not found. **Group count is still not found.**
2. **Groups keep 50–56%, not 15–20%.** Halenda's groups buy at $261–$300 a case and sell at $600. A J&W storefront that gives 15–20% will be compared with that.
   - The pitch must lean on: no upfront cash, no product handling, a bigger basket (so more dollars per order), and products families already buy.
   - Alternatively, add a hand-sell J&W protein stick at 40–50% to the group. That needs product development and a shelf-stable process approved for J&W's provincially licensed plant. Sale would be limited to Ontario, which is also Halenda's footprint.
3. **Year-2 sizing is a stretch.** The selection's year 2 (100 groups × $4,000 ≈ $400K) is close to Halenda's whole fundraising run-rate, which took 13 years and field reps to build.
   - Year 1 at about $120K is plausible.
   - A safer plan is **≈ $0.25–0.45M a year by year 2 including DTC follow-on** (ESTIMATE). This still uses the selection's 10% repeat × $130 × 4 a year logic on 3,000–6,000 buyer households.
4. **All five stores are in Durham**: Oshawa ×3, Whitby and Bowmanville. The "GTA" sites are the Etobicoke plant and pick-up point, not shops, even though the logo names Mississauga and Etobicoke.
5. **The award wording.** The Diamond winner is one of the six awarded products, so it is not "Diamond plus six more".
6. **Charcuterie retailers.** The charcuterie page lists Metro, Sobeys, Foodland and Fortinos. Food Basics appears only on the locations page.
7. **Self-claims.** "Ontario's Fastest Growing Fundraising Program" is Halenda's own claim and is unverified.
8. **"Premium".** Halenda's is award-winning but value-priced. Use it as the channel benchmark only.

## Sources
- https://halendasfundraising.com/ (home; ©2026; headline "Celebrating Six Million Meat Sticks Sold")
- https://halendasfundraising.com/about-halendas-fundraising/ (program, two modes, 50–56%, ingredients, school compliance; modified 2026-09-23)
- https://halendasfundraising.com/purchase/ (calculator, tier table, $25/bag, $18/case shipping, legacy PayPal block; modified 2026-09-23)
- https://halendasfundraising.com/product/halendas-pepperoni-stix/ ($300/$288/$273/$261 per case)
- https://halendasfundraising.com/fundraising-faqs/ (case contents, pick-up Oshawa/Etobicoke, shelf life, phone)
- https://halendasfundraising.com/contact-us/
- https://halendasfundraising.com/reviews-testimonials/ (testimonials dated 2020)
- https://halendasfundraising.com/fundraising-resources/ (blog index)
- https://halendasfundraising.com/fundraising-resources/celebrating-six-million-meat-sticks-sold/ (June 27, 2013 start; Nov 6, 2025)
- https://halendasfundraising.com/fundraising-resources/dance-fundraising-success-story/ ($10,300; Sept 2, 2026)
- https://halendasfundraising.com/fundraising-resources/youth-sports-fundraising-success-story-paige/ (8 cases, $1,536; Aug 24, 2026)
- https://halendasfundraising.com/fundraising-resources/support-local-fundraising-with-halendas/ (Buy Canadian post)
- https://halendasfundraising.com/fundraising-resources/the-advantage-of-our-new-plant-15-brydon-dr-etobicoke/
- https://www.halendas.com/ (home; 6 locations and 2 plants; ©2026)
- https://www.halendas.com/halendas-locations/ (store locator; retail partners)
- https://www.halendas.com/products/meat-freezer-packs/ (Hibernator $199/$299/$349)
- https://www.halendas.com/halendas-charcuterie/
- https://www.halendas.com/on-sale-durham/ (sale Oct 15–21, 2026)
- https://www.halendas.com/halendas-wins-2026-ontarios-finest-meat-diamond-award/ (Oct 6, 2026)
- https://www.halendas.com/david-hobson-joins-mpo-board-of-directors/ (June 2026)
- https://store.themeatdepot.ca/ (online store; WooCommerce Store API, 75 products)
- J&W comparisons: /Users/erwingarcia/Claude/JWFOODSPROPOSAL/research/jw-facts.md, jw-catalog.json, jw-audit.md

# Play 7: Team Fuel Fundraiser

Prepared by Minastech (Erwin Garcia) for J&W Foods / J&W Meal Butler · October 16, 2026
All money in CAD. Every figure is an ESTIMATE unless it is a J&W published price (jwfoods.com, Oct 16 2026) or carries a source. Shared figures come from `model-assumptions.md`. Sample groups, players and people in this file are fictional.

**One-liner (hub card):** A fundraising storefront where hockey teams, schools, soccer clubs, cadets and community groups each get their own J&W page, share link and live progress bar, and families buy freezer packs and Meal Butler meals with the group's share shown under every price.

**Why it makes money:** It turns the families around a team or school into J&W customers at about $33 each, paid to the group instead of to Meta. Every order is pre-sold and delivered in one drop on a route J&W already drives.

**Focus:** Community fundraising that brings new households to J&W.

---

## 1. Modelled on: Halenda's Fundraising (Oshawa, Durham Region)

| | |
|---|---|
| URL | https://halendasfundraising.com/ |
| Scope | GTA (Durham Region). Head office 915 Nelson St, Oshawa. Five stores, all in Durham (Oshawa ×3, Whitby, Bowmanville), plus St Jacobs Market. Fundraising pick-up at Oshawa and 15 Brydon Dr, Etobicoke (competitor-07.md §2). |
| What they do | A family butcher (since 1979) that runs a school and team fundraising program on one product: Pepperoni Stix. Groups buy a case of 240 sticks (24 bags of 10) for $261–$300 and sell each bag at $25, keeping 50–56%. Shipping is $18 a case anywhere in Ontario, pick-up is free. It offers two modes: "order the sticks, then sell" (about 95% of groups) and "collect orders, then buy" with a personalised flyer and order form (about 5%) ([purchase](https://halendasfundraising.com/purchase/), [about](https://halendasfundraising.com/about-halendas-fundraising/)). |
| Proof | First case shipped June 27, 2013. "Six million meat sticks sold" and "more than six million dollars" raised for groups (post of Nov 6, 2025) ([post](https://halendasfundraising.com/fundraising-resources/celebrating-six-million-meat-sticks-sold/)). Implied ≈ 450K sticks, ≈ 1,880 cases and ≈ $0.5M of wholesale revenue a year (ESTIMATE, competitor-07.md §2). Recent stories: a Newcastle dance studio raised $10,300 (Sept 2026); a 12-year-old BJJ athlete sold 8 cases in a month and raised $1,536 (Aug 2026). Pages updated Sept 23, 2026. Group count and company revenue were not found. |
| What we borrow (ideas only) | The two-way profit calculator (goal → orders, orders → profit) on a light-blue card. A plain rate table. A numbered order block. The "collect orders, then buy" mode, rebuilt as an online team page. The sales-rep attribution field on the order form, rebuilt as per-player links. An objection-handling FAQ for schools. Segment success stories (dance, hockey, cadets) as a content habit. From **Rowe Farms' meat fundraisers** we borrow one more idea: the group's donation shown under each product price ([Rowe Farms](https://rowefarmsonline.ca/pages/meat-fundraisers), competitors-gta-meat-grocery.md §4.2). |
| Where Halenda's is ahead (say it plainly) | 13 years of fundraising, field sales reps, two plants, three Diamond Awards, supermarket listings, and a shelf-stable product a child can sell door to door. Groups keep 50–56% of Halenda's sales. J&W's share will be 12–20%, so J&W must win on dollars per order, zero upfront cash and food families already buy. |
| J&W's edge | **Halenda's never meets the supporter.** It sells cases to the group, and the group sells bags for cash, so buyers never become Halenda's customers. J&W sells to each family directly on a team page, with consent, so every buyer becomes a J&W customer. The basket is bigger: a typical $135 J&W order sends about $21 to the group, against $12.50–$14.13 per $25 bag. J&W has pork-free packs (the Halenda's stick is pork), cooked Meal Butler meals for busy sports weeks, and its own weekly routes, including the Tuesday Durham route that passes every Halenda's store. One Shopify storefront with current prices, against three WordPress domains with conflicting price tables (competitor-07.md §3.1, §6). |

---

## 2. The mechanism: what J&W changes

J&W already sells the right products: a 25-pack of chicken burgers ($35.50), 4 kg chicken breast cases ($92), a 5 lb ground beef special ($40), family boxes ($84.99–$199) and about 292 Meal Butler cooked items. It has no fundraising offer and almost no non-brand discovery (jw-audit.md §9). This play adds six things.

1. **A team page for every group.** Each school, team, club or community group gets `jwfoods.com/team/<name>` with its name, goal, a live progress bar, days left, the drop time and place, and a "who are you ordering for?" picker. Every player or family gets a personal link (`?p=maya14`) so the organizer can see who sold what. Pages are unlisted by default and show first names, last initials and jersey numbers only.

2. **A short Team Fuel menu at regular store prices.** Families pay what they would pay at Brimley Rd. J&W pays the group a share from its own margin, and the exact dollar amount shows under every price.

   | Pack | What's in it (real J&W products and prices) | Price | Group gets |
   |---|---|---|---|
   | **Team Freezer Pack** (Concept bundle) | Premium Chicken Burgers, 25 × 6 oz ($35.50) + Case of Portioned Chicken Breast, 4 kg, 6 oz pieces, about 23 ($92) + Ground Beef Bulk Mix, 5 lb ($40). About 23 lb of meat | $167.50 | 12% = **$20.10** |
   | **Game-Week Meal Pack** (Concept bundle, Meal Butler) | 3 × Teriyaki Chicken, Green Beans & Rice 4 oz ($9.99) + 3 × Tenders, Broccoli & Sweet Potato 4 oz ($9.99) + 2 × Jerk Chicken, Green Beans & Sweet Potato 4 oz ($12.99) + 2 × Turkey, Spinach & Rice 4 oz ($12.99) + 2 × Egg White Bites, Spinach & Feta ($5.25). About 37 g protein per meal (est.) | $122.40 | 20% = **$24.48** |
   | **Kids Favourite Combo** (J&W box) | 4 chicken breasts 6–8 oz, 2 packs beef hot dogs, 2 × 1 lb ground beef, 1 lb cooked beef meatballs, 1 lb AAA beef stew, 2 kg breaded chicken fingers | $95.00 | 12% = **$11.40** |
   | **Long Weekend Box** (J&W box) | AAA striploin steaks, ribs, sausages, burgers, sliders, buns and fries | $199.00 | 12% = **$23.88** |

   Add-ons with the share shown: Beef Chili 10 oz $12 ($2.40) · Lemon Chicken Rice Soup $8.99 ($1.80) · Egg White Bites $5.25 ($1.05) · Breakfast Wrap, Egg, Spinach & Feta $5.99 ($1.20) · Chicken Souvlaki Wrap $5.99 ($1.20) · Marinated Chicken Breast Case 4 kg $100 ($12.00) · AAA New York Striploin, case of 8 × 8–9 oz $110 ($13.20) · No-Salt Chicken Souvlaki Case 5 kg $95 ($11.40).

3. **Group share rates (Concept):** 20% on Meal Butler cooked and portioned items, 12% on butcher boxes, freezer packs and cases, and 5% on any order placed through the team link for six months after the drop. Cooked food carries about 45% gross margin and raw about 30% (model-assumptions.md), so J&W keeps about 25% and 18% after the share. The higher cooked rate steers organizers toward J&W's best-margin, most distinctive product.

4. **One drop, one day.** Orders close on a Sunday, which matches J&W's existing "order by Sunday" cut-off. The following week, on the route day for that area, a J&W van parks at the arena, field, hall or studio for a 60-minute pickup window. Every order is bagged, labelled with the family's name and kept cold, and a J&W staffer stays with it. Team drops have no fee and no $100 minimum. Families can also pick up free at 2201 Brimley Rd, or choose home delivery on their usual route day at the normal fee and minimum. Drop days: Tuesday (Durham, GTA 1), Wednesday (Toronto, Scarborough, North York, Etobicoke, Mississauga, GTA 2), Thursday (Oakville to Hamilton, GTA 3), Friday (York and Peel, GTA 4). Schools default to Brimley pickup or home delivery until their board approves a school drop.

5. **Perks that cost little and help groups raise more:**
   - **"Fuel for Game Day" talk:** at $1,500 in campaign sales, a J&W butcher brings a free 30-minute talk and a tasting tray to one practice. It covers early-ice breakfasts, tournament coolers and reheating at the hotel. General food tips, not medical advice. Cost about $70.
   - **Raffle box:** at $3,000 in campaign sales, J&W adds a Long Weekend Box ($199) for the group's raffle or year-end barbecue. Cost about $139 (ESTIMATE, 70% of list).
   - **Keep fuelling the team:** 5% of orders through the team link for six months after the drop.

6. **Every buyer becomes a J&W customer, with consent.** Checkout asks for express consent to email and SMS (CASL). Those who say yes get a welcome flow: storage and reheating tips, then **$10 off their first regular order of $100 or more within 60 days**, then a reminder that the team still earns 5% through the link. The organizer sees names and order totals for the pickup list, never buyers' contact details.

**No upfront money and no cash handling.** Families pay J&W online. The group gets a statement of every order and its share by e-transfer or cheque within 10 business days of the drop. The payment is a fundraising payment from J&W, not a charitable donation, so buyers do not get tax receipts.

**Later, not counted: Team Fuel Jerky (Concept).** A J&W-made beef or chicken jerky that players could sell by hand would close the gap with Halenda's 50% model. It needs a tested recipe, shelf-life work, labels and approval under J&W's provincial licence, and could only be sold in Ontario. The prototype shows it as "in development" with a register-interest form. Its revenue is not in the numbers below.

### Launch plan
- **Oct 19 – Nov 20, 2026:** build the lean storefront on Shopify (team pages as collections, attribution through an affiliate or referral app, a share ledger), photograph the two Concept packs, write the school pack, fix the product-data issues in §9.
- **Nov 23 – Dec 6, 2026: pilot, 4 groups.** Recruit from J&W's own customers who coach, teach or sit on a parent council (in-store sign, an Instagram post to 30K followers, an email). Drops the week of Dec 1 and Dec 7: "Fill the freezer before the holidays."
- **Jan – Feb 2027:** the second half of hockey and ringette, plus school winter campaigns.
- **Mar – Jun 2027:** spring soccer and baseball, school spring fundraisers, dance and cadets. The Long Weekend Box leads in May.
- **Jul – Aug 2027:** quiet (camps and tournament teams).
- **Sep – Oct 2027:** back to school and the new hockey season. Re-book every pilot group.

---

## 3. The money

### Year 1 (Nov 2026 to Oct 2027), mid case, with ramp from startMonth 2 (Dec 2026)

Campaigns by drop month: Nov 0 · Dec 4 · Jan 3 · Feb 4 · Mar 5 · Apr 6 · May 6 · Jun 3 · Jul 1 · Aug 1 · Sep 4 · Oct 5 = **42 campaigns** (about 38 groups).

| Line | Formula | Amount |
|---|---|---|
| Fundraiser sales | 42 campaigns × 25 orders × $135 | $141,750 |
| × 0.80 incremental | About 30% of buyers are existing J&W customers; some of their orders would have happened anyway | **$113,400** |
| Buyer households | 1,050 orders × 0.9 unique | 945 |
| New to J&W | 945 × 70% | 662 |
| Follow-on regular orders | 662 × 12% become repeat = 79 × 4 orders a year × $130 × 5.26 months left on average ÷ 12 | $18,100 |
| × 0.85 incremental | | **$15,385** |
| **Year 1 mid** | $113,400 + $15,385 | **$128,785 ≈ $129K** |

Year-1 range:
- **Low $46K:** 25 campaigns × 18 orders × $125 = $56,250 × 0.75 = $42,188. Follow-on: 284 new households × 8% × 4 × $130 × 5.16/12 = $5,071 × 0.75 = $3,803.
- **High $271K:** 60 campaigns × 32 orders × $140 = $268,800 × 0.85 = $228,480. Follow-on: 1,210 new households × 18% × 4 × $130 × 5.32/12 = $50,162 × 0.85 = $42,638.

Monthly shape, year 1 (gross booked, fundraiser + follow-on): Nov $0 · Dec $13.5K · Jan $10.5K · Feb $14.1K · Mar $17.8K · Apr $21.6K · May $22.1K · Jun $12.4K · Jul $5.9K · Aug $6.0K · Sep $16.2K · Oct $19.9K = $159.9K gross, or $128.8K after incrementality.

### Run-rate (year 2, Nov 2027 to Oct 2028)

| Line | Formula | Amount |
|---|---|---|
| Campaigns | ≈ 27 returning groups (70% of 38) × 1.5 campaigns a year + 45 new groups | 85 |
| Fundraiser sales | 85 × 27 orders × $138 | $316,710 |
| × 0.80 | | **$253,368** |
| Follow-on, year-1 cohort | 79 repeat households × 60% still active × 4 × $130 | $24,767 |
| Follow-on, year-2 cohort | 85 × 27 × 0.9 × 65% new = 1,343 new households × 12% = 161 × 4 × $130 × 5.67/12 | $39,589 |
| × 0.85 | ($24,767 + $39,589) × 0.85 | **$54,702** |
| **Run-rate** | $253,368 + $54,702 | **$308,070 ≈ $308K** |

Year-2 campaign shape: Nov 6 · Dec 8 · Jan 6 · Feb 7 · Mar 9 · Apr 11 · May 11 · Jun 6 · Jul 2 · Aug 2 · Sep 8 · Oct 9.

### Margin and contribution
- **Product margin:** an assumed mix of 55% raw (30% margin) and 45% Meal Butler (45%) gives 36.75% blended.
- **Group share:** 55% × 12% + 45% × 20% = **15.6%** of fundraiser sales on average, about $21 on a $135 order.
- **Margin after the share:** 21.15% on fundraiser sales. Follow-on orders earn 36.75% less the 5% team-link share on about 60% of them = 33.75%.
- **Displacement cost:** the 20% of fundraiser sales that existing customers would have placed anyway now carries the group share too: year 1 $28,350 × 15.6% = $4,423; year 2 $63,342 × 15.6% = $9,881.
- **Gross profit after the share and displacement:** year 1 = $113,400 × 21.15% + $15,385 × 33.75% − $4,423 = **$24,754** (19% of counted revenue). Year 2 = $253,368 × 21.15% + $54,702 × 33.75% − $9,881 = **$62,168** (20%). Use **marginPct 20**.
- **Contribution after J&W's running costs (§6):** year 1 $24,754 − $22,066 − $3,200 setup ≈ **−$0.5K, break-even**. Year 2 $62,168 − $40,000 ≈ **+$22K**.
- **What J&W really buys:** about 2,000 new households in two years (662 + 1,343). The group share works out to about **$33 per new household** in year 1 ($22,113 ÷ 662) and $37 in year 2, against $60–120 for a new customer through paid ads (model-assumptions.md). Counting J&W's margin on the orders, those households arrive at roughly zero net cost in year 1.

### Sanity checks
- Year 1 is about 5% of J&W's ~$2.5M mid-case revenue; the run-rate is about 12%. Both sit inside the $60–450K year-1 and sub-$900K run-rate guardrails.
- **Against Halenda's:** about 1,880 cases a year at an assumed 6 cases per group is roughly 300 group campaigns a year (ESTIMATE; Halenda's group count was not found). J&W's 85 campaigns in year 2 is about 28% of that, spread over a wider route area (Durham, Toronto, York, Peel, Halton).
- **Market room:** the GTHL alone has 493 teams in 54 clubs and 30,000+ players (market-benchmarks.md §6b). Add soccer, ringette, baseball, schools, cadets, dance and faith groups, and 85 campaigns is a small share.
- **The selection's year-2 idea** (100 groups × $4,000 ≈ $400K plus a large DTC tail) was trimmed, as competitor-07.md §7 advised. The follow-on tail here (≈ $55K) is smaller than the selection's $0.16–0.31M, because only two cohorts exist by year 2.
- **Capacity:** year 2 is about 2,300 orders, about 44 a week on average and about 70 a week in April and May. That is 2–3 drops a week at peak, each about 2 hours of van and packer time. All volume is pre-sold before the Monday cook.

### Notes on the math
- Revenue is counted at full retail price. The group share is treated as a cost inside the margin, not as a discount.
- The average order ($135) matches J&W's online AOV assumption ($130) plus fundraiser bundling. Pilot sample orders in the prototype average $138–$154.
- Orders per campaign (25) is an estimate for a mixed set of teams (15–20 families) and schools (more families, lower take-up). It needs the pilot to confirm it.
- Follow-on orders count one-time regular orders only. If a fundraiser buyer later joins the Butcher Club (Play 3), a Goal Plan subscription (Play 1) or the AI Coach (Play 6), those revenues belong to those plays. The 0.85 factor partly covers that overlap.
- Nothing here counts corporate gifting (Play 5), office meal programs (Play 4) or partner wholesale (Play 2). A gym or club that becomes a wholesale partner is counted in Play 2 from that point.
- The jerky line is not counted.

---

## 4. KPIs

| KPI | Target |
|---|---|
| Pilot groups live by Dec 6, 2026 | 4 |
| Campaigns, Nov 2026 – Oct 2027 | 42 (about 38 groups) |
| Orders per campaign | 25 average |
| Average order | $135 |
| Group share per new household | $35 or less |
| Buyers new to J&W | 70% |
| Email/SMS opt-in at checkout | 60%+ |
| New households placing a regular order within 6 months | 12% |
| Groups that book another campaign within 12 months | 70% |
| Orders collected in the drop window | 97%+ (the rest picked up at Brimley within 3 days) |
| Group payouts sent within 10 business days of the drop | 100% |
| Campaigns reaching 75% of their goal | 60%+ |

---

## 5. AI agents this play needs

| Agent | Job | Where it shows on screen |
|---|---|---|
| **Team Fuel Desk** (the shared Butler Concierge in fundraising mode) | Answers organizers and parents on rates, goals, drops, payouts, school rules, allergens (only from approved product data) and the Ontario-only rule. Hands exceptions to the coordinator. | Chat "Team Fuel Desk" on the page |
| **Team Page Builder** (new) | Turns a two-minute form into a draft team page: goal and orders needed, campaign dates, the route-day drop slot, perks, and a share kit (team-app post, text, email, QR flyer). Checks claims: no blanket salt or sugar claims, Ontario-only note, school-board caveat. The coordinator approves before the page goes live. | "Build my team page" result in the organizer form; team view draft for Markham Northstar Dance |
| **Campaign Coach** (new) | Watches each campaign against its goal and pace. Drafts day-3, day-7 and last-48-hours messages for the organizer to send to their own families, plus shout-outs. Forecasts orders at close for production. J&W never messages families who have not opted in. | Progress bar pace chip; team view nudge drafts for the Snowhawks and Cedar Hollow |
| **Drop and Production Planner** (shared with the production forecast and route agents) | At Sunday close, rolls orders into named bags, a pick list and labels. Adds pack counts to Monday's cook, cut and pack sheet and the raw order. Slots the drop as the last stop on the route day with a 60-minute window, and drafts the transactional text to each family. | Team view "Production and route impact" and the Whitby Wolves drop sheet |
| **Fundraiser Payout agent** (new) | Calculates each group's share by product rate, handles refunds and missed pickups, drafts the statement and the e-transfer or cheque request. The owner approves payouts over $500. | Team view payout ledger and the Whitby Wolves statement |
| **Lifecycle marketing agent** (shared, Klaviyo) | Runs the welcome flow for opted-in buyers: reheating tips, the $10 first-order offer, the 5% team-link reminder, then the regular J&W flows. Invites organizers to re-book next season. CASL consent and unsubscribe checks on every send. | Team view welcome-flow draft and the new-customer funnel |
| **Group Prospecting agent** (shared B2B prospecting agent) | Builds seasonal lead lists of minor hockey and ringette teams, soccer clubs, school councils, cadet corps, dance studios and faith groups along the GTA 1–4 corridors. Drafts intro emails with a tasting-tray offer to published volunteer or fundraising contacts. The coordinator approves each sequence. | Team view "Next season" pipeline: 32 new leads |

---

## 6. JW's costs to run it (excluding Minastech's fee)

- **Setup about $3,200:**
  - Photos of the two Concept packs and a team-kit design (flyer, QR poster, bag label): $800
  - Insulated totes, name labels, "Team Fuel" stickers and 4 drop coolers: $900
  - Pilot tasting trays and the printed school pack: $500
  - Shopify setup time, 20 h × $25: $500
  - Label printer: $300
  - First flyer print run: $200
- **Year 1 running about $22.1K, or $1,840 a month on average:**
  - Fundraising coordinator, 5 h/week average × 48 weeks × $25: $6,000
  - Drop van time, 42 drops × $67 (2 h of driver and packer at about $26 loaded, plus $15 of fuel): $2,814
  - Named bags and labels, 1,050 orders × $2.33 ($1.50 packaging + 2 minutes of packing): $2,447
  - "Fuel for Game Day" talks, 25 × $70 (1.5 h of staff time + a $25 tasting tray at cost): $1,750
  - Raffle boxes, 19 × $139 at cost: $2,641
  - Meta ads to coaches and parent councils in route corridors, $200 × 11 months: $2,200
  - Flyers and QR posters, 42 × $40: $1,680
  - Software, $80 × 11 months (attribution app about $50, payout fees about $10, Claude API about $20): $880
  - Welcome offers, 662 new households × 25% redeem × $10: $1,654
- **Year 2 running about $40K:** coordinator 8 h/week ($10,000), 85 drops ($5,695), 2,295 orders packed ($5,347), 50 talks ($3,500), 38 raffle boxes ($5,282), ads ($2,400), flyers ($3,400), software ($1,020), welcome offers ($3,356).
- **Not in this list, because it sits inside the margin:** the group share itself (about $22.1K in year 1, $49.4K in year 2) and the 5% team-link share on follow-on orders (about $0.5K and $1.9K).
- **Contribution:** year 1 about break-even (−$0.5K); year 2 about +$22K, plus about 2,000 new households.

---

## 7. Who does the work at J&W

- **Fundraising coordinator** (Tasia or Lucas, as J&W decides): about 3 h/week during the December pilot, 5 h/week on average in year 1, 8 h/week in year 2. Approves team pages, calls organizers, books talks, runs drops and approves agent drafts.
- **Driver:** about 1.5 h per drop on the existing route day (42 drops in year 1, 85 in year 2).
- **Packer:** about 2 minutes per order for named bags, plus 30 minutes per drop.
- **Butcher or Lucas:** 1.5 h per "Fuel for Game Day" talk, about 2 a month.
- **Owner (Bill or Steve):** about 15 minutes a week to approve payouts over $500 and new school partners.
- **Minastech** builds the storefront and the agents.

---

## 8. Assumptions

- The lean storefront is live by Mon Nov 23, 2026. Four pilot groups come from J&W's own customer base.
- 42 campaigns in year 1 and 85 in year 2, with 70% of groups returning and running about 1.5 campaigns a year.
- 25 orders per campaign in year 1 (27 in year 2) at $135 ($138 in year 2).
- Product mix 55% raw and 45% Meal Butler. Group share averages 15.6%.
- Margins from model-assumptions.md: cooked 45%, raw 30%.
- 0.9 unique households per order; 70% new to J&W in year 1 and 65% in year 2.
- 12% of new households become repeat customers, ordering 4 times a year at $130; 60% of the year-1 repeaters are still active in year 2.
- Incrementality 0.80 on fundraiser sales (existing customers shifting orders) and 0.85 on follow-on.
- 60% of follow-on orders use the team link (5% share). 25% of new households redeem the $10 welcome offer.
- About 60% of campaigns pass $1,500 (talk) and 45% pass $3,000 (raffle box).
- Team drops run on GTA routes 1–4 only. Long-route areas use home delivery, or a group drop by request for 40+ orders.
- Ontario-only delivery: J&W's plant is provincially inspected.
- J&W confirms the price and margin of the 25-pack chicken burgers before launch (see §9).

---

## 9. Risks and how to handle them

- **The share is lower than Halenda's 50–56%.** Lead with dollars per order (about $21 against $12.50–$14.13 per bag), fewer sales per family, no upfront case purchase and food families already buy. If pilot groups still say no, raise the Meal Butler rate to 25% (J&W still keeps about 20%).
- **Thin margin.** About 21% after the share. Keep the menu short, keep drops on existing route days, and watch contribution per campaign. A campaign below about 12 orders loses money once drop time is counted, so set a 12-order minimum for a team drop (smaller campaigns use Brimley pickup).
- **Product data must be fixed first.** The 25-pack chicken burgers are listed at $35.50, about $3.79/lb, which may be below the 30% margin model; confirm before launch. The "Ground Beef Bulk Mix" title says 5 lb but its description says 10 lb, and its photo file is named "GROUNDPORK". J&W's "salt and sugar free" line conflicts with some ingredient lists (Beef Chili lists brown sugar and salt). Fundraiser pages make no blanket salt or sugar claims until labels are checked.
- **Schools.** School boards have fundraising rules, and Ontario's school food and beverage policy (PPM 150) may apply to food sold through a school. Send each principal a one-page school pack. Default schools to Brimley pickup or home delivery until the board approves a school drop.
- **Cold chain at drops.** Frozen food in coolers, a J&W staffer on site for the whole window, and uncollected orders back to Brimley the same day and held 3 days for free pickup.
- **Children's names and privacy.** First name, last initial and jersey number only. Families can hide their name. Pages are unlisted and not indexed. Organizers never see buyers' contact details.
- **CASL.** J&W emails and texts only buyers who gave express consent. Organizers send campaign messages to their own contacts. Drop-day texts are transactional.
- **Allergens and dietary needs.** Allergen answers come only from approved per-product data or from a person. The Long Weekend Box includes sausages and ribs, so it is flagged for families who avoid pork. J&W does not label packs halal or kosher (only 5 of 979 SKUs mention halal).
- **Tax and accounting.** The group payment is a marketing cost for J&W, not a charitable gift, and buyers get no tax receipts. J&W's accountant confirms how group payments are recorded, including any HST question.
- **Peak overlap.** December also carries corporate gifts (Play 5). Cap the pilot at 4 groups and put drops on Tuesday and Wednesday.
- **Owner-led brand.** Schools and church groups will look J&W up. Put the 4.8★ Google rating (611 reviews) on the page and keep the coordinator as the program's face (jw-audit.md §2).
- **Ontario-only sales.** Out-of-province relatives can buy only for pickup or delivery in Ontario; the meat never leaves the province.
- **Jerky.** Not counted. Development needs approval under the provincial licence and a shelf-life plan. Treat it as a 2027 project, not a launch item.

---

## 10. Prototype spec (one self-contained page)

**File:** `site/prototypes/07-team-fuel-fundraiser.html` · `JWC.init({ n: 7, ... })`

### Concept (what it demonstrates)
A fundraising front door J&W does not have today. Organizers see what their group earns, work out a goal in two taps, and set up a team page that an AI agent drafts in seconds. Parents and supporters see a real team page: a live progress bar, the group's share under every price, a player picker, and checkout on J&W's real routes with a free team drop. The JW team view shows the December pilot: live campaigns, agent drafts to approve, the drop sheet, the production and route impact, payouts, and the new customers the program brings in.

### The wow
On the Snowhawks team page, a parent picks "Maya R. #14", taps Add on the Team Freezer Pack, and the sticky bar shows "$20.10 to the Snowhawks". The progress bar shows a striped "pending" segment on top of the $456.12 already raised. After the demo checkout, the segment fills in, the total counts up to $476.22, the order count ticks from 22 to 23, Maya's shout-out count goes up, and a thank-you card says how much this order sent to the team.

### Design direction
- **Inspired by Halenda's Fundraising:** a white utility bar with an outlined call-to-action pill; a full-bleed photo hero with a dark overlay and a centred white headline; short coloured rules under centred section titles; a light-blue calculator card; a plain rate table; a numbered order block; an objection-handling FAQ. **J&W adds** what Halenda's lacks: per-team pages with a scoreboard-style progress bar, the share under every price, per-player links, and one storefront with current prices. Rink and pitch line drawings (inline SVG) stand in for team photos. No Halenda's text, logos or photos.
- **Palette:**

  | Hex | Role |
  |---|---|
  | `#154D8E` | J&W laurel navy: links, secondary buttons, headings on light, progress "raised" fill |
  | `#0E1E36` | Rink night: hero overlay, team-page scoreboard band, closing band |
  | `#C2481A` | Ember: primary CTAs, "to your group" amounts (white on ember 4.96:1) |
  | `#9E3B12` | Ember deep: share-chip text on ember tint (5.78:1) |
  | `#FCE9DD` | Ember tint: share chips under prices, pending progress stripe |
  | `#F3F7FB` | Ice: page background |
  | `#FFFFFF` | Cards, utility bar |
  | `#13202F` | Ink: body text (15.3:1 on ice) |
  | `#526070` | Muted text (5.97:1 on ice) |
  | `#D9E2EC` | Hairlines and borders |
  | `#7FB3D5` | Meal Butler sky: calculator card border, rink-line SVG, accents on rink night (7.4:1) |
  | `#E6F1F8` | Sky tint: calculator card background |
  | `#5B5A8C` | Meal Butler slate: "Meal Butler" pack tags, AI agent badges in team view |
  | `#237A4B` | Turf green: "on pace", "paid", unlocked milestones |
  | `#F2B33D` | Goal gold: goal marker and big numerals on rink night only (8.98:1) |

- **Fonts:** **Big Shoulders Display** (700/800) for uppercase headings and scoreboard numerals; **Instrument Serif** italic for one accent line per section (a nod to Halenda's serif accents); **Inter** (400–700) for body, with tabular numbers in all money. `https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&display=swap`
- **Layout:** mobile-first single column with 16px gutters; max width 1120px. White utility bar under the concept bar: J&W logo (`../assets/img/jw-logo.jpg`, 36px) + "TEAM FUEL" wordmark, and an outlined ember pill "Start a fundraiser". Centred section titles with a 40px ember rule. Hero: full-bleed product photo under a rink-night gradient, centred headline; the "at a glance" card overlaps the hero bottom on mobile and sits right of the headline on desktop. Team page: a rink-night scoreboard band (team crest circle with initials, name, big numerals, a 14px progress bar with a gold goal tick) and pack cards in 1 column (mobile), 2 (tablet), 4 (desktop). Add-ons in a horizontal snap rail with the next card peeking. Sticky bottom bar on mobile while the team page is in view (items · total · share · "Review order"), 52px tall, above the framework dock. Tables become stacked cards under 640px. Tap targets 44px.
- **Tone:** warm, local and practical. Talks to volunteer parents who are short on time. Short sentences, Canadian spelling, no exclamation-mark pile-ups, no hype.

### Customer view: sections in order (exact copy)

**S0 · Season strip** (ember tint, ember-deep text): "Holiday freezer fundraiser: sign up by Sun Nov 22. Orders close Sun Dec 6, and your drop is the week of Dec 7."

**S1 · Utility bar:** logo + "TEAM FUEL" · links: How it works · Team page · Earnings · FAQ · button "Start a fundraiser".

**S2 · Hero** (photo: `chicken-burgers-1` image at width 1600, rink-night overlay):
- Eyebrow: "J&W Team Fuel Fundraiser"
- H1: "Raise money with food your families already buy."
- Accent line (Instrument Serif italic, sky): "For teams, schools and clubs across the GTA."
- Sub: "Ontario chicken, butcher-cut beef and Meal Butler cooked meals from our family plant in Scarborough. Your group's share shows under every price. Nothing to pre-buy, no cash to collect, and one drop at your arena, field or hall."
- Buttons: "Start a fundraiser" (ember) · "See a team page" (white outline).
- **"At a glance" card:**
  - 12% to 20% of every order goes to your group
  - About $21 on a typical $135 order (est.)
  - $0 up front. Families pay J&W online
  - One drop on our route day, or free pickup at 2201 Brimley Rd
  - Paid within 10 business days of the drop
  - Free "Fuel for Game Day" talk at $1,500 in sales

**S3 · Proof band** (4 items, icons): "Family butcher since 1995" · "Ontario-inspected plant since 2008" · "4.8★ from 611 Google reviews" · "Weekly routes from Port Perry to Hamilton".

**S4 · How it works** (H2 "How it works", accent "Four steps, about three weeks."):
1. **Tell us about your group.** "Name, goal, dates and where you practise. Your team page is ready within one business day."
2. **Share your link.** "Every player or family gets their own link, so you can see who sold what. Post it in your team app, text it, or print the QR flyer."
3. **Families order online.** "Supporters pay J&W directly. You never handle cash or product. Your group's share shows under every price."
4. **One drop, then you get paid.** "We bring every order, bagged and labelled by name, to your arena or hall on our route day. Your group's money arrives by e-transfer or cheque within 10 business days."

**S5 · Team page demo** (id `team`; H2 "This is your team page", sub "Here's what a family sees when they tap your link. Try it: add a pack and watch the bar move." Small grey tag: "Sample team. Names are fictional."):
- **Scoreboard band:** crest circle "SH" · "SCARBOROUGH SNOWHAWKS U11 AA" · "Raising $750 for tournament fees and ice time." · big numerals "$456.12" + "raised of $750" · progress bar 61% with gold goal tick · "22 orders · 6 days left · Orders close Sun Dec 6" · drop chip "Team drop: Wed Dec 9, 5:00–6:30 pm · team arena, east lot" · milestone chips (turf): "✓ Coach talk unlocked" "✓ Raffle box unlocked" · pace chip "On pace for about $705".
- **"Who are you ordering for?"** chips (radio group): Maya R. #14 · Ethan K. #7 · Arjun P. #22 · Leo M. #3 · Sofia D. #11 · Noah T. #9 · Just the team (default).
- **Pack cards** (photo via `JWC.img` or the extra URLs below, name, tag, 1-line pitch, contents list, price, share chip "$20.10 to the Snowhawks", stepper + "Add"):
  - Team Freezer Pack · tag "Concept bundle" · "About 23 lb of Ontario chicken and beef for the freezer." · $167.50 · $20.10
  - Game-Week Meal Pack · tags "Meal Butler" (slate) + "Concept bundle" · "10 cooked meals and 2 egg-bite breakfasts for a week of practices and games. About 37 g protein per meal (est.). Heat in the bag." · $122.40 · $24.48
  - Kids Favourite Combo · tag "J&W box" · "Weeknight dinners kids ask for." · $95.00 · $11.40
  - Long Weekend Box · tag "J&W box" · "Steaks, ribs, sausages, burgers and sliders for a team barbecue." · note "Includes pork" · $199.00 · $23.88
- **"Add to any order"** rail: the 8 add-ons in §2 with their share chips.
- **Shout-outs:** "Ethan K. #7 · 4 orders" · "Maya R. #14 · 3 orders" · "Arjun P. #22 · 3 orders" · small note "Families can hide their name."
- **Share row:** "Share this page" · Copy link · Text · Team app (demo toasts: "Link copied (demo)").
- **Sticky bar** (when cart has items): "{n} items · {total} · {share} to the Snowhawks · Review order".

**S6 · What your group earns** (id `earn`; H2 "What your group earns", accent "Same prices as our store."):
- Copy: "Families pay our regular prices. J&W pays your group a share of every order from our side, and we show the exact amount under each price."
- Rate table: Meal Butler cooked and portioned packs → **20%** · Butcher boxes, freezer packs and cases → **12%** · Orders through your team link for 6 months after the drop → **5%**.
- Chip: "Typical order $135 → about $21 for your group (est.)"
- Fine print: "Rates are a Concept for the 2026–27 pilot."
- **Goal calculator** (sky-tint card, two tabs):
  - Tab "I have a goal": inputs Goal ($, default 1,000) and Families (default 16). Output: "About **48 orders**. That's 3 per family: your own freezer fill plus two supporters." Formula: orders = ceil(goal ÷ 21.06); per family = orders ÷ families, 1 decimal. If per family ≤ 3.5 use "your own order plus a couple of supporters", else "about {n} per family". Button "Start with this goal" (prefills S11).
  - Tab "I know our orders": input Orders (default 40). Output: "About **$5,400** in sales and **$842** for your group." Plus milestone lines: "✓ Coach talk at $1,500 in sales" and "✓ Raffle box at $3,000 in sales" (grey if not reached).
  - Footnote: "Based on a $135 average order and a 15.6% average share. Estimates, not a promise."

**S7 · Perks** (H2 "A little extra for your team", 3 cards):
- **Fuel for Game Day.** "Pass $1,500 in sales and a J&W butcher brings a free 30-minute talk and a tasting tray to one practice. Early-ice breakfasts, tournament coolers, reheating at the hotel. General food tips, not medical advice." Button "Book your talk".
- **Raffle box.** "Pass $3,000 in sales and we add a Long Weekend Box ($199) for your team raffle or year-end barbecue."
- **Keep fuelling the team.** "For six months after your drop, every order through your team link still sends 5% to your group."

**S8 · Who it's for** (6 cards; each button "Plan a fundraiser" scrolls to S11 with the type preselected):
- Hockey and ringette · best Oct–Feb · "Tournament fees, ice time, team jackets."
- Soccer and baseball · best Mar–Jun · "Spring kit, field rentals, travel."
- Schools and parent councils · best Nov–Dec and Apr–May · "Trips, playgrounds, graduation."
- Cadets, scouts and guides · any time · "Camps and gear."
- Dance, gymnastics and martial arts · best Jan–Apr · "Competition and recital costs."
- Faith and community groups · any time · "Youth programs and community meals."

**S9 · Questions organizers ask** (id `faq`, accordion):
1. "Do we have to pre-buy anything?" "No. Families pay J&W online when they order. You never hold cash or product."
2. "When do we get paid?" "Within 10 business days of your drop, by e-transfer or cheque, with a statement of every order."
3. "Is this a donation? Do buyers get tax receipts?" "No. Your group's share is a fundraising payment from J&W, not a charitable donation, so we don't issue tax receipts."
4. "Can you deliver to our school?" "School boards have their own fundraising and food rules. We send your principal a one-page school pack. Until your board says yes to a school drop, families can pick up free at Brimley Rd or choose home delivery."
5. "What if a family misses the drop?" "We take their order back to Brimley Rd frozen and hold it 3 days for free pickup (Mon–Fri 9–6, Sat 10–4)."
6. "Allergies, pork and halal?" "Every pack comes with an ingredient and allergen sheet before your campaign starts, and our coordinator confirms anything specific. The Freezer Pack, Game-Week Pack and Kids Combo list no pork. The Long Weekend Box includes sausages and ribs. We don't label packs halal or kosher."
7. "Can relatives outside Ontario help?" "Yes, if the food stays here. We deliver only in Ontario because our plant is provincially inspected. A grandparent in BC can buy a pack for a team family to pick up at the drop."
8. "How long should a campaign run?" "Two weeks works well: open on a Monday, close on a Sunday, drop the next week on our route day."
9. "Where do you do team drops?" "On our weekly routes: Tuesday in Durham (Pickering to Port Perry), Wednesday in Toronto, Scarborough, North York, Etobicoke and Mississauga, Thursday from Oakville to Hamilton, Friday in York and Peel. Farther away, families choose home delivery on our long routes."

**S10 · Coming next** (dashed card, tag "Concept · in development"): H3 "Team Fuel Jerky" · "We're working on a J&W-made jerky that players could sell by hand. It isn't for sale yet. It needs a tested recipe, shelf-life testing and approval under our provincial licence." · email input + "Tell me when it's ready" · "Demo: nothing is sent."

**S11 · Start a fundraiser** (id `start`; H2 "Start a fundraiser", sub "About two minutes. Our coordinator checks every page before it goes live."):
- Fields: Group name · Type (select: the 6 types in S8 + Other) · City (`JWC.cities()`) · Campaign window (radio): "Holiday 2026 · Nov 23 – Dec 6" / "Winter 2027 · Jan 18 – 31" / "Spring 2027 · Apr 19 – May 2" · Goal ($) · Number of families · Drop spot ("Arena, field, hall or studio") · Your name · Email. "Use sample" link fills: Rouge Valley Rapids U12 Girls · Soccer and baseball · Pickering · Spring 2027 · $1,000 · 16 · "Soccer fields, north lot" · Dana L. · dana@example.com. Note: "Demo: nothing is sent."
- Button "Build my team page" → 900 ms "Team Page Builder is drafting…" shimmer → **draft card** (slate "Drafted by Team Page Builder" badge):
  - "Your page: jwfoods.com/team/rouge-valley-rapids-u12 (demo)"
  - "Goal $1,000 ≈ 48 orders, about 3 per family (est. at $21 an order)."
  - "Orders open Mon Apr 19 and close Sun May 2, 2027. Drop: Tue May 4 on our GTA 1 route, 4:30–6:00 pm at Soccer fields, north lot. We'll confirm the spot with you."
  - "Perks: free coach talk at $1,500 in sales; raffle box at $3,000."
  - Share-kit tabs: **Team app** "Rapids families: our J&W fundraiser opens Monday. Fill your freezer with Ontario chicken and beef, or grab a week of cooked Meal Butler meals. About $20 of every order goes to our team. One pickup at the field on Tue May 4. Order here: {link}" · **Text** "Hi! Our soccer team is raising money with J&W Foods in Scarborough. If you buy meat or meal prep anyway, about $20 of your order goes to the team. Order by Sun May 2: {link}" · **Email** subject "Help the Rapids and stock your freezer" · **Flyer** (QR placeholder SVG + team name + dates).
  - Buttons: "Send for approval" · "Edit".
- Drop-day logic: route = first route from `JWC.routesFor(city)` that is not `pickup` or `express`. Drop day = that weekday in the week after the window closes: Holiday → Tue Dec 8 / Wed Dec 9 / Thu Dec 10 / Fri Dec 11, 2026; Winter → Feb 2 / 3 / 4 / 5, 2027; Spring → May 4 / 5 / 6 / 7, 2027. Long routes (Wednesday and Friday long, $35) show: "Team drops run on our GTA routes. For {city}, families can choose home delivery on the {day} route, or we can plan a group drop for 40+ orders."

**S12 · Closing band** (rink night): H2 "Ready when your team is." · "Tell us your goal and your dates. We'll have your team page ready within one business day." · "Start a fundraiser" · "Call (416) 298-1350".

### Customer flows (each clickable end to end)
1. **Parent orders a freezer pack for the team drop.**
   - "See a team page" → pick "Maya R. #14" → Add on Team Freezer Pack (sticky bar: "1 item · $167.50 · $20.10 to the Snowhawks"; striped pending segment on the bar).
   - "Review order" opens a `JWC.modal` review sheet: items, "To the Snowhawks: $20.10, paid by J&W from our share, not added to your price", "Ordering for: Maya R. #14", and three choices: **Team drop** "Wed Dec 9, 5:00–6:30 pm · team arena, east lot · no fee, no minimum" (default) · **Pick up at 2201 Brimley Rd** "free, ready from Tue Dec 8" · **Home delivery** "on your route day · $20–$35 · $100 minimum" (shows a city select, default Scarborough).
   - "Continue to demo payment" → `JWC.checkout({ title: 'Snowhawks U11 AA fundraiser · team drop Wed Dec 9', extraRows: [{ label: 'Team drop, Wed Dec 9 (no fee, no minimum)', amount: 0 }], note: 'Team drop Wed Dec 9, 5:00–6:30 pm, team arena east lot. For Maya R. #14. $20.10 to the Snowhawks, paid by J&W.', onPlaced })`. Do not pass `city`, so the framework defaults to free pickup.
   - onPlaced: raised $456.12 → $476.22 (count-up), orders 22 → 23, Maya 3 → 4, toast "You just sent $20.10 to the Snowhawks." The page shows a thank-you card (not a modal): "Thank you. The Snowhawks are at $476.22 of $750 (63%)." with "Share with one more family" (copy demo link) and a consent card: "Want $10 off your first regular J&W order of $100 or more? [Yes, email me the offer] [No thanks]. Demo: nothing is sent."
2. **Grandparent orders Meal Butler with home delivery in Whitby.**
   - "Just the team" → Add Game-Week Meal Pack + Beef Chili (sticky bar "2 items · $134.40 · $26.88 to the Snowhawks").
   - Review → "Home delivery" → city Whitby → `JWC.checkout({ title: 'Snowhawks U11 AA fundraiser · home delivery', city: 'Whitby', note: '$26.88 to the Snowhawks, paid by J&W.', onPlaced })`. The framework shows the real Tuesday GTA 1 route, $20 fee, $100 minimum met, total $154.40. Place → bar to $483.00 (or +$26.88 on whatever the current total is).
3. **Organizer sets up a team page.**
   - Goal calculator: Goal $1,000, Families 16 → "About 48 orders…" → "Start with this goal" (scrolls to S11 with goal and families filled).
   - "Use sample" → "Build my team page" → draft card with dates, drop slot and share kit → switch share-kit tabs → "Send for approval".
   - Demo confirmation (`JWC.modal`): "Thanks, Dana. Our fundraising coordinator will check your page and call you within one business day. Demo: nothing is sent." Save the application with `JWC.store.set('p7-apps', …)` so it appears in the team view's applications list.
4. **Coach books the free talk.** Perks → "Book your talk" → modal with practice date (date input), start time, arena or field name → "Request this time" → confirmation "Requested. We'll confirm by phone within one business day. Demo: nothing is sent."
5. **Earnings check.** Calculator tab "I know our orders" → 40 → "$5,400 in sales and $842 for your group" with both milestones ticked → "Start with this goal" prefills the form with goal $842.
6. **Jerky interest.** S10 → email → "Tell me when it's ready" → toast "Saved. We'll email you when it's ready (demo)."

### JW team view (`data-team`; all sample data, fictional groups)
`teamNote`: "The fundraising desk for the December pilot: live campaigns, agent drafts to approve, the drop sheet, the production and route impact, and payouts."

1. **Header:** "Team Fuel Desk · Mon Nov 30, 2026 · pilot week (sample data, fictional groups)".
2. **KPI tiles:** Live campaigns **4** · Orders **97** · Sales **$14,046** · Owed to groups **$2,068** · New to J&W **69 of 97 (71%)** · Opted in to email/SMS **61 (63%)**. Demo orders placed in the customer view add to Orders, Sales and Owed.
3. **Live campaigns** (with mini progress bars):

   | Group | Type | Drop | Goal | Raised | Orders | Closes | Status / next step |
   |---|---|---|---|---|---|---|---|
   | Scarborough Snowhawks U11 AA | Hockey | Wed Dec 9 · GTA 2 · team arena, 5:00–6:30 pm | $750 | $456.12 (61%) | 22 | Sun Dec 6 | On pace for ≈ $705. Last-48-hours message drafted |
   | Cedar Hollow PS Parent Council | School | Brimley pickup + home delivery (school drop waiting on board) | $1,500 | $707.80 (47%) | 34 | Sun Dec 6 | Behind pace. Newsletter post drafted |
   | Whitby Wolves Ringette U14 | Ringette | Tue Dec 1 · GTA 1 · arena lot, 4:30–5:30 pm | $600 | $643.74 (107%) | 29 | Closed Sun Nov 29 | Drop sheet ready. Raffle box earned |
   | 1st Ajax Lakeshore Cadets | Cadets | Tue Dec 8 · GTA 1 · cadet hall, 6:00–7:00 pm | $500 | $260.28 (52%) | 12 | Sun Dec 6 | Coach talk booked Thu Dec 3 |

   Demo orders from `jwc:order` (proto 7) appear in a "Latest Snowhawks orders" mini-table above: order no · for · items · delivery · to team.
4. **AI drafts waiting for you** (Approve / Edit / Skip; Approve shows a toast and moves the card to "Approved today"; slate agent badge on each):
   - **Campaign Coach · Snowhawks:** "For the team manager to post in the team app on Fri Dec 4: 'Snowhawks families: two days left. We're at $456 of $750. A Team Freezer Pack sends $20.10 to the team and a Game-Week Meal Pack sends $24.48. Pickup is Wed Dec 9 at the rink, 5:00–6:30. Order by Sunday: {link}'" · note "J&W doesn't message families who haven't opted in. The manager sends this."
   - **Campaign Coach · Cedar Hollow PS:** "Behind pace: 47% with 6 days left. Forecast at close ≈ 52 orders, $1,083 (72%). Drafted a newsletter blurb: 'Skip a week of cooking and help our school. A Game-Week Meal Pack is 10 cooked meals for $122.40, and $24.48 of it comes to Cedar Hollow. Order by Sunday.'"
   - **Drop and Production Planner · Whitby Wolves, Tue Dec 1:** "29 orders in 29 named bags, 4 coolers. Last stop on GTA 1: arrive 4:15, window 4:30–5:30, about +80 min of van time. Pick list attached. Transactional text to 29 families with the window." Button label "Approve and print labels".
   - **Fundraiser Payout agent · Whitby Wolves statement:** "29 orders, sales $4,462.46. Meal Butler $1,352.96 × 20% = $270.60. Butcher $3,109.50 × 12% = $373.14. Total **$643.74** by e-transfer to the club treasurer by Tue Dec 15, plus a Long Weekend Box raffle prize ($199 value) at the drop. Needs owner approval (over $500)."
   - **Lifecycle agent · welcome flow, 61 opted-in buyers:** "Day 2: how to store and reheat. Day 10: $10 off your first regular order of $100+. Day 30: your team still earns 5% through its link for six months after the drop. CASL consent ✓ · unsubscribe ✓."
   - **Team Page Builder · Markham Northstar Dance (application):** "Goal $1,500 ≈ 72 orders, about 2.9 per family (25 families). Orders Jan 18–31, drop Fri Feb 5 on GTA 4 at the studio, 4:30–6:00 pm. Claims check ✓ (no salt or sugar claims, Ontario-only note)."
   - **Group Prospecting agent:** "32 new leads for Jan–Feb along GTA 1 and GTA 2: minor hockey and ringette teams, school councils and cadet corps in Pickering, Ajax, Whitby and Scarborough. Intro emails drafted to published volunteer contacts, with a tasting-tray offer. CASL check ✓. Sends 8 a day once approved."
5. **Production and route impact:**

   | | Tue Dec 1 (Whitby Wolves, final) | Week of Dec 7 (3 campaigns, forecast at close) |
   |---|---|---|
   | Team Freezer Packs | 11 | 32 |
   | Game-Week Meal Packs | 10 | 38 |
   | Kids Favourite Combos | 5 | 20 |
   | Long Weekend Boxes | 3 + 1 raffle | 7 + 2 raffle |
   | Cases and add-ons | 1 marinated chicken case, 1 no-salt souvlaki case, 6 beef chili, 4 lemon chicken soup, 4 egg white bites | about 7 orders |
   | Orders | 29 | about 104 |

   - **Cook plan, Mon Dec 7 (from 38 Game-Week packs):** 114 Teriyaki Chicken, Green Beans & Rice · 114 Tenders, Broccoli & Sweet Potato · 76 Jerk Chicken, Green Beans & Sweet Potato · 76 Turkey, Spinach & Rice · 76 Egg White Bites.
   - **Raw:** 32 chicken breast cases (128 kg), 32 burger 25-packs, 160 lb ground beef.
   - **Route:** Tue Dec 8 GTA 1 +1 drop (Ajax cadet hall, 6:00–7:00 pm, +90 min, 1.5 h driver overtime) · Wed Dec 9 GTA 2 +1 drop (Snowhawks rink, 5:00–6:30 pm, +100 min) · Brimley pickups ≈ 40 (Cedar Hollow) · home deliveries ≈ 12 on the usual routes.
   - **Planner note:** "All of it is pre-sold, so nothing is cooked on spec. Order about 150 kg of chicken breast and 160 lb of ground beef by Thu Dec 3."
6. **Payout ledger:**

   | Group | Orders | Sales | To group | Extras | Status |
   |---|---|---|---|---|---|
   | Whitby Wolves Ringette U14 | 29 | $4,462.46 | $643.74 | Raffle box | Statement drafted · owner approval · pay by Tue Dec 15 |
   | Scarborough Snowhawks U11 AA | 22 (open) | $3,171.77 | $456.12 so far | Raffle box earned · talk to book | Open |
   | Cedar Hollow PS Parent Council | 34 (open) | $4,687.02 | $707.80 so far | Raffle box earned | Open |
   | 1st Ajax Lakeshore Cadets | 12 (open) | $1,724.98 | $260.28 so far | Talk Thu Dec 3 | Open |
   | **Total** | **97** | **$14,046.23** | **$2,067.94** | | |

7. **New customers from fundraisers (pilot so far):** Buyers 97 → New to J&W 69 (71%) → Opted in 61 → Welcome flow scheduled 61 → Target: 12% of new households place a regular order within 6 months (≈ 8 from this pilot). Line: "Group share per new household so far: $30 ($2,068 ÷ 69)."
8. **Next season:** Applications 3 (Markham Northstar Dance · draft ready; Pickering Pond Kings U13 · call booked; Milner Avenue Faith Centre youth group · new) · Leads 32 · Re-runs booked 1 (Whitby Wolves, spring Apr 19 – May 2). Applications saved from the customer form appear here.

### Chat: "Team Fuel Desk"
- **Greeting:** "Hi, I'm the Team Fuel Desk. I can work out how many orders your group needs, explain how drops and payouts work, or answer a parent's question. Is your group a team, a school or a club?"
- **Suggestions:** "How much does our group earn?" · "How many orders for a $1,000 goal?" · "Can you deliver to our arena?" · "Is anything peanut-free or pork-free?"
- **Rules** (first match wins; regex case-insensitive):
  1. `\b(allerg\w*|peanuts?|nuts?|nut-free|gluten|celiac|dairy|sesame|pork|halal|kosher)\b` → dietary
  2. `\b(tax|receipts?|charit\w*)\b` → no tax receipts
  3. `(outside ontario|out of province|out-of-province|\bbc\b|british columbia|alberta|quebec|québec|manitoba|nova scotia|grandparents?|another province)` → Ontario-only
  4. `\b(schools?|principal|school board|tdsb|tcdsb|ddsb|dcdsb|parent council|ppm)\b` → school rules
  5. `\b(arena|rink|drop|field|hall|studio|miss(es|ed)?|can'?t make)\b` → team drop
  6. `(how many orders|orders (do|would|will) we need|\bgoal\b|\btarget\b|\braise\b)` → goal math
  7. `\b(up ?front|pre-?buy|cash|cheque|e-?transfer|payout|get paid|paid out|handle (the )?money|collect (the )?money)\b` → money handling
  8. `\b(perks?|talk|coach|raffle|prize|bonus|team link|after the drop)\b` → perks
  9. `\b(jerky|meat sticks?|pepperoni|snacks?|hand.?sell|door.?to.?door)\b` → jerky
  10. `\b(earn\w*|share|percent\w*|commission|how much|rates?|keep)\b` → rates
  The reply text for each is in the structured output (tested: each suggestion routes to the intended rule).

### Product ids to use (from `site/assets/catalog.js`)
- Packs and boxes: `chicken-breast-portioned-4-5-6-8-oz-box-broken-down-and-pkg-in-vacuum-bags` (6oz variant, $92), `kids-favourite-combo-special`, `summer-bbq-box-special`
- Game-Week Meal Pack: `pre-set-meal-teriyaki-chicken-breast-green-beans-basmati-white`, `chicken-broccoli-sweet-potato-fries` (4 oz), `jerk-chicken-broccoli-sweet-potato-chunks` (4 oz), `turkey-spinach-white-rice` (4 oz), `copy-of-feta-omelette-cups-cooked-portioned-2-pkg`
- Add-ons: `beef-chilli`, `soup-chicken-lemon-soup`, `spinach-feta-egg-wrap`, `beef-souvlaki-wrap` (Chicken Souvlaki Wrap), `chicken-breast-marinated-korean-4kg` (Korean BBQ 6oz case), `new-york-striploin` (Case 8 x 8-9oz, $110), `chicken-souvlaki-no-salt`
- Tasting tray reference: `chicken-breast-souvlaki`
- Two extra real items from `research/jw-catalog.json` (copy exactly; define locally):
  - `chicken-burgers-1` · "Premium Chicken Burgers — 25 Pack (6 oz each)" · $35.50 · img `https://cdn.shopify.com/s/files/1/1156/0176/files/chicken-burger-on-cutting-board.png?v=1782841639&width=600` · url `https://www.jwfoods.com/products/chicken-burgers-1`
  - `ground-beef-10lb-bulk-mix-special` · "GROUND BEEF - BULK MIX SPECIAL - 5lb" (show as "Ground Beef Bulk Mix, 5 lb") · $40.00 · img `https://cdn.shopify.com/s/files/1/1156/0176/products/GROUNDPORK.jpg?v=1613490076&width=600` · url `https://www.jwfoods.com/products/ground-beef-10lb-bulk-mix-special`

### Concept products (label each "Concept")
| Concept | Price | Basis |
|---|---|---|
| Team Freezer Pack | $167.50 | Premium Chicken Burgers 25 × 6 oz $35.50 + Case of Portioned Chicken Breast 4 kg (6 oz) $92 + Ground Beef Bulk Mix 5 lb $40, at J&W list prices. Group share 12% = $20.10 |
| Game-Week Meal Pack | $122.40 | 3 × Teriyaki Chicken, Green Beans & Rice 4 oz $9.99 + 3 × Tenders, Broccoli & Sweet Potato 4 oz $9.99 + 2 × Jerk Chicken, Green Beans & Sweet Potato 4 oz $12.99 + 2 × Turkey, Spinach & Rice 4 oz $12.99 + 2 × Egg White Bites, Spinach & Feta $5.25. Group share 20% = $24.48 |
| Group share rates | 20% / 12% / 5% | 20% on Meal Butler cooked items (45% margin leaves about 25%), 12% on raw boxes and cases (30% leaves about 18%), 5% on team-link orders for 6 months after the drop |
| Team drop | Free, no minimum | One stop on the existing route day replaces 25+ home stops at $8–14 each (market-benchmarks.md §8); about $67 of van and packer time per drop |
| Raffle box | Free at $3,000 in campaign sales | J&W's Long Weekend Box ($199); about $139 at cost (70%, ESTIMATE) |
| "Fuel for Game Day" talk | Free at $1,500 in campaign sales | 1.5 h of staff time + a tasting tray of 10 × Chicken Breast Souvlaki 4 oz ($4.62 each, $46.20 retail, about $25 at cost) ≈ $70 |
| Welcome offer | $10 off a first regular order of $100+ within 60 days | Cost about $10 × 25% redemption per new household |
| Team Fuel Jerky | Not priced, in development | To be priced from raw cost after yield and shelf-life testing, e.g. AAA Flank Steak bulk 12–13 lb $240 (≈ $18.80/lb) or Boneless Chicken Breast bulk 55 lb $350 (≈ $6.36/lb). Not orderable |

### Build notes
- Share map for the page (id → price → share): Freezer Pack $167.50 → $20.10 · Game-Week $122.40 → $24.48 · Kids Combo $95 → $11.40 · Long Weekend $199 → $23.88 · Beef Chili $12 → $2.40 · Lemon Chicken Rice Soup $8.99 → $1.80 · Egg White Bites $5.25 → $1.05 · Breakfast Wrap $5.99 → $1.20 · Chicken Souvlaki Wrap $5.99 → $1.20 · Marinated Chicken Breast Case $100 → $12.00 · NY Striploin case $110 → $13.20 · No-Salt Souvlaki Case $95 → $11.40. Share = round(price × rate, 2), shown "$20.10 to the Snowhawks".
- Concept packs go in `JWC.cart` as one line each, e.g. `{ id: 'p7-freezer-pack', name: 'Team Freezer Pack (Concept)', variant: 'Snowhawks fundraiser', price: 167.50, qty, img, note: 'For Maya R. #14 · $20.10 to the team' }`.
- Team state (raised, orders, shout-out counts) lives in `JWC.store('p7-team')`, starting from $456.12 / 22 / Ethan 4, Maya 3, Arjun 3. On `jwc:order` with `proto === 7`, add the share computed from the order's items using the share map. "Reset demo" restores the start values.
- The progress bar animates width over 900 ms and counts up the dollar figure; respect `prefers-reduced-motion`.
- All forms say "Demo: nothing is sent." No real payment fields. Macros carry "est.".
- No horizontal scroll at 375px; team-view tables become stacked cards under 640px.

---

## Sources
- Halenda's Fundraising home: https://halendasfundraising.com/
- About the program (two modes, 50–56%, school compliance): https://halendasfundraising.com/about-halendas-fundraising/
- Purchase page (calculator, tier table, $25 a bag, $18 a case shipping): https://halendasfundraising.com/purchase/
- Pepperoni Stix case prices ($300 / $288 / $273 / $261): https://halendasfundraising.com/product/halendas-pepperoni-stix/
- FAQ (case contents, pick-up Oshawa and Etobicoke, shelf life): https://halendasfundraising.com/fundraising-faqs/
- Six million meat sticks (start June 27, 2013; post Nov 6, 2025): https://halendasfundraising.com/fundraising-resources/celebrating-six-million-meat-sticks-sold/
- Dance studio success story ($10,300): https://halendasfundraising.com/fundraising-resources/dance-fundraising-success-story/
- Youth sports success story (8 cases, $1,536): https://halendasfundraising.com/fundraising-resources/youth-sports-fundraising-success-story-paige/
- Halenda's store locations: https://www.halendas.com/halendas-locations/
- Halenda's Hibernator freezer packs: https://www.halendas.com/products/meat-freezer-packs/
- Rowe Farms meat fundraisers (donation shown under each price): https://rowefarmsonline.ca/pages/meat-fundraisers
- GTHL 2025–26 team entries (493 teams, 54 clubs): https://gthlcanada.com/article/gthl-announces-team-entries-for-2025-2026-season
- J&W delivery routes and fees: https://www.jwfoods.com/pages/home
- J&W story: https://www.jwfoods.com/pages/about-us
- J&W products used: https://www.jwfoods.com/products/chicken-burgers-1 · https://www.jwfoods.com/products/chicken-breast-portioned-4-5-6-8-oz-box-broken-down-and-pkg-in-vacuum-bags · https://www.jwfoods.com/products/ground-beef-10lb-bulk-mix-special · https://www.jwfoods.com/products/kids-favourite-combo-special · https://www.jwfoods.com/products/summer-bbq-box-special · https://www.jwfoods.com/products/beef-chilli
- J&W Google rating 4.8★ / 611: https://yably.ca/reviews/toronto/j-w-foods-2201-brimley-road
- CFIA, activities that need a federal licence (interprovincial trade): https://inspection.canada.ca/en/food-licences/food-business-activities
- Local research files: competitor-07.md, selection.json (pick 7), jw-facts.md, jw-audit.md, model-assumptions.md, market-benchmarks.md (§5, §6b, §8), competitors-gta-meat-grocery.md (§4.2, §4.6, §5), ai-agents-research.md (Agents 3, 5, 6, 12, 13), site/assets/catalog.js, jw-catalog.json

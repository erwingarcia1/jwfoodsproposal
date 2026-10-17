# Play 4: J&W at Work

**One line:** A workplace meal perk for GTA employers. The company covers part or all of each Meal Butler meal, staff pre-order by the Sunday cut-off, and J&W drops one order of named bags at the site on a route it already drives. Sites with 75+ staff on site also get a loaned freezer, restocked weekly.

**Modelled on:** WeCook for Business (Montreal, sells in Ontario). We borrow ideas only, never its copy, logos or photos.

**Why it makes money:** One dock drop of 50+ prepaid meals, on a route the J&W van already drives, is the cheapest and highest-margin order J&W can take. The employer subsidy keeps staff ordering every week.

**Headline numbers (estimates):**

| | Low | Mid | High |
|---|---|---|---|
| Year 1 added revenue (Nov 2026 to Oct 2027, live from Jan 2027) | $68K | **$162K** | $323K |
| Run-rate, year 2 | | **$622K** | |
| Gross margin | | **40%** | |
| JW's running cost, year 1 | | ~$54.5K (incl. $10.8K freezers) | |

Start month: **3 (January 2027)**. November and December go to the build, labels and three friendly pilots. HR wellness budgets reset in January.

---

## 1. What WeCook for Business proves

Verified in `competitor-04.md` (checked Oct 16 2026):

- WeCook delivers about **90,000 meals a week** with **nearly 400 staff** ([Retail Insider, Aug 26 2025](https://retail-insider.com/?p=177907)). Trustpilot shows **4.8 from 6,584 reviews** ([Trustpilot](https://www.trustpilot.com/review/wecookmeals.ca)).
- On the B2B platform the CEO puts meals at **"$11.75-ish"**, against **$20-25** for traditional catering. Employers can **"contribute $1 per meal, or 100%"**. The program fits **20 to 500 employees**, and larger firms get on-site fridges (Retail Insider). The article is 14 months old, but the B2B page and dashboard copy were live on Oct 16 2026.
- Consumer plans cost **$11.99-15.49 a meal**, with a 6-meal minimum ([WeCook plans API](https://www.wecookmeals.ca/api/plans)).
- Mechanics behind the dashboard (from WeCook's own UI strings):
  - an allowance engine with four types ($ per employee, $ on meals only, N meals per employee, $ per meal up to a cap) and caps;
  - invites locked to the company email domain;
  - a weekly joint order that cancels itself when nobody orders;
  - a live order roll-up;
  - a receipt split into "covered by the company" and "paid by the employee(s)";
  - a company-wide volume price tier.
- Its B2B social proof is a set of small Quebec firms. It ships from Quebec through couriers and has no GTA plant.

## 2. What J&W changes (the mechanism)

1. **The employer picks a perk.** The options are dollars off each meal ($2 up to the full price), lunches covered each week (1 to 5 per person), or everything covered up to a weekly cap. HR can add an optional monthly budget cap. The company's share is drawn from a **prepaid company wallet** that is topped up monthly by card or EFT, so J&W carries no receivables.
2. **Staff join with their work email** and order from a 20-item **At Work menu** of real Meal Butler items by J&W's existing Sunday cut-off. Examples:
   - Teriyaki Chicken, Green Beans & Rice, $9.99
   - Tenders, Broccoli & Sweet Potato, 4 oz, $9.99
   - Tilapia, Asparagus & Brown Rice, 4 oz, $11.99
   - Jerk Chicken, Green Beans & Sweet Potato, 4 oz, $12.99
   - Salmon, Brussels & Quinoa, 4 oz, $12.99
   - Souvlaki, Broccoli & Greek Potatoes, 4 oz, $13.99
   - Chicken Souvlaki Wrap, $5.99
   - Chicken Chili, $9.99
   - Egg White Bites, Spinach & Feta, $5.25
   - Steel Cut Oats, $4.40
3. **Work pricing (Concept).** This is a company-wide volume tier, borrowed as an idea from WeCook:
   - under 40 items a week: published prices;
   - **40-99 items: 5% off every item**;
   - **100+ items: 10% off**. A $12.99 pre-set meal then costs $11.69 before the allowance.
4. **One drop on an existing route.** Each week's orders go out as one stop of sealed, **named bags** on the route day already serving that city:
   - Tuesday: Durham
   - Wednesday: Toronto, Scarborough, North York, Etobicoke, Mississauga
   - Thursday: Halton and Hamilton
   - Friday: York and Peel

   Delivery is **free when the week's team order is $250+**. Below that, the usual $20 route fee applies. If nobody orders in a week, nothing ships and nothing is billed.
5. **The At Work Freezer (Concept).** Sites with 75+ staff on site and $250+ a week in combined orders get a **loaned glass-door freezer**:
   - J&W restocks it on the route day, and the production agent sets par levels per site.
   - Staff scan a QR code and pay with their allowance or a card.
   - J&W counts stock at each visit. If unpaid items pass **3%** of what was stocked, the company covers the difference at work prices.

   This suits hospitals, care homes, warehouses and plants, where night shifts and closed cafeterias are the norm.
6. **Team Table packs (Concept).** These are priced at the sum of J&W's published prices and ride the same drop:
   - **Lunch & Learn Pack for 12, $147.88**: 4 Souvlaki, Broccoli & Greek Potatoes, 4 Teriyaki Chicken, Green Beans & Rice, and 4 Salmon, Brussels & Quinoa.
   - **Breakfast Meeting Pack for 12, $115.80**: 12 Egg White Bites, Spinach & Feta and 12 Steel Cut Oats.
   - **Team BBQ Pack for about 25, $134.95**: a No-Salt Chicken Souvlaki Case (5 kg, about 50 raw skewers) at $95, Tzatziki 1.5 L at $15, and 5 packs of Whole Grain Greek Pita at $4.99 each. This is the butcher advantage WeCook cannot match.
7. **HR gets:**
   - one monthly split invoice;
   - a monthly report covering participation, meals, company and staff spend, estimated protein per lunch, and the per-person company-paid total for payroll;
   - a free quarterly 30-minute lunch-and-learn for accounts ordering 40+ items a week;
   - a step-challenge prize: a $60 Meal Butler credit each quarter (Concept).
8. **Sales are assisted, not self-serve.** A lead form with a "Who are the meals for?" question routes each lead:
   - gyms and clinics that resell go to Play 2;
   - gifts go to Play 5;
   - teams and schools go to Play 7;
   - "just me" goes to Play 1.

   The B2B prospecting agent drafts outreach to employers along the route corridors. Lucas or the owner run free tastings (8 pre-set meals, $99.92 at published prices, about $55 food cost).

### Weekly cycle

| Day | What happens |
|---|---|
| Monday | Next week's menu opens. The previous week's company share is posted to the wallet. |
| Thursday | The order desk agent drafts reminders for staff who opted in and have not ordered. Staff approve the batch. |
| Sunday 11:59 pm | Cut-off (J&W's existing rule). Weeks with no orders cancel automatically. |
| Monday-Tuesday | Cook, portion and pack named bags (J&W's existing 2-3 business-day fulfilment). Freezer pars are set. |
| Tue / Wed / Thu / Fri | Dock drop and freezer restock on the city's route day. The site contact gets an ETA window. |

### Why J&W wins against WeCook here

- **Frozen, vacuum-sealed meals** suit an unattended office freezer. There is no use-by pressure and no Friday waste. WeCook's fresh trays need fridges and quick turnover.
- **The Scarborough plant and its own routes.** The Scarborough, Markham, North York, Vaughan and Mississauga business parks sit on the Wednesday and Friday runs. WeCook ships from Quebec by courier.
- **Prices at or below WeCook's.** J&W's pre-set meals cost $9.99-13.99 for 4 oz, against WeCook's $11.99-15.49, with no plan minimum per employee.
- **Macro-exact à la carte portions**, plus a promise of no added salt, sugar or oil. WeCook's sample bowl carries 795-1,015 mg sodium and canola oil (`competitor-04.md` section 6). This goes in the business case only. Customer copy never names a competitor.
- **A butcher behind the meals.** The same account can buy a BBQ pack, or holiday boxes through Play 5 (counted there, not here).

## 3. The math

All figures in CAD and all are ESTIMATES. Shared assumptions come from `model-assumptions.md`: cooked-meal margin 45% less the tier discount, incrementality 0.85 (the top of 0.75-0.85, because this is a new buyer), route cost $8-14 a stop, and 48 order weeks a year.

**Unit economics of one account at steady state.** A typical site has 100-140 staff on site, three on-site days a week and a $3-4 allowance.
- 25-30% of on-site staff order each week, at 2.2 items each, which gives **about 55 items a week**.
- **Average net item price: about $10.00.**
  - Lunches are 75% of items, at an average published 4 oz price of $12.32 across the 9 menu meals.
  - Breakfast items are 25%, at about $5.
  - That gives a $10.49 list mix, less about 5% for the volume tier.
- One account is worth about $550 a week, or about $26.4K a year.
- At 40% margin, the gross profit is about $10.6K a year. The added route cost is about $530 a year (48 stops × $11).

**Year 1 (Nov 2026 to Oct 2027, live from Jan 2027), mid case:**
- Team orders:
  - Live accounts ramp from 3 in Jan to 16 in Oct (3, 4, 6, 8, 10, 11, 12, 12, 14, 16), which is **96 account-months**.
  - 96 account-months × 4 order weeks × 40 items a week (new accounts start at about half volume) × $10.00 = **$153,600**.
- Freezers: installed from Mar, ramping from 1 to 6 (1, 2, 3, 4, 4, 5, 5, 6), which is **30 freezer-months**. 30 × 4.2 weeks × $250 a week = **$31,500**.
- Team Table packs: 96 account-months × 0.4 packs × $150 = **$5,760**.
- Gross: $190,860 × 0.85 incrementality = **$162,231, about $162K**.

**Low ($68K):**
- 9 accounts by Oct, which is 57 account-months, at 30 items a week: 57 × 4 × 30 × $10 = $68,400.
- 3 freezers, which is 12 freezer-months: 12 × 4.2 × $200 = $10,080.
- Packs: 57 × 0.2 × $150 = $1,710.
- Total: $80,190 × 0.85 = $68,162.

**High ($323K):**
- 24 accounts by Oct, which is 145 account-months, at 50 items a week and $10.50: 145 × 4 × 50 × $10.50 = $304,500.
- 10 freezers, which is 50 freezer-months: 50 × 4.2 × $300 = $63,000.
- Packs: 145 × 0.55 × $150 = $11,963.
- Total: $379,463 × 0.85 = $322,543.

**Run-rate, year 2 (Nov 2027 to Oct 2028):**
- 22 average live accounts (16 rising to about 28) × 55 items × $10.00 × 48 weeks = $580,800.
- 9 freezers × $300 × 50 weeks = $135,000.
- 22 accounts × 5 packs × $150 = $16,500.
- Gross: $732,300 × 0.85 = **$622,455, about $622K**.

**Gross profit and JW's own costs:**
- Year 1:
  - Gross profit is about $65K (40% of $162K).
  - Costs are about $54.5K: $13.8K setup plus 11 × $3.7K a month.
  - That is **roughly break-even**, and the freezers are reusable capex.
- Year 2:
  - Gross profit is about $249K.
  - Running costs are about $80K: a coordinator at 20 h a week, more packing hours, about 22 extra stops a week and 3 more freezers.
  - That leaves **about $170K contribution** before Minastech's fee.

**Sanity checks:**
- Year 1 mid is about 6.5% of J&W's ~$2.5M mid-case revenue. The run-rate is about 25%. Both sit within the $60-450K year-1 and below-$900K run-rate guardrails.
- 28 live accounts by Oct 2028 is about **0.2%** of the ~11-14K GTA sites with 50+ staff ([York Region factsheet](https://yorklink.ca/2025-york-region-business-counts-factsheet/), `market-benchmarks.md` section 6a). Toronto alone has ~810K office jobs ([Toronto Employment Survey 2025](https://www.toronto.ca/wp-content/uploads/2025/11/97af-CityPlanning-Toronto-Employment-Survey-Two-Pager-Summary-2025.pdf)).
- The benchmark in `market-benchmarks.md` section 11 (40 offices × 25 staff × 2 meals × $13 × 48 ≈ $1.25M) is about twice this plan. The plan assumes lower prices and fewer accounts.
- Year-2 volume is about **1,470 extra items a week** (about 1,210 pre-ordered plus about 260 from freezers). That is likely +1 cook/packer FTE. Plant headroom must be confirmed with J&W (`market-benchmarks.md` section 12).
- Selection planning midpoint: about $0.6M run-rate. The selection note gave $0.2-0.3M for year 1. This plan is more conservative because of the January start.

**Not counted here, to avoid double counting:** gifts bought by the same employers (Play 5), resale by gyms and clinics (Play 2), team and school fundraisers (Play 7), and staff who later subscribe at home (Plays 1 and 6).

## 4. Costs to J&W (excluding Minastech's fee)

**Setup: about $13,800.**
- 6 glass-door merchandiser freezers at about $1,800 each: $10,800. This is an estimate; plan on $1,500-2,500 each.
- QR signage, freezer wraps and printed menus: $1,500.
- Pilot agreement template and an insurance check for loaned equipment: $1,500.

**Monthly: about $3,700 (year-1 average).**
- Part-time At Work coordinator, 12 h a week × about $28/h loaded: $1,450.
- Named-bag pick, pack and label labour, about 0.75 h per account-week × $24/h: $745.
- Extra stops on existing routes, about 10 a week × $11, plus freezer restocks: $475.
- Software and AI tokens (prospecting tool share, B2B or wallet app, Claude tokens): $300.
- Paid search and LinkedIn for "office lunch program" terms in the 416/905: $400.
- Tasting boxes (4 a month × about $55 food cost) and step-challenge prizes: $330.

**Year 2:** about $80K a year, as volume grows (see section 3).

## 5. Who does the work

- **Lucas or the owner:** 6 h a week on tastings, HR calls and pilot check-ins.
- **At Work coordinator (part-time):** 12 h a week in year 1, rising to 20 h in year 2. Covers onboarding, wallet top-ups, freezer counts, invoices and approving agent drafts.
- **Kitchen:** 4-8 extra packing hours a week for named bags, part of a second cook/pack shift by year 2.
- **Drivers:** 10-15 minutes per extra dock drop on existing routes, plus a 20-minute freezer restock.
- **Minastech:** builds the portal, sets up the agents and trains the team (fee separate).

## 6. KPIs

| KPI | Target |
|---|---|
| Employer accounts live | 16 by Oct 2027; 28 by Oct 2028 |
| Weekly participation (on-site staff who order) | 25-30% |
| Items per account per week | 40 in year 1 (ramp), 55 at steady state |
| Average net item price | about $10.00 |
| Tasting to pilot / pilot to paid | 40% / 70% |
| Account retention at 6 months | 85%+ |
| Freezer sales per freezer | $250 a week in year 1, $300 in year 2; shrink under 3% |
| Gross margin | 40%+ |
| Added time per dock drop | under 15 minutes (under $14 a stop) |

## 7. AI agents this play needs

| Agent | Job here | On screen in the prototype |
|---|---|---|
| **B2B prospecting and account agent** | Builds lists of GTA employers with 50+ staff along J&W's route corridors (Scarborough, Markham, North York, Vaughan, Mississauga). Drafts CASL-compliant intro emails to HR, books tastings, and watches live accounts for falling participation, with save-offer suggestions. | Team view: the drafted intro email to Maple Ridge Packaging, the Don Mills Design Co. save-offer and the pipeline board, all waiting for approval |
| **At Work order desk agent** (new) | Runs each employer's weekly order. It applies allowances and caps, drafts Thursday reminders for opted-in staff, closes at the Sunday cut-off, cancels empty weeks, rolls picks into one named-bag pick list per site, and drafts the split company/staff invoice. | Staff app allowance meter and confirmation; team view reminder-SMS approval and the Northline split invoice |
| **Production forecast and prep-sheet agent** | Adds At Work volume to Monday's cook, portion and pack plan, and sets freezer par levels per site from sell-through | Team view cook-plan change (648 items) and the Milliken freezer par change |
| **Route and delivery experience agent** | Slots dock drops and freezer restocks into the existing Tue-Fri routes and texts each site contact an ETA window | Team view route impact (Wednesday: 7 drops, about +52 min) |
| **Nutrition data and label agent** | Drafts the full prepackaged labels needed for meals sold from a workplace freezer: ingredients, allergens, Nutrition Facts, the front-of-pack symbol and from-frozen heating times. Also supplies the protein figures in the HR report. A labelling consultant approves. | Protein badges (est.) on menu cards; average protein in the HR report |
| **Butler Concierge 24/7 support and sales chat** | Answers HR and staff questions on pricing, route day, allergens, the freezer and the taxable-benefit caveat. Hands allergies and complaints to staff. | The "At Work Desk" chat on this page |

Human checkpoints:
- Every outbound email or SMS, every price or allowance change, and every freezer par change is approved by J&W staff.
- The owner approves any pricing outside the published tiers.

## 8. Assumptions

- Launch in January 2027 with 3 friendly pilots. November and December go to the build, labels and recruiting.
- About 5 tastings a month. 40% become pilots and 70% of pilots convert, so about 1.4 net new accounts a month after a little churn.
- An average account has 100-140 staff on site, 25-30% weekly participation and 2.2 items per person on 3 on-site days, which gives 55 items a week at steady state. New accounts start at about half that.
- The average item is about $10.00 net: 75% lunches (avg $12.32 published) and 25% breakfast (about $5), less about 5% for the volume tier.
- 48 order weeks a year (holidays and summer skips).
- About 40% of accounts qualify for a freezer, at about $1,800 each. Sales are $250 a week in year 1 and $300 in year 2. The low end of the $300-900 smart-fridge benchmark is used because the menu is frozen.
- Gross margin is 40%: the cooked 45%, less the tier discount, shrink and named-bag packaging.
- Incrementality is 0.85. Some staff already buy J&W at home.
- Drops ride existing routes at about $8-14 a stop. Delivery is free on $250+ weeks.
- The company share is prepaid through a wallet, so there are no receivables.
- J&W confirms microwave times from frozen for each At Work item before launch. The current guidance is to thaw overnight, then heat 60-90 seconds.

## 9. Risks

- **A slow B2B sales cycle.** HR budgets are set in Q4 and Q1. The mitigations are free-delivery pilots, a January launch and a route-day pitch ("our truck is already in Markham on Fridays").
- **Labels gate the freezer.** Meals sold away from J&W's store need full prepackaged labels: ingredients, allergens, Nutrition Facts, and the front-of-pack symbol, which has been mandatory since Jan 2026. Budget a labelling consultant, with the label agent drafting.
- **Claims must match the labels.** Some jwfoods.com ingredient lists conflict with the site-wide promise of no salt, sugar or added oil. Chicken Breast Souvlaki, for example, lists salt and oil. Reconcile these before pitching clinics and hospitals.
- **Participation fades after the first month.** The mitigations are menu rotation, Thursday reminders, allowance nudges from the account agent and the quarterly lunch-and-learn.
- **Hybrid work cuts on-site days.** The frozen format and take-home help, but volume may sit at the low end.
- **Taxable benefit.** Subsidised meals can be a taxable benefit for staff. J&W must not give tax advice. The portal reports each person's company-paid amount for payroll.
- **Plant capacity.** About 1,470 extra items a week by year 2 may need a second cook/pack shift.
- **Freezer shrink or damage** under honour-system QR pay. The mitigations are the 3% clause, weekly counts and a lock option for public-facing sites.
- **Competitive response.** WeCook already sells B2B in Ontario. J&W's local routes, the freezer format and the butcher range are the moat.
- **Founder bandwidth.** Tastings depend on Bill or Lucas. Protect 6 h a week.

## 10. How this stays distinct from the other six plays

| Play | Buyer | Difference |
|---|---|---|
| 2. Pro Partner Portal | Gyms and clinics that **resell** to members | Here the **employer** funds meals for its own staff. Nothing is resold. |
| 5. Corporate Gift Studio | Employers buying **gifts** | A gift order from an At Work account is counted in Play 5 only |
| 1 and 6. Goal Plan Builder, AI Coach | Individuals at home | Staff who later subscribe at home count there |
| 7. Team Fuel | Teams and schools raising money | The lead form routes them to Play 7 |

---

## 11. Prototype spec (for the front-end builder)

**File:** `site/prototypes/04-jw-at-work.html`. **Init:** `JWC.init({ n: 4, teamNote: 'The JW team sees every employer account, this week's team orders rolled into the cook plan and routes, and AI-drafted outreach, reminders and invoices waiting for approval.', chat: {...} })`.

**Concept:** an HR manager at a GTA employer lands on the page, designs a meal perk with live numbers, previews the staff app their team would use, tries the night-shift freezer, and books a tasting or starts a pilot. In JW team view, the same actions appear as leads, pilots and orders, alongside a week of sample accounts, AI-drafted outreach and reminders waiting for approval, the cook-plan and route impact, and a split invoice.

**The wow moment:** the **Perk Designer**. HR drags the allowance slider, and a real meal card (Jerk Chicken, Green Beans & Sweet Potato, $12.99) splits live into a sky-blue "Company covers $3.00" bar and a navy "Staff pay $9.34" bar. The weekly lunches, monthly cost and pricing tier update as the slider moves, and a badge animates when the team reaches Team or Site pricing. One tap on "See it in the staff app" carries the settings into the phone preview, which immediately says "Northline covers $3.00 off each meal".

### Design

- **Inspired by** WeCook for Business, ideas only:
  - a lead form placed as the hero;
  - an auto-scrolling benefit marquee;
  - three numbered set-up cards;
  - a 2×2 grid of objections;
  - round protein stickers on meal cards.

  These are reinterpreted with J&W's navy laurel, a frost-blue "freezer" motif and Meal Butler's slate purple. The look is crisp, premium and calm, not WeCook green.
- **Palette:**

  | Hex | Role |
  |---|---|
  | `#154D8E` | Primary (JW laurel navy): buttons, H1/H2, "Staff pay" bar |
  | `#0F1E33` | Ink: body text and dark bands |
  | `#7FB3D5` | Sky (Meal Butler): "Company covers" bar, highlights, focus rings (use as a fill, never as text on white) |
  | `#EAF3FA` | Frost: freezer section and app background |
  | `#5B5A8C` | Slate purple (Meal Butler): tier badges, HR report, Concept tags, team-view accents |
  | `#F6F1E7` | Oat: alternating section bands |
  | `#E3A33B` | Saffron: pilot-offer pill and low-stock badges (ink text on top) |
  | `#2E7D6B` | Teal: success ticks |
  | `#5A6472` | Muted text |
  | `#FFFFFF` | Paper |

- **Fonts (Google):** **Bricolage Grotesque** 600/700/800 for display, and **Inter** 400/500/600 for body. Use tabular numbers (`font-variant-numeric: tabular-nums`) in all money figures.
- **Layout:**
  - Mobile-first single column with a 16 px gutter.
  - Desktop (≥1024 px):
    - the hero splits 55/45, with the form card on the right;
    - steps sit in 3 columns;
    - the designer has controls on the left and a sticky result card on the right;
    - the staff app sits in a phone frame in the centre, with callouts either side;
    - packs sit in 3 columns, and Fair questions in a 2×2 grid.
  - Under 480 px, the phone frame becomes a full-width card without device chrome.
  - Cards have a 16 px radius and a soft navy shadow. Buttons have a 10 px radius and are at least 44 px tall.
- **Tone:** neighbourly, plain and specific. Short sentences, Canadian spelling, no hype words.

### Sections in order (customer view)

1. **Sticky header.**
   - A navy laurel badge reading "J&W", the wordmark **"J&W at Work"**, and a small sub-label "from J&W Meal Butler".
   - Nav: How it works · Menu · Freezer · Pricing · For HR. On mobile these become horizontal scroll chips.
   - Buttons: "See the staff app" (ghost) and **"Book a tasting"** (navy).
2. **Hero**
   - Eyebrow: "Workplace meals · Scarborough, since 1995"
   - H1: **"Lunch at work, cooked by your butcher."**
   - Sub: "J&W at Work is a meal perk for GTA teams. You decide what the company covers. Your staff pick their meals by Sunday. We bring the whole order to one door on our regular route, packed and labelled by name."
   - Saffron pill: "Pilot offer: a free tasting and 4 weeks of free delivery for our first 10 employers (Concept)"
   - Proof chips: "4.8★ on Google · 611 reviews" · "Ontario-inspected plant since 2008" · "Frozen and sealed, so nothing spoils"
   - **Lead form card**, titled "Book a free team tasting"
     - Note: "We bring 8 meals for your team to try, on our route day. Demo: nothing is sent."
     - Fields:
       - First name*, Last name*, Work email*, Company*, Phone
       - **"Who are the meals for?"**: Our employees (default) / Members or patients at a gym or clinic we run / A sports team or school group / Gifts for clients or staff / Just me
       - Staff on site: 20-49 / 50-99 / 100-249 / 250+
       - Site city: `JWC.cities()` + Other
       - Notes: 200-character maximum with a live counter
       - Checkbox: "We already order from J&W"
     - When a city is picked, a live hint shows, for example: "Good news: Markham is on our Friday route (GTA 4). Your team order would arrive Fridays."
     - Routing notes for non-employee choices: gym or clinic → "That's our Pro Partner Portal. See prototype 2"; team or school → prototype 7; gifts → prototype 5; just me → prototype 1. Each links to that prototype.
     - Button: **"Book my tasting"**
3. **Benefit marquee.** It auto-scrolls, pauses on hover or focus, and shows as a static wrap when the user prefers reduced motion. Items:
   - "Less than a food-court lunch"
   - "Frozen, so nothing goes to waste"
   - "Protein printed on every meal"
   - "One drop. One invoice."
   - "Skip a week, nothing ships"
   - "Ontario chicken, no hormones or antibiotics"
   - "A freezer on loan for 75+ staff"
4. **How it works.** H2: **"Set up in an afternoon. Runs itself after that."**
   - **1 · "Choose what the company covers."** "Take $2 to $13 off each meal, cover a few lunches a week, or pay for all of it. Set a cap per person and a monthly budget, so there are no surprises."
   - **2 · "Invite your team."** "Staff join with their work email. Each week they pick meals by Sunday night. If they forget, a friendly reminder goes out on Thursday."
   - **3 · "We bring it to one door."** "Your order rides our regular Wednesday or Friday route. Each person's meals come in one sealed, named bag. One monthly invoice shows what the company paid and what staff paid."
   - Footnote: "If nobody orders in a week, nothing ships and you pay nothing."
5. **Perk Designer (the wow).** H2: **"Design your perk."** Sub: "Move the sliders. The numbers change as you go. They are estimates to help you plan, not a quote."
   - Controls:
     - Staff on site: slider 20-500, default 100.
     - Days on site each week: segmented 1-5, default 3.
     - What the company covers: segmented "$ off each meal" (slider $0-12, step $0.50, default $3) / "Lunches covered" (1-5 per person per week, default 2) / "Everything" (cap 1-5 a week, default 3).
     - Optional monthly budget cap: toggle plus $ input.
   - Result card:
     - The Jerk Chicken meal card: published $12.99, work price at the tier, and the split bar.
     - "Staff likely to order each week (est.)"
     - "Lunches a week (est.)"
     - Tier badge: Starter / Team, 5% off / Site, 10% off. When the tier changes, show "Team pricing reached: 5% off for everyone".
     - "Company cost per month (est.)"
     - "Staff pay per lunch, on average (est.)"
     - "Fully covered, a lunch here costs the company about $11.70, compared with $20 to $25 a head for typical office catering (est.)"
     - If a budget cap is set below the cost: "Your cap covers about N weeks a month at this level. After that, staff still order at work prices."
   - Buttons: **"Start a 4-week pilot with these settings"** · "See it in the staff app" · "Email this summary to a colleague" (opens a demo modal with a printable summary; nothing is sent).
   - **Formulas** (label every output "est."):
     - `avgLunch = 12.32` (average published 4 oz price of the 9 menu lunches)
     - `itemsPerPerson = 0.6 × days + 0.4`
     - **$ off X:**
       - `p = min(0.60, 0.15 + 0.035 × X)`
       - `lunches = round(N × p × itemsPerPerson)`
       - `companyWeek = lunches × min(X, workPrice)`
     - **Lunches covered K:**
       - `p = min(0.65, 0.35 + 0.06 × K)`
       - `lunches = round(N × p × max(itemsPerPerson, K))`
       - `companyWeek = N × p × K × workPrice`
     - **Everything, cap C:**
       - `p = 0.60`
       - `lunches = round(N × p × min(C, days))`
       - `companyWeek = lunches × workPrice`
     - **Tier:** lunches <40 → 0%; 40-99 → 5%; 100+ → 10%. `workPrice = avgLunch × (1 − tier)`.
     - `monthly = companyWeek × 4.33`, capped by the budget if one is set
     - `staffPerLunch = workPrice − companyWeek / lunches`
     - Defaults check: N 100, 3 days, $3 → p 25.5%, 56 lunches, Team tier, about $168 a week, **about $727 a month**, staff pay about $8.70 on average.
6. **Staff app preview.** H2: **"What your team sees."** Sub: "A short weekly menu on their phone. Their allowance comes off before they pay." Small note: "Sample company: Northline Logistics, Markham (fictional)."
   - Screen A, Join: "Join J&W at Work". "Use your work email to join your company's meal perk."
     - Email input and a "Send my sign-in link" button (demo).
     - Hint chip: "Try priya@northline.example".
     - Any other domain shows: "That email isn't on Northline's list. Use your @northline.example address, or ask HR to add you."
   - Screen B, Menu: "Hi Priya" and "Northline covers $3.00 off each meal, up to 5 a week". The amount follows the designer.
     - "Order by Sunday, Oct 18 at midnight · Arrives Friday, Oct 23 at the shipping office"
     - Tabs: Lunch / Breakfast / Wraps & soups
     - Each card shows the photo, the name, a round navy "est. 38 g protein" sticker, the published price struck through next to the work price, and "You pay $X" in bold, with +/- steppers.
     - Allowance meter: "3 of 5 covered this week".
   - Screen C, Review:
     - Rows: Meals (4) at the work price; "Northline covers −$12.00"; "You pay $34.51".
     - Pay by "Card on file · DEMO •••• 4242" or "Payroll deduction (if your company allows it)".
     - Toggle: "Repeat this order every week (skip any time)".
     - Button: **"Confirm my meals"**.
   - Screen D, Done:
     - "You're in Friday's Northline drop."
     - "Your bag will say PRIYA S. and sits on shelf 2 of the staff freezer."
     - "Thaw tomorrow's lunch in the fridge overnight, then heat 60 to 90 seconds."
     - Buttons: "Done" · "Edit until Sunday".
7. **The At Work Freezer.** H2: **"The At Work Freezer."** Sub: "For sites with 75 or more people on site, we lend you a glass-door freezer and keep it stocked. Good for night shifts, early starts and the days someone forgot to order."
   - Bullets:
     - "Free loan. We deliver it, plug it in and restock it on your route day."
     - "Staff scan the QR code, pick a meal and pay with their allowance or a card."
     - "We count stock at every visit. If unpaid items go over 3% of what we stocked, the company covers the difference at work prices."
     - "Frozen meals keep for months, so nothing is thrown out on Friday."
   - Interactive: "Try it: 2:10 am, night shift at a Scarborough care residence (sample)."
     - A CSS glass-door freezer with 3 shelves of product thumbnails and stock counts: Jerk Chicken ×6, Turkey, Spinach & Rice ×4, Salmon, Brussels & Quinoa ×3, Chicken Chili ×5, Egg White Bites ×8, Steel Cut Oats ×7.
     - Tapping an item opens a sheet with a mock QR. The choices are "Use my allowance ($3.00 off)" and "Pay the work price by card (demo)", followed by **"Pay $9.34"**.
     - Confirmation: "Paid. Enjoy your meal. 5 Jerk Chicken left." Stock decrements, and at 2 or fewer a saffron badge reads "Low: restock Wednesday".
   - Small print: "The site provides a standard outlet. The freezer loan terms are a Concept for discussion."
8. **Team Table packs.** H2: **"Feeding a meeting? Order a Team Table pack."** Sub: "For lunch-and-learns, all-hands and the summer BBQ. Packs ride the same route as your team order." Every card carries a Concept tag.
   - **Lunch & Learn Pack, 12 people, $147.88.** "4 Souvlaki, Broccoli & Greek Potatoes · 4 Teriyaki Chicken, Green Beans & Rice · 4 Salmon, Brussels & Quinoa. Name labels and a printed menu card." It has a mix editor with steppers that must total 12, choosing from 6 favourite lunches. The price recalculates at published prices.
   - **Breakfast Meeting Pack, 12 people, $115.80.** "12 Egg White Bites, Spinach & Feta · 12 Steel Cut Oats."
   - **Team BBQ Pack, about 25 people, $134.95.** "No-Salt Chicken Souvlaki Case (5 kg, about 50 skewers) · Tzatziki 1.5 L · 5 packs of Whole Grain Greek Pita. Raw skewers for your grill. Cook chicken to 74°C."
   - Buttons: "Add to cart" and **"Order this pack"**. "Order this pack" calls `JWC.checkout` with:
     - title "Team Table order"
     - city "Markham"
     - `extraRows: [{label:'At Work delivery credit (team order over $250)', amount:-20}]`
     - note "Rides with the Northline team order on Friday"
9. **For HR.** H2: **"A monthly report you can send upstairs."**
   - Sample report card, "Northline Logistics · October 2026 (sample)":
     - "Meals delivered: 470 (352 pre-ordered, 118 from the freezer)"
     - "On-site staff who ordered each week: 31%"
     - "Company covered: $1,410.00 · Staff paid: $3,434.88"
     - "Average protein per lunch: 36 g (est.)"
     - "Most ordered: Jerk Chicken, Green Beans & Sweet Potato"
     - "Freezer shrink: 1.2%"
   - Line: "Each person's company-paid total is listed for payroll. Ask your payroll provider how to treat it."
   - Add-ons:
     - "Quarterly lunch-and-learn: 30 minutes with our team on protein, portions and meal prep. Free for accounts ordering 40+ items a week."
     - "Step-challenge prize: a $60 Meal Butler credit for your winner each quarter (Concept)."
10. **Fair questions** (2×2). H2: **"Fair questions."**
    - "We don't have a kitchen." → "You need a microwave and some freezer space. Meals heat in 60 to 90 seconds once thawed. Sites with 75+ staff can borrow our freezer."
    - "Half the team is remote on Fridays." → "Meals are frozen, so they keep. Staff can take theirs home, and anyone can skip a week. No orders means no delivery and no bill."
    - "Healthy lunches are boring." → "Jerk chicken, Korean BBQ flank, Greek lemon souvlaki, teriyaki, honey garlic salmon. Our own marinades, cooked in our own plant."
    - "HR doesn't need another job." → "Staff order for themselves. You get one invoice and one short report a month. Reminders and order roll-ups are handled for you."
11. **Who it's for.** H2: **"Built for GTA workplaces on our routes."**
    - Tiles:
      - "Hospitals, clinics and care homes": "Night shifts and closed cafeterias. The freezer does the work."
      - "Warehouses, plants and distribution centres": "No food court nearby, early starts, big shifts."
      - "Offices and studios": "Hybrid teams on site two or three days a week. A lunch that brings people in."
      - "Property managers": "A tenant amenity for your towers. Tenants order, you choose the perk."
    - City lookup: "Is your site on our route?" with an input that uses `JWC.findCity` / `JWC.routesFor`. Example result: "Vaughan: Friday route (GTA 4)."
    - Route list:
      - Tue Durham
      - Wed Toronto, Scarborough, North York, East York, Etobicoke, Mississauga
      - Thu Oakville, Burlington, Hamilton, Milton
      - Fri Markham, Vaughan, Richmond Hill, Brampton, Newmarket, Aurora
12. **Pricing.** H2: **"Simple work pricing."** (Concept)

    | Your company's weekly order | Price for everyone | Included |
    |---|---|---|
    | Under 40 items | Our published prices | Free tasting, monthly report |
    | 40 to 99 items | 5% off every item | + quarterly lunch-and-learn |
    | 100 or more | 10% off every item | + a say in next month's menu |

    Notes:
    - "Free delivery to one door on any week over $250. Under $250, the regular $20 route fee applies."
    - "At Work Freezer on loan for sites with 75+ staff on site and $250+ a week in combined orders."
    - "Your allowance comes off after the work price."
    - "No contract. Pilots run 4 weeks. After that, 30 days' notice."
    - "Prices in CAD. For your own staff, not for resale."
13. **Closing.** H2: **"Let's feed your team."**
    - Sub: "Book a free tasting and we'll bring 8 meals to your site on our route day. Or call us at (416) 298-1350."
    - Button: "Book a tasting", which scrolls to the hero form.
    - Small print: "J&W Foods · 2201 Brimley Rd, Unit 1, Scarborough · Family-run since 1995."

### Customer flows (each clickable end to end)

1. **HR books a free tasting.**
   1. Fill the hero form and pick "Our employees".
   2. Choose Markham. The Friday GTA 4 hint appears.
   3. Submit. A demo modal opens: "Thanks, Dana. Your tasting request is in. Lucas from our team will call within one business day. You're on our Friday route, so we could bring the tasting Friday, Oct 23 or Oct 30. Demo: nothing was sent."
   4. The lead is saved to `JWC.store('p4-leads')`.
   5. Buttons: "Design your perk" (scrolls) and "Close".
   - Branch: choosing "Members or patients at a gym or clinic we run" shows the routing note to prototype 2 instead of submitting.
2. **HR designs the perk and starts a pilot.**
   1. In the Perk Designer, set 140 staff, 3 days and $3 off. The tier badge changes to Team.
   2. Click "Start a 4-week pilot with these settings". A 4-step modal opens.
   3. Step 1, Company: prefilled from the lead or "Northline Logistics", Markham. Route: Friday GTA 4. Dock instructions.
   4. Step 2, Perk: a summary that can be edited, with "Who's eligible: everyone with an @northline.example email".
   5. Step 3, Invite: paste emails. The domain check reports, for example, "12 invites ready, 1 not on your domain (sam@gmail.com)". Toggle Thursday reminders.
   6. Step 4, Billing: "Company wallet, topped up monthly by card or EFT (demo). We bill only what staff use." Pilot: 4 weeks with free delivery. Tick the terms (demo).
   7. Click "Start my pilot". A demo confirmation reads: "Invites go out Monday, Oct 19. Staff can order until Sunday, Oct 25. Your first drop is Friday, Oct 30 on the GTA 4 route."
   8. The pilot appears in the team-view accounts and pipeline.
3. **An employee orders next week's meals.**
   1. Enter priya@northline.example (try a wrong domain first and see the error).
   2. Click "Send my sign-in link". The demo signs her straight in.
   3. Add 4 lunches. The allowance meter fills.
   4. Review the split (company −$12.00, you pay $34.51) and toggle the weekly repeat.
   5. Click "Confirm my meals". The demo confirmation shows her named bag.
   6. The order is saved through `JWC.addOrder` with the note "At Work staff order · Northline". A toast appears, and the team-view Northline count rises.
4. **A night-shift worker buys from the At Work Freezer.**
   1. Tap Jerk Chicken in the freezer.
   2. A QR sheet opens. Choose "Use my allowance ($3.00 off)".
   3. Tap "Pay $9.34". The demo confirmation appears and stock drops to 5.
   4. Repeat until the item shows "Low: restock Wednesday".
   5. The team-view freezer table and the production agent's par card reflect the sale.
5. **An office manager orders a Team Table pack.**
   1. In the Lunch & Learn Pack, swap 2 Salmon for 2 Jerk Chicken. The total recalculates.
   2. Click "Order this pack". `JWC.checkout` opens with Markham and the −$20 At Work delivery credit.
   3. Choose the Friday GTA 4 route and click "Place demo order".
   4. The standard order confirmation appears, and the order shows in team view.

### JW team view (`data-team`)

1. **At Work desk · week of Oct 19 (sample data: a typical week about 9 months in).**
   - KPI strip:
     - Live accounts 14
     - Pilots 2
     - Items ordered this week 648 (31% company-funded)
     - Freezers 6 (2 low)
     - Cut-off countdown to Sunday 11:59 pm
     - This month so far $24,900
2. **Accounts table.** Fictional sample names. Clicking a row opens a detail drawer with a 6-week participation sparkline and the invoice preview.

   | Account | Site · route | On site | Perk | Took part | Items this week | Freezer | Health |
   |---|---|---|---|---|---|---|---|
   | Northline Logistics | Markham · Fri GTA 4 | 140 | $3 off, max 5/wk | 31% | 96 | Yes, 68% stocked | Good |
   | Milliken Precision Plastics | Scarborough · Wed GTA 2 | 210 | 2 lunches covered | 27% | 118 | Yes, 41% (low) | Good |
   | Don Mills Design Co. | North York · Wed GTA 2 | 45 | $4 off | 29% (was 44%) | 31 | — | Watch |
   | Eastgate Care Residence | Scarborough · Wed GTA 2 | 120 (3 shifts) | $5 off nights | 24% | 64 | Yes, 55% | Good |
   | Vaughan Cold Storage | Vaughan · Fri GTA 4 | 95 | $2 off | 22% | 44 | — | Good |
   | Brightpath Software (pilot, week 2 of 4) | Toronto · Wed GTA 2 | 38 | Everything on Wednesdays | 61% | 52 | — | Pilot |
   | Ajax Fleet Services | Ajax · Tue GTA 1 | 80 | $3 off | 26% | 42 | Yes, 80% | Good |
   | Mississauga Print Works | Mississauga · Wed GTA 2 | 60 | $2.50 off | 20% | 26 | — | Watch (Starter tier) |

   New pilots from flow 2 appear at the top with a "New" tag.
3. **Approvals: AI drafts waiting for you.** Each card has Approve / Edit / Skip, and its state is saved in `p4-approvals`.
   - *B2B prospecting and account agent.* Intro email to Maple Ridge Packaging (Markham, about 180 staff, on the Friday route).
     - Subject: "Lunch for your night shift, from a Scarborough butcher".
     - Body: "Hi there, we're J&W Foods, a family butcher and meal-prep kitchen on Brimley Rd since 1995. Our truck is in Markham every Friday. We run a simple meal perk: you choose what the company covers, staff order by Sunday, and we drop everything at your door. Could we bring 8 meals for your team to try on Friday, Oct 30? Lucas, J&W Foods, (416) 298-1350. Reply STOP to opt out."
     - CASL check: "Published business contact, relevant to role, unsubscribe included: OK".
   - *At Work order desk agent.* Thursday reminder SMS to 97 opted-in Northline staff who haven't ordered: "Hi from J&W at Work. Your $3 lunch credit is waiting. Pick next week's meals by Sunday at midnight: [link]".
   - *B2B prospecting and account agent (account health).* "Don Mills Design Co.: participation fell from 44% to 29% in 3 weeks. Suggest a free Breakfast Meeting Pack ($115.80 retail, about $64 food cost) for their Oct 28 all-hands, plus 2 new menu items."
   - *Production forecast and prep-sheet agent.* "Add At Work volume to Monday's cook plan: +212 chicken breast portions (about 24 kg cooked, 32 kg raw at an est. 75% yield), +64 salmon, +58 tilapia, +120 egg-bite 2-packs, +60 oats."
   - *Production forecast and prep-sheet agent.* "Freezer B (Milliken) sold out of Jerk Chicken by Tuesday two weeks running. Raise par from 8 to 14; cut Lemon Chicken Rice Soup from 8 to 4."
   - *Route and delivery experience agent.* "Wednesday GTA 2: insert 7 At Work drops between stops 9 and 21. Adds about 52 min and 14 km. Text site contacts a 10:30 to 11:30 window."
4. **Production and route impact this week.**
   - Cook-plan change:

     | Item | Count |
     |---|---|
     | Teriyaki Chicken, Green Beans & Rice | 112 |
     | Jerk Chicken, Green Beans & Sweet Potato | 96 |
     | Souvlaki, Broccoli & Greek Potatoes | 84 |
     | Salmon, Brussels & Quinoa | 64 |
     | Tilapia, Asparagus & Brown Rice | 58 |
     | Turkey, Spinach & Rice | 46 |
     | Egg White Bites | 120 |
     | Steel Cut Oats | 60 |
     | Chicken Chili | 8 |
     | **Total** | **648** |

   - Packing: "Named bags: 241 · label and pack about 7.5 h (Monday 1-5 pm, 2 people)".
   - Routes:
     - Tue GTA 1: 1 drop
     - Wed GTA 2: 7 drops, +52 min
     - Thu GTA 3: 1 drop
     - Fri GTA 4: 5 drops, +41 min
     - Freezer restocks: 6 (20 min each)
5. **Split invoice preview, "Northline Logistics · October 2026 (sample)".**

   | Line | Amount |
   |---|---|
   | Team orders (4 weeks), 352 items at work prices | $3,612.48 |
   | Freezer sales, 118 items | $1,232.40 |
   | Company covered (470 × $3.00) | $1,410.00 |
   | Staff paid by card | $3,434.88 |
   | Delivery | $0 (every week over $250) |
   | Freezer shrink | 1.2% (under 3%, nothing billed) |
   | **Drawn from the company wallet** | **$1,410.00** |

   Button: "Approve and send" (demo). The draft is from the At Work order desk agent.
6. **Pipeline board.** Researched 46 → Contacted 19 → Tasting booked 6 (+ leads from flow 1) → Pilot 2 (+ pilots from flow 2) → Live 14 → Paused 1.
7. **Orders from this device.** `JWC.orders()` filtered to proto 4: staff orders, freezer buys and packs.

### Chat ("At Work Desk")

- Greeting: "Hi, I'm the At Work Desk. I can price a meal perk for your team, check your delivery day, or explain how the freezer works."
- Suggestions:
  - "What would $3 off a meal cost us for 100 staff?"
  - "Which day do you deliver to Markham?"
  - "Do we need a freezer?"
  - "Is this a taxable benefit?"
- Rules:

Rules (regex source, case-insensitive, then the scripted reply):

1. `(cost|budget|how much).*(staff|team|employee|people)|\$\s?\d+(\.\d+)?\s*off`  
   "Here's a rough example. With 100 staff on site 3 days a week and $3 off each meal, about a quarter of people order, which is roughly 56 lunches a week. The company would cover about $168 a week, or around $730 a month, and staff pay about $8.70 for a typical lunch. Try the perk designer on this page to change any number. All figures are estimates."
2. `freezer|fridge|storage|space|kitchen`  
   "You need a microwave and some freezer space. Each person's meals arrive in one sealed, named bag. Sites with 75 or more staff on site can borrow a J&W glass-door freezer at no charge when team orders and freezer sales average $250 a week. We restock it on your route day."
3. `\btax|taxable|\bcra\b|payroll`  
   "Subsidised meals can count as a taxable benefit for staff in Canada, depending on how much they pay. We can't give tax advice, but your monthly report lists each person's company-paid total so your payroll team can handle it. Please check with your accountant or payroll provider."
4. `contract|cancel|commit|minimum|skip|pause|notice`  
   "There's no contract. Pilots run 4 weeks, and after that you give 30 days' notice to stop. If nobody orders in a week, nothing ships and nothing is billed. Delivery is free on any week over $250; under that, the usual $20 route fee applies."
5. `allerg|\bnuts?\b|gluten|halal|vegetarian|vegan|dairy|kosher`  
   "Every meal shows its ingredients and allergens before staff order. Vegetarian options include the Egg White Bites with Spinach & Feta, and the Steel Cut Oats are vegan. We don't claim any At Work item is halal or kosher certified. For a serious allergy, please call us at (416) 298-1350 before ordering."
6. `night|shift|hospital|nurse|warehouse|24.?7`  
   "Night shifts are where the freezer shines. Staff grab a meal, scan the QR code and pay with their allowance or a card. Thaw it in the staff fridge for tomorrow, or follow the from-frozen time on the label. We set the freezer mix to what your shifts actually buy and restock weekly."
7. `tasting|\btry\b|\bvisit|come by`  
   "We'll bring a free tasting of 8 meals to your site on our route day, with a short talk on protein and portions. Fill in the form at the top of the page and Lucas will call within one business day. (Demo: nothing is sent.)"
8. `meeting|catering|\bevents?\b|party|bbq|lunch.and.learn|all.hands`  
   "For meetings, the Lunch & Learn Pack feeds 12 for $147.88 and the Breakfast Meeting Pack is $115.80, both at our published prices. For a summer BBQ, the Team BBQ Pack ($134.95) has a 5 kg case of no-salt chicken souvlaki skewers, tzatziki and pita for about 25 people. Packs come frozen on your route day, so plan a few days ahead."
9. `discount|tier|volume|cheaper|work pric`  
   "Work pricing starts at our published prices. When your whole company orders 40 or more items a week, everyone gets 5% off. At 100 or more it's 10% off, which brings a $12.99 pre-set meal to $11.69 before your company allowance."
10. `gym|resell|resale|wholesale|gift|fundrais|school`  
   "J&W at Work is for employers feeding their own staff. To resell meals at a gym or clinic, see the Pro Partner Portal (prototype 2). For client or holiday gifts, see the Corporate Gift Studio (prototype 5). For a team or school fundraiser, see Team Fuel (prototype 7)."

### Products

- **Catalog ids (`site/assets/catalog.js`):**
  - Lunch:
    - `pre-set-meal-teriyaki-chicken-breast-green-beans-basmati-white`
    - `chicken-broccoli-sweet-potato-fries`
    - `tilapia-asparagus-brown-rice`
    - `jerk-chicken-broccoli-sweet-potato-chunks`
    - `turkey-spinach-white-rice`
    - `salmon-brussel-sprouts-quinoa`
    - `copy-of-chicken-broccoli-sweet-potato-fries`
    - `sirloin-ground-green-beans-sweet-potato-chunks`
    - `chicken-souvlaki-broccoli-sweet-potato-chunks`
  - Wraps and soups:
    - `beef-souvlaki-wrap`
    - `wrap-beef-flank-fajitas-copy-1`
    - `copy-of-wrap-chicken-breast-chipotle`
    - `chicken-ground-chilli`
    - `soup-chicken-lemon-soup`
    - `beef-chilli`
  - Breakfast:
    - `copy-of-feta-omelette-cups-cooked-portioned-2-pkg`
    - `copy-of-egg-bites-omelette-w-peppers-onions-mushrooms-cooked-portioned-2-pkg`
    - `steel-cut-oats`
    - `spinach-feta-egg-wrap`
    - `copy-of-breakfast-wrap-egg-chicken-breakfast-sausage`
    - `oatmeal-breakfast-bars-baked-3oz-cooked-portioned-copy`
  - BBQ pack: `chicken-souvlaki-no-salt`
- **From `research/jw-catalog.json`.** Copy the name, price and image exactly. These are needed only for the BBQ pack:
  - `copy-of-tzatziki-sauce`: "TZATZIKI SAUCE", 1.5 LITRE $15.00, image `https://cdn.shopify.com/s/files/1/1156/0176/products/tzatzi_small.JPEG_05c73538-5d17-4b94-a467-1fdf5256d3b3.png?v=1603817943`
  - `whole-wheat-pita-bread`: "WHOLE GRAIN GREEK PITA" (12 per pack), $4.99, image `https://cdn.shopify.com/s/files/1/1156/0176/products/WHOLEWHEATPITA.jpg?v=1603989548`
- **Concept products:**

| Concept | Price | How it is priced |
|---|---|---|
| Work pricing, Team tier | 5% off every item at 40-99 items a week (e.g. $12.99 → $12.34) | JW's published prices less 5%. The cost is covered by one-stop delivery and steady weekly volume |
| Work pricing, Site tier | 10% off at 100+ items a week ($12.99 → $11.69) | JW's published prices less 10% |
| Lunch & Learn Pack, 12 people | $147.88 | 4 × $13.99 + 4 × $9.99 + 4 × $12.99, at published 4 oz prices |
| Breakfast Meeting Pack, 12 people | $115.80 | 12 × $5.25 Egg White Bites + 12 × $4.40 Steel Cut Oats |
| Team BBQ Pack, about 25 people | $134.95 | $95 No-Salt Chicken Souvlaki Case (5 kg) + $15 Tzatziki 1.5 L + 5 × $4.99 Whole Grain Greek Pita |
| Free team tasting | $0 (value $99.92) | 2 each of Souvlaki ($13.99), Jerk Chicken ($12.99), Teriyaki Chicken ($9.99) and Salmon ($12.99). Food cost about $55 |
| At Work Freezer loan | $0 to the employer | For 75+ staff on site and $250+ a week. The 3% shrink clause is billed at work prices. J&W's capex is about $1,800 (est.) |
| At Work delivery | Free on weeks over $250 | Replaces the $20 route fee. The cost to J&W is about $8-14 a stop on an existing route |
| Step-challenge prize | $60 Meal Butler credit per account per quarter | Food cost about $33 |

## Sources

- WeCook for Business: https://www.wecookmeals.ca/en/business
- WeCook plans API (consumer prices): https://www.wecookmeals.ca/api/plans
- WeCook UI string file (B2B dashboard mechanics): https://www.wecookmeals.ca/js/i18n.js
- Retail Insider, "WeCook launches 'WeCook for Business'" (Aug 26 2025): https://retail-insider.com/?p=177907
- Trustpilot, WeCook: https://www.trustpilot.com/review/wecookmeals.ca
- Strategy, WeCook and P.K. Subban (Aug 26 2025): https://strategyonline.ca/2025/08/26/wecook-pk-subban/
- City of Toronto Employment Survey 2025: https://www.toronto.ca/wp-content/uploads/2025/11/97af-CityPlanning-Toronto-Employment-Survey-Two-Pager-Summary-2025.pdf
- York Region business counts (StatCan CBC, Jun 2025): https://yorklink.ca/2025-york-region-business-counts-factsheet/
- Byte smart-fridge pricing (phase-2 comparison): https://www.bytetechnology.co/pricing
- Job Bank, delivery driver wages, Ontario: https://www.jobbank.gc.ca/marketreport/wages-occupation/21667/ON
- J&W delivery routes and cut-off: https://www.jwfoods.com/pages/home
- J&W products and prices: https://www.jwfoods.com/products.json
- J&W Google rating (4.8, 611 reviews) via Yably: https://yably.ca/reviews/toronto/j-w-foods-2201-brimley-road
- Internal: `research/competitor-04.md`, `research/selection.json` (pick 4), `research/model-assumptions.md`, `research/market-benchmarks.md` (sections 6a, 8, 9, 10, 11), `research/jw-facts.md`, `research/jw-audit.md`, `research/ai-agents-research.md` (agents 2, 3, 6, 12, 13), `site/assets/catalog.js`

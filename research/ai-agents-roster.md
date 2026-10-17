# AI agents roster: ten times the capacity, not ten times the staff

Prepared by Minastech (Erwin Garcia) for J&W Foods / J&W Meal Butler · October 16, 2026
All money in CAD (US-priced tools converted at about $1.37). Every figure is an estimate unless it is J&W's own published price or carries a source. Shared figures come from `model-assumptions.md`; evidence links come from `ai-agents-research.md`.

---

## 1. The short version

- **16 agents, one shared roster.** 10 Core agents are built in the first 90 days (Nov 2026 to Jan 2027). 6 Add-on agents follow in months 4 to 9 (Feb to Jul 2027), once there is data for them to work on.
- **They take the desk work, not the knife work.** Answering, quoting, confirming, planning, labelling, routing and invoicing. Cooking, cutting, packing and driving still need people.
- **Every agent drafts and a named person at J&W approves** anything that reaches a customer, changes a price, moves money or commits the plant.
- **The 10x is capacity.** The same team can handle about 10 times the online and B2B orders and conversations per staff hour. Revenue does not 10x overnight; it grows only as the seven plays fill that capacity (about 2 to 3 times today's online and B2B revenue by year 2, mid case).
- **Running cost:** about $1,600 to $3,500 a month for all 16 once live, rising to about $3,000 to $5,000 at year-2 volume. Less than one added full-time person.

---

## 2. The roster at a glance

| # | Agent | Area | Tier | Starts | Build | Run cost / month | Who approves (short) | Plays on screen |
|---|---|---|---|---|---|---|---|---|
| 1 | Butler Concierge | Serve | Core | Nov 2026 | 4 wks | $150-350 | Counter lead: every refund and credit | Chat on all 7; desk modes on 5, 6, 7 |
| 2 | Macro Butler | Sell | Core | Dec 2026 | 5 wks | $60-150 | Lucas: every personal plan and re-plan | 1, 6 |
| 3 | Reorder & Save | Sell | Core | Dec 2026 | 4 wks | $250-500 | Lucas: save-offer and discount limits | 1, 3, 6 |
| 4 | Business Desk | Sell | Core | Nov 2026 | 6 wks | $150-350 | Lucas: tiers and terms; owners: quotes over $5,000 | 2, 4, 5, 7 |
| 5 | Account Scout | Sell | Core | Nov 2026 | 3 wks | $250-400 | Lucas: every outreach sequence | 2, 4, 5, 7 |
| 6 | Lifecycle Marketing | Grow | Core | Nov 2026 | 3 wks | $250-600 | Lucas: every campaign and flow | 1, 5, 7 |
| 7 | Catalogue & SEO | Grow | Core | Nov 2026 | 3 wks | $10-50 | Tasia: 10% spot-check; Bill: nav changes | 3 |
| 8 | Reviews & UGC | Grow | Core | Nov 2026 | 2 wks | $25-70 | Bill or Tasia: every 1-3 star reply | 1 |
| 9 | Nutrition & Safety | Make | Core | Nov 2026 | 5 wks | $30-90 | Partner dietitian: every macro panel and medical case | 1, 2, 4, 6 |
| 10 | Production Planner | Make | Core | Dec 2026 | 5 wks | $30-100 | Kitchen lead: Monday plan and purchase orders | 1-7 |
| 11 | Route Planner | Move | Add-on | Feb 2027 (month 4) | 3 wks | $200-350 | Dispatcher: each day's routes | 2, 4 |
| 12 | Receivables Desk | Serve | Add-on | Feb 2027 (month 4) | 3 wks | $40-120 | Bookkeeper: invoices; owners: pauses and terms | 2, 4 |
| 13 | Phone Order Line | Serve | Add-on | Mar 2027 (month 5) | 4 wks | $70-260 | Counter lead: next-morning callbacks | 3 |
| 14 | Paid Ads Analyst | Grow | Add-on | Mar 2027 (month 5) | 2 wks | $30-80 plus ad spend | Owners: monthly cap; Lucas: moves over 20% | 3 |
| 15 | Carcass Balancer | Make | Add-on | Apr 2027 (month 6) | 4 wks | $10-40 | Head butcher: cut plan; Lucas: price changes | 3 |
| 16 | Monday Brief | Grow | Add-on | May 2027 (month 7) | 2 wks | $10-30 | Bill and Steven: the three proposed decisions | (behind all 7) |

Core build total is about 40 build-weeks, so the first 90 days need three build tracks running in parallel. Several Core agents are mostly configuration of tools J&W would buy anyway (Klaviyo, Judge.me, a subscription app).

---

## 3. The agents

### 1. Butler Concierge · Serve · Core
- **Short:** Answers shoppers and businesses 24/7 on chat, Instagram, email and SMS.
- **Job:** Answers order status, delivery day by town, the Sunday cut-off, the $100 minimum, reheating, points and what's in a box from J&W's own data, with cart links, on site chat, Instagram DMs, email and SMS. It is the "Ask the Butler" chat on every prototype, runs as the partner, At Work, Gift and Team Fuel desks, and hands refunds, allergies, medical questions and complaints to a person with a summary.
- **Reads:** Shopify orders and customers, the route and zone table, policies, the catalogue with approved macros and allergen fields, B2B price lists and agreements, FAQ, past tickets.
- **Produces:** Resolved conversations, cart links, tagged escalations with a summary, a weekly "top 10 questions" report that feeds the catalogue and FAQ.
- **Who approves:** The counter lead approves every refund or credit and takes every escalation. Tasia handles Instagram escalations and reviews 20 sampled chats a week. Lucas answers partner pricing exceptions.
- **Moves:** Support hours per conversation; conversion of browsing visitors; evening and Sunday coverage.
- **Expected effect:** Resolves an estimated 60-65% of chats, DMs and emails without staff (vendor range 51-76%). At 3,000 conversations a month that frees about 90 staff hours.
- **Built with:** Claude API (claude-sonnet-5-5 replies, claude-haiku-5-5 triage) + Shopify Admin API + Shopify Inbox and Instagram messaging + Klaviyo SMS.
- **Run cost:** about $150-350 a month (tokens about $140 at 3,000 conversations, plus helpdesk and messaging).
- **Evidence:** [Intercom's Fin, built on Claude, resolves about 51% of conversations out of the box](https://www.anthropic.com/customers/intercom)
- **Plays:** chat on all 7; featured desk modes in 5, 6, 7.

### 2. Macro Butler · Sell · Core
- **Short:** Turns a goal quiz or chat into a priced week of meals.
- **Job:** Runs the 60-second goal quiz and the coach chat, calculates targets with dietitian-approved rules and builds a plan or cart from tagged Meal Butler SKUs within budget, dislikes and stock. It splits households into profiles, explains swaps with the price and macro change, and drafts the 4-week re-plan after a check-in or InBody scan.
- **Reads:** Quiz and chat answers, the approved macro rules, catalogue macros and tags from Nutrition & Safety, live stock and prices, the customer's route day.
- **Produces:** A plan with a "why this plan" note, a cart link or subscription draft, the household split, Personal Macro Plan drafts, re-plan drafts.
- **Who approves:** The partner dietitian signs off the calculation rules and the six plan templates (not each plan). Lucas (coach desk) approves every Personal Macro Plan and every re-plan before it changes. Nutrition & Safety holds medical cases for the dietitian.
- **Moves:** New-customer conversion, average order, plan and subscription uptake.
- **Expected effect:** Aims for 8-12% of finished quizzes and coach chats to become a cart or plan (Play 6 sample week: 22 of 186). At 1,500 sessions a month, that is 120-180 orders a month.
- **Built with:** Claude API (claude-sonnet-5-5) + Shopify Storefront API + quiz front end + Shopify Subscriptions + Instagram messaging.
- **Run cost:** about $60-150 a month.
- **Evidence:** [Octane AI quiz case (Wicked Edge): quiz takers spent $727 vs $450 and converted at 3.6% vs 1.5%](https://octaneai.com/customers/wicked-edge)
- **Plays:** 1, 6.

### 3. Reorder & Save · Sell · Core
- **Short:** Confirms standing orders by text before Sunday and saves cancellations.
- **Job:** Before each Sunday cut-off it texts and emails every subscriber, Club member and regular their box or "same as last week" cart, and handles OK, SKIP, SWAP and PAUSE replies in plain language. It offers cancel-save options inside owner-set limits and follows up failed payments with a payment link.
- **Reads:** Subscription contracts, order history, Klaviyo predicted next-order date and churn risk, stock, route day, SMS consent records, save-offer rules.
- **Produces:** Confirmed orders and skips, swap edits, save offers, payment-link follow-ups, a cancellation-reason log, a weekly retention report.
- **Who approves:** Lucas sets save-offer and discount limits and approves anything outside them. The Meal Butler lead clears the exception queue (out-of-stock swaps, address changes). No charge changes without the customer's own reply.
- **Moves:** Repeat-order rate and churn; demand known before cooking.
- **Expected effect:** About 9 in 10 standing orders confirmed by a text reply. Save flows keep about 1 in 4 cancellations (Recharge reports up to 33%), worth an estimated $40-65K a year at 250 subscribers.
- **Built with:** Claude API (claude-sonnet-5-5 replies, claude-haiku-5-5 intent) + Shopify Subscriptions or Recharge + Klaviyo SMS and email + Shopify Admin API.
- **Run cost:** about $250-500 a month (subscription app, SMS at about $0.15 a message, tokens).
- **Evidence:** [Recharge Retain: up to 33% of cancellations saved; Toronto's Open Farm cut churn 29%](https://getrecharge.com/products/retain/cancellation-prevention/)
- **Plays:** 1, 3, 6.

### 4. Business Desk · Sell · Core
- **Short:** Turns business requests into quotes, accounts and weekly standing orders.
- **Job:** Reads each business application (gym, clinic, employer, gift buyer, team), checks the business is real, maps it to a route day and suggests a tier, terms and starter order. It then runs the account week to week: gift quotes, recipient-list checks and card proofs, team pages and campaign pace, workplace allowances, partner standing orders from freezer counts, certificates, and each group's payout statement.
- **Reads:** Applications, Google listings and websites, the route-zone table, B2B price lists and tiers, partner freezer counts and sell-through, employer allowance rules, recipient lists, the certificate ledger, fundraiser product rates.
- **Produces:** Tier and terms suggestions, quotes and Shopify draft orders, route-sorted recipient lists, draft team pages and share kits, suggested standing orders, certificate codes and redemption nudges, payout statements, account-health flags.
- **Who approves:** Lucas approves every new account's tier and terms. The Gift Desk lead approves quotes and card proofs. Bill or Steven approve any quote over $5,000, any net terms and any payout over $500. Partners and employers approve their own orders before anything ships.
- **Moves:** Business accounts managed per account lead; quote speed; order accuracy.
- **Expected effect:** One account lead can run about 70-80 business accounts instead of about 15-20, and a gift quote goes out in minutes rather than a day (estimate).
- **Built with:** Claude API (claude-sonnet-5-5 drafting, claude-haiku-5-5 list cleaning) + Shopify B2B catalogues and draft orders + wholesale pricing app + Google Places API + Klaviyo.
- **Run cost:** about $150-350 a month.
- **Evidence:** [Heritage Foods doubled order conversion after moving ordering into a WhatsApp catalogue and order flow (WATI case)](https://www.casestudies.com/company/wati/case-study/heritage-foods-doubles-order-conversion-with-wati)
- **Plays:** 2, 4, 5, 7.

### 5. Account Scout · Sell · Core
- **Short:** Finds and books gyms, offices, realtors and teams along J&W routes.
- **Job:** Builds target lists along the GTA 1-4 corridors (gyms, clinics, supplement shops, employers with 50+ staff, realtors, teams, schools and clubs), scores fit and drafts personal outreach with a tasting-tray offer. It books tastings, follows up, and times seasonal pushes such as January wellness budgets, the Holiday 2027 gifting renewal and hockey fundraising season.
- **Reads:** Clay enrichment, Google Maps listings, route zones, B2B offers and case studies, the CRM, published business contacts, CASL rules.
- **Produces:** Qualified lead lists, drafted sequences, booked tastings, the pipeline board, a weekly pipeline report.
- **Who approves:** Lucas approves every sequence and offer before anything sends. Bill or Steven approve non-standard pricing. Nutrition & Safety runs the CASL and claims check on every message.
- **Moves:** New business accounts per month; pipeline per person.
- **Expected effect:** One person can work about 500 prospects a quarter instead of about 60, aiming for 15-20 tastings or calls a month across the four business plays (estimate).
- **Built with:** Clay Launch + Claude API (claude-opus-5-5 research, claude-sonnet-5-5 drafts) + Google Maps listings + HubSpot free CRM + Gmail.
- **Run cost:** about $250-400 a month.
- **Evidence:** [Clay case (Qrew): about 2x positive replies and 40% more meetings with half the sales team](https://clay.com/blog/qrew-case-study)
- **Plays:** 2, 4, 5, 7.

### 6. Lifecycle Marketing · Grow · Core
- **Short:** Writes and runs Klaviyo email and SMS flows in J&W's voice.
- **Job:** Builds and runs the Klaviyo flows and campaigns: quiz-abandon, welcome by plan, reheating tips, "running low" timed to each customer's predicted next order, win-back, the January Reset and Wild Fork-town campaigns, gift-buyer occasion reminders and the Holiday 2027 renewal, and welcomes for gift and fundraiser buyers who opt in. It drafts subject-line tests and reads the results weekly.
- **Reads:** Klaviyo predictive metrics (lifetime value, churn risk, next-order date), Shopify events, the catalogue and approved macros, the promo calendar, review snippets, consent records.
- **Produces:** Flow and campaign drafts, segment definitions, A/B tests, a weekly revenue-per-recipient report.
- **Who approves:** Lucas approves every campaign before it sends and every new flow before it goes live. Nutrition & Safety checks claims and CASL first.
- **Moves:** Repeat revenue, recovered carts, email and SMS share of online revenue.
- **Expected effect:** Takes email and SMS from near zero (no email app today) to 20-30% of online revenue, the well-run benchmark, with about 40% of it from always-on flows (estimate).
- **Built with:** Klaviyo email and SMS (predictive analytics, K:AI) + Claude API (claude-opus-5-5 copy and weekly read-out) + Shopify.
- **Run cost:** about $250-600 a month (Klaviyo plan not yet verified for J&W's list size; tokens under $15).
- **Evidence:** [Klaviyo benchmarks: flows earn about 41% of email revenue from 5.3% of sends](https://klaviyo.com/products/email-marketing/benchmarks)
- **Plays:** 1, 5, 7.

### 7. Catalogue & SEO · Grow · Core
- **Short:** Writes the missing product copy and makes all 979 pages findable.
- **Job:** Rewrites the ~504 thin or empty product descriptions, fills product types on 413 items, normalizes vendors and adds tags (protein, cut, diet, portion, heat), then writes SEO titles, alt text and landing pages such as "meal prep delivery Toronto". It fixes the nav errors (swapped fresh and frozen fruit links, the "mediteranian" URL), keeps every new listing complete and briefs real-photo reshoots for the 59 products with no image.
- **Reads:** The Shopify catalogue (979 products), Nutrition & Safety metafields, a brand voice guide, Search Console, a keyword set, review snippets.
- **Produces:** Bulk product-update drafts, a redirect list, collection and landing pages, structured data, a clean Google Shopping and AI-shopping feed, a weekly SEO report against a holdout set.
- **Who approves:** Tasia spot-checks a random 10% of every batch before it publishes. The labelling consultant approves any health, origin or "no hormones" claim. Bill approves nav and URL changes.
- **Moves:** Organic traffic, on-site search, conversion, visibility in AI shopping assistants.
- **Expected effect:** Product pages with full copy go from 475 of 979 to 979 of 979 in about 3 weeks, with about 25 staff hours of review instead of an estimated 150-200 hours by hand. One-off token cost about $20.
- **Built with:** Claude API (claude-opus-5-5 via the Batch API) + Shopify Admin API bulk edits and metafields + Google Search Console + Shopify Magic.
- **Run cost:** about $10-50 a month.
- **Evidence:** [Reviewer test: 100 AI product descriptions in about 20 minutes vs about 20 hours by hand](https://tenten.co/shopify/shopify-magic-ai-features-ranked/)
- **Plays:** 3 (and every product page on jwfoods.com).

### 8. Reviews & UGC · Grow · Core
- **Short:** Shows the 4.8 Google stars on site and answers every review.
- **Job:** Shows J&W's 4.8-star Google rating (611 reviews) on the site, asks for product and Google reviews 5-7 days after a second delivery, and drafts a reply to every review. It sends complaints to the kitchen or dispatcher within 24 hours and builds a testimonial and photo library, with permission, for product pages, ads and sell sheets.
- **Reads:** Delivered orders, Judge.me, Google Business Profile, Instagram mentions and tags, Facebook.
- **Produces:** Review requests, reply drafts, issue tickets, a weekly themes report, a testimonial library.
- **Who approves:** Bill or Tasia approve every reply to a 1-3 star review and any make-good offer. No incentives without disclosure. Instagram photos are reposted only with the creator's written OK.
- **Moves:** Conversion (social proof), local search ranking, the quality feedback loop.
- **Expected effect:** Google stars on every page in week 1 and 100+ on-site product reviews in the first 90 days, starting with the top 20 sellers. Plan on a conservative +8-15% conversion lift on reviewed pages (model-assumptions.md).
- **Built with:** Judge.me + Google Business Profile API + Claude API (claude-haiku-5-5 sentiment, claude-sonnet-5-5 reply drafts) + Klaviyo triggers.
- **Run cost:** about $25-70 a month.
- **Evidence:** [Spiegel Research Center: a product with 5 reviews is 270% more likely to be bought than one with none](https://spiegel.medill.northwestern.edu/from-reviews-to-revenue/)
- **Plays:** 1.

### 9. Nutrition & Safety · Make · Core
- **Short:** Owns macros, allergens and labels, and holds medical questions for people.
- **Job:** Computes est. macros and allergens for Meal Butler SKUs from J&W recipes, cooked yields and Health Canada's Canadian Nutrient File, and drafts every label J&W prints (workplace-freezer and partner labels, personal-plan labels with name and grams). It also screens every chat, plan and email from the other agents: medical, medication, pregnancy, allergy, eating-disorder or under-18 signals stop the reply and go to a person, and unapproved claims (GLP-1, diabetes, "salt and sugar free") are blocked.
- **Reads:** Recipes and ingredient weights, raw-to-cooked yield tests, CNF data, supplier spec sheets, label templates, the approved claims list, the message and draft stream from the other agents, consent records.
- **Produces:** A per-SKU macro and allergen table in Shopify metafields, label PDFs for each print run, claim flags, a lab-test shortlist for the top sellers, pass or hold decisions with a holding reply, escalations with a summary.
- **Who approves:** The partner dietitian (contract) signs off every published macro panel and answers medical escalations within one business day. A labelling consultant approves every new label template and claim. The kitchen lead confirms recipes and yields.
- **Moves:** Trust and compliance; it unlocks Macro Butler, partner and workplace sales (gyms, clinics and HR need macros) and product-page conversion.
- **Expected effect:** Meal Butler SKUs with numeric macros go from about 6 of 265 to all 265 (the 31 plan SKUs first) for under $25 in tokens. About 3-5% of coach chats are held for a person (Play 6 sample: 7 of 186).
- **Built with:** Claude API (claude-opus-5-5 batch with code execution for macros, claude-haiku-5-5 for screening) + Health Canada CNF + Shopify metafields + thermal label templates.
- **Run cost:** about $30-90 a month (lab tests and label stock are separate).
- **Evidence:** [Health Canada's Canadian Nutrient File is free and covers 5,993 foods and up to 173 nutrients](https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/nutrient-data.html)
- **Plays:** 1, 2, 4, 6.

### 10. Production Planner · Make · Core
- **Short:** Turns Sunday's orders into Monday's cook, cut and pack sheet.
- **Job:** After the Sunday cut-off it rolls every channel's orders (plans, Club boxes, partner and workplace orders, gifts, fundraiser packs) plus a walk-in forecast into Monday's cook, cut, portion and pack sheet, the raw purchase list and frozen par levels. It drafts the Butcher's Pick default boxes, shows plant load and van load by route day (alert at 90%), and reports forecast against actual and waste each week.
- **Reads:** Closed orders by channel, pickup, express and walk-in history, frozen inventory, yields, recipes, supplier lead times, the waste log, capacity by station.
- **Produces:** The production sheet by station, purchase-order drafts, par levels, Butcher's Pick defaults, the weigh-and-pack sheet for personal plans, named-bag pick lists, boxes and stops by route day, a forecast-vs-actual and waste report.
- **Who approves:** The kitchen lead (production manager) approves the plan and every purchase order each Monday. Lucas approves the Butcher's Pick boxes before the cut-off. Bill or Steven approve new par levels or a second shift.
- **Moves:** Food cost and waste, prep labour, stockouts, plant capacity.
- **Expected effect:** Weekly planning drops from about 7 hours of manual tallying to under 1 hour of review, and it targets 10-15% less waste (independent pilot: 14.8%).
- **Built with:** Claude API (claude-opus-5-5, scheduled weekly on Managed Agents) + a Python forecast + Shopify Admin API + Google Sheets ops store + a tablet-and-scale waste log.
- **Run cost:** about $30-100 a month.
- **Evidence:** [Independent two-retailer pilot: AI ordering forecasts cut food waste 14.8% per store](https://pacificcoastcollaborative.org/wp-content/uploads/2022/12/PCFWC-Case-Study_AI_Final.pdf)
- **Plays:** 1, 2, 3, 4, 5, 6, 7.

### 11. Route Planner · Move · Add-on (month 4, Feb 2027)
- **Short:** Sequences the weekly GTA routes and texts every customer an ETA.
- **Job:** Slots home stops, office drops, partner freezer restocks and team drops into the existing Tuesday-Friday routes, sequences them in Routific and texts each customer a delivery window the day before. It adds dry ice for long-haul boxes, flags vans over 90% full and maps route density for new zones or pickup points.
- **Reads:** Orders with addresses and route day, van capacity and cold-chain limits, driver hours, drop windows, Routific.
- **Produces:** Optimized routes and driver manifests, ETA and proof-of-delivery texts, the route-impact table, van-load alerts, a zone-density map.
- **Who approves:** The dispatcher approves each day's routes. Bill or Steven approve any new zone, extra van or fee change.
- **Moves:** Stops per driver-hour, cost per stop, on-time rate.
- **Expected effect:** Stops per driver-hour rise from about 3.5 to about 4.2 (Thistle: 10-20% more deliveries a day with the same staff) and route planning takes about 80% less time.
- **Built with:** Routific (or Circuit for Teams) + Claude API (claude-sonnet-5-5) + Klaviyo SMS + Shopify.
- **Run cost:** about $200-350 a month.
- **Evidence:** [Inspired Go (Canadian prepared meals) cut route planning from 8-10 hours a day to under 1 hour](https://onfleet.com/blog/case-studies-inspired-go/)
- **Plays:** 2, 4.
- **Before month 4:** the Production Planner shows stops and van load by route day, and the dispatcher sequences by hand.

### 12. Receivables Desk · Serve · Add-on (month 4, Feb 2027)
- **Short:** Invoices business accounts, chases late payments, reconciles payouts.
- **Job:** Issues net-15 partner invoices, Net 30 gift invoices and At Work monthly split statements from approved orders, reconciles payments, wallet top-ups and pay-on-redemption certificates, and sends polite reminders at 3 and 7 days overdue. At 30 days it recommends pausing the standing order, and it prepares group payouts for a person to send.
- **Reads:** Approved Shopify B2B orders, payment records, terms per account, the certificate ledger, payout statements from the Business Desk.
- **Produces:** Invoices, aging buckets and days to pay, reminder drafts, pause recommendations, payout requests, a month-end reconciliation file for the bookkeeper.
- **Who approves:** The bookkeeper approves every invoice batch and write-off. Bill or Steven approve pausing an account and any new net terms. People send all payments; the agent never moves money.
- **Moves:** Days sales outstanding, bad debt, admin hours per account.
- **Expected effect:** Keeps average days to pay under about 20 on net-15 accounts and bad debt near the 0.5% reserve, with 2-3 bookkeeper hours a week at 100+ business accounts (estimate).
- **Built with:** QuickBooks Online API + Shopify B2B payment terms + Claude API (claude-haiku-5-5 matching, claude-sonnet-5-5 reminders).
- **Run cost:** about $40-120 a month.
- **Evidence:** [No small-business receivables case in our research; cost basis: Claude scheduled agents run at $0.08 per session-hour plus tokens](https://platform.claude.com/docs/en/about-claude/pricing)
- **Plays:** 2, 4.
- **Why month 4:** partners move to net-15 only after 4 paid orders, so invoice volume really starts in February. Until then the bookkeeper handles the few Net 30 gift invoices and fundraiser payouts from the Business Desk's drafts.

### 13. Phone Order Line · Serve · Add-on (month 5, Mar 2027)
- **Short:** Answers the store line after hours and texts a ready cart.
- **Job:** Answers (416) 298-1350 after hours, on Sundays (store closed, cut-off day) and on overflow, using the same approved data as the Concierge. It answers menu, route-day and order-status questions, texts a pre-filled cart or deposit link, books pickups and logs what callers asked for.
- **Reads:** The catalogue and approved macros, the route table, order lookup, policies, SMS.
- **Produces:** Answered calls, cart and deposit links, call summaries, a missed-demand report.
- **Who approves:** The counter lead calls back every complaint, custom-cut request, allergy question and large business order the next business morning. The line never takes card numbers; the customer confirms in the cart.
- **Moves:** Revenue from missed calls; counter staff time.
- **Expected effect:** If 30-40 Sunday and after-hours calls a month become orders at about $130, that is about $47-62K a year (estimate).
- **Built with:** Retell or Vapi voice platform + Claude API (claude-sonnet-5-5 reasoning, claude-haiku-5-5 routing) + call forwarding + Shopify cart links by SMS.
- **Run cost:** about $70-260 a month (600-900 minutes).
- **Evidence:** [Vendor data (Loman): a typical restaurant misses about 150 calls a month worth $35-85 each](https://loman.ai/blog/restaurant-ai-phone-receptionist-revenue)
- **Plays:** 3.

### 14. Paid Ads Analyst · Grow · Add-on (month 5, Mar 2027)
- **Short:** Runs route-town ads and moves budget toward the lowest cost.
- **Job:** Runs geo-targeted Meta and Google ads by route town (Whitby, Oakville, Ancaster and Newmarket first), catalogue retargeting and B2B ads to gym owners and HR. It reads cost per new customer by town against geo holdouts each week and proposes budget moves under a monthly cap.
- **Reads:** Ad accounts, Shopify orders by postal code, the route map, margin per SKU, the creative library, the holdout plan.
- **Produces:** A weekly test plan, budget-move proposals, creative briefs from real photos, cost per new customer and incremental return by town.
- **Who approves:** Bill or Steven set the monthly cap. Lucas approves any budget move over 20% and all new creative.
- **Moves:** Cost to win a new customer.
- **Expected effect:** Holds new-customer cost at or below the ~$85 planned in Play 1 by moving spend between towns weekly; aim for 10-20% lower cost than set-and-forget campaigns (estimate).
- **Built with:** Meta Ads (Advantage+ catalogue) + Google Ads + GA4 and Meta CAPI + Claude API (claude-opus-5-5 weekly analyst).
- **Run cost:** about $30-80 a month plus ad spend.
- **Evidence:** [Haus, 640 geo-holdout tests: Meta Advantage+ beat manual campaigns only 42% of the time](https://www.haus.io/blog/the-meta-report-lessons-from-640-haus-incrementality-experiments)
- **Plays:** 3.

### 15. Carcass Balancer · Make · Add-on (month 6, Apr 2027)
- **Short:** Plans what to buy and cut so the whole animal sells.
- **Job:** Each week it plans which primals and whole animals to buy and how to break them, so raw cuts, the cooked line (trim to burgers, flank to fajitas) and boxes use the whole animal at the best margin. It pools 1/16 and 1/8 beef shares into full quarters, logs yield by quarter and cutter, and proposes Cut of the month and clearance deals for slow or short-dated cuts.
- **Reads:** The yield-test log, purchase prices, the demand forecast from the Production Planner, share orders, cooked recipes, inventory with pack dates, margin floors.
- **Produces:** The cut plan, a buy list, the share-pooling board, yield variance by cutter and supplier, Cut of the month and clearance proposals, a margin-per-carcass report.
- **Who approves:** The head butcher approves the weekly cut plan. Lucas approves every price change, Cut of the month and clearance deal. Bill or Steven approve supplier changes.
- **Moves:** Gross margin through yield and whole-animal use; waste.
- **Expected effect:** Each point of beef and lamb yield is worth about $4-6K a year on an estimated $400-600K of purchases; pooling and clearance turn slow cuts into sales instead of waste (estimate; vendors claim 1-3% yield, unverified).
- **Built with:** Claude API (claude-opus-5-5 with code execution) + a Google Sheets yield log + Shopify Admin API price drafts + Klaviyo clearance drop.
- **Run cost:** about $10-40 a month.
- **Evidence:** [Völur cut planning at JBS and others: 2-6 hours by hand down to 15-30 seconds](https://www.volur.ai/solutions)
- **Plays:** 3.

### 16. Monday Brief · Grow · Add-on (month 7, May 2027)
- **Short:** One page each Monday: the week, the risks, three decisions.
- **Job:** Every Monday morning it reads every agent's log and J&W's numbers (sales by channel, margin, waste, churn, plant and van load, approvals and overrides) and writes one page for the owners. It ends with three proposed decisions, each with the data behind it.
- **Reads:** Shopify, Klaviyo, the subscription app, Routific, the ops sheets, every agent's approval log.
- **Produces:** The Monday one-pager, the 10x scorecard (the seven levers below against target), three proposed decisions.
- **Who approves:** Bill and Steven read it and approve or reject each proposed decision. Nothing in it changes the shop by itself.
- **Moves:** Owner time per decision; how fast problems are caught.
- **Expected effect:** The week in one page and about 30 minutes, instead of an estimated 3-4 hours pulling reports from five systems.
- **Built with:** Claude API (claude-opus-5-5, scheduled on Managed Agents) + read access to Shopify, Klaviyo, Routific and the ops sheets + email.
- **Run cost:** about $10-30 a month.
- **Evidence:** [Shopify Sidekick surfaces proactive tasks and never changes the shop without merchant approval](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick/features)
- **Plays:** none on screen; it reads all seven.

---

## 4. How the seven plays' agent needs were merged

| Play | Agent named in the play | Roster agent |
|---|---|---|
| 1 Goal Plan Builder | Macro Butler (plan matcher) | Macro Butler |
| 1 | Nutrition Data Agent | Nutrition & Safety |
| 1 | Butcher's Pick Menu Agent | Production Planner |
| 1 | Subscription & Reorder Agent | Reorder & Save |
| 1 | Production Forecast Agent | Production Planner |
| 1 | Lifecycle Marketing Agent | Lifecycle Marketing |
| 1 | Review & Reputation Agent | Reviews & UGC |
| 2 Pro Partner Portal | Partner Scout | Account Scout |
| 2 | Application Checker | Business Desk |
| 2 | Par Level Planner | Business Desk |
| 2 | Production & Route Planner | Production Planner + Route Planner |
| 2 | Label & Claims Checker | Nutrition & Safety |
| 2 | Partner Receivables agent | Receivables Desk |
| 2 | Partner desk chat | Butler Concierge |
| 3 Butcher Club | Box Reminder & Save agent | Reorder & Save |
| 3 | Butler Concierge | Butler Concierge |
| 3 | Production forecast & pick-list agent | Production Planner |
| 3 | Carcass & share-pooling agent | Carcass Balancer |
| 3 | Route & delivery agent | Route Planner |
| 3 | Lifecycle marketing agent | Lifecycle Marketing |
| 3 | Paid ads optimiser | Paid Ads Analyst |
| 4 J&W at Work | B2B prospecting and account agent | Account Scout (prospecting) + Business Desk (account care) |
| 4 | At Work order desk agent | Business Desk (+ Receivables Desk for the split statement) |
| 4 | Production forecast and prep-sheet agent | Production Planner |
| 4 | Route and delivery experience agent | Route Planner |
| 4 | Nutrition data and label agent | Nutrition & Safety |
| 4 | Butler Concierge | Butler Concierge |
| 5 Corporate Gift Studio | Gift Concierge (quotes and orders) | Butler Concierge (chat) + Business Desk (quotes, draft orders) |
| 5 | Recipient List Checker | Business Desk |
| 5 | Card and Message Writer | Business Desk |
| 5 | Occasion and Renewal agent | Lifecycle Marketing |
| 5 | B2B Prospecting agent | Account Scout |
| 5 | Production and Route Planner | Production Planner + Route Planner |
| 5 | Certificate and Redemption agent | Business Desk (+ Receivables Desk for pay-on-redemption) |
| 6 Meal Butler AI Coach | Macro Butler coach | Macro Butler |
| 6 | Nutrition data and label agent | Nutrition & Safety |
| 6 | Instagram DM concierge | Butler Concierge |
| 6 | Check-in and re-plan agent | Macro Butler |
| 6 | Safety triage agent | Nutrition & Safety |
| 6 | Production sheet agent | Production Planner |
| 7 Team Fuel Fundraiser | Team Fuel Desk | Butler Concierge |
| 7 | Team Page Builder | Business Desk |
| 7 | Campaign Coach | Business Desk |
| 7 | Drop and Production Planner | Production Planner + Route Planner |
| 7 | Fundraiser Payout agent | Business Desk (statement) + Receivables Desk (reconciliation) |
| 7 | Lifecycle marketing agent | Lifecycle Marketing |
| 7 | Group Prospecting agent | Account Scout |

Also covered: catalogue and SEO repair (Catalogue & SEO), reviews and UGC (Reviews & UGC), Klaviyo email and SMS retention (Lifecycle Marketing + Reorder & Save), production and cut forecasting (Production Planner + Carcass Balancer), weekly GTA routes (Route Planner), B2B prospecting (Account Scout), phone and DM ordering (Phone Order Line + Butler Concierge), finance and receivables for business invoices (Receivables Desk).

---

## 5. The 10x argument

### Why 10x is realistic for a butcher with its own plant

J&W already owns the parts that take decades to build: an Ontario-inspected plant since 2008, about 292 cooked and portioned SKUs, vacuum-frozen packs that keep for months, weekly routes from Durham to Hamilton, and a 4.8-star Google rating from 611 reviews. What caps growth today is the desk, not the kitchen. Every question, quote, order change and invoice runs through a few people, most of them family.

The Sunday cut-off is the advantage. Most route demand is known before anything is cooked: reminders go out Saturday, orders lock Sunday, the plan prints Monday. That rhythm suits AI agents, because the work is narrow, repeated every week and full of data. Answering "which day do you deliver to Whitby?" or rolling 300 orders into a cook sheet is what they do reliably.

So the 10x is capacity. With agents drafting and people approving, the same 15-25 person team can handle about ten times the online and B2B orders and conversations per staff hour. Revenue does not 10x overnight. It grows only as the seven plays fill that capacity. At the mid case, weekly orders reach about 5 to 7 times today's by year 2, but online and B2B revenue roughly doubles to triples, because many new orders are small (a staff lunch, a fundraiser pack).

The physical ceiling is real. Cooking, packing and driving still need hands, and the agents do not change that. The plays add about 3-5 full-time equivalents across packing, the coach desk, an account lead and coordinators, plus a second packing shift if year-2 volume arrives. That is the honest difference: 10x the desk capacity, not 10x the staff.

### Headline numbers

| Stat | Value | Note |
|---|---|---|
| Agents | 16 | 10 Core in the first 90 days, 6 add-ons in months 4-9 |
| Desk capacity | ~10x | Online and B2B orders and conversations per staff hour (estimate) |
| Orders a week the desk can run | 150 → 1,500 | Estimate; the seven plays fill about 700-1,100 by year 2 |
| People added | 3-5 FTE | Packing, coach desk, account lead, coordinators; not 10x the 15-25 today |
| Online + B2B revenue | ~2-3x | By year 2 at mid; revenue follows as the plays fill capacity |
| Running cost | $1.6-3.5K | A month for all 16 agents, software and tokens (estimate) |

How the year-2 order count is built (mid cases, orders a week): Goal Plans ~145 (312 subscribers × 26 × 0.9 ÷ 52, plus one-offs) · Pro Partners ~44 · Butcher Club ~65 · J&W at Work ~500-550 staff orders (22 accounts × 55 items ÷ 2.2 items each) · Gifts ~65 on average (peaks near 250 in December) · AI Coach ~75 · Team Fuel ~44. That is about 960 new orders a week on top of today's estimated ~150, or about 700 on the recommended three-play path after its 25% overlap discount. Today's online and B2B revenue is about $1.2M (delivery $0.9M + trade $0.3M, jw-audit.md mid); the recommended path adds about $1.29M (million.md), and all seven plays at mid with the same 25% discount add about $2.75M.

### The 10x math, lever by lever

| Lever | Today (est.) | With agents | Multiple | Agents | Note |
|---|---|---|---|---|---|
| Conversations handled per staff hour | About 8. Every chat, DM, email and call answered by hand, about 7 minutes each | About 55. The Concierge resolves 60-65%; staff answer the rest from a drafted summary in about 3 minutes | 7x | Butler Concierge, Nutrition & Safety, Phone Order Line | Vendor resolution rates run 51-76%; we plan below that. Allergy, medical and complaints stay with people. Evenings and Sundays are covered for the first time |
| Orders processed per admin hour | About 6. Entry, edits, tallies, pick lists and labels by hand, about 10 minutes an order | About 60. Agents roll orders into sheets, pick lists and labels; a person checks each in about 1 minute | 10x | Business Desk, Reorder & Save, Production Planner, Nutrition & Safety | Desk time only. Cooking, packing and driving still scale with people, which is why the plays add packers and coordinators |
| Repeat orders confirmed per staff hour | About 12. No subscription app; regulars rebuild carts online or call, about 5 minutes each | About 150. Saturday text, reply OK, SKIP or SWAP; about 1 in 10 needs a person | 12x | Reorder & Save, Lifecycle Marketing, Macro Butler | Standing-order customers go from 0 today to about 500 by Oct 2027 (Goal Plans 251, Butcher Club 247, mid). Save flows keep about 1 in 4 cancellations |
| Product pages with complete copy | 475 of 979 (49%). About 4 pages written per staff hour by hand | 979 of 979 (100%) in about 3 weeks. About 40 pages per staff hour with a 10% spot-check | 10x | Catalogue & SEO, Nutrition & Safety, Reviews & UGC | Reviewer test: 100 AI drafts in about 20 minutes vs about 20 hours by hand. SEO lift is measured against a holdout set, not assumed |
| Business accounts per account lead | About 15-20. Orders by phone and email, quotes and invoices by hand, about 1 hour per account a week | About 70-80. Orders, quotes and invoices arrive drafted; about 15 minutes per account a week to approve | 4x | Business Desk, Account Scout, Receivables Desk | Plays 2, 4, 5 and 7 bring about 150 business relationships by Oct 2027 (34 partners, 16 employers, about 60 gift buyers, about 38 groups, mid): 7-8 account leads by hand, or about 2 with agents |
| Production forecast accuracy and planning time | About 70% of SKUs within 10% of plan; about 7 hours a week to tally and plan by hand | About 90% within 10%, because 75-80% of volume is pre-sold before cooking; under 1 hour to review | 7x | Production Planner, Reorder & Save, Carcass Balancer | The 7x is planning time; accuracy improves about 1.3x, mostly because more volume is ordered ahead. Target 10-15% less waste (independent pilot: 14.8%) |
| Route stops per driver-hour | About 3.5 (30-40 stops on a 9-hour route); routes sequenced by hand | About 4.2 with Routific sequencing; planning about 80% faster; office, partner and team drops carry 20-150 items in one stop | 1.2x | Route Planner, Production Planner, Business Desk | Driving does not 10x. Thistle got 10-20% more deliveries a day with the same staff. Items delivered per driver-hour roughly double because of bulk drops |

### Rollout phases

1. **Fix the shop, open the desks** · Weeks 1-4, Nov 2026 · Catalogue & SEO, Reviews & UGC, Nutrition & Safety, Butler Concierge, Lifecycle Marketing, Business Desk (gift mode first), Account Scout. **Milestone by Nov 29:** 979 of 979 product pages complete, Google stars on the site, Klaviyo welcome and cart flows live, the Concierge on 24/7, the Gift Desk quoting holiday orders in minutes, and macros signed off for the 31 plan SKUs.
2. **Launch standing orders** · Weeks 5-13, Dec 2026 to Jan 2027 · Macro Butler, Reorder & Save, Production Planner. **Milestone:** Goal Plans live in December and Butcher Club boxes from Dec 1; every Sunday cut-off becomes Monday's cook, cut and pack sheet without manual tallying; partner drops start in December and At Work pilots in January through the Business Desk.
3. **Scale routes, money and reach** · Months 4-6, Feb to Apr 2027 · Route Planner, Receivables Desk, Phone Order Line, Paid Ads Analyst, Carcass Balancer. **Milestone:** routes planned in under an hour a day, net-15 invoices and reminders automatic once partners pass 4 paid orders, Sunday calls answered, ad spend moved weekly by town, and the first beef quarters on the yield log.
4. **Run it from one page** · Months 7-9, May to Jul 2027 · Monday Brief. **Milestone:** Bill and Steven approve the week from a Monday Brief; every agent is re-tuned on J&W's own data, holdout tests are read, and the year-2 calls are made (second packing shift, extra van, next plays).

### Guardrails

1. People approve. Agents draft; a named person approves every price change, refund, credit, payout, new account, label, campaign and purchase order. Every approval is logged, and the Monday Brief shows what was approved, edited or rejected.
2. Food facts come only from J&W's approved data. Macros and allergens are signed off by the partner dietitian and never come from the model's general knowledge. Medical, medication, pregnancy, eating-disorder and under-18 signals go to a person within one business day.
3. No health or disease claims. Nothing about GLP-1, diabetes, "salt and sugar free" or "no hormones" goes live until the labelling consultant approves it. Meat orders and addresses are checked against the Ontario-only rule for a provincially inspected plant.
4. CASL on every commercial message: express consent on file, sender ID and STOP in every text. J&W never messages fundraiser families or business contacts without consent or a valid exemption.
5. Agents never handle card numbers or send money. They send payment links and draft invoices and payouts; the bookkeeper and owners release them. Discounts, save offers and ad budgets have hard caps.
6. Honest and private. Real food in every photo (AI touches backgrounds only), no fake or undisclosed incentivized reviews, every AI reply labelled with a way to reach a person, and customer data kept in Shopify, Klaviyo and J&W's own sheets. Results are measured with holdouts, not vendor claims.

### What the agents cost to run

Once all 16 are live, the agents cost an estimated $1,600-3,500 a month in software, SMS and Claude API tokens (CAD; US-priced tools at about $1.37). Claude tokens are the small part, about $250-600 a month across every agent; the bigger lines are Klaviyo, the subscription app, SMS, Clay, Routific and the voice line. At year-2 volume, about 5,000 conversations a month and 1,000 orders a week, it rises to about $3,000-5,000 a month. That is less than one added full-time person (about $4,000 a month loaded) for desk capacity worth several. It excludes ad spend, lab tests, label stock, freezers and Minastech's fee, and many of these lines already sit in each play's cost table, so they should not be counted twice.

---

## 6. Which agents power each prototype

The "Ask the Butler" chat (Butler Concierge) runs on all seven prototypes; it is listed below only where its desk mode is a feature of the page. Each prototype shows at most six agents.

**Play 1 · Goal Plan Builder**
- Macro Butler: quiz result card "Why we picked Lean Bulk for you", labelled as drafted by Macro Butler, with the household split. Medical or allergy answers route to a person instead.
- Nutrition & Safety: "est." macro chips on every plan card and meal row; team tile "Macro sign-off: 9 of 31 plan SKUs verified"; one GLP-1 email held for labelling review.
- Reorder & Save: Saturday SMS preview in My Plan (reply OK, SKIP, SWAP or PAUSE), the cancel-save modal, and 3 save offers waiting for approval.
- Production Planner: Butcher's Pick approval card (Lean box swaps the Tilapia pre-set for the Haddock plate, margin +$0.40 a box), the Monday prep sheet and boxes by route day.
- Lifecycle Marketing: quiz-abandon, plan welcome, January 6-Week Reset and meal-kit switch campaign drafts waiting for Lucas.
- Reviews & UGC: team queue with 2 reply drafts for new Google reviews, and the review request after the second box.

**Play 2 · J&W Pro Partner Portal**
- Account Scout: outreach draft to Birchmount Strength Co. with a CASL check line and Approve, Edit or Skip.
- Business Desk: instant pre-check card after "Send application", the Applications queue with a suggested tier, and the partner's "Suggested order for Wednesday" built from freezer count and sell-through.
- Nutrition & Safety: live "Fuelled by J&W at [partner]" label preview from the master recipe file, and a draft with "great for GLP-1 patients" removed.
- Production Planner: production impact of +180 pre-set meals and 8 chicken cases, with the plant-load meter.
- Route Planner: partner stops by route day on GTA 1-4, with added minutes for the dispatcher to approve.
- Receivables Desk: aging buckets, days to pay and a reminder draft to Harbour & Hill Nutrition; the invoice list in the partner portal.

**Play 3 · J&W Butcher Club**
- Reorder & Save: Thursday reminder SMS in Approvals, the Retention queue, and the My Club skip, pause and cancel flow.
- Production Planner: Monday pick list (cases to pull, steaks to cut by thickness, cooked chicken packs from Meal Butler stock) with Approve.
- Carcass Balancer: beef share board pooling 1/16 and 1/8 shares into quarters, and the short-rib Cut of the month proposal.
- Catalogue & SEO: cut cards with full descriptions, $/lb and thickness options, rewritten from J&W's raw-meat pages.
- Paid Ads Analyst: "Move $10/day from Mississauga to Newmarket" proposal in Approvals, with cost per new member by Club town.
- Phone Order Line: Sunday call summary, a caller asked about a 1/8 beef share and got the cut sheet and deposit link by text (sample).

**Play 4 · J&W at Work**
- Account Scout: intro email to Maple Ridge Packaging and the pipeline board, waiting for approval.
- Business Desk: staff app allowance meter and confirmation, the Thursday reminder SMS, and the Don Mills Design Co. save offer after participation dipped.
- Production Planner: the cook-plan change of 648 items and the Milliken freezer par change from 8 to 14.
- Route Planner: route impact of 7 Wednesday drops adding about 52 minutes, and ETA texts to each site contact.
- Nutrition & Safety: "est." protein stickers on menu cards, full freezer labels with heating times, and average protein per lunch in the HR report.
- Receivables Desk: the Northline split statement, company wallet share and staff share on one page.

**Play 5 · Corporate Gift Studio**
- Business Desk: "Price in two taps" quote (Steeles: 60 Gentleman's Boxes at 8% volume pricing), the route-sorted recipient list check, the Maple Ridge Dental card proof and the certificate ledger.
- Butler Concierge: Gift Desk chat that prices 50 gifts and explains Pick-a-Box certificates, invoice terms, deadlines and the CRA $500 gift note.
- Account Scout: 24 new realtor and mortgage-broker leads on the Friday route, with step-1 emails drafted and CASL checked.
- Production Planner: cut list for the week of Dec 14 (280 ribeyes, 840 lamb chops), packing hours, and the Wednesday van at 94% with a second van suggested.
- Lifecycle Marketing: last-call email to 142 past buyers and warm leads (logo cards close Sunday, Dec 6), and opted-in recipients handed to the welcome flow.

**Play 6 · Meal Butler AI Coach**
- Macro Butler: intake stepper, the "Here's your week" planner with swaps, and drafts waiting for Lucas: Maria S.'s re-plan after her scan and Dev P.'s new plan.
- Nutrition & Safety: macro dots and "est." values on cards, the personal label that prints, the Korean BBQ marinade flagged for a sugar check, and the "Let's get a person on this" card when a DM mentions diabetes and metformin.
- Butler Concierge: Instagram DM demo that answers delivery-day and price questions, starts the coach when someone types PLAN and books InBody scans (61 of 74 DMs answered without help).
- Reorder & Save: skip or pause before the Sunday cut-off with no contract (Priya N. paused to Mar 29).
- Production Planner: Saturday weigh-and-pack sheet (330 personal meals and labels) with the route split, and the Honey Garlic Salmon stock swap.

**Play 7 · Team Fuel Fundraiser**
- Butler Concierge: Team Fuel Desk chat on goal math, drops, payouts, school rules and allergens, from approved data only.
- Business Desk: "Build my team page" draft for Markham Northstar Dance, pace nudges for the Snowhawks and Cedar Hollow, and the Whitby Wolves payout statement ($643.74) waiting for owner approval.
- Production Planner: Whitby Wolves drop sheet (29 named bags, 4 coolers), the Monday cook plan from 38 Game-Week packs and the raw order.
- Lifecycle Marketing: welcome flow for 61 opted-in buyers (reheating tips, the $10 first-order offer, the team-link reminder), CASL checked.
- Account Scout: next-season pipeline of 32 new leads for Jan-Feb along GTA 1 and GTA 2, with intro emails drafted.

---

## 7. Assumptions and gaps

- J&W's real order count, conversation volume, call volume, list size and staff hours were not available. "Today" figures are estimates from jw-audit.md (mid: ~100 route orders a week plus pickup and trade) and should be replaced with J&W's Shopify, Inbox and phone data in month 1.
- Vendor resolution, yield and lift figures are mostly vendor-published (grades B/C in ai-agents-research.md). We plan below them and measure with holdouts.
- Klaviyo, subscription-app and Shopify B2B pricing for J&W's tier were not verified.
- No small-business receivables or small-butcher yield case study was found.
- Front-of-pack and labelling exemptions for J&W's products must be confirmed with Health Canada and CFIA before any label prints.
- Sample names in the prototype notes (partners, employers, groups, clients) are fictional.

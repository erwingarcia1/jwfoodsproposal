# AI Agents for J&W Foods / J&W Meal Butler: Research Report

**Prepared for:** Minastech (Erwin Garcia), growth proposal for J&W Foods Inc. (J&W Meal Butler), 2201 Brimley Rd, Scarborough
**Date:** October 16, 2026
**Scope:** How AI agents are used in 2025-2026 by food, meal-prep, butcher/meat-processing, grocery and DTC Shopify businesses, with evidence and URLs, then 15 candidate agents designed specifically for J&W.

---

## 0. Executive summary

1. **The evidence is strongest where the work is narrow, repetitive and data-rich.** Customer-service agents resolve roughly 50-76% of conversations at the vendor level (Intercom Fin, Tidio Lyro). Route optimisation cuts planning time by 80%+ (Onfleet: Inspired Go, a Canadian prepared-meal company). AI production and ordering forecasts cut fresh-food shrink by about 15-25% (Afresh, Shelf Engine, plus an independent multi-retailer pilot). Kitchen waste AI cut waste 18% at an Ontario cook-chill production kitchen (Winnow at Compass Group Canada's Milton Cook Chill).
2. **Revenue-side AI is less proven but already large at platform scale.** Amazon says shoppers who use its Rufus assistant are 60% more likely to buy, and it expects $10B+ in annual incremental sales. Shopify reports orders from AI search channels up 11x (Q3 2025) and 15x (Q4 2025) since January 2025, then tripling year over year in Q2 2026. Personalisation leaders typically see 5-15% revenue lifts (McKinsey).
3. **J&W's gaps line up closely with where the proven agents work.** By J&W's own catalog: 979 products; about 504-508 with empty or very short descriptions; 413 with no product type; only 15 tagged; 59 with no image; 265 Meal Butler SKUs, of which only about 6 show numeric macro values; no subscription; no reviews; no macro or meal builder; no B2B portal. Every one of these is a known, solved AI use case.
4. **Running custom agents on the Claude API costs very little next to the levers they move.** Rewriting the whole 979-product catalog costs an estimated US$10-15 one-off on Claude Opus 5.5 via the Batch API. A 3,000-conversation-per-month concierge costs an estimated US$100/month on Claude Sonnet 5.5. Off-the-shelf Gorgias AI Agent would cost about US$0.90-1.00 per automated interaction ([Gorgias pricing](https://www.gorgias.com/pricing)).
5. **The 15 recommended agents fall into three groups:**
   - **Revenue engines (5):** Macro Butler meal-plan builder, auto-reorder/subscription agent, B2B prospecting agent, lifecycle marketing agent, phone/voice order agent.
   - **Conversion enablers (6):** nutrition data and label agent, concierge, catalog/SEO/AI-shopping agent, visual studio, ads optimiser, reviews agent.
   - **Margin and ops (4):** production forecast, carcass and cut-yield, smart markdown, route and delivery.
6. **Caveat on evidence quality.** Most quantified results in this market are vendor-published. Each figure below carries an evidence grade, and anything not found is marked as such, with a labelled estimate where useful.

**Evidence grades used below**
- **A:** Public filing or earnings call, government statistic, peer-reviewed or independent multi-party study.
- **B:** Named-customer case study (usually vendor-published) or independent measurement firm.
- **C:** Vendor marketing claim, aggregator, or blog with no stated method.

---

## 1. J&W starting point: the data the agents would work on

From the 16 Oct 2026 crawl (`jw-facts.md`) and my own pass over `jw-catalog.json`:

| Signal | Value | Why it matters for AI |
|---|---|---|
| Products online | 979 (743 available, 1,252 variants, 65 collections) | Big enough that manual copy and merchandising never get done; small enough for an agent to finish in one batch run |
| Thin or empty descriptions | ~504-508 (51-52%) | Catalog/SEO agent target |
| No product type | 413 | Breaks filtering, Shopify search, Google Shopping and AI-agent feeds |
| Products with any tag | 15 | No structured attributes (protein, diet, cut, heat level, portion) for a meal builder to filter on |
| Vendor field inconsistent | e.g. "Costco" (129) vs "COSTCO" (31); "J&W Meal Butler" (159) vs "MEAL BUTLER" (106); "Kariba" vs "KARIBA"; "JW Foods Production" vs "JW Foods Production BAND SAW" | Data hygiene task an agent can fix in one pass |
| Products with no image | 59 | Visual studio agent target |
| Meal Butler SKUs | 265 (median price $9.99) | Core of the macro builder |
| Meal Butler SKUs with numeric macros in copy | ~6 (39 mention protein/calorie words at all) | **The main blocker for a macro coach.** The nutrition data agent must come first |
| Case/bulk SKUs | ~45 (e.g. 10 lb salmon case $175, 25-pack chicken burgers $35.50, beef burger cases $49-79) | Base for a B2B and wholesale price list |
| Whole-animal SKUs | 3 (quarter cow $1,200; whole lamb $400 deposit structure; half lamb $250) | Yield and carcass-balancing agent; premium bundles |
| Fulfilment | Order by Sunday; 6 weekly route days; $100 delivery minimum; express $30 | Order cut-off gives near-perfect demand visibility. Ideal for production forecasting, reorder nudges and route agents |
| Subscriptions, reviews, quiz, B2B portal | None | Greenfield |

---

## 2. Landscape: how AI agents are being used (2025-2026)

### 2.1 AI nutrition and macro coaches, meal-plan builders

| Company | What it does | Evidence | Grade |
|---|---|---|---|
| **Trifecta Nutrition** (US meal prep + app) | App has a macro calculator (inputs: goals, activity, body metrics) plus food logging and a barcode scanner. Meals customised to calorie and macro goals | [App Store listing](https://apps.apple.com/us/app/trifecta/id492100601); [Food Business News](https://www.foodbusinessnews.net/articles/16933-trifecta-bolsters-personalized-nutrition-services). **No source found** confirming a generative-AI meal planner | C |
| **HelloFresh / Factor** | Aug 2025: US$70M investment. Doubled the weekly menu to 100+ options. AI/ML personalised recommendations to "streamline decision making" as choice grows. The group president tied it to retention ("the more we invest in customers, the more they stay"). Nov 2025: AI in recipe-card production, with human chefs still creating recipes | [Bloomberg Government](https://news.bgov.com/artificial-intelligence/hellofresh-is-investing-70-million-to-have-ai-help-plan-dinner); [Business Wire](https://www.businesswire.com/news/home/20250804201495/en); [Food Manufacture](https://www.foodmanufacture.co.uk/Article/2025/11/24/hellofresh-uses-ai-to-accelerate-delivery-of-chef-created-recipes) | A/B |
| **Fresh Fitness Food** (London) | Quizzes height, weight and weekly workouts, then computes daily macros and the calorie surplus or deficit. Example: Fat Loss plan uses a 20% deficit with a 40/20/40 protein/carb/fat split; Muscle Gain uses a 10% deficit. Users can set custom macros; changes need 2 working days' notice. Trial from about £23/day for two meals | [City Matters](https://citymatters.london/counting-macros-fresh-fitness-food-math); [Women's Fitness](https://womensfitness.co.uk/?p=7585); Trustpilot (DE) 4.3 from 1,254 reviews: [link](https://de.trustpilot.com/review/freshfitnessfood.com?page=9) | B/C |
| **Noom: Welli AI assistant** | Launched June 2024 for 24/7 answers alongside human coaches. The CEO said it let Noom add 1:1 human coaching to Premium. A hybrid AI + human-escalation model | [Press release](https://www.fintechfutures.com/press-releases/noom-introduces-ai-enabled-products-to-enhance-on-demand-health-care-and-interactive-coaching); [TechTarget](https://techtarget.com/searchenterpriseai/news/366598870/Noom-CEO-on-the-need-for-AI-in-wellness-and-health) | B |
| **Cal AI → MyFitnessPal** | Photo-based calorie tracking. 15M+ downloads and US$30-40M+ annual revenue (figures vary by source). Acquired by MyFitnessPal (closed Dec 2025, announced Mar 2026) | [Fitt Insider](https://insider.fitt.co/myfitnesspal-acquires-rival-food-tracker-cal-ai/); [Let's Data Science](https://letsdatascience.com/news/cal-ai-sells-to-myfitnesspal-after-rapid-growth-f789c949) | B |
| **CookUnity** | Hiring staff ML scientists to build recommendation and ranking systems, measured with A/B tests and lift analysis. Delivers 35-50M meals/year (figures vary by posting) | [CookUnity careers](https://careers.cookunity.com/jobs/7507651003) | C |
| **Octane AI quizzes** (Shopify) | Product-finder quizzes. Wicked Edge: quiz-taker AOV $727 vs $450 store-wide (+61%); conversion 3.6% vs 1.5% | [Octane AI case study](https://octaneai.com/customers/wicked-edge); [platform claims](https://octaneai.com/platform) | B/C |
| **Personalisation, general** | Personalisation leaders achieve 5-15% revenue increases and 10-30% better marketing-spend efficiency | [McKinsey PDF](https://www.mckinsey.com/~/media/McKinsey/Business%20Functions/Marketing%20and%20Sales/Our%20Insights/The%20future%20of%20personalization%20and%20how%20to%20get%20ready%20for%20it/The-future-of-personalization-and-how-to-get-ready-for-it.pdf) | A/B |
| **Amazon Rufus** (shopping assistant) | Shoppers who engage are 60% more likely to purchase. Expected US$10B+ annual incremental sales. 250M users in 2025 (Q3 2025 earnings call) | [Fortune](https://www.fortune.com/2025/11/02/amazon-rufus-ai-shopping-assistant-chatbot-10-billion-sales-monetization) | A |

**Data sources and compliance J&W needs before building a macro coach:**
- **Health Canada Canadian Nutrient File (CNF).** Free, downloadable as CSV relational files; 2026 edition covers 5,993 foods and up to 173 nutrients. Values are averages, not brand-specific. [Nutrient Data](https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/nutrient-data.html); [CNF 2015 downloads](https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/nutrient-data/canadian-nutrient-file-2015-download-files.html). An agent can compute per-SKU macros from J&W recipes plus cooked yields plus CNF values.
- **Front-of-package "high in" symbol.** Mandatory since **January 1, 2026** for most prepackaged foods at or above thresholds (e.g. 15% DV) for saturated fat, sugars or sodium. [Packaging Insights](https://www.packaginginsights.com/news/canada-mandates-nutrition-symbol-2026.html); [Retail Council of Canada](https://www.retailcouncil.org/topics/food-grocery/food-product-labelling/front-of-package-nutrition-labelling/). Meat-specific and retail-packaged exemptions were **not verified** in this research; confirm with Health Canada/CFIA guidance before publishing panels.

**Takeaway for J&W:** The leaders (Fresh Fitness Food, Trifecta, Factor) all pair a goals intake with macro math and a menu filtered to those goals. J&W has the menu but not the macro data or tags. Build the data first, then the coach.

### 2.2 AI customer service on Shopify

| Tool | Resolution / automation evidence | Price evidence | Grade |
|---|---|---|---|
| **Shopify Sidekick** (merchant-side) | Winter '26 Edition (Dec 2025): moved from reactive to proactive (Sidekick Pulse tasks on Home). Generates admin apps from natural language, edits themes, builds segments and Flow workflows, saves reusable "skills". Never changes the shop without merchant approval | Included in Shopify admin (plan pricing not verified) | [Shopify Help: Sidekick](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick/features); [Shopifreaks](https://www.shopifreaks.com/shopify-unveils-winter-26-edition-with-major-upgrades-to-sidekick-and-new-ai-commerce-tools/); [Shopify Community](https://community.shopify.com/t/winter-editions-2026-is-now-out-highlights-for-merchants/579120). Grade B |
| **Gorgias AI Agent** (customer-side, Shopify-native) | Vendor advertises 60% automation. Named stories: ALOHAS 83%, Cocorico 48%, Orthofeet 56% ([Gorgias customers](https://www.gorgias.com/customers)). A competitor says published case studies land at 26-56% ([Ringly](https://www.ringly.io/blog/gorgias-ai-agent-pricing-per-resolution)). G2 response-accuracy score reportedly 59% vs 71% category average ([Ringly G2 analysis](https://www.ringly.io/blog/gorgias-g2-rating-2025)) | Helpdesk Starter $10, Basic $50-60, Pro $300-360, Advanced $750-900/mo. AI Agent **$0.90** (annual) / **$1.00** (monthly) per automated interaction; $1.50 overage ([Gorgias pricing](https://www.gorgias.com/pricing)) | B/C |
| **Intercom Fin** | 51% out of the box ([Anthropic customer story](https://www.anthropic.com/customers/intercom)). 56% average within 30 days ([AWS case study](https://aws.amazon.com/solutions/case-studies/intercom-anthropic/)). 67% average at the Fin 3 launch, 2025 ([CreateWith](https://www.createwith.com/tool/intercom/updates/intercom-ships-200-updates-in-2025-fin-3-reaches-67-average-resolution-rate)). 76% across 12,000+ customers, verified June 2026 ([AI Agent Index](https://theaiagentindex.com/agents/intercom-fin)) | **$0.99 per resolution**, 50-resolution monthly minimum ([Gleap](https://www.gleap.io/blog/intercom-fin-ai-pricing-2026)) | B/C |
| **Tidio Lyro** | Jiffy.com (ecommerce): 70% resolution "within weeks", 7,700 knowledge articles ([Tidio case study](https://www.tidio.com/customers/jiffy/)). Platform average 67%, with a 50% resolution guarantee on Plus/Premium ([mer.vin guide](https://mer.vin/2026/07/tidio-platform-guide-lyro-ai-agent-help-desk-and-flows-pricing/)) | Lyro standalone from **$32.50/mo** with 50 conversations; first 50 free on Free/Starter ([Tidio pricing](https://www.tidio.com/pricing/)) | B/C |
| **Daily Harvest** (frozen meal DTC) | AI guide "Sage" reported a 60% containment rate (2022) | [Quiq customer story PDF](https://Quiq.com/wp-content/uploads/2022/05/Daily-Harvest-Customer-Story.pdf) (figure from search summary; PDF text not extractable here) | B |

**Caveat:** "Containment" counts a customer who gave up the same as one who was helped. Measure resolution plus repeat contact plus CSAT ([Kaizo](https://kaizo.com/blog/what-is-containment-rate/)).

**Takeaway for J&W:** For a family business with an estimated low-thousands of tickets a month, the realistic target is 50-70% automated resolution of "where's my order / what's in this / which zone and day / can I change my order / is this gluten-free" questions. Allergen and medical questions must go to a human.

### 2.3 WhatsApp / SMS ordering bots

| Case | Result | Source | Grade |
|---|---|---|---|
| JioMart (India grocery, Haptik) | 200,000+ monthly orders via WhatsApp; 68% of users bought again | [Voicebot.ai](https://voicebot.ai/2022/12/29/whatsapp-chatbot-for-buying-groceries-spikes-repeat-purchase-rate-for-indian-grocery-chain-jiomart/) | B |
| Heritage Foods (dairy, WATI) | 2x higher order conversion after a WhatsApp-first catalog and ordering flow | [CaseStudies.com](https://www.casestudies.com/company/wati/case-study/heritage-foods-doubles-order-conversion-with-wati) | B/C |
| FreshVeget (Razorpay) | +25% conversion after in-chat payments | [Razorpay](https://razorpay.com/blog/?p=18260) | C |
| Bakery order bot (Indigitall) | 65% of inquiries resolved by bot; +30% repeat purchases | [Indigitall](https://indigitall.com/en/success-story/revolutionizing-e-commerce-order/) | C |
| Vico Food Box (Italian e-grocer, live chat + bot) | +8% AOV; 21.4% of earnings via chat | [Smartsupp](https://smartsupp.com/case-studies/vico-food-box-obtained-98-percent-customer-satisfaction-rating-and-increased-their-average-order-value-with-Smartsupp/) | B/C |

- **Channel economics:** WhatsApp moved to per-message pricing on July 1, 2025 ([Meta developer docs](https://developers.facebook.com/docs/whatsapp/pricing)). A May 2026 rate card lists Canada at 30.87 (marketing) / 4.20 (utility) / 0 (service). Units are unconfirmed in the snippet ([Salesforce-hosted rate card](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/WhatsApp-Business-Messaging-Rate-Card-MM-Lite-May-1-2026.pdf)). For SMS, a dataset of 246M+ sends shows 12.39% CTR, 0.12% conversion per send, $125 AOV, and about $0.15 per SMS ([Omnisend benchmarks](https://www.omnisend.com/blog/sms-marketing-benchmarks/)).
- **Canadian law (CASL):** SMS needs express, SMS-specific consent, sender identification, contact info and an easy "Reply STOP", and the business must be able to prove consent ([Telair CASL guide](https://www.telair.net/resources/knowledge-base/guides/casl-sms-compliance/); [BulkSMS](https://www.bulksms.com/resources/regulations/canadian-requirements-for-sending-commercial-sms-messages.htm)).
- **WhatsApp penetration among GTA customers: not found.** Estimate: SMS should be the default reorder channel and WhatsApp an opt-in for customers who prefer it.

**Takeaway for J&W:** The Sunday order cut-off suits a conversational reorder: "Hi Maria, same as last week (12 items, $164)? Reply YES, or tell me what to change." This works with no app download, which is the pattern behind JioMart's repeat rate.

### 2.4 AI demand forecasting and production planning for perishables

| Company / case | Result | Source | Grade |
|---|---|---|---|
| **Afresh** (fresh-department ordering AI) | Claims 25% shrink reduction and 80% fewer stockouts. CEO interview: 20-25% shrink reduction, 3-5% sales growth. Cub Foods CIO: 18% produce shrink cut after full rollout. Raised $34M (Apr 2026); live in 12,500+ departments in 40 states | [Afresh](https://www.afresh.com); [AndNowUKnow](https://andnowuknow.com/node/83880); [Supermarket News](https://www.supermarketnews.com/grocery-technology/how-afresh-is-revolutionizing-grocery-perimeters-with-ai); [Shelby Report](https://theshelbyreport.com/2026/04/21/afresh-raises-34m-to-scale-ai-across-grocery-industry/) | B/C |
| **Shelf Engine** (acquired by Crisp, Mar 2025) | Independent Pacific Coast Food Waste Commitment pilot (Afresh + Shelf Engine, two retailers): **14.8% food waste reduction per store**, with savings that more than covered the AI cost. Kimberton Whole Foods: +42% sales on managed items | [PCFWC pilot PDF](https://pacificcoastcollaborative.org/wp-content/uploads/2022/12/PCFWC-Case-Study_AI_Final.pdf); [Business Wire](https://www.businesswire.com/news/home/20250327362637/en/Crisp-Acquires-Shelf-Engine-AI-Demand-Planning-Solution-to-Support-Optimal-Retail-Forecasting-and-Inventory-Management); [Perishable News](https://perishablenews.com/retailfoodservice/kimberton-whole-foods-increases-sales-by-42-with-shelf-engine-ai/) | **A-/B** |
| **Crisp** | "Demand Forecasting Innovation of the Year" (June 2026). Ingests daily sales from 40+ retailers; no published accuracy figures found | [Crisp](https://gocrisp.com/blog/crisp-wins-demand-forecasting-innovation-award-for-ai-that-translates-to-real-world-supply-chains) | C |
| **PreciTaste at honeygrow** (restaurant prep AI) | 4-5 hours of prep time saved per location per day; "dramatic decrease" in waste (not quantified) | [Fast Casual](https://www.fastcasual.com/blogs/from-prep-to-profit-how-honeygrow-is-tackling-rising-costs-with-ai-automation/) | B |
| **Winnow at Compass Group Canada, Milton Cook Chill** (an Ontario production kitchen) | **18% reduction in food waste by value; $63,000/yr saved**; about 1.2 tons diverted | [CaseStudies.com](https://www.casestudies.com/company/winnow/case-study/compass-group-saves-63000-a-year-with-winnow) | B |
| **Winnow at Salem Health** | 33% waste cut by value; ROI in 17 weeks; 65% less salmon waste through repurposing | [CaseStudies.com](https://www.casestudies.com/company/winnow/case-study/salem-health-cuts-food-waste-33-with-winnow) | B |
| Academic (Favorita perishables data, 2026) | The model with the best accuracy metric was not the one with the least waste; XGBoost produced the lowest estimated waste. Optimise for waste, not just MAPE | [Oeconomica](https://www.oeconomica.org.ro/abstract/697/When-Accurate-Forecasts-Still-Produce-Waste-Demand-Shocks-and-Over-Forecasting.html) | A- |

**Canadian context:** 46.5% of food produced for Canada is wasted; avoidable waste is worth an estimated $58B (Second Harvest 2024 update) ([Second Harvest](https://wfprod.secondharvest.ca/post/new-report-from-second-harvest-reveals-canadas-58-billion-food-waste-problem); [CTV](https://www.ctvnews.ca/toronto/article/almost-half-of-all-food-wasted-in-canada-is-avoidable-new-report-suggests/)).

**Takeaway for J&W:** Afresh, Shelf Engine and Crisp are built for multi-store grocers and are overkill here. J&W's advantage is the Sunday cut-off: most route demand is known before cooking starts. The forecasting problem shrinks to three parts: (a) pickup, express and walk-in demand, (b) raw-material purchasing ahead of the cut-off, and (c) frozen safety-stock levels. A custom Claude agent with a simple statistical forecast fits this well, plus Winnow-style waste logging (a tablet and scale) to close the loop.

### 2.5 Meat cut-yield and carcass optimisation

- **Völur.** AI decides how each carcass should be sorted and cut. It generates daily cutting plans for JBS USA's Utah beef plant on Microsoft Azure ([Völur solutions](https://www.volur.ai/solutions)). Its site cites planning time falling from 2-6 hours (manual) to 15-30 seconds, plus a Yield Insights tool for trim-vs-boning decisions. Named users include Nortura (Norway) and Grupo D'Avinyó ([Völur](https://www.volur.ai/)). Grade B/C.
- **Vendor claim:** AI-driven precision cutting delivers 1-3% more yield per carcass ([Folio3 whitepaper](https://foodtech.folio3.com/whitepapers/ai-automation-for-the-meat-industry/)). Grade C, unverified.
- **ERP-level yield tracking** (actual vs expected yield per primal, sub-primal and retail cut): [inecta](https://www.inecta.com/meat-processing-software). Grade C.
- **No small-butcher AI yield case study was found.**

**Takeaway for J&W:** At J&W's scale, the value isn't robotic cutting. It's carcass balancing: matching which primals to buy and break against (a) raw-cut demand, (b) the cooked line's appetite for trim and secondary cuts (flank for fajitas, trim for burgers and meatballs), and (c) box and bundle promotions that move overstocked cuts. An agent on top of a simple yield-test log (cutter, primal, input weight, output by cut) can do this weekly.

### 2.6 AI dynamic pricing and markdowns for perishables

- **Wasteless (Spanish retailer, 12 weeks, salads, sandwiches and cut fruit):** waste down 32.7%, revenue up 6.2% ([Wasteless](https://wasteless.com/success/leading-spanish-retailer-cuts-waste-by-32)). An Italian retailer reportedly halved waste and gained 1.2 points of margin ([Wasteless resources](https://Wasteless.com/resources)). Results depend heavily on context ([FAO Agritech Observatory](https://agritechobservatory.review.fao.org/zh/wasteless)). Grade B.

**Takeaway for J&W:** Most Meal Butler stock is flash-frozen, so expiry-driven electronic shelf labels aren't the play. The lever is (a) the fresh raw counter and short-dated items, sold through a weekly "Butcher's Clearance" SMS/email drop, and (b) bundling overstocked cuts into boxes. Margin floors are set by the owner.

### 2.7 AI product descriptions, SEO and AI-shopping discoverability at catalog scale

- **Shopify Magic:** writes product descriptions in the admin; Shopify notes millions of its products have no description ([Shopify blog](https://www.shopify.com/blog/ai-product-descriptions)). A reviewer estimates 100 descriptions take about 20 minutes with Magic vs about 20 hours by hand, plus 8-10 hours of editing ([tenten](https://tenten.co/shopify/shopify-magic-ai-features-ranked/)). Grade C.
- **Measured SEO effects vary widely:**
  - +5.4% organic clicks for a major US retailer ([WordLift](https://wordlift.io/free-ai-product-description-generator/))
  - +18% organic traffic and +12% conversion on 1,200 SKUs ([VortexIQ](https://www.vortexiq.ai/?p=23886))
  - +112% year-on-year organic clicks after AI rewrites ([EXPRE / Sewing Online](https://expre.co.uk/?p=30658))
  - All vendor or agency results (grade C). Run a Search Console holdout.
- **AI shopping channels are growing fast:**
  - Shopify AI-attributed orders up 11x since Jan 2025 by Q3 2025 ([PYMNTS](https://www.pymnts.com/news/ecommerce/2025/shopify-president-agentic-ai-drives-11x-spike-in-orders))
  - Up 15x by Q4 2025 ([Digital Commerce 360](https://www.digitalcommerce360.com/2026/02/17/shopify-revenue-gmv-q4-2025/))
  - AI-referred traffic and orders tripled year over year in Q2 2026 ([PYMNTS](https://www.pymnts.com/earnings/2026/shopifys-ai-traffic-triples-as-shoppers-skip-the-search-bar/))
  - Grade A (earnings calls), small base.
  - Shopify's Agentic Storefronts list merchant products in ChatGPT, Perplexity and Copilot ([BetaKit](https://betakit.com/?p=397830)). **Canadian merchant eligibility was not confirmed.**
- **Why J&W's data matters:** AI assistants and Shopify search depend on structured product data. J&W's 413 blank product types and 15 tagged products mean it is close to invisible to these channels today.

### 2.8 AI-generated photography

- **Pebblely pricing:** listings run US$9/mo (30 images), $19/mo (200) and $39/mo (500), which is about $0.08-0.30 per image ([Kive comparison](https://kive.ai/learn/kive-vs-pebblely); [Capterra](https://www.capterra.com/p/10016326/Pebblely/)). Grade C. A professional food still-life example was priced around $500/image ([Wonderful Machine](https://wonderfulmachine.com/article/pricing-negotiating-combining-food-still-life-projects/)).
- **Best practice:** start from a clean, real product shot and use AI only for the scene or background ([tenten AI photography guide](https://tenten.co/shopify/ai-product-photography-shopify/)).
- **Takeaway for J&W:** Food must never be AI-altered to look different from what ships (an accuracy guardrail). Use AI for backgrounds, lifestyle scenes, ad resizes and the 59 missing images, all from real photos.

### 2.9 AI ad creative and campaign automation (Meta Advantage+)

- **Meta's own figures:** Advantage+ sales campaigns deliver +22% ROAS on average, and the GEM model improves conversions by up to 5% (Cannes 2025) ([eMarketer](https://www.emarketer.com/content/meta-launches-11-new-ai-ad-tools-cannes-lions-2025)). 30% more advertisers used AI creative tools in Q1 2025 ([PPC Land](https://ppc.land/metas-ad-business-soars-as-ai-tools-drive-16-revenue-growth-in-q1/)). Grade A-/B, company-reported.
- **Independent measurement (Haus, 640 geo-holdout tests):** Advantage+ beat manual only 42% of the time. It led by about 9% mid-test but finished about 12% *worse* on incremental ROAS once post-treatment effects were counted ([Haus](https://www.haus.io/meta); [Haus blog](https://www.haus.io/blog/the-meta-report-lessons-from-640-haus-incrementality-experiments)). Grade B.
- **Takeaway for J&W:** Use Advantage+ for catalog retargeting. Keep manual, zone-targeted prospecting (by delivery route day) and measure by geo holdout.

### 2.10 Klaviyo AI: predictive analytics and segments

- **Predictive metrics:** predicted CLV, churn risk, average time between orders and **expected date of next order**. Requirements: at least 500 customers who have placed orders, 180+ days of history, orders in the last 30 days, and some customers with 3+ orders ([Klaviyo Help](https://help.klaviyo.com/hc/en-us/articles/360020919731)). J&W (online since 2016, weekly ordering) very likely qualifies; this needs confirming in their account. Grade A (vendor docs).
- **Flows vs campaigns:** flows generate about 41% of email revenue from 5.3% of sends, with about 18x campaign revenue per recipient ([Klaviyo benchmarks](https://klaviyo.com/products/email-marketing/benchmarks)). Grade B.
- **K:AI and AI segments:** Klaviyo's K:AI Marketing Agent builds campaigns, flows and forms ([Klaviyo](https://marketing-origin-netlify.klaviyo.com/solutions/ai/marketing-agent)). AI segments are described in plain language ([Klaviyo](https://www.klaviyo.com/product/whats-new/segments-ai)). Force of Nature: +52% YoY Klaviyo-attributed value using AI segments ([Klaviyo blog](https://marketing-origin-netlify.klaviyo.com/blog/companies-using-ai-marketing)). Grade B/C.
- **Cart abandonment** averages 70.22% across 50 studies ([Baymard](https://baymard.com/lists/cart-abandonment-rate)). Grade A-.

### 2.11 Route optimisation for weekly delivery routes

| Case | Result | Source | Grade |
|---|---|---|---|
| **Inspired Go** (Canadian prepared-meal delivery, Onfleet) | Route planning 8-10 h/day cut to under 1 h (85%+). 72,000+ deliveries/month in Canada; about 10,000 in one day; new-market launch cut from about 3 months to 1-2 weeks | [Onfleet](https://onfleet.com/blog/case-studies-inspired-go/) | B |
| Thistle (prepared meals, Onfleet) | 10-20% more deliveries per day with the same staff; 95%+ on time | [Onfleet](https://onfleet.com/blog/thistle-case-study/) | B |
| Asian Veggies (grocery, Onfleet) | 83% less route-management time (was up to 1.5 h/day) | [Onfleet](https://onfleet.com/blog/case-study-asian-veggies/) | B |
| Fresh Prep (Western Canada meal kits, Onfleet) | Weekly push of orders to the routing engine triggers production | [Onfleet](https://onfleet.com/blog/case-study-fresh-prep/) | B |
| The Foodery (Boston meal delivery, Routific) | 28% lower delivery costs vs paper-and-pencil zip-code routing | [IoT ONE](https://v2.iotone.com/case-study/the-foodery-saves-28-on-delivery-costs-with-routific/c17543) | B |
| Food Made Fresh (Routific) | "4x more meals" (headline only) | [FeaturedCustomers](https://www.featuredcustomers.com/vendor/routific/case-studies) | C |

**Pricing:**
- Routific: free up to 100 orders/month; $150/month for 101-1,000 orders; unlimited drivers ([Capterra](https://www.capterra.ie/software/142530/routific); [Upper](https://www.upperinc.com/blog/routific-pricing/))
- Circuit for Teams: from about $100/month for 500 stops ([Circuit pricing](https://getcircuit.com/teams/pricing))

### 2.12 AI B2B prospecting (gyms, trainers, corporate, teams)

- **Clay:**
  - Qrew: half the sales team, about 2x positive replies, +40% meetings ([Clay](https://clay.com/blog/qrew-case-study))
  - Harmonic: 3x outbound reply rates ([Clay for Sales](https://www.clay.com/clay-for-sales))
  - 2026 pricing: Launch $185/mo ($167 annual) with 2,500 data credits; Growth $495/mo ([Valley](https://www.joinvalley.co/blog/clay-pricing-and-credits-explained-2026))
  - Grade B/C.
- **Apollo:**
  - Vendor claims +46% meetings with its AI Research Agent ([Apollo](https://www.apollo.io/solutions/small-businesses)). Grade C.
  - A solo founder's 60-day test: 4.2% reply rate, 12 then 18 meetings/month ([AI Agent Rank](https://aiagentrank.io/blog/apollo-io-review-2026)). Grade C, single anecdote.
  - Basic about $49-59/user/month ([Capterra](https://www.capterra.com/p/158696/Apollo/pricing/)).
- **Market size:** 9,493 fitness and recreational sports centre locations in Canada (June 2023) ([Statistics Canada](https://statcan.gc.ca/o1/en/plus/5329-working-out-numbers-your-gym-resolution)). Grade A. **GTA count not found.** Estimate: about 1,300-1,600 locations, assuming the GTA holds roughly 15-17% of Canada's population and gym density matches the national average. Needs verifying against the StatCan Business Register for Toronto (NAICS 71394).

### 2.13 AI voice agents for phone orders

- **Loman (vendor):** up to 22% higher phone revenue and up to 17% lower labour; a typical restaurant misses about 150 calls/month worth $35-85 each ([Loman](https://loman.ai/blog/restaurant-ai-phone-receptionist-revenue)). Grade C.
- **Hostie (vendor, modelled):** 87% fewer missed peak-hour calls ([Hostie](https://hostie.ai/resources/500k-call-study-ai-hosts-slash-missed-dinner-rush-calls-87-percent-revenue-impact)). Grade C.
- **Cost:**
  - Vapi platform fee $0.05/min plus model and telephony; all-in commonly $0.07-0.31/min ([Ainora](https://ainora.lt/blog/ai-voice-agent-cost-per-minute-2026); [Fora Soft](https://www.forasoft.com/blog/article/vapi-vs-retell-vs-custom))
  - Retell infra about $0.055/min plus TTS/LLM ([Macha](https://www.getmacha.com/blog/retell-ai-vs-vapi))
- **Takeaway for J&W:** The store line (416) 298-1350 is staffed only Mon-Fri 9-6 and Sat 10-4, so evenings and Sundays (the order-cut-off day) are uncovered. An after-hours voice agent that answers menu, zone and order-status questions and texts a pre-filled cart link is low-risk and measurable.

### 2.14 AI review generation and response

- **Spiegel Research Center (with PowerReviews data):**
  - A product with 5 reviews has 270% higher purchase likelihood than one with none. The effect is +190% for lower-priced and +380% for higher-priced items.
  - The first five reviews matter most, and purchase likelihood peaks at 4.2-4.5 stars.
  - Source: [Spiegel](https://spiegel.medill.northwestern.edu/from-reviews-to-revenue/). Grade B (correlational).
- **Responding to reviews:**
  - Hotels that started responding on TripAdvisor got 12% more reviews and +0.12 stars (HBR, via [Buffer](https://buffer.com/resources/replying-to-google-reviews/))
  - Diminishing returns past about a 40% response rate (Cornell, via [Hotel Management](https://www.hotelmanagement.net/operate/go-ahead-respond-to-online-reviews-but-not-all-them))
  - SMBs replying to more than 20% of reviews earned 33% more revenue (Womply, vendor, 200k businesses, [WP Business Reviews](https://wpbusinessreviews.com/review-management-increased-revenue-200000-small-businesses/))
  - Grade B/C.
- **Local search:** reviews remain a top local ranking and conversion factor ([Whitespark 2023 study summary](https://www.j2nj.com/?p=775)). Grade B.
- **Tooling:** Judge.me includes AI reply drafts, summaries and translation in its $15/month plan, with merchant approval per reply ([Judge.me](https://judge.me/app/ai-review-features)).
- **J&W today:** zero on-site reviews.

### 2.15 AI loyalty, retention and subscriptions

- **Recharge Retain (AI cancellation insights and offers):**
  - Over 700,000 subscriptions saved; up to 33% of cancellations saved
  - **Open Farm** (Toronto pet-food brand): 29% churn reduction
  - **Wild Grain** (frozen bakery subscription): 22% of cancellations saved
  - Source: [Recharge](https://getrecharge.com/products/retain/cancellation-prevention/). Grade B.
- **Smile.io:** loyalty members show a 56% higher repeat purchase rate and 16.5% higher AOV with rewards coupons. This is non-randomised, so it overstates causality ([eCommerce Fastlane](https://ecommercefastlane.com/the-state-of-ecommerce-customer-loyalty-in-2023/)). Grade C.
- **ButcherBox:** segmented members by taste and buying habits and offered alternatives to at-risk box types ([Microsoft](https://news.microsoft.com/transform/from-farm-to-cloud-to-table-butcherbox-serves-up-a-new-approach-to-meat-delivery/)). A support vendor estimated each 1% of churn reduction protects $5M for ButcherBox ([CaseStudies.com / Hugo](https://www.casestudies.com/company/hugo-118434/case-study/butcherbox-protects-20m-30m-annually-with-hugo)). Grade B/C.

### 2.16 Canadian adoption context

- 12.2% of Canadian businesses used AI to produce goods or deliver services in Q2 2025, up from 6.1% a year earlier ([Statistics Canada](https://www150.statcan.gc.ca/n1/pub/11-621-m/11-621-m2025008-eng.pdf); [BetaKit](https://betakit.com/statscan-finds-ai-adoption-has-doubled-in-businesses-but-hasnt-yet-affected-headcounts/)). Grade A.
- **Implication:** an Ontario-inspected butcher and meal-prep business that runs AI well is still an early adopter.
- **Not verified (no search budget left):** government AI-adoption funding programs (e.g. NRC IRAP) available to J&W. Worth a follow-up.

---

## 3. Using the Claude API for J&W's custom agents

**Pricing** (USD per million tokens, from [Claude pricing docs](https://platform.claude.com/docs/en/about-claude/pricing), Oct 2026):

| Model (API id) | Input | Output | Cache hit | Batch (50% off) | Best J&W use |
|---|---|---|---|---|---|
| Claude Opus 5.5 (`claude-opus-5-5`) | $4 | $20 | $0.20 | $2 / $10 | Weekly planning and reasoning: production forecast review, carcass balancing, ads and business review, catalog rewrite (batch) |
| Claude Sonnet 5.5 (`claude-sonnet-5-5`) | $2 | $10 | $0.10 | $1 / $5 | Customer-facing chat (concierge, Macro Butler, SMS reorder), outreach drafting |
| Claude Haiku 5.5 (`claude-haiku-5-5`) | $0.10 | $0.50 | $0.01 | $0.05 / $0.25 | High-volume classification: ticket triage, review sentiment, tagging, intent routing on voice/SMS |

Other line items: web search $10 per 1,000 searches. Managed Agents runtime is $0.08 per session-hour plus tokens, which suits scheduled weekly agents. Prompt caching cuts repeated catalog and policy context to 5% of input price on Opus/Sonnet 5.5.

**Worked cost estimates** (all labelled estimates; token counts assumed):
- **Catalog rewrite, one-off, 979 SKUs**, Opus 5.5 batch, about 3,000 input + 800 output tokens each: 979 × (3,000×$2 + 800×$10)/1M ≈ **$14**.
- **Concierge chat, 3,000 conversations/month**, 6 turns each, Sonnet 5.5: per turn ~7k cached tokens ($0.0007) + 1k new ($0.002) + 300 output ($0.003) ≈ $0.0057, so about $0.034 per conversation, **≈ $100/month**. Gorgias AI Agent for the same volume would be about $0.90-1.00 per automated interaction, or roughly $1,350-1,500/month at 1,500 automated ([Gorgias pricing](https://www.gorgias.com/pricing)). Custom build cost is extra, but run cost is about 10x lower.
- **Macro Butler, 1,000 plan sessions/month**, 4 turns, ~10k context (9k cached), 800 output, Sonnet 5.5: ≈ **$45-50/month**.
- **Weekly production and carcass planning run**, Opus 5.5: ~200k input + 20k output ≈ $1.20/run, **≈ $5/month**.

**Architecture pattern:**
- Shopify Admin API, Klaviyo API, the routing tool's API and a Google Sheet or Postgres "ops data" store serve as tools.
- Agents propose and humans approve, through Shopify Flow tasks, Slack/email approval links, or Sidekick-style review.
- Use strict tool schemas. Give Claude the catalog and policies via cached system context. Use structured outputs for anything written back to Shopify.

---

## 4. Fifteen candidate AI agents for J&W

Each agent lists: **Job**, **Inputs**, **Outputs**, **Human checkpoint**, **Lever**, **Evidence**, **Build (buy/build, model)**, **Est. run cost** and **KPI**.

### Agent 1: "Macro Butler" AI meal-plan and macro coach
- **Job:** Turn a 60-second goals intake into a 5-7 day J&W meal plan with exact SKUs, portion sizes and daily calorie/protein/carb/fat totals, then a one-click cart or subscription.
- **Inputs:**
  - Goal (cut / maintain / gain / performance), sex, age, height, weight, training days
  - Dietary rules (no pork, pescatarian, dairy-free, halal *if* certified product exists), budget, delivery zone and day
  - J&W catalog with computed macros and tags (from Agent 2); live stock
- **Outputs:** Plan by day and meal; cart permalink; "subscribe weekly" option; macro summary PDF/email; swaps ("prefer salmon over chicken Tue").
- **Human checkpoint:**
  - A registered dietitian or nutrition professional signs off the calculation rules and the macro database, not each plan.
  - Any medical condition, pregnancy, eating-disorder signal or allergy is routed to a human with a "consult your doctor" message.
  - The owner approves plan templates.
- **Lever:** New-customer conversion, AOV, subscription uptake (revenue).
- **Evidence:**
  - Fresh Fitness Food and Trifecta use the same intake-to-macros model.
  - HelloFresh invested $70M in AI personalisation for retention.
  - Octane AI quizzes: +61% AOV / 2.4x conversion for one brand.
  - Amazon Rufus users are 60% more likely to buy.
  - McKinsey: 5-15% revenue from personalisation (all §2.1).
- **Build:** Custom (Claude Sonnet 5.5 + Shopify Storefront API + quiz front end). Octane AI is an off-the-shelf quiz alternative, but it can't do the macro math.
- **Est. run cost:** about $50/month in tokens.
- **KPI:** Quiz-to-cart rate, plan-to-order conversion, plan-to-subscription %, AOV.

### Agent 2: Nutrition data and label agent
- **Job:** Compute and maintain verified macro and allergen data for all 265 Meal Butler SKUs, and the main raw SKUs, from recipes, cooked yields and Health Canada CNF values. Draft nutrition-facts-style panels and front-of-package "high in" flags. Write structured attributes (protein g, kcal, carbs, fat, allergens, diet tags) to Shopify metafields.
- **Inputs:** Recipes and ingredient weights; raw-to-cooked yield tests; CNF CSV; supplier spec sheets; current product pages.
- **Outputs:** Per-SKU nutrition table (per 4 oz / 6 oz variant); metafields; "macros" block on product pages; flags where a claim (e.g. "salt and sugar free") needs a compliance check; lab-test shortlist for the top 20 SKUs.
- **Human checkpoint:**
  - A nutrition professional or food-labelling consultant approves every published panel and claim.
  - Lab analysis for best-sellers.
  - CFIA/Health Canada labelling exemptions confirmed before printing labels.
- **Lever:** Enabler for Agent 1, SEO and B2B (gyms and dietitians need macros). Conversion on product pages.
- **Evidence:** Only ~6 of 265 Meal Butler SKUs show numeric macros today (§1). CNF is free and covers 5,993 foods / 173 nutrients. FOP labelling has been mandatory since Jan 1, 2026 (§2.1).
- **Build:** Custom (Claude Opus 5.5 with code execution for calculations; batch). One-off build plus maintenance on recipe changes.
- **Est. run cost:** under $25 one-off in tokens; negligible ongoing.
- **KPI:** % of SKUs with verified macros (target 100% of Meal Butler); PDP conversion on SKUs with macros vs without.

### Agent 3: "Butler Concierge" 24/7 support and sales chat
- **Job:** Answer on site chat, email and Instagram DMs:
  - Order status; "which day does my area get delivery?"; Sunday cut-off; $100 minimum
  - Substitutions; storage and reheating; what's in a box; loyalty points
- **Inputs:** Shopify orders and customers; route and zone table; policies; catalog plus macros; FAQ; past tickets.
- **Outputs:** Resolved conversations; product recommendations with cart links; tagged escalations with a summary; weekly "top questions" report that feeds back into the FAQ and catalog.
- **Human checkpoint:**
  - Refunds and credits above a set dollar threshold, allergen and medical questions, and complaints about food quality or safety go to staff.
  - Weekly sampled transcript review.
- **Lever:** Support cost and staff time; conversion of browsing visitors.
- **Evidence:**
  - Intercom Fin 51-76%; Tidio Lyro 70% (Jiffy); Gorgias named stories 48-83% (26-56% per a competitor)
  - Daily Harvest 60% containment
  - Vico Food Box: 21.4% of earnings via chat (§2.2-2.3)
- **Build:** Option A: Gorgias Basic/Pro plus AI Agent ($0.90-1.00/interaction). Option B: custom Claude Sonnet 5.5 widget, Haiku 5.5 for triage (about $100/month at 3,000 conversations).
- **KPI:** Automated resolution rate (with CSAT and repeat-contact checks), first-response time, chat-assisted revenue.

### Agent 4: Auto-reorder and subscription agent (SMS / WhatsApp)
- **Job:** Turn weekly cart-rebuilders into subscribers. Before the Sunday cut-off, text each customer a pre-built cart based on their pattern and predicted next order ("Same as last week, $164? Reply YES / SKIP / CHANGE"). Handle edits in natural language. Run AI cancellation-save flows (pause, skip, swap, delivery-day change before discount).
- **Inputs:** Order history; Klaviyo expected-next-order date and churn risk; subscription app (Shopify Subscriptions or Recharge); stock; route-day schedule; SMS consent records.
- **Outputs:** Confirmed draft orders and subscriptions; payment links; skip/pause events; cancellation reasons dataset; weekly retention report.
- **Human checkpoint:**
  - The owner sets discount ceilings and save-offer rules.
  - The customer must confirm every order (no silent charges).
  - CASL consent verified before any send.
  - Staff review exception queue (out-of-stock swaps, address changes).
- **Lever:** Purchase frequency, retention, predictability of production (revenue + cost).
- **Evidence:**
  - JioMart: 68% repeat via WhatsApp ordering
  - Heritage Foods: 2x conversion
  - Recharge saves up to 33% of cancellations; Open Farm (Toronto) 29% churn reduction; Wild Grain 22%
  - Klaviyo predicts next order date; ButcherBox treats churn as its key lever (§2.3, 2.10, 2.15)
- **Build:** Buy the subscription app plus a custom Claude Sonnet 5.5 conversational layer over SMS (Twilio or Klaviyo SMS) and optional WhatsApp.
- **Est. run cost:** tokens about $30-60/month; SMS about $0.15/message benchmark ([Omnisend](https://www.omnisend.com/blog/sms-marketing-benchmarks/)).
- **KPI:** % of active customers on subscription or auto-reorder; orders per customer per month; save rate; SMS reply-to-order rate.

### Agent 5: Lifecycle marketing agent (Klaviyo predictive + AI copy)
- **Job:** Build and maintain flows and segments:
  - Welcome by goal; abandoned cart; post-purchase reheating tips
  - "Running low" timed to expected next order; churn-risk win-back; VIP; whole-animal and BBQ seasonal; weekly menu email
- **Inputs:** Klaviyo predictive metrics; Shopify events; catalog/macros; promotions calendar; review snippets.
- **Outputs:** Drafted flows, campaigns and subject-line tests; segment definitions; weekly performance and next-best-test report.
- **Human checkpoint:** The owner approves every campaign before send and every new flow before activation; CASL consent and unsubscribe checks are automatic.
- **Lever:** Repeat revenue, recovered carts (revenue).
- **Evidence:** Flows earn about 41% of email revenue from 5.3% of sends (about 18x RPR); cart abandonment averages 70.22%; Force of Nature +52% YoY using AI segments (§2.10).
- **Build:** Buy (Klaviyo, K:AI) plus a Claude Opus 5.5 copy and strategy layer in J&W's voice ("Eat Clean - Train Mean - Live Lean").
- **Est. run cost:** under $10/month in tokens. Klaviyo plan cost not verified.
- **KPI:** Flow revenue share, revenue per recipient, win-back rate of churn-risk segment.

### Agent 6: Production forecast and prep-sheet agent
- **Job:** Every Sunday night after cut-off (and mid-week for pickup and express), forecast unit demand per SKU and variant. Produce the cook, portion, vacuum-pack and flash-freeze plan, the raw-material purchase list by supplier, and frozen safety-stock targets.
- **Inputs:** Closed route orders; historical pickup, express and walk-in sales; seasonality and holidays; promotions; current frozen inventory; yields (raw to cooked); supplier lead times; waste log.
- **Outputs:** Monday production schedule by station; purchase orders (drafts); par levels; stockout and overproduction alerts; weekly forecast-vs-actual and waste report.
- **Human checkpoint:** The production manager approves the plan and all purchase orders; the owner approves new par levels.
- **Lever:** Food cost and waste, labour hours, stockouts (cost + revenue protection).
- **Evidence:**
  - Independent PCFWC pilot: 14.8% waste reduction per store
  - Afresh: 18-25% shrink cuts
  - PreciTaste at honeygrow: 4-5 h/day prep time saved
  - Winnow at an Ontario cook-chill kitchen: 18% waste cut by value, $63k/yr
  - Academic: optimise for waste, not accuracy alone (§2.4)
- **Build:** Custom (Python forecast plus Claude Opus 5.5 for plan reasoning and exceptions; Managed Agents scheduled weekly). Optionally Winnow-style waste logging (tablet plus scale).
- **Est. run cost:** about $5/month in tokens.
- **KPI:** Forecast error by SKU; waste % of production; stockouts per week; prep labour hours per 100 portions.

### Agent 7: Carcass and cut-yield optimiser
- **Job:** Each week, decide which primals and whole animals to buy and how to break them, so raw-cut demand, cooked-line usage (trim to burgers and meatballs, flank to fajitas, chicken to cooked breast) and box promotions consume the whole animal at the best margin. Track cutter-level yield tests.
- **Inputs:** Yield-test log (cutter, primal, in-weight, out-weight by cut, trim, waste); purchase prices; demand forecast (Agent 6); whole-animal orders (quarter cow, lamb); cooked recipes.
- **Outputs:** Cut plan; buy list; "overstocked cut" alerts sent to Agent 8 and Agent 5 (bundle/box promo suggestions); yield variance by cutter and supplier; margin-per-carcass report.
- **Human checkpoint:** The head butcher approves the cut plan; the owner approves supplier changes.
- **Lever:** Gross margin through yield and full-carcass utilisation; waste (cost).
- **Evidence:** Völur cut planning (2-6 h down to 15-30 s at JBS and others); vendor claim of 1-3% more yield per carcass (unverified); ERP yield tracking (§2.5). No small-butcher case found.
- **Build:** Custom (Google Sheet/Postgres log plus Claude Opus 5.5 with code execution for the optimisation).
- **Est. run cost:** about $5/month.
- **KPI:** Yield % by primal vs baseline; trim sold-through %; margin per carcass.

### Agent 8: Smart markdown and "Butcher's Clearance" agent
- **Job:** Identify short-dated fresh items, slow movers and overstocked cuts. Set tiered markdowns within owner-set floors. Package them into bundles or "deal of the week". Push a weekly clearance drop to an opted-in SMS/email segment and the store counter.
- **Inputs:** Inventory with pack dates; sell-through velocity; margin floors; Agent 7 alerts.
- **Outputs:** Price changes (drafts); bundle SKUs; clearance campaign; recovered-revenue report.
- **Human checkpoint:** The owner approves all price changes; hard floor rules (never below cost plus X%); food-safety date rules enforced.
- **Lever:** Waste turned into revenue; margin recovery (cost + revenue).
- **Evidence:** Wasteless: -32.7% waste, +6.2% revenue in 12 weeks; Italian retailer halved waste and gained 1.2 margin points (§2.6).
- **Build:** Custom (Claude Sonnet 5.5 plus Shopify Admin API price drafts).
- **Est. run cost:** under $10/month.
- **KPI:** Waste $ per week; clearance revenue; margin on clearance.

### Agent 9: Catalog, SEO and AI-shopping readiness agent
- **Job:**
  - Rewrite the ~504-508 thin descriptions and fill product types for the 413 SKUs missing one.
  - Normalise vendors (Costco/COSTCO, J&W Meal Butler/MEAL BUTLER, etc.); add tags (protein, cut, diet, portion, cooking method, heat).
  - Write alt text, SEO titles and meta; build collection landing pages ("meal prep delivery Toronto", "Ontario lamb", "air-chilled chicken").
  - Add structured data; fix nav errors (fresh/frozen fruit swap, "mediteranian" URL redirect).
  - Keep the catalog clean as new SKUs are added daily.
- **Inputs:** Shopify catalog; Agent 2 metafields; brand voice guide; Search Console; competitor keyword set.
- **Outputs:** Bulk product updates (drafts); redirect list; collection pages; weekly SEO and AI-channel report.
- **Human checkpoint:** Staff spot-check a random 10% sample. Every health, nutrition, origin or "no hormones" claim goes to an approval queue. The owner approves nav changes.
- **Lever:** Organic traffic; on-site search; conversion; discoverability in ChatGPT, Copilot, Perplexity and Google AI channels (revenue).
- **Evidence:**
  - Shopify Magic: 100 descriptions in about 20 min (vs 20 h)
  - SEO lifts of +5.4% to +112% (vendor and agency)
  - Shopify AI-channel orders up 11x/15x and tripling YoY (§2.7)
  - Spiegel: product information and reviews drive purchase likelihood (§2.14)
- **Build:** Shopify Magic for ad-hoc edits plus a custom Claude Opus 5.5 batch pipeline for the bulk rewrite and ongoing QA.
- **Est. run cost:** about $14 one-off; under $5/month ongoing.
- **KPI:** % of SKUs with complete copy, type and tags (target 100%); organic sessions and revenue (holdout vs control set); AI-referred sessions.

### Agent 10: Visual content studio agent
- **Job:** Fill the 59 missing images. Create consistent lifestyle and background variants from real product photos. Produce ad sizes, menu cards and short-form video stills for each week's menu.
- **Inputs:** Real product photos taken in-house (phone light box); brand guide; menu calendar.
- **Outputs:** Approved images for product pages, Meta/IG and email; weekly content pack.
- **Human checkpoint:** The owner approves every image. Hard rule: the food itself is never AI-generated or altered; only background and scene are.
- **Lever:** Conversion; ad performance; content cost (revenue + cost).
- **Evidence:** AI product-photo tools run about $0.08-0.30/image vs about $500/image for a professional food still-life example; best practice is a real product shot plus AI scene (§2.8). Meta reports 30% more advertisers using AI creative (§2.9).
- **Build:** Buy (Shopify Magic image tools, Pebblely or similar) plus a Claude Sonnet 5.5 brief-writer and QA checklist.
- **Est. run cost:** about $20-40/month in tools.
- **KPI:** % of SKUs with imagery; PDP conversion; ad CTR and CPA by creative.

### Agent 11: Paid ads optimiser agent (Meta / Google)
- **Job:** Run Advantage+ catalog retargeting and zone-targeted manual prospecting (by route day and postal code). Launch and rotate creative from Agent 10. Read results weekly with geo holdouts by delivery zone. Propose budget shifts.
- **Inputs:** Ad accounts; Shopify orders by postal code; route map; margin per SKU; creative library.
- **Outputs:** Weekly test plan; creative briefs; budget-change proposals; incrementality readout.
- **Human checkpoint:** The owner approves any budget change above a set % and all new creative; a monthly spend cap is enforced.
- **Lever:** New-customer acquisition cost; new-zone growth (revenue).
- **Evidence:** Meta: +22% ROAS for Advantage+ (company-reported). Haus (640 tests): Advantage+ wins only 42% of the time and ends about 12% worse on incremental ROAS, so balance and test (§2.9).
- **Build:** Buy (Meta Advantage+, Google PMax) plus a custom Claude Opus 5.5 weekly analyst.
- **Est. run cost:** under $10/month in tokens (ad spend separate).
- **KPI:** New customers per week; CAC; incremental ROAS by zone.

### Agent 12: Route and delivery experience agent
- **Job:** Optimise the six weekly routes and the express runs. Send ETA texts and live tracking. Run "your driver is in your area Wednesday; add items by Sunday" upsells. Flag route density to decide new zones, pickup partners or lockers (e.g. partner gyms).
- **Inputs:** Orders by address and route day; driver availability; vehicle capacity and cold-chain limits; routing tool (Routific/Onfleet/Circuit).
- **Outputs:** Optimised routes; driver manifests; customer ETA and proof-of-delivery texts; zone-density map; new-zone recommendations.
- **Human checkpoint:** The dispatcher approves routes; the owner approves zone or pricing changes.
- **Lever:** Delivery cost per drop; driver hours; capacity; CX and retention (cost + revenue).
- **Evidence:** Inspired Go (Canada): 8-10 h/day of planning down to under 1 h, with 72,000+ deliveries/month. Thistle: 10-20% more deliveries per day. The Foodery: -28% delivery cost (§2.11).
- **Build:** Buy (Routific from free to $150/month for 101-1,000 orders, or Onfleet) plus a Claude Sonnet 5.5 messaging and analysis layer.
- **Est. run cost:** $0-150/month for the tool plus under $10 in tokens.
- **KPI:** Planning hours per week; cost per drop; on-time %; deliveries per driver-hour.

### Agent 13: B2B prospecting and account agent (gyms, trainers, corporate, teams, schools)
- **Job:** Build and work target lists along the existing route corridors:
  - GTA gyms and boutique studios, personal trainers, physio and dietitian clinics
  - Corporate offices (wellness lunches), sports teams and academies, daycares, restaurants and caterers (wholesale heritage)
- **What it does with them:** Personalised outreach, tasting-box offers, gym-fridge consignment proposals, wholesale price sheets from the ~45 case/bulk SKUs, follow-ups and reorder reminders for won accounts.
- **Inputs:** Clay/Apollo enrichment; Google Maps listings; route zones; B2B price list; case studies and testimonials; CRM.
- **Outputs:** Qualified lead lists; drafted sequences; booked tastings; proposals; account health reports (reorder cadence, churn risk).
- **Human checkpoint:** Erwin or the owner approves each sequence and offer. Pricing and terms above set limits are approved by the owner. CASL compliance check on every commercial message.
- **Lever:** New B2B revenue stream; larger, steadier weekly volume (revenue).
- **Evidence:** Clay: Qrew 2x replies and +40% meetings, Harmonic 3x reply rates. Apollo SMB test: 4.2% reply rate, 12-18 meetings/month. 9,493 fitness centres in Canada (GTA estimated at about 1,300-1,600) (§2.12).
- **Build:** Buy (Clay Launch $185/month or Apollo Basic about $49-59/user/month) plus Claude Opus 5.5 for research and personalisation.
- **Est. run cost:** about $200-250/month all-in.
- **KPI:** Meetings booked; accounts won; B2B weekly revenue; account retention.

### Agent 14: Phone and after-hours voice order agent
- **Job:** Answer (416) 298-1350 after hours and on overflow, especially Sunday, the cut-off day, when the store is closed. Answer menu, zone, delivery-day, macro and order-status questions. Take orders by texting a pre-filled cart or payment link. Book pickups and whole-animal deposits. Log every call.
- **Inputs:** Catalog plus macros; zones and route days; order lookup; policies; SMS sending.
- **Outputs:** Answered calls; cart links sent; call summaries; missed-demand report (what people asked for that J&W doesn't sell).
- **Human checkpoint:** Escalation and voicemail to staff for complaints, custom cut orders, large B2B orders and allergen questions. The customer confirms the order in the cart (the agent never charges cards by voice).
- **Lever:** Captured revenue from missed calls; staff time (revenue + cost).
- **Evidence:** Restaurants miss about 150 calls/month at $35-85 each, and voice AI reports up to 22% higher phone revenue (vendor). Modelled 87% cut in missed peak calls (vendor). Cost about $0.07-0.31/min (§2.13).
- **Build:** Buy a voice platform (Retell/Vapi) with Claude Sonnet 5.5 as the reasoning model, or Haiku 5.5 for low-latency routing.
- **Est. run cost:** about $40-190/month at 600 minutes.
- **KPI:** Calls answered after hours; cart links sent to orders; revenue per call.

### Agent 15: Review and reputation agent
- **Job:**
  - Ask for product reviews (Judge.me) and Google reviews after second delivery and once the customer has eaten (timed around 5-7 days).
  - Draft replies to every review; summarise themes; route quality complaints ("chicken dry", "portion small", "late delivery") to the kitchen or dispatcher within 24 hours.
  - Surface UGC and testimonials for Agents 5, 10 and 13.
- **Inputs:** Delivered orders; review platforms; Google Business Profile; social mentions.
- **Outputs:** Review requests; reply drafts; weekly sentiment and issue report; testimonial library.
- **Human checkpoint:** All replies to 1-3 star reviews are human-approved. The agent never offers compensation without approval, and never solicits or writes fake or incentivised-without-disclosure reviews.
- **Lever:** Conversion (social proof), local SEO, quality feedback loop (revenue + cost).
- **Evidence:** 5 reviews vs 0 = 270% purchase likelihood, +380% for higher-priced items (Spiegel). Responding gives 12% more reviews and +0.12 stars (HBR via Buffer). Judge.me AI replies are included at $15/month (§2.14). J&W currently has zero reviews.
- **Build:** Buy (Judge.me) plus Claude Haiku 5.5 for sentiment and Sonnet 5.5 for reply drafts.
- **Est. run cost:** about $20/month.
- **KPI:** Reviews per month; average rating; % of reviews answered (target 100% of negative, 40%+ overall); Google rating and review count.

**Orchestration layer (optional, not counted): Owner's weekly business review.** A Monday digest built from Shopify (Sidekick plus a Claude Opus 5.5 scheduled agent):
- Sales by channel and zone, margin, waste, subscription churn
- Top support issues, review themes, B2B pipeline
- Three recommended actions to approve

---

## 5. Which levers add up to an extra $1M/year (illustrative sizing)

**J&W revenue, order count, traffic and AOV were not found.** Every number below is an **illustrative estimate** with its assumptions stated, meant to be replaced with J&W's Shopify data. The assumed AOV of $140 rests on the $100 delivery minimum plus multi-item weekly carts.

| Agent | Formula (assumptions) | Illustrative annual revenue |
|---|---|---|
| 4 Auto-reorder/subscription | 150 customers moved from ~1.2 to ~2.2 orders/month × 12 × $140 | ≈ $252k |
| 13 B2B accounts | 15 accounts (gyms, PT studios, corporate, teams) × $350/week × 48 weeks | ≈ $252k |
| 1 Macro Butler (+2 data) | 600 completed plans/month × 8% convert × $140 ≈ $81k first orders; plus 25% of converters repeat 1.5×/month for ~4 months ≈ $121k | ≈ $150-200k |
| 5 Lifecycle + cart recovery | Flows reaching ~25-35% of email revenue (Eightx SMB guidance; see [Eightx](https://eightx.co/blog/average-klaviyo-flow-revenue-contribution-benchmarks)); depends on list size (not found) | ≈ $60-100k |
| 14 Voice/after-hours | 40 captured orders/month × $140 × 12 | ≈ $67k |
| 9, 10, 11, 15 Conversion stack | +10-15% conversion on existing online revenue (base not found) | Scales with base |
| 6, 7, 8, 12 Margin and ops | Waste, yield and delivery savings (e.g. 18% waste cut at an Ontario cook-chill kitchen = $63k/yr at Compass's scale) | Cost-side, not revenue |
| **Total of revenue rows shown** | | **≈ $780k-870k**, plus the conversion stack, which plausibly reaches $1M+ |

---

## 6. Suggested sequencing (by dependency)

1. **Weeks 0-4, foundation:**
   - Agent 9 (catalog clean-up, types, tags, vendor normalisation)
   - Agent 2 (macros for the top 50 Meal Butler SKUs first)
   - Agent 15 (reviews start accruing immediately)
   - Agent 3 (concierge on FAQs)
2. **Weeks 4-8, revenue engines:**
   - Agent 4 (subscriptions plus SMS reorder before Sunday cut-off)
   - Agent 5 (Klaviyo predictive flows)
   - Agent 1 (Macro Butler on the top 50 SKUs, expanding as Agent 2 completes)
3. **Weeks 8-12, growth and ops:**
   - Agent 13 (B2B pilot: 50 gyms on GTA 2 and GTA 4 routes)
   - Agent 12 (routing)
   - Agent 6 (production forecast)
   - Agent 14 (after-hours voice)
4. **Quarter 2:**
   - Agent 7 (yield log plus carcass planning)
   - Agent 8 (markdowns)
   - Agent 10 (content studio)
   - Agent 11 (incrementality-tested ads)

---

## 7. Guardrails and risks

- **Nutrition and health claims:** A human professional approves all macro data, panels and claims ("salt and sugar free", "no hormones"). No medical advice; medical, pregnancy and eating-disorder cases are escalated. Confirm front-of-package and labelling obligations and exemptions with Health Canada/CFIA.
- **Allergens:** Allergen answers never come from an LLM's general knowledge. They come only from the approved per-SKU allergen field, or the question goes to a human.
- **CASL:** Express, SMS-specific consent with proof; sender ID and STOP in every message ([Telair](https://www.telair.net/resources/knowledge-base/guides/casl-sms-compliance/)).
- **Pricing and money:** Agents draft; humans approve price changes, refunds above a threshold, and discount ceilings. Voice and SMS agents send payment links rather than taking card numbers.
- **Imagery honesty:** Never alter the food in images. Never write or incentivise undisclosed reviews.
- **Measurement:** Use holdouts (SEO control set, geo holdouts for ads, matched cohorts for reorder nudges). Vendor case-study numbers are directional, not guarantees.
- **Privacy:** Keep customer data in Shopify, Klaviyo and J&W-controlled stores. Send agents only the fields they need.

---

## 8. Research gaps (not found or not verified)

- J&W revenue, order volume, traffic, AOV, list sizes, ticket volume, call volume (needed to replace estimates).
- GTA gym and studio count; WhatsApp usage share among GTA consumers.
- Small-butcher AI yield case study; Afresh-style results for a single-site meal-prep producer.
- Shopify Agentic Storefronts eligibility for Canadian merchants.
- Canadian AI-adoption funding programs (e.g. NRC IRAP). Not searched, because the web-search budget for this run was exhausted.
- Klaviyo, Recharge and Shopify Subscriptions pricing for J&W's tier.

---

## 9. Sources (grouped)

**Customer service:**
[Gorgias pricing](https://www.gorgias.com/pricing) ·
[Gorgias customers](https://www.gorgias.com/customers) ·
[Ringly on Gorgias pricing](https://www.ringly.io/blog/gorgias-ai-agent-pricing-per-resolution) ·
[Ringly G2 analysis](https://www.ringly.io/blog/gorgias-g2-rating-2025) ·
[AI Agent Index: Fin](https://theaiagentindex.com/agents/intercom-fin) ·
[CreateWith: Fin 3](https://www.createwith.com/tool/intercom/updates/intercom-ships-200-updates-in-2025-fin-3-reaches-67-average-resolution-rate) ·
[AWS: Intercom](https://aws.amazon.com/solutions/case-studies/intercom-anthropic/) ·
[Anthropic: Intercom](https://www.anthropic.com/customers/intercom) ·
[Gleap: Fin pricing](https://www.gleap.io/blog/intercom-fin-ai-pricing-2026) ·
[Tidio: Jiffy](https://www.tidio.com/customers/jiffy/) ·
[Tidio pricing](https://www.tidio.com/pricing/) ·
[mer.vin Tidio guide](https://mer.vin/2026/07/tidio-platform-guide-lyro-ai-agent-help-desk-and-flows-pricing/) ·
[Quiq: Daily Harvest](https://Quiq.com/wp-content/uploads/2022/05/Daily-Harvest-Customer-Story.pdf) ·
[Kaizo: containment](https://kaizo.com/blog/what-is-containment-rate/) ·
[Shopify Help: Sidekick](https://help.shopify.com/en/manual/shopify-admin/productivity-tools/sidekick/features) ·
[Shopifreaks: Winter '26](https://www.shopifreaks.com/shopify-unveils-winter-26-edition-with-major-upgrades-to-sidekick-and-new-ai-commerce-tools/) ·
[Shopify Community: Winter '26](https://community.shopify.com/t/winter-editions-2026-is-now-out-highlights-for-merchants/579120)

**Nutrition and personalisation:**
[Trifecta App Store](https://apps.apple.com/us/app/trifecta/id492100601) ·
[Food Business News: Trifecta](https://www.foodbusinessnews.net/articles/16933-trifecta-bolsters-personalized-nutrition-services) ·
[BGov: HelloFresh $70M](https://news.bgov.com/artificial-intelligence/hellofresh-is-investing-70-million-to-have-ai-help-plan-dinner) ·
[Business Wire: HelloFresh](https://www.businesswire.com/news/home/20250804201495/en) ·
[Food Manufacture: HelloFresh AI](https://www.foodmanufacture.co.uk/Article/2025/11/24/hellofresh-uses-ai-to-accelerate-delivery-of-chef-created-recipes) ·
[City Matters: Fresh Fitness Food](https://citymatters.london/counting-macros-fresh-fitness-food-math) ·
[Women's Fitness](https://womensfitness.co.uk/?p=7585) ·
[Trustpilot: FFF](https://de.trustpilot.com/review/freshfitnessfood.com?page=9) ·
[Noom Welli](https://www.fintechfutures.com/press-releases/noom-introduces-ai-enabled-products-to-enhance-on-demand-health-care-and-interactive-coaching) ·
[TechTarget: Noom](https://techtarget.com/searchenterpriseai/news/366598870/Noom-CEO-on-the-need-for-AI-in-wellness-and-health) ·
[Fitt: Cal AI](https://insider.fitt.co/myfitnesspal-acquires-rival-food-tracker-cal-ai/) ·
[Let's Data Science: Cal AI](https://letsdatascience.com/news/cal-ai-sells-to-myfitnesspal-after-rapid-growth-f789c949) ·
[CookUnity careers](https://careers.cookunity.com/jobs/7507651003) ·
[Octane AI: Wicked Edge](https://octaneai.com/customers/wicked-edge) ·
[Octane AI platform](https://octaneai.com/platform) ·
[McKinsey: personalization](https://www.mckinsey.com/~/media/McKinsey/Business%20Functions/Marketing%20and%20Sales/Our%20Insights/The%20future%20of%20personalization%20and%20how%20to%20get%20ready%20for%20it/The-future-of-personalization-and-how-to-get-ready-for-it.pdf) ·
[Fortune: Rufus](https://www.fortune.com/2025/11/02/amazon-rufus-ai-shopping-assistant-chatbot-10-billion-sales-monetization) ·
[Health Canada: nutrient data](https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/nutrient-data.html) ·
[CNF downloads](https://www.canada.ca/en/health-canada/services/food-nutrition/healthy-eating/nutrient-data/canadian-nutrient-file-2015-download-files.html) ·
[Packaging Insights: FOP](https://www.packaginginsights.com/news/canada-mandates-nutrition-symbol-2026.html) ·
[Retail Council: FOP](https://www.retailcouncil.org/topics/food-grocery/food-product-labelling/front-of-package-nutrition-labelling/)

**Messaging:**
[Voicebot: JioMart](https://voicebot.ai/2022/12/29/whatsapp-chatbot-for-buying-groceries-spikes-repeat-purchase-rate-for-indian-grocery-chain-jiomart/) ·
[WATI: Heritage Foods](https://www.casestudies.com/company/wati/case-study/heritage-foods-doubles-order-conversion-with-wati) ·
[Razorpay](https://razorpay.com/blog/?p=18260) ·
[Indigitall](https://indigitall.com/en/success-story/revolutionizing-e-commerce-order/) ·
[Smartsupp: Vico](https://smartsupp.com/case-studies/vico-food-box-obtained-98-percent-customer-satisfaction-rating-and-increased-their-average-order-value-with-Smartsupp/) ·
[Meta WhatsApp pricing](https://developers.facebook.com/docs/whatsapp/pricing) ·
[WhatsApp rate card May 2026](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/WhatsApp-Business-Messaging-Rate-Card-MM-Lite-May-1-2026.pdf) ·
[Omnisend SMS benchmarks](https://www.omnisend.com/blog/sms-marketing-benchmarks/) ·
[Telair: CASL](https://www.telair.net/resources/knowledge-base/guides/casl-sms-compliance/) ·
[BulkSMS: Canada](https://www.bulksms.com/resources/regulations/canadian-requirements-for-sending-commercial-sms-messages.htm)

**Forecasting, waste, yield, pricing:**
[Afresh](https://www.afresh.com) ·
[AndNowUKnow](https://andnowuknow.com/node/83880) ·
[Supermarket News](https://www.supermarketnews.com/grocery-technology/how-afresh-is-revolutionizing-grocery-perimeters-with-ai) ·
[Shelby Report](https://theshelbyreport.com/2026/04/21/afresh-raises-34m-to-scale-ai-across-grocery-industry/) ·
[PCFWC pilot](https://pacificcoastcollaborative.org/wp-content/uploads/2022/12/PCFWC-Case-Study_AI_Final.pdf) ·
[Crisp acquires Shelf Engine](https://www.businesswire.com/news/home/20250327362637/en/Crisp-Acquires-Shelf-Engine-AI-Demand-Planning-Solution-to-Support-Optimal-Retail-Forecasting-and-Inventory-Management) ·
[Kimberton](https://perishablenews.com/retailfoodservice/kimberton-whole-foods-increases-sales-by-42-with-shelf-engine-ai/) ·
[Crisp award](https://gocrisp.com/blog/crisp-wins-demand-forecasting-innovation-award-for-ai-that-translates-to-real-world-supply-chains) ·
[Fast Casual: honeygrow](https://www.fastcasual.com/blogs/from-prep-to-profit-how-honeygrow-is-tackling-rising-costs-with-ai-automation/) ·
[Winnow: Compass Milton](https://www.casestudies.com/company/winnow/case-study/compass-group-saves-63000-a-year-with-winnow) ·
[Winnow: Salem Health](https://www.casestudies.com/company/winnow/case-study/salem-health-cuts-food-waste-33-with-winnow) ·
[Oeconomica study](https://www.oeconomica.org.ro/abstract/697/When-Accurate-Forecasts-Still-Produce-Waste-Demand-Shocks-and-Over-Forecasting.html) ·
[Second Harvest](https://wfprod.secondharvest.ca/post/new-report-from-second-harvest-reveals-canadas-58-billion-food-waste-problem) ·
[CTV](https://www.ctvnews.ca/toronto/article/almost-half-of-all-food-wasted-in-canada-is-avoidable-new-report-suggests/) ·
[Völur](https://www.volur.ai/) ·
[Völur solutions](https://www.volur.ai/solutions) ·
[Folio3 whitepaper](https://foodtech.folio3.com/whitepapers/ai-automation-for-the-meat-industry/) ·
[inecta](https://www.inecta.com/meat-processing-software) ·
[Wasteless: Spain](https://wasteless.com/success/leading-spanish-retailer-cuts-waste-by-32) ·
[Wasteless resources](https://Wasteless.com/resources) ·
[FAO: Wasteless](https://agritechobservatory.review.fao.org/zh/wasteless)

**Catalog, SEO, creative, ads:**
[Shopify blog: AI descriptions](https://www.shopify.com/blog/ai-product-descriptions) ·
[tenten: Shopify Magic](https://tenten.co/shopify/shopify-magic-ai-features-ranked/) ·
[WordLift](https://wordlift.io/free-ai-product-description-generator/) ·
[VortexIQ](https://www.vortexiq.ai/?p=23886) ·
[EXPRE](https://expre.co.uk/?p=30658) ·
[PYMNTS 11x](https://www.pymnts.com/news/ecommerce/2025/shopify-president-agentic-ai-drives-11x-spike-in-orders) ·
[DC360 Q4 2025](https://www.digitalcommerce360.com/2026/02/17/shopify-revenue-gmv-q4-2025/) ·
[PYMNTS Q2 2026](https://www.pymnts.com/earnings/2026/shopifys-ai-traffic-triples-as-shoppers-skip-the-search-bar/) ·
[BetaKit: Agentic Storefronts](https://betakit.com/?p=397830) ·
[Kive vs Pebblely](https://kive.ai/learn/kive-vs-pebblely) ·
[Capterra: Pebblely](https://www.capterra.com/p/10016326/Pebblely/) ·
[Wonderful Machine](https://wonderfulmachine.com/article/pricing-negotiating-combining-food-still-life-projects/) ·
[tenten: AI photography](https://tenten.co/shopify/ai-product-photography-shopify/) ·
[eMarketer: Meta Cannes](https://www.emarketer.com/content/meta-launches-11-new-ai-ad-tools-cannes-lions-2025) ·
[PPC Land: Meta Q1](https://ppc.land/metas-ad-business-soars-as-ai-tools-drive-16-revenue-growth-in-q1/) ·
[Haus: Meta report](https://www.haus.io/meta) ·
[Haus blog](https://www.haus.io/blog/the-meta-report-lessons-from-640-haus-incrementality-experiments)

**Lifecycle, loyalty, reviews:**
[Klaviyo predictive analytics](https://help.klaviyo.com/hc/en-us/articles/360020919731) ·
[Klaviyo benchmarks](https://klaviyo.com/products/email-marketing/benchmarks) ·
[Klaviyo K:AI agent](https://marketing-origin-netlify.klaviyo.com/solutions/ai/marketing-agent) ·
[Klaviyo segments AI](https://www.klaviyo.com/product/whats-new/segments-ai) ·
[Klaviyo: AI marketing examples](https://marketing-origin-netlify.klaviyo.com/blog/companies-using-ai-marketing) ·
[Eightx: flow share](https://eightx.co/blog/average-klaviyo-flow-revenue-contribution-benchmarks) ·
[Baymard](https://baymard.com/lists/cart-abandonment-rate) ·
[Recharge Retain](https://getrecharge.com/products/retain/cancellation-prevention/) ·
[Smile.io data](https://ecommercefastlane.com/the-state-of-ecommerce-customer-loyalty-in-2023/) ·
[Microsoft: ButcherBox](https://news.microsoft.com/transform/from-farm-to-cloud-to-table-butcherbox-serves-up-a-new-approach-to-meat-delivery/) ·
[Hugo: ButcherBox](https://www.casestudies.com/company/hugo-118434/case-study/butcherbox-protects-20m-30m-annually-with-hugo) ·
[Spiegel](https://spiegel.medill.northwestern.edu/from-reviews-to-revenue/) ·
[Buffer: HBR](https://buffer.com/resources/replying-to-google-reviews/) ·
[Hotel Management: Cornell](https://www.hotelmanagement.net/operate/go-ahead-respond-to-online-reviews-but-not-all-them) ·
[Womply](https://wpbusinessreviews.com/review-management-increased-revenue-200000-small-businesses/) ·
[Judge.me AI](https://judge.me/app/ai-review-features) ·
[Whitespark summary](https://www.j2nj.com/?p=775)

**Delivery, B2B, voice:**
[Onfleet: Inspired Go](https://onfleet.com/blog/case-studies-inspired-go/) ·
[Onfleet: Thistle](https://onfleet.com/blog/thistle-case-study/) ·
[Onfleet: Asian Veggies](https://onfleet.com/blog/case-study-asian-veggies/) ·
[Onfleet: Fresh Prep](https://onfleet.com/blog/case-study-fresh-prep/) ·
[IoT ONE: Foodery](https://v2.iotone.com/case-study/the-foodery-saves-28-on-delivery-costs-with-routific/c17543) ·
[FeaturedCustomers: Routific](https://www.featuredcustomers.com/vendor/routific/case-studies) ·
[Capterra: Routific](https://www.capterra.ie/software/142530/routific) ·
[Upper: Routific pricing](https://www.upperinc.com/blog/routific-pricing/) ·
[Circuit pricing](https://getcircuit.com/teams/pricing) ·
[Clay: Qrew](https://clay.com/blog/qrew-case-study) ·
[Clay for Sales](https://www.clay.com/clay-for-sales) ·
[Valley: Clay pricing](https://www.joinvalley.co/blog/clay-pricing-and-credits-explained-2026) ·
[Apollo SMB](https://www.apollo.io/solutions/small-businesses) ·
[AI Agent Rank: Apollo](https://aiagentrank.io/blog/apollo-io-review-2026) ·
[Capterra: Apollo](https://www.capterra.com/p/158696/Apollo/pricing/) ·
[StatCan: gyms](https://statcan.gc.ca/o1/en/plus/5329-working-out-numbers-your-gym-resolution) ·
[Loman](https://loman.ai/blog/restaurant-ai-phone-receptionist-revenue) ·
[Hostie](https://hostie.ai/resources/500k-call-study-ai-hosts-slash-missed-dinner-rush-calls-87-percent-revenue-impact) ·
[Ainora: voice pricing](https://ainora.lt/blog/ai-voice-agent-cost-per-minute-2026) ·
[Fora Soft](https://www.forasoft.com/blog/article/vapi-vs-retell-vs-custom) ·
[Macha: Retell vs Vapi](https://www.getmacha.com/blog/retell-ai-vs-vapi)

**Canada and Claude:**
[StatCan: AI adoption](https://www150.statcan.gc.ca/n1/pub/11-621-m/11-621-m2025008-eng.pdf) ·
[BetaKit: StatCan AI](https://betakit.com/statscan-finds-ai-adoption-has-doubled-in-businesses-but-hasnt-yet-affected-headcounts/) ·
[Claude API pricing](https://platform.claude.com/docs/en/about-claude/pricing)

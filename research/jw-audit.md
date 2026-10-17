# J&W Foods / J&W Meal Butler: off-site audit

Prepared for Minastech (Erwin Garcia) · Research date: **October 16, 2026**
Scope: what the business looks like from outside its own website. That covers reputation, social, press, wholesale, people, third-party data, tech stack, search visibility and a revenue estimate.
Companion files: `jw-facts.md` (on-site facts) and `jw-catalog.json` (979-product digest).

> **Method note.** Every figure below links to its source. Where no figure could be found, the report says **"not found"** and gives an **estimate** with its reasoning. The shared web-search quota for this run ran out partway through. After that, evidence came only from direct page fetches: review directories, the business's own social profiles, government lists, the Shopify storefront and ISED/StatCan benchmarks. Owler and RocketReach in particular were **not checked**. A follow-up run can cover them.

---

## 1. Key findings (TL;DR)

1. **Customers rate it highly, but the website shows none of that.** Google shows **4.8★ from 611 reviews** and Facebook **4.6★ from 56** ([Yably aggregate](https://yably.ca/reviews/toronto/j-w-foods-2201-brimley-road)). The Shopify store has **no reviews app**, so this social proof never reaches the product pages.
2. **Review volume roughly doubled in about 2.5–3 years.** A Google-sourced snapshot whose newest review is from March 2023 showed **4.7★ / 295 reviews** ([Chamber of Commerce](https://canada.chamberofcommerce.com/business-directory/ontario/scarborough/food-products-supplier/534332-j-w-foods)). Today's count is 611, so the customer base is active and growing.
3. **The owner is the brand.** Reviews repeatedly name **"Bill"** (co-founder **William Fehr**), his wife **Tasia** and his son **Lucas**. Customers praise the personal education and service. This is also the main risk: a 2020 Yelp review accuses Bill of offensive COVID-19 remarks ([Yelp](https://www.yelp.ca/biz/jw-foods-scarborough-2)).
4. **Instagram is the only social channel with real reach.** It has **30K followers and 3,736 posts** ([Instagram](https://www.instagram.com/jwfoods/)). Facebook has **5,021 followers** and its last public post is from **Jan 5, 2024** ([Facebook](https://www.facebook.com/jandwfoods/)). A second, abandoned Facebook page with 576 followers last posted in 2013. TikTok **@jwfoods has 132 followers** and no visible videos, even though the Instagram bio claims "5M+ Views On TikTok". There is **no owned YouTube channel**.
5. **There is wholesale history but no B2B offer today.** Evidence includes restaurant supply ([Alignable, 2018](https://www.alignable.com/toronto-on/jw-foods-inc/jwfoods-com-jul-2018)), a third-party retail placement (Michael-Angelo's Market Place) and a WagJag deal. The firm holds a **2026 federal chicken import quota as a "processor"**: it is one of about 203 WTO and about 205 CPTPP processor-category holders ([WTO list](https://www.international.gc.ca/trade-commerce/controls-controles/chicken-poulet/wto_processor-2026-omc_transformateurs.aspx?lang=eng), [CPTPP list](https://www.international.gc.ca/trade-commerce/controls-controles/chicken-poulet/cptpp_processor-2026-ptpgp_transformateurs.aspx?lang=eng)). Despite all this, the website has **no wholesale page, B2B pricing or account portal**.
6. **The operation is small and family-run.** It had about **15 employees** in 2018, by its own description ([Alignable](https://www.alignable.com/toronto-on/jw-foods-inc/jwfoods-com-jul-2018)). ZoomInfo puts it at **<25 employees and <$5M revenue**. D&B lists modelled sales of about **$1.07M** with **Steven (Stavros) Trougakos as President** ([D&B](https://www.dnb.com/business-directory/company-profiles.j__w_foods_inc.66f5b22e4d6f7d525e9da24a692e5e47.html), [ZoomInfo](https://www.zoominfo.com/c/j--w-foods-inc/411664737)).
7. **The tech stack is thin.** It runs on Shopify with the **Refresh** theme (v13.0.1), **Smile.io** loyalty, **Shopify Inbox** chat, a **Meta pixel** and a **TikTok pixel**. There is **no subscription app** (no selling plans on products), **no reviews app**, **no email-marketing app** detected on the storefront and **no Google Analytics/GTM tag** in the theme.
8. **Search visibility is close to zero for non-brand terms.** JW was not in the top 12 DuckDuckGo-Canada results for "meal prep Toronto" and is absent from all three Toronto meal-delivery round-ups checked. The site's meta description is a hashtag list, and its title does not contain "Toronto", "meal prep" or "butcher".
9. **The listings contradict each other, which hurts local SEO and trust.** Hours differ across the website, Yelp and other directories. One directory uses a different postal code. The delivery minimum is shown as $100 on one page and $130 on another. The business lists three contact emails. The Instagram bio says **"CFIA Approved"**, but the website says **Ontario (provincially) inspected**. A provincial licence limits sales to within Ontario.
10. **Revenue estimate (CAD, all channels): low $1.2M · mid $2.5M · high $4.0M.** See section 10.

---

## 2. Reputation: ratings and review counts

| Platform | Rating | Count | As-of / note | Source |
|---|---|---|---|---|
| **Google** | **4.8 / 5** | **611** | Via Yably aggregator, fetched Oct 16, 2026. Yably's hours stamp is 20/08/2025, so the count is mid-2025 or later | [Yably](https://yably.ca/reviews/toronto/j-w-foods-2201-brimley-road) |
| Google (older snapshot) | 4.7 / 5 | 295 | Newest review shown is Mar 19, 2023. Distribution: **270 five-star, 2 four, 1 three, 0 two, 22 one-star** | [Chamber of Commerce](https://canada.chamberofcommerce.com/business-directory/ontario/scarborough/food-products-supplier/534332-j-w-foods) |
| Facebook (main page) | 4.6 / 5 · "92% recommend" | 56 (Yably) / 53 (FB) | Fetched Oct 16, 2026 | [Yably](https://yably.ca/reviews/toronto/j-w-foods-2201-brimley-road), [Facebook](https://www.facebook.com/jandwfoods/) |
| Facebook (old "JW Foods Inc." page) | 94% recommend | 19 | Dormant since 2013 | [Facebook](https://www.facebook.com/p/JW-Foods-Inc-100068059854436/) |
| Yelp | 4.0 / 5 | 13 (+14 "not recommended") | Claimed listing, "$$", categories Grocery / Meat Shops / Food Delivery Services | [Yelp](https://www.yelp.ca/biz/jw-foods-scarborough-2) |
| Unilocal | 3.8 / 5 | 4 | Old reviews copied from Yelp | [Unilocal](https://unilocal.net/canada/toronto/jw-foods) |
| RestaurantGuru | not found | — | No listing found before the search quota ran out | — |

Google's own page could not be opened directly. The Google figures above come from two aggregators that pull Google data.

### Recurring themes in reviews

**Positive (most of the 5-star reviews):**
- **The owner is personally involved.** "Bill" explains products, educates customers and "goes the extra mile". Reviews call him "an owner who is completely hands on" and say customers are treated "like family" ([Chamber](https://canada.chamberofcommerce.com/business-directory/ontario/scarborough/food-products-supplier/534332-j-w-foods), [Yably](https://yably.ca/reviews/toronto/j-w-foods-2201-brimley-road), [Yelp](https://www.yelp.ca/biz/jw-foods-scarborough-2)).
- **Meat quality.** Steaks, brisket bacon, bison and venison get specific praise, and reviewers say it is better than supermarket meat.
- **Value.** Reviewers say "You really can't find better value for the quality" (Yelp, 2013) and "prices are great especially for organic food" (Yelp, 2025).
- **Meal Butler convenience.** Customers like that there is no oil and everything is baked, and that the boil-in-bag pouches mean no pots to wash. One reviewer orders for a **prediabetic** family member, which shows a health and medical audience beyond fitness (Yelp, Sep 2025).
- **Fitness community and referrals.** Reviewers call the store "a shopping haven for body builders and fitness enthusiasts". One heard about JW "from somebody at my gym", and a personal trainer says "I recommend all of my clients" ([Chamber](https://canada.chamberofcommerce.com/business-directory/ontario/scarborough/food-products-supplier/534332-j-w-foods)).
- **Delivery and fast pick-up readiness.** Reviewers mention next-business-day pick-up and quick delivery of a first order.
- **Community events.** One reviewer mentions a networking event held at or by JW in 2023.

**Negative (about 7–8% one-star on the 2023 Google snapshot, plus Yelp):**
- **Owner conduct and politics.** A 2020 Yelp review reports offensive remarks about COVID-19 deaths among seniors. A 2023 reviewer defends Bill's "stance on covid". This is a live reputation risk ([Yelp](https://www.yelp.ca/biz/jw-foods-scarborough-2)).
- **Inconsistent counter service.** A 2015 review alleges unequal treatment at the cash and calls the souvlaki "bland". Bill replied publicly and offered a free replacement, which shows the owner does respond to reviews.
- **Location and access.** Customers describe the store as "a bit far" and say they don't go to Scarborough often, and it is closed on Sundays. Convenience is the friction point.
- **Price vs Costco on commodity items.** One reviewer says frozen broccoli costs more than at Costco.

---

## 3. Social media

| Channel | Handle | Followers | Activity | Source |
|---|---|---|---|---|
| **Instagram** | @jwfoods ("JW Foods 🇬🇷🇨🇦") | **30K** (following 1,323) | **3,736 lifetime posts**. Bio: "Family-Founded · Est. 1995 / 5M+ Views On TikTok / Premium Meats \| CFIA Approved / Toronto, ON GTA Delivery / Collabs: Jwfoodscontenttt@gmail.com" | [Instagram](https://www.instagram.com/jwfoods/) |
| **Facebook** (main) | /jandwfoods | **5,021** followers · 18 "talking about this" · 256 "were here" | **Last public post: Jan 5, 2024** (a TikTok link). Logged-out view shows nothing newer, so the page is effectively dormant | [Facebook](https://www.facebook.com/jandwfoods/) |
| Facebook (duplicate) | "JW Foods Inc." | 576 | Last post Apr 15, 2013. Lists john@jwfoods.com | [Facebook](https://www.facebook.com/p/JW-Foods-Inc-100068059854436/) |
| **TikTok** | @jwfoods | **132** followers · 124 likes | No public videos visible. Bio: "Processor of Fine Foods! Eat Clean, Train Mean, Live Lean!" | [TikTok](https://www.tiktok.com/@jwfoods) |
| TikTok (linked from FB, Jan 2024) | @williamfehr3rd | 0 | The account is now empty, renamed or wiped. The "5M+ views" claim **could not be verified** | [TikTok](https://www.tiktok.com/@williamfehr3rd) |
| **YouTube** | none owned | — | Homepage video is "JW Foods Promotional Video" by a third party (@byprincejohn), Oct 26, 2018, **3,137 views**. Also "JW Foods @ CANFITPRO Toronto 2014" by @pixcode, **716 views** | [video 1](https://www.youtube.com/watch?v=w6IBvPqv6TI), [video 2](https://www.youtube.com/watch?v=VtOHjKZoTvc) |
| X / Twitter | @jwfoods | not found | The website's link to it is broken | [x.com/jwfoods](https://x.com/jwfoods) |

**Instagram posting cadence: not verifiable.** Instagram now requires a login to see post dates. The 3,736 lifetime posts and a dedicated "Collabs" email address suggest the account is still active and run partly by an outside or creator contact. That is an inference only. Facebook is clearly abandoned, and its last post was a cross-post of a TikTok video.

**Implications:** the 30K Instagram audience is the biggest owned asset after the customer list. Instagram, Facebook and TikTok have very different audience sizes, so a short-video and UGC engine (Reels, TikTok, YouTube Shorts) is wide open. The duplicate Facebook page should be merged into the main one.

---

## 4. Press, awards, events and sponsorships

- **Press or news coverage: not found.** The searches made before the quota ran out returned only directory listings and JW's own pages. JW does not appear in blogTO, Toronto Life or the meal-delivery round-ups checked (see section 9).
- **Awards: not found.**
- **Fitness trade shows and events, from older evidence:**
  - Exhibited at **CanFitPro Toronto 2014** ([YouTube](https://www.youtube.com/watch?v=VtOHjKZoTvc)).
  - Had a booth at **"Me First Fitness", Ajax**, in July 2018 ([Alignable](https://www.alignable.com/toronto-on/jw-foods-inc/jwfoods-com-jul-2018)).
  - In 2013, posted outreach to out-of-town athletes competing at the **TO Pro Super Show** (a bodybuilding show), offering food support ([Facebook](https://www.facebook.com/p/JW-Foods-Inc-100068059854436/)). It is unclear whether this was a paid sponsorship.
  - Says it has been "catering to a lot of pro athletes for the last 25 Years" ([Alignable](https://www.alignable.com/toronto-on/jw-foods-inc/jwfoods-com-jul-2018)).
- **Gym and trainer channel:** this channel is informal. Referrals happen by word of mouth (see the reviews). A fitness studio site once had a "JW Foods" page, but its domain (back2basicsfitnessandhealth.com) **no longer resolves**. No formal gym partner programme was found.
- **Deals and marketplaces:** a **WagJag** voucher (souvlaki box of 50) was redeemed through **Michael-Angelo's Market Place** in 2011 ([Yelp](https://www.yelp.ca/biz/jw-foods-scarborough-2)).

---

## 5. Wholesale and B2B today

| Evidence | What it shows | Source |
|---|---|---|
| A 2018 self-description says JW "provides fresh and frozen food to the public **and restaurants**" | Foodservice sales existed as of 2018 | [Alignable](https://www.alignable.com/toronto-on/jw-foods-inc/jwfoods-com-jul-2018) |
| The old Facebook link preview titles the site "J & W Foods Inc - **Wholesaler & Retail Outlet** Scarborough" | Wholesale was once part of the positioning | [Facebook](https://www.facebook.com/p/JW-Foods-Inc-100068059854436/) |
| D&B classifies the firm under **grocery and related product wholesaling** | Its registered activity is wholesale | [D&B](https://www.dnb.com/business-directory/company-profiles.j__w_foods_inc.66f5b22e4d6f7d525e9da24a692e5e47.html) |
| **2026 WTO and CPTPP chicken TRQ quota holder, processor category** (one of about 203 and about 205 holders nationally) | JW is a recognised chicken processor that holds a federal import allocation, a scarce asset in a supply-managed market | [WTO list](https://www.international.gc.ca/trade-commerce/controls-controles/chicken-poulet/wto_processor-2026-omc_transformateurs.aspx?lang=eng), [CPTPP list](https://www.international.gc.ca/trade-commerce/controls-controles/chicken-poulet/cptpp_processor-2026-ptpgp_transformateurs.aspx?lang=eng) |
| Retail placement at Michael-Angelo's Market Place in 2011 | JW has supplied other retailers before | [Yelp](https://www.yelp.ca/biz/jw-foods-scarborough-2) |
| Products sold online as cases: 4 kg chicken breast cases at $100, a 10 lb salmon case at $175, a 10-bag ground beef case at $103, 25-pack burgers. The homepage banner says "BUY IN BULK & SAVE". Meta keywords include #wholesalechicken and #wholesaleprices | There is semi-wholesale demand from consumers and trainers | `jw-catalog.json`, homepage HTML |
| **No** wholesale page, B2B application, tiered pricing, net terms or account portal in the site's sitemap (15 pages) | The B2B channel is not productised online | [sitemap](https://www.jwfoods.com/sitemap.xml) |

Yelp shows a **sponsored foodservice competitor**, Woodward Meats, in the "You might also consider" slot on JW's own listing ([Yelp](https://www.yelp.ca/biz/jw-foods-scarborough-2)). Foodservice meat suppliers are already bidding for JW's audience.

**Conclusion:** JW very probably still does some restaurant and trade business informally, by phone and relationships. There is **no visible, scalable B2B channel**. That gap, combined with the provincially inspected plant and the chicken quota, is the strongest base for the "+$1M" plan.

---

## 6. Ownership, people and headcount

| Person | Role (as evidenced) | Source |
|---|---|---|
| **Stavros "Steve/Steven" Trougakos** | Co-founder (1995). **President / key principal** per D&B and ZoomInfo | [About](https://www.jwfoods.com/pages/about-us), [D&B](https://www.dnb.com/business-directory/company-profiles.j__w_foods_inc.66f5b22e4d6f7d525e9da24a692e5e47.html), [ZoomInfo](https://www.zoominfo.com/c/j--w-foods-inc/411664737) |
| **William "Bill" Fehr** | Co-founder. The public face and floor operator. Replies to Yelp reviews as "Business Owner". LinkedIn lists JW Foods Inc. | [About](https://www.jwfoods.com/pages/about-us), [Yelp](https://www.yelp.ca/biz/jw-foods-scarborough-2), [LinkedIn](https://www.linkedin.com/in/william-fehr-39662547/) |
| **Tasia** | Bill's wife, active in the store (2023 review) | [Chamber](https://canada.chamberofcommerce.com/business-directory/ontario/scarborough/food-products-supplier/534332-j-w-foods) |
| **Lucas** | Bill's son, helps with orders (Sep 2025 review). Likely next generation | [Yelp](https://www.yelp.ca/biz/jw-foods-scarborough-2) |
| "John" | john@jwfoods.com on the old Facebook page. Role unknown | [Facebook](https://www.facebook.com/p/JW-Foods-Inc-100068059854436/) |
| George Trougakos | Late patriarch. Founded Advance Food Products (1973) | [About](https://www.jwfoods.com/pages/about-us) |

- **Headcount:** about **15 employees** (self-described, 2018, [Alignable](https://www.alignable.com/toronto-on/jw-foods-inc/jwfoods-com-jul-2018)). ZoomInfo gives **<25**, and its employee-directory page says **1–10** ([ZoomInfo](https://www.zoominfo.com/pic/j--w-foods-inc/411664737)). D&B leaves the employee fields blank. **Estimate for today: 10–18 people**, including part-time counter, cooking, butchery and delivery staff. Reasoning: it runs 6 route-runs a week plus express delivery, a 979-SKU store open 6 days, and in-house cooking and portioning.
- **Fragmented contact identity:** the business publishes mealbutler@gmail.com (website), Jwfoods@rogers.com (Facebook), john@jwfoods.com (old Facebook), Jwfoodscontenttt@gmail.com (Instagram collabs), and two phone numbers, (416) 298-1350 and (416) 471-9368 (Yably).

---

## 7. Third-party company data

| Provider | Revenue | Employees | Other | Source |
|---|---|---|---|---|
| **Dun & Bradstreet** | **≈ $1.07M annual sales** (modelled; currency not stated in the snippet) | blank | Key principal Steven Trougakos (President). Address 1-2201 Brimley Rd. Industry: grocery and related product wholesaling | [D&B](https://www.dnb.com/business-directory/company-profiles.j__w_foods_inc.66f5b22e4d6f7d525e9da24a692e5e47.html). The page blocks bots, so these figures come from the search-result summary |
| **ZoomInfo** | **< $5M** | **< 25** (company page) / **1–10** (directory page) | Founded 1995. Steve Trougakos, President/Owner. Category: grocery retail | [ZoomInfo company](https://www.zoominfo.com/c/j--w-foods-inc/411664737), [ZoomInfo people](https://www.zoominfo.com/pic/j--w-foods-inc/411664737). Also from search summaries |
| Owler | not found (not checked; search quota ran out) | — | — | — |
| RocketReach | not found (not checked; search quota ran out) | — | — | — |

These are **modelled estimates, not filings**. J & W Foods Inc. is private, and no public financial statements were found.

### Regulatory and licensing notes
- The website says JW became an **Ontario Inspected Meat Plant in 2008** ([About](https://www.jwfoods.com/pages/about-us)). The Instagram bio says **"CFIA Approved"** ([Instagram](https://www.instagram.com/jwfoods/)). These claims need reconciling.
- Under the Safe Food for Canadians Regulations, a **federal licence is required to slaughter or process meat for interprovincial trade or export** ([CFIA](https://inspection.canada.ca/en/food-licences/food-business-activities)). If JW holds only a provincial licence, its delivery footprint and any e-commerce growth are limited to Ontario. Its current routes, which reach as far as Ottawa, Windsor and Sarnia, already stay inside that limit. **This is a strategic question for the proposal: whether to stay Ontario-only or seek a federal SFCR licence for national DTC and B2B.**

---

## 8. Tech stack (from https://www.jwfoods.com HTML, fetched Oct 16, 2026)

| Layer | Finding |
|---|---|
| Platform | **Shopify**. Store "J&W Meal Butler", jw-foods.myshopify.com, shop ID 11560176 (an early store; oldest products date from 2016). CAD. Shop Pay / Shop app present |
| Theme | **Refresh** v13.0.1 (Shopify Theme Store #1567), a free Shopify theme. Fonts: Titillium Web and Chivo |
| Loyalty | **Smile.io** (app block plus `smile-loader.js`). Points are mentioned on the delivery page |
| Chat / support | **Shopify Inbox** chat widget, greeting "Welcome to J&W Meal Butler. How can I help?" |
| Reviews / UGC | **None.** No Judge.me, Yotpo, Okendo, Loox or Stamped. No star ratings on products |
| Subscriptions | **None.** Products return `selling_plan_groups: []`, and no ReCharge, Seal, Appstle or Shopify Subscriptions |
| Email / SMS | **No ESP script detected** on the storefront (no Klaviyo, Omnisend, Mailchimp or Privy). The newsletter form is Shopify's native "Subscribe to our emails" |
| Analytics / ads | **Meta pixel** (Facebook & Instagram app, pixel 255929925589412). **TikTok pixel** (C8TTK3J3NCHNQFBBFLNG). One unidentified app pixel (Shopify app client 246667608065). **No Google Analytics 4 or GTM tag** found in the theme. Shopify's standard pixels are present |
| Content | **Blog: 1 post** ("BLOW OUT SPECIAL"), sitemap lastmod 2021-10-14. 15 static pages. Homepage video is the 2018 third-party YouTube promo |
| SEO metadata | Title: "Health and wellness from real foods both raw and fully cooked foods – J&W Meal Butler". Meta description: a string of hashtags (#fish #beef #chicken … #wholesalechicken #wholesaleprices #fooddelivery). Neither contains "Toronto", "Scarborough", "meal prep" or "butcher" |
| Other | Shopify's `sitemap_agentic_discovery.xml` is present (Shopify default) |

The page-level SEO is partly offset by product titles such as "Broccoli - High Quality Veggies & Groceries Toronto & GTA - JW Foods" (seen in search result titles).

---

## 9. Search visibility

| Query (Canada) | JW in results? | Evidence |
|---|---|---|
| "meal prep Toronto" | **No.** Not in the top 12 organic results | DuckDuckGo-Canada results, ranked: Power Kitchen, Meal Project, thebesttoronto list, Protein Chefs, torontoblogs list, Easy Mealz, One Life Meals, MealFix, plus WeCook ads |
| "meal prep Toronto best cooked portioned meals delivery" | **No** | Web search returned Savvy New Canadians, Toronto Life (CookUnity), GoFoodie, blogTO 2015 |
| "cooked portioned meals Toronto athletes …" | **No** | Results: Athlete's Kitchen, Power Kitchen, Yumba |
| "best butcher Scarborough" | **No** | Results were irrelevant (Great East Butcher Co., UK listings) |
| Toronto meal-delivery round-ups | **Not listed in any** | [torontoblogs.ca](https://torontoblogs.ca/best-meal-delivery-services-in-toronto/) (0 mentions), [Savvy New Canadians, 18 services](https://www.savvynewcanadians.com/best-prepared-meal-delivery-ontario/) (0 mentions), [blogTO 2015](https://blogto.com/eat_drink/2015/03/the_top_10_prepared_meal_delivery_options_in_toronto/) (0 mentions) |
| Brand queries ("J&W Meal Butler", "jwfoods", "J&W Foods Brimley") | **Yes.** The website, Yelp, Facebook, Instagram and directories rank | Search results |

**Google local pack: not verified.** Google results could not be checked directly. Its ranking for "butcher near me" and "meal prep near me" around Agincourt is unknown. With 611 reviews at 4.8★, JW very likely ranks well in the immediate area (estimate). The inconsistent listings below work against it:
- **Hours:** the website says M–F 9–6 and Sat 10–4. Yelp says M–F **10**–6. Unilocal and Canada Online say M–F **8**–6 and Sat 8–**3**.
- **Postal code:** M1S 4N7 vs **M1S 2E2** (Unilocal).
- **Delivery minimum:** $100 (delivery page) vs **$130**, with free delivery from $200 ([free-delivery page](https://www.jwfoods.com/pages/free-delivery)).

**Conclusion:** JW gets almost all of its demand from repeat customers, word of mouth and Instagram. Organic discovery for the two biggest categories, meal prep and butcher, is effectively zero outside the brand name.

---

## 10. Revenue estimate (store + online + wholesale), CAD

**No reported revenue was found.** The estimate triangulates three methods.

### A. Third-party models
- D&B modelled sales of about **$1.07M**. This is a floor-type figure; D&B models for small private firms are often driven by thin data.
- ZoomInfo gives **< $5M**, which works as a ceiling.

### B. Labour-cost ratio (ISED / StatCan 2024 small-business benchmarks)
Benchmarks: Canadian Industry Statistics, firms with $30K–$5M revenue, data year 2024.
- **Specialty food stores (NAICS 4452)**, top quartile ($947K–$5M): average revenue **$1,918.2K**; wages and benefits $89.9K plus labour and commissions $304.7K, so **revenue ≈ 4.86 × labour cost**; gross margin 37.1% ([ISED 4452](https://ised-isde.canada.ca/app/ixb/cis/performance/rev/4452)).
- **Meat product manufacturing (NAICS 3116)**, top quartile ($1.63M–$5M): average revenue **$3,021.7K**; labour $308.8K plus $367.4K, so **revenue ≈ 4.47 × labour cost**; gross margin 33.5% ([ISED 3116](https://ised-isde.canada.ca/app/ixb/cis/performance/rev/3116)).
- Ontario general minimum wage is **$17.95/h from Oct 1, 2026**, about $37.3K for a full-time year ([Ontario](https://www.ontario.ca/document/your-guide-employment-standards-act-0/minimum-wage)). Butchers, cooks and drivers are paid above that.

| Case | FTEs | Loaded cost/FTE | Labour cost | Ratio | Revenue |
|---|---|---|---|---|---|
| Low | 10 | $40K | $400K | 4.0× | **$1.6M** |
| Mid | 14 | $45K | $630K | 4.5× | **$2.8M** |
| High | 18 | $50K | $900K | 4.86× | **$4.4M** |

### C. Channel build-up (order-volume signals)
Signals: 6 route-runs a week plus express, a $100–$130 minimum and free delivery at $200, 611 Google reviews growing about 100 a year, 30K Instagram followers, a 979-SKU catalogue with about 142 new listings a year, and a chicken TRQ processor allocation.

| Channel | Low | Mid | High | Assumptions |
|---|---|---|---|---|
| Delivery (routes + express) | $0.48M | $0.90M | $1.60M | 60 / 100 / 160 orders a week × $160 / $180 / $200 AOV × 50 weeks |
| Store walk-in + pick-up | $0.59M | $1.20M | $2.28M | 30 / 50 / 80 transactions a day × $65 / $80 / $95 × 300 days |
| Wholesale / foodservice / trade | $0.10M | $0.30M | $0.60M | Informal restaurant, trainer and retail accounts (section 5) |
| **Total** | **$1.17M** | **$2.40M** | **$4.48M** | |

### Blended estimate

| | **Low** | **Mid** | **High** |
|---|---|---|---|
| **Annual revenue (CAD)** | **$1.2M** | **$2.5M** | **$4.0M** |

**Why:**
- The **low** case matches D&B's ~$1.07M model and the bottom of both build-ups.
- The **mid** case sits between the 2024 top-quartile averages for specialty food stores ($1.9M) and small meat processors ($3.0M). It fits a 12–15-person, six-day, three-channel operation.
- The **high** case is capped below ZoomInfo's <$5M ceiling. It is also trimmed from the ~$4.4–4.5M build-ups, because current headcount may be below 18.

**Use the $2.5M mid-case as the proposal baseline.** On that base, **+$1M a year is about +40%**. That is ambitious but credible if most of it comes from new channels: B2B and foodservice, subscriptions, and gym and trainer partnerships. Squeezing the existing store harder would not get there.

---

## 11. What this means for the proposal (hand-off notes)

1. **Social proof:** pull the 611 Google reviews and 30K Instagram audience onto the site with a reviews app, UGC and a "4.8★ on Google" badge.
2. **Retention:** add subscriptions and auto-reorder for Meal Butler. The tech stack confirms there is none today, and customers rebuild their carts every week.
3. **B2B portal:** cover gyms, trainers, restaurants, corporate, and athletic or sports teams. Use the provincially inspected plant, the chicken TRQ allocation and the family's wholesale heritage (Advance Food Products) as proof points.
4. **Creator and athlete programme:** relaunch the fitness-show presence (CanFitPro, OPA/CPA shows, TO Pro Super Show). Turn the informal gym referrals into a tracked affiliate programme.
5. **Local SEO clean-up:** fix hours, postal code and delivery minimum everywhere. Add proper titles and meta descriptions. Create "meal prep Toronto", "butcher Scarborough" and "Ontario-inspected" landing pages. Restart the blog.
6. **Brand-risk management:** shift the brand from founder-dependent to team-and-product-driven (Lucas as next-gen face). Set up a review-response playbook, since the AI agents can draft replies.
7. **Analytics:** install GA4 and a server-side Meta CAPI, and add an email/SMS platform such as Klaviyo before any growth spend.
8. **Licensing decision:** decide whether to stay Ontario-only or pursue a federal SFCR licence for national DTC. Reconcile the "CFIA Approved" claim.

---

## 12. Gaps / not found

- Google Business Profile itself was not opened. Its rating and count come from aggregators (Yably and the Chamber of Commerce snapshot).
- Instagram post dates and engagement are behind a login, so cadence was not verified.
- The TikTok account behind "5M+ views" was not found.
- Owler, RocketReach, RestaurantGuru, news archives and the Ontario licensed meat plant directory were not checked because the search quota ran out.
- Google local-pack rankings were not verified.

---

## Sources

- J&W Foods site: [home](https://www.jwfoods.com/), [about](https://www.jwfoods.com/pages/about-us), [meal-butler](https://www.jwfoods.com/pages/meal-butler), [free-delivery](https://www.jwfoods.com/pages/free-delivery), [location-hours](https://www.jwfoods.com/pages/location-hours), [sitemap](https://www.jwfoods.com/sitemap.xml)
- [Yably: J & W Foods inc reviews (Google 611 / 4.8; Facebook 56 / 4.6)](https://yably.ca/reviews/toronto/j-w-foods-2201-brimley-road)
- [Chamber of Commerce: J & W Foods (4.7 / 295 Google snapshot)](https://canada.chamberofcommerce.com/business-directory/ontario/scarborough/food-products-supplier/534332-j-w-foods)
- [Yelp: JW Foods (4.0 / 13)](https://www.yelp.ca/biz/jw-foods-scarborough-2)
- [Unilocal: JW Foods](https://unilocal.net/canada/toronto/jw-foods)
- [Instagram @jwfoods](https://www.instagram.com/jwfoods/)
- [Facebook /jandwfoods](https://www.facebook.com/jandwfoods/) · [Facebook JW Foods Inc. (old)](https://www.facebook.com/p/JW-Foods-Inc-100068059854436/)
- [TikTok @jwfoods](https://www.tiktok.com/@jwfoods) · [TikTok @williamfehr3rd](https://www.tiktok.com/@williamfehr3rd)
- [YouTube: JW Foods Promotional Video (2018)](https://www.youtube.com/watch?v=w6IBvPqv6TI) · [YouTube: JW Foods @ CANFITPRO 2014](https://www.youtube.com/watch?v=VtOHjKZoTvc)
- [Alignable: Jw foods inc (15 employees, restaurants)](https://www.alignable.com/toronto-on/jw-foods-inc/jwfoods-com-jul-2018)
- [Dun & Bradstreet: J & W Foods Inc](https://www.dnb.com/business-directory/company-profiles.j__w_foods_inc.66f5b22e4d6f7d525e9da24a692e5e47.html)
- [ZoomInfo: J & W Foods](https://www.zoominfo.com/c/j--w-foods-inc/411664737) · [ZoomInfo: employee directory](https://www.zoominfo.com/pic/j--w-foods-inc/411664737)
- [LinkedIn: William Fehr](https://www.linkedin.com/in/william-fehr-39662547/)
- [Global Affairs Canada: 2026 WTO Chicken Quota Holders, Processor](https://www.international.gc.ca/trade-commerce/controls-controles/chicken-poulet/wto_processor-2026-omc_transformateurs.aspx?lang=eng)
- [Global Affairs Canada: 2026 CPTPP Chicken Quota Holders, Processor](https://www.international.gc.ca/trade-commerce/controls-controles/chicken-poulet/cptpp_processor-2026-ptpgp_transformateurs.aspx?lang=eng)
- [CFIA: Food business activities that require a licence](https://inspection.canada.ca/en/food-licences/food-business-activities)
- [ISED Canadian Industry Statistics: Specialty food stores 4452, financial performance 2024](https://ised-isde.canada.ca/app/ixb/cis/performance/rev/4452)
- [ISED Canadian Industry Statistics: Meat product manufacturing 3116, financial performance 2024](https://ised-isde.canada.ca/app/ixb/cis/performance/rev/3116)
- [Ontario: Minimum wage](https://www.ontario.ca/document/your-guide-employment-standards-act-0/minimum-wage)
- [torontoblogs.ca: Best prepared meal delivery services in Toronto](https://torontoblogs.ca/best-meal-delivery-services-in-toronto/)
- [Savvy New Canadians: Best prepared meal delivery Ontario](https://www.savvynewcanadians.com/best-prepared-meal-delivery-ontario/)
- [blogTO: Top 10 prepared meal delivery options in Toronto (2015)](https://blogto.com/eat_drink/2015/03/the_top_10_prepared_meal_delivery_options_in_toronto/)
- Competitor sites seen in the "meal prep Toronto" results: [Power Kitchen](https://powerkitchen.ca/), [Meal Project](https://mealproject.ca/), [Protein Chefs](https://proteinchefs.com/), [Easy Mealz](https://easymealz.ca/), [One Life Meals](https://www.onelifemeals.com/), [MealFix](https://mealfixcanada.com/)

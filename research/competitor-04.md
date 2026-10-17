# Competitor #4: WeCook (WeCook for Business), Montreal, QC

Checked October 16, 2026. All prices are in CAD. WeCook says its meals are not taxable (FAQ).

Method:
- Direct fetches of wecookmeals.ca. The site is a Laravel + Vue single-page app, so most text loads by script. I read:
  - the public JSON endpoints the site itself calls: `/api/plans`, `/api/menus`, `/api/menus/422/meals`, `/api/menus/422/meals/<slug>/details`, `/api/products`, `/api/snacks`, `/api/faqs/faq/search`, `/api/config/*`;
  - the site's English string file `/js/i18n.js`, which holds all UI copy, including the logged-in B2B dashboard;
  - `/css/app.css`, for colours and fonts.
- The built-in browser, used to render /en, /en/business, /en/week-menu, /en/gift-cards, /en/about-us and /en/retail-products, take screenshots and read computed styles. I declined non-essential cookies.
- Third-party pages: Trustpilot, Retail Insider (two articles) and Strategy.
- Limitation: the shared web-search budget was used up before this pass started. I made no news searches for 2026 coverage, such as funding, ownership changes or layoffs. The operating status rests on WeCook's own live data, Trustpilot reviews dated October 2026 and 2025 trade press.

## 1. Verdict: operating? premium?

**Operating in October 2026: YES, and actively.**
- The `/api/menus` endpoint lists weekly menus published through **Nov 8-14, 2026**. Menu #422, for the **week of Oct 18, 2026**, has 15 meals. The browser shows "Week of October 18 2026" on /en/week-menu.
- The footer reads "© 2026 WeCook. All rights reserved." The server's Date header was Fri, 16 Oct 2026.
- Trustpilot lists **4.8, "Excellent", from 6,584 reviews, 672 of them in the last 12 months**. The five newest reviews run from Oct 6 to Oct 8, 2026, and all are 5-star. WeCook replies to 80% of negative reviews ([Trustpilot](https://www.trustpilot.com/review/wecookmeals.ca)).
- WeCook is expanding. The About page and FAQ now say it delivers in "Quebec, Ontario, the Maritimes, and **now Western Canada**". The site's tax config includes BC, AB, SK and MB. A retail line ("Find us in the fresh aisle") is live, with one SKU enabled: the Grilled Chicken Burrito Bowl.

**Premium: YES. This is premium mass-market, not luxury.**
- The executive chef is Gabriel Drapeau (named on WeCook's retail page and in the PK Subban copy). Retail Insider says the menu is backed by "an executive chef from Montreal's celebrated restaurant Joe Beef" ([Retail Insider, Aug 26 2025](https://retail-insider.com/?p=177907)).
- Meals are fresh and never frozen, with no preservatives (site copy). The menu has 15 new meals a week from a database of 500+ recipes (FAQ).
- Brand partnerships:
  - P.K. Subban, two collaborations ([Strategy, Aug 26 2025](https://strategyonline.ca/2025/08/26/wecook-pk-subban/)).
  - A Schwartz's Deli pop-up in Toronto on Jul 30, 2025 ([Retail Insider, Jul 28 2025](https://retail-insider.com/retail-insider/2025/07/wecook-partners-with-schwartz-for-one-day-immersive-pop-up-in-toronto/)).
  - A collaboration with Maripier Morin was announced next (Strategy).
- Prices are mid-market: **$11.99-15.49 a meal** on consumer plans and about **$11.75** on the B2B platform. The positioning is "premium and accessible", in the CEO's words to Strategy.

**The pick holds.** WeCook for Business is the clearest live Canadian example of an employer-subsidy meal platform. Section 7 lists the corrections to the selection notes.

## 2. Scale signals

| Signal | Value | Source |
|---|---|---|
| Meals | 90,000 a week | [Retail Insider, Aug 2025](https://retail-insider.com/?p=177907) |
| Meals (company claim) | "+4 million meals delivered per year" | [About us](https://www.wecookmeals.ca/en/about-us) |
| Customers | "+150,000 unique customers" | About us |
| Growth | "demand has increased by 1000% since 2020", "600 new jobs", "two production facilities" | About us |
| Employees | "nearly 400" | Retail Insider, Aug 2025 |
| Founded | 2012, as Nutrition Fit Plus | Retail Insider; site brand-change modal |
| Ownership | Desjardins Capital, Investissement Québec, and Claridge Food Group as majority holder | Retail Insider, Aug 2025 |
| CEO | Michel Gagné, President & CEO | Retail Insider; Strategy |
| Revenue | Not found. ESTIMATE: 90,000 meals/wk × ~$13 × 52 ≈ **$60M/yr gross**, from the plan prices below | Derived |
| Reviews | Trustpilot 4.8 from 6,584; 81% 5-star, 15% 4-star, 1% 1-star | [Trustpilot](https://www.trustpilot.com/review/wecookmeals.ca) |
| Markets | QC, ON, Maritimes, Western Canada | FAQ "Where do you deliver?" |
| Social proof on the B2B page | Logo wall: Fédération de natation du Québec, PlanetHoster, MEGA Pompage de béton, Advanced Racing and a sports-club crest. These are mostly small Quebec firms | /en/business (screenshot) |
| Tech stack (page source) | Laravel + Vue SPA; Klaviyo; VWO A/B testing; Zendesk chat; Trustpilot widget; Nuvei payments with email OTP at checkout; CloudSponge contact import for referrals; Cloudflare Turnstile; GTM; CookieYes; iOS and Android apps | home HTML |

## 3. Real prices (live from `/api/plans` and the menu/product APIs, Oct 16 2026)

**Consumer subscription plans.** The price is per meal, and it falls as the plan grows:

| Plan (meals/week) | Small (300-400 g) | Regular (440-550 g) |
|---|---|---|
| 6 meals | $14.49 | $15.49 |
| 9 meals | $13.49 | $14.49 |
| 14 meals | $12.99 | $13.99 |
| 22-30 meals | $11.99 | $12.99 |

- **Family size** (serves 4-5): $29.95. It counts toward the plan's meal total (FAQ).
- **Premium meals** carry a surcharge. 4 of the 15 meals each week are premium. For the week of Oct 18: Smoked Pulled Pork **+$1.95**; Shrimp Tuscan Pasta, Maple-Soy Salmon Poke and Grilled Beef Steak Marsala **+$4.25** each.
- **Minimum order:** 6 meals. Orders can be planned **up to 5 weeks ahead**, and weeks can be skipped.
- **Delivery:** the FAQ contradicts itself. One entry says "The delivery charge is $7.99", with the first delivery free when a promo code is used. Two other entries answer "Is delivery free?" with "Yes". Home delivery runs 7am-9pm and office delivery 7am-5pm, in an insulated box with ice packs.
- **Acquisition offer** on the homepage hero: "**$100 total discount** on your first 4 orders" (code PROMO100 in the page config). Other copy on the page offers "$20 off your first order".

**Add-ons** (`/api/products`, `/api/snacks`):
- 4 egg bites: $9.99, down from $11.99 (≈ $2.50 each).
- 6 protein bites: $13.99.
- 4 protein brownies or cookies: $14.95.
- 4 × 300 mL juices or smoothies: $20.95.
- Mox shake: $13.99.
- Shaker: $9.99.

**WeCook for Business:**
- "$11.75-ish when you order through our platform". The CEO puts traditional catering at about $20-25 a meal.
- The employer "can decide to contribute $1 per meal, or 100%".
- The program fits companies of "20 employees or 500 employees". Larger firms get dedicated on-site fridges ([Retail Insider, Aug 2025](https://retail-insider.com/?p=177907)).
- The dashboard says: "*Meal prices are adjusted according to the total volume ordered by all users." So there is a company-wide volume tier (i18n `meal-b2b-section.price-per-meal-note`).

**Gift cards:**
- Amounts: $25, $50, $100, $200, or a custom amount (minimum $10).
- **A 10% bonus is live today**: "You have an extra of $5.00!" on $50.
- Gift cards can be paid with WeCoins.

**Loyalty and referral:**
- WeCoins levels: Bronze 0-29,999, Silver 30,000-59,999, Gold 60,000+.
- A $20 credit costs 50,000 WeCoins.
- Referral reward: "Refer 6 friends = 1 year of FREE snacks."

**Nutrition sample.** Steak-Spiced Turkey Protein Power Bowl (`/details` API):

| Size | Calories | Protein | Sodium |
|---|---|---|---|
| Small | 420 | 33 g | **795 mg** |
| Regular | 570 | 47 g | **1,015 mg** |

The ingredients include canola oil and salt.

## 4. Flows worth borrowing (step by step)

### A. B2B signup and employer onboarding (the core of "J&W at Work")
1. Landing page /en/business. The hero shows the Trustpilot strip, then the H1 "The ready-to-eat meal perk your team will actually use", then a lead form placed **above the fold**.
2. Form fields:
   - First name, Last name, Email, Company name, Phone.
   - **"For who"** dropdown: Business / Gym / Sports team / Retail / Other / For me. Choosing "For me" redirects the visitor to consumer plans.
   - Number of employees.
   - Notes (200 characters maximum).
   - A checkbox: "I am already a WeCook client".
3. The CTA reads "Talk to our team". On success the page says: "Your business account request has been delivered… we will communicate with you over the next business days". This is sales-assisted, not self-serve.
4. Sales approves the account. The admin then gets an email: "Here is your temporary password to login to your WeCook business portal."
5. On first login a **guided tour** runs: "Here is your Business Program", then "Here you can invite employees", then "Manage invitations".
6. **The allowance engine.** It sets a default allowance for all users, with per-employee overrides. The types are:
   - $X per employee, on all items;
   - $X per employee, on meals only;
   - N meals per employee;
   - $X per meal, up to a cap.

   The caps are max meals per employee, max meals paid by the company, and max per order.
7. **Invite employees** by email. The employee's address must match the company's email domain ("The email address entered does not belong to the company's domain"). The admin sees Pending and Accepted lists, can resend an invite after 24h, and can delete a user, which removes that user's future selections.
8. Each employee picks meals weekly on the platform. Personal and corporate accounts are kept separate, and an account-migration flow handles existing consumers.
9. **The joint weekly order.**
   - The admin sees the upcoming delivery dates, a meal overview of everything the team picked, and a "**Refresh order**" button for live changes.
   - If nobody orders that week, the delivery "will automatically be cancelled — simple, no admin burden."
10. The **receipt and invoice** split the order into "Total covered by the company" and "Total paid by the employee(s)". Delivery goes to the office, 7am-5pm.
11. Limitation: business accounts **cannot use the mobile app** yet (FAQ).

### B. Consumer subscription (from the FAQ "How does it work" plus the live UI)
1. Email capture in the hero, tied to the $100-off offer.
2. Choose a delivery date and location: postal code, home or office.
3. Choose a portion size (Small or Regular), then a plan (6, 9, 14 or 22-30 meals).
4. Split the plan's count between individual and family-size meals.
5. Pick from 15 meals and **customise the side**: rice & veg, potatoes & veg, quinoa & veg, or veg only.
6. Set **preferences**: ingredients to exclude, and a preferred side style. WeCook uses these to auto-select meals.
7. Enter delivery details, then pay by Visa, MC, Amex, Apple Pay or Google Pay, with an email OTP.
8. Manage the account under My Deliveries:
   - Plan 5 weeks ahead and skip weeks.
   - Turn on "**Premium Feature**", which lets auto-selection include surcharge meals and earns WeCoins.
   - Add snacks or oats on a recurring frequency, such as weekly or biweekly.
   - Cancelling triggers a retention flow (`/api/unsubscribe/retention`).

### C. Gift card
1. Choose an amount (presets or a custom amount of $10+). A 10% bonus is shown.
2. Personalise: recipient name and email, sender, and a message.
3. **Choose the date the email is sent**, or choose "Print yourself".
4. Optionally "Send the bonus gift card to a different person".
5. Pay by credit card **or with WeCoins**. The recipient redeems the card at /activate-gift-cards.

### D. Gamified loyalty
- Members earn WeCoins on orders, on badges (first breakfast order, first sous-vide order and others) and on social challenges (FB, IG and TikTok endpoints).
- Levels give perks.
- The WeCoins Market redeems coins for credit, freebies (egg bites, shaker) or gift cards.
- Coins are lost on unsubscribe, which acts as a churn brake.

## 5. Site design (for a designer's brief; borrow ideas only, never copy content)

**Layout**
- **Header:** sticky and white, at about 56 px. On the left, a lowercase green wordmark; the B2B pages add a small "for business" sub-label. On the right, an FR/EN toggle, a solid green CTA ("Try WeCook" or "Log In") and a hamburger menu.
- **Consumer hero:** split. A white rounded card on the left holds:
  - the H1;
  - the subhead;
  - a **pale-yellow promo pill**;
  - the email field and CTA;
  - a "Proudly Canadian" maple-leaf stamp in the corner.

  On the right is a full-bleed photo of green branded boxes and clear meal trays on marble.
- **B2B hero:** 50/50. On the left, a lifestyle photo of office workers eating from trays at a table. On the right, a Trustpilot strip, a large green H1 and the lead form, which works as the hero itself.
- **Section order (B2B):**
  1. An auto-scrolling **benefit marquee**: "More affordable than takeout", "Fridge stocked, zero hassle"…
  2. "Set it up once" as **3 numbered step cards**, each with a product/UI photo.
  3. "Perks that finally make sense", an asymmetric photo pair with copy.
  4. "**Myth-Busters**", a 2×2 photo grid with green objection-handling headlines.
  5. A logo band on cream.
  6. A closing form block, "Culture is built in moments, not meetings", with a Trustpilot badge and a photo.
  7. A 5-column footer.
- **Menu page:** category tabs with round icons on pale green (Ready-to-eat, Family, Snacks, Beverages, Breakfasts), a week picker, and a 4-column card grid. Each card has:
  - a square photo;
  - a **green circular protein sticker** ("52 g protein");
  - a "Family size available" outline pill;
  - a dark-green "Premium meals" band on surcharge dishes.

**Palette** (from app.css frequency counts and computed styles)

| Role | Hex |
|---|---|
| Primary green | **#03894E / #00894E** |
| Darker greens (hover, bands) | #026B3D, #027040, #025732 |
| Text charcoal | **#232522**; headings in grey #393C3F |
| Mid grey | #979797 |
| Cream bands | **#FBF8EA**, #F9F4EF, #FBFAF6 |
| Promo yellow | #FDCF32 / #FAB418 |
| Family-size orange | #FF9D1E / #F37601 |
| Error red | #F44336 |
| Base | white |

**Typography**
- Headings: **Rubik 700**. H1 48/57.6 px, H2 32 px, H3 24 px, set in green.
- Body: **museo-sans** (Adobe Fonts) at 16/24.
- Accents: **Fierce Vector**, a heavy condensed display face, is used on the retail page ("Ready to eat. Reinvented."). **Permanent Marker** is used as a handwritten accent.
- Buttons: 8 px radius, white on green, 14-16 px bold.
- Inputs: 44 px tall, 8 px radius.

**Photography**
- Bright, natural-light food shot top-down on linen, stone or marble, in clear plastic trays or ceramic bowls, with chunky visible ingredients.
- Lifestyle images show diverse people eating at work or at a family table.
- The retail line uses colour-blocked studio backgrounds (pink, mustard) with close-ups of a person eating.

**Tone**
- Friendly, punchy and benefit-first, with light humour: "Heat, eat, repeat", "WeCook, so you don't have to!", "Your office fridge says more about your company than your About Us page".
- Bilingual FR/EN.
- B2B copy speaks to HR and culture outcomes (productivity ROI, retention, "cheaper than churn") rather than to food.

## 6. What J&W already does better

- **A real butcher with an Ontario-inspected plant.** J&W has been provincially inspected since 2008, with family butcher roots going back to George Trougakos in the 1960s, Advance Food Products in 1973 and J&W in 1995. WeCook is a ready-meal kitchen. Its raw-meat landing page ("Our meats from Quebec") and its vacuum-sealed DTC line appear wound down: the site carries the string "We no longer offer vacuum-sealed foods", and the sealed-menu API returns placeholder $1.00 prices. Its retail page now pushes sous-vide meals instead. J&W can sell an office the meal **and** the steaks for the team BBQ or holiday boxes.
- **À la carte, macro-exact portions.** J&W's cooked chicken breast is 4 oz for $4.20-4.99, salmon 6 oz for $11.00, egg bites $4.25-5.50 per 2-pack, and pre-set meals $8.99-14.99 (4 oz or 6 oz protein). WeCook sells fixed dishes in two sizes with a 6-meal minimum. A trainer or athlete can build exact macros only at J&W.
- **Salt-free, sugar-free, no added oil.** J&W states "All products are salt and sugar free, with no added oils". WeCook's protein bowl carries **795-1,015 mg sodium** and contains canola oil. That gives J&W a clean pitch to hospitals, clinics and wellness-driven HR teams.
- **A frozen, vacuum-sealed format.** It suits an unattended office freezer with no weekly expiry pressure and less waste. WeCook's fresh trays must be eaten by the use-by date, and WeCook has to supply fridges.
- **Price parity or better on comparable items.** J&W pre-set meals at $9.99-12.99 sit at or below WeCook's $11.99-15.49 plan prices, with no plan minimum. Egg bites are about equal per piece: J&W about $2.13-2.75, WeCook about $2.50.
- **GTA home turf.** J&W has its Scarborough plant and storefront (free pickup) and its own weekly GTA routes: GTA 2 on Wednesday covers Toronto, Scarborough and North York; GTA 4 on Friday covers Markham, Vaughan and Richmond Hill. WeCook ships from Quebec through third-party couriers. It is not a local brand, and its B2B logos are Quebec firms.
- **Breadth.** J&W also carries raw cuts, Wagyu, whole and half animals, Greek specialties, supplements and snacks, which make it a one-stop shop for gym-goers and families.

**Where WeCook is clearly ahead** (gaps J&W must close):
- a working employer dashboard and allowance engine;
- tiered plans and subscriptions;
- 6.5K reviews of social proof;
- an app;
- gamified loyalty;
- the polish of a chef-and-celebrity brand.

## 7. Checks and corrections on the selection notes

- **"Verified Oct 16 2026" (Retail Insider):** the page was re-fetched today, but the **article is dated Aug 26, 2025**. The figures of 90K meals a week, ~400 staff, $11.75 a meal, $1-100% subsidy and 20-500 employees are therefore **14 months old**. The B2B page and dashboard copy are still live, which supports that the program is current.
- **Scope:** "Ontario incl. GTA, Quebec, New Brunswick, Halifax" is out of date. WeCook now says "Quebec, Ontario, the Maritimes, and Western Canada".
- **Joe Beef:** this rests on Retail Insider's wording. WeCook's own site names the executive chef (Gabriel Drapeau) but does not mention Joe Beef.
- **Schwartz's Toronto pop-up:** confirmed. It ran Jul 30, 2025, 4-8pm, at Avenue Diner, 222 Davenport Rd, with $5 smoked-meat dishes.
- **PK Subban:** confirmed. The Strategy article covers the **second** collaboration, P.K.'s Spaghetti and Meatballs, on the menu from Sep 7 to Oct 4, 2025.
- **Consumer price:** competitors-gta-mealprep.md said "official price list not found, $10-13 anecdotal". The live API now gives **$11.99-15.49 a meal** (table above) and **$29.95 for family size**.
- **"Fresh, never frozen":** true at delivery. The FAQ does let customers freeze meals.
- **The J&W play's staff price of ~$11-13 is consistent** with WeCook's ~$11.75 B2B rate and $11.99-12.99 high-volume consumer tiers. J&W should not price above about $13 for a pre-set meal at work.

## 8. Implications for "J&W at Work"

- Copy the mechanics, not the look:
  - the allowance types and caps;
  - domain-locked invites;
  - the weekly joint order that auto-cancels;
  - the live order roll-up;
  - the company/employee split invoice;
  - the volume-tiered price.

  The MVP can run on Shopify B2B (company accounts, catalogs and payment terms) plus a discount-code or wallet layer for the subsidy. Native B2B needs Shopify Plus; check J&W's plan before committing.
- Lead with what WeCook cannot claim:
  - "Ontario-inspected butcher, 30 years in Scarborough";
  - "salt-free, sugar-free, no added oil";
  - "freezer-stocked, no weekly waste";
  - "macro-exact portions".
- Sell first to the healthcare, logistics and manufacturing sites around Brimley Rd. WeCook's B2B social proof there is thin.
- Add the B2B lead form's "For who" segmentation (Business / Gym / Team / Retail). It routes leads to plays #2 and #4 from one page.

## Sources

- WeCook home (EN): https://www.wecookmeals.ca/en
- WeCook for Business: https://www.wecookmeals.ca/en/business
- Weekly menu (week of Oct 18 2026): https://www.wecookmeals.ca/en/week-menu
- Plans API: https://www.wecookmeals.ca/api/plans
- Menus API: https://www.wecookmeals.ca/api/menus and https://www.wecookmeals.ca/api/menus/422/meals
- Meal detail API (nutrition): https://www.wecookmeals.ca/api/menus/422/meals/steak-spiced-turkey-protein-power-bowl/details
- Products and snacks APIs: https://www.wecookmeals.ca/api/products · https://www.wecookmeals.ca/api/snacks
- FAQ API: https://www.wecookmeals.ca/api/faqs/faq/search
- UI string file (B2B dashboard, gift card, loyalty copy): https://www.wecookmeals.ca/js/i18n.js
- Stylesheet (palette, fonts): https://www.wecookmeals.ca/css/app.css
- About us: https://www.wecookmeals.ca/en/about-us
- Gift cards: https://www.wecookmeals.ca/en/gift-cards
- Retail products: https://www.wecookmeals.ca/en/retail-products
- Trustpilot: https://www.trustpilot.com/review/wecookmeals.ca
- Retail Insider, "WeCook launches 'WeCook for Business'…" (Aug 26 2025): https://retail-insider.com/?p=177907
- Retail Insider, Schwartz's Toronto pop-up (Jul 28 2025): https://retail-insider.com/retail-insider/2025/07/wecook-partners-with-schwartz-for-one-day-immersive-pop-up-in-toronto/
- Strategy, "WeCook hopes pop-ups and partnerships score with customers" (Aug 26 2025): https://strategyonline.ca/2025/08/26/wecook-pk-subban/
- J&W facts: /Users/erwingarcia/Claude/JWFOODSPROPOSAL/research/jw-facts.md; J&W catalog: jw-catalog.json

# Builds site/assets/catalog.js: a curated subset of REAL JW Foods products (titles, prices, variants, images, URLs
# from https://www.jwfoods.com/products.json, crawled Oct 16 2026) plus ILLUSTRATIVE macros from USDA reference values.
import json, re
C = json.load(open('research/jw-catalog.json'))
by_title = {o['title'].strip(): o for o in C}

# per-oz cooked macros (kcal, protein g, carb g, fat g) from USDA FoodData Central reference values (per 100 g / 3.527)
M = {
 'chicken_breast': (46.8, 8.8, 0, 1.0), 'chicken_thigh': (59, 7.4, 0, 3.1), 'turkey_breast': (38, 8.5, 0, 0.3),
 'ground_turkey': (50, 6.5, 0, 2.6), 'ground_chicken': (54, 6.5, 0, 2.8), 'beef_flank': (54, 7.9, 0, 2.3),
 'beef_ground_lean': (61, 7.4, 0, 3.4), 'meatballs': (62, 5.7, 1.4, 4.0), 'salmon': (58, 6.2, 0, 3.5),
 'tilapia': (36, 7.4, 0, 0.8), 'sole': (24, 4.3, 0, 0.7), 'haddock': (26, 5.7, 0, 0.2), 'shrimp': (28, 6.8, 0, 0.1),
 'sausage': (85, 4.5, 0.8, 7.0), 'white_rice': (37, 0.8, 7.9, 0.1), 'brown_rice': (32, 0.7, 6.7, 0.2),
 'quinoa': (34, 1.2, 6.0, 0.5), 'sweet_potato': (26, 0.6, 5.9, 0.1), 'potato': (26, 0.7, 6.0, 0.0),
 'broccoli': (10, 0.7, 2.0, 0.1), 'green_beans': (10, 0.5, 2.2, 0.1), 'asparagus': (6, 0.7, 1.2, 0.1),
 'brussels': (10, 0.7, 2.0, 0.1), 'spinach': (7, 0.9, 1.1, 0.1), 'cauli_rice': (7, 0.5, 1.2, 0.1),
 'mixed_veg': (18, 0.8, 3.7, 0.1), 'carrots': (10, 0.2, 2.3, 0.1), 'oats': (20, 0.7, 3.4, 0.4),
 'eggs': (42, 2.8, 0.5, 3.1), 'beans_rice': (35, 1.3, 6.8, 0.3), 'squash': (11, 0.3, 2.9, 0.0),
}
# (exact title, short name, category, macro key or None, per-unit macros if not per-oz, tags)
PICK = [
 # cooked proteins
 ('Chicken Breast  SOUVLAKI - Cooked & Portioned', 'Chicken Breast Souvlaki', 'protein', 'chicken_breast', None, ['Bestseller','Greek']),
 ('Chicken Breast TENDERS - Cooked & Portioned', 'Chicken Breast Tenders', 'protein', 'chicken_breast', None, ['Lean']),
 ('Chicken Breast JERK - Cooked & Portioned', 'Jerk Chicken Breast', 'protein', 'chicken_breast', None, ['Spicy']),
 ('Chicken Breast GREEK LEMON - Cooked & Portioned', 'Greek Lemon Chicken Breast', 'protein', 'chicken_breast', None, ['Greek']),
 ('Chicken Breast KOREAN BBQ - Cooked & Portioned', 'Korean BBQ Chicken Breast', 'protein', 'chicken_breast', None, []),
 ('Chicken Breast TERIYAKI - Cooked & Portioned', 'Teriyaki Chicken Breast', 'protein', 'chicken_breast', None, []),
 ('Chicken Breast ARABIC 7 SPICE - Cooked & Portioned', 'Arabic 7 Spice Chicken Breast', 'protein', 'chicken_breast', None, []),
 ('Chicken Breast BBQ FLAVOUR  - Cooked & Portioned', 'BBQ Chicken Breast', 'protein', 'chicken_breast', None, []),
 ('Chicken Breast GROUND - Cooked & Portioned', 'Ground Chicken Breast', 'protein', 'ground_chicken', None, []),
 ('Chicken THIGHS - Boneless - Cooked & Portioned - 4oz', 'Boneless Chicken Thighs', 'protein', 'chicken_thigh', None, []),
 ('Chicken Breast BUTTER CHICKEN - Cooked & Portioned', 'Butter Chicken Breast', 'protein', 'chicken_breast', None, []),
 ('Turkey Breast ROASTED - Cooked & Portioned', 'Roasted Turkey Breast', 'protein', 'turkey_breast', None, ['Lean']),
 ('Turkey Breast GROUND - Cooked & Portioned', 'Ground Turkey Breast', 'protein', 'ground_turkey', None, []),
 ('Beef - Flank Steak - Cooked & Portioned', 'Beef Flank Steak', 'protein', 'beef_flank', None, []),
 ('Beef - KOREAN BBQ Flank Steak  - Cooked & Portioned', 'Korean BBQ Flank Steak', 'protein', 'beef_flank', None, []),
 ('Beef Top Sirloin GROUND - Cooked & Portioned', 'Ground Top Sirloin', 'protein', 'beef_ground_lean', None, []),
 ('Beef Meatballs - Cooked & Portioned', 'Beef Meatballs', 'protein', 'meatballs', None, ['Kids']),
 ('Salmon Fillet - Cooked & Portioned', 'Salmon Fillet', 'protein', 'salmon', None, ['Omega-3']),
 ('Salmon Fillet - Honey Garlic - Cooked & Portioned', 'Honey Garlic Salmon', 'protein', 'salmon', None, ['Omega-3']),
 ('Tilapia Fillets - Cooked & Portioned', 'Tilapia Fillet', 'protein', 'tilapia', None, ['Lean']),
 ('Haddock Loin - Cooked & Portioned', 'Haddock Loin', 'protein', 'haddock', None, ['Lean']),
 ('Sole Fillet - Cooked & Portioned', 'Sole Fillet', 'protein', 'sole', None, ['Lean']),
 # carbs
 ('Basmati Rice - WHITE - Cooked & Portioned', 'White Basmati Rice', 'carb', 'white_rice', None, []),
 ('Basmati Rice - BROWN - Cooked & Portioned', 'Brown Basmati Rice', 'carb', 'brown_rice', None, []),
 ('Quinoa - Cooked & Portioned', 'Quinoa', 'carb', 'quinoa', None, ['Gluten-free']),
 ('Sweet Potato Chunks - Cooked & Portioned', 'Sweet Potato Chunks', 'carb', 'sweet_potato', None, []),
 ('Potato Baked - Cooked & Portioned', 'Baked Potato', 'carb', 'potato', None, []),
 ('Greek Lemon Roasted Potatoes - Cooked & Portioned', 'Greek Lemon Potatoes', 'carb', 'potato', None, ['Greek']),
 ('Basmati Rice - CILANTRO LIME -  Cooked & Portioned', 'Cilantro Lime Rice', 'carb', 'white_rice', None, []),
 ('Caribbean Rice & Black Beans - Cooked & Portioned', 'Caribbean Rice & Beans', 'carb', 'beans_rice', None, ['Vegan']),
 # veg
 ('Broccoli - Cooked & Portioned', 'Broccoli', 'veg', 'broccoli', None, []),
 ('Green Beans - Cooked & Portioned', 'Green Beans', 'veg', 'green_beans', None, []),
 ('Asparagus - Cooked & Portioned', 'Asparagus', 'veg', 'asparagus', None, []),
 ('Brussel Sprouts - Cooked & Portioned', 'Brussels Sprouts', 'veg', 'brussels', None, []),
 ('Spinach - Cooked & Portioned', 'Spinach', 'veg', 'spinach', None, []),
 ('Cauliflower Rice - Cooked & Portioned', 'Cauliflower Rice', 'veg', 'cauli_rice', None, ['Low-carb']),
 ('Mixed Veggies - Cooked & Portioned', 'Mixed Veggies', 'veg', 'mixed_veg', None, []),
 ('Broccoli & Cauliflower Mix - Cooked & Portioned', 'Broccoli & Cauliflower', 'veg', 'broccoli', None, []),
 # pre-set meals (per-unit macros, 4oz protein version, illustrative)
 ('Pre-Set Meal - Chicken Breast Souvlaki, Broccoli & Greek Lemon Potatoe', 'Souvlaki, Broccoli & Greek Potatoes', 'meal', None, (420, 41, 30, 9), ['Bestseller']),
 ('Pre-Set Meal - Salmon Fillet, Brussel Sprouts & Quinoa', 'Salmon, Brussels & Quinoa', 'meal', None, (430, 31, 32, 17), ['Omega-3']),
 ('Pre-Set Meal - Beef Flank Steak, Green Beans & Baked Potato', 'Flank Steak, Green Beans & Potato', 'meal', None, (380, 34, 33, 10), []),
 ('Pre-Set Meal - Turkey Breast, Spinach & White Rice', 'Turkey, Spinach & Rice', 'meal', None, (330, 37, 33, 2), ['Lean']),
 ('Pre-Set Meal - Tilapia Fillet, Asparagus & Brown Rice', 'Tilapia, Asparagus & Brown Rice', 'meal', None, (310, 33, 32, 4), ['Lean']),
 ('Pre-Set Meal - Chicken Breast Tenders, Broccoli & Sweet Potato Chunks', 'Tenders, Broccoli & Sweet Potato', 'meal', None, (340, 38, 32, 4), []),
 ('Pre-Set Meal - Jerk Chicken Breast (Boneless), Green Beans & Sweet Pot', 'Jerk Chicken, Green Beans & Sweet Potato', 'meal', None, (350, 38, 33, 4), ['Spicy']),
 ('Pre-Set Meal - Beef Top Sirloin Ground, Green Beans  & Sweet Potato Ch', 'Ground Sirloin, Green Beans & Sweet Potato', 'meal', None, (420, 32, 33, 14), []),
 ('Pre-Set Meal - Teriyaki Chicken Breast, Green Beans & Basmati White Ri', 'Teriyaki Chicken, Green Beans & Rice', 'meal', None, (370, 37, 42, 4), []),
 # breakfast
 ('Egg Bites - EGG WHITES, SPINACH & FETA - Cooked & Portioned - 2/Pkg', 'Egg White Bites, Spinach & Feta', 'breakfast', None, (170, 12, 11, 7), ['Vegetarian']),
 ('Egg Bites - OMELETTE W/BACON & DOUBLE CHEDDAR CHEESE- Cooked & Portion', 'Omelette Bites, Bacon & Cheddar', 'breakfast', None, (300, 19, 9, 20), []),
 ('Steel Cut Oats - Cooked & Portioned - 6oz', 'Steel Cut Oats', 'breakfast', None, (120, 4, 20, 2.5), ['Vegan']),
 ('Pre-Set Meal - BREAKFAST - Scrambled Eggs, Turkey Breakfast Sausages &', 'Eggs, Turkey Sausage & Home Fries', 'breakfast', None, (390, 28, 18, 23), []),
 ('BREAKFAST WRAP - EGG, SPINACH & FETA', 'Breakfast Wrap, Egg, Spinach & Feta', 'breakfast', None, (310, 19, 28, 13), []),
 ('Apple Cinnamon Oatmeal Breakfast Bar BAKED - 3oz - Cooked & Portioned', 'Apple Cinnamon Oat Bar', 'breakfast', None, (260, 7, 38, 9), ['Kids']),
 # wraps / soups
 ('WRAP - CHICKEN SOUVLAKI', 'Chicken Souvlaki Wrap', 'wrap', None, (420, 34, 38, 13), []),
 ('WRAP - CHICKEN BREAST FAJITAS', 'Chicken Fajita Wrap', 'wrap', None, (450, 36, 40, 14), []),
 ('WRAP - BEEF FLANK FAJITAS', 'Beef Flank Fajita Wrap', 'wrap', None, (480, 33, 40, 18), []),
 ('WRAP - TURKEY BACON CLUB', 'Turkey Bacon Club Wrap', 'wrap', None, (470, 35, 37, 19), []),
 ('Chicken Chili - Cooked & Portioned - 10oz', 'Chicken Chili, 10oz', 'soup', None, (320, 30, 28, 8), []),
 ('Beef Chili - Cooked & Portioned - 10oz', 'Beef Chili, 10oz', 'soup', None, (380, 28, 26, 17), []),
 ('Lemon Chicken Rice Soup  - 10oz portion - Cooked & Portioned', 'Lemon Chicken Rice Soup', 'soup', None, (210, 16, 24, 5), ['Greek']),
 # premium raw
 ('WAGYU STRIPLOIN STEAK - 8-9OZ', 'Wagyu Striploin Steak, 8-9oz', 'raw', None, None, ['Premium']),
 ('BEEF RIBEYE BONELESS AAA', 'AAA Boneless Ribeye', 'raw', None, None, ['AAA']),
 ('BEEF RIBEYE BONE-IN AAA', 'AAA Bone-In Ribeye', 'raw', None, None, ['AAA']),
 ('BEEF - NEW YORK STRIPLOIN AAA', 'AAA New York Striploin', 'raw', None, None, ['AAA']),
 ('BEEF TENDERLOIN AAA/CAB -6-8oz Portion', 'AAA Beef Tenderloin, 6-8oz', 'raw', None, None, ['AAA']),
 ('PICANHA (TOP SIRLOIN CAP) GRILLING STEAK 9-10oz', 'Picanha Grilling Steak', 'raw', None, None, []),
 ('LAMB CHOPS - RAISED IN SOUTHERN ONTARIO - 8/PKG', 'Ontario Lamb Chops, 8 pack', 'raw', None, None, ['Ontario']),
 ('FRENCHED LAMB RACK', 'Frenched Lamb Rack', 'raw', None, None, []),
 ('BISON RIBEYE STEAKS', 'Bison Ribeye Steak', 'raw', None, None, ['Game']),
 ('BISON STRIPLOIN STEAKS - 6oz portions', 'Bison Striploin, 6oz', 'raw', None, None, ['Game']),
 ('VENISON STRIPLOIN STEAKS - 6oz portions', 'Venison Striploin, 6oz', 'raw', None, None, ['Game']),
 ('CASE of PORTIONED CHICKEN BREAST -  Vacuumed in 4/pk', 'Case of Portioned Chicken Breast (4 kg)', 'case', None, None, ['Ontario','Bulk']),
 ('CHICKEN BREAST MARINATED - 4 KG CASE', 'Marinated Chicken Breast Case (4 kg)', 'case', None, None, ['Bulk']),
 ('GROUND - BEEF EXTRA LEAN  AAA - 10 X 1LB - CASE', 'Extra Lean AAA Ground Beef, 10 x 1 lb', 'case', None, None, ['Bulk']),
 ('ONTARIO GROUND TURKEY BREAST - CASE - 10bgs X 1lb', 'Ontario Ground Turkey Breast, 10 x 1 lb', 'case', None, None, ['Bulk','Ontario']),
 ('CHICKEN BREAST SOUVLAKI - NO SALT - 5KG CASE', 'No-Salt Chicken Souvlaki Case (5 kg)', 'case', None, None, ['Bulk']),
 ('QUARTER COW PURCHASE', 'Quarter Cow', 'whole', None, None, ['Whole animal']),
 ('ONTARIO RAISED WHOLE LAMB', 'Ontario Whole Lamb', 'whole', None, None, ['Whole animal','Ontario']),
 ('AAA WHOLE STRIPLOIN - CUT ANY SIZE AND VACUMED 11-12lbs APPROXIMATELY', 'Whole AAA Striploin, cut to order', 'whole', None, None, ['Cut to order']),
 # boxes
 ("GENTLEMENS'S BOX SPECIAL", "Gentleman's Box", 'box', None, None, ['Gift']),
 ('A TASTE OF GREECE BOX SPECIAL', 'A Taste of Greece Box', 'box', None, None, ['Gift','Greek']),
 ('LONG WEEKEND BOX SPECIAL', 'Long Weekend Box', 'box', None, None, ['Gift']),
 ('Girls Night Box Special', 'Girls Night Box', 'box', None, None, ['Gift']),
 ('ULTIMATE BBQ DAD PACK', 'Ultimate BBQ Dad Pack', 'box', None, None, ['Gift']),
 ('KIDS FAVOURITE COMBO SPECIAL', 'Kids Favourite Combo', 'box', None, None, ['Kids']),
 ('COMBO #1 SPECIAL', 'Combo #1', 'box', None, None, []),
]

def tidy(t):
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r'(?i)\bsingle\b\s*-?\s*', 'Single ', t); t = re.sub(r'(?i)\bcase\b\s*-?\s*', 'Case ', t)
    t = re.sub(r'(?i)\s*portions?\b', '', t); t = re.sub(r'(?i)(\d)OZ', r'\1oz', t)
    t = t.replace('Single 9- 10oz', 'Single 9-10oz').replace(' - ', ' ').replace('  ', ' ')
    return t.strip()

def oz_of(label):
    m = re.search(r'(\d+(?:\.\d+)?)\s*oz', label, re.I)
    return float(m.group(1)) if m else None

out = []
missing = []
for t, name, cat, mk, unit, tags in PICK:
    o = by_title.get(t)
    if not o:
        cands = [x for x in C if x['title'].strip().startswith(t[:40])]
        o = cands[0] if cands else None
    if not o:
        missing.append(t); continue
    vs = []
    for v in o['variants']:
        lab = 'Single' if v['t'] == 'Default Title' else tidy(v['t'])
        oz = oz_of(lab) or (oz_of(o['title']) if v['t'] == 'Default Title' else None)
        vs.append({'label': lab if lab != 'Single' or not oz else f"{int(oz) if oz==int(oz) else oz}oz", 'oz': oz, 'price': v['p']})
        if re.search(r'2\s*/\s*pkg', o['title'], re.I) and vs[-1]['label'] == 'Single': vs[-1]['label'] = '2-pack'
    rec = {'id': o['handle'], 'name': name, 'title': o['title'].strip(), 'cat': cat, 'variants': vs,
           'price': vs[0]['price'], 'img': (o['img'] + ('&' if '?' in o['img'] else '?') + 'width=600') if o['img'] else None,
           'url': 'https://www.jwfoods.com/products/' + o['handle'], 'tags': tags}
    if mk:
        k, p, c, f = M[mk]; rec['perOz'] = {'kcal': k, 'p': p, 'c': c, 'f': f}
    if unit:
        k, p, c, f = unit; rec['perUnit'] = {'kcal': k, 'p': p, 'c': c, 'f': f}
    out.append(rec)

# Extra real products that the play specs asked for (research/catalog-extra.json): added as-is, no macros.
import os
by_handle = {o['handle']: o for o in C}
have = {r['id'] for r in out}
def guess_cat(o):
    t = (o['title'] + ' ' + (o['type'] or '')).upper()
    if 'CASE' in t or 'BULK' in t or '10LB' in t or '10 X' in t: return 'case'
    if any(k in t for k in ('SAUCE', 'PITA', 'TZATZIKI', 'BREAD', 'SPICE')): return 'pantry'
    if 'COOKED' in t: return 'protein'
    return 'raw'
if os.path.exists('research/catalog-extra.json'):
    for h in json.load(open('research/catalog-extra.json')):
        o = by_handle.get(h)
        if not o or h in have: continue
        vs = [{'label': 'Single' if v['t'] == 'Default Title' else tidy(v['t']), 'oz': oz_of(v['t']), 'price': v['p']} for v in o['variants']]
        name = re.sub(r'\s+', ' ', o['title']).strip().title().replace('Aaa', 'AAA').replace('Lb', 'lb').replace('Oz', 'oz')
        out.append({'id': h, 'name': name, 'title': o['title'].strip(), 'cat': guess_cat(o), 'variants': vs, 'price': vs[0]['price'],
                    'img': (o['img'] + ('&' if '?' in o['img'] else '?') + 'width=600') if o['img'] else None,
                    'url': 'https://www.jwfoods.com/products/' + h, 'tags': ['More']})

hdr = ("/* J&W Foods proposal: shared demo catalog. Product names, prices, variants, photos and URLs are REAL, taken from\n"
       "   https://www.jwfoods.com/products.json on Oct 16 2026. Macros are ILLUSTRATIVE estimates from USDA reference values\n"
       "   (perOz for single components, perUnit for pre-set meals/breakfast/wraps); JW does not publish nutrition panels online.\n"
       "   Generated by tools/build_catalog.py - do not edit by hand. */\n")
open('site/assets/catalog.js', 'w').write(hdr + 'window.JWCAT = ' + json.dumps(out, indent=1, ensure_ascii=False) + ';\n')
print(len(out), 'products; missing:', missing)

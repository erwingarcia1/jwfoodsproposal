# Builds site/assets/site-data.js (window.JW) from the two workflow outputs:
#   research/research-output.raw  (research + selection + deep-dives)
#   research/strategy-output.raw   (plays, $1M plan, agent roster, CFO review, portfolio, edited copy)
# Usage: python3 tools/build_data.py
import json, re, math

def load(p):
    s = open(p).read()
    d = json.loads(s[s.find('{'):])
    return d.get('result', d)

RS = load('research/research-output.raw')
ST = load('research/strategy-output.raw')
ED = ST['edited']
ROSTER = ST['roster']
plays_in = sorted(ST['plays'], key=lambda p: p['n'])
comps = ED['competitors']

def fmM(v):
    return '$' + ('%.1f' % (round(v / 1e5) / 10)) + 'M' if v >= 1e6 else '$' + str(int(round(v / 1e3))) + 'K'

agent_ids = {a['id'] for a in ROSTER['agents']}
pa = {x['n']: x['agents'] for x in ROSTER['playAgents']}

# Notes that still quoted pre-CFO figures (plays 1, 2 and 5 were trimmed by the CFO review): replace or drop by prefix.
NOTE_FIX = {
    1: [('Gross margin 40% after the 10% discount', 'Gross margin 40% after the 10% discount (model-assumptions.md). Year 1 mid: $341K x 40% = ~$136K gross profit, minus ~$89K all-in J&W costs = ~$47K contribution before Minastech\'s fee.'),
        ('Year 2: $757K', 'Year 2: $726K x 40% = ~$290K gross profit, minus ~$120K running costs = ~$170K contribution.'),
        ('Cross-check: market-benchmarks.md', 'Cross-check: market-benchmarks.md section 11 says ~320 active every-2-weeks subscribers at $120 is about $1M gross. This play\'s year-2 average of ~299 at $125 with 10% skips gives ~$875K gross.'),
        ('Revenue counts only subscribers who were not already', None)],
    2: [('Incrementality 0.85', 'Incrementality 0.80 (trimmed from 0.85 in the CFO review): most volume is new, because a gym freezer sells to people who would not place a $100 route order, but some trainers and gym owners already buy cases at retail and will move to partner pricing. Existing informal restaurant and trade accounts are not counted.'),
        ("J&W's own costs: year 1", "J&W's own costs: year 1 is ~$65,000 (setup ~$26,000 including freezers, plus ~$3,400 a month), against ~$39,400 gross profit, so about -$26,000 in year 1. Year 2 is ~$78,000 against ~$127,800, so about +$50,000. This is a volume and plant-utilisation play, not a high-margin one.")],
    5: [('The $120 average gift already nets out', 'The $120 average gift already nets out volume pricing (5% / 8% / 10%). Gross margin is planned at 38%: the model\'s 40% for gift boxes, less the volume tiers most accounts will use.'),
        ('Year-1 monthly shape', None),
        ('Capacity: Holiday 2026', 'Capacity: Holiday 2026 is about 360 gifts over 5 weeks (18 accounts x 20), peaking in the week of Dec 14. Holiday 2027 is about 1,440 gifts over 7 weeks (60 accounts x 24), so it needs one seasonal packer and an extra Wednesday van in December.'),
        ('Contribution after JW', 'Contribution after J&W\'s own costs, before Minastech\'s fee: year 1 is about $36K gross profit less ~$29K running costs and $5.5K setup, so roughly break-even; its value is Q4 cash and the door to HR buyers. Year 2 is about $120K less ~$45K, leaving about $75K.'),
        ('Sanity check: year 1 is about 5%', 'Sanity check: year 1 is about 4% of J&W\'s ~$2.5M mid-case revenue and the run-rate about 13%. The market-benchmarks.md upside of 115 firms x 60 boxes x $120 (about $830K) would need 1% of the ~11-14K GTA locations with 50+ staff.')],
}
def fix_notes(n, notes):
    out = []
    for m in notes:
        rule = next((r for r in NOTE_FIX.get(n, []) if m.startswith(r[0])), None)
        if rule is None: out.append(m)
        elif rule[1]: out.append(rule[1])
    return out

plays = []
for p in plays_in:
    n = p['n']
    c = comps[n - 1] if n - 1 < len(comps) else {}
    mo = dict(p['modelledOn'])
    if c.get('name'):
        mo['name'] = c['name']
    ags = [a for a in pa.get(n, []) if a['id'] in agent_ids]
    q = {k: v for k, v in p.items() if k not in ('prototype', 'agentNeeds', 'cfo')}
    q['mathNotes'] = fix_notes(n, p.get('mathNotes', []))
    q.update({
        'modelledOn': mo,
        'file': f"prototypes/{n:02d}-{p['slug']}.html",
        'thumb': f"assets/shots/{n:02d}-phone.jpg",
        'thumbWide': f"assets/shots/{n:02d}-wide.jpg",
        'agents': [a['id'] for a in ags],
        'agentNotes': {a['id']: a['onScreen'] for a in ags},
        'inPlan': n in ST['portfolio'].get('inPlan', []),
    })
    plays.append(q)

# Year-2 low/high and J&W's own running costs per play, taken from each play's own math (final review, findings 21-22)
RUN_RANGE = {1: (371000, 1174000), 2: (315000, 836000), 3: (305000, 957000), 4: (310000, 980000), 5: (140000, 500000), 6: (299000, 535000), 7: (113000, 480000)}
OWN_COST = {1: (88900, 120000), 2: (63400, 78000), 3: (71400, 76800), 4: (54500, 80000), 5: (34500, 45000), 6: (36000, 42000), 7: (25300, 40000)}
for p in plays:
    lo, hi = RUN_RANGE.get(p['n'], (p['runRate'], p['runRate']))
    p['runRateLow'], p['runRateHigh'] = lo, hi
    y1c, y2c = OWN_COST.get(p['n'], (0, 0))
    p['costs'] = dict(p['costs'], year1Total=y1c, year2Total=y2c)

# portfolio + return figures
pf = ST['portfolio']
ov = pf['overlapPct'] / 100
inplan = [p for p in plays if p['inPlan']]
y1 = {k: sum(p['year1'][k] for p in inplan) * (1 - ov) for k in ('low', 'mid', 'high')}
y2mid = sum(p['runRate'] for p in inplan) * (1 - ov)
y2 = {'low': sum(p['runRateLow'] for p in inplan) * (1 - ov), 'mid': y2mid, 'high': sum(p['runRateHigh'] for p in inplan) * (1 - ov)}
gp1 = sum(p['year1']['mid'] * p['marginPct'] / 100 for p in inplan) * (1 - ov)
gp2 = sum(p['runRate'] * p['marginPct'] / 100 for p in inplan) * (1 - ov)
blend = gp1 / y1['mid'] if y1['mid'] else 0.35
fee = ED['fee']
ads = ED['roi'].get('adsMonthly', 0)
own1 = sum(p['costs']['year1Total'] for p in inplan)
own2 = sum(p['costs']['year2Total'] for p in inplan)
cost1 = fee['monthly'] * 12 + fee['setup'] + ads * 12 + own1
cost2 = fee['monthly'] * 12 + ads * 12 + own2
portfolio = {
    'overlapPct': pf['overlapPct'], 'inPlan': pf['inPlan'], 'note': ST['skeptic']['portfolio'].get('note', ''),
    'year1': {k: round(v, -3) for k, v in y1.items()},
    'year2': {k: round(v, -3) for k, v in y2.items()},
    'grossProfit': {'year1': round(gp1, -3), 'year2': round(gp2, -3), 'blendedPct': round(blend * 100)},
    'allInYear1Cost': round(cost1, -3), 'allInYear2Cost': round(cost2, -3),
}
def fmR(v):
    if v < 1e6: return '$' + str(int(round(v / 1e3))) + 'K'
    t = ('%.2f' % (v / 1e6)).rstrip('0')
    return '$' + (t + '0' if t.endswith('.') else t) + 'M'
portfolio['year1']['plan'] = fmR(round(y1['low'], -3)) + '–' + fmR(round(y1['high'], -4))
portfolio['year2']['plan'] = fmR(round(y2['low'], -5)) + '–' + fmR(round(y2['high'], -5))
be_fee = (fee['monthly'] * 12 + fee['setup']) / blend if blend else 0
portfolio['breakEven'] = f"about {fmM(round(be_fee, -3))} of added revenue in year 1 at a {round(blend*100)}% blended margin"
portfolio['roiYear1'] = f"year-1 gross profit of about {fmM(gp1)} is {gp1/cost1:.1f}x the all-in year-1 cost of {fmM(cost1)}"
portfolio['roiYear2'] = f"{gp2/cost2:.1f}x"

M = ST['million']
million = dict(M)
pid = M['path']['ideas']
idea = {d['n']: d for d in M['ideas']}
path_total = sum(idea[n]['sales']['mid'] for n in pid if n in idea) * (1 - M['path'].get('overlapPct', 10) / 100)
def sentences(t, n):
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z$])', t.strip())
    return ' '.join(parts[:n])
million['path'] = dict(M['path'], total=round(path_total, -3), summary=sentences(M['path']['summary'], 4), rampNote=sentences(M['path']['rampNote'], 1))
for d in million['ideas']:
    d.pop('cfo', None)
KEYS = [('gift', 5), ('capacity', 0), ('licence', 0), ('goal plan', 1), ('pre-sale', 1), ('wild fork', 3), ('butcher club', 3), ('at work', 4), ('clinic', 10), ('dietitian', 10)]
for f in million.get('firstTests', []):
    t = (f.get('test', '') + ' ' + f.get('signal', '')).lower()
    idn = next((n for k, n in KEYS if k in t), None)
    f['idea'] = idn or None
    f['name'] = next((d['name'] for d in million['ideas'] if d['n'] == idn), 'Before any play: capacity and licence')

roi = dict(ED['roi'], overlapPct=pf['overlapPct'])

def scrub(o):
    # client-facing clean-up of internal notes the agents left in copy
    if isinstance(o, dict): return {k: scrub(v) for k, v in o.items()}
    if isinstance(o, list): return [scrub(v) for v in o]
    if isinstance(o, str):
        o = o.replace('Placeholder for Erwin to confirm. ', '').replace('Set at the bottom of our range because year 1 is a build year.', 'Priced for a build year.')
        o = re.sub(r'Owner-led brand risk \(a 2020 Yelp complaint[^)]*\)\.?', 'Key-person risk: the brand leans on the owners.', o)
        o = o.replace('Owner-led brand risk (a 2020 Yelp complaint).', 'Key-person risk: the brand leans on the owners.')
    return o

JW = {
    'business': {
        'name': 'J&W Foods · Meal Butler', 'legal': 'J & W Foods Inc', 'address': '2201 Brimley Rd, Unit 1, Scarborough, ON M1S 4N7',
        'phone': '(416) 298-1350', 'founded': 1995, 'plantSince': 2008, 'realFacts': ED['realFacts'],
    },
    'preparedBy': {'name': 'Minastech', 'person': 'Erwin Garcia', 'email': 'erwin.garcia@minastech.ca', 'date': 'October 16, 2026'},
    'hub': ED['hub'], 'fee': fee, 'baseline': ED['baseline'], 'portfolio': portfolio, 'roi': roi,
    'plays': plays, 'agents': ROSTER['agents'], 'tenX': ROSTER['tenX'], 'million': million,
    'competitors': comps, 'research': ED['research'], 'proposal': ED['proposal'],
}
hdr = ('/* J&W Foods growth proposal: shared data for every page and prototype. Generated by tools/build_data.py from the\n'
       '   research and strategy workflows (research/*.raw). All money figures are CAD estimates unless they are JW\'s own prices. */\n')
JW = scrub(JW)
import os
FIXES = json.load(open('research/data-fixes.json')) if os.path.exists('research/data-fixes.json') else []
hits = {i: 0 for i in range(len(FIXES))}
def apply_fixes(o):
    if isinstance(o, dict): return {k: apply_fixes(v) for k, v in o.items()}
    if isinstance(o, list): return [apply_fixes(v) for v in o]
    if isinstance(o, str):
        for i, f in enumerate(FIXES):
            if f['old'] in o:
                o = o.replace(f['old'], f['new']); hits[i] += 1
    return o
JW = apply_fixes(JW)
missed = [FIXES[i]['old'][:70] for i, c in hits.items() if c == 0]
print('data-fixes applied:', sum(1 for c in hits.values() if c), 'of', len(FIXES), '| not found:', missed)
open('site/assets/site-data.js', 'w').write(hdr + 'window.JW = ' + json.dumps(JW, indent=1, ensure_ascii=False) + ';\n')
print('plays', [(p['n'], p['name'], p['year1']['mid'], p['runRate'], p['marginPct'], p['inPlan']) for p in plays])
print('portfolio', json.dumps(portfolio, indent=1))
print('million path', pid, round(path_total))
print('agents', len(ROSTER['agents']), 'fee', fee)

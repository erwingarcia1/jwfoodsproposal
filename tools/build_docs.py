# Builds site/assets/research-docs.js (window.JWDOCS) from the research markdown files, for research.html.
# Client-facing: clean() strips personal-review lines, family names, prototype build specs, local paths and dead links,
# and applies -ize spelling. The research/*.md sources are never edited; fix the output here.
import json, os, re

R = 'research'
DOCS = [
    ('jw-facts', 'jw-facts.md', 'J&W today: the on-site facts', 'What jwfoods.com, its catalogue and its delivery page say, crawled on October 16, 2026.'),
    ('jw-audit', 'jw-audit.md', 'J&W today: the off-site audit', 'Reviews, social, search visibility, tech stack, wholesale history and the revenue estimate.'),
    ('gta-mealprep', 'competitors-gta-mealprep.md', 'Premium meal prep in the GTA', 'Eighteen GTA and Ontario meal-prep services, ranked by how premium and how directly competitive they are.'),
    ('gta-meat', 'competitors-gta-meat-grocery.md', 'Premium butchers and grocers in the GTA', 'The butchers, meat-delivery services and specialty grocers that compete with J&W’s raw side.'),
    ('global', 'competitors-global.md', 'Best in class, worldwide', 'The global operators whose models J&W could copy, with revenue and scale.'),
    ('market', 'market-benchmarks.md', 'Market benchmarks', 'Market size, GTA households and gyms, churn, CAC, email, delivery and margin benchmarks.'),
    ('ai', 'ai-agents-research.md', 'AI agents in food and DTC', 'How food, meal-prep, butcher and Shopify brands use AI agents, with results and costs.'),
    ('assumptions', 'model-assumptions.md', 'The shared modelling assumptions', 'The figures every estimate in this proposal uses, in one place.'),
]
for i in range(1, 8):
    f = f'competitor-{i:02d}.md'
    if os.path.exists(os.path.join(R, f)):
        first = open(os.path.join(R, f)).read().splitlines()[0].lstrip('# ').strip()
        DOCS.append((f'dive-{i:02d}', f, f'Deep-dive: {first}' if first else f'Competitor deep-dive {i}', 'Verification, prices, flows worth borrowing and the design notes behind the prototype.'))
for f in sorted(os.listdir(os.path.join(R))):
    m = re.match(r'play-(\d\d)\.md$', f)
    if m:
        first = open(os.path.join(R, f)).read().splitlines()[0].lstrip('# ').strip()
        DOCS.append((f'play-{m.group(1)}', f, first or f'Play {m.group(1)}', 'The full play: mechanism, math, KPIs, agents, assumptions and risks.'))

# ---- Client-facing clean-up (final-review findings 1, 3, 5, 7, 14, 49, 51, 79). Sources stay untouched. ----

def drop_sections(md, heading_re):
    """Drop every '## ' section whose heading matches heading_re, through to the next '## ' heading."""
    out, skip, fence = [], False, False
    for line in md.splitlines():
        if line.lstrip().startswith('```'):
            fence = not fence
        if not fence and line.startswith('## '):
            skip = bool(re.match(heading_re, line))
        if not skip:
            out.append(line)
    return '\n'.join(out)

LOCAL_FACTS = 'J&W catalogue and facts (jwfoods.com, crawled Oct 16, 2026)'
FILE_LIST = re.compile(r'^(?:[\w&\' ]+:\s*)?`?[\w./-]+\.(?:md|json)`?(?:,\s*`?[\w./-]+\.(?:md|json)`?)*$')

def fix_local_paths(md):
    out = []
    for line in md.splitlines():
        if 'site/prototypes/' in line or 'JWC.init' in line:
            continue
        if '/Users/' in line:
            m = re.match(r'^(\s*[-*]\s*)([^:]*):\s*(.*)$', line)
            if not m:
                continue
            tail = [seg.strip() for seg in re.split(r';\s*|\s+·\s+', m.group(3))[1:]]
            tail = [t for t in tail if t and '/Users/' not in t and not FILE_LIST.match(t)]
            line = m.group(1) + m.group(2) + ': ' + LOCAL_FACTS + ''.join(' · ' + t for t in tail)
        out.append(line)
    return '\n'.join(out)

# Dead or hijacked links. Live replacements first (label fixed where the old label named the dead site).
URL_SWAPS = [
    ('https://citymatters.london/counting-macros-fresh-fitness-food-math', 'https://www.cbinsights.com/company/fresh-fitness-food/financials', lambda t: 'CB Insights: Fresh Fitness Food' if 'Fresh Fitness' in t else 'CB Insights'),
    ('https://octaneai.com/customers/wicked-edge', 'https://octaneai.com/case-studies/wicked-edge', None),
    ('https://octaneai.com/platform', 'https://octaneai.com/', None),
    ('https://www.volur.ai/solutions', 'https://www.volur.ai/', lambda t: 'Völur' if t == 'Völur solutions' else t),
]
# Dead links with no replacement: keep the citation text, drop the link. Value = text used when the URL is bare.
DEAD = [
    (r'https?://blog\.revgear\.com/megafit-meals-review/?', 'RevGear review'),
    (r'https?://[a-z]+\.worktrucksolutions\.com/[^\s)]*', 'dealer listing'),
    (r'https?://careers\.cookunity\.com/jobs/7507651003', 'CookUnity careers'),
    (r'https?://expre\.co\.uk/\?p=30658', 'EXPRE'),
    (r'https?://tenten\.co/shopify/ai-product-photography-shopify/?', 'tenten AI photography guide'),
    (r'https?://www\.wecookmeals\.ca/api/menus/422/meals/steak-spiced-turkey-protein-power-bowl/details', 'WeCook meal detail API'),
    (r'https?://aiagentrank\.io/blog/apollo-io-review-2026', 'AI Agent Rank'),
    (r'https?://v2\.iotone\.com/case-study/[^\s)]*', 'IoT ONE'),
    (r'https?://www\.vincesmarket\.com/?', None),
]
GONE = 'page no longer available'

def fix_links(md):
    for old, new, relabel in URL_SWAPS:
        md = re.sub(r'\[([^\]]*)\]\(' + re.escape(old) + r'\)', lambda m: '[' + (relabel(m.group(1)) if relabel else m.group(1)) + '](' + new + ')', md)
        md = md.replace(old, new)
    for pat, bare in DEAD:
        md = re.sub(r'\(\[([^\]]+)\]\(' + pat + r'\)\)', r'(\1, ' + GONE + ')', md)
        md = re.sub(r'\[([^\]]+)\]\(' + pat + r'\)', r'\1 (' + GONE + ')', md)
        md = re.sub(pat, (bare + ' (' + GONE + ')') if bare else (lambda m: re.sub(r'^https?://(www\.)?|/$', '', m.group(0))), md)
    # The Foodery claim (finding 7): its only source is retired.
    md = md.replace('28% lower delivery costs vs paper-and-pencil zip-code routing', '28% lower delivery costs than manual routing (vendor figure; source page retired)')
    md = md.replace('The Foodery: -28% delivery cost (§2.11)', 'The Foodery: -28% delivery cost (vendor figure; source page retired; §2.11)')
    # Relative links to research files (they 404 on the site): plain text.
    md = re.sub(r'\[([^\]]+)\]\((?!https?://|#|mailto:)[^)\s]*\)', r'\1', md)
    return md

# People: no family members named; Bill and Stavros stay as the owners (always "Stavros").
NAME_FIXES = {
    'dive-06': [('customers know the owners by name (Bill, Tasia, Lucas)', 'customers know Bill and his team by name')],
    'play-01': [('**Meal Butler lead** (e.g. Lucas or Tasia)', '**Meal Butler lead** (named at kickoff)')],
    'play-02': [
        ('a person (Lucas or the account lead) approves', 'a person (the account lead) approves'),
        ('Lucas approves each sequence.', 'The account lead approves each sequence.'),
        ('Hands any pricing exception to Lucas.', 'Hands any pricing exception to the account lead.'),
        ('**Lucas (or a new B2B account lead):**', '**Account lead (an existing team member or a new B2B hire):**'),
        ('10. **Owner-brand risk.** Partners see the brand daily. Make Lucas and the team the face of the program.', '10. **One contact.** Give every partner a named account lead.'),
    ],
    'play-04': [
        ('Lucas or the owner run free tastings', 'The account lead or the owner runs free tastings'),
        ('**Lucas or the owner:**', '**Account lead or the owner:**'),
        ('Tastings depend on Bill or Lucas.', 'Tastings depend on Bill or the account lead.'),
    ],
    'play-05': [
        ('(a named person, for example Lucas or Tasia)', '(a named person, chosen at kickoff)'),
        (' (jw-audit.md §2)', ''),
    ],
    'play-06': [
        ('Lucas (or the coach desk) approves', 'the coach desk approves'),
        ('| Lucas or Tasia (food, orders, plan)', '| The coach desk (food, orders, plan)'),
        ('**Lucas (or a hired part-time nutrition coach), "coach desk":**', '**Coach desk (a team member or a hired part-time nutrition coach):**'),
        ('**Tasia:** ~1–2 h a week', '**Store lead:** ~1–2 h a week'),
        ('If the coach desk depends on Lucas alone it stalls when he is away.', 'If the coach desk depends on one person it stalls when that person is away.'),
    ],
    'play-07': [
        ('(Tasia or Lucas, as J&W decides)', '(a named team member, as J&W decides)'),
        ('**Butcher or Lucas:**', '**Butcher or the fundraising coordinator:**'),
    ],
    'assumptions': [('- Owner-led brand: customers name "Bill" (co-founder William Fehr), Tasia and Lucas.', '- Team-led brand: customers name "Bill" (co-founder William Fehr) and his team.')],
}
LINE_FIXES = {  # whole-line rewrites, keyed by the line's opening text
    'jw-audit': [
        ('3. **The owner is the brand.**', '3. **The owner is the brand:** reviews name Bill and his team personally and praise the service.'),
        ('6. **Brand-risk management:**', '6. **Team-led brand:** show the wider J&W team and the product alongside the founders, and set up a review-response playbook, since the AI agents can draft replies.'),
        ('| **Tasia**', None),
        ('| **Lucas**', None),
    ],
    'play-07': [('- **Owner-led brand.**', '- **Trust.** Schools and faith groups check reviews before they partner. Show the 4.8★ Google rating (611 reviews) and give each group one named coordinator.')],
}

def fix_people(key, md):
    for old, new in NAME_FIXES.get(key, []):
        if old not in md:
            print(f'  note: {key}: expected text not found: {old[:60]!r}')
        md = md.replace(old, new)
    fixes = LINE_FIXES.get(key, [])
    if fixes:
        out = []
        for line in md.splitlines():
            hit = next((f for f in fixes if line.lstrip().startswith(f[0])), None)
            if hit and hit[1] is None:
                continue
            out.append(re.match(r'\s*', line).group(0) + hit[1] if hit else line)
        md = '\n'.join(out)
    md = md.replace('Stavros "Steve/Steven" Trougakos', 'Stavros Trougakos').replace('Steven (Stavros)', 'Stavros')
    md = re.sub(r'\bSteven?\b', 'Stavros', md)
    md = md.replace(' (jw-audit.md §2)', '')
    return md

# -ise -> -ize (US/Canadian -ize house style), never inside URLs.
ISE = re.compile(r'(subsid|annual|personal|cannibal|util|priorit|organ|optim|recogn|minim|standard|final|summar|random|product|normal|item|incentiv|custom)(is)(e|ed|es|ing|ation|ations|er|ers)\b', re.I)
URLISH = re.compile(r'(https?://[^\s)\]>]+|\]\([^)]*\))')

def ize(md):
    parts = URLISH.split(md)
    for i in range(0, len(parts), 2):
        parts[i] = ISE.sub(lambda m: m.group(1) + ('IZ' if m.group(2).isupper() else 'iz') + m.group(3), parts[i])
    return ''.join(parts)

# Client-facing wording: the salt/sugar/oil line is J&W's own claim, and the research-run budget notes are internal.
TEXT_FIXES = [
    ("J&W's salt-, sugar- and oil-free cooking makes this credible.", "J&W's promise of salt-, sugar- and oil-free cooking makes this credible."),
    ('a cooked and portioned line that has no added salt, sugar or oil,', 'a cooked and portioned line marketed as having no added salt, sugar or oil,'),
    ("This fits J&W's existing no-salt, no-sugar, no-oil line,", "This fits J&W's existing line, which it markets as having no added salt, sugar or oil,"),
    ('The shared web-search budget ran out partway through. After that I collected data only by fetching', 'Part of this data was collected by fetching'),
    ('The shared web-search budget for this workflow ran out after the first four searches, so almost every figure below comes from', 'Almost every figure below comes from'),
    ('A follow-up run with search budget should fill the gaps listed in section 7.', 'The gaps are listed in section 7.'),
    ('This run used up its shared web-search budget before every candidate was covered in depth. These items were not verified and are listed as not found:', 'Not every candidate could be covered in depth. These items were not verified and are listed as not found:'),
    (' A follow-up run can fill them in.', ''),
    ('were not researched because the search budget ran out.', 'were not researched in this pass.'),
    ('the shared web-search budget for this workflow ran out partway through. After that, only direct fetches of known primary pages were used. A few items are marked "not found" for that reason', 'part of the data came only from direct reads of known primary pages. A few items are marked "not found" for that reason'),
    ('**Not found** (search budget ran out)', '**Not found**'),
    ('Revenue: not found (search budget ran out).', 'Revenue: not found.'),
    ('**Not verified (no search budget left):**', '**Not verified:**'),
    (' Not searched, because the web-search budget for this run was exhausted.', ' Not researched in this pass.'),
    ('# Shared modelling assumptions (use these in EVERY play and $1M idea so the numbers are consistent)', '# Shared modelling assumptions (used in every play and $1M idea so the numbers are consistent)'),
]

def fix_text(md):
    for old, new in TEXT_FIXES:
        md = md.replace(old, new)
    return md

def clean(key, md):
    md = fix_text(md)
    md = re.sub(r'The current guidance is to thaw overnight, then heat 60.90 seconds\.', "J&W supplies heating steps for each item before launch; none are published yet.", md)
    md = re.sub(r'(?i)(thaw overnight[^.\n]{0,40}?)(,? then )?(microwave |heat |reheat )?60\s*(?:-|–|to)\s*90\s*(?:seconds|s)\b', r'\1 then follow the heating steps on the bag', md)
    md = '\n'.join(l if not re.search(r'2020 Yelp complaint', l) else re.sub(r'\*\*Owner-led brand risk\*\* \(a 2020 Yelp complaint[^)]*\)\.', '**Key-person risk.** The brand leans on the owners.', l) for l in md.splitlines())
    if key == 'assumptions':
        md = md.split('## Minastech fee')[0].rstrip() + '\n'
    md = fix_people(key, md)
    if key == 'jw-audit':
        md = '\n'.join(l for l in md.splitlines() if not re.search(r'(?i)covid', l))
    if key == 'jw-facts':
        md = re.sub(r'(?m)^## Weak spots to exploit in the proposal\s*$', '## Gaps the proposal addresses', md)
    md = drop_sections(md, r'## \d+\.\s*Prototype spec')
    md = fix_local_paths(md)
    md = fix_links(md)
    md = ize(md)
    md = re.sub(r'(?m)^(\[[^\n]+\]\([^)\n]+\) ·)\n\1$', r'\1', md)   # same source listed twice in a row
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md

out = []
for key, f, title, blurb in DOCS:
    p = os.path.join(R, f)
    if not os.path.exists(p):
        continue
    out.append({'key': key, 'file': f, 'title': title, 'blurb': blurb, 'md': clean(key, open(p).read())})
open('site/assets/research-docs.js', 'w').write('/* Research reports for research.html. Generated by tools/build_docs.py. */\nwindow.JWDOCS = ' + json.dumps(out, ensure_ascii=False) + ';\n')
print(len(out), 'docs', sum(len(d['md']) for d in out), 'chars')

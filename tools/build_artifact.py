# Builds artifact/ : the copy of site/ that is published as a claude.ai Artifact.
# Differences from the Netlify build (dist/):
#  - product photos are downloaded and published alongside the pages (the Artifact CSP blocks hotlinked images)
#  - index.html becomes the artifact's main page: no doctype/html/head/body tags of its own (the viewer adds them)
#  - print buttons are removed (printing is disabled inside an artifact)
# Usage: python3 tools/build_artifact.py   -> prints the files map used for publishing
import os, re, shutil, json, hashlib, urllib.request

ROOT = '/Users/erwingarcia/Claude/JWFOODSPROPOSAL'
SRC, OUT = f'{ROOT}/site', f'{ROOT}/artifact'
SKIP = {'_check.html', 'FRAMEWORK.md', 'robots.txt', 'favicon.ico', '.DS_Store'}

shutil.rmtree(OUT, ignore_errors=True)
for dp, dn, fn in os.walk(SRC):
    rel = os.path.relpath(dp, SRC)
    for f in fn:
        if f in SKIP or f.startswith('00-') or f.startswith('_b'):
            continue
        os.makedirs(os.path.join(OUT, rel), exist_ok=True)
        shutil.copy2(os.path.join(dp, f), os.path.join(OUT, rel, f))

# 1) localise every cdn.shopify.com image
URL = re.compile(r'https://cdn\.shopify\.com/[^"\'\s)\\]+')
texts = [os.path.join(dp, f) for dp, dn, fn in os.walk(OUT) for f in fn if f.endswith(('.html', '.js', '.css'))]
bases = {}
for p in texts:
    for u in URL.findall(open(p, encoding='utf-8').read()):
        bases.setdefault(u.split('?')[0], set()).add(u)
os.makedirs(f'{OUT}/assets/products', exist_ok=True)
local = {}
for base in sorted(bases):
    ext = os.path.splitext(base)[1].lower()
    ext = ext if ext in ('.jpg', '.jpeg', '.png', '.webp', '.gif') else '.jpg'
    name = re.sub(r'[^a-z0-9]+', '-', os.path.splitext(os.path.basename(base))[0].lower()).strip('-')[:48] + '-' + hashlib.md5(base.encode()).hexdigest()[:6] + ext
    dest = f'{OUT}/assets/products/{name}'
    cache = f'{ROOT}/research/img-cache/{name}'
    if not os.path.exists(cache):
        os.makedirs(os.path.dirname(cache), exist_ok=True)
        req = urllib.request.Request(base + '?width=600', headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as r, open(cache, 'wb') as fh:
            fh.write(r.read())
    shutil.copy2(cache, dest)
    local[base] = name
def rewrite(p):
    s = open(p, encoding='utf-8').read()
    in_root_page = os.path.dirname(p) == OUT and p.endswith('.html')
    prefix = 'assets/products/' if in_root_page else '../assets/products/'   # catalog.js and prototypes run in prototypes/
    s2 = URL.sub(lambda m: prefix + local[m.group(0).split('?')[0]], s)
    if s2 != s:
        open(p, 'w', encoding='utf-8').write(s2)
for p in texts:
    rewrite(p)

# 1b) research reports: the artifact carries the 8 core reports; the per-play and deep-dive working files stay local
CORE_DOCS = {'jw-facts', 'jw-audit', 'gta-mealprep', 'gta-meat', 'global', 'market', 'ai', 'assumptions'}
rd = f'{OUT}/assets/research-docs.js'
raw = open(rd, encoding='utf-8').read()
docs = json.loads(raw[raw.index('['):raw.rindex(']') + 1])
docs = [d for d in docs if d['key'] in CORE_DOCS]
open(rd, 'w', encoding='utf-8').write('/* Core research reports for research.html (artifact copy). */\nwindow.JWDOCS = ' + json.dumps(docs, ensure_ascii=False) + ';\n')
open(f'{ROOT}/research/artifact-docs.md', 'w', encoding='utf-8').write('\n\n'.join('=== ' + d['file'] + '\n' + d['md'] for d in docs))

# 2) the main page: drop the document wrapper, keep head content and body classes
p = f'{OUT}/index.html'
s = open(p, encoding='utf-8').read()
s = re.sub(r'<!doctype html>\s*', '', s, flags=re.I)
s = re.sub(r'<html[^>]*>\s*', '', s, flags=re.I).replace('</html>', '')
s = re.sub(r'<head>\s*', '', s, flags=re.I).replace('</head>', '')
s = re.sub(r'<meta charset="utf-8">\s*', '', s, flags=re.I)
s = re.sub(r'<meta name="viewport"[^>]*>\s*', '', s, flags=re.I)
m = re.search(r'<body class="([^"]*)">', s)
s = s.replace(m.group(0), '<div class="' + m.group(1) + '">').replace('</body>', '</div>')
s = s.replace('<style>', '<style>\n    body { background: #F6F7F9; color: #0F1B2D; margin: 0; }', 1)
s = s.replace(' Prints cleanly to PDF.', '')
open(p, 'w', encoding='utf-8').write(s)

# 3) no print buttons
p = f'{OUT}/proposal.html'
s = open(p, encoding='utf-8').read()
s = re.sub(r'\s*<button type="button" onclick="window\.print\(\)"[^>]*>Save as PDF</button>', '', s)
s = re.sub(r'\s*<p class="no-print mt-10"><button type="button" onclick="window\.print\(\)"[^>]*>Save this proposal as a PDF</button></p>', '', s)
open(p, 'w', encoding='utf-8').write(s)

files = {}
for dp, dn, fn in os.walk(OUT):
    for f in fn:
        rel = os.path.relpath(os.path.join(dp, f), OUT)
        if rel != 'index.html':
            files[rel] = os.path.join(dp, f)
left = sum(len(URL.findall(open(t, encoding='utf-8').read())) for t in texts)
size = sum(os.path.getsize(v) for v in files.values()) + os.path.getsize(f'{OUT}/index.html')
print(json.dumps({'images': len(local), 'shopifyUrlsLeft': left, 'files': len(files), 'bytes': size,
                  'printLeft': open(f'{OUT}/proposal.html').read().count('window.print') + open(f'{OUT}/index.html').read().count('window.print')}))
json.dump(files, open(f'{ROOT}/research/artifact-files.json', 'w'), indent=1)

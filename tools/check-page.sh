#!/bin/zsh
# Headless phone (390) + desktop (1280) layout audit of a non-prototype page via _check.html. Usage: tools/check-page.sh index.html
PAGE=$1
PROF=$(mktemp -d /private/tmp/claude-501/-Users-erwingarcia-Claude-JWFOODSPROPOSAL/7f9cea33-ca57-4f08-a5f5-40df3c313a82/scratchpad/cp.XXXX)
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for W in 390 1280; do
  "$CHROME" --headless=new --disable-gpu --user-data-dir=$PROF/p$W --enable-logging=stderr --v=0 --window-size=$((W+40)),900 --virtual-time-budget=9000 --dump-dom "http://localhost:8787/_check.html?audit=1&w=$W&h=900&src=/$PAGE" >/dev/null 2>$PROF/log$W
  echo "== $PAGE @ $W"; grep CONSOLE $PROF/log$W | sed -E 's/^.*CONSOLE[^]]*\] //' | grep -i -E 'PAGE-CHECK|error|uncaught|not defined|cannot read' | head -12
done
rm -rf $PROF

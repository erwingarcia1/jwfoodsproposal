#!/bin/zsh
# Headless check of one page: JS errors + layout/a11y self-check at phone (390, via iframe) and desktop (1280) widths.
# Usage: tools/check.sh prototypes/03-butcher-club.html   (local server must be running on :8787)
PAGE=$1
PROF=$(mktemp -d /private/tmp/claude-501/-Users-erwingarcia-Claude-JWFOODSPROPOSAL/7f9cea33-ca57-4f08-a5f5-40df3c313a82/scratchpad/chk.XXXX)
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
for W in 390 1280; do
  for V in customer team; do
    LOG=$PROF/log-$W-$V.txt
    if [[ $W == 390 ]]; then URL="http://localhost:8787/_check.html?w=390&src=/$PAGE%3Fcheck%3D1%26view%3D$V"; WS=900,1000; else URL="http://localhost:8787/$PAGE?check=1&view=$V"; WS=1280,900; fi
    "$CHROME" --headless=new --disable-gpu --user-data-dir=$PROF/p-$W-$V --enable-logging=stderr --v=0 --window-size=$WS --virtual-time-budget=8000 --dump-dom "$URL" >/dev/null 2>$LOG
    echo "== width $W, $V view"
    grep -E "CONSOLE" $LOG | sed -E 's/^.*CONSOLE[^]]*\] //' | grep -i -E 'JWC-CHECK|error|uncaught|failed|not defined|undefined|cannot read' | head -20
  done
done
rm -rf $PROF

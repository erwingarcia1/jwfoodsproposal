#!/bin/zsh
# Screenshots every prototype for the hub cards: phone (390x1120 @2x -> 780x2240 cropped to 780x1120) and wide (1440x900).
# Usage: tools/shoot.sh [NN]   (needs the local server on :8787)
set -e
ROOT=/Users/erwingarcia/Claude/JWFOODSPROPOSAL
OUT=$ROOT/site/assets/shots
PROF=$(mktemp -d /private/tmp/claude-501/-Users-erwingarcia-Claude-JWFOODSPROPOSAL/7f9cea33-ca57-4f08-a5f5-40df3c313a82/scratchpad/shot.XXXX)
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
mkdir -p $OUT
for f in $ROOT/site/prototypes/[0-9][0-9]-*.html; do
  b=$(basename $f .html); nn=${b[1,2]}
  [[ -n "$1" && "$1" != "$nn" ]] && continue
  [[ "$nn" == "00" ]] && continue
  # headless Chrome will not go below ~500px wide, so render the phone view in a 390px iframe and crop to it
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --user-data-dir=$PROF --force-device-scale-factor=2 --window-size=520,560 --virtual-time-budget=${BUDGET:-9000} --screenshot=$OUT/$nn-phone.png "http://localhost:8787/_check.html?w=390&h=560&src=/prototypes/$b.html%3Fshot%3D1" >/dev/null 2>&1
  sips -c 1120 780 $OUT/$nn-phone.png >/dev/null   # centred crop; the iframe is centred in _check.html
  "$CHROME" --headless=new --disable-gpu --hide-scrollbars --user-data-dir=$PROF --force-device-scale-factor=1 --window-size=1440,900 --virtual-time-budget=${BUDGET:-8000} --screenshot=$OUT/$nn-wide.png "http://localhost:8787/prototypes/$b.html?shot=1" >/dev/null 2>&1
  sips -s format jpeg -s formatOptions 82 $OUT/$nn-phone.png --out $OUT/$nn-phone.jpg >/dev/null
  sips -s format jpeg -s formatOptions 80 $OUT/$nn-wide.png --out $OUT/$nn-wide.jpg >/dev/null
  rm -f $OUT/$nn-phone.png $OUT/$nn-wide.png
  echo "shot $nn"
done
rm -rf $PROF

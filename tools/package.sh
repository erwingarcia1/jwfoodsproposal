#!/bin/zsh
# Packages site/ into dist/ (deploy-ready static site) and JWFoods-proposal.zip (for Netlify Drop or any static host).
set -e
ROOT=/Users/erwingarcia/Claude/JWFOODSPROPOSAL
rm -rf $ROOT/dist && mkdir -p $ROOT/dist
rsync -a --exclude '00-test.html' --exclude '_check.html' --exclude 'FRAMEWORK.md' --exclude '.DS_Store' $ROOT/site/ $ROOT/dist/
printf 'User-agent: *\nDisallow: /\n' > $ROOT/dist/robots.txt
cd $ROOT/dist && rm -f $ROOT/JWFoods-proposal.zip && zip -qr $ROOT/JWFoods-proposal.zip . && cd $ROOT
du -sh dist JWFoods-proposal.zip
find dist -type f | wc -l

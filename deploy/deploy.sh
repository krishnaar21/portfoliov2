#!/usr/bin/env bash
# Deploy krishnaar.work from a cloud session (needs CLOUDFLARE_API_TOKEN and api.cloudflare.com allowed).
# Same worker, KV and custom domains as outputs/portfolio-cloudflare/deploy.command on Krishna's Mac.
set -euo pipefail
P=/mnt/project-files/portfolio
OUT=${1:-$(mktemp -d)}
mkdir -p "$OUT/images"
cp "$P/site/index.html" "$P/site/resume.html" "$OUT/"
cp "$P/site/images/"* "$OUT/images/"
cp "$P/cloudflare/_worker.js" "$P/cloudflare/_headers" "$P/deploy/wrangler.jsonc" "$OUT/"
printf '%s\n' _worker.js wrangler.jsonc .assetsignore .wrangler node_modules .dev.vars > "$OUT/.assetsignore"
cd "$OUT"
# every image the page references must be there
grep -o 'images/[A-Za-z0-9_.-]*' index.html | sort -u | while read f; do [ -f "$f" ] || { echo "missing $f"; exit 1; }; done
npx -y wrangler@4 deploy

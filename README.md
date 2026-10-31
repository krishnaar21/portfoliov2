# krishnaar.work (portfolio v2)

Source for [krishnaar.work](https://krishnaar.work), Krishna AR's design portfolio.

- `site/` is the deployable site: a single-page `index.html`, `resume.html` and `images/`.
- `cloudflare/` and `deploy/` hold the Cloudflare Worker (`krishnaar`) that serves it, and the deploy script.
- `build/` holds the scripts that inject case studies and card thumbnails into `site/index.html`.

Secrets (`CLOUDFLARE_API_TOKEN`, `LOVES_PASS`, `RESEND_API_KEY`) live in the hosting environment, never in this repo.

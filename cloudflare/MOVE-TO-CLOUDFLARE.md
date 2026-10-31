# Move krishnaar.work to Cloudflare Pages

Upload `outputs/portfolio-cloudflare` (or `portfolio-cloudflare.zip`) on your Mac. It is the same site as `portfolio-final`, plus two files:
- `_worker.js` runs the private loves counts and the contact form. It replaces the Netlify function and Netlify Forms.
- `_headers` keeps images cached for a year, like before.

## 1. Create the project (about 2 min)
1. Go to dash.cloudflare.com, then **Workers & Pages → Create → Pages → Upload assets**.
2. Name it `krishnaar` and drag in the **portfolio-cloudflare** folder (or the zip). Click **Deploy**.
3. You get a `krishnaar.pages.dev` link, and the site already works there. Hearts and contact start working after step 2.

## 2. Storage and passphrase
1. Go to **Storage & Databases → KV → Create**, and name it `portfolio-loves`.
2. In the Pages project, go to **Settings → Bindings → Add → KV namespace**. Set the variable name to `LOVES` and pick `portfolio-loves`.
3. Go to **Settings → Variables and Secrets → Add**. Set the type to *Secret* and the name to `LOVES_PASS`. For the value, enter the passphrase you'll use for `?loves`.
4. Bindings only apply to new deployments, so go to **Deployments → Create deployment** and drag the folder in again.

## 3. Contact form email (recommended)
Messages are always saved, but they only reach your inbox once this is set up:
1. Make a free account at resend.com **with the email you want messages sent to**, then create an API key.
2. Add two more secrets: `RESEND_API_KEY` = the key, and `CONTACT_TO` = that email.
3. Redeploy as in 2.4.

## 4. Check on krishnaar.pages.dev
- Tap a heart in Archived work, then open `/?loves`, enter the passphrase, and confirm the count shows.
- Send yourself a message through Contact.

## 5. Switch the domain
1. In the Pages project, go to **Custom domains → Set up a domain** and enter `krishnaar.work` (and `www.krishnaar.work` if you use it).
2. Cloudflare will ask you to move the domain's nameservers to Cloudflare. A bare domain like krishnaar.work needs this. Change them at your registrar. It's usually live within an hour.
3. After that, you can stop or delete the Netlify site.

Notes
- Loves stored on Netlify don't carry over, so counts restart at 0.
- Future updates: **Deployments → Create deployment** and drag the folder in. There's no credit limit.
- If the upload ever says it can't run `_worker.js`, tell me and I'll give you a one-line `npx wrangler pages deploy` instead.

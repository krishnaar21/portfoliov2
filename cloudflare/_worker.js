// Cloudflare Pages (advanced mode) for krishnaar.work: serves the static site and replaces the two Netlify-only pieces.
//   POST /api/loves {k, v, d}           k = design key (a01..), v = random visitor id, d = 1 love / -1 unlove
//   GET  /api/loves   header x-pass     -> {"a01": 3, ...}  (Krishna's private ?loves view)
//   POST /  form-name=contact           contact form (was Netlify Forms): saved to KV, emailed through Resend when set up
//   GET  /api/messages header x-pass    -> saved contact messages, newest first
// Bindings (Pages > Settings > Bindings / Variables): KV namespace LOVES; secrets LOVES_PASS, and optionally
// RESEND_API_KEY + CONTACT_TO for email. Each love is its own key "<design>/<visitor>" so two visitors never overwrite each other.
const json = (b, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { "content-type": "application/json", "cache-control": "no-store" } });
const sha = async t => new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(t)));
const owner = async (req, env) => {
  if (!env.LOVES_PASS) return false;
  const a = await sha(req.headers.get("x-pass") || ""), b = await sha(env.LOVES_PASS);
  let d = 0; for (let i = 0; i < a.length; i++) d |= a[i] ^ b[i];
  return d === 0;
};
const listAll = async (kv, prefix) => {
  const keys = []; let cursor;
  do { const r = await kv.list({ prefix, cursor }); keys.push(...r.keys); cursor = r.list_complete ? null : r.cursor } while (cursor);
  return keys;
};
const esc = s => String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

async function loves(req, env) {
  if (!env.LOVES) return json({ error: "storage not set up" }, 503);
  if (req.method === "POST") {
    let b; try { b = await req.json() } catch { return json({ error: "bad json" }, 400) }
    const { k, v, d } = b || {};
    if (!/^a\d{1,3}$/.test(k) || !/^[a-z0-9]{12,40}$/.test(v) || (d !== 1 && d !== -1)) return json({ error: "bad input" }, 400);
    if (d === 1) await env.LOVES.put(`${k}/${v}`, "1"); else await env.LOVES.delete(`${k}/${v}`);
    return json({ ok: true });
  }
  if (req.method === "GET") {
    if (!(await owner(req, env))) return json({ error: "nope" }, 401);
    const n = {};
    for (const { name } of await listAll(env.LOVES, "a")) { const k = name.split("/")[0]; n[k] = (n[k] || 0) + 1 }
    return json(n);
  }
  return json({ error: "method" }, 405);
}

async function contact(req, env) {
  const f = await req.formData();
  if (f.get("bot-field")) return new Response("ok");
  const m = { name: String(f.get("name") || "").slice(0, 200), email: String(f.get("email") || "").slice(0, 200),
    subject: String(f.get("subject") || "").slice(0, 300), message: String(f.get("message") || "").slice(0, 5000), at: new Date().toISOString() };
  if (!m.message.trim() || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(m.email)) return new Response("missing fields", { status: 400 });
  if (env.LOVES) await env.LOVES.put(`msg/${m.at}`, JSON.stringify(m));
  if (env.RESEND_API_KEY && env.CONTACT_TO) {
    const r = await fetch("https://api.resend.com/emails", { method: "POST", headers: { authorization: `Bearer ${env.RESEND_API_KEY}`, "content-type": "application/json" },
      body: JSON.stringify({ from: env.CONTACT_FROM || "krishnaar.work <onboarding@resend.dev>", to: [env.CONTACT_TO], reply_to: m.email,
        subject: `Portfolio: ${m.subject || "new message"} (from ${m.name || m.email})`,
        html: `<p><b>${esc(m.name)}</b> &lt;${esc(m.email)}&gt;</p><p><b>${esc(m.subject)}</b></p><p style="white-space:pre-wrap">${esc(m.message)}</p>` }) });
    if (!r.ok) console.log("resend failed", r.status, await r.text());
    if (!r.ok && !env.LOVES) return new Response("could not send", { status: 502 });
  } else if (!env.LOVES) return new Response("contact not set up", { status: 503 });
  return new Response("ok");
}

async function messages(req, env) {
  if (!(await owner(req, env))) return json({ error: "nope" }, 401);
  const keys = (await listAll(env.LOVES, "msg/")).map(k => k.name).sort().reverse().slice(0, 100);
  return json(await Promise.all(keys.map(async k => JSON.parse(await env.LOVES.get(k)))));
}

export default {
  async fetch(req, env) {
    const u = new URL(req.url);
    if (u.pathname === "/api/loves") return loves(req, env);
    if (u.pathname === "/api/messages") return messages(req, env);
    if (req.method === "POST" && u.pathname === "/") {
      const ct = req.headers.get("content-type") || "";
      if (ct.includes("form")) return contact(req, env);
    }
    return env.ASSETS.fetch(req);
  }
};

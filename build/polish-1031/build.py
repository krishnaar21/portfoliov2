# Site polish 2026-10-31 (Krishna): the sticky top bar's background (.crumb ::before, inset 0 -22px) covered the page's
# dotted side rails (.wrap ::before/::after, 4px inside .wrap). Now the bar background stops 1px inside each rail.
# JS measures each crumb against .wrap and sets --rl/--rr. Idempotent. Usage: python3 build.py in.html [out.html]
import sys,re
src=sys.argv[1]; dst=sys.argv[2] if len(sys.argv)>2 else src
s=open(src).read()
s=re.sub(r'<style id="rails-css">.*?</style><script id="rails-js">.*?</script>','',s,flags=re.S)
css='.crumb:has(.cur.pj)::before,.crumb.stk::before{left:calc(-1*var(--rl,22px));right:calc(-1*var(--rr,22px))}'
js=('(()=>{const f=()=>{const w=document.querySelector(".wrap");if(!w)return;const r=w.getBoundingClientRect();'
    'document.querySelectorAll(".crumb").forEach(c=>{const b=c.getBoundingClientRect();'
    'c.style.setProperty("--rl",Math.max(0,b.left-(r.left+5))+"px");c.style.setProperty("--rr",Math.max(0,(r.right-5)-b.right)+"px")})};'
    'const g=()=>{f();setTimeout(f,60);setTimeout(f,400)};addEventListener("load",g);addEventListener("resize",f);addEventListener("hashchange",g);'
    'new MutationObserver(()=>requestAnimationFrame(f)).observe(document.documentElement,{childList:true,subtree:true});g()})()')
s=s.replace('</body>',f'<style id="rails-css">{css}</style><script id="rails-js">{js}</script></body>',1) if '</body>' in s else s+f'<style id="rails-css">{css}</style><script id="rails-js">{js}</script>'
open(dst,'w').write(s); print('ok',dst)

# Halftone Earth in Siri colours (Krishna 2026-11-03): replaces the ⌘ logo (.cmk: home hero + profile
# header) with a turning halftone globe whose dots flow in pink/violet/blue/cyan + the site's --ac yellow.
# Writes images/earth-siri.webp next to the page (pass --inline to embed it as a data URI instead).
# Idempotent. Usage: python3 build.py site/index.html [out.html] [--inline]
import sys,re,os,shutil,base64
a=[x for x in sys.argv[1:] if not x.startswith('--')]; inline='--inline' in sys.argv
src=a[0]; dst=a[1] if len(a)>1 else src
d=os.path.dirname(os.path.abspath(__file__))
css=open(os.path.join(d,'globe.css')).read().strip().replace('\n','')
js=open(os.path.join(d,'globe.js')).read().strip()
if inline: url='data:image/webp;base64,'+base64.b64encode(open(os.path.join(d,'earth.webp'),'rb').read()).decode()
else:
    im=os.path.join(os.path.dirname(os.path.abspath(dst)),'images'); os.makedirs(im,exist_ok=True)
    shutil.copyfile(os.path.join(d,'earth.webp'),os.path.join(im,'earth-siri.webp')); url='images/earth-siri.webp'
mount=('(()=>{const m=k=>{if(k.dataset.sg)return;k.dataset.sg=1;const c=document.createElement("canvas");c.className="sgc";'
 'c.setAttribute("aria-hidden","true");k.appendChild(c);k.classList.add("sgon");sgGlobe(c,{src:'+repr(url).replace("'",'"')+',cells:44})};'
 'const s=()=>document.querySelectorAll(".cmk:not([data-sg])").forEach(m);'
 'new MutationObserver(s).observe(document.documentElement,{childList:true,subtree:true});s()})()')
assert '</script' not in js
s=open(src).read()
s=re.sub(r'<style id="sg-css">.*?</style><script id="sg-js">.*?</script>','',s,flags=re.S)
blk=f'<style id="sg-css">{css}</style><script id="sg-js">{js}\n{mount}</script>'
s=s.replace('</body>',blk+'</body>',1) if '</body>' in s else s+blk
open(dst,'w').write(s); print('ok',dst,'inline' if inline else url)

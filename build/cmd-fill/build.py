# ⌘ logo animated fill (Krishna 2026-11-03, ref: a Pinterest "silk" gradient video).
# The hero/About .cmk logo becomes a bold ⌘ (CSS mask) filled by a small WebGL shader:
# an orange and a violet glow split by a sharp S-curve seam, slowly turning. Footer logo unchanged.
# Idempotent. Usage: python3 build.py in.html [out.html]
import sys,re,os
src=sys.argv[1]; dst=sys.argv[2] if len(sys.argv)>2 else src
d=os.path.dirname(os.path.abspath(__file__))
css=open(os.path.join(d,'cmd.css')).read().strip().replace('\n','')
js=open(os.path.join(d,'cmd.js')).read().strip()
assert '</script' not in js and '</style' not in css
s=open(src).read()
s=re.sub(r'<style id="cmf-css">.*?</style><script id="cmf-js">.*?</script>','',s,flags=re.S)
blk=f'<style id="cmf-css">{css}</style><script id="cmf-js">{js}</script>'
s=s.replace('</body>',blk+'</body>',1) if '</body>' in s else s+blk
open(dst,'w').write(s); print('ok',dst)

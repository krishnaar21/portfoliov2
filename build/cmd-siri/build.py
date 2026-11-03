# ⌘ logo in Siri colours (Krishna 2026-11-03): the hero/profile .cmk ⌘ gets a flowing pink/violet/blue/cyan
# + site-yellow fill with a soft glow. Footer ⌘ unchanged. Replaces the earlier cmd-fill / siri-globe ideas
# (apply only one). Idempotent. Usage: python3 build.py site/index.html [out.html]
import sys,re,os
src=sys.argv[1]; dst=sys.argv[2] if len(sys.argv)>2 else src
d=os.path.dirname(os.path.abspath(__file__))
css=open(os.path.join(d,'cmd-siri.css')).read().strip().replace('\n','')
js=open(os.path.join(d,'cmd-siri.js')).read().strip()
assert '</script' not in js and '</style' not in css
s=open(src).read()
s=re.sub(r'<style id="cs-css">.*?</style><script id="cs-js">.*?</script>','',s,flags=re.S)
blk=f'<style id="cs-css">{css}</style><script id="cs-js">{js}</script>'
s=s.replace('</body>',blk+'</body>',1) if '</body>' in s else s+blk
open(dst,'w').write(s); print('ok',dst)

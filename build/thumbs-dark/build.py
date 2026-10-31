# Injects dark-mode card thumbnails into a built index.html (idempotent). Usage: python3 build.py in.html [out.html]
# Cards with an entry in TD get class "tdk" and two CSS vars; dark theme shows --d, light shows --l. Missing/null = same image both themes.
import sys,re,json
TL={"bookjoy":["images/bookjoy-thumb1-l.webp","images/bookjoy-thumb2-l.webp"]}  # light thumbnail overrides
src=sys.argv[1]; dst=sys.argv[2] if len(sys.argv)>2 else src
TD={"shellf":["images/shellf-thumb1-d.webp","images/shellf-thumb2-d.webp"],
 "interview-cracker":["images/ic-thumb1-d.svg","images/ic-thumb2-d.svg"],
 "trugen-ai":["images/tg-thumb1-d.svg","images/tg-thumb2-d.svg"],
 "tirimiri":[None,"images/tirimiri-thumb2-d.webp"],
 "nclex100":["images/nclex100-thumb1-d.webp",None],
 "xnprotel":["images/xnprotel-thumb1-d.webp","images/xnprotel-thumb2-d.webp"],
 "bookjoy":["images/bookjoy-thumb1-d.webp","images/bookjoy-thumb2-d.webp"]}
s=open(src).read()
s=re.sub(r'<style id="td-css">.*?</style><script id="td-js">.*?</script>','',s,flags=re.S)
OLD='const e=t=>`<div class="pst" style="${A.th?`background:url(${A.th[t]}) center/cover`:M}"></div>`'
NEW='const e=t=>{const d=(window.TD||{})[A.id],k=d&&d[t],o=(window.TL||{})[A.id],l=o&&o[t]||A.th&&A.th[t];return`<div class="pst${k?" tdk":""}" style="${A.th?(k?`--l:url(${l});--d:url(${k})`:`background:url(${l}) center/cover`):M}"></div>`}'
OLD2='const e=t=>{const d=(window.TD||{})[A.id],k=d&&d[t];return`<div class="pst${k?" tdk":""}" style="${A.th?(k?`--l:url(${A.th[t]});--d:url(${k})`:`background:url(${A.th[t]}) center/cover`):M}"></div>`}'
if OLD in s: s=s.replace(OLD,NEW,1)
elif OLD2 in s: s=s.replace(OLD2,NEW,1)
elif NEW not in s: raise SystemExit('renderer not found')
inj=('<style id="td-css">.pst.tdk{background:var(--l) center/cover}:root[data-theme=dark] .pst.tdk{background-image:var(--d)}</style>'
     f'<script id="td-js">window.TD={json.dumps(TD,separators=(",",":"))};window.TL={json.dumps(TL,separators=(",",":"))}</script>')
s=s.replace('</head>',inj+'</head>',1)
open(dst,'w').write(s); print('ok',dst)

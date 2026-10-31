# Dark-mode card thumbnails for every project (Krishna 2026-10-31). Reuses each project's own thumbnail generator
# (source exec'd without its render/save tail), swaps the palette, renders to site/images/<id>-thumbN-d.webp|svg.
# Principle: same composition, deep tinted background of the project hue; small cards stay light, big sheets go dark.
import os,re,subprocess,sys
from PIL import Image
P=os.path.abspath(os.path.join(os.path.dirname(__file__),'..')); OUT=f'{P}/site/images'; TMP='/tmp/claude-0/tdark'; os.makedirs(TMP,exist_ok=True)
def rep(s,pairs):
    for a,b in pairs:
        if a not in s: raise SystemExit(f'missing: {a[:60]}')
        s=s.replace(a,b)
    return s
def load(path,cut,subs=()):
    src=open(path).read(); src=src[:src.index(cut)]
    for a,b in subs: src=src.replace(a,b)
    ns={'__file__':path}; cwd=os.getcwd(); os.chdir(os.path.dirname(path))
    exec(compile(src,path,'exec'),ns); return ns  # stays in the project dir so its relative image paths work
jobs=[]  # (outname, html_or_svg_text, kind)
# ---- Shellf ----
sf=load(f'{P}/shellf/thumbs/make.py','for n,h in')
jobs.append(('shellf-thumb1-d',rep(sf['t1'](),[('#eceef2,#dfe3ea','#1e2129,#14161c'),('rgba(40,48,64,.16)','rgba(255,255,255,.06)'),('background:rgba(40,44,58,','background:rgba(255,255,255,'),('background:#3a3b40','background:#5b5d64')]),'html'))
jobs.append(('shellf-thumb2-d',rep(sf['t2'](),[('#e9edf4,#dce3ee','#1a1f2a,#12161e'),('rgba(40,60,110,.16)','rgba(255,255,255,.06)'),('rgba(255,255,255,.45)','rgba(255,255,255,.06)'),('rgba(255,255,255,.7)','rgba(255,255,255,.12)'),
  ('background:#fff;box-shadow:0 28px','background:#20252f;box-shadow:0 0 0 1px rgba(255,255,255,.06),0 28px'),('#f3f4f6','#2b313c'),('color:inherit','color:#1a1a1a'),('#111827','#eef1f6'),('#eef0f3','#2c323d'),('#64748b','#8f9bb0')]),'html'))
# ---- Interview Cracker (SVG) ----
ic=load(f'{P}/interview-cracker/thumbs/make.py','for n,s in')
jobs.append(('ic-thumb1-d',rep(ic['t1'],[('#f9e3ec','#2a1520'),('#f1cddd','#1c0e15'),('rx="16" fill="#fff"','rx="16" fill="#1e1a1d"'),('fill="#fff" stroke="#efe5ea"','fill="#26212a" stroke="#3a3036"'),('#fbf7f9','#231e22'),('#efe7eb','#332a30'),('#e9dfe4','#3a3036'),
  ('#fbe6ef','#4a2234'),('#26201f','#f1e9ec'),('#8f8689','#a2969b'),('#fdf1f6','#33202a'),('#f3d3e1','#4d2a3a'),('#5b3a49','#e7c8d5'),('#eee7ea','#2f282c'),('#e7dfe3','#3a3236'),('#e3f2e9','#1f3a2b'),('#c2457a','#e0679a')]),'svg'))
jobs.append(('ic-thumb2-d',rep(ic['t2'],[('stop-color="#8c8698"','stop-color="#3b3545"'),('stop-color="#6c6679"/>','stop-color="#26212e"/>'),('stop-color="#6c6679" stop-opacity="0"','stop-color="#26212e" stop-opacity="0"'),('#635d70','#211d28'),('fill="#e9e5ee" stroke="#f6f3f8"','fill="#3d3647" stroke="#4b4357"'),('#26201f','#f3edf0'),('#8f8689','#b5abb0'),('#d6cedb','#4f475a'),('#fdecef','#4a2433'),('#e3f2e9','#1f3a2b')]),'svg'))
# ---- TruGen AI (SVG) ----
tg=load(f'{P}/trugen/thumbs/make2.py','for n,s in')
jobs.append(('tg-thumb1-d',rep(tg['t1'],[('#e6f4ed','#12251d'),('#d3ebdf','#0b1813'),('rx="18" fill="#fff"','rx="18" fill="#161c1a"'),('#f7faf8','#1b2220'),('#e6ece9','#27302c'),('#dfe7e3','#2c3531'),('#e3f2ea','#183a2c'),('#1f2623','#eef3f1'),
  ('#7f8a86','#93a19b'),('#5d6763','#a9b5b0'),('#e3ebe7','#2a332f'),('#eef2f0','#242c29'),('#11795a','#5fd3a8')]),'svg'))
jobs.append(('tg-thumb2-d',rep(tg['t2'],[('fill="#e9eeec"','fill="#141a18"')]),'svg'))
# ---- NCLEX100: thumb1 (peach form) only; thumb2 is already dark ----
nc=load(f'{P}/nclex100/thumbs.py',"open('thumbs/thumb-1.svg'")
jobs.append(('nclex100-thumb1-d',rep(nc['form'](),[('fill="#f4bb9b"/>','fill="#3a2219"/>'),('stop-color="#f8d7c5"','stop-color="#5a3424"'),('stop-color="#f4bb9b"','stop-color="#3a2219"'),('fill-opacity=".28" stroke="#ffffff" stroke-opacity=".7"','fill-opacity=".07" stroke="#ffffff" stroke-opacity=".2"'),
  ('fill-opacity=".22" stroke="#ffffff" stroke-opacity=".6"','fill-opacity=".05" stroke="#ffffff" stroke-opacity=".14"'),('font-size="46" fill="#2f2833"','font-size="46" fill="#fbe9df"')]),'svg'))
# ---- XNProtel ----
xn=load(f'{P}/xnprotel/hero/thumbs.py',"open('thumb-1.svg'")
jobs.append(('xnprotel-thumb1-d',rep(xn['thumb_device'](),[('#ecf8f1','#12281e'),('#cdebd9','#0a1912'),('fill="#ffffff" fill-opacity=".45"','fill="#ffffff" fill-opacity=".04"'),('fill="#2f9e6c" fill-opacity=".14"','fill="#6cc79a" fill-opacity=".12"')]),'svg'))
jobs.append(('xnprotel-thumb2-d',rep(xn['thumb_widget'](),[('#efe9fb','#241c36'),('#d8cdf2','#151022'),('fill="#7a4ea6" fill-opacity=".12"','fill="#c4a6ec" fill-opacity=".1"'),('fill="#ffffff" fill-opacity=".45"','fill="#ffffff" fill-opacity=".05"'),('fill="#ffffff" fill-opacity=".75"','fill="#ffffff" fill-opacity=".1"'),('fill="#2a1f45" text-anchor','fill="#ece6fb" text-anchor')]),'svg'))
# ---- BookJoy: new pair (Krishna 18:34 picked A1 + C2) comes from bookjoy/thumbs/options.py, copied as bookjoy-thumbN-l/-d.webp ----
# ---- Tirimiri: thumb1 is already deep purple; thumb2 coral goes deep wine ----
tm=load(f'{P}/tirimiri/thumbs/make.py','for k,h in',[("data:font/ttf;base64,{b64(f'{T}/fonts/Poppins-{w}.ttf')}","data:font/woff;base64,{b64(f'/tmp/claude-0/fonts/fontsource-poppins/files/poppins-latin-{w}-normal.woff')}"),("av=img64('chats',300)","av=''")])
jobs.append(('tirimiri-thumb2-d',rep(tm['widget'](),[('#f19a8d 0%,#e07a6d 62%','#6a2f30 0%,#3e1c22 62%'),('rgba(224,122,109,0),rgba(224,122,109,.85) 55%,#e07a6d 80%','rgba(62,28,34,0),rgba(62,28,34,.85) 55%,#3e1c22 80%')]),'html'))
only=sys.argv[1:]
todo=[j for j in jobs if not only or any(o in j[0] for o in only)]
shots=[]
for n,t,k in todo:
    if n.startswith(('ic-','tg-')) and k=='svg': open(f'{OUT}/{n}.svg','w').write(t); continue
    f=f'{TMP}/{n}.'+('svg' if k=='svg' else 'html'); open(f,'w').write(t if k=='svg' or t.startswith('<!doctype') else '<!doctype html><meta charset=utf-8>'+t); shots.append((n,f))
if shots:
    js="const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:744}});for(const [n,f] of "+repr([[n,f] for n,f in shots])+"){await p.goto('file://'+f);await p.waitForTimeout(500);await p.screenshot({path:'"+TMP+"/'+n+'.png'})}await b.close()})()"
    subprocess.run(['node','-e',js],check=True,cwd='/tmp')
    for n,_ in shots: Image.open(f'{TMP}/{n}.png').convert('RGB').save(f'{OUT}/{n}.webp','WEBP',quality=86,method=6)
print('wrote',[j[0] for j in todo])

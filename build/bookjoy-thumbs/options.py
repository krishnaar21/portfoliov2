# BookJoy card thumbnail OPTIONS (Krishna 2026-10-31): 3 concepts x 2 thumbs x light/dark -> opt/<c><n>-<l|d>.webp
# A = drawn day calendar with a drag-to-reschedule moment + type poster; B = real screens close up; C = appointment ticket + one booking, many services.
import base64,os,subprocess
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__)); F=os.path.join(D,'../fonts'); S=os.path.join(D,'../s'); O=os.path.join(D,'opt')
b64=lambda p:base64.b64encode(open(p,'rb').read()).decode()
ff=''.join(f"@font-face{{font-family:P;font-weight:{w};src:url(data:font/woff2;base64,{b64(f'{F}/poppins-latin-{w}-normal.woff2')})}}" for w in (400,500,600))
ff+=''.join(f"@font-face{{font-family:S;font-weight:{w};src:url(data:font/woff2;base64,{b64(f'{F}/fraunces-latin-{w}-normal.woff2')})}}" for w in (500,600))
IMG=lambda p,m='png':f"data:image/{m};base64,{b64(p)}"
R,BL,GR='#fb6672','#0084f4','#10a377'
TH={'l':dict(bgA='linear-gradient(160deg,#ffd9dc,#fbbcc2)',bgC='linear-gradient(160deg,#dcecfe,#b9d8fb)',c2card='#ffffff',c2line='rgba(0,90,180,.12)',c2ink='#24324a',c2mute='#5d6b85',bg='#fbf4f1',bg2='#eef5fd',bg3='#fdf6f1',card='#ffffff',ink='#24324a',mute='#7b8496',line='#ece7e4',soft='#f6f1ee',post=R,postink='#ffffff',postmute='rgba(255,255,255,.82)',sh='rgba(80,30,30,.16)'),
    'd':dict(bgA='linear-gradient(160deg,#5a2029,#38141b)',bgC='linear-gradient(160deg,#173a66,#0e2442)',c2card='#1c3457',c2line='rgba(255,255,255,.1)',c2ink='#eef4ff',c2mute='#9fb3d1',bg='#1c1719',bg2='#121a24',bg3='#1d1820',card='#262024',ink='#f3eef0',mute='#a59ca2',line='#352d31',soft='#2e272b',post='#3a1f25',postink='#ffe4e7',postmute='rgba(255,228,231,.75)',sh='rgba(0,0,0,.45)')}
def base(t): return f'<!doctype html><meta charset=utf-8><style>{ff}*{{box-sizing:border-box;margin:0}}body{{width:1200px;height:744px;overflow:hidden;font-family:P;color:{t["ink"]}}}.c{{position:relative;width:1200px;height:744px;overflow:hidden}}</style>'
def ic(d,c,s=28,w=2.2): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{d}</svg>'
CAL='<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M8 3v4M16 3v4M3 10h18"/>'
CHK='<path d="M5 12.5l4.5 4.5L19 7.5"/>'
CLK='<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'
# ---------- A1: drawn day calendar ----------
def A1(t,k):
  M=72; cols=[('Lucy',R),('Jennie',BL),('Francisco',GR)]; cw=300; x0=M+130; top=M+150; rh=92
  o=f'{base(t)}<div class="c" style="background:{t["bgA"]}"><div style="position:absolute;left:{M}px;top:{M}px;width:1300px;height:900px;border-radius:28px;background:{t["card"]};box-shadow:0 30px 60px -30px {t["sh"]}">'
  o+=f'<div style="position:absolute;left:40px;top:34px;display:flex;align-items:center;gap:14px">{ic(CAL,R,30)}<b style="font-size:30px;font-weight:600">Mon, 16 Mar</b><span style="font-size:20px;color:{t["mute"]};margin-left:8px">Brisbane Lashes · 3 stylists</span></div>'
  for i,(n,c) in enumerate(cols):
    x=130+i*cw; o+=f'<div style="position:absolute;left:{x+16}px;top:98px;display:flex;align-items:center;gap:12px"><span style="width:38px;height:38px;border-radius:50%;background:{c};color:#fff;font-size:17px;font-weight:600;display:flex;align-items:center;justify-content:center">{n[0]}</span><span style="font-size:20px;font-weight:500">{n}</span></div>'
  for r,tm in enumerate(['9:00','10:00','11:00','12:00','1:00']):
    y=150+r*rh; o+=f'<div style="position:absolute;left:40px;top:{y-12}px;font-size:18px;color:{t["mute"]}">{tm}</div><div style="position:absolute;left:120px;right:0;top:{y}px;height:1.5px;background:{t["line"]}"></div>'
  for i in range(4): o+=f'<div style="position:absolute;left:{130+i*cw-6}px;top:146px;bottom:0;width:1.5px;background:{t["line"]}"></div>'
  def blk(ci,r0,h,title,sub,c,extra=''):
    x=130+ci*cw+8; y=150+r0*rh+6
    tint=c+('1f' if k=='l' else '33')
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{cw-28}px;height:{h*rh-12}px;border-radius:14px;background:{tint};border-left:5px solid {c};padding:14px 18px;{extra}"><div style="font-size:20px;font-weight:600">{title}</div><div style="font-size:16px;color:{t["mute"]};margin-top:4px">{sub}</div></div>'
  o+=blk(0,0,1.5,'Lash Lift','Rebecca · 9:00',R)+blk(1,0.5,1,'Brow Tint','Vivian · 9:30',BL)+blk(2,0,2,'Classic Full Set','Danielle · 9:00',GR)+blk(0,2,1,'Lash Fill','Amy · 11:00',R)+blk(2,2.5,1,'Facial','Christian · 11:30',GR)
  # drag-to-reschedule: dashed old slot + lifted block
  o+=f'<div style="position:absolute;left:{130+cw+8}px;top:{150+2*rh+6}px;width:{cw-28}px;height:{rh-12}px;border-radius:14px;border:2.5px dashed {BL};opacity:.7"></div>'
  o+=blk(1,1.75,1,'Eyebrow Tint','Rebecca · moved to 10:45',BL,f'background:{t["card"]};box-shadow:0 24px 40px -14px {t["sh"]},0 0 0 2px {BL};transform:rotate(-2deg) translate(10px,6px);z-index:2')
  return o+'</div></div>'
# ---------- A2: type poster ----------
def A2(t,k):
  o=f'{base(t)}<div class="c" style="background:{t["post"]};color:{t["postink"]}">'
  o+=f'<div style="position:absolute;left:84px;top:96px;font-family:S;font-weight:600;font-size:118px;line-height:.98;letter-spacing:-3px">Book.<br>Move.<br>Paid.</div>'
  o+=f'<div style="position:absolute;left:720px;top:110px;width:1.5px;height:520px;background:{t["postmute"]};opacity:.5"></div>'
  o+=f'<div style="position:absolute;left:780px;top:118px"><div style="font-size:140px;font-weight:600;letter-spacing:-5px;line-height:1">35%</div><div style="font-size:26px;line-height:1.35;color:{t["postmute"]};margin-top:14px">fewer clicks per screen<br>in the beta</div></div>'
  o+=f'<img src="{IMG(D+"/word_white.png")}" style="position:absolute;left:784px;bottom:96px;height:54px;opacity:.95">'
  return o+'</div>'
# ---------- B: real screens close up ----------
def shot(path,box,scale,t,k,bg):
  im=Image.open(path).convert('RGB').crop(box); w,h=im.size; p=f'/tmp/claude-0/bjo_{os.path.basename(path)}_{box[0]}.png'; im.save(p)
  M=72
  return (f'{base(t)}<div class="c" style="background:{bg}"><div style="position:absolute;left:{M}px;top:{M}px;width:{w*scale:.0f}px;height:{h*scale:.0f}px;border-radius:22px;overflow:hidden;box-shadow:0 0 0 1px {t["line"]},0 30px 60px -28px {t["sh"]}">'
          f'<img src="{IMG(p)}" style="width:100%;height:100%;display:block"></div></div>')
def B1(t,k): return shot(f'{S}/cal_new.webp',(260,140,1440,790),1.08,t,k,t['bg'])
def B2(t,k): return shot(f'{S}/nb_sum.webp',(560,40,1440,899),1.36,t,k,t['bg2'])
# ---------- C1: appointment ticket (outline follows the notch arcs) ----------
def C1(t,k):
  x,y,w,h,stub,r,n=150,170,900,404,250,30,26
  sx=x+stub
  path=(f'M{x+r} {y}H{sx-n}A{n} {n} 0 0 0 {sx+n} {y}H{x+w-r}A{r} {r} 0 0 1 {x+w} {y+r}V{y+h-r}A{r} {r} 0 0 1 {x+w-r} {y+h}'
        f'H{sx+n}A{n} {n} 0 0 0 {sx-n} {y+h}H{x+r}A{r} {r} 0 0 1 {x} {y+h-r}V{y+r}A{r} {r} 0 0 1 {x+r} {y}Z')
  o=f'{base(t)}<div class="c" style="background:{t["bg2"]}"><svg width="1200" height="744" style="position:absolute;left:0;top:0"><defs><filter id="s" x="-10%" y="-10%" width="120%" height="140%"><feDropShadow dx="0" dy="24" stdDeviation="24" flood-color="{"#0b2a4a" if k=="l" else "#000"}" flood-opacity="{.16 if k=="l" else .5}"/></filter></defs>'
  o+=f'<path d="{path}" fill="{t["card"]}" stroke="{t["line"]}" stroke-width="2" filter="url(#s)"/><path d="M{sx} {y+n+14}V{y+h-n-14}" stroke="{t["line"]}" stroke-width="3" stroke-dasharray="2 12" stroke-linecap="round"/></svg>'
  o+=f'<div style="position:absolute;left:{x}px;top:{y}px;width:{stub}px;height:{h}px;display:flex;flex-direction:column;align-items:center;justify-content:center"><div style="font-size:24px;font-weight:600;color:{R};letter-spacing:3px">MAR</div><div style="font-family:S;font-weight:600;font-size:120px;line-height:1">16</div><div style="font-size:24px;color:{t["mute"]}">Monday</div></div>'
  cx=sx+64
  o+=f'<div style="position:absolute;left:{cx}px;top:{y+58}px"><span style="display:inline-flex;align-items:center;gap:8px;padding:9px 20px 9px 14px;border-radius:30px;background:#3fd09a;color:#0b0b0b;font-size:20px;font-weight:600">{ic(CHK,"#0b0b0b",22,2.8)}Confirmed</span>'
  o+=f'<div style="font-family:S;font-weight:600;font-size:66px;letter-spacing:-1.5px;margin-top:26px">Lash Lift</div>'
  o+=f'<div style="display:flex;gap:34px;margin-top:22px;font-size:23px;color:{t["mute"]}"><span style="display:flex;align-items:center;gap:10px">{ic(CLK,t["mute"],24)}10:30 – 11:30 AM</span><span>with Lucy</span></div>'
  o+=f'<div style="margin-top:40px;height:2px;width:{w-stub-128}px;background:{t["line"]}"></div><div style="display:flex;justify-content:space-between;width:{w-stub-128}px;margin-top:22px;font-size:22px"><span style="color:{t["mute"]}">Rebecca Taylor</span><b style="font-weight:600">$60</b></div></div>'
  return o+'</div>'
# ---------- C2: one booking, many services ----------
def C2(t,k):
  rows=[('Eyebrow Tint','30 min',R,'11:30'),('Textured Hybrid Full Set','2 hr',BL,'12:00'),('Lash Serum','Product',GR,'2:00')]
  x,y0,w,h,g=250,150,760,120,26
  o=f'{base(t)}<div class="c" style="background:{t["bgC"]};color:{t["c2ink"]}">'
  o+=f'<div style="position:absolute;left:150px;top:{y0+10}px;width:44px;height:{3*h+2*g-20}px;border:3px solid {t["c2ink"]};border-right:0;border-radius:22px 0 0 22px;opacity:.85"></div>'
  o+=f'<div style="position:absolute;left:58px;top:{y0+(3*h+2*g)//2-20}px;transform:rotate(-90deg);transform-origin:center;width:220px;margin-left:-110px;left:116px;text-align:center;font-size:19px;font-weight:600;letter-spacing:2px;color:{t["c2mute"]}">ONE BOOKING</div>'
  for i,(n,d,c,tm) in enumerate(rows):
    y=y0+i*(h+g)
    o+=f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:24px;background:{t["c2card"]};box-shadow:0 0 0 1.5px {t["c2line"]};display:flex;align-items:center;padding:0 34px;gap:26px">'
    o+=f'<span style="width:16px;height:16px;border-radius:50%;background:{c};flex:none"></span><span style="font-size:22px;color:{t["c2mute"]};width:74px">{tm}</span><span style="flex:1;font-family:S;font-weight:600;font-size:36px;letter-spacing:-.5px">{n}</span><span style="font-size:22px;color:{t["c2mute"]}">{d}</span></div>'
  y=y0+3*(h+g)+8
  o+=f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;display:flex;justify-content:space-between;align-items:center;padding:0 34px"><span style="font-size:22px;color:{t["c2mute"]}">Thursday, 16 March</span><span style="font-size:30px;font-weight:600">Total $100</span></div>'
  return o+'</div>'
jobs=[]
for k,t in TH.items():
  for n,f in (('A1',A1),('A2',A2),('B1',B1),('B2',B2),('C1',C1),('C2',C2)):
    p=f'/tmp/claude-0/bjo_{n}-{k}.html'; open(p,'w').write(f(t,k)); jobs.append((f'{n}-{k}',p))
js="const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:744}});for(const [n,f] of "+repr([list(j) for j in jobs])+"){await p.goto('file://'+f);await p.waitForTimeout(400);await p.screenshot({path:'/tmp/claude-0/bjo_'+n+'.png'})}await b.close()})()"
subprocess.run(['node','-e',js],check=True,cwd='/tmp')
os.makedirs(O,exist_ok=True)
for n,_ in jobs: Image.open(f'/tmp/claude-0/bjo_{n}.png').convert('RGB').save(f'{O}/{n}.webp','WEBP',quality=86,method=6)
print('ok',len(jobs))

# TruGen AI card thumbnails v2 (Krishna 10-31 18:11): real trugen.ai avatars embedded as base64 webp.
# thumb1 = builder panel (left = top margin), Start a call fully visible; thumb2 = live call tile with floating setup chips.
import os,io,base64
from PIL import Image
H=os.path.dirname(os.path.abspath(__file__))
D=os.path.join(H,'..','..','site','images')
HERO=os.path.join(H,'..','web','lisa.jpg')   # 1000x1080 crop of trugen.ai hero.avif
F='font-family="Inter,-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif"'
G='#11795a';GF='#3fcf98';INK='#0b0b0b'
def b64(im,w,h,q=80):
    sw,sh=im.size;r=w/h
    if sw/sh>r: nw=int(sh*r);im=im.crop(((sw-nw)//2,0,(sw-nw)//2+nw,sh))
    else: nh=int(sw/r);im=im.crop((0,0,sw,nh))
    im=im.convert('RGB').resize((w,h),Image.LANCZOS);b=io.BytesIO();im.save(b,'WEBP',quality=q,method=6)
    return 'data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
av=lambda n:Image.open(os.path.join(D,f'tg-av-{n}.webp'))
tick=lambda x,y,s=1:f'<path d="M{x-4*s} {y}l{3*s} {3*s} {6*s}-{6*s}" stroke="{INK}" stroke-width="{2.2*s}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
shadow='<filter id="s" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#0f4d3a" flood-opacity=".18"/></filter>'
# ---------- thumb 1 ---------- (Work card shows thumbs at ~1.61:1, so viewBox 600x372)
W,HH=600,372; M=36; SB=84; X=M+SB+22; RIGHT=W-M
cw=(RIGHT-X-24)//3; ch=124; cy=M+74
cs=''
for i,(n,k) in enumerate([('Lisa','lisa'),('Priya','priya'),('Aman','aman')]):
    x=X+i*(cw+12);on=i==0
    cs+=(f'<clipPath id="a{i}"><rect x="{x}" y="{cy}" width="{cw}" height="{ch}" rx="12"/></clipPath>'
         f'<image href="{b64(av(k),cw*2,ch*2)}" x="{x}" y="{cy}" width="{cw}" height="{ch}" preserveAspectRatio="xMidYMid slice" clip-path="url(#a{i})"/>'
         +(f'<rect x="{x-3}" y="{cy-3}" width="{cw+6}" height="{ch+6}" rx="14" fill="none" stroke="{GF}" stroke-width="3"/>'
           f'<circle cx="{x+cw-14}" cy="{cy+14}" r="11" fill="{GF}"/>{tick(x+cw-14,cy+13,.9)}' if on else
           f'<rect x="{x}" y="{cy}" width="{cw}" height="{ch}" rx="12" fill="none" stroke="#e3ebe7"/>')
         +f'<text x="{x+2}" y="{cy+ch+22}" font-size="13" font-weight="{600 if on else 500}" fill="{G if on else "#5d6763"}">{n}</text>')
fy=cy+ch+40  # footer top
nav=''.join(f'<rect x="{M+18}" y="{M+70+i*28}" width="{w}" height="8" rx="4" fill="#dfe7e3"/>' for i,w in enumerate([46,38,52,42,34]))
wave=''.join(f'<rect x="{X+92+i*5}" y="{fy+28-h/2}" width="2.6" height="{h}" rx="1.3" fill="{G}" opacity="{.35+.65*(h/16)}"/>' for i,h in enumerate([4,8,13,7,16,10,6,12,14,7,5,9,12,6,4,7,10,6,4,3]))
bx=RIGHT-128
t1=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {HH}" {F}>
<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e6f4ed"/><stop offset="1" stop-color="#d3ebdf"/></linearGradient>{shadow}</defs>
<rect width="{W}" height="{HH}" fill="url(#g)"/>
<g filter="url(#s)"><rect x="{M}" y="{M}" width="{W}" height="{HH}" rx="18" fill="#fff"/></g>
<path d="M{M+18} {M}h{SB-18}v{HH}h-{SB}v-{HH-18}a18 18 0 0 1 18-18z" fill="#f7faf8"/><line x1="{M+SB}" y1="{M}" x2="{M+SB}" y2="{HH}" stroke="#e6ece9"/>
<rect x="{M+18}" y="{M+18}" width="26" height="26" rx="8" fill="{GF}"/>{tick(M+31,M+30)}
{nav}<rect x="{M+10}" y="{M+87}" width="64" height="24" rx="8" fill="#e3f2ea"/><rect x="{M+18}" y="{M+95}" width="40" height="8" rx="4" fill="{G}"/>
<text x="{X}" y="{M+34}" font-size="19" font-weight="600" fill="#1f2623">Agent setup</text>
<text x="{X}" y="{M+55}" font-size="12.5" fill="#7f8a86">Avatar · Choose how your teammate looks</text>
{cs}
<line x1="{X}" y1="{fy}" x2="{RIGHT}" y2="{fy}" stroke="#eef2f0"/>
<circle cx="{X+12}" cy="{fy+28}" r="12" fill="#e3f2ea"/><path d="M{X+7} {fy+28}v0M{X+10} {fy+24}v8M{X+13.5} {fy+21}v14M{X+17} {fy+25.5}v5" stroke="{G}" stroke-width="1.9" stroke-linecap="round"/>
<text x="{X+32}" y="{fy+25}" font-size="12.5" font-weight="600" fill="#1f2623">Voice</text><text x="{X+32}" y="{fy+40}" font-size="11.5" fill="#7f8a86">Warm</text>{wave}
<rect x="{bx}" y="{fy+9}" width="128" height="38" rx="19" fill="{GF}"/>
<rect x="{bx+16}" y="{fy+22}" width="13" height="12" rx="3" fill="none" stroke="{INK}" stroke-width="1.8"/><path d="M{bx+29} {fy+26.5}l5-3v9l-5-3z" fill="{INK}"/>
<text x="{bx+42}" y="{fy+33}" font-size="13" font-weight="600" fill="{INK}">Start a call</text>
</svg>'''
# ---------- thumb 2 ---------- v3 (Krishna 18:18): no floating chips, light like thumb1. A call-style roster grid of real trugen.ai avatars.
SRC=os.path.join(H,'src')
ppl=[('Lisa','lisa'),('Priya','priya'),('Aman','aman'),('Chloe','chole'),('Matt','matt'),('Sameer','sameer')]
P2,GP=24,12; tw2=(600-2*P2-2*GP)/3; th2=(372-2*P2-GP)/2
tiles=''
for i,(n,k) in enumerate(ppl):
    x=P2+(i%3)*(tw2+GP); y=P2+(i//3)*(th2+GP); on=i==0
    im=Image.open(os.path.join(SRC,k+'.jpg'))
    if k=='lisa': im=im.crop((380,0,1540,1080))
    tiles+=(f'<clipPath id="t{i}"><rect x="{x:.1f}" y="{y:.1f}" width="{tw2:.1f}" height="{th2:.1f}" rx="14"/></clipPath>'
            f'<image href="{b64(im,int(tw2*2),int(th2*2),78)}" x="{x:.1f}" y="{y:.1f}" width="{tw2:.1f}" height="{th2:.1f}" preserveAspectRatio="xMidYMid slice" clip-path="url(#t{i})"/>'
            f'<rect x="{x+10:.1f}" y="{y+th2-34:.1f}" width="{len(n)*7.4+(52 if on else 22):.1f}" height="24" rx="12" fill="#000" fill-opacity=".5"/>'
            +(''.join(f'<rect x="{x+20+j*4.5:.1f}" y="{y+th2-22-h/2:.1f}" width="2.6" height="{h}" rx="1.3" fill="{GF}"/>' for j,h in enumerate([5,10,7,12,6]))
              +f'<text x="{x+50:.1f}" y="{y+th2-17.5:.1f}" font-size="12" font-weight="600" fill="#fff">{n}</text>'
              +f'<rect x="{x-3:.1f}" y="{y-3:.1f}" width="{tw2+6:.1f}" height="{th2+6:.1f}" rx="17" fill="none" stroke="{GF}" stroke-width="3"/>' if on else
              f'<text x="{x+21:.1f}" y="{y+th2-17.5:.1f}" font-size="12" font-weight="500" fill="#fff">{n}</text>'))
t2=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 372" {F}>
<rect width="600" height="372" fill="#e9eeec"/>
{tiles}
</svg>'''
for n,s in (('tg-thumb1.svg',t1),('tg-thumb2.svg',t2)):
    open(os.path.join(D,n),'w').write(s);print(n,len(s)//1024,'KB')

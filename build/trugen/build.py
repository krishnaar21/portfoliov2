#!/usr/bin/env python3
"""Inject the TruGen AI case study into the portfolio page.
Usage: python3 build.py [in.html] [out.html]   (defaults: ../site/index.html in place)
Idempotent: removes an earlier injection first. The card goes right before Tirimiri,
so with Interview Cracker injected the Work page reads Shellf, Interview Cracker, TruGen AI, Tirimiri."""
import os,re,sys
H=os.path.dirname(os.path.abspath(__file__))
src=sys.argv[1] if len(sys.argv)>1 else os.path.join(H,'..','site','index.html')
dst=sys.argv[2] if len(sys.argv)>2 else src
s=open(src,encoding='utf-8').read()
css=open(os.path.join(H,'tg.css'),encoding='utf-8').read()
js=open(os.path.join(H,'tg.js'),encoding='utf-8').read()
s=re.sub(r'<style id="tg-css">.*?</style>','',s,flags=re.S)
s=re.sub(r'<script id="tg-js">.*?</script>','',s,flags=re.S)
s=re.sub(r'\{id:"trugen-ai".*?secs:\[\]\},','',s,flags=re.S)
assert '</head>' in s and '<script>const NSI=' in s and s.count('{id:"tirimiri"')==1, 'anchor missing'
s=s.replace('</head>',f'<style id="tg-css">{css}</style></head>',1)
s=s.replace('<script>const NSI=',f'<script id="tg-js">{js}</script><script>const NSI=',1)
card='{id:"trugen-ai",tag:"AI platform · Product and website",title:"TruGen AI",date:"2026",c:"#11795a,#14261f",blurb:"Building an AI teammate, without assembling an AI stack.",role:"Product Designer",tools:"Figma, Web",th:["images/tg-thumb1.svg","images/tg-thumb2.svg"],cs:TG,stats:[],secs:[]},'
s=s.replace('{id:"tirimiri"',card+'{id:"tirimiri"',1)
open(dst,'w',encoding='utf-8').write(s)
print('wrote',dst,len(s))

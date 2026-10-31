#!/usr/bin/env python3
"""Inject the Interview Cracker case study into the portfolio page.
Usage: python3 build.py [in.html] [out.html]   (defaults: ../site/index.html in place)
Idempotent: removes an earlier injection first."""
import os,re,sys
H=os.path.dirname(os.path.abspath(__file__))
src=sys.argv[1] if len(sys.argv)>1 else os.path.join(H,'..','site','index.html')
dst=sys.argv[2] if len(sys.argv)>2 else src
s=open(src,encoding='utf-8').read()
css=open(os.path.join(H,'ic.css'),encoding='utf-8').read()
js=open(os.path.join(H,'ic.js'),encoding='utf-8').read()
# remove previous injection
s=re.sub(r'<style id="ic-css">.*?</style>','',s,flags=re.S)
s=re.sub(r'<script id="ic-js">.*?</script>','',s,flags=re.S)
s=re.sub(r'\{id:"interview-cracker".*?secs:\[\]\},','',s,flags=re.S)
assert '</head>' in s and '<script>const NSI=' in s and s.count('o=[')==1, 'anchor missing'
s=s.replace('</head>',f'<style id="ic-css">{css}</style></head>',1)
s=s.replace('<script>const NSI=',f'<script id="ic-js">{js}</script><script>const NSI=',1)
card='{id:"interview-cracker",tag:"Internal product · AI interview platform",title:"Interview Cracker",date:"2026",c:"#c2457a,#2a1420",blurb:"One workspace for the work around an interview, from resume to placement.",role:"Product Designer",tools:"Figma, Web",th:["images/ic-thumb1.svg","images/ic-thumb2.svg"],cs:IC,stats:[],secs:[]},'
s=s.replace('o=[','o=['+card,1)
open(dst,'w',encoding='utf-8').write(s)
print('wrote',dst,len(s))

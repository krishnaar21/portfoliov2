# 2026-10-31 (Krishna, via TruGen thread): thumb2 cards are solid soft lilac-white #e9e5ee (not pure white, not transparent: Krishna rejected see-through). Dark version: portfolio/thumbs-dark/make.py
# Placeholder card thumbnails for Interview Cracker (until real visuals arrive). Writes SVGs to ../../site/images/
import os
D=os.path.join(os.path.dirname(__file__),'..','..','site','images')
F='font-family="Inter,-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif"'
t1=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 504" {F}>
<defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f9e3ec"/><stop offset="1" stop-color="#f1cddd"/></linearGradient>
<filter id="s" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="14" stdDeviation="16" flood-color="#7a2a4f" flood-opacity=".18"/></filter></defs>
<rect width="600" height="504" fill="url(#g)"/>
<g filter="url(#s)"><rect x="70" y="92" width="560" height="380" rx="16" fill="#fff"/></g>
<rect x="70" y="92" width="96" height="380" rx="16" fill="#fbf7f9"/><rect x="150" y="92" width="16" height="380" fill="#fbf7f9"/>
<line x1="166" y1="92" x2="166" y2="472" stroke="#efe7eb"/>
<rect x="90" y="116" width="28" height="28" rx="8" fill="#c2457a"/>
<g fill="#e9dfe4"><rect x="90" y="170" width="56" height="9" rx="4.5"/><rect x="90" y="226" width="50" height="9" rx="4.5"/><rect x="90" y="254" width="58" height="9" rx="4.5"/><rect x="90" y="282" width="44" height="9" rx="4.5"/></g>
<rect x="82" y="190" width="72" height="26" rx="8" fill="#fbe6ef"/><rect x="90" y="199" width="48" height="9" rx="4.5" fill="#c2457a"/>
<text x="190" y="140" font-size="20" font-weight="600" fill="#26201f">Interviews</text>
<text x="190" y="164" font-size="13" fill="#8f8689">Pick a way to start</text>
<g font-size="14" font-weight="600" fill="#26201f">
<rect x="190" y="186" width="128" height="104" rx="12" fill="#fff" stroke="#efe5ea"/><circle cx="214" cy="212" r="12" fill="#fbe6ef"/><circle cx="214" cy="212" r="4.5" fill="#c2457a"/><text x="204" y="262">Live</text><text x="204" y="279" font-size="12" font-weight="400" fill="#8f8689">interview</text>
<rect x="330" y="186" width="128" height="104" rx="12" fill="#fff" stroke="#efe5ea"/><rect x="342" y="202" width="24" height="22" rx="5" fill="none" stroke="#c2457a" stroke-width="2"/><text x="344" y="262">Schedule</text><text x="344" y="279" font-size="12" font-weight="400" fill="#8f8689">a session</text>
<rect x="470" y="186" width="128" height="104" rx="12" fill="#fff" stroke="#efe5ea"/><rect x="486" y="200" width="14" height="24" rx="4" fill="none" stroke="#c2457a" stroke-width="2"/><text x="484" y="262">Phone</text><text x="484" y="279" font-size="12" font-weight="400" fill="#8f8689">interview</text></g>
<rect x="190" y="306" width="408" height="44" rx="10" fill="#fdf1f6" stroke="#f3d3e1"/><circle cx="210" cy="328" r="5" fill="#2f8a57"/><text x="224" y="333" font-size="13" fill="#5b3a49">“Python Developer” is in progress</text><rect x="520" y="316" width="66" height="24" rx="12" fill="#c2457a"/><text x="553" y="332" font-size="11.5" font-weight="600" fill="#fff" text-anchor="middle">Return</text>
<g fill="#eee7ea"><rect x="190" y="372" width="408" height="1"/><rect x="190" y="402" width="408" height="1"/><rect x="190" y="432" width="408" height="1"/></g>
<g fill="#e7dfe3"><rect x="190" y="384" width="120" height="8" rx="4"/><rect x="190" y="414" width="96" height="8" rx="4"/><rect x="190" y="444" width="110" height="8" rx="4"/></g>
<g><rect x="530" y="381" width="56" height="15" rx="7.5" fill="#e3f2e9"/><rect x="530" y="411" width="56" height="15" rx="7.5" fill="#fbe6ef"/><rect x="530" y="441" width="56" height="15" rx="7.5" fill="#e3f2e9"/></g>
</svg>'''
t2=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 504" {F}>
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8c8698"/><stop offset="1" stop-color="#6c6679"/></linearGradient>
<filter id="s" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="16" stdDeviation="18" flood-color="#2a2433" flood-opacity=".28"/></filter>
<linearGradient id="f" x1="0" y1="0" x2="0" y2="1"><stop offset=".6" stop-color="#6c6679" stop-opacity="0"/><stop offset="1" stop-color="#635d70" stop-opacity=".95"/></linearGradient></defs>
<rect width="600" height="504" fill="url(#g)"/>

<g transform="translate(36,56) scale(.88)"><g filter="url(#s)"><rect x="70" y="58" width="300" height="300" rx="18" fill="#e9e5ee" stroke="#f6f3f8" stroke-width="1.5"/></g>
<rect x="88" y="78" width="54" height="22" rx="11" fill="#fdecef"/><circle cx="101" cy="89" r="4" fill="#e5484d"/><text x="110" y="93.5" font-size="11" font-weight="700" fill="#c2457a" font-family="ui-monospace,Menlo,monospace">LIVE</text>
<text x="88" y="132" font-size="11.5" fill="#a39a9e" font-family="ui-monospace,Menlo,monospace">AI-GENERATED RESPONSE</text>
<text x="88" y="160" font-size="17" font-weight="600" fill="#26201f">Tell me about a project</text>
<text x="88" y="181" font-size="17" font-weight="600" fill="#26201f">you’re proud of.</text>
<g fill="#d6cedb"><rect x="88" y="204" width="262" height="8" rx="4"/><rect x="88" y="222" width="240" height="8" rx="4"/><rect x="88" y="240" width="252" height="8" rx="4"/><rect x="88" y="258" width="180" height="8" rx="4"/></g>
<rect x="88" y="222" width="120" height="8" rx="4" fill="#f3c6d8"/>
<g transform="translate(88,296)" fill="#c2457a">{''.join(f'<rect x="{i*8}" y="{18-h/2}" width="4" height="{h}" rx="2" opacity="{.45+.5*(h/30)}"/>' for i,h in enumerate([8,14,22,12,28,18,10,24,30,16,8,20,26,12,18,9,22,14,6,16,24,10,18,12,8,14,20,10,6,12,8,4]))}</g>
<g filter="url(#s)"><rect x="330" y="150" width="210" height="96" rx="14" fill="#e9e5ee" stroke="#f6f3f8" stroke-width="1.5"/></g>
<text x="348" y="176" font-size="11" fill="#a39a9e" font-family="ui-monospace,Menlo,monospace">TRANSCRIPT</text>
<text x="348" y="200" font-size="13" fill="#26201f"><tspan font-weight="600">Interviewer:</tspan> Walk me</text>
<text x="348" y="219" font-size="13" fill="#26201f">through your role…</text>
<rect x="348" y="230" width="90" height="6" rx="3" fill="#d6cedb"/>
<g filter="url(#s)"><rect x="372" y="268" width="168" height="54" rx="14" fill="#e9e5ee" stroke="#f6f3f8" stroke-width="1.5"/></g>
<circle cx="396" cy="295" r="10" fill="#e3f2e9"/><circle cx="396" cy="295" r="4" fill="#2f8a57"/>
<text x="414" y="291" font-size="12.5" font-weight="600" fill="#26201f">Connected</text><text x="414" y="308" font-size="11" fill="#8f8689">Meeting room</text></g>
<rect width="600" height="504" fill="url(#f)"/>
<text x="300" y="410" text-anchor="middle" fill="#fff" fill-opacity=".95" font-size="19" font-weight="500" letter-spacing="-.2">Copilot First, Context Alongside</text>
</svg>'''
for n,s in (('ic-thumb1.svg',t1),('ic-thumb2.svg',t2)):
    open(os.path.join(D,n),'w').write(s)
print('ok')

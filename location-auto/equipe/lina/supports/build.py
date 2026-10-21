import base64, io, segno, re, os
D=os.path.dirname(os.path.abspath(__file__)); Y=os.path.join(D,'../../yasmine/final')
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
FONT=''.join(f"@font-face{{font-family:Saira;font-style:italic;font-weight:{w};src:url(data:font/woff2;base64,{b64('/tmp/claude-0/-home-user-golady-landing/8903800a-f2cc-5c52-a993-fc3707ce5853/scratchpad/fonts/s%d.woff2'%w)}) format('woff2')}}" for w in (500,800,900))
def svg(n): return re.sub(r'<\?xml[^>]*>','',open(os.path.join(Y,n)).read())
LOGO_D=svg('haboub-logo-sur-fond-sombre.svg'); LOGO_L=svg('haboub-logo-sur-fond-clair.svg'); ICON=svg('haboub-icone.svg')
def qr(dark,light):
    q=segno.make('https://wa.me/213557190401',error='h'); b=io.BytesIO(); q.save(b,kind='svg',scale=10,border=2,dark=dark,light=light,xmldecl=False,svgns=True)
    return b.getvalue().decode().replace('<svg ','<svg class="qr" ',1)
TEL='0796 96 04 26'; WA='0557 19 04 01'; H='09h – 12h · 14h – 18h'
C=dict(bg='#101317',red='#E3262F',metal='#E9ECEF',ink='#F4F5F7')
BASE=f"""<!doctype html><meta charset=utf8><style>{FONT}
*{{box-sizing:border-box;margin:0;padding:0}}html,body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:Saira,Arial,sans-serif;font-style:italic}}svg{{display:block}}
.qr{{width:100%;height:auto}}
"""
def page(w,h,css,body): return BASE+f"@page{{size:{w}mm {h}mm;margin:0}}.p{{width:{w}mm;height:{h}mm;overflow:hidden;position:relative}}"+css+"</style><body>"+body
cars=[('Renault Clio 5','Techno'),('Renault Clio 5','Evolution'),('Dacia Sandero','')]
# ---------- AFFICHE A3 ----------
rows=''.join(f'<div class="car"><div><b>{a}</b><span>{b}</span></div><div class="pr">12 000 <small>DA / jour</small></div></div>' for a,b in cars)
affiche=page(297,420,f"""
.p{{background:{C['bg']};color:{C['ink']};padding:22mm 20mm;display:flex;flex-direction:column;gap:12mm}}
.logo svg{{width:100%;height:auto}}
.band{{background:{C['red']};color:#fff;font-weight:900;font-size:15mm;padding:4mm 8mm;transform:skewX(-8deg);align-self:flex-start}}
.car{{display:flex;justify-content:space-between;align-items:center;border-bottom:.6mm solid #2a2f37;padding:6mm 0}}
.car b{{display:block;font-weight:900;font-size:13mm;line-height:1}}.car span{{font-weight:500;font-size:7mm;color:#9aa1aa}}
.pr{{font-weight:900;font-size:15mm;color:{C['red']};white-space:nowrap}}.pr small{{font-size:6mm;color:{C['ink']};font-weight:800}}
.inc{{font-weight:500;font-size:6.5mm;color:#c8ccd2}}
.foot{{margin-top:auto;display:grid;grid-template-columns:1fr 62mm;gap:10mm;align-items:center}}
.tel{{font-weight:900;font-size:19mm;line-height:1}}.h{{font-weight:800;font-size:8mm;color:#c8ccd2;margin-top:3mm}}
.qrb{{background:#fff;padding:3mm;border-radius:3mm}}.ql{{font-weight:800;font-size:4.5mm;text-align:center;margin-top:2mm}}
""",f"""<div class="p"><div class="logo">{LOGO_D}</div><div class="band">NOS VOITURES</div><div>{rows}</div>
<div class="inc">Voitures récentes, propres et entretenues · Mazouna et alentours</div>
<div class="foot"><div><div class="tel">{TEL}</div><div class="h">WhatsApp {WA}</div><div class="h">Ouvert {H}</div></div><div><div class="qrb">{qr('#101317','#ffffff')}</div><div class="ql">Scannez · WhatsApp</div></div></div></div>""")
# ---------- FLYER A5 recto / verso ----------
flyer=page(148,210,f"""
.p{{page-break-after:always}}
.r{{background:{C['bg']};color:{C['ink']};padding:12mm 10mm;display:flex;flex-direction:column;gap:6mm}}
.r .logo svg{{width:100%;height:auto}}
.big{{font-weight:900;font-size:13mm;line-height:1.02}}.big em{{color:{C['red']};font-style:italic}}
.from{{display:flex;align-items:baseline;gap:3mm}}.from b{{font-weight:900;font-size:17mm;color:{C['red']}}}.from span{{font-weight:800;font-size:5mm}}
.ic{{position:absolute;right:-22mm;bottom:20mm;width:85mm;opacity:.14}}.ic svg{{width:100%;height:auto}}
.tag{{margin-top:auto;font-weight:900;font-size:9mm}}.tag small{{display:block;font-size:4.5mm;font-weight:500;color:#c8ccd2}}
.v{{background:#fff;color:{C['bg']};padding:12mm 10mm;display:flex;flex-direction:column;gap:5mm}}
.v .logo svg{{width:70%;height:auto}}
.v h2{{font-weight:900;font-size:7mm;background:{C['bg']};color:#fff;padding:2mm 4mm;align-self:flex-start;transform:skewX(-8deg)}}
.car{{display:flex;justify-content:space-between;border-bottom:.4mm solid #e3e5e8;padding:2.6mm 0}}
.car b{{font-weight:900;font-size:5.4mm}}.car span{{font-weight:500;font-size:3.6mm;color:#666;display:block}}
.pr{{font-weight:900;font-size:6mm;color:{C['red']};white-space:nowrap}}.pr small{{font-size:3mm;color:{C['bg']}}}
.foot{{margin-top:auto;display:grid;grid-template-columns:1fr 36mm;gap:5mm;align-items:center}}
.tel{{font-weight:900;font-size:10mm}}.h{{font-weight:800;font-size:4.2mm;color:#444}}.ql{{font-weight:800;font-size:3mm;text-align:center}}
""",f"""<div class="p r"><div class="logo">{LOGO_D}</div><div class="big">Louez votre voiture<br>à <em>Mazouna</em>.</div>
<div class="from"><b>12 000</b><span>DA / jour</span></div><div class="ic">{ICON}</div>
<div class="tag">{TEL}<small>WhatsApp {WA} · {H}</small></div></div>
<div class="p v"><div class="logo">{LOGO_L}</div><h2>NOS VOITURES</h2><div>{rows}</div>
<div style="font-weight:500;font-size:3.8mm;color:#444">Voitures récentes et entretenues. Mazouna, Sidi M'hamed Ben Ali, Aïn Merane, Guettar, Ouarizane, Mediouna.</div>
<div class="foot"><div><div class="tel">{TEL}</div><div class="h">WhatsApp {WA}</div><div class="h">{H}</div></div><div>{qr('#101317','#ffffff')}<div class="ql">WhatsApp</div></div></div></div>""")
# ---------- STICKER VITRINE 60x40 cm ----------
sticker=page(600,400,f"""
.p{{background:{C['bg']};color:{C['ink']};padding:40mm 45mm;display:grid;grid-template-columns:1fr 130mm;gap:30mm;align-items:center}}
.logo svg{{width:100%;height:auto}}
.tel{{font-weight:900;font-size:44mm;margin-top:14mm}}.h{{font-weight:800;font-size:17mm;color:#c8ccd2}}
.qrb{{background:#fff;padding:7mm;border-radius:6mm}}.ql{{font-weight:800;font-size:9mm;text-align:center;margin-top:5mm}}
""",f"""<div class="p"><div><div class="logo">{LOGO_D}</div><div class="tel">{TEL}</div><div class="h">WhatsApp {WA}</div><div class="h">Ouvert {H}</div></div><div><div class="qrb">{qr('#101317','#ffffff')}</div><div class="ql">WhatsApp</div></div></div>""")
for n,h in (('affiche-tarifs-A3',affiche),('flyer-A5-recto-verso',flyer),('sticker-vitrine-60x40',sticker)):
    open(os.path.join(D,n+'.html'),'w').write(h)
print('ok')

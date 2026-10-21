import base64, io, os, segno
D=os.path.dirname(os.path.abspath(__file__)); FL=os.path.join(D,'../../yasmine/flow')
b64=lambda p: base64.b64encode(open(p,'rb').read()).decode()
FONT=''.join(f"@font-face{{font-family:M;font-weight:{w};src:url(data:font/woff2;base64,{b64('/tmp/claude-0/-home-user-golady-landing/8903800a-f2cc-5c52-a993-fc3707ce5853/scratchpad/fonts/m%d.woff2'%w)})}}" for w in (500,700,800,900))
LOGO='data:image/jpeg;base64,'+b64(os.path.join(FL,'haboub-logo-flow-v1.jpg'))
ICON='data:image/jpeg;base64,'+b64(os.path.join(FL,'haboub-icone-flow.jpg'))
def qr():
    b=io.BytesIO(); segno.make('https://wa.me/213557190401',error='h').save(b,kind='svg',scale=10,border=1,dark='#101317',xmldecl=False)
    return b.getvalue().decode().replace('<svg ','<svg style="width:100%;height:auto;display:block" ',1)
TEL='0796 96 04 26'; WA='0557 19 04 01'
cars=[('Renault Clio 5','Techno'),('Renault Clio 5','Evolution'),('Dacia Sandero','')]
rows=''.join(f'<div class="car"><div class="nm"><b>{a}</b><span>{b or "&nbsp;"}</span></div><div class="pr">12 000<small>DA / jour</small></div></div>' for a,b in cars)
html=f"""<!doctype html><meta charset=utf8><style>{FONT}
@page{{size:297mm 420mm;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:M,Arial,sans-serif;color:#F4F5F7}}
.p{{width:297mm;height:420mm;position:relative;overflow:hidden;background:radial-gradient(120% 70% at 50% 0%,#1c2026 0%,#0c0e11 60%,#08090b 100%)}}
.hero{{position:absolute;inset:0 0 auto 0;height:166mm;background:url({LOGO}) center/cover}}
.hero::after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(8,9,11,0) 55%,#0c0e11 100%)}}
.wm{{position:absolute;right:-70mm;top:150mm;width:230mm;height:230mm;background:url({ICON}) center/cover;border-radius:50%;opacity:.10;filter:grayscale(.3)}}
.body{{position:absolute;left:22mm;right:22mm;top:150mm;bottom:22mm;display:flex;flex-direction:column}}
.band{{align-self:flex-start;background:#E3262F;color:#fff;font-weight:900;font-size:13mm;letter-spacing:1mm;padding:3.5mm 9mm;transform:skewX(-12deg);box-shadow:0 2mm 6mm rgba(227,38,47,.35)}}
.band span{{display:inline-block;transform:skewX(12deg)}}
.cars{{margin-top:10mm}}
.car{{display:flex;justify-content:space-between;align-items:center;padding:6.5mm 0;border-bottom:.5mm solid rgba(255,255,255,.12)}}
.nm b{{display:block;font-weight:800;font-size:12mm;line-height:1.05}}.nm span{{font-weight:500;font-size:6mm;color:#9AA1AA;letter-spacing:.5mm}}
.pr{{font-weight:900;font-size:16mm;color:#E3262F;text-align:right;line-height:1}}.pr small{{display:block;font-size:5mm;color:#C8CCD2;font-weight:700;letter-spacing:.8mm;margin-top:1.5mm}}
.inc{{margin-top:7mm;font-weight:500;font-size:6mm;color:#B4BAC2}}
.foot{{margin-top:auto;display:grid;grid-template-columns:1fr 60mm;gap:12mm;align-items:end;border-top:1mm solid #E3262F;padding-top:9mm}}
.lab{{font-weight:700;font-size:5mm;letter-spacing:1mm;color:#9AA1AA}}
.tel{{font-weight:900;font-size:17mm;line-height:1.05;letter-spacing:.5mm}}
.wa{{font-weight:800;font-size:9mm;margin-top:4mm}}.wa i{{font-style:normal;color:#E3262F}}
.h{{font-weight:700;font-size:6.5mm;color:#C8CCD2;margin-top:4mm}}
.qrb{{background:#fff;padding:3.5mm;border-radius:4mm}}.ql{{font-weight:800;font-size:4mm;letter-spacing:.3mm;white-space:nowrap;text-align:center;margin-top:3mm}}
</style><body><div class="p"><div class="hero"></div><div class="wm"></div><div class="body">
<div class="band"><span>NOS VOITURES</span></div><div class="cars">{rows}</div>
<div class="inc">Voitures récentes, propres et entretenues · Mazouna et alentours</div>
<div class="foot"><div><div class="lab">APPELEZ</div><div class="tel">{TEL}</div><div class="wa"><i>WhatsApp</i> {WA}</div><div class="h">Ouvert 09h – 12h · 14h – 18h</div></div>
<div><div class="qrb">{qr()}</div><div class="ql">SCANNEZ · WHATSAPP</div></div></div></div></div>"""
open(os.path.join(D,'affiche-tarifs-A3.html'),'w').write(html); print('ok')

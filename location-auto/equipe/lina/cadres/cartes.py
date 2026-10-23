import base64, os, subprocess, sys
D=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(D,'..','..','..')
F='/tmp/claude-0/-home-user-golady-landing/8903800a-f2cc-5c52-a993-fc3707ce5853/scratchpad/fonts'
b64=lambda p: base64.b64encode(open(p,'rb').read()).decode()
def ff(fam,files): return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};src:url(data:font/woff2;base64,{b64(F+'/'+f)})}}" for w,f in files)
FONT=ff('M',[(500,'m500.woff2'),(700,'m700.woff2'),(800,'m800.woff2'),(900,'m900.woff2')])+ff('C',[(600,'c600.woff2'),(800,'c800.woff2'),(900,'c900.woff2')])
def u(p,t='jpeg'): return f'data:image/{t};base64,'+b64(os.path.join(R,p))
LOGO=u('haboub-logo-kit/3-png-transparent/haboub-logo-couleur-pour-fond-sombre-3000px.png','png')
CARS={
 'sandero':dict(photo='equipe/lina/sandero/photos-flow/sandero-3-4-avant.jpg',brand='DACIA',model='Sandero Stepway',ar='داسيا سانديرو ستيبواي',
   specs=[('2025','2025'),('Finition Extreme','نسخة إكستريم'),('Essence','بنزين'),('5 places','5 بلايص')],price='11 500',accent='#7d8a5a'),
 'clio':dict(photo='equipe/lina/clio/photos-flow/clio-3-4-avant.jpg',brand='RENAULT',model='Clio 5',ar='رونو كليو 5',
   specs=[('2025','2025'),('Finition Techno','نسخة تكنو'),('Essence','بنزين'),('5 places','5 بلايص')],price=None,accent='#2b4f8f'),
}
W,H=606,306
for k,c in CARS.items():
    ph=os.path.join(R,c['photo']); has=os.path.exists(ph)
    bg=f"background:#0b0c0f url({u(c['photo'])}) left center/440mm auto no-repeat" if has else "background:linear-gradient(135deg,#232830,#101216)"
    price=f"<div class='pr'>{c['price']}<small>DA / jour · <i>دج / اليوم</i></small></div>" if c['price'] else "<div class='pr' style='color:#666'>PRIX ?</div>"
    specs=''.join(f"<li><b>{a}</b><span>{b}</span></li>" for a,b in c['specs'])
    html=f"""<!doctype html><meta charset=utf8><style>{FONT}@page{{size:{W}mm {H}mm;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
.p{{width:{W}mm;height:{H}mm;position:relative;overflow:hidden;background:#0b0c0f;color:#F4F5F7;font-family:M}}
.ph{{position:absolute;left:0;top:0;bottom:0;width:420mm;{bg};-webkit-mask-image:linear-gradient(90deg,#000 82%,transparent 100%)}}
.ph::after{{content:'';position:absolute;inset:0;background:linear-gradient(180deg,#0b0c0f 0,#0b0c0f 11%,rgba(11,12,15,0) 26%,rgba(11,12,15,0) 76%,#0b0c0f 90%,#0b0c0f 100%)}}
.ph .x{{position:absolute;inset:0;display:grid;place-items:center;font-weight:800;font-size:14mm;color:#E3262F;letter-spacing:2mm}}
.info{{position:absolute;right:24mm;top:22mm;bottom:22mm;width:200mm;display:flex;flex-direction:column}}
.logo{{height:44mm;background:url({LOGO}) left center/contain no-repeat}}
.br{{margin-top:12mm;font-weight:700;font-size:8mm;letter-spacing:3mm;color:#9AA1AA}}
.md{{font-weight:900;font-size:21mm;line-height:1}}
.ar{{font-family:C,M;font-weight:900;font-size:13mm;direction:rtl;text-align:left;margin-top:3mm;color:#E9ECEF}}
ul{{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:3mm 8mm;margin-top:9mm}}
li{{border-left:1.2mm solid #E3262F;padding-left:4mm}}li b{{display:block;font-weight:800;font-size:7mm}}li span{{font-family:C,M;font-weight:800;font-size:6.5mm;color:#B4BAC2}}
.pr{{margin-top:auto;font-weight:900;font-size:30mm;color:#E3262F;line-height:.9}}.pr small{{display:block;font-size:7mm;color:#F4F5F7;margin-top:3mm}}.pr i{{font-style:normal;font-family:C,M}}
.bar{{position:absolute;left:0;right:0;bottom:0;height:5mm;background:#E3262F}}
</style><div class="p"><div class="ph">{'' if has else '<div class=x>PHOTO FLOW ICI</div>'}</div>
<div class="info"><div class="logo"></div><div class="br">{c['brand']}</div><div class="md">{c['model']}</div><div class="ar">{c['ar']}</div><ul>{specs}</ul>{price}</div><div class="bar"></div></div>"""
    f=os.path.join(D,f'carte-{k}.html'); open(f,'w').write(html)
    subprocess.run(['/opt/pw-browsers/chromium','--headless','--no-sandbox','--disable-gpu','--no-pdf-header-footer',f'--print-to-pdf={D}/carte-{k}-60x30.pdf','file://'+f],capture_output=True); os.remove(f)
    subprocess.run(['pdftoppm','-png','-r','60','-singlefile',f'{D}/carte-{k}-60x30.pdf',f'{D}/apercu-carte-{k}'])
print('ok')

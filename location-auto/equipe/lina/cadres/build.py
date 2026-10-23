import base64, os, subprocess
D=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(D,'..','..','..')
b64=lambda p: base64.b64encode(open(p,'rb').read()).decode()
def ff(fam,files): return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};src:url(data:font/woff2;base64,{b64('/tmp/claude-0/-home-user-golady-landing/8903800a-f2cc-5c52-a993-fc3707ce5853/scratchpad/fonts/'+f)})}}" for w,f in files)
FONT=ff('M',[(500,'m500.woff2'),(700,'m700.woff2'),(800,'m800.woff2'),(900,'m900.woff2')])+ff('C',[(600,'c600.woff2'),(800,'c800.woff2'),(900,'c900.woff2')])
def u(p,t='jpeg'): return f'data:image/{t};base64,'+b64(os.path.join(R,p))
PHOTO=u('equipe/lina/sandero/photos-flow/scenes/route-dahra.jpg')
LOGO_CL=u('haboub-logo-kit/3-png-transparent/haboub-logo-couleur-pour-fond-clair-3000px.png','png')
LOGO_FL=u('equipe/yasmine/flow/haboub-logo-flow-v1.jpg'); LOGO_DK=u('haboub-logo-kit/3-png-transparent/haboub-logo-couleur-pour-fond-sombre-3000px.png','png')
ICON=u('equipe/yasmine/flow/haboub-icone-flow.jpg'); CARB='data:image/jpeg;base64,'+b64(os.path.join(D,'carbone-tuile.jpg'))
W,H=606,306
base=f"""<!doctype html><meta charset=utf8><style>{FONT}@page{{size:{W}mm {H}mm;margin:0}}*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}.p{{width:{W}mm;height:{H}mm;position:relative;overflow:hidden}}"""
c1=base+f""".p{{background:url({PHOTO}) 50% 60%/cover}}
.sky{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(255,248,235,.7) 0%,rgba(255,248,235,.35) 30%,rgba(255,248,235,0) 50%)}}
.logo{{position:absolute;left:30mm;top:20mm;width:150mm;height:52mm;background:url({LOGO_CL}) left center/contain no-repeat}}
.t{{position:absolute;left:30mm;top:82mm;color:#101317}}
.t h1{{font-family:M;font-weight:900;font-size:30mm;line-height:1;letter-spacing:-.5mm}}
.t h1 b{{color:#E3262F}}
.t h2{{font-family:C;font-weight:900;font-size:24mm;line-height:1.3;direction:rtl;text-align:left;margin-top:4mm}}
.bar{{width:40mm;height:2.5mm;background:#E3262F;margin-top:7mm}}
</style><div class="p"><div class="sky"></div><div class="logo"></div><div class="t"><h1>La route<br>est à <b>vous.</b></h1><h2>الطريق ليك</h2><div class="bar"></div></div></div>"""
c2=base+f""".p{{background:repeating-linear-gradient(45deg,rgba(255,255,255,.035) 0 1.2mm,rgba(0,0,0,0) 1.2mm 2.4mm),repeating-linear-gradient(-45deg,rgba(0,0,0,.25) 0 1.2mm,rgba(0,0,0,0) 1.2mm 2.4mm),#121418;color:#F4F5F7}}
.veil{{position:absolute;inset:0;background:radial-gradient(80% 90% at 50% 40%,rgba(8,9,11,.15),rgba(8,9,11,.75))}}
.logo{{position:absolute;left:50%;top:22mm;transform:translateX(-50%);width:300mm;height:80mm;background:url({LOGO_DK}) center/contain no-repeat}}
.wm{{position:absolute;right:-60mm;bottom:-70mm;width:260mm;height:260mm;border-radius:50%;background:url({ICON}) center/cover;opacity:.12}}
.vals{{position:absolute;left:30mm;right:30mm;top:118mm;display:grid;grid-template-columns:1fr 1fr 1fr;text-align:center}}
.v{{padding:0 6mm;border-left:.8mm solid rgba(255,255,255,.18)}}.v:first-child{{border-left:0}}
.v b{{display:block;font-family:M;font-weight:900;font-size:21mm;letter-spacing:.5mm}}
.v span{{display:block;font-family:C;font-weight:800;font-size:19mm;color:#E3262F;margin-top:3mm}}
.bot{{position:absolute;left:0;right:0;bottom:26mm;text-align:center;font-family:M;font-weight:700;font-size:7mm;letter-spacing:4mm;color:#B4BAC2}}
</style><div class="p"><div class="veil"></div><div class="wm"></div><div class="logo"></div>
<div class="vals"><div class="v"><b>CONFIANCE</b><span>الثقة</span></div><div class="v"><b>LIBERTÉ</b><span>الحرية</span></div><div class="v"><b>PROXIMITÉ</b><span>القرب</span></div></div>
<div class="bot">MAZOUNA · DEPUIS 2026</div></div>"""
for n,h in (('cadre-1-la-route-est-a-vous',c1),('cadre-2-valeurs',c2)):
    f=os.path.join(D,n+'.html'); open(f,'w').write(h)
    subprocess.run(['/opt/pw-browsers/chromium','--headless','--no-sandbox','--disable-gpu','--no-pdf-header-footer','--print-to-pdf='+os.path.join(D,n+'.pdf'),'file://'+f],capture_output=True); os.remove(f)
print('ok')

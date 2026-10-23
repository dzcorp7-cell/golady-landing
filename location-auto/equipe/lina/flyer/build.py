import base64, io, os, segno, subprocess
D=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(D,'..','..','..')
b64=lambda p: base64.b64encode(open(p,'rb').read()).decode()
def ff(fam,files): return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};src:url(data:font/woff2;base64,{b64('/tmp/claude-0/-home-user-golady-landing/8903800a-f2cc-5c52-a993-fc3707ce5853/scratchpad/fonts/'+f)})}}" for w,f in files)
FONT=ff('M',[(500,'m500.woff2'),(700,'m700.woff2'),(800,'m800.woff2'),(900,'m900.woff2')])+ff('C',[(600,'c600.woff2'),(800,'c800.woff2'),(900,'c900.woff2')])
img=lambda p:'data:image/jpeg;base64,'+b64(os.path.join(R,p))
LOGO=img('equipe/lina/sandero/logo-crop.jpg'); CAR=img('equipe/lina/sandero/photos-flow/sandero-3-4-avant.jpg'); FAM=img('equipe/lina/sandero/photos-flow/scenes/famille.jpg')
b=io.BytesIO(); segno.make('https://wa.me/213557190401',error='h').save(b,kind='svg',scale=10,border=1,dark='#101317',xmldecl=False)
QR=b.getvalue().decode().replace('<svg ','<svg style="width:100%;height:auto;display:block" ',1)
W,H=154,216  # A5 + 3mm fonds perdus
html=f"""<!doctype html><meta charset=utf8><style>{FONT}
@page{{size:{W}mm {H}mm;margin:0}}*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:M,sans-serif;color:#F4F5F7}}
.p{{width:{W}mm;height:{H}mm;position:relative;overflow:hidden;page-break-after:always;background:#0b0c0f}}
.in{{position:absolute;inset:3mm;}} /* zone finie A5 */
.ar{{font-family:C,sans-serif;direction:rtl}}
/* RECTO */
.logo{{position:absolute;left:0;right:0;top:0;height:46mm;background:url({LOGO}) center/cover;-webkit-mask-image:linear-gradient(180deg,#000 72%,transparent)}}
.car{{position:absolute;left:0;right:0;top:40mm;height:88mm;background:url({CAR}) center/118% auto no-repeat;-webkit-mask-image:linear-gradient(180deg,transparent 0,#000 12%,#000 78%,transparent)}}
.r-txt{{position:absolute;left:10mm;right:10mm;top:118mm}}
.h1{{font-weight:900;font-size:9.5mm;line-height:1.05}}.h1 b{{color:#E3262F}}
.h1ar{{font-weight:900;font-size:8mm;line-height:1.3;margin-top:2mm;text-align:right}}
.chips{{display:flex;gap:1.5mm;margin-top:3.5mm;flex-wrap:wrap}}.chips span{{font-weight:700;font-size:3mm;border:.3mm solid rgba(255,255,255,.35);border-radius:5mm;padding:1mm 2.6mm}}
.price{{position:absolute;left:10mm;bottom:23mm;font-weight:900;font-size:17mm;color:#E3262F;line-height:.9}}.price small{{display:block;font-size:4mm;color:#F4F5F7;margin-top:1.5mm}}.price small i{{font-style:normal;font-family:C;font-weight:800;margin-left:3mm}}
.band{{position:absolute;left:0;right:0;bottom:0;height:21mm;background:#E3262F;display:flex;align-items:center;justify-content:space-between;padding:0 10mm 3mm}}
.band span{{display:block;font-weight:700;font-size:2.8mm;opacity:.9}}.band b{{font-weight:900;font-size:6.2mm}}
/* VERSO */
.v-top{{position:absolute;left:0;right:0;top:0;height:78mm;background:url({FAM}) 70% 50%/cover;-webkit-mask-image:linear-gradient(180deg,#000 70%,transparent)}}
.v-tag{{position:absolute;left:10mm;top:60mm;background:#E3262F;padding:2mm 4mm;transform:skewX(-10deg)}}.v-tag span{{display:block;transform:skewX(10deg);font-weight:900;font-size:5mm}}
.cols{{position:absolute;left:10mm;right:10mm;top:84mm;display:grid;grid-template-columns:1fr 1fr;gap:6mm}}
.cols h3{{font-weight:900;font-size:4.2mm;color:#E3262F;margin-bottom:2mm}}
.cols li{{list-style:none;font-weight:700;font-size:3.4mm;line-height:1.55}}.cols li::before{{content:"✓ ";color:#E3262F}}
.cols .ar h3{{font-size:4.6mm}}.cols .ar li{{font-size:3.6mm;line-height:1.6}}
.towns{{position:absolute;left:10mm;right:10mm;top:131mm;font-weight:700;font-size:3mm;color:#B4BAC2;line-height:1.5}}
.towns b{{color:#F4F5F7}}.towns .ar{{margin-top:1mm;font-size:3.3mm}}
.contact{{position:absolute;left:10mm;right:10mm;bottom:12mm;display:grid;grid-template-columns:1fr 34mm;gap:6mm;align-items:end;border-top:.6mm solid #E3262F;padding-top:5mm}}
.lab{{font-weight:700;font-size:2.8mm;color:#9AA1AA;letter-spacing:.4mm}}.tel{{font-weight:900;font-size:8mm}}.wa{{font-weight:800;font-size:5mm;margin-top:1.5mm}}.wa i{{font-style:normal;color:#E3262F}}
.hrs{{font-weight:700;font-size:3mm;color:#C8CCD2;margin-top:2mm}}
.qrb{{background:#fff;padding:1.8mm;border-radius:2mm}}.ql{{font-weight:800;font-size:2.4mm;text-align:center;margin-top:1.5mm;white-space:nowrap}}
</style><body>
<div class="p"><div class="logo"></div><div class="car"></div>
<div class="r-txt"><div class="h1">Louez la <b>Dacia Sandero</b> à Mazouna</div><div class="h1 ar h1ar">اكري داسيا سانديرو في مازونة</div>
<div class="chips"><span>2025</span><span>Finition Extreme</span><span>Essence</span><span>Climatisation</span></div></div>
<div class="price">11 500<small>DA / jour <i>دج / اليوم</i></small></div>
<div class="band"><div><span>Appel · اتصل</span><b>0796 96 04 26</b></div><div style="text-align:right"><span>WhatsApp · واتساب</span><b>0557 19 04 01</b></div></div></div>

<div class="p"><div class="v-top"></div><div class="v-tag"><span>Pour tous vos besoins</span></div>
<div class="v-tag" style="left:auto;right:10mm;top:68mm"><span class="ar" style="font-family:C">لكل احتياجاتك</span></div><div class="cols"><div><h3>Pourquoi Haboub ?</h3><ul><li>Voiture neuve 2025</li><li>Propre et entretenue</li><li>5 places, grand coffre</li><li>Prix clair, sans surprise</li><li>Réservation par WhatsApp</li></ul></div>
<div class="ar"><h3>علاش حبوب؟</h3><ul><li>طوموبيل جديدة 2025</li><li>نقية ومصانة</li><li>5 بلايص وصندوق واسع</li><li>سومة واضحة بلا مفاجآت</li><li>الحجز عبر واتساب</li></ul></div></div>
<div class="towns"><b>Mazouna</b> · Sidi M'hamed Ben Ali · Aïn Merane · Guettar · Ouarizane · Mediouna<div class="ar">مازونة · سيدي امحمد بن علي · عين مران · القطار · واريزان · مديونة</div></div>
<div class="contact"><div><div class="lab">APPELEZ · اتصل</div><div class="tel">0796 96 04 26</div><div class="wa"><i>WhatsApp</i> 0557 19 04 01</div><div class="hrs">Ouvert 09h–12h · 14h–18h</div><div class="hrs ar" style="font-family:C;text-align:left;direction:rtl;unicode-bidi:plaintext">مفتوح من 9 إلى 12 ومن 14 إلى 18</div></div>
<div><div class="qrb">{QR}</div><div class="ql">Scannez · WhatsApp</div></div></div></div>
"""
open(os.path.join(D,'flyer.html'),'w').write(html)
subprocess.run(['/opt/pw-browsers/chromium','--headless','--no-sandbox','--disable-gpu','--no-pdf-header-footer','--print-to-pdf='+os.path.join(D,'flyer-A5-haboub-sandero.pdf'),'file://'+os.path.join(D,'flyer.html')],capture_output=True)
os.remove(os.path.join(D,'flyer.html')); print('ok')

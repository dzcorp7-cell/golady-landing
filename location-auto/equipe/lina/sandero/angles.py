import base64, io, os, glob, segno, subprocess
D=os.path.dirname(os.path.abspath(__file__))
b64=lambda p: base64.b64encode(open(p,'rb').read()).decode()
def ff(fam,files): return ''.join(f"@font-face{{font-family:{fam};font-weight:{w};src:url(data:font/woff2;base64,{b64('/tmp/claude-0/-home-user-golady-landing/8903800a-f2cc-5c52-a993-fc3707ce5853/scratchpad/fonts/'+f)})}}" for w,f in files)
FONT=ff('M',[(500,'m500.woff2'),(700,'m700.woff2'),(800,'m800.woff2'),(900,'m900.woff2')])+ff('C',[(600,'c600.woff2'),(800,'c800.woff2'),(900,'c900.woff2')])
LOGO='data:image/jpeg;base64,'+b64(os.path.join(D,'logo-crop.jpg'))
def qr():
    b=io.BytesIO(); segno.make('https://wa.me/213557190401',error='h').save(b,kind='svg',scale=10,border=1,dark='#101317',xmldecl=False)
    return b.getvalue().decode().replace('<svg ','<svg style="width:100%;height:auto;display:block" ',1)
QR=qr()
T={'fr':dict(dir='ltr',font='M',model='Dacia Sandero',chips=['2025','Finition Extreme','Essence'],price='11 500',unit='DA / jour',
           avail='Disponible à Mazouna',call='Appel',wa='WhatsApp',hours='Ouvert 09h–12h · 14h–18h',scan='Scannez pour WhatsApp'),
   'ar':dict(dir='rtl',font='C',model='داسيا سانديرو',chips=['2025','نسخة إكستريم','بنزين'],price='11 500',unit='دج / اليوم',
           avail='متوفرة في مازونة',call='اتصل',wa='واتساب',hours='مفتوح من 9 إلى 12 ومن 14 إلى 18',scan='امسح للتواصل عبر واتساب')}
SIZES={'post':(1080,1350),'story':(1080,1920)}
def page(car,lang,fmt,ang=None):
    t=T[lang]; W,H=SIZES[fmt]; carh=380 if fmt=='post' else 680
    carcss=f"background:url(data:image/jpeg;base64,{b64(car)}) center/{'100%' if fmt=='post' else '112%'} auto no-repeat #0b0c0f" if car else "background:linear-gradient(135deg,#2a2f37,#14171b);display:grid;place-items:center"
    ph='' if car else '<div style="font:800 40px M;color:#E3262F;letter-spacing:4px">PHOTO FLOW ICI</div>'
    chips=''.join(f'<span>{c}</span>' for c in t['chips'])
    A=ANG[ang][lang]; bl=''.join(f'<li>{b}</li>' for b in A['b'])
    angle=f'<div class="tag"><span>{A["t"]}</span></div><ul class="bl">{bl}</ul>'
    return f"""<!doctype html><html dir="{t['dir']}"><meta charset=utf8><style>{FONT}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{display:flow-root;position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:{t['font']},M,sans-serif;color:#F4F5F7;
 background:radial-gradient(110% 60% at 50% 0%,#1d2228 0%,#0c0e11 55%,#07080a 100%)}}
.logo{{height:{265 if fmt=='post' else 320}px;background:url({LOGO}) center/cover;-webkit-mask-image:linear-gradient(180deg,#000 70%,transparent 100%);margin-top:{0 if fmt=='post' else 60}px}}
.car{{height:{carh}px;margin:-40px 0 0;-webkit-mask-image:linear-gradient(180deg,transparent 0,#000 14%,#000 72%,transparent 100%);{carcss};position:relative}}

.info{{padding:0 60px;margin-top:-30px;position:relative;z-index:1}}
h1{{font-weight:900;font-size:{74 if lang=='fr' else 68}px;line-height:{1.05 if lang=='fr' else 1.25}}}
.chips{{display:flex;gap:12px;margin-top:14px;flex-wrap:wrap}}
.chips span{{font-weight:700;font-size:26px;padding:8px 18px;border:2px solid rgba(255,255,255,.25);border-radius:40px}}
.row{{display:flex;justify-content:space-between;align-items:flex-end;margin-top:{14 if fmt=='post' else 50}px;gap:30px}}
.price{{direction:ltr;unicode-bidi:isolate;font-weight:900;font-size:{120 if fmt=='post' else 150}px;color:#E3262F;line-height:.9;white-space:nowrap}}
.price small{{direction:{t['dir']};text-align:{'left' if lang=='fr' else 'right'};display:block;font-size:34px;color:#F4F5F7;font-weight:800;margin-top:12px}}
.qr{{width:{190 if fmt=='post' else 230}px;flex:none;text-align:center}}.qr .b{{background:#fff;padding:10px;border-radius:14px}}
.qr p{{font-weight:700;font-size:18px;margin-top:8px;color:#C8CCD2}}
.foot{{position:absolute;left:0;right:0;bottom:0;padding:{26 if fmt=='post' else 50}px 60px;background:#E3262F;display:flex;justify-content:space-between;align-items:center;gap:20px}}
.foot b{{font-weight:900;font-size:44px;direction:ltr;unicode-bidi:isolate}}.foot span{{font-weight:700;font-size:24px;display:block;opacity:.9}}
.avail{{font-weight:800;font-size:28px;color:#C8CCD2;margin-top:{14 if fmt=='post' else 30}px}}
.hours{{font-weight:700;font-size:24px;color:#9AA1AA;margin-top:10px}}
.tag{{display:inline-block;background:#E3262F;padding:10px 22px;transform:skewX(-10deg);margin-bottom:16px}}
.tag span{{display:block;transform:skewX(10deg);font-weight:900;font-size:{40 if lang=='fr' else 42}px;line-height:1.15;color:#fff}}
.bl{{list-style:none;display:grid;gap:{6 if lang=='fr' else 0}px;margin-bottom:16px}}
.bl li{{line-height:{1.25 if lang=='fr' else 1.45};font-weight:700;font-size:{28 if lang=='fr' else 27}px;color:#E9ECEF}}.bl li::before{{content:"✓";color:#E3262F;font-weight:900;margin-inline-end:12px}}
h1{{font-size:{50 if lang=='fr' else 46}px !important;line-height:1.15 !important}}.chips span{{font-size:22px !important;padding:5px 14px !important}}
.price{{font-size:{100 if fmt=='post' else 140}px !important}}.qr{{width:{150 if fmt=='post' else 200}px !important}}.qr p{{font-size:15px !important;white-space:nowrap;margin-top:6px !important}}.price small{{margin-top:6px !important;font-size:30px !important}}
</style><body>
<div class="logo"></div><div class="car">{ph}</div>
<div class="info">{angle}<h1>{t['model']}</h1><div class="chips">{chips}</div>
<div class="row"><div><div class="price">{t['price']}<small>{t['unit']}</small></div></div>
<div class="qr"><div class="b">{QR}</div><p>{t['scan']}</p></div></div></div>
<div class="foot"><div><span>{t['call']}</span><b>0796 96 04 26</b></div><div><span>{t['wa']}</span><b>0557 19 04 01</b></div></div>
</body></html>"""
ANG={
 'famille':{'fr':dict(t='La voiture de toute la famille',b=['5 places confortables','Grand coffre pour les bagages','Climatisation']),
            'ar':dict(t='سيارة العائلة كاملة',b=['5 بلايص مريحة','صندوق واسع للحوايج','مكيف هواء'])},
 'fetes':{'fr':dict(t='Mariages, fêtes, visites : arrivez en beauté',b=['Voiture neuve et impeccable','Réservez à l\'avance','Prix fixe, sans surprise']),
          'ar':dict(t='أعراس، زيارات… أوصل بأناقة',b=['طوموبيل جديدة ونقية','احجز مسبقاً','سومة ثابتة بلا مفاجآت'])},
 'travail':{'fr':dict(t='Vos déplacements pro, sans souci',b=['Économique en essence','Fiable sur la route','Disponible rapidement']),
            'ar':dict(t='تنقلاتك للخدمة بلا تخمام',b=['اقتصادية في البنزين','موثوقة في الطريق','متوفرة بسرعة'])},
 'securite':{'fr':dict(t='Neuve. Sûre. Entretenue.',b=['Modèle 2025, presque neuf','Airbags et ABS','Vérifiée avant chaque location']),
             'ar':dict(t='جديدة، آمنة ومصانة',b=['موديل 2025 شبه جديدة','وسائد هوائية و ABS','مراقبة قبل كل كراء'])},
 'diaspora':{'fr':dict(t='Vous rentrez au bled ? Votre voiture vous attend',b=['Réservation par WhatsApp','Remise des clés à Mazouna','Voiture neuve 2025']),
             'ar':dict(t='راجع للبلاد؟ طوموبيلتك تستناك',b=['الحجز عبر واتساب','استلام المفاتيح في مازونة','طوموبيل جديدة 2025'])},
 'depannage':{'fr':dict(t='Votre voiture est au garage ? Pas de panique',b=['Disponible rapidement','Location dès 1 jour','Mazouna et alentours']),
              'ar':dict(t='طوموبيلتك في لاقاراج؟ ما تقلقش',b=['متوفرة بسرعة','الكراء من نهار واحد','مازونة وما جاورها'])},
}
car=os.path.join(D,'photos-flow','sandero-3-4-avant.jpg')
from PIL import Image
for ang in ANG:
    for lang in T:
        for fmt,(W,H) in SIZES.items():
            out=os.path.join(D,'angles',f'{ang}-{fmt}-{lang}')
            open(out+'.html','w').write(page(car,lang,fmt,ang))
            subprocess.run(['/opt/pw-browsers/chromium','--headless','--no-sandbox','--disable-gpu','--hide-scrollbars',f'--window-size={W},{H+300}',f'--screenshot={out}.full.png','file://'+out+'.html'],capture_output=True)
            Image.open(out+'.full.png').crop((0,0,W,H)).convert('RGB').save(out+'.png'); os.remove(out+'.full.png'); os.remove(out+'.html')
print('ok')

import sys, re
sys.path.insert(0,'v2'); from gen import PAL, wheel
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FONTS={w:TTFont(f'/tmp/claude-0/-home-user-golady-landing/8903800a-f2cc-5c52-a993-fc3707ce5853/scratchpad/fonts/s{w}.woff2') for w in (500,800,900)}
def text_path(s,w,size,x,y,ls=0,anchor='start'):
    f=FONTS[w]; gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm; hm=f['hmtx']
    sc=size/upm; adv=[hm[cmap[ord(c)]][0]*sc+ls for c in s]; tot=sum(adv)-ls
    cx = x - (tot/2 if anchor=='middle' else 0)
    ds=[]
    for c,a in zip(s,adv):
        g=cmap[ord(c)]; pen=SVGPathPen(gs); tp=TransformPen(pen,(sc,0,0,-sc,cx,y)); gs[g].draw(tp); ds.append(pen.getCommands()); cx+=a
    return ' '.join(ds)
def logo_paths(p, ink):
    W=wheel(p,100)
    W=re.sub(r'<text[^>]*>H</text>', f'<path d="{text_path("H",900,12,0,4.2,anchor="middle")}" fill="{p["acc"]}"/>', W)
    W=W.replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="-50 -50 100 100" width="100" height="100">','<g transform="translate(300,78) scale(.92)">').replace('</svg>','</g>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 10 560 150">
<path d="{text_path('HAB',900,96,40,112,-1)}" fill="{ink}"/>
{W}
<path d="{text_path('UB',900,96,350,112,-1)}" fill="{ink}"/>
<rect x="88" y="132" width="40" height="7" fill="{p['acc']}" transform="skewX(-20)"/>
<path d="{text_path('LOCATION',800,24,128,141,10)}" fill="{ink}"/>
<rect x="377" y="122" width="4" height="20" fill="{ink}" transform="skewX(-20)"/>
<path d="{text_path('MAZOUNA',800,24,346,141,10)}" fill="{p['acc']}"/>

</svg>'''
p=PAL['carbone']
open('final/haboub-logo-sur-fond-sombre.svg','w').write(logo_paths(p,p['ink']))
open('final/haboub-logo-sur-fond-clair.svg','w').write(logo_paths(p,p['bg']))
open('final/haboub-logo-noir.svg','w').write(re.sub(r'fill="#[0-9A-Fa-f]{6}"','fill="#000000"',logo_paths(p,'#000000')))
ic=wheel(p,512); ic=re.sub(r'<text[^>]*>H</text>', f'<path d="{text_path("H",900,12,0,4.2,anchor="middle")}" fill="{p["acc"]}"/>', ic)
open('final/haboub-icone.svg','w').write(ic)
pp=ic.replace('viewBox="-50 -50 100 100" width="512" height="512">','viewBox="-62 -62 124 124" width="512" height="512"><circle r="62" fill="'+p['bg']+'"/>')
open('final/haboub-photo-profil.svg','w').write(pp)
print('ok')

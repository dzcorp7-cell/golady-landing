import os, re
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
FT={w:TTFont(f'/tmp/claude-0/-home-user-golady-landing/8903800a-f2cc-5c52-a993-fc3707ce5853/scratchpad/fonts/m{w}.woff2') for w in (500,700,800,900) if os.path.exists(f'/tmp/claude-0/-home-user-golady-landing/8903800a-f2cc-5c52-a993-fc3707ce5853/scratchpad/fonts/m{w}.woff2')}
def tp(s,w,size,x,y,ls=0,skew=0.0):
    f=FT[w]; gs=f.getGlyphSet(); cm=f.getBestCmap(); upm=f['head'].unitsPerEm; hm=f['hmtx']; sc=size/upm; cx=x; ds=[]
    for c in s:
        if c==' ': cx+=hm[cm[32]][0]*sc+ls; continue
        g=cm[ord(c)]; p=SVGPathPen(gs); gs[g].draw(TransformPen(p,(sc,0,-sc*skew,-sc,cx,y))); ds.append(p.getCommands()); cx+=hm[g][0]*sc+ls
    return ' '.join(ds), cx-ls
def wheel(mode, cx, cy, r):
    # mode: color | white | black
    if mode=='color': rim='url(#rim)'; spoke='url(#metal)'; hub='url(#metal)'; red='#E3262F'; cap='#2a2d31'; slot='#16181b'
    else:
        c='#FFFFFF' if mode=='white' else '#000000'; rim=spoke=hub=c; red=c; cap='none'; slot='none'
    ro, ri = r, r*0.74
    # flat-bottom ring via even-odd path
    import math
    def ring(rad, flat):
        a=math.acos(flat/rad); x=rad*math.sin(a)
        return f"M{cx-x:.1f},{cy+flat:.1f} A{rad},{rad} 0 1 1 {cx+x:.1f},{cy+flat:.1f} Z"
    d=ring(ro,ro*0.86)+' '+ring(ri,ri*0.80)
    out=f'<path d="{d}" fill="{rim}" fill-rule="evenodd"/>'
    if mode=='color': out+=f'<path d="{ring(ro,ro*0.86)}" fill="none" stroke="#9AA1A8" stroke-width="{r*0.03:.2f}"/>'
    out+=f'<rect x="{cx-r*0.07:.1f}" y="{cy-ro:.1f}" width="{r*0.14:.1f}" height="{ro-ri+1:.1f}" fill="{red}"/>'
    if mode=='color': out+=f'<path d="{ring(ro-r*0.04,ro*0.83)}" fill="none" stroke="#E3262F" stroke-width="{r*0.012:.2f}" stroke-dasharray="{r*.04:.1f} {r*.03:.1f}" opacity=".7"/>'
    # spokes
    w=r*0.17
    out+=f'<path d="M{cx-ri-2:.1f},{cy-w*0.6:.1f} L{cx-r*0.2:.1f},{cy-w*0.9:.1f} L{cx-r*0.2:.1f},{cy+w*0.9:.1f} L{cx-ri-2:.1f},{cy+w*0.6:.1f}Z" fill="{spoke}"/>'
    out+=f'<path d="M{cx+ri+2:.1f},{cy-w*0.6:.1f} L{cx+r*0.2:.1f},{cy-w*0.9:.1f} L{cx+r*0.2:.1f},{cy+w*0.9:.1f} L{cx+ri+2:.1f},{cy+w*0.6:.1f}Z" fill="{spoke}"/>'
    out+=f'<path d="M{cx-w*0.9:.1f},{cy+r*0.15:.1f} L{cx+w*0.9:.1f},{cy+r*0.15:.1f} L{cx+w*0.6:.1f},{cy+ri*0.82:.1f} L{cx-w*0.6:.1f},{cy+ri*0.82:.1f}Z" fill="{spoke}"/>'
    if mode=='color':
        for sx in (-1,1): out+=f'<rect x="{cx+sx*r*0.47-r*0.09:.1f}" y="{cy-r*0.025:.1f}" width="{r*0.18:.1f}" height="{r*0.05:.1f}" rx="{r*0.025:.1f}" fill="{slot}"/>'
        out+=f'<rect x="{cx-r*0.025:.1f}" y="{cy+r*0.33:.1f}" width="{r*0.05:.1f}" height="{r*0.2:.1f}" rx="{r*0.025:.1f}" fill="{slot}"/>'
    out+=f'<circle cx="{cx}" cy="{cy}" r="{r*0.27:.1f}" fill="{hub}"/>'
    if mode=='color': out+=f'<circle cx="{cx}" cy="{cy}" r="{r*0.17:.1f}" fill="{cap}"/><circle cx="{cx}" cy="{cy}" r="{r*0.13:.1f}" fill="url(#metal)"/>'
    else: out+=f'<circle cx="{cx}" cy="{cy}" r="{r*0.15:.1f}" fill="{"#000" if mode=="white" else "#fff"}"/>'
    return out
DEFS='''<defs><linearGradient id="rim" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a3e44"/><stop offset=".5" stop-color="#16181b"/><stop offset="1" stop-color="#0b0c0e"/></linearGradient>
<linearGradient id="metal" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F4F6F8"/><stop offset=".5" stop-color="#A9B0B8"/><stop offset="1" stop-color="#E2E6EA"/></linearGradient>
<linearGradient id="chrome" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".48" stop-color="#C9CED4"/><stop offset=".52" stop-color="#6E757D"/><stop offset="1" stop-color="#D8DCE0"/></linearGradient>
<linearGradient id="chromeD" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a6068"/><stop offset=".48" stop-color="#2b2f34"/><stop offset=".52" stop-color="#101214"/><stop offset="1" stop-color="#3a3f45"/></linearGradient></defs>'''
def logo(mode):
    # mode: dark (on dark bg), light (on light bg), white, black
    sk=0.0; size=150
    A,xa=tp('HAB',900,size,40,170,4,sk)
    R=58; wx=xa+R+14; wy=118
    B,xb=tp('UB',900,size,wx+R+14,170,4,sk)
    L,xl=tp('LOCATION',700,40,46,250,15)
    S,xs=tp('/',700,40,xl+26,250,0)
    M,xm=tp('MAZOUNA',700,40,xs+26,250,15)
    W=max(xb,xm)+60
    if mode=='dark': f1='url(#chrome)'; st='#9aa1a8'; f2='#C9CED4'; red='#E3262F'; wm='color'
    elif mode=='light': f1='url(#chromeD)'; st='#000'; f2='#3a3f45'; red='#D11F28'; wm='color'
    else:
        c='#FFFFFF' if mode=='white' else '#000000'; f1=f2=red=c; st='none'; wm=mode
    stroke=''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W:.0f} 290">{DEFS}
<g transform="translate(36,0) skewX(-12)"><path d="{A}" fill="{f1}"/></g>{wheel(wm,wx+14,wy,R)}<g transform="translate(36,0) skewX(-12)"><path d="{B}" fill="{f1}"/></g>
<path d="{L}" fill="{f2}"/><path d="{S}" fill="{f2}"/><path d="{M}" fill="{red}"/></svg>'''
def icon(mode):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 300">{DEFS}{wheel(mode,150,150,130)}</svg>'
D='2-vectoriel'
for m,n in (('dark','haboub-logo-couleur-pour-fond-sombre'),('light','haboub-logo-couleur-pour-fond-clair'),('white','haboub-logo-blanc'),('black','haboub-logo-noir')):
    open(f'{D}/{n}.svg','w').write(logo(m))
for m,n in (('color','haboub-volant-couleur'),('white','haboub-volant-blanc'),('black','haboub-volant-noir')):
    open(f'{D}/{n}.svg','w').write(icon(m))
print('ok')

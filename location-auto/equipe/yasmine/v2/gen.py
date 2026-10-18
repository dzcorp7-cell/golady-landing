import itertools, sys
_n=itertools.count()
PAL={
 "carbone":dict(nom="Carbone & rouge course",bg="#101317",ink="#F4F5F7",rim1="#6A727D",rim2="#23272D",acc="#E3262F",acc2="#FF5A4F",metal1="#E9ECEF",metal2="#8A939C"),
 "nuit":dict(nom="Bleu nuit & orange sport",bg="#0A2240",ink="#FFFFFF",rim1="#5E7698",rim2="#1A2C47",acc="#FF6A13",acc2="#FF9A55",metal1="#F1F4F8",metal2="#8FA0B5"),
 "racing":dict(nom="Anthracite & jaune racing",bg="#1A1D22",ink="#FFFFFF",rim1="#717883",rim2="#2A2E34",acc="#FFC20E",acc2="#FFE07A",metal1="#EDEFF2",metal2="#8C939B"),
}
def wheel(p, size=100):
    i=next(_n); u=lambda s:f"{s}{i}"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="-50 -50 100 100" width="{size}" height="{size}">
<defs>
 <linearGradient id="{u('rim')}" x1="0" y1="-1" x2="0" y2="1" gradientUnits="objectBoundingBox"><stop offset="0" stop-color="{p['rim1']}"/><stop offset="1" stop-color="{p['rim2']}"/></linearGradient>
 <radialGradient id="{u('hub')}" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="{p['metal1']}"/><stop offset="1" stop-color="{p['metal2']}"/></radialGradient>
 <linearGradient id="{u('sp')}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{p['metal1']}"/><stop offset="1" stop-color="{p['metal2']}"/></linearGradient>
 <clipPath id="{u('fo')}"><rect x="-50" y="-50" width="100" height="85"/></clipPath>
 <clipPath id="{u('fi')}"><rect x="-50" y="-50" width="100" height="76"/></clipPath>
 <mask id="{u('m')}"><g clip-path="url(#{u('fo')})"><circle r="44" fill="#fff"/></g><g clip-path="url(#{u('fi')})"><circle r="32" fill="#000"/></g></mask>
</defs>
<g mask="url(#{u('m')})">
 <rect x="-50" y="-50" width="100" height="100" fill="url(#{u('rim')})"/>
 <path d="M-44,-8 A44,44 0 0 1 -30,-32 L-23,-24 A32,32 0 0 0 -32,-6Z M44,-8 A44,44 0 0 0 30,-32 L23,-24 A32,32 0 0 1 32,-6Z" fill="#000" opacity=".35"/>
 <rect x="-4.5" y="-50" width="9" height="20" fill="{p['acc']}"/>
 <path d="M-46,-14 A46,46 0 0 1 -14,-44" stroke="#fff" stroke-opacity=".18" stroke-width="3" fill="none"/>
 <circle r="38" fill="none" stroke="{p['acc']}" stroke-width="1.6" stroke-dasharray="3 2.2" opacity=".9"/>
</g>
<g clip-path="url(#{u('fo')})"><circle r="43.5" fill="none" stroke="{p['metal1']}" stroke-width="1.6" opacity=".85"/></g>
<line x1="-30" y1="35" x2="30" y2="35" stroke="{p['metal1']}" stroke-width="1.6" opacity=".85"/>
<path d="M-32,-1 L-12,-5 Q-8,4 -12,10 L-30,14 Z" fill="url(#{u('sp')})"/>
<path d="M32,-1 L12,-5 Q8,4 12,10 L30,14 Z" fill="url(#{u('sp')})"/>
<path d="M-9,10 L9,10 L13,26 L-13,26 Z" fill="url(#{u('sp')})"/>
<path d="M-6,15 L6,15 L8,22 L-8,22Z" fill="{p['rim2']}" opacity=".55"/>
<circle r="13" fill="url(#{u('hub')})"/>
<circle r="9" fill="{p['rim2']}"/>
<text x="0" y="4.2" text-anchor="middle" font-family="Saira, Montserrat, Arial Black, sans-serif" font-style="italic" font-weight="900" font-size="12" fill="{p['acc']}">H</text>
</svg>'''
def logo(p, w=560, onlight=False):
    ink = p['bg'] if onlight else p['ink']
    W=wheel(p,100).replace('<svg xmlns="http://www.w3.org/2000/svg" viewBox="-50 -50 100 100" width="100" height="100">','<g transform="translate(300,78) scale(.92)">').replace('</svg>','</g>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 190" width="{w}" style="max-width:100%;height:auto">
<g font-family="Saira, Montserrat, Arial Black, sans-serif" font-style="italic" font-weight="900">
 <text x="40" y="112" font-size="96" fill="{ink}" letter-spacing="-1">HAB</text>
 {W}
 <text x="350" y="112" font-size="96" fill="{ink}" letter-spacing="-1">UB</text>
 <rect x="88" y="132" width="40" height="7" fill="{p['acc']}" transform="skewX(-20)"/>
 <text x="128" y="141" font-size="24" font-weight="800" fill="{ink}" letter-spacing="10">LOCATION</text>
 <text x="44" y="174" font-size="17" font-weight="500" fill="{ink}" opacity=".75" letter-spacing="1">La confiance, au volant.</text>
</g></svg>'''

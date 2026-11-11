# Put the Monogram artwork on the printer's dieline (974BANDS_200_80_220 — face 200 mm, gusset 80 mm, height 220 mm).
# Sheet in points (2060 x 1232 pt) exactly like the printer's file; their cut (black), fold (red) and dimension lines are copied on top.
import re, sys, os, xml.etree.ElementTree as ET
import importlib.util
_sp = importlib.util.spec_from_file_location('bag_gen', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gen.py'))
gen = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(gen)
SRC = sys.argv[1]  # printer's dieline as SVG (pdftocairo -svg of their PDF)

SW, SH = 2060, 1232
TOP_CUT, TOP_FOLD, BOT_FOLD, BOT_CUT = 120.748, 219.9606, 843.5826, 1007.9921
GLUE_L, A, GA, B, GB, RIGHT = 276.5039, 327.5276, 894.4567, 1121.2284, 1688.1575, 1912.0945
k = (GA - A) / 1000  # pt per design unit (566.93 pt / 1000 u)

# ---- printer's dieline, artwork removed ----
ET.register_namespace('', 'http://www.w3.org/2000/svg'); ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
NS = '{http://www.w3.org/2000/svg}'
root = ET.parse(SRC).getroot()
DIE = ('13.729858%', '93.273926%', '92.939758%')  # cut (black), fold (red), dimensions (red)
def keep(e):
    st, fi = e.get('stroke', ''), e.get('fill', '')
    return any(c in st for c in DIE) or '92.939758%' in fi
def filt(e):
    out = []
    for c in list(e):
        if c.tag == NS + 'defs': continue
        if keep(c): out.append(c); continue
        if c.tag == NS + 'g':
            kids = filt(c)
            if kids:
                g = ET.Element(c.tag, c.attrib); g.extend(kids); out.append(g)
    return out
defs = root.find(NS + 'defs')
die = ET.tostring(defs, encoding='unicode') + ''.join(ET.tostring(x, encoding='unicode') for x in filt(root))

# ---- artwork panels (nested viewports reuse the Monogram design 1:1) ----
art = gen.svg
_pc = [0]
def panel(x, w, vx, vw):
    _pc[0] += 1; i = _pc[0]; h = BOT_FOLD - TOP_FOLD; sx, sy = w / vw, h / gen.PH
    return (f'<defs><clipPath id="pc{i}"><rect x="{x}" y="{TOP_FOLD}" width="{w}" height="{h}"/></clipPath></defs>'
            f'<g clip-path="url(#pc{i})"><g transform="translate({x - vx*sx},{TOP_FOLD - gen.Y*sy}) scale({sx},{sy})">{art}</g></g>')
s = [f'<rect width="{SW}" height="{SH}" fill="#fff"/>',
     panel(A, GA-A, gen.FR, 1000), panel(GA, B-GA, gen.LG, gen.GW),
     panel(B, GB-B, gen.FR, 1000), panel(GB, (GB-B)*gen.GW/1000, gen.RG, gen.GW),
     die]
mm = 25.4/72
gen.render(''.join(s), SW, SH, round(SW*mm, 3), round(SH*mm, 3), '974-bag-monogram-white-DIELINE', '974 Bag — Monogram (white) on dieline 200x80x220')

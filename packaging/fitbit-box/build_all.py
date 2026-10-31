import json
W='#F2F2F2'
C=[
 ('01-peach',  'Peach',        '#E3B29B','#D9A48A','#1E1410','#D9522F','#D9522F'),
 ('02-pink',   'Pink',         '#E6A6B2','#DD98A5','#2A1218','#F7DFE2','#E6A6B2'),
 ('03-black',  'Black',        '#141414','#0C0C0C',W,'#E9E9E9','#111111'),
 ('06-khaki',  'Khaki',        '#B7A27C','#A89470','#1E1A12','#E8DBC1','#B7A27C'),
 ('07-sky-blue','Sky Blue',    '#A6C4DF','#97B7D4','#10243A','#F4F8FB','#A6C4DF'),
 ('08-olive-orange','Olive Orange','#4A5440','#3E4735',W,'#D97A3C','#D97A3C'),
 ('09-navy',   'Navy',         '#1F2A5A','#182048',W,'#E6E8F0','#1F2A5A'),
 ('10-cream',  'Cream',        '#EEE2CB','#E4D6BC','#2A2218','#FFFFFF','#EEE2CB'),
 ('11-burgundy','Burgundy',    '#4A2027','#3C1920',W,'#EADDDA','#4A2027'),
]
src=open('box.html').read()
from PIL import Image, ImageDraw
out=[]
IDX={'01-peach':1,'02-pink':2,'03-black':3,'06-khaki':6,'07-sky-blue':7,'08-olive-orange':8,'09-navy':9,'10-cream':10,'11-burgundy':11}
for (slug,name,bg,bg2,fg,loop,dot) in C:
    k=IDX[slug]
    light = fg!=W
    im=Image.new('RGBA',(64,355),(0,0,0,0)); ImageDraw.Draw(im).rounded_rectangle((14,40,50,315),radius=18,fill=loop); im.save(f'loops-{slug}.png')
    s=src.replace('__BAND__',f'band{k}.png').replace('__COL__',name).replace('__DOT__',dot).replace('__BG__',bg).replace('__BG2__',bg2).replace('__FG__',fg)
    s=s.replace('__REAR__',f'rear-{slug}.png').replace('__LOGO__','logo-black.png' if light else 'logo-white.png').replace('__ICONS__','icons-dark.png' if light else 'icons-white.png')
    s=s.replace('__BC__','974100'+slug[:2]).replace('url(loops.png)',f'url(loops-{slug}.png)')
    open(f'box-{slug}.html','w').write(s); out.append(slug)
json.dump(out,open('slugs.json','w'))

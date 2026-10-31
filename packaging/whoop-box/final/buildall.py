import subprocess,json,os
from map import M
from PIL import Image
AR={'sil':('سير سيليكون لساعة Whoop','ناعم · مقاوم للماء والعرق · يناسب 5.0 و MG'),
    'fab':('سير قماش لساعة Whoop','خفيف · يتنفس · يناسب 5.0 و MG'),
    'wp':('سير مقاوم للماء لساعة Whoop','للسباحة والتمرين · يجف بسرعة · يناسب 5.0 و MG')}
tpl=open('tpl.html').read()
os.makedirs('img',exist_ok=True); os.makedirs('pages',exist_ok=True)
for p,(col,mat,key,bc,_) in M.items():
    if not os.path.exists(f'img/p{p}-2.png'):
        subprocess.run(['pdfimages','-f',str(p),'-l',str(p),'-png','src.pdf',f'img/t{p}'],check=True)
        for k,(a,m) in enumerate([(0,1),(2,3),(4,5)]):
            im=Image.open(f'img/t{p}-{a:03d}.png').convert('RGB'); mk=Image.open(f'img/t{p}-{m:03d}.png').convert('L'); im.putalpha(mk); im.save(f'img/p{p}-{k}.png')
    t=tpl
    for a,b in dict(__IMG0__=f'img/p{p}-0.png',__IMG1__=f'img/p{p}-1.png',__IMG2__=f'img/p{p}-2.png',__COL__=col,__MATU__=mat,__ARTITLE__=AR[key][0],__ARSUB__=AR[key][1],__BC__=bc).items(): t=t.replace(a,b)
    open(f'pages/w{p:02d}.html','w').write(t)
print('ok')

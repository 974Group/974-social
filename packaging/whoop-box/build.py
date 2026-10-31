import json
src=open('w.html').read()
S=dict(sil=dict(C='#141414',TINT='#E9E9EA',FG='#FFFFFF',FG2='#DDDDDD',COL='Black',MATU='SILICONE',ARHERO='سيليكون',ARTITLE='سير سيليكون لساعة Whoop',ARSUB='ناعم · مقاوم للماء والعرق · يناسب 5.0 و MG',IMG0='sil0.png',IMG2='sil2.png',LOGO='../pkg/logo-white.png',ICONS='../pkg/icons-white.png'),
       fab=dict(C='#E6A6B2',TINT='#F7E3E7',FG='#2A1218',FG2='#5A3A44',COL='Pink',MATU='SOFT FABRIC',ARHERO='قماش ناعم',ARTITLE='سير قماش ناعم لساعة Whoop',ARSUB='خفيف · يتنفس · يناسب 5.0 و MG',IMG0='fab0.png',IMG2='fab2.png',LOGO='../pkg/logo-black.png',ICONS='../pkg/icons-dark.png'))
for k,v in S.items():
    s=src
    for a,b in v.items(): s=s.replace('__'+a+'__',b)
    open(f'w-{k}.html','w').write(s)

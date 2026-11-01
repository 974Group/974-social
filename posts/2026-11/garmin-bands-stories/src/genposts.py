head=open('d.html').read().split('<!-- 1 CANVAS')[0]
P=[
 dict(id='p1',kick='GARMIN · QUICKFIT',title='قوي.. ويستحمل',sub='سير <span class="en">Garmin Canvas</span> المنسوج ببكلة',bg='#2B3224',fg='#fff',ac='#C8CFA8',card='rgba(255,255,255,.07)',logo='logo-white.png',price='89',old=None,sizes='20 · 22 · 26 mm',
  cols=[('canvas_c','Navy'),('canvas_or_c','Orange'),('canvas_gr_c','Green'),('canvas_dg_c','Dark Green'),('canvas_bk_c','Black')]),
 dict(id='p2',kick='GARMIN · FABRIC',title='نعومة القماش.. وثبات القارمن',sub='سير <span class="en">Garmin Fabric QuickFit</span>',bg='#EDE6D9',fg='#2E2620',ac='#5B4B3A',card='#E2D8C6',logo='logo-black.png',price='89',old=None,sizes='22 · 26 mm',
  cols=[('fabric_c','Light Grey'),('fabric_grey_c','Grey'),('fabric_bk_c','Black'),('fabric_wh_c','White'),('fabric_kh_c','Khaki'),('fabric_gr_c','Green'),('fabric_blue_c','Blue'),('fabric_navy_c','Navy')]),
 dict(id='p3',kick='NYLON · GEN 2',title='نايلون يلزق ويفك بثانية',sub='<span class="en">Garmin Nylon Gen2</span>',bg='#1C1F1D',fg='#fff',ac='#E4572E',card='#2A2E2B',logo='logo-white.png',price='89',old='99',sizes='20 · 22 · 26 mm',
  cols=[('gen2_c','Black'),('gen2_grey_c','Grey'),('gen2_green_c','Green')]),
 dict(id='p4',kick='GARMIN SILICONE',title='14 لون.. لكل يوم لون',sub='سير <span class="en">Garmin Silicone</span>',bg='#FFFFFF',fg='#111',ac='#7A7A7A',card='#F3F3F3',logo='logo-black.png',price='99',old=None,sizes='22 · 26 mm',
  cols=[('silicone_c','Black'),('sil_white_c','White'),('sil_grey_c','Grey'),('sil_slate_c','Slate'),('sil_royal_c','Dark Blue'),('sil_dblue_c','Royal Blue'),('sil_bb_c','Baby Blue'),('sil_teal_c','Teal'),('sil_mint_c','Mint'),('sil_lgreen_c','Light Green'),('sil_army_c','Army Green'),('sil_ye_c','Yellow'),('sil_or_c','Orange'),('sil_red_c','Red')]),
 dict(id='p5',kick='QUICKFIT NYLON',title='خفيف.. تنساه بيدك',sub='سير <span class="en">Garmin QuickFit Nylon</span>',bg='#14213D',fg='#fff',ac='#C6F432',card='rgba(255,255,255,.07)',logo='logo-white.png',price='99',old=None,sizes='22 · 26 mm',
  cols=[('qfnylon_c','Black'),('qfn_grey_c','Grey'),('qfn_green_c','Green'),('qfn_bg_c','Black & Grey'),('qfn_bp_c','Blue & Purple')]),
 dict(id='p6',kick='FKM RUBBER',title='للشغل الثقيل والرياضة القوية',sub='سير <span class="en">Garmin FKM Rubber</span>',bg='#0E0E0E',fg='#fff',ac='#FF6A13',card='#1A1A1A',logo='logo-white.png',price='119',old=None,sizes='22 · 26 mm',
  cols=[('fkm_c','Black'),('fkm_grey_c','Grey'),('fkm_nv_c','Navy'),('fkm_or_c','Orange'),('fkm_be_c','Beige')]),
 dict(id='p7',kick='QUICK RELEASE · 20MM',title='لونين في سير واحد',sub='<span class="en">Garmin Quick Release · Two-tone</span>',bg='linear-gradient(90deg,#F7D6E0 0 50%,#E3F7A0 50% 100%)',fg='#1E1E1E',ac='#3A3A3A',card='rgba(255,255,255,.55)',logo='logo-black.png',price='89',old=None,sizes='20 mm',
  cols=[('qr20_c','Orange & Black'),('qr20_pk_c','Pink & White'),('qr20_lg_c','Lime & Black'),('qr20_bg_c','Black & Grey'),('qr20_gb_c','Green & Black')]),
 dict(id='p8',kick='QUICK RELEASE · 24MM',title='تبدّله بدون أدوات',sub='<span class="en">Garmin Quick Release Nylon 24mm</span>',bg='#3A0C14',fg='#fff',ac='#E8A0A6',card='rgba(255,255,255,.06)',logo='logo-white.png',price='99',old=None,sizes='24 mm',
  cols=[('qr24_rb_c','Red & Black'),('qr24_c','Black'),('qr24_cb_c','Cape Blue'),('qr24_mg_c','Military Green'),('qr24_fg_c','Fog Grey'),('qr24_or_c','Orange')]),
 dict(id='p9',kick='GARMIN MAGNETIC',title='يسكّر بالمغناطيس',sub='<span class="en">Garmin Magnetic Silicone</span>',bg='#EFE6DA',fg='#1E1A16',ac='#E2601A',card='#FFFFFF',logo='logo-black.png',price='99',old=None,sizes='22 · 26 mm',
  cols=[('mag_bk_c','Black'),('magnetic_c','Green'),('mag_or_c','Orange')]),
]
def grid(cols):
  n=len(cols);per={3:3,5:3,6:3,8:4,14:7}[n];rows=(n+per-1)//per
  L,R,T,B=48,48,310,1160;gap=16
  W=(1080-L-R-gap*(per-1))/per;H=(B-T-gap*(rows-1))/rows
  if rows==1:
    H=min(H,W*1.75);T=T+((B-T)-H)/2
  out=''
  for i,(f,nm) in enumerate(cols):
    r=i//per;c=i%per;cnt=min(per,n-r*per);off=(per-cnt)*(W+gap)/2
    x=1080-R-(c+1)*W-c*gap-off;y=T+r*(H+gap)
    fs=24 if W>250 else (20 if W>200 else (19 if W>150 else 16))
    out+=f'<div class="c" style="left:{x:.0f}px;top:{y:.0f}px;width:{W:.0f}px;height:{H:.0f}px"><img src="web/{f}.png" style="left:{W*0.07:.0f}px;top:{H*0.05:.0f}px;width:{W*0.86:.0f}px;height:{H*0.78:.0f}px"><span style="font-size:{fs}px">{nm}</span></div>'
  return out
html=head.replace('</style>','''.c{position:absolute;border-radius:24px;overflow:hidden}
.c img{position:absolute;object-fit:contain;filter:drop-shadow(0 12px 16px rgba(0,0,0,.25))}
.c span{position:absolute;left:0;right:0;bottom:14px;text-align:center;font-family:Poppins;font-weight:600;direction:ltr;white-space:nowrap}
</style>''')
for p in P:
  oldh=f'<s class="en" style="font-size:34px;opacity:.55;margin-left:6px">{p["old"]}</s>' if p['old'] else ''
  html+=f'''<div class="s" id="{p['id']}" style="height:1350px;background:{p['bg']};color:{p['fg']}">
 <img class="a" src="{p['logo']}" style="top:56px;right:56px;width:120px">
 <div class="a en" style="top:70px;left:56px;color:{p['ac']};font-weight:700;letter-spacing:5px;font-size:20px">{p['kick']}</div>
 <h1 class="a" style="top:130px;right:56px;left:56px;margin:0;font-size:68px;font-weight:900;line-height:1.1">{p['title']}</h1>
 <div class="a" style="top:230px;right:56px;font-size:32px;font-weight:700;color:{p['ac']}">{p['sub']} · {len(p['cols'])} ألوان</div>
 <style>#{p['id']} .c{{background:{p['card']}}} #{p['id']} .c span{{color:{p['fg']}}}</style>
 {grid(p['cols'])}
 <div class="a" style="top:1186px;left:56px;right:56px;display:flex;justify-content:space-between;align-items:center;border-top:2px solid {p['ac']};padding-top:22px">
  <div style="display:flex;align-items:baseline;gap:10px">{oldh}<b class="en" style="font-size:84px;line-height:1">{p['price']}</b><span style="font-size:34px;font-weight:800">ر.ق</span></div>
  <div style="text-align:left"><div class="en" style="font-size:30px;font-weight:700">{p['sizes']}</div><div class="en" style="font-size:22px;letter-spacing:4px;color:{p['ac']}">974GROUP.NET</div></div></div>
</div>
'''
open('posts.html','w').write(html)

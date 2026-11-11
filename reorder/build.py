# Reorder list with photos — out of stock + running out within ~60 days. Suggested qty covers 60 days of sales.
import sys, os, json, math, base64, io
from PIL import Image
D = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, D)
from rows import ROWS, BASE
SHEET = sys.argv[1]
order = [l.split()[1] for l in open(D + 'urls.txt')]
sh = Image.open(SHEET).convert('RGB'); C, R = 11, 6
cw, ch = sh.width / C, sh.height / R
def thumb(path):
    i = order.index(BASE + path); x, y = (i % C) * cw, (i // C) * ch
    im = sh.crop((round(x), round(y), round(x + cw), round(y + ch))).resize((220, 220), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=82); return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

items = []
for sup, p, v, q, s30, s60, img in ROWS:
    rate = max(s30 / 30, s60 / 60)
    days = 0 if q <= 0 else round(q / rate)
    sug = max(0, round(rate * 60 - q))
    if q > 0 and days > 45: continue
    if sug <= 0: continue
    items.append(dict(sup=sup, p=p, v=v, q=q, s30=s30, days=days, sug=sug, img=thumb(img)))

SUP = [('1', 'المورد 1', 'Whoop 5 fabric · Navigator · Wool · Rolex 3D print · Fitbit silicone 2.0'),
       ('2', 'المورد 2', 'Whoop soft fabric · Waterproof'),
       ('3', 'المورد 3', 'Whoop silicone'),
       ('X', 'موردين ثانيين', 'ستيل · جلد · Rolex heat print · Fitbit · Garmin · Apple Watch · نظارات وماسكات')]
def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;')
secs = ''; total_all = 0; n_out = sum(1 for i in items if i['q'] == 0)
for k, name, sub in SUP:
    its = sorted([i for i in items if i['sup'] == k], key=lambda i: (i['q'] > 0, i['days'], -i['s30']))
    if not its: continue
    tot = sum(i['sug'] for i in its); total_all += tot
    cards = ''
    for i in its:
        st = '<span class="tag out">خلص</span>' if i['q'] == 0 else f'<span class="tag low">يخلص بعد {i["days"]} يوم</span>'
        cards += f'''<article class="card"><img src="{i['img']}" alt="">
<div class="info">{st}<h3 dir="ltr">{esc(i['p'])}</h3>{f'<div class="var" dir="ltr">{esc(i["v"])}</div>' if i['v'] else ''}
<div class="nums"><span>المتوفر <b>{i['q']}</b></span><span>بيع 30 يوم <b>{i['s30']}</b></span></div></div>
<div class="qty"><b>{i['sug']}</b><span>حبة</span></div></article>'''
    secs += f'''<section><header><div><h2>{name}</h2><p dir="ltr">{sub}</p></div><div class="sum"><b>{tot}</b> حبة · {len(its)} صنف</div></header>
<div class="grid">{cards}</div></section>'''

html = f'''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>طلبية جديدة 974</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@500;700;900&family=Poppins:wght@500;600&display=swap" rel="stylesheet">
<style>
:root{{--bg:#F4F1F2;--card:#fff;--ink:#1d1a1c;--mute:#6f6870;--bur:#720842;--dark:#51022D;--line:#e7e1e4;--out:#b3261e;--low:#a8680a;--lowbg:#fff4e0;--outbg:#fde9e8}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#151214;--card:#1f1b1e;--ink:#f1edef;--mute:#a59ca2;--bur:#d9a0bd;--dark:#f1edef;--line:#332c31;--out:#ff8a80;--low:#ffc266;--lowbg:#3a2c12;--outbg:#3d1a19}}}}
:root[data-theme="dark"]{{--bg:#151214;--card:#1f1b1e;--ink:#f1edef;--mute:#a59ca2;--bur:#d9a0bd;--dark:#f1edef;--line:#332c31;--out:#ff8a80;--low:#ffc266;--lowbg:#3a2c12;--outbg:#3d1a19}}
*{{box-sizing:border-box;margin:0}} body{{background:var(--bg);color:var(--ink);font-family:Cairo,sans-serif;padding:20px 16px 48px}}
.wrap{{max-width:1080px;margin:0 auto}}
h1{{font-weight:900;font-size:30px;color:var(--dark)}} .lead{{color:var(--mute);margin-top:4px;font-size:15px}}
.kpis{{display:flex;gap:28px;flex-wrap:wrap;margin:18px 0 8px}} .kpis div b{{display:block;font-size:28px;font-weight:900;color:var(--bur);font-family:Poppins}} .kpis div span{{color:var(--mute);font-size:13px}}
section{{margin-top:30px}} header{{display:flex;justify-content:space-between;align-items:flex-end;gap:12px;border-bottom:2px solid var(--bur);padding-bottom:8px;margin-bottom:14px}}
h2{{font-size:22px;font-weight:900}} header p{{font-family:Poppins;font-size:12px;color:var(--mute);text-align:right}} .sum{{white-space:nowrap;color:var(--mute)}} .sum b{{color:var(--bur);font-size:20px;font-family:Poppins}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px}}
.card{{display:flex;gap:12px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:10px;break-inside:avoid}}
.card img{{width:84px;height:84px;object-fit:contain;background:#fff;border-radius:10px;flex:none}}
.info{{flex:1;min-width:0}} .info h3{{font-family:Poppins;font-weight:600;font-size:13px;line-height:1.3;text-align:right}} .var{{font-family:Poppins;font-size:12px;color:var(--bur);margin-top:2px;text-align:right}}
.tag{{display:inline-block;font-size:11px;font-weight:700;border-radius:20px;padding:0 9px;margin-bottom:3px}} .out{{color:var(--out);background:var(--outbg)}} .low{{color:var(--low);background:var(--lowbg)}}
.nums{{display:flex;gap:12px;font-size:12px;color:var(--mute);margin-top:4px}} .nums b{{color:var(--ink);font-family:Poppins}}
.qty{{text-align:center;flex:none;min-width:58px}} .qty b{{display:block;font-family:Poppins;font-size:24px;color:var(--bur);line-height:1}} .qty span{{font-size:11px;color:var(--mute)}}
.note{{margin-top:28px;color:var(--mute);font-size:13px;line-height:1.7}}
@media print{{body{{background:#fff;padding:0}} .card{{border-color:#ddd}}}}
</style></head><body><div class="wrap">
<h1>طلبية جديدة</h1>
<p class="lead">اللي خلص واللي بيخلص خلال 45 يوم، مع الصور. الكمية المقترحة تغطي بيع شهرين. المخزون محدّث 11 نوفمبر 2026.</p>
<div class="kpis"><div><b>{len(items)}</b><span>صنف</span></div><div><b>{n_out}</b><span>خلص</span></div><div><b>{total_all}</b><span>حبة مقترحة</span></div></div>
{secs}
<p class="note">الكمية = بيع 60 يوم المتوقع (حسب أعلى معدل بيع في آخر 30 أو 60 يوم) ناقص المتوفر. عدّلها حسب أقل كمية عند كل مورد.</p>
</div></body></html>'''
open(D + 'out/reorder.html', 'w').write(html)
print(len(items), n_out, total_all)

# Elastic Loop Bands (new merged product, 14 Nov 2026) — 2-slide carousel + story. All 26 colours are in stock.
import subprocess, sys
sys.path.insert(0, '/home/claude/974-social/templates'); import payfoot
SP = '/tmp/claude-0/-home-claude/bcc2c2d5-4d57-5df4-9795-f402b1a1cd9a/scratchpad'
D = '/home/claude/974-social/posts/2026-11/elastic-loop/'
S = D + 'src/'
LOGO = '/home/claude/974-social/posts/2026-11/pilates-socks/src/logo-black.png'
INK = '#2A0F1C'; M = '#720842'; BG = '#F4F1F2'
COLS = [('black', 'Black'), ('grey-black', 'Grey & Black'), ('black-grey', 'Black & Grey'), ('dark-grey', 'Dark Grey'),
        ('grey', 'Grey'), ('grey-white', 'Grey & White'), ('black-white', 'Black & White'), ('white', 'White'),
        ('black-red', 'Black & Red'), ('red', 'Red'), ('maroon', 'Maroon'), ('maroon-beige', 'Maroon & Beige'), ('orange', 'Orange'),
        ('yellow', 'Yellow'), ('khaki', 'Khaki'), ('khaki-white', 'Khaki & White'), ('black-khaki', 'Black & Khaki'),
        ('green', 'Green'), ('green-white', 'Green & White'), ('green-yellow', 'Green & Yellow'), ('tiffany', 'Tiffany'),
        ('lightblue-white', 'Light Blue & White'), ('blue', 'Blue'), ('navy', 'Navy'), ('darkblue-white', 'Dark Blue & White'),
        ('navy-white-orange', 'Navy, White & Orange')]
XL = {'maroon', 'black-white', 'navy-white-orange', 'khaki-white', 'black-khaki', 'khaki', 'green', 'grey', 'dark-grey', 'black-grey', 'navy'}
FONTS = f'''@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscQyyS8p4_RHH1.woff2)}}
@font-face{{font-family:'Cairo';font-weight:400 900;src:url(file://{SP}/aw/fonts/cairo-SLXVc1nY6HkvangtZmpQdkhzfH5lkSscRiyS8p4_RA.woff2);unicode-range:U+0000-00FF}}
@font-face{{font-family:'Poppins';font-weight:500;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf)}}
@font-face{{font-family:'Poppins';font-weight:700;src:url(file:///usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf)}}'''


def strips(items, top, sw, sh, gap, W=1080):
    x0 = (W - (len(items) * sw + (len(items) - 1) * gap)) // 2
    h = ''
    for i, (f, nm) in enumerate(items):
        x = x0 + i * (sw + gap)
        xl = '<em>XL</em>' if f in XL else ''
        h += f'''<div class="st" style="left:{x}px;top:{top}px;width:{sw}px">
 <img src="file://{S}{f}-v.png" style="width:{sw}px;height:{sh}px">{xl}<i>{nm}</i></div>'''
    return h


CSS = lambda story: f'''{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:{1920 if story else 1350}px;font-family:Cairo;color:{INK};position:relative;overflow:hidden;
background:radial-gradient(900px 600px at 100% 0%,#F1DCE6 0%,transparent 65%),radial-gradient(700px 600px at 0% 100%,#EFE6E9 0%,transparent 70%),{BG}}}
.top{{position:absolute;left:48px;right:48px;display:flex;justify-content:space-between;align-items:center}}
.top img{{height:44px}} .top span{{font-family:Poppins;font-weight:700;font-size:16px;letter-spacing:5px}}
.st{{position:absolute;display:flex;flex-direction:column;align-items:center}}
.st img{{object-fit:fill;filter:drop-shadow(0 10px 10px rgba(60,10,30,.18))}}
.st em{{position:absolute;top:8px;font-style:normal;font-family:Poppins;font-weight:700;font-size:12px;color:#fff;background:{M};border-radius:10px;padding:1px 7px}}
.st i{{font-style:normal;font-family:Poppins;font-weight:500;font-size:13px;letter-spacing:.5px;margin-top:12px;writing-mode:vertical-rl;transform:rotate(180deg);white-space:nowrap;opacity:.75}}
.pf{{position:absolute;left:28px;right:28px;bottom:{30 if not story else 250}px}}
{payfoot.css(1.0 if not story else 1.12)}
.chip{{display:inline-block;background:#fff;border-radius:30px;padding:4px 18px 8px;font-weight:800;box-shadow:0 6px 16px rgba(60,10,30,.08)}}
.bo{{display:inline-block;border:1.5px dashed currentColor;border-radius:30px;padding:2px 16px 6px;font-weight:800;opacity:.75}}
.pill{{background:{M};color:#fff;border-radius:40px;padding:6px 30px 10px;font-weight:900;font-size:38px;white-space:nowrap}} .pill b{{font-family:Poppins}}
'''


def slide1():
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS(False)}
.h{{position:absolute;left:48px;right:48px;top:118px;direction:rtl}}
.h .new{{display:inline-block;background:{M};color:#fff;font-family:Poppins;font-weight:700;font-size:16px;letter-spacing:3px;border-radius:20px;padding:3px 14px}}
.h b{{display:block;font-weight:900;font-size:64px;line-height:1.15;margin-top:8px}} .h b em{{font-style:normal;color:{M}}}
.h i{{display:block;font-style:normal;font-weight:700;font-size:26px;opacity:.75;margin-top:2px}}
.en{{position:absolute;left:48px;top:128px;font-family:Poppins;font-weight:700;font-size:58px;line-height:.95;letter-spacing:-1px;color:{M}}}
.en small{{display:block;font-weight:500;font-size:15px;letter-spacing:4px;color:{INK};opacity:.55;margin-top:8px}}
.fits{{position:absolute;left:48px;right:48px;top:1000px;display:flex;justify-content:center;gap:10px;direction:rtl;font-size:21px}}
.foot{{position:absolute;left:48px;right:48px;top:1080px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.foot .t{{font-weight:800;font-size:27px}} .foot .t span{{display:block;font-weight:700;font-size:19px;opacity:.65}}
</style></head><body>
<div class="top" style="top:44px"><img src="file://{LOGO}"><span>NEW · 26 COLOURS</span></div>
<div class="h"><span class="new">NEW</span><b>ينلبس <em>بسحبة..</em><br>بدون بكلة</b><i>سير مطاطي منسوج · خفيف ومريح طول اليوم</i></div>
<div class="en">Elastic<br>Loop<small>26 COLOURS · 1 / 2</small></div>
{strips(COLS[:13], 440, 62, 380, 14)}
<div class="fits"><span class="chip">Apple Watch</span><span class="chip">ساعات 20mm</span><span class="chip">MoonSwatch</span><span class="bo">سير فقط · بدون الساعة</span></div>
<div class="foot"><div class="t">٢٦ لون.. وكلها متوفرة<span>اسحب ← للباقي والمقاسات</span></div><div class="pill"><b>99</b> ر.ق</div></div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''


def slide2():
    rows = [('S', '120mm'), ('M', '130mm'), ('L', '140mm'), ('XL', '150mm')]
    sz = ''.join(f'<div class="sz"><b>{a}</b><span>{b}</span></div>' for a, b in rows)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS(False)}
.h{{position:absolute;left:48px;right:48px;top:110px;direction:rtl;text-align:right}}
.h b{{display:block;font-weight:900;font-size:50px;line-height:1.2}} .h b em{{font-style:normal;color:{M}}}
.h i{{display:block;font-style:normal;font-weight:700;font-size:22px;opacity:.7}}
.card{{position:absolute;left:48px;right:48px;top:840px;background:#fff;border-radius:30px;padding:22px 28px;box-shadow:0 14px 34px rgba(60,10,30,.10);direction:rtl}}
.card h3{{font-weight:900;font-size:24px;margin-bottom:10px}} .card h3 small{{font-weight:700;font-size:18px;opacity:.6;margin-right:8px}}
.szr{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}}
.sz{{background:{BG};border-radius:18px;padding:6px 0 10px;text-align:center}} .sz b{{display:block;font-family:Poppins;font-weight:700;font-size:28px;color:{M}}} .sz span{{font-family:Poppins;font-weight:500;font-size:16px;opacity:.7}}
.fit{{margin-top:16px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}}
.fit div{{border:1.5px solid #E6D9DF;border-radius:18px;padding:8px 10px 10px;text-align:center;font-weight:800;font-size:18px;line-height:1.3}}
.fit div span{{display:block;font-family:Poppins;font-weight:500;font-size:14px;opacity:.65;direction:ltr}}
.note{{margin-top:12px;font-weight:700;font-size:17px;opacity:.7}}
</style></head><body>
<div class="top" style="top:44px"><img src="file://{LOGO}"><span>ELASTIC LOOP · 2 / 2</span></div>
<div class="h"><b>اختار <em>لونك..</em> واختار مقاسك</b><i>الألوان اللي عليها XL متوفر فيها مقاس XL بعد</i></div>
{strips(COLS[13:], 250, 62, 380, 14)}
<div class="card">
 <h3>طول السير<small>حسب مقاس معصمك</small></h3>
 <div class="szr">{sz}</div>
 <div class="fit"><div>ساعات 20mm<span>MoonSwatch · 20mm lugs</span></div><div>Apple Watch صغير<span>38 · 40 · 41 · 42mm</span></div><div>Apple Watch كبير<span>44 · 45 · 46 · 49mm</span></div></div>
 <div class="note">• الكبير يجيك بقطعة توصيل رصاصي أو أسود تناسب لون ساعتك · مب متأكد من المقاس؟ راسلنا ونساعدك</div>
</div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''


def story():
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS(True)}
.h{{position:absolute;left:48px;right:48px;top:300px;text-align:center;direction:rtl}}
.h .en{{font-family:Poppins;font-weight:700;font-size:96px;line-height:1;color:{M};direction:ltr}}
.h b{{display:block;font-weight:900;font-size:58px;line-height:1.2;margin-top:10px}}
.h i{{display:block;font-style:normal;font-weight:700;font-size:28px;opacity:.7}}
.st i{{display:none}}
.fits{{position:absolute;left:30px;right:30px;top:1318px;display:flex;justify-content:center;gap:10px;direction:rtl;font-size:23px}}
.foot{{position:absolute;left:48px;right:48px;top:1395px;display:flex;justify-content:space-between;align-items:center;direction:rtl}}
.foot .t{{font-weight:800;font-size:30px}} .foot .t span{{display:block;font-family:Poppins;font-weight:500;font-size:20px;opacity:.65;direction:ltr;text-align:right}}
</style></head><body>
<div class="top" style="top:220px"><img src="file://{LOGO}"><span>NEW · 26 COLOURS</span></div>
<div class="h"><div class="en">Elastic Loop</div><b>ينلبس بسحبة.. بدون بكلة</b><i>٢٦ لون · Apple Watch و ساعات 20mm</i></div>
{strips(COLS[:13], 580, 64, 330, 14)}
{strips(COLS[13:], 950, 64, 330, 14)}
<div class="fits"><span class="chip">S · M · L · XL</span><span class="bo">سير فقط · بدون الساعة</span></div>
<div class="foot"><div class="t">كل الألوان متوفرة<span>120 · 130 · 140 · 150mm</span></div><div class="pill"><b>99</b> ر.ق</div></div>
<div class="pf">{payfoot.html()}</div>
</body></html>'''


def shot(html, out, H):
    p = out.replace('.png', '.html'); open(p, 'w').write(html)
    js = f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1080,height:{H}}}}});await p.goto('file://{p}');await p.waitForTimeout(900);await p.screenshot({{path:'{out}'}});await b.close();}})()"
    subprocess.run(['node', '-e', js], check=True, cwd='/home/claude/974-social')


if __name__ == '__main__':
    shot(slide1(), D + 'out/974-elastic-loop-post-1.png', 1350)
    shot(slide2(), D + 'out/974-elastic-loop-post-2.png', 1350)
    shot(story(), D + 'out/974-elastic-loop-story.png', 1920)
    print('ok')

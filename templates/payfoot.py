"""Shared footer for 974 posts/stories: payment methods + 'متوفر في' Snoonu. Owner rule (4 Nov 2026): every post from now on."""
PILLS=open('/home/claude/974-social/templates/pay_pills.html').read()
SNOONU='file:///home/claude/974-social/reels/2026-11/pilates/end/logos/snoonu.png'
def css(scale=1.0, text='#4A1630', label='#7E3D5C'):
    s=scale
    return f'''
.payfoot{{display:flex;align-items:center;justify-content:space-between;direction:rtl;gap:{int(16*s)}px}}
.payfoot .pills{{display:flex;gap:{int(8*s)}px;direction:rtl}}
.payfoot .ch{{display:flex;flex-direction:column;align-items:center;gap:{int(3*s)}px}}
.payfoot .ch .lg{{width:{int(72*s)}px;height:{int(40*s)}px;background:#fff;border-radius:{int(12*s)}px;display:flex;align-items:center;justify-content:center;box-shadow:0 3px 8px rgba(0,0,0,.12);overflow:hidden}}
.payfoot .ch .lg svg{{height:{int(24*s)}px!important;width:auto!important}}
.payfoot .ch.applepay .lg svg{{height:{int(44*s)}px!important}}
.payfoot .ch .lg img{{height:{int(14*s)}px!important}}
.payfoot .ch i{{display:none;font-style:normal;font-size:{int(13*s)}px;color:{label};font-weight:700;font-family:Cairo;white-space:nowrap}}
.payfoot .av{{display:flex;flex-direction:column;align-items:center;gap:{int(6*s)}px;font-family:Cairo;font-weight:800;font-size:{int(17*s)}px;color:{text};white-space:nowrap}}
.payfoot .av .chip{{background:#fff;border-radius:{int(30*s)}px;height:{int(46*s)}px;padding:0 {int(14*s)}px;display:flex;align-items:center;box-shadow:0 3px 8px rgba(0,0,0,.12)}}
.payfoot .av .chip img{{height:{int(24*s)}px}}
.payfoot .av .chip.site{{gap:{int(6*s)}px;padding:0 {int(12*s)}px}}
.payfoot .av .chip.site img{{height:{int(20*s)}px}}
.payfoot .av .row{{display:flex;align-items:center;gap:{int(7*s)}px}}
.payfoot .av .site{{background:#fff;border-radius:{int(30*s)}px;height:{int(46*s)}px;padding:0 {int(20*s)}px;display:flex;align-items:center;box-shadow:0 3px 8px rgba(0,0,0,.12);font-family:Poppins;font-weight:700;font-size:{int(24*s)}px;letter-spacing:.3px;color:#51022D;direction:ltr}}
.payfoot .av .chip b{{font-family:Poppins;font-weight:700;font-size:{int(15*s)}px;color:#51022D}}
'''
MARK='file:///home/claude/974-social/posts/2026-11/waterproof/src/mark-c.png'
def html():
    return f'<div class="payfoot"><div class="pills">{PILLS}</div><div class="av"><div class="site">974group.net</div><div class="row"><span>متوفر في</span><div class="chip"><img src="{SNOONU}"></div></div></div></div>'

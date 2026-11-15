/*
  974Group - Elastic Loop Bands: guided "Fits" choice.
  The product has one option "Fits" with 4 values (20mm / Apple Watch Small / Apple Watch Large grey
  connector / Apple Watch Large black connector). This file shows it as steps, placed before Colour:
    1. 20mm watch  or  Apple Watch
    2. (Apple Watch) Small or Large
    3. (Large) Steel or Black connector
  It only drives the theme's own radio buttons, so variants, stock and the cart stay as they are.
  Add to cart is held until the steps are answered. Runs only where a "Fits" option with exactly
  these 4 values exists.
*/
(function () {
  'use strict';
  var AR = (document.documentElement.lang || '').toLowerCase().indexOf('ar') === 0;
  var IMG = window.lxElf || {};
  var T = AR ? {
    q1: 'السير حق شنو؟', o20: 'ساعة 20 ملم', o20s: 'أي ساعة مقاس سيرها 20 ملم', oaw: 'Apple Watch', oaws: 'مع الوصلة',
    q2: 'مقاس Apple Watch', os: 'صغير', oss: '38 – 42 ملم', ol: 'كبير', ols: '44 – 49 ملم · Ultra',
    q3: 'لون الوصلة', steel: 'ستيل', black: 'أسود',
    e1: 'اختر أول: ساعة 20 ملم أو Apple Watch', e2: 'اختر مقاس ساعتك', e3: 'اختر لون الوصلة'
  } : {
    q1: 'What is it for?', o20: '20mm watch', o20s: 'Any watch with a 20mm band', oaw: 'Apple Watch', oaws: 'Connector included',
    q2: 'Apple Watch size', os: 'Small', oss: '38 – 42mm', ol: 'Large', ols: '44 – 49mm · Ultra',
    q3: 'Connector colour', steel: 'Steel', black: 'Black',
    e1: 'Choose first: 20mm watch or Apple Watch', e2: 'Choose your Apple Watch size', e3: 'Choose the connector colour'
  };
  var CSS = '.elf-picker{display:flex;flex-direction:column}.elf-picker>fieldset{min-width:0}.elf-host{order:-1}' +
    '.elf-host>legend,.elf-host>.option-selector__btns{display:none!important}' +
    '.elf__q{display:block;margin:0 0 8px}.elf__sub{margin-top:14px}.elf__sub[hidden],.elf__err[hidden]{display:none}' +
    '.elf__row{display:grid;grid-template-columns:1fr 1fr;gap:10px}' +
    '.elf__opt{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;min-height:64px;margin:0;padding:10px 8px;border:1px solid var(--lx-line,#e7e7ec);border-radius:14px;background:#fff;color:var(--lx-wine,#51022d);font:inherit;text-align:center;cursor:pointer;-webkit-tap-highlight-color:transparent;transition:border-color .15s,box-shadow .15s,background-color .15s}' +
    '.elf__opt b{font-size:14px;font-weight:700;line-height:1.2}.elf__opt small{font-size:11.5px;line-height:1.25;color:var(--lx-muted,#6e6e73)}' +
    '.elf__opt img{display:block;width:100%;max-width:150px;height:auto;margin-bottom:4px}' +
    '.elf__opt.is-on{border-color:var(--lx-wine2,#720842);box-shadow:inset 0 0 0 1px var(--lx-wine2,#720842);background:#fbf6f8}' +
    '.elf__opt:active{transform:scale(.98)}.elf__err{margin:10px 0 0;font-size:12.5px;font-weight:600;color:#e32b2b}' +
    '.elf.is-shake{animation:elfShake .3s 2}@keyframes elfShake{25%{transform:translateX(-4px)}75%{transform:translateX(4px)}}';

  function isFits(fs) {
    var v = [].map.call(fs.querySelectorAll('input.js-option'), function (i) { return i.value; });
    return v.length === 4 && /^20\s*mm/i.test(v[0]) && /Apple Watch Small/i.test(v[1]) &&
      /Apple Watch Large/i.test(v[2]) && /Apple Watch Large/i.test(v[3]);
  }

  function opt(key, val, title, sub, img) {
    return '<button type="button" class="elf__opt" data-k="' + key + '" data-v="' + val + '" aria-pressed="false">' +
      (img ? '<img src="' + img + '" alt="" width="480" height="150" loading="lazy">' : '') +
      '<b>' + title + '</b>' + (sub ? '<small>' + sub + '</small>' : '') + '</button>';
  }

  function setup(picker) {
    if (picker.lxElfDone) return;
    var fs = [].filter.call(picker.querySelectorAll('fieldset.option-selector'), isFits)[0];
    if (!fs) return;
    picker.lxElfDone = true;
    if (!document.getElementById('elf-css')) {
      var st = document.createElement('style'); st.id = 'elf-css'; st.textContent = CSS; document.head.appendChild(st);
    }
    var inputs = fs.querySelectorAll('input.js-option');
    var state = { a: null, b: null, c: null };
    function derive() {
      var i = [].findIndex.call(inputs, function (x) { return x.checked; });
      state = i === 0 ? { a: '20', b: null, c: null } : i === 1 ? { a: 'aw', b: 's', c: null }
        : i === 2 ? { a: 'aw', b: 'l', c: 'steel' } : i === 3 ? { a: 'aw', b: 'l', c: 'black' } : { a: null, b: null, c: null };
    }
    /* a link to a specific variant keeps its choice; otherwise the customer chooses first */
    if (/[?&]variant=/.test(window.location.search) && !picker.closest('quick-add-drawer')) derive();

    var ui = document.createElement('div');
    ui.className = 'elf';
    ui.innerHTML =
      '<span class="label elf__q">' + T.q1 + '</span>' +
      '<div class="elf__row">' + opt('a', '20', T.o20, T.o20s) + opt('a', 'aw', T.oaw, T.oaws) + '</div>' +
      '<div class="elf__sub" data-sub="b" hidden><span class="label elf__q">' + T.q2 + '</span>' +
      '<div class="elf__row">' + opt('b', 's', T.os, T.oss) + opt('b', 'l', T.ol, T.ols) + '</div></div>' +
      '<div class="elf__sub" data-sub="c" hidden><span class="label elf__q">' + T.q3 + '</span>' +
      '<div class="elf__row">' + opt('c', 'steel', T.steel, '', IMG.steel) + opt('c', 'black', T.black, '', IMG.black) + '</div></div>' +
      '<p class="elf__err" role="alert" hidden></p>';
    fs.appendChild(ui);
    fs.classList.add('elf-host');
    picker.classList.add('elf-picker');
    var err = ui.querySelector('.elf__err');

    function index() {
      if (state.a === '20') return 0;
      if (state.a === 'aw' && state.b === 's') return 1;
      if (state.a === 'aw' && state.b === 'l' && state.c === 'steel') return 2;
      if (state.a === 'aw' && state.b === 'l' && state.c === 'black') return 3;
      return -1;
    }
    function missing() {
      if (!state.a) return T.e1;
      if (state.a === 'aw' && !state.b) return T.e2;
      if (state.b === 'l' && !state.c) return T.e3;
      return '';
    }
    function render() {
      ui.querySelectorAll('.elf__opt').forEach(function (b) {
        var on = state[b.dataset.k] === b.dataset.v;
        b.classList.toggle('is-on', on);
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
      });
      ui.querySelector('[data-sub="b"]').hidden = state.a !== 'aw';
      ui.querySelector('[data-sub="c"]').hidden = !(state.a === 'aw' && state.b === 'l');
    }
    var mine = false;
    ui.addEventListener('click', function (e) {
      var b = e.target.closest('.elf__opt');
      if (!b) return;
      var k = b.dataset.k, v = b.dataset.v;
      if (state[k] !== v) {
        state[k] = v;
        if (k === 'a') { state.b = null; state.c = null; }
        if (k === 'b') state.c = null;
      }
      err.hidden = true;
      render();
      var i = index();
      if (i >= 0 && !inputs[i].checked) { mine = true; inputs[i].click(); mine = false; }
    });
    fs.addEventListener('change', function () { if (!mine) { derive(); render(); } });

    function hold(e) {
      var m = missing();
      if (!m) return false;
      e.preventDefault();
      e.stopImmediatePropagation();
      err.textContent = m;
      err.hidden = false;
      ui.classList.remove('is-shake');
      void ui.offsetWidth;
      ui.classList.add('is-shake');
      ui.scrollIntoView({ block: 'center', behavior: 'smooth' });
      return true;
    }
    var section = picker.closest('.js-product') || document;
    section.addEventListener('click', function (e) {
      if (e.target.closest && e.target.closest('[name="add"], .shopify-payment-button, .product-info__dynamic-checkout-button')) hold(e);
    }, true);
    section.addEventListener('submit', function (e) { hold(e); }, true);
    if (!picker.closest('quick-add-drawer')) {
      document.addEventListener('click', function (e) {
        if (e.target.closest && e.target.closest('.pdp-bar__btn')) hold(e);
      }, true);
    }
    render();
  }

  function scan(root) {
    if (root.matches && root.matches('variant-picker')) setup(root);
    if (root.querySelectorAll) root.querySelectorAll('variant-picker').forEach(setup);
  }
  function start() {
    scan(document);
    new MutationObserver(function (muts) {
      muts.forEach(function (m) { m.addedNodes.forEach(function (n) { if (n.nodeType === 1) scan(n); }); });
    }).observe(document.body, { childList: true, subtree: true });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();

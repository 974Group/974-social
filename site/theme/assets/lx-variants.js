/*
  974Group - products with more than 250 variants (e.g. Elastic Loop Bands, 356 variants).
  Shopify gives the theme only the first 250 variants, so the variant picker could not see the
  rest: some colours had no swatch, could not be bought, and every swatch looked sold out.
  This file (1) adds the missing swatches, (2) loads the remaining variants from
  sections/lx-variants.liquid and hands them to the theme's own variant picker.
  It does nothing on products with fewer than 250 variants.
*/
(function () {
  'use strict';
  var LIMIT = 250;

  function repairLabels(picker) {
    picker.querySelectorAll('fieldset.option-selector').forEach(function (fs) {
      var tpl = fs.querySelector('label.opt-label');
      if (!tpl) return;
      fs.querySelectorAll('input.js-option').forEach(function (input) {
        var next = input.nextElementSibling;
        if (next && next.tagName === 'LABEL') return;
        var label = tpl.cloneNode(true);
        label.setAttribute('for', input.id);
        label.removeAttribute('title');
        label.classList.add('lx-late');
        var val = label.querySelector('.js-value') || label.querySelector('span');
        if (val) val.textContent = input.value;
        var img = label.querySelector('img');
        if (img) {
          img.removeAttribute('srcset');
          img.removeAttribute('sizes');
          img.removeAttribute('src');
          img.alt = input.value;
          img.style.opacity = '0';
        }
        if (label.hasAttribute('data-swatch')) label.setAttribute('data-swatch', input.value.toLowerCase());
        input.insertAdjacentElement('afterend', label);
      });
    });
  }

  function fillImages(picker) {
    var variants = picker.data.product.variants;
    picker.querySelectorAll('.option-selector').forEach(function (fs, idx) {
      fs.querySelectorAll('label.lx-late').forEach(function (label) {
        var img = label.querySelector('img');
        var input = label.previousElementSibling;
        if (!img || !input) return;
        var v = variants.find(function (x) {
          return x.options[idx] === input.value && x.featured_media && x.featured_media.preview_image;
        });
        if (!v) return;
        var src = v.featured_media.preview_image.src;
        img.src = src + (src.indexOf('?') > -1 ? '&' : '?') + 'width=160';
        img.style.opacity = '';
      });
    });
  }

  function refresh(picker) {
    try {
      picker.selectedOptions = picker.getSelectedOptions();
      picker.variant = picker.getSelectedVariant();
      picker.preSelection = !picker.variant && picker.selectedOptions.find(function (o) { return o === null; }) === null;
      if (picker.variant) picker.updateVariantInput();
      picker.updateAddToCartButton();
      picker.updateAvailability();
      picker.updatePrice();
    } catch (e) { console.warn('lx-variants refresh', e); }
  }

  function loadRest(picker) {
    var data = picker.data;
    if (!data || !data.product || !data.product.variants || !data.formatted) return;
    if (data.product.variants.length < LIMIT || picker.lxLoading) return;
    picker.lxLoading = true;
    var base = picker.dataset.url || window.location.pathname;

    function page(n) {
      return fetch(base + '?section_id=lx-variants&page=' + n, { credentials: 'same-origin' })
        .then(function (r) {
          if (!r.ok) throw new Error('lx-variants ' + r.status);
          return r.text();
        })
        .then(function (html) {
          var el = new DOMParser().parseFromString(html, 'text/html').querySelector('.js-lx-variants');
          if (!el) return null;
          var more = JSON.parse(el.textContent);
          var have = {};
          data.product.variants.forEach(function (v) { have[v.id] = 1; });
          more.variants.forEach(function (v) { if (!have[v.id]) data.product.variants.push(v); });
          Object.keys(more.formatted).forEach(function (k) { data.formatted[k] = more.formatted[k]; });
          return n < Number(el.dataset.pages || 1) ? page(n + 1) : null;
        });
    }

    page(2)
      .then(function () { fillImages(picker); refresh(picker); })
      .catch(function (e) { picker.lxLoading = false; console.warn(e); });
  }

  function scan(root) {
    var list = [];
    if (root.matches && root.matches('variant-picker')) list.push(root);
    if (root.querySelectorAll) list = list.concat([].slice.call(root.querySelectorAll('variant-picker')));
    list.forEach(function (picker) {
      repairLabels(picker);
      customElements.whenDefined('variant-picker').then(function () {
        setTimeout(function () { loadRest(picker); }, 0);
      });
    });
  }

  /* the theme's helper crashes on an option without a label; make it safe */
  customElements.whenDefined('variant-picker').then(function () {
    var VP = customElements.get('variant-picker');
    var orig = VP.updateOptionAvailability;
    if (typeof orig !== 'function') return;
    VP.updateOptionAvailability = function (el, exists, available) {
      if (!el.classList.contains('custom-select__option') && !el.nextElementSibling) {
        el.classList.toggle('is-unavailable', !available);
        el.classList.toggle('is-nonexistent', !exists);
        return;
      }
      orig.call(VP, el, exists, available);
    };
  });

  function start() {
    scan(document);
    new MutationObserver(function (muts) {
      muts.forEach(function (m) {
        m.addedNodes.forEach(function (n) { if (n.nodeType === 1) scan(n); });
      });
    }).observe(document.body, { childList: true, subtree: true });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();

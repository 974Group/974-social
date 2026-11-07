# Theme copy "974Group – Designy T-shirts" (gid 189840752931), 7 Nov 2026
Duplicated from MAIN "974Group – Device per colour (Navigator)". Owner publishes it.

Changes:
- templates/index.json — new first hero slide (designy-tshirts-desktop/mobile.jpg → /collections/t-shirts); new category group "Designy" with tile "T-shirts" (designy-tshirts-tile.jpg).
- templates/collection.tshirts.json — collection page shows the collection image full width, no title/description (the image carries them). Assigned to collections t-shirts and designy (templateSuffix, store-level).
- snippets/pdp-tee-size.liquid — height/weight size finder for Designy tees (vendor Designy Studios or type T-shirt). Weight bands S<60, M<73, L<86, XL; +1 size if height ≥184, −1 if ≤164 (lower half of band); fit choice ±1; "between sizes" hint near band edges. Button selects the size radio.
- snippets/pdp-size-help.liquid — renders pdp-tee-size for Designy tees.

# PDF

## Online tools

- <https://pdfux.com/>

## Compare PDF

- <https://draftable.com/compare>
- <https://parepdf.com/>
- <https://vslavik.github.io/diff-pdf/>
- <https://www.qtrac.eu/diffpdf.html>
- <https://www.qtrac.eu/diffpdf-foss.html>
- <https://gitlab.com/eang/diffpdf>

## Make PDF looks scanned

Make your pdf look scanned: <https://news.ycombinator.com/item?id=23157408>

Works well (edge or chrome): <https://lookscanned.io/>

- just do some tests with a dumb pdf so that it caches the javascript code locally, then unplug, then try with real pdf
- meh on firefox: <https://github.com/rwv/lookscanned.io/issues/4>

Manually:

```bash
convert -density 150 document_origine.pdf -colorspace gray +noise Gaussian -rotate 2 -depth 2 document_modifie.pdf

convert letter.pdf -colorspace gray \( +clone -blur 0x1 \) +swap -compose divide -composite -linear-stretch 5%x0% -rotate 1.5 as-scanned.pdf

convert letter.pdf \( +clone -blur 0x1 \) +swap -compose divide -composite -gamma 0.1 -linear-stretch 5%x0% -rotate 1.5 as-scanned.pdf

convert -density 150 input.pdf -colorspace gray -linear-stretch 3.5%x10% -blur 0x0.5 -attenuate 0.25 +noise Gaussian output.pdf
```

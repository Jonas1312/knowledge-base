# PDF

## Online tools

- https://pdfux.com/

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

## Watermark

Make sure you have Ghostscript ≥9.24:

```bash
gs --version
```

If yes, just remove this whole following section from /etc/ImageMagick-6/policy.xml:

```bash
<!-- disable ghostscript format types -->
<policy domain="coder" rights="none" pattern="PS" />
<policy domain="coder" rights="none" pattern="PS2" />
<policy domain="coder" rights="none" pattern="PS3" />
<policy domain="coder" rights="none" pattern="EPS" />
<policy domain="coder" rights="none" pattern="PDF" />
<policy domain="coder" rights="none" pattern="XPS" />
```

```bash
convert -density 100 -background None -fill "rgba(100, 100, 100, 0.25)" -pointsize 9 label:"mon_texte" -rotate -20 +repage +write mpr:TILE +delete document_origine.pdf -alpha set \( +clone -fill mpr:TILE -draw "color 0,0 reset" \) -composite document_modifie.pdf
```

```bash
convert -density 100 document_origine.pdf \
\( -size 100x -background none -fill "rgba(100, 100, 100, 0.25)" -gravity center \
label:"watermark" -trim -rotate -30 \
-bordercolor none -border 10 \
-write mpr:wm +delete \
+clone -fill mpr:wm  -draw 'color 0,0 reset' \) \
-compose over -composite \
document_modifie.pdf
```

Also consider using `-density 100` or even `-density 75` for long text documents. Using a density of 75 dpi produces documents that are 4x smaller than 150 dpi (75²=150²/4) and doesn't affect the readability of normal-sized (10-12pt) text that much.

# Watermark

## Online tools

<https://filigrane.beta.gouv.fr/>

## Offline tools

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

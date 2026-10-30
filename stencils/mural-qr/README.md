# Mural QR stencil

**20-inch version:** see 20in/. The code itself is exactly 20 in square; with its 4-module white border the sheet is 25.52 in square. CUT (outline, hairline 0.25 pt) and PRINT (solid) as PDF and SVG; the SVGs are sized in inches for Cricut or laser software.

**Use the QRCG Level H files (Mural_QR_QRCG_H_*).** They come from QRCG's own Level H export (Mural_Project_QR_Code.eps, 3000 pt), so the wall matches the company's official code. The earlier self-generated Level H set (different mask pattern, same link) is kept in level-H-self-generated/.

Earlier note: They encode the same link, https://qrco.de/bh3jJQ, at the highest error correction (about 30% recoverable), 29 x 29 modules. The QRCG SVG download was still Level L, so the H version was generated from the same link with segno; QRCG still tracks scans and the link can still be repointed. The first Level L stencil is kept in level-L-original/.

Made with QR_STENCILER by Golan Levin and Asa Foster III (FFFFF.AT), https://github.com/golanlevin/QR_STENCILER, run unmodified apart from a headless file input.

- Level L original: decoded from Mural_Project_QR_Code-01.eps, 25 x 25 modules. Level H: 29 x 29 modules. Both have a 4-module quiet zone.
- **CUT files** are the stenciler's own output: hairline cut paths for a laser cutter, Cricut or plotter. Black is cut away; you spray or roll dark paint through the holes.
- **PRINT files** are the same shapes filled solid black, for printing on cardstock or mylar and cutting by hand with a knife. Cut out the black.
- Floating pieces (the centers of the three corner squares and every enclosed white area) are held in by thin bridges, so the stencil stays in one piece. The bridges leave hairline gaps in the painted code; it still scans (tested at full and quarter resolution).
- Sizes: the 10.3 in (H) and 9.2 in (L) files are the native output; the letter files put the code at 8 in on a US Letter page. Both are vector and scale to any size. Keep the white border when you scale; it is part of the code.
- Before painting the mural, test-spray on cardboard and scan it with a phone.

Rebuild: `python3 tool/pde2java.py <QR_STENCILER dir> QR_STENCILER.java`, compile against Processing 3.3.7 core, pdf, iText 2.1.7 and controlP5, then run `java -Dqr=<png> [-Dfilled=1] QR_STENCILER` under a display (xvfb-run).

QR_STENCILER is licensed CC BY-NC-SA 3.0 (the software); credit FFFFF.AT.

# Mural QR stencil

Made with QR_STENCILER by Golan Levin and Asa Foster III (FFFFF.AT), https://github.com/golanlevin/QR_STENCILER, run unmodified apart from a headless file input.

- The code reads `https://qrco.de/bh3jJQ` (decoded from Mural_Project_QR_Code-01.eps). 25 x 25 modules plus a 4-module quiet zone.
- **CUT files** are the stenciler's own output: hairline cut paths for a laser cutter, Cricut or plotter. Black is cut away; you spray or roll dark paint through the holes.
- **PRINT files** are the same shapes filled solid black, for printing on cardstock or mylar and cutting by hand with a knife. Cut out the black.
- Floating pieces (the centers of the three corner squares and every enclosed white area) are held in by thin bridges, so the stencil stays in one piece. The bridges leave hairline gaps in the painted code; it still scans (tested at full and quarter resolution).
- Sizes: the 9.2 in files are the native output; the letter files put the code at 8 in on a US Letter page. Both are vector and scale to any size. Keep the white border when you scale; it is part of the code.
- Before painting the mural, test-spray on cardboard and scan it with a phone.

Rebuild: `python3 tool/pde2java.py <QR_STENCILER dir> QR_STENCILER.java`, compile against Processing 3.3.7 core, pdf, iText 2.1.7 and controlP5, then run `java -Dqr=<png> [-Dfilled=1] QR_STENCILER` under a display (xvfb-run).

QR_STENCILER is licensed CC BY-NC-SA 3.0 (the software); credit FFFFF.AT.

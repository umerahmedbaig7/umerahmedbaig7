#!/usr/bin/env python3
"""Make images the same size so they line up side by side in a GitHub README table.

GitHub strips CSS (object-fit, fixed heights, etc.), so two images with different aspect ratios
always render at different heights. The reliable fix is to give every image in a row the SAME
aspect ratio: this script scales each image to fit inside a common canvas and fills the rest
with the image's own background colour, so nothing is cropped or distorted.

Usage:
  python scripts/normalize_images.py a.png b.png --out assets/gallery
  python scripts/normalize_images.py a.png b.png c.png --aspect 1.9 --out assets/gallery

Then use the printed paths in the README with width="100%" (and NO height attribute):
  <td width="50%"><img src="assets/gallery/a.jpg" width="100%" alt="..."></td>
"""
import argparse
import os
import statistics
from PIL import Image


def edge_colour(im):
    """Median colour of the 1-pixel border: a good guess for the image background."""
    w, h = im.size
    px = im.load()
    pts = [px[x, 0] for x in range(0, w, max(1, w // 60))] + [px[x, h - 1] for x in range(0, w, max(1, w // 60))] \
        + [px[0, y] for y in range(0, h, max(1, h // 60))] + [px[w - 1, y] for y in range(0, h, max(1, h // 60))]
    return tuple(int(statistics.median(p[i] for p in pts)) for i in range(3))


def letterbox(path, out_dir, aspect, width=1400, quality=92):
    im = Image.open(path).convert("RGB")
    cw, ch = width, round(width / aspect)
    scale = min(cw / im.width, ch / im.height) * 0.98          # 2% breathing room
    nw, nh = round(im.width * scale), round(im.height * scale)
    canvas = Image.new("RGB", (cw, ch), edge_colour(im))
    canvas.paste(im.resize((nw, nh), Image.LANCZOS), ((cw - nw) // 2, (ch - nh) // 2))
    os.makedirs(out_dir, exist_ok=True)
    name = os.path.splitext(os.path.basename(path))[0].replace(" ", "-").lower() + ".jpg"
    dst = os.path.join(out_dir, name)
    canvas.save(dst, quality=quality, subsampling=0, optimize=True)
    return dst


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("images", nargs="+")
    ap.add_argument("--out", default="assets/gallery")
    ap.add_argument("--aspect", type=float, default=None, help="canvas width/height (default: average of the inputs, clamped 1.2-2.2)")
    ap.add_argument("--width", type=int, default=1400)
    a = ap.parse_args()
    ratios = [Image.open(p).width / Image.open(p).height for p in a.images]
    aspect = a.aspect or min(2.2, max(1.2, sum(ratios) / len(ratios)))
    for p in a.images:
        print(letterbox(p, a.out, aspect, a.width))

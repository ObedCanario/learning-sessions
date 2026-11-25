"""Generate a 3000x3000 cover.jpg (Apple requires 1400-3000px square).
Usage: make_cover.py [SHOW_FOLDER] [--subtitle TEXT] [--colors R,G,B:R,G,B]"""
import json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

args = [a for a in sys.argv[1:]]
subtitle = ""
if "--subtitle" in args:
    i = args.index("--subtitle"); subtitle = args[i + 1]; del args[i:i + 2]
if "--colors" in args:
    i = args.index("--colors"); del args[i:i + 2]
root = Path(__file__).resolve().parent / (args[0] if args else "")
title = json.loads((root / "podcast.json").read_text())["title"]
S = 3000
img = Image.new("RGB", (S, S))
d = ImageDraw.Draw(img)
top, bot = ((24, 40, 72), (196, 120, 48)) if not args else ((18, 18, 22), (120, 92, 52))
if "--colors" in sys.argv:
    top, bot = (tuple(int(v) for v in c.split(",")) for c in sys.argv[sys.argv.index("--colors") + 1].split(":"))
for y in range(S):
    t = y / S
    d.line([(0, y), (S, y)], fill=tuple(int(a + (b - a) * t) for a, b in zip(top, bot)))
font_path = "/System/Library/Fonts/Avenir Next.ttc"
words, lines, cur = title.split(), [], ""
font = ImageFont.truetype(font_path, 330, index=2)
for w in words:
    test = (cur + " " + w).strip()
    if d.textlength(test, font=font) > S * 0.8 and cur:
        lines.append(cur); cur = w
    else:
        cur = test
lines.append(cur)
lh = 400
y = S // 2 - lh * len(lines) // 2
for ln in lines:
    d.text((S // 2, y), ln, font=font, fill=(250, 245, 235), anchor="mt"); y += lh
d.rectangle([S * 0.4, y + 80, S * 0.6, y + 100], fill=(250, 245, 235))
if subtitle:
    sf = ImageFont.truetype(font_path, 150, index=0)
    d.text((S // 2, y + 220), subtitle, font=sf, fill=(250, 245, 235), anchor="mt")
img.save(root / "cover.jpg", quality=88)
print("cover.jpg written")

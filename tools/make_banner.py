#!/usr/bin/env python3
"""Profile banner — strict-slice Z-Grid logo, official slogan, no redraw."""
from PIL import Image, ImageDraw, ImageFont
W, H = 2400, 800
BG = (7, 17, 31)
WHITE = (247, 250, 255)
GRAY = (148, 163, 184)
CYAN = (56, 189, 248)
BLUE = (37, 99, 235)
AMBER = (251, 191, 36)
GREEN = (52, 211, 153)
CORAL = (251, 113, 133)
F = "/usr/local/share/fonts/inter/Inter.ttf"
import os
if not os.path.exists(F):
    F = "/root/.local/share/fonts/Inter.ttf"
INTER = "/root/.local/share/fonts/Inter.ttf"
CJK = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
CJK_B = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
SERIF_I = "/usr/share/fonts/truetype/noto/NotoSerifDisplay-BoldItalic.ttf"
def font(path, size, idx=0):
    try: return ImageFont.truetype(path, size, index=idx)
    except Exception: return ImageFont.truetype(path, size)

im = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(im)
# subtle grid dots
for y in range(0, H, 32):
    for x in range(0, W, 32):
        d.point((x, y), fill=(17, 39, 66))
# right-side system map panel
d.line([(1700, 170), (1700, 640)], fill=(50, 70, 96), width=2)
d.text((1750, 180), "SYSTEM MAP", font=font(INTER, 26), fill=GRAY)
f_dir = font(INTER, 26); d.text((2280, 180), "04 / DIRECTIONS", font=f_dir, fill=GRAY, anchor="ra")
d.line([(1750, 228), (2280, 228)], fill=(50, 70, 96), width=2)
items = [("01", "BUILD", "构建系统", CYAN), ("02", "THINK", "工程知识", AMBER),
         ("03", "MEASURE", "量化生活", GREEN), ("04", "CREATE", "创造作品", CORAL)]
for i, (no, en, zh, col) in enumerate(items):
    y = 270 + i * 82
    d.text((1750, y), no, font=font(INTER, 30), fill=GRAY)
    d.text((1810, y - 4), en, font=font(INTER, 42), fill=col)
    d.text((2210, y + 6), zh, font=font(CJK, 28), fill=(190, 205, 225))
    d.line([(1750, y + 62), (2280, y + 62)], fill=(38, 56, 78), width=1)
# top: strict-sliced symbol (no redraw) + wordmark
sym = Image.open("/oc/zhubao-pages/public/brand/slices/symbol-panel.png").convert("RGB")
sym = sym.resize((60, 50), Image.LANCZOS)
im.paste(sym, (100, 58))
d.text((180, 62), "ZHUBAO / PERSONAL DIGITAL PORTFOLIO", font=font(INTER, 28), fill=WHITE)
d.text((1930, 62), "BEIJING · UTC+8 · 2026", font=font(INTER, 28), fill=GRAY)
d.line([(100, 140), (2300, 140)], fill=(45, 66, 92), width=2)
# main official slogan, direction colors restrained
d.text((100, 196), "AI SYSTEMS · KNOWLEDGE ENGINEERING · QUANTIFIED LIFE · CREATIVE WORK",
       font=font(INTER, 28), fill=GRAY)
y = 250
for parts in [
    [("Build ", WHITE), ("Systems.", CYAN)],
    [("Engineer ", WHITE), ("Knowledge.", AMBER)],
    [("Measure ", WHITE), ("Life. ", GREEN), ("Create ", WHITE), ("Things.", CORAL)],
]:
    x = 100
    for txt, col in parts:
        d.text((x, y), txt, font=font(INTER, 94), fill=col)
        x += d.textlength(txt, font=font(INTER, 94))
    y += 124
d.text((100, 650), "构建系统 · 工程知识 · 量化生活 · 创造作品", font=font(CJK, 40), fill=(203, 214, 230))
# footer
d.line([(100, 726), (2300, 726)], fill=(45, 66, 92), width=2)
d.text((100, 746), "ZHUBAO.GITHUB.IO", font=font(INTER, 26), fill=AMBER)
d.text((940, 746), "CIS 1.0 · MIDNIGHT SIGNAL · STRICT SLICE LOGO", font=font(INTER, 24), fill=GRAY)
d.text((1960, 746), "BUILDING IN PUBLIC", font=font(INTER, 24), fill=GRAY)
im.save("/oc/zb-profile/assets/profile-banner.png")
print("banner written", im.size)

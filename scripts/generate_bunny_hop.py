#!/usr/bin/env python3
"""Light full-width bunny hop strip for profile README."""

from math import sin, pi
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1000, 72
FRAMES = 36
BG = "#fafafa"
LINE = "#e8e8e8"


def font(size: int) -> ImageFont.ImageFont:
    for name in ("Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def hop(t: int) -> int:
    return int(abs(sin((t % 10) / 10 * pi)) * 14)


def frame(t: int, f_big: ImageFont.ImageFont, f_sm: ImageFont.ImageFont) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw.line((24, H - 18, W - 24, H - 18), fill=LINE, width=1)
    x = 40 + int((t / (FRAMES - 1)) * (W - 120))
    y = H - 42 - hop(t)
    bunny = "🐰" if t % 4 < 2 else "🐇"
    draw.text((x, y), bunny, font=f_big, embedded_color=True)
    if hop(t) < 3:
        draw.text((x + 28, y - 4), "·", fill="#d0d0d0", font=f_sm)
    return img


def main() -> None:
    out = Path(__file__).resolve().parent.parent / "assets" / "bunny-hop.gif"
    out.parent.mkdir(exist_ok=True)
    frames = [frame(t, font(36), font(16)) for t in range(FRAMES)]
    frames[0].save(out, save_all=True, append_images=frames[1:], duration=80, loop=0, optimize=True)
    print(f"Wrote {out} ({out.stat().st_size // 1024}KB)")


if __name__ == "__main__":
    main()

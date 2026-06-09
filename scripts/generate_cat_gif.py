#!/usr/bin/env python3
"""Generate looping office-cat GIF — laser pointer chaos."""

from math import sin
from pathlib import Path

from PIL import Image, ImageDraw

W, H = 720, 130
FRAMES = 48
BG = "#0f1419"
ACCENT = "#30363d"


def draw_desk(draw: ImageDraw.ImageDraw) -> None:
    draw.rounded_rectangle((10, 10, W - 10, H - 10), radius=16, outline=ACCENT, width=1)
    draw.rectangle((24, 78, W - 24, 96), fill="#1c2128")
    # laptop
    draw.rectangle((44, 52, 118, 78), fill="#2d333b", outline="#484f58")
    draw.rectangle((50, 56, 112, 72), fill="#58a6ff", outline="#1f6feb")
    draw.polygon([(40, 78), (122, 78), (128, 86), (34, 86)], fill="#3d444d")
    draw.text((24, 16), "office cat cam · live · not a commit graph", fill="#8b949e")


def draw_cat(draw: ImageDraw.ImageDraw, x: int, y: int, phase: str, t: int) -> None:
    """phase: sleep | stare | pounce | dizzy"""
    bob = int(sin(t / 4) * 2)
    orange = "#f4a261"
    stripe = "#e76f51"
    cream = "#ffe8d6"

    if phase == "sleep":
        y += 4
        draw.ellipse((x - 22, y - 10, x + 22, y + 18), fill=orange)
        draw.ellipse((x - 18, y - 8, x + 18, y + 14), fill=cream)
        # closed eyes
        draw.line((x - 10, y + 2, x - 4, y + 2), fill="#333", width=2)
        draw.line((x + 4, y + 2, x + 10, y + 2), fill="#333", width=2)
        # ears
        draw.polygon([(x - 16, y - 12), (x - 8, y - 24), (x - 2, y - 10)], fill=orange)
        draw.polygon([(x + 2, y - 10), (x + 8, y - 24), (x + 16, y - 12)], fill=orange)
        # zzz
        zy = y - 20 - (t % 8)
        draw.text((x + 26, zy), "z" * (1 + t % 3), fill="#8b949e")
        return

    if phase == "stare":
        draw.ellipse((x - 24, y - 12 + bob, x + 24, y + 20 + bob), fill=orange)
        draw.ellipse((x - 20, y - 8 + bob, x + 20, y + 16 + bob), fill=cream)
        draw.polygon([(x - 18, y - 14 + bob), (x - 8, y - 28 + bob), (x - 2, y - 12 + bob)], fill=orange)
        draw.polygon([(x + 2, y - 12 + bob), (x + 8, y - 28 + bob), (x + 18, y - 14 + bob)], fill=orange)
        # wide eyes
        draw.ellipse((x - 12, y - 2 + bob, x - 4, y + 6 + bob), fill="#fff")
        draw.ellipse((x + 4, y - 2 + bob, x + 12, y + 6 + bob), fill="#fff")
        draw.ellipse((x - 9, y + 1 + bob, x - 6, y + 4 + bob), fill="#222")
        draw.ellipse((x + 6, y + 1 + bob, x + 9, y + 4 + bob), fill="#222")
        # tail twitch
        tx = x + 24 + int(sin(t / 2) * 8)
        draw.line((x + 20, y + 10, tx, y - 4), fill=stripe, width=4)
        return

    if phase == "pounce":
        lean = (t % 6) * 4
        draw.ellipse((x - 26 - lean, y - 6, x + 20, y + 22), fill=orange)
        draw.ellipse((x - 22 - lean, y - 2, x + 16, y + 18), fill=cream)
        draw.polygon([(x - 20 - lean, y - 10), (x - 10 - lean, y - 26), (x - 4 - lean, y - 8)], fill=orange)
        draw.polygon([(x + 0, y - 8), (x + 6, y - 26), (x + 16, y - 10)], fill=orange)
        # excited eyes
        draw.ellipse((x - 14 - lean, y, x - 6 - lean, y + 8), fill="#fff")
        draw.ellipse((x + 2, y, x + 10, y + 8), fill="#fff")
        # paws up
        draw.ellipse((x + 18 + lean, y + 8, x + 30 + lean, y + 20), fill=cream)
        draw.ellipse((x - 8 - lean, y + 10, x + 4 - lean, y + 22), fill=cream)
        draw.text((x + 32 + lean, y - 8), "!!", fill="#ff7b72")
        return

    # dizzy
    draw.ellipse((x - 22, y - 4, x + 22, y + 20), fill=orange)
    draw.ellipse((x - 18, y, x + 18, y + 16), fill=cream)
    draw.text((x - 8, y + 2), "x x", fill="#333")
    draw.arc((x - 30, y - 20, x + 10, y + 10), 0, 300, fill="#8b949e", width=2)


def draw_laser(draw: ImageDraw.ImageDraw, x: int, y: int, on: bool) -> None:
    if not on:
        return
    draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill="#ff3b3b")
    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill="#ffb4b4")
    # tiny glow
    draw.ellipse((x - 8, y - 8, x + 8, y + 8), outline="#ff3b3b")


def draw_mug(draw: ImageDraw.ImageDraw, x: int, y: int, tipped: bool) -> None:
    if tipped:
        draw.ellipse((x, y + 8, x + 28, y + 20), fill="#6e7681")
        for i in range(4):
            draw.ellipse((x + 10 + i * 8, y + 18 + i * 2, x + 14 + i * 8, y + 24 + i * 2), fill="#8b5a2b")
    else:
        draw.rectangle((x, y, x + 22, y + 18), fill="#6e7681", outline="#484f58")
        draw.arc((x + 18, y + 4, x + 30, y + 16), 270, 90, fill="#6e7681", width=3)
        draw.text((x + 4, y + 4), "☕", fill="#0f1419")


def frame(t: int) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw_desk(draw)

    # laser path
    laser_x = 180 + int((sin(t / 5) * 0.5 + 0.5) * 420)
    laser_y = 58 + int(sin(t / 3) * 12)

    cat_x = 560
    cat_y = 58

    if t < 12:
        phase = "sleep"
        draw_laser(draw, laser_x, laser_y, on=False)
        draw_mug(draw, 150, 44, tipped=False)
    elif t < 22:
        phase = "stare"
        draw_laser(draw, laser_x, laser_y, on=True)
        draw_mug(draw, 150, 44, tipped=False)
    elif t < 36:
        phase = "pounce"
        cat_x = 560 - (t - 22) * 18
        draw_laser(draw, laser_x, laser_y, on=True)
        if t > 32:
            draw_mug(draw, 140, 44, tipped=True)
        else:
            draw_mug(draw, 150, 44, tipped=False)
    else:
        phase = "dizzy"
        cat_x = 320
        draw_laser(draw, laser_x, laser_y, on=False)
        draw_mug(draw, 140, 44, tipped=True)

    draw_cat(draw, cat_x, cat_y, phase, t)
    return img


def main() -> None:
    out = Path(__file__).resolve().parent.parent / "assets" / "office-cat.gif"
    out.parent.mkdir(exist_ok=True)
    frames = [frame(t) for t in range(FRAMES)]
    frames[0].save(
        out,
        save_all=True,
        append_images=frames[1:],
        duration=95,
        loop=0,
        optimize=True,
    )
    print(f"Wrote {out} ({len(frames)} frames, {W}x{H})")


if __name__ == "__main__":
    main()

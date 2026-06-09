#!/usr/bin/env python3
"""Generate full-width office cat GIF — laser chaos across the whole desk."""

from math import sin
from pathlib import Path

from PIL import Image, ImageDraw

W, H = 980, 220
FRAMES = 56
BG = "#0d1117"
PANEL = "#161b22"
LINE = "#30363d"


def draw_scene(draw: ImageDraw.ImageDraw, t: int) -> tuple[int, str]:
    draw.rounded_rectangle((0, 0, W - 1, H - 1), radius=18, fill=PANEL, outline=LINE, width=2)
    draw.rectangle((20, 150, W - 20, 172), fill="#21262d")  # desk
    draw.rectangle((20, 18, W - 20, 42), fill="#0d1117", outline=LINE)
    draw.text((32, 24), "🐱 office cat cam  ·  LIVE  ·  definitely not github contributions", fill="#8b949e")

    # monitor + keyboard zone
    draw.rounded_rectangle((36, 72, 200, 148), fill="#2d333b", outline="#484f58", radius=6)
    draw.rectangle((48, 84, 188, 128), fill="#1f6feb")
    draw.text((70, 98), "{ code }", fill="#c9d1d9")
    draw.rectangle((52, 132, 184, 144), fill="#3d444d")

    # plant
    draw.rectangle((W - 90, 118, W - 70, 150), fill="#6e4c2a")
    draw.ellipse((W - 104, 88, W - 56, 124), fill="#3fb950")
    draw.ellipse((W - 98, 78, W - 62, 108), fill="#2ea043")

    # fish bowl
    draw.ellipse((W - 200, 108, W - 140, 152), outline="#58a6ff", width=2)
    draw.ellipse((W - 178, 126, W - 170, 134), fill="#ff7b72")

    laser_x = 220 + int((sin(t / 4.5) * 0.5 + 0.5) * (W - 360))
    laser_y = 108 + int(sin(t / 3.2) * 28)

    if t < 14:
        phase = "sleep"
        cat_x = W - 240
    elif t < 26:
        phase = "stare"
        cat_x = W - 240
    elif t < 44:
        phase = "pounce"
        cat_x = max(260, W - 240 - (t - 26) * 28)
    else:
        phase = "dizzy"
        cat_x = 300 + int(sin(t) * 6)

    # mug
    mug_x = 230
    tipped = t >= 40
    if tipped:
        draw.ellipse((mug_x, 128, mug_x + 36, 148), fill="#6e7681")
        for i in range(5):
            draw.ellipse((mug_x + 8 + i * 10, 140 + i * 3, mug_x + 14 + i * 10, 150 + i * 3), fill="#8b5a2b")
    else:
        draw.rounded_rectangle((mug_x, 108, mug_x + 30, 138), radius=4, fill="#6e7681")
        draw.text((mug_x + 6, 112), "☕", fill="#0d1117")

    if phase != "sleep":
        draw.ellipse((laser_x - 7, laser_y - 7, laser_x + 7, laser_y + 7), fill="#ff3b3b")
        draw.ellipse((laser_x - 12, laser_y - 12, laser_x + 12, laser_y + 12), outline="#ff7b72", width=2)

    draw_cat(draw, cat_x, 118, phase, t)
    return cat_x, phase


def draw_cat(draw: ImageDraw.ImageDraw, x: int, y: int, phase: str, t: int) -> None:
    scale = 1.35
    o, c, s = "#f4a261", "#ffe8d6", "#e76f51"
    bob = int(sin(t / 3) * 3)

    def ear(px: int, py: int) -> None:
        draw.polygon([(px - 22, py - 18), (px - 10, py - 44), (px - 2, py - 16)], fill=o)
        draw.polygon([(px + 2, py - 16), (px + 10, py - 44), (px + 22, py - 18)], fill=o)

    if phase == "sleep":
        draw.ellipse((x - 34, y - 18, x + 34, y + 30), fill=o)
        draw.ellipse((x - 28, y - 12, x + 28, y + 24), fill=c)
        ear(x, y)
        draw.line((x - 14, y + 4, x - 4, y + 4), fill="#333", width=3)
        draw.line((x + 4, y + 4, x + 14, y + 4), fill="#333", width=3)
        draw.text((x + 40, y - 30 - (t % 10)), "z" * (1 + (t % 3)), fill="#8b949e")
        draw.text((x - 70, y + 36), "😴 napping on prod duties", fill="#8b949e")
        return

    if phase == "stare":
        draw.ellipse((x - 36, y - 20 + bob, x + 36, y + 32 + bob), fill=o)
        draw.ellipse((x - 30, y - 14 + bob, x + 30, y + 26 + bob), fill=c)
        ear(x, y + bob)
        for ex in (-14, 6):
            draw.ellipse((x + ex, y - 4 + bob, x + ex + 12, y + 8 + bob), fill="#fff")
            draw.ellipse((x + ex + 4, y + 1 + bob, x + ex + 7, y + 5 + bob), fill="#222")
        tail = x + 38 + int(sin(t / 2) * 14)
        draw.line((x + 32, y + 14, tail, y - 10), fill=s, width=6)
        draw.text((x - 80, y + 40), "👀 laser detected", fill="#ffa657")
        return

    if phase == "pounce":
        lean = (t % 8) * 5
        draw.ellipse((x - 40 - lean, y - 10, x + 30, y + 34), fill=o)
        draw.ellipse((x - 34 - lean, y - 4, x + 24, y + 28), fill=c)
        ear(x - lean, y)
        draw.ellipse((x - 18 - lean, y + 4, x - 4 - lean, y + 16), fill="#fff")
        draw.ellipse((x + 6, y + 4, x + 20, y + 16), fill="#fff")
        draw.ellipse((x + 34 + lean, y + 10, x + 54 + lean, y + 30), fill=c)
        draw.ellipse((x - 10 - lean, y + 14, x + 10 - lean, y + 34), fill=c)
        draw.text((x + 50, y - 20), "⚡ POUNCE", fill="#ff7b72")
        return

    draw.ellipse((x - 34, y - 6, x + 34, y + 32), fill=o)
    draw.ellipse((x - 28, y, x + 28, y + 26), fill=c)
    ear(x, y)
    draw.text((x - 12, y + 8), "× ×", fill="#333")
    draw.arc((x - 50, y - 40, x + 20, y + 10), 0, 300, fill="#8b949e", width=3)
    draw.text((x - 90, y + 40), "☕ knocked over coffee · no regrets", fill="#8b949e")


def frame(t: int) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw_scene(draw, t)
    return img


def main() -> None:
    out = Path(__file__).resolve().parent.parent / "assets" / "office-cat.gif"
    out.parent.mkdir(exist_ok=True)
    frames = [frame(t) for t in range(FRAMES)]
    frames[0].save(out, save_all=True, append_images=frames[1:], duration=85, loop=0, optimize=True)
    print(f"Wrote {out} ({W}x{H}, {len(frames)} frames)")


if __name__ == "__main__":
    main()

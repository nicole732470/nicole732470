#!/usr/bin/env python3
"""Small light-theme cat walking GIF for GitHub profile README."""

from pathlib import Path

from PIL import Image, ImageDraw

W, H = 520, 88
FRAMES = 32
BG = "#fff8f3"
GROUND = "#f4d4b8"
LINE = "#f4a261"
ORANGE = "#f4a261"
CREAM = "#ffe8d6"
PINK = "#e76f51"


def draw_ground(draw: ImageDraw.ImageDraw) -> None:
    draw.rectangle((0, 0, W, H), fill=BG)
    draw.rounded_rectangle((8, 8, W - 8, H - 8), radius=14, outline=LINE, width=2)
    draw.rectangle((20, 62, W - 20, 68), fill=GROUND)
    for x in range(28, W - 20, 36):
        draw.ellipse((x, 70, x + 8, 76), fill="#edd5bc")


def paw_offset(t: int) -> tuple[int, int]:
    cycle = t % 8
    if cycle in (0, 4):
        return 0, 0
    if cycle in (1, 5):
        return 3, -2
    if cycle in (2, 6):
        return 0, -1
    return -3, -2


def draw_cat(draw: ImageDraw.ImageDraw, x: int, t: int) -> None:
    y = 34
    bob = (t % 4) // 2
    fx, fy = paw_offset(t)

    # tail swish
    tail = 10 + (t % 6) * 2
    draw.line((x + 26, y + 14, x + 26 + tail, y - 2 + (t % 3)), fill=PINK, width=4)

    # body
    draw.ellipse((x - 4, y + bob, x + 28, y + 28 + bob), fill=ORANGE)
    draw.ellipse((x, y + 4 + bob, x + 24, y + 24 + bob), fill=CREAM)

    # head
    draw.ellipse((x + 14, y - 10 + bob, x + 44, y + 16 + bob), fill=ORANGE)
    draw.ellipse((x + 18, y - 6 + bob, x + 40, y + 12 + bob), fill=CREAM)
    draw.polygon([(x + 20, y - 8 + bob), (x + 24, y - 20 + bob), (x + 28, y - 8 + bob)], fill=ORANGE)
    draw.polygon([(x + 32, y - 8 + bob), (x + 36, y - 20 + bob), (x + 40, y - 8 + bob)], fill=ORANGE)

    # face
    draw.ellipse((x + 24, y + bob, x + 30, y + 6 + bob), fill="#333")
    draw.ellipse((x + 34, y + bob, x + 40, y + 6 + bob), fill="#333")
    draw.arc((x + 28, y + 6 + bob, x + 38, y + 12 + bob), 10, 170, fill=PINK, width=2)

    # paws
    draw.ellipse((x + 2 + fx, y + 22 + bob, x + 10 + fx, y + 30 + bob + fy), fill=CREAM)
    draw.ellipse((x + 16 - fx, y + 22 + bob, x + 24 - fx, y + 30 + bob - fy), fill=CREAM)

    # tiny sparkles when walking
    if t % 6 == 0:
        draw.text((x - 12, y + 8), "✨", fill=PINK)


def frame(t: int) -> Image.Image:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    draw_ground(draw)
    x = -50 + int((t / (FRAMES - 1)) * (W + 100))
    draw_cat(draw, x, t)
    draw.text((24, 18), "🐾  cat on duty  ·  mrow ~", fill=PINK)
    return img


def main() -> None:
    out = Path(__file__).resolve().parent.parent / "assets" / "cat-walk.gif"
    out.parent.mkdir(exist_ok=True)
    frames = [frame(t) for t in range(FRAMES)]
    frames[0].save(out, save_all=True, append_images=frames[1:], duration=90, loop=0, optimize=True)
    print(f"Wrote {out} ({W}x{H}, {len(frames)} frames, {out.stat().st_size // 1024}KB)")


if __name__ == "__main__":
    main()

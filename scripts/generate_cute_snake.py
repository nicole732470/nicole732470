#!/usr/bin/env python3
"""Generate a looping cute snake GIF (not tied to GitHub contributions)."""

from pathlib import Path

from PIL import Image, ImageDraw

W, H = 480, 100
FRAMES = 40
DOTS = [(60 + i * 28, 50) for i in range(12)]
COLORS = ["#ffb7c5", "#ffd6a5", "#fdffb6", "#caffbf", "#9bf6ff", "#a0c4ff"]
SNAKE = ["#ff6b9d", "#ff8fab", "#ffa6c1", "#ffb3d1"]


def draw_frame(t: int) -> Image.Image:
    img = Image.new("RGB", (W, H), "#0f1419")
    draw = ImageDraw.Draw(img)
    # soft border
    draw.rounded_rectangle((8, 8, W - 8, H - 8), radius=14, outline="#30363d", width=1)

    # candy dots (not contribution data)
    for i, (x, y) in enumerate(DOTS):
        c = COLORS[i % len(COLORS)]
        draw.ellipse((x - 7, y - 7, x + 7, y + 7), fill=c)
        draw.text((x - 3, y - 8), "✦", fill="#0f1419")

    # snake eats dots in order
    eaten = (t // 3) % (len(DOTS) + 4)
    head_idx = max(0, eaten - 1)
    if head_idx < len(DOTS):
        hx, hy = DOTS[head_idx]
        # erase eaten dot
        draw.ellipse((hx - 8, hy - 8, hx + 8, hy + 8), fill="#0f1419")

    # body segments trail behind head
    seg_len = 5
    for s in range(seg_len):
        idx = head_idx - s
        if idx < 0 or idx >= len(DOTS):
            continue
        x, y = DOTS[idx]
        wobble = ((t + s) % 4) - 2
        r = 9 - s
        draw.ellipse((x - r, y - r + wobble, x + r, y + r + wobble), fill=SNAKE[s % len(SNAKE)])

    # head + face
    if head_idx < len(DOTS):
        hx, hy = DOTS[head_idx]
        wobble = (t % 4) - 2
        draw.ellipse((hx - 11, hy - 11 + wobble, hx + 11, hy + 11 + wobble), fill="#ff4d8d")
        draw.ellipse((hx - 5, hy - 4 + wobble, hx - 2, hy - 1 + wobble), fill="#1a1a1a")
        draw.ellipse((hx + 2, hy - 4 + wobble, hx + 5, hy - 1 + wobble), fill="#1a1a1a")
        draw.arc((hx - 4, hy + wobble, hx + 4, hy + 8 + wobble), 20, 160, fill="#1a1a1a", width=1)

    draw.text((18, 14), "snack snake · not my commit graph · just vibing", fill="#8b949e")
    return img


def main() -> None:
    out = Path(__file__).resolve().parent.parent / "assets" / "snack-snake.gif"
    out.parent.mkdir(exist_ok=True)
    frames = [draw_frame(t) for t in range(FRAMES)]
    frames[0].save(
        out,
        save_all=True,
        append_images=frames[1:],
        duration=90,
        loop=0,
        optimize=True,
    )
    print(f"Wrote {out} ({len(frames)} frames)")


if __name__ == "__main__":
    main()

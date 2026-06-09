#!/usr/bin/env python3
"""Generate full-width bunny intro header SVG + hopping bunny GIF."""

from math import sin, cos, pi
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent / "assets"
W, H = 1100, 150
FRAMES = 40


def write_intro_svg(path: Path) -> None:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="120" viewBox="0 0 {W} 120">
  <defs>
    <linearGradient id="sky" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#ffe8f3"/>
      <stop offset="55%" stop-color="#fff5f8"/>
      <stop offset="100%" stop-color="#e8f7ff"/>
    </linearGradient>
    <linearGradient id="ear" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffb3c9"/>
      <stop offset="100%" stop-color="#ff8fab"/>
    </linearGradient>
    <linearGradient id="earIn" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#ffd6e3"/>
      <stop offset="100%" stop-color="#ffc2d6"/>
    </linearGradient>
    <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#ff9eb8" flood-opacity="0.35"/>
    </filter>
    <filter id="pill" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#ffb3c6" flood-opacity="0.4"/>
    </filter>
  </defs>
  <rect width="{W}" height="120" rx="0" fill="url(#sky)"/>
  <ellipse cx="130" cy="18" rx="52" ry="68" fill="url(#ear)" filter="url(#soft)" transform="rotate(-12 130 18)"/>
  <ellipse cx="130" cy="22" rx="28" ry="42" fill="url(#earIn)" transform="rotate(-12 130 22)"/>
  <ellipse cx="{W - 130}" cy="18" rx="52" ry="68" fill="url(#ear)" filter="url(#soft)" transform="rotate(12 {W - 130} 18)"/>
  <ellipse cx="{W - 130}" cy="22" rx="28" ry="42" fill="url(#earIn)" transform="rotate(12 {W - 130} 22)"/>
  <rect x="24" y="52" width="{W - 48}" height="56" rx="28" fill="#ffffff" filter="url(#pill)"/>
  <rect x="30" y="58" width="{W - 60}" height="44" rx="22" fill="#fffafc" stroke="#ffd6e3" stroke-width="2"/>
  <circle cx="{W // 2}" cy="38" r="30" fill="#fff" stroke="#ffc2d6" stroke-width="3" filter="url(#pill)"/>
  <ellipse cx="{W // 2 - 12}" cy="36" rx="5" ry="7" fill="#4a3b47"/>
  <ellipse cx="{W // 2 + 12}" cy="36" rx="5" ry="7" fill="#4a3b47"/>
  <circle cx="{W // 2 - 10}" cy="34" r="2" fill="#fff"/>
  <circle cx="{W // 2 + 14}" cy="34" r="2" fill="#fff"/>
  <ellipse cx="{W // 2}" cy="44" rx="4" ry="3" fill="#ff8fab"/>
  <path d="M {W // 2 - 8} 48 Q {W // 2} 52 {W // 2 + 8} 48" stroke="#ff8fab" stroke-width="2" fill="none" stroke-linecap="round"/>
  <text x="{W // 2}" y="88" text-anchor="middle" font-family="ui-sans-serif, system-ui, sans-serif" font-size="22" font-weight="700" fill="#5c3d4e">nicole li</text>
  <text x="{W // 2}" y="108" text-anchor="middle" font-family="ui-sans-serif, system-ui, sans-serif" font-size="13" fill="#9d6b7d">data × product · chicago · northwestern</text>
</svg>"""
    path.write_text(svg, encoding="utf-8")
    print(f"Wrote {path}")


def lerp_color(a: str, b: str, t: float) -> str:
    ar, ag, ab = int(a[1:3], 16), int(a[3:5], 16), int(a[5:7], 16)
    br, bg, bb = int(b[1:3], 16), int(b[3:5], 16), int(b[5:7], 16)
    r = int(ar + (br - ar) * t)
    g = int(ag + (bg - ag) * t)
    bl = int(ab + (bb - ab) * t)
    return f"#{r:02x}{g:02x}{bl:02x}"


def draw_bg(draw: ImageDraw.ImageDraw) -> None:
    for x in range(W):
        c = lerp_color("#ffe8f3", "#e8f7ff", x / W)
        draw.line((x, 0, x, H), fill=c)
    draw.rounded_rectangle((16, 12, W - 16, H - 12), radius=22, fill="#fffafc", outline="#ffc2d6", width=2)
    draw.rectangle((40, H - 46, W - 40, H - 38), fill="#c8f0c8")
    for x in range(50, W - 40, 48):
        draw.ellipse((x, H - 42, x + 10, H - 34), fill="#a8e6a8")


def try_font(size: int) -> ImageFont.ImageFont:
    for name in ("Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def draw_emoji(draw: ImageDraw.ImageDraw, emoji: str, x: int, y: int, font: ImageFont.ImageFont) -> None:
    draw.text((x, y), emoji, font=font, embedded_color=True)


def hop_y(t: int) -> int:
    phase = (t % 10) / 10.0
    return int(abs(sin(phase * pi)) * 32)


def frame(t: int, font_big: ImageFont.ImageFont, font_sm: ImageFont.ImageFont) -> Image.Image:
    img = Image.new("RGB", (W, H), "#ffe8f3")
    draw = ImageDraw.Draw(img)
    draw_bg(draw)

    progress = (t / (FRAMES - 1)) * (W - 120)
    bx = 60 + int(progress)
    by = H - 78 - hop_y(t)
    bunny = "🐰" if t % 4 < 2 else "🐇"
    draw_emoji(draw, bunny, bx, by, font_big)

    # carrot trail
    for i, cx in enumerate(range(80, W - 80, 90)):
        if cx < bx - 20:
            draw_emoji(draw, "🥕", cx, H - 72 + (i % 2) * 4, font_sm)

    # clouds + sparkles
    draw_emoji(draw, "☁️", 70 + int(sin(t / 6) * 8), 28, font_sm)
    draw_emoji(draw, "☁️", W - 140, 24, font_sm)
    if hop_y(t) < 4:
        draw_emoji(draw, "✨", bx + 40, by - 10, font_sm)
        draw_emoji(draw, "💫", bx - 10, by + 6, font_sm)

    draw.text((44, 22), "bunny commute · hop hop · not a commit graph", fill="#b07a8c", font=font_sm)
    return img


def main() -> None:
    ROOT.mkdir(exist_ok=True)
    write_intro_svg(ROOT / "intro-header.svg")

    font_big = try_font(52)
    font_sm = try_font(22)
    frames = [frame(t, font_big, font_sm) for t in range(FRAMES)]
    out = ROOT / "bunny-hop.gif"
    frames[0].save(out, save_all=True, append_images=frames[1:], duration=75, loop=0, optimize=True)
    print(f"Wrote {out} ({W}x{H}, {len(frames)} frames, {out.stat().st_size // 1024}KB)")


if __name__ == "__main__":
    main()

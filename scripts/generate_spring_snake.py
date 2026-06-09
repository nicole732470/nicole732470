#!/usr/bin/env python3
"""Generate contribution snake SVG for a date range (default: 2026-03-01 → today)."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

USER = "nicole732470"
FROM_DATE = date(2026, 3, 1)
CELL = 14
PAD = 16
GAP = 3
COLORS_LIGHT = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]
COLORS_DARK = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
SNAKE_LIGHT = "#2ea043"
SNAKE_DARK = "#3fb950"


def level(count: int) -> int:
    if count <= 0:
        return 0
    if count <= 2:
        return 1
    if count <= 5:
        return 2
    if count <= 9:
        return 3
    return 4


def fetch_contributions(user: str, start: date, end: date) -> list[dict]:
    url = (
        "https://github-contributions-api.jogruber.de/v4/"
        f"{user}?from={start.isoformat()}&to={end.isoformat()}"
    )
    raw = subprocess.check_output(["curl", "-sf", "--max-time", "30", url], text=True)
    data = json.loads(raw)
    return data.get("contributions", [])


def week_start(d: date) -> date:
    return d - timedelta(days=d.weekday())


def build_grid(contributions: list[dict]) -> tuple[list[list[int]], date, int]:
    by_date = {c["date"]: c["count"] for c in contributions}
    end = max(datetime.strptime(c["date"], "%Y-%m-%d").date() for c in contributions)
    start = week_start(FROM_DATE)
    weeks = ((end - start).days // 7) + 1
    grid = [[0] * weeks for _ in range(7)]
    for w in range(weeks):
        for row in range(7):
            day = start + timedelta(days=w * 7 + row)
            if day < FROM_DATE or day > end:
                continue
            grid[row][w] = by_date.get(day.isoformat(), 0)
    return grid, start, weeks


def snake_path(grid: list[list[int]]) -> list[tuple[int, int]]:
    cells: list[tuple[int, int, int]] = []
    weeks = len(grid[0])
    for w in range(weeks):
        rows = range(7) if w % 2 == 0 else range(6, -1, -1)
        for r in rows:
            if grid[r][w] > 0:
                cells.append((r, w, grid[r][w]))
    return [(r, w) for r, w, _ in cells]


def render_svg(grid: list[list[int]], path: list[tuple[int, int]], dark: bool) -> str:
    weeks = len(grid[0])
    width = PAD * 2 + weeks * (CELL + GAP) - GAP
    height = PAD * 2 + 7 * (CELL + GAP) - GAP + 28
    palette = COLORS_DARK if dark else COLORS_LIGHT
    snake = SNAKE_DARK if dark else SNAKE_LIGHT
    bg = "#0d1117" if dark else "#ffffff"
    label = "#8b949e" if dark else "#57606a"

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}">',
        f'<rect width="{width}" height="{height}" rx="8" fill="{bg}"/>',
        f'<text x="{PAD}" y="14" fill="{label}" font-family="ui-monospace,monospace" font-size="11">'
        f"commits since {FROM_DATE.strftime('%b %Y')} · {sum(sum(r) for r in grid)} contributions</text>",
    ]

    for r in range(7):
        for w in range(weeks):
            x = PAD + w * (CELL + GAP)
            y = PAD + 20 + r * (CELL + GAP)
            parts.append(
                f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3" '
                f'fill="{palette[level(grid[r][w])]}"/>'
            )

    if len(path) >= 2:
        pts = []
        for r, w in path:
            x = PAD + w * (CELL + GAP) + CELL / 2
            y = PAD + 20 + r * (CELL + GAP) + CELL / 2
            pts.append(f"{x},{y}")
        parts.append(
            f'<polyline points="{" ".join(pts)}" fill="none" stroke="{snake}" '
            f'stroke-width="3" stroke-linecap="round" stroke-linejoin="round" opacity="0.9"/>'
        )
        lr, lw = path[-1]
        hx = PAD + lw * (CELL + GAP) + CELL / 2
        hy = PAD + 20 + lr * (CELL + GAP) + CELL / 2
        parts.append(f'<circle cx="{hx}" cy="{hy}" r="5" fill="{snake}"/>')
        parts.append(f'<text x="{hx + 8}" y="{hy + 4}" font-size="12">🐍</text>')

    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    out_dir = Path(__file__).resolve().parent.parent / "assets"
    out_dir.mkdir(exist_ok=True)
    end = date.today()
    contributions = fetch_contributions(USER, FROM_DATE, end)
    if not contributions:
        print("No contributions in range", file=sys.stderr)
        sys.exit(1)
    grid, _, _ = build_grid(contributions)
    path = snake_path(grid)
    (out_dir / "spring-snake.svg").write_text(render_svg(grid, path, dark=False), encoding="utf-8")
    (out_dir / "spring-snake-dark.svg").write_text(render_svg(grid, path, dark=True), encoding="utf-8")
    print(f"Wrote spring snake ({len(path)} active cells, {sum(sum(r) for r in grid)} commits)")


if __name__ == "__main__":
    main()

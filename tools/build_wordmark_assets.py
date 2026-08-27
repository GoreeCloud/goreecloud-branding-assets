#!/usr/bin/env python3
"""Generate canonical GoreeCloud Deep Cloud wordmark and lockup SVG assets.

The generator converts DejaVu Sans Bold lettering into SVG path geometry so
production output does not depend on font availability at render time. It does
not modify the approved Unified Clean platform-symbol geometry.
"""
from __future__ import annotations

from pathlib import Path

from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextPath
from matplotlib.transforms import Affine2D

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "generated" / "wordmark"
OUT.mkdir(parents=True, exist_ok=True)

DARK = "#111827"
PRIMARY_BLUE = "#3B82F6"
DEEP_BLUE = "#174EA6"
LIGHT_FIELD = "#F7FAFF"
DARK_FIELD = "#0B1220"
REVERSED_TEXT = "#F8FAFC"
REVERSED_BLUE = "#60A5FA"

FONT = FontProperties(family="DejaVu Sans", weight="bold")

SYMBOL = f'''\
<path fill-rule="evenodd" d="M256 98c87 0 158 71 158 158s-71 158-158 158S98 343 98 256 169 98 256 98Zm0 67c-50 0-91 41-91 91s41 91 91 91c35 0 65-20 80-49h-80c-23 0-42-19-42-42s19-42 42-42h80c-15-29-45-49-80-49Z" fill="{PRIMARY_BLUE}"/>
<path d="M256 231h158c14 0 25 11 25 25s-11 25-25 25H256c-14 0-25-11-25-25s11-25 25-25Z" fill="{DEEP_BLUE}"/>
<circle cx="256" cy="256" r="13" fill="{LIGHT_FIELD}"/>
'''


def text_path(text: str, size: float = 150.0) -> tuple[str, object]:
    path = TextPath((0, 0), text, size=size, prop=FONT, usetex=False)
    path = Affine2D().scale(1, -1).transform_path(path)
    parts: list[str] = []
    for polygon in path.to_polygons():
        if not len(polygon):
            continue
        parts.append(f"M {polygon[0][0]:.3f} {polygon[0][1]:.3f}")
        for x, y in polygon[1:]:
            parts.append(f"L {x:.3f} {y:.3f}")
        parts.append("Z")
    return " ".join(parts), path.get_extents()


GOREE_PATH, GOREE_BOX = text_path("Goree")
CLOUD_PATH, CLOUD_BOX = text_path("Cloud")
CLOUD_OFFSET = GOREE_BOX.x1 - GOREE_BOX.x0 - 1.5


def wordmark_group(dark: str = DARK, blue: str = DEEP_BLUE) -> str:
    return f'''\
<path d="{GOREE_PATH}" fill="{dark}" fill-rule="evenodd"/>
<g transform="translate({CLOUD_OFFSET:.3f} 0)">
  <path d="{CLOUD_PATH}" fill="{blue}" fill-rule="evenodd"/>
</g>'''


def write(name: str, content: str) -> None:
    (OUT / name).write_text(content, encoding="utf-8")


write(
    "goreecloud-wordmark.svg",
    f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 190" role="img">
<title>GoreeCloud Deep Cloud Wordmark</title>
<g transform="translate(20 150)">{wordmark_group()}</g>
</svg>\n''',
)

write(
    "goreecloud-lockup-horizontal.svg",
    f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 420" role="img">
<title>GoreeCloud Horizontal Lockup</title>
<rect width="1400" height="420" rx="48" fill="{LIGHT_FIELD}"/>
<g transform="translate(50 37) scale(.675)">{SYMBOL}</g>
<g transform="translate(420 257)">{wordmark_group()}</g>
</svg>\n''',
)

stack_scale = 0.72
stack_width = (CLOUD_OFFSET + CLOUD_BOX.x1) * stack_scale
stack_x = (900 - stack_width) / 2
write(
    "goreecloud-lockup-stacked.svg",
    f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 900" role="img">
<title>GoreeCloud Stacked Lockup</title>
<rect width="900" height="900" rx="72" fill="{LIGHT_FIELD}"/>
<g transform="translate(194 55)">{SYMBOL}</g>
<g transform="translate({stack_x:.3f} 680) scale({stack_scale})">{wordmark_group()}</g>
</svg>\n''',
)

# Reversed and monochrome wordmark-only derivatives.
write(
    "goreecloud-wordmark-reversed.svg",
    f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 190" role="img">
<title>GoreeCloud Deep Cloud Wordmark — Reversed</title>
<rect width="1000" height="190" fill="{DARK_FIELD}"/>
<g transform="translate(20 150)">{wordmark_group(REVERSED_TEXT, REVERSED_BLUE)}</g>
</svg>\n''',
)
write(
    "goreecloud-wordmark-monochrome.svg",
    f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 190" role="img">
<title>GoreeCloud Deep Cloud Wordmark — Monochrome</title>
<g transform="translate(20 150)">{wordmark_group(DARK, DARK)}</g>
</svg>\n''',
)

print(f"Generated assets in {OUT}")

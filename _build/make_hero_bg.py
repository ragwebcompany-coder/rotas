# -*- coding: utf-8 -*-
"""Παράγει το background του hero: assets/hero-waves.svg

Μοτίβο: τομέας υπερηχογραφικής δέσμης (sector scan) — ομόκεντρα τόξα που
εκπέμπονται από σημείο έξω από το κάδρο, πάνω δεξιά. Αφηρημένο, χωρίς
ανθρώπους, στην παλέτα του site (azure #2166b0 / navy #17497f).

    python _build/make_hero_bg.py
"""
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "assets", "hero-waves.svg")

W, H = 1600, 900

# Κέντρο εκπομπής — έξω από το κάδρο, πάνω δεξιά.
CX, CY = 1560.0, -90.0

# Η δέσμη ανοίγει προς τα κάτω-αριστερά.
A0, A1 = 96.0, 196.0          # μοίρες
R_MIN, R_MAX = 210.0, 2150.0
N_ARCS = 46

ACCENT = "#2166b0"
DEEP = "#17497f"


def polar(r, deg):
    a = math.radians(deg)
    return CX + r * math.cos(a), CY + r * math.sin(a)


def arc_path(r, a0, a1):
    x0, y0 = polar(r, a0)
    x1, y1 = polar(r, a1)
    large = 1 if (a1 - a0) > 180 else 0
    return f"M {x0:.1f} {y0:.1f} A {r:.1f} {r:.1f} 0 {large} 1 {x1:.1f} {y1:.1f}"


def ease(t):
    """Ομαλή καμπύλη 0→1→0, ώστε τα τόξα να σβήνουν στις δύο άκρες."""
    return math.sin(math.pi * t) ** 0.85


arcs = []
for i in range(N_ARCS):
    t = i / (N_ARCS - 1)
    # Μη γραμμική κατανομή: πυκνότερα κοντά στην πηγή.
    r = R_MIN + (R_MAX - R_MIN) * (t ** 1.35)

    # Κάθε τόξο στενεύει ελαφρώς και μετατοπίζεται — δίνει ροή.
    shrink = 13.0 * math.sin(t * math.pi * 1.6)
    a0 = A0 + shrink
    a1 = A1 - shrink * 0.55

    # Κάθε 7ο τόξο πιο έντονο και σε navy — δίνει ρυθμό χωρίς θόρυβο.
    strong = (i % 7 == 0)
    opacity = (0.20 + 0.26 * ease(t)) if strong else (0.075 + 0.20 * ease(t))
    width = (1.8 + 3.2 * (t ** 1.7)) if strong else (1.0 + 2.4 * (t ** 1.7))
    color = DEEP if strong else ACCENT

    arcs.append(
        f'    <path d="{arc_path(r, a0, a1)}" stroke="{color}" '
        f'stroke-width="{width:.2f}" stroke-opacity="{opacity:.3f}" '
        f'stroke-linecap="round" fill="none" />'
    )

svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
     width="{W}" height="{H}" preserveAspectRatio="xMaxYMid slice" role="img"
     aria-label="Αφηρημένο μοτίβο υπερηχογραφικής δέσμης">
  <defs>
    <radialGradient id="glow" cx="96%" cy="2%" r="86%">
      <stop offset="0%"   stop-color="{DEEP}"   stop-opacity="0.34" />
      <stop offset="28%"  stop-color="{ACCENT}" stop-opacity="0.18" />
      <stop offset="62%"  stop-color="{ACCENT}" stop-opacity="0.06" />
      <stop offset="100%" stop-color="{ACCENT}" stop-opacity="0" />
    </radialGradient>
    <linearGradient id="fade" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%"  stop-color="#fff" stop-opacity="0" />
      <stop offset="26%" stop-color="#fff" stop-opacity="0.18" />
      <stop offset="52%" stop-color="#fff" stop-opacity="0.7" />
      <stop offset="100%" stop-color="#fff" stop-opacity="1" />
    </linearGradient>
    <mask id="leftFade">
      <rect width="{W}" height="{H}" fill="url(#fade)" />
    </mask>
  </defs>

  <rect width="{W}" height="{H}" fill="url(#glow)" />
  <g mask="url(#leftFade)">
{chr(10).join(arcs)}
  </g>
</svg>
"""

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(svg)

print(f"wrote {OUT}  ({len(svg)/1024:.1f} KB, {len(arcs)} arcs)")

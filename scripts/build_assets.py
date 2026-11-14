#!/usr/bin/env python3
"""Generate the animated SVG assets used by the profile README.

Every number drawn here comes from a paper, thesis table, README or stored
evaluation file in the corresponding repository (see DATA below).
Run:  python scripts/build_assets.py      -> writes ../assets/*.svg
Edit the DATA block, re-run, commit.  No external services are used, so the
graphics render the same everywhere GitHub renders SVG (SMIL animation).
"""
import math
import os
import random

STATIC = os.environ.get("STATIC") == "1"   # QA mode: bake final animation state
OUT = os.environ.get("OUT_DIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- palette
BG0, BG1, PANEL = "#071426", "#0c2238", "#0f2a43"
GRID, TEXT, MUTED = "#17324d", "#e6edf3", "#8aa0b8"
TEAL, BLUE, CORAL, AMBER, GREEN, VIOLET = (
    "#2dd4bf", "#60a5fa", "#fb7185", "#fbbf24", "#4ade80", "#a78bfa")
SANS = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "'SFMono-Regular',Consolas,'DejaVu Sans Mono',monospace"

# ---------------------------------------------------------------- DATA
DATA = {
    # TriLayer-Nav paper, Table 2: 12 scenarios x 10 runs = 120 runs / architecture
    "nav": [("DWA only", 71.6, MUTED), ("A* + DWA", 76.6, BLUE), ("TriLayer-Nav", 96.6, TEAL)],
    # NeRF paper, Table 4 (Lego, 100 validation views)
    "nerf_psnr": [("NONE", 20.21, MUTED), ("SOFT", 20.71, BLUE), ("HARD", 21.17, AMBER), ("HYBRID", 22.36, TEAL)],
    "nerf_ssim": {"NONE": 0.658, "SOFT": 0.522, "HARD": 0.685, "HYBRID": 0.778},
    # Thesis Tables 6 and 9 (validation set of 30 crack images, IoU 0.5)
    "shots": [5, 7, 10, 20, 30],
    "fewshot_std": [0.218, 0.291, 0.323, 0.524, 0.535],
    "fewshot_kd": [0.286, 0.276, 0.319, 0.559, 0.606],
    # ProcuraAI reports/evaluation/evaluation_results.json (synthetic data)
    "proc_struct": (1.00, 1.00, 1.00),
    "proc_docs": (0.6974, 0.9815, 0.8154),
}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def head(w, h, title, desc=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{esc(title)}"><title>{esc(title)}</title><desc>{esc(desc)}</desc>')


def text(x, y, s, size=14, fill=TEXT, weight="normal", anchor="start", font=SANS, extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" {extra}>{esc(s)}</text>')


def bezier(p0, p1, p2, p3, t):
    u = 1 - t
    return (u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
            u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1])


# =================================================================== BANNER
def banner():
    W, H = 1280, 440
    s = [head(W, H, "Umer Ahmed Baig Mughal - Robotics and AI engineer",
              "Animated banner: a robot follows an A* path among obstacles; headline results from the author's projects.")]
    s.append(f'<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
             f'<stop offset="0" stop-color="{BG0}"/><stop offset="0.6" stop-color="{BG1}"/>'
             f'<stop offset="1" stop-color="#0b3a4a"/></linearGradient>'
             f'<linearGradient id="bar" x1="0" x2="1"><stop offset="0" stop-color="{TEAL}"/>'
             f'<stop offset="1" stop-color="{BLUE}"/></linearGradient></defs>')
    s.append(f'<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/>')
    for gx in range(40, W, 40):
        s.append(f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}" stroke="{GRID}" stroke-width="1" opacity=".45"/>')
    for gy in range(40, H, 40):
        s.append(f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}" stroke="{GRID}" stroke-width="1" opacity=".45"/>')

    # ---- left text block
    s.append(text(52, 78, "ROBOTICS · AI · AUTONOMOUS SYSTEMS", 13, TEAL, "bold", font=MONO, extra='letter-spacing="3"'))
    s.append(text(52, 140, "Umer Ahmed", 56, TEXT, "800"))
    s.append(text(52, 198, "Baig Mughal", 56, TEXT, "800"))
    s.append(f'<rect x="52" y="214" width="120" height="4" rx="2" fill="url(#bar)">'
             f'<animate attributeName="width" values="0;120;120;0" keyTimes="0;.1;.9;1" dur="8s" repeatCount="indefinite"/></rect>')
    s.append(text(52, 250, "MSc Robotics & AI · ITMO University · CGPA 4.82/5 · Diploma with Honours", 14, MUTED, font=MONO))

    lines = ["perception → planning → control",
             "few-shot defect detection for robotic inspection",
             "depth-supervised NeRF · under review",
             "RAG + LangGraph invoice auditor",
             "published: A* + DWA + MPC navigation"]
    n, per = len(lines), 3.6
    cyc = n * per
    for i, ln in enumerate(lines):
        if STATIC:
            if i == 0:
                s.append(f'<text x="52" y="292" font-family="{MONO}" font-size="21" fill="{TEAL}">&gt; {esc(ln)}</text>')
            continue
        a, b = i / n, (i + 1) / n
        kt = f"0;{a:.3f};{a + .02:.3f};{b - .03:.3f};{b - .01:.3f};1"
        s.append(f'<text x="52" y="292" font-family="{MONO}" font-size="21" fill="{TEAL}" opacity="0">'
                 f'&gt; {esc(ln)}<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="{kt}" '
                 f'dur="{cyc}s" repeatCount="indefinite"/></text>')
    s.append(f'<rect x="52" y="304" width="9" height="3" fill="{TEAL}"><animate attributeName="opacity" '
             f'values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>')

    # ---- metric chips
    chips = [("96.6%", "nav success · 120 runs/arch.", TEAL),
             ("0.658→0.778", "NeRF SSIM · hybrid depth", BLUE),
             ("0.22→0.53", "crack mAP@50 · 5→30 shots", AMBER),
             ("0.82 F1", "invoice audit · OCR path", VIOLET)]
    for i, (big, small, col) in enumerate(chips):
        cx, cy, cw = 52 + (i % 2) * 345, 316 + (i // 2) * 60, 335
        anim = "" if STATIC else (f'<animate attributeName="opacity" values="0;0;1;1" keyTimes="0;{.1 + i * .12:.2f};{.2 + i * .12:.2f};1" '
                                  f'dur="2.4s" begin="0s" fill="freeze"/>')
        s.append(f'<g opacity="{1 if STATIC else 0}">{anim}'
                 f'<rect x="{cx}" y="{cy}" width="{cw - 10}" height="52" rx="10" fill="{PANEL}" stroke="{col}" stroke-opacity=".55"/>'
                 f'{text(cx + 16, cy + 25, big, 20, col, "800")}{text(cx + 16, cy + 43, small, 11.5, MUTED)}</g>')
    # ---- right: navigation scene
    px, py, pw, ph = 770, 44, 470, 352
    s.append(f'<g transform="translate({px},{py})">')
    s.append(f'<rect width="{pw}" height="{ph}" rx="14" fill="#06101d" stroke="#1e4263" stroke-width="1.5"/>')
    for gx in range(30, pw, 30):
        s.append(f'<line x1="{gx}" y1="10" x2="{gx}" y2="{ph - 50}" stroke="{GRID}" stroke-width="1" opacity=".7"/>')
    for gy in range(30, ph - 50, 30):
        s.append(f'<line x1="10" y1="{gy}" x2="{pw - 10}" y2="{gy}" stroke="{GRID}" stroke-width="1" opacity=".7"/>')
    p0, p1, p2, p3 = (40, 280), (160, 270), (190, 90), (428, 56)
    samples = [bezier(p0, p1, p2, p3, t / 200) for t in range(201)]
    length = sum(math.dist(samples[i], samples[i + 1]) for i in range(200))
    rnd = random.Random(7)
    obst = []
    tries = 0
    while len(obst) < 15 and tries < 4000:
        tries += 1
        r = rnd.randint(11, 20)
        x, y = rnd.randint(30, pw - 30), rnd.randint(58, ph - 80)
        if min(math.dist((x, y), q) for q in samples) < r + 22:
            continue
        if math.dist((x, y), p0) < r + 30 or math.dist((x, y), p3) < r + 30:
            continue
        if any(math.dist((x, y), (ox, oy)) < r + orr + 8 for ox, oy, orr in obst):
            continue
        obst.append((x, y, r))
    for ox, oy, orr in obst:
        s.append(f'<circle cx="{ox}" cy="{oy}" r="{orr}" fill="{CORAL}" fill-opacity=".55" stroke="{CORAL}"/>')
    # A* path: coarse polyline of the same corridor
    pts = [bezier(p0, p1, p2, p3, t / 9) for t in range(10)]
    gp = " ".join(f"{x:.0f},{y:.0f}" for x, y in pts)
    s.append(f'<polyline points="{gp}" fill="none" stroke="{AMBER}" stroke-width="2" stroke-dasharray="6 5" opacity=".9"/>')
    d = f"M{p0[0]} {p0[1]} C{p1[0]} {p1[1]} {p2[0]} {p2[1]} {p3[0]} {p3[1]}"
    if STATIC:
        s.append(f'<path d="{d}" fill="none" stroke="{TEAL}" stroke-width="3.2" stroke-linecap="round"/>')
    else:
        s.append(f'<path d="{d}" fill="none" stroke="{TEAL}" stroke-width="3.2" stroke-linecap="round" '
                 f'stroke-dasharray="{length:.0f}" stroke-dashoffset="{length:.0f}">'
                 f'<animate attributeName="stroke-dashoffset" values="{length:.0f};0;0;{length:.0f}" '
                 f'keyTimes="0;.62;.92;1" dur="9s" repeatCount="indefinite"/></path>')
    s.append(f'<circle cx="{p0[0]}" cy="{p0[1]}" r="8" fill="{GREEN}"/>{text(p0[0] - 6, p0[1] + 26, "start", 11, MUTED)}')
    s.append(f'<circle cx="{p3[0]}" cy="{p3[1]}" r="9" fill="{CORAL}"/>{text(p3[0] - 30, p3[1] - 16, "goal", 11, MUTED)}')
    rel = f"M0 0 C{p1[0]-p0[0]} {p1[1]-p0[1]} {p2[0]-p0[0]} {p2[1]-p0[1]} {p3[0]-p0[0]} {p3[1]-p0[1]}"
    robot = (f'<g transform="translate({p0[0]},{p0[1]})"><circle r="10" fill="none" stroke="{TEAL}" stroke-width="2"><animate attributeName="r" values="8;26;8" '
             f'dur="1.4s" repeatCount="indefinite"/><animate attributeName="opacity" values=".8;0;.8" dur="1.4s" repeatCount="indefinite"/></circle>'
             f'<polygon points="12,0 -9,-8 -9,8" fill="{TEXT}" stroke="{TEAL}" stroke-width="1.5"/>'
             f'<animateMotion dur="9s" repeatCount="indefinite" rotate="auto" keyPoints="0;1;1" keyTimes="0;.62;1" '
             f'calcMode="linear" path="{rel}"/></g>')
    s.append(robot)
    s.append(text(18, 30, "MuJoCo-style arena · simplified illustration", 11, MUTED, font=MONO))
    # layer indicator
    labs = ["A*", "DWA", "MPC", "PID"]
    cols = [AMBER, BLUE, TEAL, VIOLET]
    for i, (lb, col) in enumerate(zip(labs, cols)):
        bx = 24 + i * 108
        a = i / 4
        s.append(f'<g><rect x="{bx}" y="{ph - 42}" width="96" height="28" rx="8" fill="{PANEL}" stroke="{col}"/>'
                 f'<rect x="{bx}" y="{ph - 42}" width="96" height="28" rx="8" fill="{col}" opacity="0">'
                 f'<animate attributeName="opacity" values="0;0;.35;.35;0;0" keyTimes="0;{a:.2f};{a + .02:.2f};{a + .24:.2f};{a + .26:.2f};1" '
                 f'dur="4s" repeatCount="indefinite"/></rect>'
                 f'{text(bx + 48, ph - 23, lb, 14, col, "bold", "middle", MONO)}</g>')
        if i < 3:
            s.append(text(bx + 102, ph - 23, "→", 14, MUTED, "normal", "middle"))
    s.append("</g></svg>")
    return "".join(s)


# =================================================================== CONSOLE
def panel(x, y, w, h, title, sub, col):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{PANEL}" stroke="#1e4263"/>'
            f'<rect x="{x}" y="{y}" width="5" height="{h}" rx="2" fill="{col}"/>'
            f'{text(x + 22, y + 30, title, 16, TEXT, "bold")}{text(x + 22, y + 50, sub, 11.5, MUTED, font=MONO)}')


def grow_h(x, y, w, wmax, delay=0.0, dur=10, fill=TEAL, rx=4):
    if STATIC:
        return f'<rect x="{x}" y="{y}" width="{wmax:.1f}" height="{w}" rx="{rx}" fill="{fill}"/>'
    return (f'<rect x="{x}" y="{y}" width="0" height="{w}" rx="{rx}" fill="{fill}">'
            f'<animate attributeName="width" values="0;{wmax:.1f};{wmax:.1f};0" keyTimes="0;.14;.92;1" '
            f'dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/></rect>')


def grow_v(x, ybase, wd, hmax, delay=0.0, dur=10, fill=TEAL, rx=4):
    if STATIC:
        return f'<rect x="{x}" y="{ybase - hmax:.1f}" width="{wd}" height="{hmax:.1f}" rx="{rx}" fill="{fill}"/>'
    return (f'<rect x="{x}" y="{ybase}" width="{wd}" height="0" rx="{rx}" fill="{fill}">'
            f'<animate attributeName="height" values="0;{hmax:.1f};{hmax:.1f};0" keyTimes="0;.14;.92;1" dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/>'
            f'<animate attributeName="y" values="{ybase};{ybase - hmax:.1f};{ybase - hmax:.1f};{ybase}" keyTimes="0;.14;.92;1" '
            f'dur="{dur}s" begin="{delay}s" repeatCount="indefinite"/></rect>')


def console():
    W, H = 1240, 672
    s = [head(W, H, "Results console - measured results from my projects",
              "Four animated charts: navigation success, NeRF depth supervision, few-shot crack detection, invoice audit.")]
    s.append(f'<rect width="{W}" height="{H}" rx="16" fill="{BG0}"/>')
    for gx in range(40, W, 40):
        s.append(f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}" stroke="{GRID}" stroke-width="1" opacity=".35"/>')
    s.append(f'<circle cx="30" cy="28" r="6" fill="#ff5f57"/><circle cx="50" cy="28" r="6" fill="#febc2e"/><circle cx="70" cy="28" r="6" fill="#28c840"/>')
    s.append(text(W / 2, 33, "results.console  —  measured numbers · limitations stated", 13, MUTED, anchor="middle", font=MONO))
    s.append(f'<line x1="0" y1="50" x2="{W}" y2="50" stroke="#1e4263"/>')

    # ---- panel 1: navigation success
    x, y, w, h = 20, 66, 600, 285
    s.append(panel(x, y, w, h, "TriLayer-Nav · navigation success", "MuJoCo simulation · 12 scenarios x 10 runs = 120 runs / architecture", TEAL))
    bx, bw = x + 130, 380
    for i, (lab, val, col) in enumerate(DATA["nav"]):
        by = y + 84 + i * 58
        s.append(text(x + 24, by + 22, lab, 14, TEXT, "600"))
        s.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="34" rx="6" fill="#0a1f33"/>')
        s.append(grow_h(bx, by, 34, bw * val / 100, 0.15 * i, fill=col))
        s.append(text(bx + bw * val / 100 - 8, by + 23, f"{val:.1f}%", 14, "#04121f", "800", "end"))
    s.append(text(x + 24, y + 272, "116 / 120 successful runs · final position error ≤ 0.2 m · simulation only", 11.5, MUTED, font=MONO))

    # ---- panel 2: NeRF
    x, y, w, h = 640, 66, 580, 285
    s.append(panel(x, y, w, h, "Depth-supervised NeRF · Lego", "PSNR (dB, axis starts at 18) · 100 held-out views · SSIM above bars", BLUE))
    base, top_v, lo, hi = y + 226, y + 84, 18.0, 23.0
    scale = (base - top_v) / (hi - lo)
    for gy in range(19, 24):
        yy = base - (gy - lo) * scale
        s.append(f'<line x1="{x + 56}" y1="{yy:.1f}" x2="{x + w - 24}" y2="{yy:.1f}" stroke="{GRID}"/>{text(x + 48, yy + 4, str(gy), 10.5, MUTED, anchor="end", font=MONO)}')
    for i, (lab, val, col) in enumerate(DATA["nerf_psnr"]):
        bx2 = x + 90 + i * 118
        hh = (val - lo) * scale
        s.append(grow_v(bx2, base, 70, hh, 0.12 * i, fill=col))
        s.append(text(bx2 + 35, base - hh - 22, f"SSIM {DATA['nerf_ssim'][lab]:.3f}", 11, MUTED, anchor="middle", font=MONO))
        s.append(text(bx2 + 35, base - hh - 7, f"{val:.2f}", 14, TEXT, "800", "middle"))
        s.append(text(bx2 + 35, base + 16, lab, 12, TEXT, "600", "middle"))
    s.append(text(x + 24, y + 272, "hybrid: MSE −41%, MAE −33% · only strategy to lift PSNR and SSIM on Lego and Chair", 11, MUTED, font=MONO))

    # ---- panel 3: few-shot line chart
    x, y, w, h = 20, 369, 600, 285
    s.append(panel(x, y, w, h, "Few-shot crack detection · MSc thesis", "mAP@50 vs labelled crack images (K) · validation set of 30 images", AMBER))
    cx0, cx1, cy0, cy1 = x + 70, x + w - 40, y + 224, y + 84
    xs = [cx0 + (cx1 - cx0) * i / 4 for i in range(5)]
    for gv in (0.2, 0.3, 0.4, 0.5, 0.6):
        yy = cy0 - (cy0 - cy1) * (gv - 0.1) / 0.6
        s.append(f'<line x1="{cx0}" y1="{yy:.1f}" x2="{cx1}" y2="{yy:.1f}" stroke="{GRID}"/>{text(cx0 - 8, yy + 4, f"{gv:.1f}", 10.5, MUTED, anchor="end", font=MONO)}')

    def ypos(v):
        return cy0 - (cy0 - cy1) * (v - 0.1) / 0.6
    for series, col, lab, dash, dly in ((DATA["fewshot_std"], BLUE, "fine-tuning", "", 0.0), (DATA["fewshot_kd"], AMBER, "+ distillation", "", 0.6)):
        pts = [(xs[i], ypos(v)) for i, v in enumerate(series)]
        d = "M" + " L".join(f"{px:.1f} {py:.1f}" for px, py in pts)
        L = sum(math.dist(pts[i], pts[i + 1]) for i in range(4))
        if STATIC:
            s.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="3" stroke-linejoin="round"/>')
        else:
            s.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="3" stroke-linejoin="round" stroke-dasharray="{L:.0f}" stroke-dashoffset="{L:.0f}">'
                     f'<animate attributeName="stroke-dashoffset" values="{L:.0f};0;0;{L:.0f}" keyTimes="0;.25;.92;1" dur="10s" begin="{dly}s" repeatCount="indefinite"/></path>')
        for i, (px, py) in enumerate(pts):
            if STATIC:
                s.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4.5" fill="{col}"/>')
                continue
            s.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4.5" fill="{col}" opacity="0"><animate attributeName="opacity" values="0;0;1;1;0" '
                     f'keyTimes="0;{0.04 + .05 * i:.2f};{0.1 + .05 * i:.2f};.92;1" dur="10s" begin="{dly}s" repeatCount="indefinite"/></circle>')
    for i, k in enumerate(DATA["shots"]):
        s.append(text(xs[i], cy0 + 20, f"{k}-shot", 11.5, MUTED, anchor="middle", font=MONO))
    s.append(text(xs[0] + 6, ypos(0.218) + 22, "0.22", 12, BLUE, "bold"))
    s.append(text(xs[4] - 4, ypos(0.535) + 20, "0.53", 12, BLUE, "bold", "end"))
    s.append(text(xs[4] - 4, ypos(0.606) - 10, "0.61", 12, AMBER, "bold", "end"))
    s.append(f'<rect x="{x + 330}" y="{y + 20}" width="14" height="4" fill="{BLUE}"/>{text(x + 350, y + 26, "fine-tuning", 11, MUTED, font=MONO)}')
    s.append(f'<rect x="{x + 440}" y="{y + 20}" width="14" height="4" fill="{AMBER}"/>{text(x + 460, y + 26, "+ distillation", 11, MUTED, font=MONO)}')
    s.append(text(x + 24, y + 272, "distillation gain is not consistent across K (negative at 7 and 10 shots)", 11, MUTED, font=MONO))

    # ---- panel 4: ProcuraAI
    x, y, w, h = 640, 369, 580, 285
    s.append(panel(x, y, w, h, "ProcuraAI · invoice audit", "72 synthetic invoices · 25 anomaly scenarios · finding-level scores", VIOLET))
    base, tp = y + 224, y + 90
    for gv in (0.0, 0.5, 1.0):
        yy = base - (base - tp) * gv
        s.append(f'<line x1="{x + 60}" y1="{yy:.1f}" x2="{x + w - 24}" y2="{yy:.1f}" stroke="{GRID}"/>{text(x + 52, yy + 4, f"{gv:.1f}", 10.5, MUTED, anchor="end", font=MONO)}')
    metrics = ["precision", "recall", "F1"]
    for i, m in enumerate(metrics):
        gx = x + 100 + i * 150
        for j, (vals, col, lab) in enumerate(((DATA["proc_struct"], "#64748b", "structured CSV"), (DATA["proc_docs"], VIOLET, "OCR documents"))):
            v = vals[i]
            hh = (base - tp) * v
            bxx = gx + j * 52
            s.append(grow_v(bxx, base, 44, hh, 0.12 * i + 0.06 * j, fill=col))
            s.append(text(bxx + 22, base - hh - 6, f"{v:.2f}", 12, TEXT, "bold", "middle"))
        s.append(text(gx + 48, base + 16, m, 12, TEXT, "600", "middle"))
    s.append(f'<rect x="{x + 330}" y="{y + 20}" width="12" height="12" rx="2" fill="#64748b"/>{text(x + 348, y + 30, "structured", 11, MUTED, font=MONO)}')
    s.append(f'<rect x="{x + 440}" y="{y + 20}" width="12" height="12" rx="2" fill="{VIOLET}"/>{text(x + 458, y + 30, "OCR docs", 11, MUTED, font=MONO)}')
    s.append(text(x + 24, y + 272, "perfect structured score = generator and engine co-designed; OCR path is the honest number", 11, MUTED, font=MONO))
    s.append("</svg>")
    return "".join(s)


# =================================================================== PIPELINES
def pipeline(name, title, stages, colors, sub=""):
    n = len(stages)
    W = 1240
    gap = 26
    bw = (W - 40 - gap * (n - 1)) / n
    H = 150
    s = [head(W, H, title, sub)]
    s.append(f'<rect width="{W}" height="{H}" rx="14" fill="{BG0}"/>')
    s.append(text(22, 28, title, 13, TEAL, "bold", font=MONO, extra='letter-spacing="1.5"'))
    for i, (st, col) in enumerate(zip(stages, colors)):
        x = 20 + i * (bw + gap)
        s.append(f'<rect x="{x:.1f}" y="46" width="{bw:.1f}" height="84" rx="10" fill="{PANEL}" stroke="{col}" stroke-opacity=".7"/>')
        s.append(f'<rect x="{x:.1f}" y="46" width="{bw:.1f}" height="84" rx="10" fill="{col}" opacity="0">'
                 f'<animate attributeName="opacity" values="0;0;.28;.28;0;0" keyTimes="0;{i / n:.3f};{i / n + .02:.3f};{(i + 1) / n - .01:.3f};{(i + 1) / n:.3f};1" '
                 f'dur="{n * 1.2}s" repeatCount="indefinite"/></rect>')
        s.append(text(x + bw / 2, 76, st[0], 14, TEXT, "bold", "middle"))
        s.append(text(x + bw / 2, 98, st[1], 11, MUTED, anchor="middle", font=MONO))
        if len(st) > 2:
            s.append(text(x + bw / 2, 116, st[2], 11, MUTED, anchor="middle", font=MONO))
        if i < n - 1:
            ax = x + bw
            s.append(f'<path d="M{ax + 4:.1f} 88 L{ax + gap - 6:.1f} 88" stroke="{MUTED}" stroke-width="2"/>'
                     f'<path d="M{ax + gap - 11:.1f} 82 L{ax + gap - 4:.1f} 88 L{ax + gap - 11:.1f} 94" fill="none" stroke="{MUTED}" stroke-width="2"/>')
    # travelling packet
    x0, x1 = 20 + bw / 2, 20 + (n - 1) * (bw + gap) + bw / 2
    s.append(f'<circle cy="136" r="5" fill="{TEAL}"><animate attributeName="cx" values="{x0:.0f};{x1:.0f}" dur="{n * 1.2}s" repeatCount="indefinite"/></circle>')
    s.append(f'<line x1="{x0:.0f}" y1="136" x2="{x1:.0f}" y2="136" stroke="{GRID}" stroke-width="2"/>')
    s.append("</svg>")
    with open(os.path.join(OUT, name), "w", encoding="utf8") as f:
        f.write("".join(s))


# =================================================================== SKILL MATRIX
REPOS = ["TriLayer-Nav", "Depth-NeRF", "ProcuraAI", "Fuel API", "RL + PINNs", "Perception", "ML in Robotics",
         "Motion & Control", "Sim. Systems", "Kinematics", "Potential Field", "Freight Rates", "Beale / Metaheur."]
R = {n: i for i, n in enumerate(REPOS)}
GROUPS = [
    ("PERCEPTION & LEARNING", BLUE, [
        ("CNN · segmentation · autoencoders (PyTorch)", ["ML in Robotics"]),
        ("Neural rendering / NeRF (PyTorch)", ["Depth-NeRF"]),
        ("Deep RL: DQN, PPO, GAE", ["RL + PINNs"]),
        ("Physics-informed learning · SVD", ["RL + PINNs"]),
        ("Gradient-boosted ML · time-aware validation", ["Freight Rates"]),
    ]),
    ("PLANNING & CONTROL", TEAL, [
        ("Global / local planning: A*, DWA, potential fields", ["TriLayer-Nav", "Potential Field"]),
        ("MPC and PID control", ["TriLayer-Nav"]),
        ("Dynamics, trajectories, computed-torque control", ["Motion & Control"]),
        ("Kinematics: DH, IK, Jacobians", ["Kinematics", "Motion & Control"]),
    ]),
    ("ESTIMATION & SIMULATION", AMBER, [
        ("State estimation: EKF / UKF · least squares", ["Perception"]),
        ("Stereo vision · camera calibration (OpenCV)", ["Perception"]),
        ("Physics simulation (MuJoCo)", ["TriLayer-Nav", "Sim. Systems"]),
        ("Numerical integration · stability analysis", ["Sim. Systems"]),
        ("Metaheuristic optimisation: GA, SA, Hooke-Jeeves", ["Beale / Metaheur."]),
    ]),
    ("LLM & DOCUMENT AI", VIOLET, [
        ("RAG: FAISS + BM25, verifiable citations", ["ProcuraAI"]),
        ("Multi-agent workflows (LangGraph)", ["ProcuraAI"]),
        ("OCR and structured extraction (Pydantic)", ["ProcuraAI"]),
    ]),
    ("SOFTWARE ENGINEERING", GREEN, [
        ("REST APIs: FastAPI, Django REST Framework", ["ProcuraAI", "Fuel API"]),
        ("Dynamic programming · geospatial routing", ["Fuel API"]),
        ("Automated tests · CI · Docker", ["ProcuraAI", "Fuel API", "Freight Rates"]),
        ("Scientific Python: NumPy, SciPy, Matplotlib", ["TriLayer-Nav", "Depth-NeRF", "RL + PINNs", "Perception", "ML in Robotics",
                                                          "Motion & Control", "Sim. Systems", "Kinematics", "Potential Field", "Freight Rates",
                                                          "Beale / Metaheur."]),
    ]),
]


def matrix():
    rowh, left, colw, top = 24, 420, 56, 138
    nrows = sum(len(g[2]) for g in GROUPS) + len(GROUPS) * 1
    W = left + colw * len(REPOS) + 110
    H = top + nrows * rowh + 40
    s = [head(W, H, "Skill evidence map: which repositories demonstrate which skills",
              "Matrix of skills versus repositories; a dot means the repository contains working code for that skill.")]
    s.append(f'<rect width="{W}" height="{H}" rx="16" fill="{BG0}"/>')
    s.append(text(28, 38, "SKILL EVIDENCE MAP", 14, TEAL, "bold", font=MONO, extra='letter-spacing="2"'))
    s.append(text(28, 60, "A dot = a public repository with working code for that skill. No self-ratings.", 12.5, MUTED, font=MONO))
    for i, name in enumerate(REPOS):
        cx = left + i * colw + colw / 2
        s.append(f'<g transform="translate({cx},{top - 12}) rotate(-45)">{text(0, 0, name, 12, TEXT, "600", "start")}</g>')
    y = top
    ri = 0
    for gname, gcol, rows in GROUPS:
        s.append(f'<rect x="20" y="{y - 3}" width="{W - 40}" height="{rowh - 2}" rx="6" fill="{gcol}" opacity=".13"/>')
        s.append(text(30, y + 14, gname, 11.5, gcol, "bold", font=MONO, extra='letter-spacing="1.5"'))
        y += rowh
        for label, repos in rows:
            s.append(text(30, y + 14, label, 12.5, TEXT))
            s.append(f'<line x1="{left}" y1="{y + rowh - 4}" x2="{left + colw * len(REPOS)}" y2="{y + rowh - 4}" stroke="{GRID}" stroke-width="1" opacity=".7"/>')
            for rp in repos:
                cx = left + R[rp] * colw + colw / 2
                d = 0.05 * R[rp] + 0.03 * ri
                if STATIC:
                    s.append(f'<circle cx="{cx}" cy="{y + 9}" r="7" fill="{gcol}"/>')
                    continue
                s.append(f'<circle cx="{cx}" cy="{y + 9}" r="0" fill="{gcol}"><animate attributeName="r" values="0;7;7;0" keyTimes="0;.05;.93;1" dur="14s" begin="{d:.2f}s" repeatCount="indefinite"/>'
                         f'<title>{esc(label)} - {esc(rp)}</title></circle>')
            s.append(text(left + colw * len(REPOS) + 22, y + 14, f"{len(repos)}", 12.5, gcol, "bold", font=MONO))
            y += rowh
            ri += 1
    s.append(text(left + colw * len(REPOS) + 22, top - 18, "repos", 11, MUTED, font=MONO))
    s.append("</svg>")
    return "".join(s)


def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf8") as f:
        f.write(content)
    print("wrote", name, f"{len(content) / 1024:.1f} KB")


if __name__ == "__main__":
    write("banner.svg", banner())
    write("results-console.svg", console())
    write("skill-evidence-map.svg", matrix())
    pipeline("pipeline-thesis.svg", "MSC THESIS · FEW-SHOT STRUCTURAL DEFECT DETECTION",
             [("Base detector", "YOLOv8n · 4 classes", "1,120 images · 0.79 mAP@50"),
              ("Few-shot adaptation", "novel class: crack", "K = 5, 7, 10, 20, 30"),
              ("Distillation", "T = 4 · α = 0.7", "base model as teacher"),
              ("Robustness suite", "6 perturbations", "x 3 severities"),
              ("Annotation audit", "missed / mislocated", "swapped labels")],
             [BLUE, TEAL, AMBER, CORAL, VIOLET])
    pipeline("pipeline-procuraai.svg", "PROCURAAI · AUDIT PIPELINE · LANGGRAPH ORCHESTRATION",
             [("Ingest", "PDF · scan · ZIP", "text layer, OCR fallback"),
              ("Extract", "Pydantic records", "rules or optional Gemini"),
              ("Match", "supplier · product", "exact → alias → fuzzy"),
              ("Evidence (RAG)", "FAISS + BM25", "verified citations"),
              ("Audit", "Decimal engine", "3-way match · tolerances"),
              ("Review + report", "human queue", "JSON · MD · CSV · XLSX")],
             [BLUE, VIOLET, AMBER, TEAL, CORAL, GREEN])
    pipeline("pipeline-pm25.svg", "HYBRID ARIMAX-LSTM · PM2.5 FORECASTING FOR ROBOT-ASSISTED MONITORING",
             [("Data", "12 Beijing stations", "hourly 2013-2017"),
              ("Preprocess", "impute · scale", "seasonal decomp · ADF"),
              ("ARIMAX", "linear + seasonal", "exogenous inputs"),
              ("LSTM", "2 layers on residuals", "nonlinear correction"),
              ("Monitoring policy", "patrol → emergency", "simulated robot")],
             [BLUE, AMBER, TEAL, VIOLET, CORAL])

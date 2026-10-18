"""Shared SVG illustration toolkit for the book. Each figure: d = Fig(name, title, sub, w, h); d.add(...); d.save()"""
import html, os
NAVY, ORANGE, BLUE, GREEN, RED, PURPLE, TEAL, GRAY, INK, MUTED = "#0D2847", "#E65100", "#1565C0", "#2E7D32", "#C62828", "#6A1B9A", "#00796B", "#546E7A", "#1d1d1f", "#55657a"
TINT = {NAVY: "#e8edf5", ORANGE: "#fff3e0", BLUE: "#e3f2fd", GREEN: "#e8f5e9", RED: "#ffebee", PURPLE: "#f3e5f5", TEAL: "#e0f2f1", GRAY: "#eceff1"}
LINE = {NAVY: "#c5cfe0", ORANGE: "#ffcc80", BLUE: "#90caf9", GREEN: "#a5d6a7", RED: "#ef9a9a", PURPLE: "#ce93d8", TEAL: "#80cbc4", GRAY: "#cfd8dc"}
DEFS = """<defs>
<linearGradient id="pcb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2f7d46"/><stop offset="1" stop-color="#1b5631"/></linearGradient>
<linearGradient id="metal" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9aa4ad"/><stop offset=".5" stop-color="#eef1f3"/><stop offset="1" stop-color="#8a949d"/></linearGradient>
<linearGradient id="shield" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f3f5f7"/><stop offset="1" stop-color="#aab3bb"/></linearGradient>
<linearGradient id="dev" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f1f3f5"/><stop offset="1" stop-color="#b8c3cb"/></linearGradient>
<linearGradient id="dark" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#4a5d68"/><stop offset="1" stop-color="#263238"/></linearGradient>
<linearGradient id="yellow" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd54f"/><stop offset="1" stop-color="#ffb300"/></linearGradient>
<linearGradient id="glass" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3a4a5c"/><stop offset=".5" stop-color="#121a24"/><stop offset="1" stop-color="#05080c"/></linearGradient>
<linearGradient id="batt" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3b4652"/><stop offset="1" stop-color="#1f262e"/></linearGradient>
<linearGradient id="copper" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e8c06a"/><stop offset="1" stop-color="#b8892e"/></linearGradient>
<linearGradient id="water" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#64b5f6"/><stop offset="1" stop-color="#1e88e5"/></linearGradient>
<filter id="sh" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="#0b1a2b" flood-opacity=".18"/></filter>
<filter id="sh2" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#0b1a2b" flood-opacity=".25"/></filter>
""" + "".join(f'<marker id="a{c[1:]}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{c}"/></marker>' for c in [NAVY, ORANGE, BLUE, GREEN, RED, PURPLE, TEAL, GRAY, INK, "#ff5722", "#ffffff"]) + "</defs>"

def esc(s): return html.escape(str(s), quote=False)

class Fig:
    def __init__(s, name, title, sub="", w=1200, h=700, foot=""):
        s.name, s.w, s.h, s.el = name, w, h, []
        s.el.append(f'<rect width="{w}" height="{h}" fill="#fff"/>')
        s.el.append(f'<text x="40" y="52" font-size="30" font-weight="700" fill="{NAVY}">{esc(title)}</text>')
        if sub: s.el.append(f'<text x="40" y="84" font-size="17" fill="{MUTED}">{esc(sub)}</text>')
        if foot: s.el.append(f'<text x="40" y="{h-22}" font-size="15" fill="{MUTED}">{esc(foot)}</text>')
    def add(s, *x): s.el.extend(x); return s
    def save(s):
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s.w} {s.h}" width="{s.w}" height="{s.h}" font-family="Inter, DejaVu Sans, sans-serif">{DEFS}' + "\n".join(s.el) + "</svg>"
        open(f"/home/claude/svg/{s.name}.svg", "w").write(svg); QUEUE.append(s.name)
QUEUE = []

# ---------- primitives ----------
def T(x, y, s, size=16, c=INK, w=400, a="start", lh=1.35, mono=False, italic=False):
    lines = str(s).split("\n"); fam = ' font-family="DejaVu Sans Mono"' if mono else ""
    st = ' font-style="italic"' if italic else ""
    if len(lines) == 1: return f'<text x="{x}" y="{y}" font-size="{size}" fill="{c}" font-weight="{w}" text-anchor="{a}"{fam}{st}>{esc(s)}</text>'
    sp = "".join(f'<tspan x="{x}" dy="{0 if i == 0 else size*lh}">{esc(l)}</tspan>' for i, l in enumerate(lines))
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{c}" font-weight="{w}" text-anchor="{a}"{fam}{st}>{sp}</text>'
def R(x, y, w, h, fill="#fff", stroke="none", r=10, sw=2, sh=False, op=1, dash=None):
    f = ' filter="url(#sh)"' if sh else ""; d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{op}"{f}{d}/>'
def C(x, y, r, fill="#fff", stroke="none", sw=2): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def L(x1, y1, x2, y2, c=INK, sw=2, dash=None, arrow=False, cap="round"):
    d = f' stroke-dasharray="{dash}"' if dash else ""; m = f' marker-end="url(#a{c[1:]})"' if arrow else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}" stroke-linecap="{cap}"{d}{m}/>'
def P(d, fill="none", stroke=INK, sw=2, arrow=False, dash=None, op=1, join="round"):
    m = f' marker-end="url(#a{stroke[1:]})"' if arrow else ""; ds = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="{join}" stroke-linecap="round" opacity="{op}"{m}{ds}/>'
def PL(pts, c=INK, sw=2.5, arrow=False, dash=None):
    return P("M" + " L".join(f"{x} {y}" for x, y in pts), stroke=c, sw=sw, arrow=arrow, dash=dash)
def G(inner, tx=0, ty=0, sc=1, rot=0):
    return f'<g transform="translate({tx},{ty}) rotate({rot}) scale({sc})">' + "".join(inner if isinstance(inner, list) else [inner]) + "</g>"

# ---------- composite elements ----------
def badge(x, y, n, c=ORANGE, r=16, fs=15): return C(x, y, r, c, "#fff", 2) + T(x, y + fs * .36, n, fs, "#fff", 700, "middle")
def card(x, y, w, h, c=BLUE, title="", body="", n=None, head=None, tsz=20, bsz=15.5):
    """Tinted header card. head: height of coloured header area (for icons) or None."""
    o = [R(x, y, w, h, "#fff", LINE[c], 18, 2, True)]
    ty = y + 40
    if head:
        o += [f'<path d="M{x} {y+18} Q{x} {y} {x+18} {y} H{x+w-18} Q{x+w} {y} {x+w} {y+18} V{y+head} H{x} Z" fill="{TINT[c]}"/>']; ty = y + head + 38
    tx = x + 22
    if n is not None: o.append(badge(x + 36, ty - 7, n, c, 17)); tx = x + 64
    if title: o.append(T(tx, ty, title, tsz, c, 700))
    if body: o.append(T(x + 22, ty + 34, body, bsz, "#263238", 400, lh=1.42))
    return "".join(o)
def box(x, y, w, h, txt, c=BLUE, fs=16, tc="#fff", sub="", r=12, grad=True):
    o = [R(x, y, w, h, c, "none", r, 0, True)]
    lines = txt.split("\n"); n = len(lines) + (1 if sub else 0)
    y0 = y + h / 2 - (n - 1) * fs * .62 + fs * .35
    o.append(T(x + w / 2, y0, txt, fs, tc, 700, "middle", 1.25))
    if sub: o.append(T(x + w / 2, y0 + len(lines) * fs * 1.25, sub, fs - 2.5, "#ffffffcc", 400, "middle"))
    return "".join(o)
def softbox(x, y, w, h, txt, c=BLUE, fs=16, sub="", r=12):
    o = [R(x, y, w, h, TINT[c], LINE[c], r, 2)]
    lines = txt.split("\n"); y0 = y + h / 2 - (len(lines) - 1) * fs * .62 + fs * .35 - (10 if sub else 0)
    o.append(T(x + w / 2, y0, txt, fs, c, 700, "middle", 1.25))
    if sub: o.append(T(x + w / 2, y0 + len(lines) * fs * 1.3, sub, fs - 2.5, "#37474f", 400, "middle", 1.3))
    return "".join(o)
def note(x, y, w, h, txt, c=ORANGE, fs=15.5, icon="!"):
    return R(x, y, w, h, TINT[c], "none", 12) + R(x, y, 6, h, c, "none", 3) + C(x + 34, y + h / 2, 15, c) + T(x + 34, y + h / 2 + 6, icon, 17, "#fff", 800, "middle") + T(x + 62, y + h / 2 - (txt.count("\n")) * fs * .7 + fs * .35, txt, fs, "#263238", 400, lh=1.4)
def arrow(x1, y1, x2, y2, c=NAVY, sw=3): return L(x1, y1, x2, y2, c, sw, arrow=True)
def flow(x, y, items, w=160, h=90, gap=36, colors=None, fs=15, subs=None, subfs=13.5):
    """horizontal step flow of boxes with numbered badges and arrows; subs = caption under each"""
    o = []
    for i, t in enumerate(items):
        c = colors[i] if colors else BLUE; bx = x + i * (w + gap)
        o.append(box(bx, y, w, h, t, c, fs))
        o.append(badge(bx + 18, y + 2, i + 1, NAVY, 14, 13))
        if subs: o.append(T(bx + w / 2, y + h + 26, subs[i], subfs, "#37474f", 400, "middle", 1.35))
        if i < len(items) - 1: o.append(arrow(bx + w + 5, y + h / 2, bx + w + gap - 5, y + h / 2, GRAY, 3))
    return "".join(o)
def check(x, y, s=16, c=GREEN): return C(x, y, s, c) + P(f"M{x-s*.45} {y} L{x-s*.1} {y+s*.38} L{x+s*.5} {y-s*.35}", stroke="#fff", sw=s * .22)
def cross(x, y, s=16, c=RED): return C(x, y, s, c) + P(f"M{x-s*.38} {y-s*.38} L{x+s*.38} {y+s*.38} M{x+s*.38} {y-s*.38} L{x-s*.38} {y+s*.38}", stroke="#fff", sw=s * .22)
def warn(x, y, s=30, c="#f9a825"):
    return P(f"M{x} {y-s*.55} L{x+s*.6} {y+s*.5} L{x-s*.6} {y+s*.5} Z", fill=c, stroke=c, sw=4) + T(x, y + s * .38, "!", s * .62, "#263238", 800, "middle")
def leader(ax, ay, lx, ly, n, title, sub="", c=ORANGE, tw=19):
    o = [P(f"M{ax} {ay} L{lx-40} {ly} L{lx-22} {ly}", stroke=c, sw=2), C(ax, ay, 5, c, "#fff", 1.5), badge(lx, ly, n, c)]
    o.append(T(lx + 28, ly - (4 if sub else -6), title, tw, INK, 700))
    if sub: o.append(T(lx + 28, ly + 19, sub, 15, MUTED))
    return "".join(o)

# ---------- objects ----------
def multimeter(x, y, val="0.412", mode="diode", sc=1, unit=""):
    o = [R(0, 0, 150, 230, "url(#yellow)", "#c49000", 22, 2, True), R(16, 16, 118, 62, "#263238", "#111", 8, 2),
         T(75, 58, val, 26, "#76ff03", 700, "middle", mono=True), T(75, 102, mode, 15, "#3e2723", 700, "middle"),
         C(75, 150, 34, "#37474f", "#263238", 3), R(71, 120, 8, 26, "#eceff1", "none", 4),
         C(38, 205, 10, "#212121"), C(75, 205, 10, "#c62828"), C(112, 205, 10, "#212121")]
    if unit: o.append(T(126, 72, unit, 13, "#76ff03", 700, "end"))
    return G(o, x, y, sc)
def meter_lead(x1, y1, x2, y2, c=RED, bend=60):
    """probe lead from meter socket (x1,y1) to probe tip (x2,y2)"""
    mx = (x1 + x2) / 2
    return P(f"M{x1} {y1} C{x1} {y1+bend} {x2} {y2+bend*1.6} {x2} {y2+28}", stroke=c, sw=3.5) + probe_tip(x2, y2, c)
def probe_tip(x, y, c=RED):
    return R(x - 6, y + 22, 12, 44, c, "none", 5) + P(f"M{x} {y+22} L{x} {y}", stroke="#90a4ae", sw=3) + C(x, y, 3, "#cfd8dc")
def pcb(x, y, w, h, r=12, sh=True): return R(x, y, w, h, "url(#pcb)", "#123d22", r, 2, sh)
def trace(pts, w=5): return PL(pts, "#d4af37", w)
def chip(x, y, w, h, label="", fs=13, bga=False, pins=True):
    o = [R(x, y, w, h, "#263238", "#111", 4, 1.5)]
    if pins and not bga:
        n = max(3, int(w // 14))
        for i in range(n):
            px = x + (i + .5) * w / n
            o += [R(px - 3, y - 6, 6, 6, "#cfd8dc", "none", 1), R(px - 3, y + h, 6, 6, "#cfd8dc", "none", 1)]
    if bga:
        n = max(4, int(w // 16))
        for i in range(n): o.append(C(x + (i + .5) * w / n, y + h + 5, 5, "#cfd8dc", "#78909c", 1))
    o.append(C(x + 9, y + 9, 3, "#455a64"))
    if label: o.append(T(x + w / 2, y + h / 2 + fs * .36, label, fs, "#cfd8dc", 700, "middle"))
    return "".join(o)
def smd(x, y, w=36, h=18, body="#8d6e4a", vertical=False):
    if vertical: w, h = h, w
    o = [R(x, y, w, h, body, "#4e342e", 2, 1)]
    if vertical: o += [R(x, y, w, h * .22, "#cfd8dc", "none", 1), R(x, y + h * .78, w, h * .22, "#cfd8dc", "none", 1)]
    else: o += [R(x, y, w * .22, h, "#cfd8dc", "none", 1), R(x + w * .78, y, w * .22, h, "#cfd8dc", "none", 1)]
    return "".join(o)
def coil(x, y, s=34): return R(x, y, s, s, "#455a64", "#263238", 4, 1.5) + C(x + s / 2, y + s / 2, s * .3, "#607d8b") + T(x + s / 2, y + s / 2 + 4, "", 10)
def phone(x, y, w=110, h=200, screen="#4fc3f7", on=True, rot=0):
    o = [R(0, 0, w, h, "#1d2630", "#0b1118", w * .14, 3, True), R(7, 9, w - 14, h - 18, screen if on else "#0b1118", "none", w * .09, 0), C(w / 2, 18, 3, "#0b1118")]
    return G(o, x, y, 1, rot)
def battery(x, y, w=150, h=80, label="Li-ion 3.85 V"):
    return R(x, y, w, h, "url(#batt)", "#0d1115", 10, 2, True) + R(x + w, y + h * .32, 8, h * .36, "#37474f", "none", 2) + R(x + 12, y + h * .22, w * .55, h * .56, ORANGE, "none", 6) + T(x + 12 + w * .275, y + h / 2 + 5, label, 12, "#fff", 700, "middle")
def psu(x, y, v="4.00", a="0.000", sc=1):
    o = [R(0, 0, 200, 140, "url(#dev)", "#78909c", 12, 2, True), R(16, 16, 120, 66, "#102027", "none", 6),
         T(76, 44, v + " V", 20, "#76ff03", 700, "middle", mono=True), T(76, 72, a + " A", 20, "#ff5252", 700, "middle", mono=True),
         C(166, 36, 15, "#37474f"), C(166, 84, 15, "#37474f"), C(46, 114, 10, "#c62828"), C(96, 114, 10, "#212121"), T(152, 122, "DC SUPPLY", 10, "#546e7a", 700, "middle")]
    return G(o, x, y, sc)
def nozzle(x, y, sc=1, hot=True):
    o = [R(-18, -70, 36, 56, "#455a64", "none", 6), P("M-22 -14 H22 L14 20 H-14 Z", fill="url(#metal)", stroke="#607d8b", sw=1.5)]
    if hot: o.append(P("M-8 28 l-6 22 M0 28 v24 M8 28 l6 22", stroke="#ff5722", sw=4))
    return G(o, x, y, sc)
def iron(x, y, rot=0, sc=1):
    return G([R(0, -8, 120, 16, BLUE, "none", 8), R(-6, -10, 14, 20, "#0d47a1", "none", 4), R(120, -4, 46, 8, "url(#metal)", "none", 2), P("M166 -4 L184 0 L166 4 Z", fill="#78909c", stroke="#78909c", sw=1)], x, y, sc, rot)
def flame(x, y, s=1):
    return G([P("M0 0 C-14 -14 -4 -26 -8 -44 C8 -32 14 -20 10 -8 C16 -12 18 -22 16 -28 C28 -14 26 6 4 10 Z", fill="#ff7043", stroke="none"), P("M0 6 C-4 -2 2 -8 0 -16 C8 -10 10 -2 4 6 Z", fill="#ffca28", stroke="none")], x, y, s)
def gnd(x, y, c=INK): return L(x, y, x, y + 12, c, 2) + L(x - 14, y + 12, x + 14, y + 12, c, 2.5) + L(x - 9, y + 18, x + 9, y + 18, c, 2.5) + L(x - 4, y + 24, x + 4, y + 24, c, 2.5)
def cap_sym(x, y, c=INK, lab=""):  # vertical capacitor symbol centred at x, from y (top) ~ 40 high
    return L(x, y, x, y + 16, c, 2) + L(x - 16, y + 16, x + 16, y + 16, c, 3) + L(x - 16, y + 24, x + 16, y + 24, c, 3) + L(x, y + 24, x, y + 40, c, 2) + (T(x + 22, y + 26, lab, 14, c, 600) if lab else "")
def res_sym(x, y, w=60, c=INK, lab=""):  # horizontal resistor box
    return R(x, y - 9, w, 18, "#fff", c, 2, 2) + (T(x + w / 2, y - 16, lab, 14, c, 600, "middle") if lab else "")
def coil_sym(x, y, n=4, c=INK, lab=""):
    d = f"M{x} {y}" + "".join(f" a9 9 0 0 1 18 0" for _ in range(n))
    return P(d, stroke=c, sw=2.5) + (T(x + n * 9, y - 16, lab, 14, c, 600, "middle") if lab else "")
def diode_sym(x, y, c=INK, lab=""):
    return P(f"M{x} {y-12} L{x+20} {y} L{x} {y+12} Z", fill=c, stroke=c, sw=1.5) + L(x + 20, y - 12, x + 20, y + 12, c, 3) + (T(x + 10, y - 18, lab, 14, c, 600, "middle") if lab else "")
def usb_c(x, y, w=90, h=34):
    return R(x, y, w, h, "url(#metal)", "#607d8b", h / 2, 2) + R(x + 12, y + h * .32, w - 24, h * .36, "#263238", "none", h * .18)
def scale_bar(x, y, w, segs, h=40):
    """segs: list of (fraction, color, label_top, label_bottom)"""
    o = []; cx = x
    for f, c, lt, lb in segs:
        sw_ = w * f; o.append(R(cx, y, sw_, h, c, "#fff", 0, 2))
        if lt: o.append(T(cx + sw_ / 2, y + h / 2 + 6, lt, 14, "#fff", 700, "middle"))
        if lb: o.append(T(cx + sw_ / 2, y + h + 26, lb, 13.5, "#37474f", 400, "middle", 1.3))
        cx += sw_
    return "".join(o)

def render_all():
    import subprocess
    if QUEUE: subprocess.run(["python3", "/home/claude/svg/render.py"] + QUEUE, check=True)

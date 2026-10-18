from sv import *
SCH = "#1a237e"  # schematic ink
def sheet(x, y, w, h):
    gid = f"g{x}{y}"
    return (f'<defs><pattern id="{gid}" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0 V20 H0" stroke="#e3e8ef" stroke-width="1" fill="none"/></pattern></defs>'
            + R(x, y, w, h, "#fbfcfe", "#c5cfe0", 14, 2, True) + R(x, y, w, h, f"url(#{gid})", "none", 14))
def net(x, y, name, c=BLUE, dir=1):
    w = 14 + len(name) * 9
    if dir > 0: return L(x - 20, y, x, y, SCH, 2.5) + P(f"M{x} {y-11} H{x+w} L{x+w+12} {y} L{x+w} {y+11} H{x} Z", fill=TINT[c], stroke=c, sw=2) + T(x + 8, y + 5, name, 14, c, 700)
    return P(f"M{x} {y-11} H{x-w} L{x-w-12} {y} L{x-w} {y+11} H{x} Z", fill=TINT[c], stroke=c, sw=2) + T(x - w + 2, y + 5, name, 14, c, 700)
def dot(x, y): return C(x, y, 5, SCH)
def zig(x, y, w=50, c=SCH):
    n = 6; st = w / n; d = f"M{x} {y}" + "".join(f" L{x+st*(i+.5)} {y+(-9 if i%2==0 else 9)}" for i in range(n)) + f" L{x+w} {y}"
    return P(d, stroke=c, sw=2.5)
def vcap(x, y, c=SCH): return L(x, y, x, y + 14, c, 2.5) + L(x - 14, y + 14, x + 14, y + 14, c, 3) + L(x - 14, y + 22, x + 14, y + 22, c, 3) + L(x, y + 22, x, y + 36, c, 2.5)
def vdiode(x, y, c=SCH, zen=False):  # cathode up (towards line)
    o = L(x, y, x, y + 10, c, 2.5) + P(f"M{x-12} {y+32} L{x+12} {y+32} L{x} {y+12} Z", fill=c, stroke=c, sw=1.5) + L(x - 12, y + 12, x + 12, y + 12, c, 3) + L(x, y + 32, x, y + 44, c, 2.5)
    if zen: o += L(x - 12, y + 12, x - 16, y + 7, c, 3) + L(x + 12, y + 12, x + 16, y + 17, c, 3)
    return o
def sgnd(x, y, c=SCH): return gnd(x, y, c)

# ---------- three views ----------
d = Fig("s4_three_views", "Schematic, board view and bitmap: three ways to see one circuit", "Professionals use the schematic to understand and the board view to locate. Open both at the same time.", 1200, 540)
for i, (t, s, c) in enumerate([("SCHEMATIC", "how parts connect", BLUE), ("BOARD VIEW", "where parts sit", PURPLE), ("BITMAP", "photo-like map with values", GREEN)]):
    x = 40 + i * 380
    d.add(R(x, 110, 360, 400, "#fff", LINE[c], 18, 2, True), T(x + 180, 152, t, 22, c, 800, "middle"), T(x + 180, 178, s, 15, MUTED, 400, "middle"))
x = 40
d.add(sheet(x + 24, 200, 312, 220), T(x + 50, 265, "VBAT", 15, RED, 700), L(x + 50, 280, x + 120, 280, SCH, 2.5), zig(x + 120, 280, 60), L(x + 180, 280, x + 300, 280, SCH, 2.5), T(x + 150, 262, "R1201", 13, SCH, 600, "middle"))
d.add(dot(x + 250, 280), vcap(x + 250, 280), sgnd(x + 250, 316), T(x + 268, 312, "C1202", 13, SCH, 600))
d.add(T(x + 180, 470, "Symbols and net names.\nUse it to understand\nhow the circuit works.", 16, "#263238", 400, "middle"))
x = 420
d.add(R(x + 24, 200, 312, 220, "#0e1116", "none", 12), R(x + 40, 216, 280, 188, "none", "#2b3a4a", 6, 1.5))
for (px, py, w, h, c) in [(80, 300, 30, 16, "#ffd54f"), (180, 296, 16, 26, "#ffd54f"), (240, 240, 60, 50, "#90a4ae"), (60, 360, 70, 30, "#90a4ae"), (190, 360, 24, 14, "#90a4ae")]:
    d.add(R(x + px, py, w, h, "none", c, 2, 2))
d.add(PL([(x + 110, 308), (x + 180, 308)], "#00e676", 3), T(x + 92, 290, "R1201", 12, "#ffd54f", 700), T(x + 180, 345, "C1202", 12, "#ffd54f", 700))
d.add(T(x + 180, 470, "Real positions. Click a pin\nand its whole net lights up.\nUse it to find the part.", 16, "#263238", 400, "middle"))
x = 800
d.add(pcb(x + 24, 200, 312, 220, 12, False), R(x + 80, 300, 30, 16, "#8d6e4a"), R(x + 80, 300, 7, 16, "#cfd8dc"), R(x + 103, 300, 7, 16, "#cfd8dc"), R(x + 180, 296, 16, 26, "#8d6e4a"), R(x + 240, 240, 60, 50, "#263238", "none", 3), R(x + 60, 360, 70, 30, "#263238", "none", 3))
d.add(T(x + 95, 292, "10K", 12, "#ffeb3b", 700, "middle"), T(x + 188, 340, "1uF", 12, "#ffeb3b", 700, "middle"), T(x + 270, 270, "U1201", 11, "#cfd8dc", 700, "middle"))
d.add(T(x + 180, 470, "Looks like the real board,\nwith part values printed.\nGood for quick checks.", 16, "#263238", 400, "middle"))
d.save()

# ---------- Figure 4.1 symbols ----------
d = Fig("s4_fig1", "Figure 4.1  Common schematic symbols and their letters", "The letter in front of a part name tells you what kind of part it is.", 1200, 860)
cells = []
def cell(i, label, letter, draw):
    cx, cy = 40 + (i % 4) * 285, 110 + (i // 4) * 172
    d.add(R(cx, cy, 265, 152, "#fff", "#dfe5ec", 14, 2, True), G(draw, cx + 132, cy + 58), T(cx + 132, cy + 116, label, 15.5, "#263238", 600, "middle"), T(cx + 132, cy + 140, letter, 15, RED, 800, "middle"))
cell(0, "Resistor", "R", [L(-60, 0, -30, 0, SCH, 2.5), zig(-30, 0, 60), L(30, 0, 60, 0, SCH, 2.5)])
cell(1, "Capacitor", "C", [L(-60, 0, -6, 0, SCH, 2.5), L(-6, -18, -6, 18, SCH, 3.5), L(6, -18, 6, 18, SCH, 3.5), L(6, 0, 60, 0, SCH, 2.5)])
cell(2, "Polarised capacitor", "C", [L(-60, 0, -6, 0, SCH, 2.5), L(-6, -18, -6, 18, SCH, 3.5), P("M10 -18 Q2 0 10 18", stroke=SCH, sw=3.5), L(4, 0, 60, 0, SCH, 2.5), T(-18, -16, "+", 16, SCH, 700, "middle")])
cell(3, "Coil / inductor", "L", [L(-60, 0, -36, 0, SCH, 2.5), coil_sym(-36, 0, 4, SCH), L(36, 0, 60, 0, SCH, 2.5)])
cell(4, "Diode", "D", [L(-60, 0, -12, 0, SCH, 2.5), P("M-12 -14 L12 0 L-12 14 Z", fill=SCH, stroke=SCH, sw=1.5), L(12, -14, 12, 14, SCH, 3.5), L(12, 0, 60, 0, SCH, 2.5)])
cell(5, "Zener / TVS diode", "D / VD", [L(-60, 0, -12, 0, SCH, 2.5), P("M-12 -14 L12 0 L-12 14 Z", fill=SCH, stroke=SCH, sw=1.5), P("M7 -18 L12 -14 V14 L17 18", stroke=SCH, sw=3), L(12, 0, 60, 0, SCH, 2.5)])
cell(6, "LED", "LED / D", [L(-60, 0, -12, 0, SCH, 2.5), P("M-12 -14 L12 0 L-12 14 Z", fill=SCH, stroke=SCH, sw=1.5), L(12, -14, 12, 14, SCH, 3.5), L(12, 0, 60, 0, SCH, 2.5), L(2, -20, 14, -32, ORANGE, 2.5, arrow=True), L(12, -16, 24, -28, ORANGE, 2.5, arrow=True)])
cell(7, "Fuse", "F", [L(-60, 0, -26, 0, SCH, 2.5), R(-26, -10, 52, 20, "#fff", SCH, 2, 2.5), L(-26, 0, 26, 0, SCH, 2), L(26, 0, 60, 0, SCH, 2.5)])
cell(8, "NPN transistor", "Q", [C(0, 0, 26, "none", SCH, 2.5), L(-46, 0, -10, 0, SCH, 2.5), L(-10, -16, -10, 16, SCH, 4), L(-10, -6, 16, -24, SCH, 2.5), L(-10, 6, 16, 24, SCH, 2.5, arrow=True), T(-50, -6, "B", 12, SCH, 700), T(20, -26, "C", 12, SCH, 700), T(20, 36, "E", 12, SCH, 700)])
cell(9, "PNP transistor", "Q", [C(0, 0, 26, "none", SCH, 2.5), L(-46, 0, -10, 0, SCH, 2.5), L(-10, -16, -10, 16, SCH, 4), L(-10, -6, 16, -24, SCH, 2.5), L(16, 24, -8, 8, SCH, 2.5, arrow=True), T(-50, -6, "B", 12, SCH, 700), T(20, -26, "E", 12, SCH, 700), T(20, 36, "C", 12, SCH, 700)])
cell(10, "MOSFET (N-channel)", "Q", [L(-46, 6, -14, 6, SCH, 2.5), L(-14, -18, -14, 18, SCH, 3), L(-6, -18, -6, -8, SCH, 3), L(-6, -4, -6, 4, SCH, 3), L(-6, 8, -6, 18, SCH, 3), L(-6, -13, 20, -13, SCH, 2.5), L(-6, 13, 20, 13, SCH, 2.5), L(20, -13, 20, -30, SCH, 2.5), L(20, 13, 20, 30, SCH, 2.5), L(20, 0, -4, 0, SCH, 2.5, arrow=True), T(-50, 2, "G", 12, SCH, 700), T(26, -24, "D", 12, SCH, 700), T(26, 32, "S", 12, SCH, 700)])
cell(11, "Crystal", "Y / X", [L(-60, 0, -18, 0, SCH, 2.5), L(-18, -16, -18, 16, SCH, 3), R(-10, -18, 20, 36, "#fff", SCH, 1, 2.5), L(18, -16, 18, 16, SCH, 3), L(18, 0, 60, 0, SCH, 2.5)])
cell(12, "Switch / button", "S / SW / K", [L(-60, 6, -22, 6, SCH, 2.5), C(-20, 6, 4, "#fff", SCH, 2), L(-16, 4, 18, -14, SCH, 2.5), C(22, 6, 4, "#fff", SCH, 2), L(26, 6, 60, 6, SCH, 2.5)])
cell(13, "Battery", "BAT", [L(-60, 0, -8, 0, SCH, 2.5), L(-8, -20, -8, 20, SCH, 3), L(4, -10, 4, 10, SCH, 5), L(4, 0, 60, 0, SCH, 2.5), T(-18, -18, "+", 16, SCH, 700, "middle")])
cell(14, "Test point", "TP", [L(-60, 0, 0, 0, SCH, 2.5), C(12, 0, 12, "#fff", SCH, 3)])
cell(15, "Antenna", "ANT", [L(0, 30, 0, -10, SCH, 2.5), P("M-22 -30 L22 -30 L0 -6 Z", stroke=SCH, sw=2.5)])
y = 110 + 4 * 172
d.add(R(40, y, 1120, 60, TINT[NAVY], "none", 12), G([gnd(0, -12, SCH)], 90, y + 26), T(125, y + 36, "Ground (GND)", 16, "#263238", 600))
d.add(R(380, y + 12, 50, 36, "#fff", SCH, 2, 2.5), T(405, y + 36, "U", 16, SCH, 800, "middle"), T(445, y + 36, "IC (chip): letter U", 16, "#263238", 600))
d.add(net(760, y + 30, "VBAT"), T(860, y + 36, "Net label / off-page link", 16, "#263238", 600))
d.save()

# ---------- schematic page anatomy ----------
d = Fig("s4_schematic_page", "Parts of a schematic page", "Five things to look at on every page before you start tracing.", 1200, 680)
d.add(sheet(40, 110, 700, 530), R(70, 140, 640, 470, "none", "#90a4ae", 4, 1.5))
for i, c in enumerate("1234"): d.add(T(70 + (i + .5) * 160, 132, c, 14, MUTED, 700, "middle"))
for i, c in enumerate("ABC"): d.add(T(54, 140 + (i + .5) * 156, c, 14, MUTED, 700, "middle"))
d.add(R(300, 250, 140, 200, "#fffde7", SCH, 4, 2.5), T(370, 238, "U1501", 16, SCH, 800, "middle"), T(370, 350, "CHARGER", 13, SCH, 600, "middle"))
for y in (290, 330, 370, 410): d.add(L(260, y, 300, y, SCH, 2.5), L(440, y, 480, y, SCH, 2.5))
d.add(net(500, 290, "VIO_1V8", PURPLE), L(480, 290, 500, 290, SCH, 2.5))
d.add(L(160, 290, 260, 290, SCH, 2.5), dot(200, 290), vcap(200, 290), sgnd(200, 326), T(186, 312, "C1520\n10uF", 14, SCH, 600, "end"))
d.add(R(470, 520, 230, 80, "#fff", SCH, 2, 2), L(470, 548, 700, 548, SCH, 1.5), T(482, 540, "CHARGER  ·  SHEET 05 / 22", 13, SCH, 800), T(482, 570, "Model X  ·  REV 1.1", 13, SCH, 400), T(482, 590, "2025-03-14", 12, MUTED))
calls = [(370, 228, "Reference designator", "U = IC. Numbers group parts by area."), (600, 290, "Net label", "Same name = connected, even on another page"), (230, 132, "Grid zones", "'C3' tells you where on the page"),
         (150, 350, "Value and part name", "C1520 is a 10 µF capacitor"), (585, 560, "Title block", "Sheet name, page number, revision")]
pos = [(445, 236), (612, 262), (230, 132), (120, 300), (455, 522)]
for i, (ax, ay, t, s) in enumerate(calls): d.add(badge(pos[i][0], pos[i][1], i + 1), badge(800, 160 + i * 98, i + 1), T(828, 154 + i * 98, t, 18, INK, 700), T(828, 177 + i * 98, s, 15, MUTED))
d.save()

# ---------- Figure 4.2 nets ----------
d = Fig("s4_fig2", "Figure 4.2  Nets, junctions and net labels", "Lines are nets (copper paths). A dot means the wires join. Two labels with the same name are the same net.", 1200, 520)
items = [("Crossing, no dot", "NOT connected", RED), ("Junction with dot", "CONNECTED", GREEN), ("Crossing with dot", "CONNECTED", GREEN), ("Same net name", "CONNECTED, far apart", GREEN)]
for i, (t, s, c) in enumerate(items):
    x = 40 + i * 285
    d.add(R(x, 110, 265, 360, "#fff", LINE[c], 16, 2, True), sheet(x + 20, 130, 225, 200))
    cx, cy = x + 132, 230
    if i == 0: d.add(L(cx - 80, cy, cx + 80, cy, SCH, 3), L(cx, cy - 80, cx, cy + 80, SCH, 3))
    if i == 1: d.add(L(cx - 80, cy, cx + 80, cy, SCH, 3), L(cx, cy - 80, cx, cy, SCH, 3), C(cx, cy, 7, SCH))
    if i == 2: d.add(L(cx - 80, cy, cx + 80, cy, SCH, 3), L(cx, cy - 80, cx, cy + 80, SCH, 3), C(cx, cy, 7, SCH))
    if i == 3: d.add(L(cx - 90, cy - 40, cx - 30, cy - 40, SCH, 3), net(cx - 30, cy - 40, "VBAT"), L(cx - 90, cy + 40, cx - 30, cy + 40, SCH, 3), net(cx - 30, cy + 40, "VBAT"), P(f"M{cx+60} {cy-28} C{cx+90} {cy-10} {cx+90} {cy+10} {cx+60} {cy+28}", stroke=GREEN, sw=2.5, dash="5 5"))
    d.add(T(x + 132, 375, t, 18, "#263238", 700, "middle"), (check if c == GREEN else cross)(x + 40, 422, 14), T(x + 62, 428, s, 15, c, 700))
d.save()

# ---------- Figure 4.3 simple circuit ----------
d = Fig("s4_fig3", "Figure 4.3  Reading a simple circuit: battery, resistor, LED", "", 1200, 560)
d.add(sheet(40, 100, 620, 420))
d.add(PL([(140, 290), (140, 180), (260, 180)], SCH, 3), zig(260, 180, 80), PL([(340, 180), (520, 180), (520, 270)], SCH, 3))
d.add(P("M506 270 L534 270 L520 296 Z", fill=SCH, stroke=SCH, sw=1.5), L(506, 296, 534, 296, SCH, 3.5), PL([(520, 296), (520, 420), (140, 420), (140, 318)], SCH, 3))
d.add(L(545, 268, 565, 252, ORANGE, 2.5, arrow=True), L(550, 284, 570, 268, ORANGE, 2.5, arrow=True))
d.add(L(110, 290, 170, 290, SCH, 4), L(124, 318, 156, 318, SCH, 6), T(176, 290, "+", 18, SCH, 700))
d.add(T(300, 160, "R1", 17, SCH, 800, "middle"), T(300, 214, "220 Ω", 15, BLUE, 600, "middle"), T(80, 300, "BAT1\n3 V", 16, SCH, 800, "end"), T(555, 300, "D1 (LED)", 16, SCH, 800))
d.add(arrow(380, 160, 460, 160, RED, 2.5), T(420, 150, "current", 14, RED, 600, "middle"))
rows = [("R1, D1, BAT1", "part names"), ("220 Ω, 3 V", "values"), ("Lines", "nets (wires)"), ("Current", "from + of the battery, through R1 and D1, back to –")]
d.add(T(700, 140, "How to read it", 21, NAVY, 700))
for i, (a, b) in enumerate(rows): d.add(R(700, 165 + i * 80, 460, 66, TINT[BLUE] if i % 2 == 0 else "#fff", LINE[BLUE], 12, 1.5), T(720, 205 + i * 80, a, 17, BLUE, 700), T(860, 205 + i * 80, b if len(b) < 34 else "from + through R1, D1, back to –", 15.5, "#263238"))
d.save()

# ---------- Figure 4.4 charging schematic ----------
d = Fig("s4_fig4", "Figure 4.4  Example phone schematic: charging input", "Read it left to right, the way the current flows.", 1200, 700)
d.add(sheet(40, 100, 1120, 360))
d.add(R(70, 170, 90, 170, "#fff", SCH, 3, 2.5), T(115, 160, "J1", 16, SCH, 800, "middle"), T(150, 226, "VBUS", 12, SCH, 600, "end"), T(150, 306, "GND", 12, SCH, 600, "end"), T(115, 365, "USB port", 13, BLUE, 600, "middle"))
d.add(L(160, 220, 220, 220, SCH, 2.5), R(220, 211, 44, 18, "#fff", SCH, 2, 2.5), T(242, 200, "F1", 15, SCH, 800, "middle"), T(242, 250, "3 A", 13, BLUE, 600, "middle"), L(264, 220, 460, 220, SCH, 2.5))
d.add(PL([(160, 300), (190, 300), (190, 330)], SCH, 2.5), sgnd(190, 330))
d.add(T(320, 208, "VBUS_IN", 13, GREEN, 700, "middle"), dot(310, 220), vdiode(310, 220, SCH, True), sgnd(310, 264), T(326, 250, "D1", 14, SCH, 800), T(326, 268, "TVS", 12, BLUE, 600))
d.add(dot(380, 220), vcap(380, 220), sgnd(380, 256), T(398, 246, "C1", 14, SCH, 800), T(398, 264, "1 µF", 12, BLUE, 600))
d.add(R(460, 190, 120, 110, "#fff", SCH, 3, 2.5), T(520, 180, "U2  OVP", 15, SCH, 800, "middle"), T(470, 226, "IN", 12, SCH, 600), T(570, 226, "OUT", 12, SCH, 600, "end"), T(520, 290, "GND", 12, SCH, 600, "middle"), L(520, 300, 520, 320, SCH, 2.5), sgnd(520, 320))
d.add(L(580, 220, 840, 220, SCH, 2.5), T(660, 208, "CHG_IN", 13, GREEN, 700, "middle"), dot(650, 220), vcap(650, 220), sgnd(650, 256), T(668, 246, "C2", 14, SCH, 800), T(668, 264, "10 µF", 12, BLUE, 600))
d.add(dot(730, 220), L(730, 220, 730, 252, SCH, 2.5), C(730, 262, 10, "#fff", SCH, 2.5), T(746, 268, "TP1", 13, SCH, 800))
d.add(R(840, 170, 150, 200, "#fff", SCH, 3, 2.5), T(915, 160, "U3  Charging IC", 15, SCH, 800, "middle"), T(850, 226, "VBUS", 12, SCH, 600), T(980, 226, "VBAT", 12, SCH, 600, "end"), T(980, 316, "VSYS", 12, SCH, 600, "end"))
d.add(L(990, 220, 1020, 220, SCH, 2.5), net(1020, 220, "VBAT"), L(990, 310, 1020, 310, SCH, 2.5), net(1020, 310, "VPH_PWR"))
steps = ["Charger 5 V enters J1 pin VBUS.", "Fuse F1, TVS diode D1 and C1 protect and filter VBUS_IN.", "OVP chip U2 blocks voltage that is too high. Its output is CHG_IN (test point TP1).", "Charging IC U3 charges the battery (VBAT) and powers the phone (VPH_PWR)."]
for i, s in enumerate(steps): d.add(badge(70, 500 + i * 46, i + 1, BLUE, 15, 14), T(98, 506 + i * 46, s, 16.5, "#263238"))
d.save()

# ---------- Figure 4.5 power key ----------
d = Fig("s4_fig5", "Figure 4.5  Example phone schematic: power key", "", 1200, 660)
d.add(sheet(40, 90, 1120, 340))
d.add(R(70, 170, 90, 120, "#fff", SCH, 3, 2.5), T(115, 160, "J5", 16, SCH, 800, "middle"), T(150, 236, "PWR", 12, SCH, 600, "end"), T(115, 315, "side-key flex", 13, BLUE, 600, "middle"))
d.add(L(160, 230, 560, 230, SCH, 2.5), dot(230, 230), vdiode(230, 230, SCH), sgnd(230, 274), T(212, 262, "D3", 14, SCH, 800, "end"), T(212, 280, "ESD", 12, BLUE, 600, "end"))
d.add(dot(310, 230), vcap(310, 230), sgnd(310, 266), T(328, 256, "C20", 14, SCH, 800), T(328, 274, "100 nF", 12, BLUE, 600))
d.add(R(380, 230, 0, 0), zig(390, 230, 60), T(420, 210, "R15", 14, SCH, 800, "middle"), T(420, 262, "1 kΩ", 12, BLUE, 600, "middle"), T(500, 218, "KPD_PWR_N", 13, GREEN, 700, "middle"))
d.add(R(560, 150, 200, 220, "#fff", SCH, 3, 2.5), T(660, 140, "U1  PMIC", 15, SCH, 800, "middle"), T(570, 236, "KPD_PWR_N", 12, SCH, 600), T(750, 186, "VPH_PWR", 12, SCH, 600, "end"), T(750, 346, "GND", 12, SCH, 600, "end"))
d.add(L(760, 180, 800, 180, SCH, 2.5), net(800, 180, "VPH_PWR"), PL([(760, 340), (820, 340), (820, 360)], SCH, 2.5), sgnd(820, 360))
d.add(R(905, 140, 230, 250, "#fff", LINE[GREEN], 14, 2), T(1020, 172, "Measure KPD_PWR_N", 16, GREEN, 700, "middle"))
for i, (st, v, c) in enumerate([("Released", "≈ 1.8 V", GREEN), ("Pressed", "0 V", BLUE), ("Always", "0 V", RED)]):
    d.add(T(925, 220 + i * 50, st, 15, "#37474f", 600), T(1115, 220 + i * 50, v, 15, c, 800, "end"), L(925, 234 + i * 50, 1115, 234 + i * 50, "#eceff1", 1.5))
d.add(T(925, 360, "→ D3 or C20 shorted", 15, RED, 700))
d.add(note(40, 460, 1120, 150, "How it works: pressing the button on J5 connects the PWR line to ground. The PMIC sees\nKPD_PWR_N go low (_N means active-low) and starts the phone. If the phone will not\npower on, measure this net before replacing the PMIC.", BLUE, 16, "i"))
d.save()

# ---------- fault flow ----------
d = Fig("s4_fault_flow", "Using a schematic to find a fault", "Follow the current from where it enters to where it is missing. The first wrong reading marks the fault.", 1200, 330)
d.add(flow(40, 125, ["Symptom", "Find the\nsection", "Follow the\nnet", "Measure at\neach part", "First wrong\nreading", "Locate on\nboard view"], 160, 100, 32, [GRAY, BLUE, BLUE, TEAL, RED, GREEN], 16,
           ["e.g. not\ncharging", "charging\nsheet", "VBUS → fuse\n→ OVP → IC", "voltage or\ndiode mode", "= the fault\narea", "repair and\nre-test"], 14.5))
d.save()
render_all()

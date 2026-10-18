from sv import *
import math, random

def curve_path(pts): return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
def boot_pts(x0, y0, w, h, kind="normal", n=400):
    """returns list of screen points for a current trace; values in 0..1"""
    random.seed(3); out = []
    for i in range(n + 1):
        t = i / n
        if kind == "normal":
            if t < .05: v = 0
            elif t < .12: v = .2
            elif t < .3: v = .2 + .3 * math.sin((t - .12) / .18 * math.pi) + (t - .12) * .5
            elif t < .6: v = .55 + .12 * math.sin(t * 60) + .05 * random.random()
            else: v = .7 + .1 * math.sin(t * 90) + .04 * random.random()
        elif kind == "zero": v = 0
        elif kind == "high": v = 0 if t < .05 else .92
        elif kind == "blip": v = .18 if .1 < t < .2 else 0
        elif kind == "stuck": v = 0 if t < .08 else .3
        elif kind == "loop":
            p = (t % .33) / .33; v = 0 if p < .08 else (.3 + .25 * abs(math.sin(p * 30)) if p < .7 else .25)
        elif kind == "nodisp":
            v = 0 if t < .05 else min(.7, .2 + t * 1.4) + .1 * math.sin(t * 70)
        out.append((x0 + t * w, y0 + h - v * h))
    return out

# ---------- Ch7 boot curve stages ----------
d = Fig("s7_boot_curve", "What the current tells you: a normal power-on, stage by stage", "Where the current stops climbing shows you which stage failed.", 1200, 620)
X0, Y0, W, H = 110, 190, 1040, 330
stages = [(0, .05, "press\nkey", GRAY), (.05, .12, "PMIC\nstarts", ORANGE), (.12, .3, "CPU reads\nboot code", BLUE), (.3, .6, "logo, system\nloads", TEAL), (.6, .82, "Android\nstarts", PURPLE), (.82, 1, "idle,\nscreen on", GREEN)]
for a, b, t, c in stages:
    d.add(R(X0 + a * W, Y0, (b - a) * W, H, TINT[c], "none", 0), T(X0 + (a + b) / 2 * W, 140, t, 14.5, c, 700, "middle"))
d.add(L(X0, Y0 + H, X0 + W, Y0 + H, INK, 2), L(X0, Y0, X0, Y0 + H, INK, 2), P(curve_path(boot_pts(X0, Y0 + 20, W, H - 20)), stroke=RED, sw=3.5))
d.add(T(X0 + W / 2, Y0 + H + 34, "time after pressing power  →", 15, MUTED, 400, "middle"), f'<text x="70" y="{Y0+H/2}" font-size="15" fill="{MUTED}" text-anchor="middle" transform="rotate(-90 70 {Y0+H/2})">current (mA)</text>')
d.save()

# ---------- Figure 7.1 PSU setup ----------
d = Fig("s7_fig1", "Figure 7.1  Connecting a phone board to the DC power supply", "Set 4.0 V and a current limit of about 1–2 A. Check polarity before you switch on.", 1200, 600, "Use a boot cable for the model, or fine clips on the battery connector pins.")
d.add(psu(60, 170, "4.00", "0.000", 1.5))
d.add(pcb(560, 120, 580, 400), R(600, 150, 170, 110, "url(#shield)", "#90a4ae", 8, 2), T(685, 210, "PMIC", 15, "#546e7a", 700, "middle"), R(900, 300, 200, 140, "url(#shield)", "#90a4ae", 8, 2), T(1000, 375, "CPU", 15, "#546e7a", 700, "middle"))
d.add(R(640, 320, 150, 80, "#263238", "none", 6), *[R(652 + i * 22, 334, 12, 52, "#d4af37", "none", 2) for i in range(6)], T(715, 310, "battery connector", 14, "#e8f5e9", 700, "middle"))
d.add(T(806, 340, "VBAT +", 15, "#ffeb3b", 800), T(806, 392, "GND –", 15, "#e8f5e9", 800))
d.add(P("M129 341 C129 480 450 470 660 336", stroke=RED, sw=5), C(660, 336, 6, RED), P("M204 341 C204 540 500 530 760 392", stroke=INK, sw=5), C(760, 392, 6, INK))
d.add(T(600, 480, "phone board, battery removed", 14, "#e8f5e9", 600))
d.save()

# ---------- Figure 7.2 normal boot ----------
d = Fig("s7_fig2", "Figure 7.2  A healthy phone's current while booting (typical shape)", "Every model is a little different. Learn the shape of the phones you repair most.", 1200, 600)
X0, Y0, W, H = 120, 150, 1020, 340
labs = [(0, .05, "connect", GRAY), (.05, .15, "PMIC on", ORANGE), (.15, .3, "CPU starts", BLUE), (.3, .6, "reading storage", TEAL), (.6, 1, "booted: logo, then home screen", PURPLE)]
for a, b, t, c in labs: d.add(R(X0 + a * W, Y0, (b - a) * W, H, TINT[c], "none", 0), T(X0 + (a + b) / 2 * W, Y0 + 26, t, 13.5, c, 700, "middle"))
for i, v in enumerate([0, .1, .2, .3, .4]): yy = Y0 + H - v / .45 * H; d.add(L(X0, yy, X0 + W, yy, "#ffffff", 1), T(X0 - 10, yy + 5, f"{v:.2f}", 13, MUTED, 400, "end"))
for s in range(0, 21, 5): xx = X0 + s / 20 * W; d.add(T(xx, Y0 + H + 24, str(s), 13, MUTED, 400, "middle"))
d.add(L(X0, Y0 + H, X0 + W, Y0 + H, INK, 2), L(X0, Y0, X0, Y0 + H, INK, 2), P(curve_path(boot_pts(X0, Y0 + 60, W, H - 60)), stroke=BLUE, sw=3.5))
d.add(T(X0 + W / 2, Y0 + H + 52, "time (seconds)", 15, MUTED, 400, "middle"), f'<text x="58" y="{Y0+H/2}" font-size="15" fill="{MUTED}" text-anchor="middle" transform="rotate(-90 58 {Y0+H/2})">current (A)</text>')
d.add(P(f"M{X0+120} {Y0+180} L{X0+60} {Y0+H-70}", stroke=ORANGE, sw=2, arrow=True), T(X0 + 124, Y0 + 176, "press power key", 14, ORANGE, 700))
d.save()

# ---------- Figure 7.3 fault signatures ----------
d = Fig("s7_fig3", "Figure 7.3  Reading the current: six common fault patterns", "Press power and watch the ammeter. Each pattern points to a different part of the board.", 1200, 800)
pats = [("1", "Nothing moves", "zero", "0 A after pressing power", "Power key line, open VBAT path\n(fuse or coil), PMIC not starting", RED), ("2", "High current at once", "high", "high before or right after pressing", "Short on VBAT or a PMIC output\nline (Chapter 6)", RED),
        ("3", "Small jump, back to 0", "blip", "about 10–80 mA, then drops", "PMIC starts but does not hold:\ncrystal, a PMIC rail, CPU", ORANGE), ("4", "Stuck at one value", "stuck", "steady 50–150 mA, no change", "CPU runs but cannot boot:\nstorage (eMMC/UFS) or firmware", ORANGE),
        ("5", "Rises, drops, repeats", "loop", "boot loop pattern", "Storage, RAM, firmware, or a\nrail that collapses", PURPLE), ("6", "Normal pattern, no display", "nodisp", "boots like Figure 7.2", "Phone works inside: check the\ndisplay, backlight, connector", GREEN)]
for i, (n, t, k, cap, cause, c) in enumerate(pats):
    x = 40 + (i % 3) * 380; y = 110 + (i // 3) * 340
    d.add(R(x, y, 360, 320, "#fff", LINE[c], 16, 2, True), badge(x + 30, y + 32, n, c, 15, 14), T(x + 54, y + 38, t, 17.5, c, 700))
    d.add(R(x + 20, y + 60, 320, 130, "#f7f9fb", "none", 8), L(x + 30, y + 180, x + 330, y + 180, "#90a4ae", 1.5), L(x + 30, y + 70, x + 30, y + 180, "#90a4ae", 1.5))
    d.add(P(curve_path(boot_pts(x + 30, y + 74, 300, 104, k, 200)), stroke=c, sw=3))
    d.add(T(x + 22, y + 214, cap, 13.5, MUTED, 400, italic=True), T(x + 22, y + 246, cause, 15, "#263238", 400))
d.save()

# ---------- Ch7 USB meter ----------
d = Fig("s7_usb_meter", "Reading charging current with a USB meter", "The meter sits between the charger and the phone and shows what is really flowing.", 1200, 520)
d.add(R(60, 190, 150, 120, "url(#dev)", "#90a4ae", 16, 2, True), R(90, 170, 12, 26, "#90a4ae", "none", 2), R(168, 170, 12, 26, "#90a4ae", "none", 2), T(135, 260, "Charger", 16, NAVY, 700, "middle"), T(135, 282, "5 V / 9 V", 14, MUTED, 400, "middle"))
d.add(P("M210 250 C260 250 270 250 320 250", stroke=INK, sw=6))
d.add(R(320, 180, 200, 140, "url(#dark)", "#263238", 16, 2, True), R(340, 198, 160, 84, "#0b1418", "#37474f", 6, 2), T(420, 232, "5.08 V", 22, "#76ff03", 700, "middle", mono=True), T(420, 266, "1.62 A", 22, "#ffd54f", 700, "middle", mono=True), T(420, 345, "USB meter", 16, NAVY, 700, "middle"))
d.add(P("M520 250 C570 250 580 250 620 250", stroke=INK, sw=6), phone(620, 150, 110, 210, "#4fc3f7"), T(675, 260, "⚡", 34, "#fff", 700, "middle"))
rows = [("0 A", "not charging: port, cable, charging path", RED), ("0.1 – 0.4 A", "weak: dirty port, poor cable, CC line", ORANGE), ("1 – 2 A or more", "normal charging", GREEN), ("falls when nearly full", "normal behaviour", BLUE)]
for i, (a, b, c) in enumerate(rows):
    y = 130 + i * 80
    d.add(R(780, y, 380, 64, TINT[c], LINE[c], 12, 2), T(800, y + 28, a, 17, c, 800), T(800, y + 50, b, 14.5, "#37474f"))
d.save()

# ---------- Ch8 dead types ----------
d = Fig("s8_dead_types", "Dead, no display, or boot loop? Sort the phone first", "Each one needs a different path. Do not open the phone until you know which one you have.", 1200, 640)
d.add(box(430, 110, 340, 64, "Press power, plug in the charger", NAVY, 17))
cols = [("DEAD", "No vibration, no sound,\nno heat, 0 mA", "Power path, short,\nPMIC, CPU", RED, "zero"), ("NO DISPLAY", "Vibrates or rings,\nPC detects it,\nscreen stays black", "Screen, connector,\nbacklight, display line", ORANGE, "nodisp"), ("BOOT LOOP", "Logo shows, then\nrestarts again\nand again", "Software, battery,\nstorage, stuck button", PURPLE, "loop")]
for i, (name, sym, cause, c, k) in enumerate(cols):
    x = 40 + i * 380
    d.add(P(f"M600 176 C600 210 {x+180} 200 {x+180} 232", stroke=c, sw=3, arrow=True))
    d.add(R(x, 240, 360, 340, "#fff", LINE[c], 18, 2, True), R(x, 240, 360, 58, c, "none", 18), R(x, 280, 360, 18, c, "none", 0), T(x + 180, 278, name, 20, "#fff", 800, "middle"))
    d.add(phone(x + 30, 320, 80, 150, "#0b1118" if i < 2 else "#4fc3f7"), T(x + 130, 350, sym, 15.5, "#263238", 600))
    if i == 1: d.add(P(f"M{x+20} 340 q-8 10 0 20 M{x+12} 334 q-14 16 0 32", stroke=ORANGE, sw=2.5))
    if i == 2: d.add(P(f"M{x+70} 395 a14 14 0 1 1 -10 -14", stroke="#fff", sw=4, arrow=False), P(f"M{x+56} 375 l6 6 l-8 2", stroke="#fff", sw=3))
    d.add(L(x + 20, 494, x + 340, 494, "#eceff1", 2), T(x + 20, 524, "Look at:", 14, c, 800), T(x + 100, 524, cause, 15, "#263238"))
d.save()

# ---------- Figure 8.1 no-power flowchart ----------
d = Fig("s8_fig1", "Figure 8.1  No-power diagnosis flowchart", "Always do the cheap, simple checks first. Most 'dead' phones have a flat battery, a dirty port or a stuck power key.", 1200, 1060)
def step(x, y, w, h, t, c=BLUE): return R(x, y, w, h, TINT[c], LINE[c], 14, 2, True) + T(x + w / 2, y + h / 2 - (t.count("\n")) * 9 + 6, t, 16, "#1a2a3a", 600, "middle", 1.3)
def dia(cx, cy, w, h, t): return f'<path d="M{cx} {cy-h/2} L{cx+w/2} {cy} L{cx} {cy+h/2} L{cx-w/2} {cy} Z" fill="#fff3e0" stroke="{ORANGE}" stroke-width="2.5" filter="url(#sh)"/>' + T(cx, cy - (t.count("\n")) * 9 + 6, t, 15.5, "#4e2a00", 700, "middle", 1.3)
d.add(step(360, 110, 480, 66, "Customer: 'the phone is dead'\nAsk: water? drop? earlier repair? charging?", GRAY), arrow(600, 178, 600, 200, NAVY, 2.5))
d.add(step(360, 204, 480, 66, "1. Quick checks: charge 30 min, try a good battery,\nforce restart, check power key and port"), arrow(600, 272, 600, 292, NAVY, 2.5))
d.add(dia(600, 340, 300, 92, "Does it power\non now?"), arrow(752, 340, 860, 340, GREEN, 2.5), T(806, 330, "YES", 14, GREEN, 800, "middle"), step(864, 304, 280, 72, "Battery, port or key fault.\nRepair and test.", GREEN))
d.add(arrow(600, 388, 600, 420, RED, 2.5), T(616, 410, "NO", 14, RED, 800))
d.add(step(360, 424, 480, 66, "2. Open the phone. Check under the microscope for\ncorrosion, burnt or missing parts, bent shields"), arrow(600, 492, 600, 512, NAVY, 2.5))
d.add(step(360, 516, 480, 66, "3. Connect the DC power supply (4.0 V, 1 A limit).\nRead the current BEFORE pressing power."), arrow(600, 584, 600, 604, NAVY, 2.5))
d.add(dia(600, 652, 320, 92, "Current before\npressing power?"), arrow(762, 652, 860, 652, RED, 2.5), T(810, 642, "HIGH", 14, RED, 800, "middle"), step(864, 616, 280, 72, "Short on VBAT. Find it with\nvoltage injection (Chapter 6).", RED))
d.add(arrow(600, 700, 600, 732, GREEN, 2.5), T(616, 722, "0 mA", 14, GREEN, 800))
d.add(step(360, 736, 480, 60, "4. Press power and read the pattern (Figure 7.3)"), arrow(600, 798, 600, 816, NAVY, 2.5))
d.add(dia(600, 856, 300, 80, "What does the\ncurrent do?"))
outs = [(80, "Nothing moves", "Power key line, VBAT\nreaching the PMIC,\nfuse or coil, PMIC"), (440, "Jumps, then 0", "PMIC rails in diode\nmode, crystal,\nCPU / PMIC"), (800, "Stuck or loops", "Connect to PC. Detected?\nFlash. Not detected?\nCheck storage and rails")]
for x, t, s in outs:
    d.add(P(f"M600 896 C600 920 {x+160} 910 {x+160} 930", stroke=NAVY, sw=2.5, arrow=True), R(x, 934, 320, 92, "#fff8e1", "#ffcc80", 14, 2, True), T(x + 160, 958, t, 16, ORANGE, 800, "middle"), T(x + 160, 982, s, 13.5, "#37474f", 400, "middle", 1.3))
d.save()

# ---------- Figure 8.2 check points ----------
d = Fig("s8_fig2", "Figure 8.2  Where to measure on a no-power phone (simplified)", "Work along the numbers. The first reading that is wrong shows where the fault is.", 1200, 680)
d.add(R(50, 200, 160, 90, "url(#batt)", "none", 12, 0, True), T(130, 240, "Battery", 15, "#fff", 700, "middle"), T(130, 262, "connector", 15, "#fff", 700, "middle"))
d.add(L(210, 245, 300, 245, RED, 4), R(300, 222, 110, 46, "#6d4c41", "#3e2723", 8, 2), T(355, 251, "Fuse / coil", 14, "#fff", 700, "middle"), L(410, 245, 520, 245, RED, 4), T(255, 232, "VBAT", 14, RED, 800, "middle"))
d.add(R(520, 150, 220, 220, NAVY, "none", 16, 0, True), chip(570, 220, 120, 70, "PMIC", 16))
d.add(R(50, 470, 160, 80, "#546e7a", "none", 12, 0, True), T(130, 516, "Power key", 15, "#fff", 700, "middle"), PL([(210, 510), (400, 510), (400, 320), (520, 320)], BLUE, 3.5), T(300, 498, "PWRKEY", 13, BLUE, 700, "middle"))
d.add(PL([(740, 190), (860, 190)], GREEN, 3.5), T(870, 196, "Buck coils → CPU, RAM, storage", 15, GREEN, 700), PL([(740, 260), (860, 260)], GREEN, 3.5), T(870, 266, "LDO outputs (1.8 V, 2.8 V ...)", 15, GREEN, 700))
d.add(PL([(700, 370), (700, 470), (780, 470)], "#6d4c41", 3.5), R(780, 448, 120, 46, "url(#metal)", "#78909c", 8, 2), T(840, 477, "Crystal", 14, "#37474f", 800, "middle"), T(912, 476, "32.768 kHz /\nmain clock", 13.5, MUTED))
for n, (x, y) in enumerate([(160, 310), (465, 245), (400, 420), (800, 190), (800, 260), (700, 420)], 1): d.add(badge(x, y, n))
notes = ["VBAT at the connector: 3.7–4.2 V with the supply on", "VBAT after the fuse or coil: same as 1 (0 V means the fuse or coil is open)", "Power key line: voltage when released, drops to 0 when pressed", "Buck outputs: diode mode not 0 (short) and not OL (open)", "LDO outputs: same check as 4", "Crystal: check for damage, corrosion or a cracked part"]
for i, t in enumerate(notes): d.add(badge(64, 600 + (i % 3) * 34, i + 1, ORANGE, 12, 12) if False else "", T(50 + (i // 3) * 570, 604 + (i % 3) * 34, f"{i+1}.  {t}", 14.5, "#263238"))
d.save()

# ---------- Path B ----------
d = Fig("s8_pathB", "Path B: current jumps, then falls. Check the PMIC output lines", "Battery off. Measure in diode mode on the coil or capacitor of each line.", 1200, 560, "One open (OL) line can also stop the boot. Compare every reading with a good board.")
d.add(R(50, 170, 220, 260, NAVY, "none", 18, 0, True), chip(100, 260, 120, 76, "PMIC", 17))
rails = [("VDD_CPU (buck)", "0.42", True), ("VDD_1V8", "0.38", True), ("VDD_MEM", "0.004", False), ("LDO_2V8", "0.55", True)]
for i, (n, v, ok) in enumerate(rails):
    y = 190 + i * 70
    d.add(L(270, y + 20, 420, y + 20, INK, 3), coil(420, y + 3, 34), T(474, y + 27, n, 18, INK, 700))
    d.add(R(700, y, 140, 44, "#263238", "none", 8), T(770, y + 30, v, 22, "#76ff03" if ok else "#ff5252", 700, "middle", mono=True))
    d.add((check if ok else cross)(880, y + 22, 15), T(906, y + 28, "OK" if ok else "SHORT → Chapter 6", 17, GREEN if ok else RED, 800))
d.add(T(770, 170, "diode reading", 14, MUTED, 600, "middle"))
d.save()

# ---------- Path C ----------
d = Fig("s8_pathC", "Path C: stuck or boot loop. Is it software or storage?", "Connect the phone to a PC in boot or flash mode and see whether the tool detects it.", 1200, 560)
d.add(R(50, 210, 240, 140, "#fff", "#cfd8dc", 16, 2, True), R(80, 230, 180, 80, "#263238", "none", 6), R(90, 240, 160, 60, "#4fc3f7", "none", 3), R(130, 316, 80, 14, "#90a4ae", "none", 3), T(170, 340, "PC in flash mode", 14, NAVY, 700, "middle"))
d.add(P("M292 260 C340 260 340 190 390 190", stroke=GREEN, sw=3.5, arrow=True), P("M292 300 C340 300 340 380 390 380", stroke=RED, sw=3.5, arrow=True))
d.add(box(396, 140, 260, 100, "Detected", GREEN, 19, sub="port shows in the tool"), box(396, 330, 260, 100, "Not detected", RED, 19, sub="after checking the cable"))
d.add(arrow(660, 190, 700, 190, GREEN, 3), arrow(660, 380, 700, 380, RED, 3))
d.add(R(704, 130, 456, 120, TINT[GREEN], LINE[GREEN], 14, 2), T(726, 168, "Flash the correct firmware.", 17, GREEN, 700), T(726, 196, "Boots? It was software. Fixed.", 16, "#263238"), T(726, 222, "Still fails? Suspect storage.", 16, "#263238"))
d.add(R(704, 320, 456, 120, TINT[RED], LINE[RED], 14, 2), T(726, 358, "Hardware path:", 17, RED, 700), T(726, 386, "check USB data lines, crystal,", 16, "#263238"), T(726, 412, "CPU and storage rails, then storage.", 16, "#263238"))
d.add(note(50, 470, 1110, 56, "Flashing can erase user data. Ask the customer and back up anything you can first.", ORANGE, 16))
d.save()
render_all()

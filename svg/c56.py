from sv import *

# ---------- board sections ----------
d = Fig("s5_board_sections", "Typical sections of a phone motherboard", "Every brand places them differently, but every phone has all of them.", 1200, 720)
d.add(pcb(60, 110, 520, 580, 26))
zones = [(80, 130, 230, 165, "RF / NETWORK", "transceiver, PAs,\nantenna switch", PURPLE), (330, 130, 230, 165, "CAMERAS + SENSORS", "camera and\nsensor connectors", TEAL),
         (80, 315, 230, 165, "CPU + RAM + STORAGE", "the brain and\nits memory", NAVY), (330, 315, 230, 165, "POWER", "PMIC, coils,\ncapacitors", ORANGE),
         (80, 500, 230, 170, "CHARGING", "OVP, charging IC,\nbattery connector", RED), (330, 500, 230, 170, "AUDIO + DISPLAY", "codec, amplifier,\nscreen connector", BLUE)]
for x, y, w, h, t, s, c in zones:
    d.add(R(x, y, w, h, c, "#ffffff55", 14, 2, False, .92), T(x + w / 2, y + 60, t, 16, "#fff", 800, "middle"), T(x + w / 2, y + 92, s, 14.5, "#ffffffdd", 400, "middle"))
    # tiny parts decoration
    d.add(R(x + w - 52, y + h - 40, 34, 22, "url(#shield)", "none", 3, 0, False, .85), R(x + 16, y + h - 34, 16, 10, "#cfd8dc", "none", 1, 0, False, .9), R(x + 38, y + h - 34, 16, 10, "#cfd8dc", "none", 1, 0, False, .9))
faults = [("Network: no SIM, no service, weak signal", PURPLE), ("Cameras and sensors not working", TEAL), ("Dead, boot loop, overheating", NAVY), ("No power, shorts on power lines", ORANGE), ("Not charging, slow charging", RED), ("No sound, no display", BLUE)]
d.add(T(630, 145, "Where faults usually show up", 21, NAVY, 700))
for i, (t, c) in enumerate(faults):
    y = 180 + i * 82
    d.add(R(630, y, 530, 64, TINT[c], LINE[c], 12, 2), R(630, y, 8, 64, c, "none", 4), T(660, y + 39, t, 17, "#263238", 600))
d.save()

# ---------- designators ----------
d = Fig("s5_designators", "Reading component names on the board and schematic", "The letter tells you the type of part. The number usually tells you the area or schematic page.", 1200, 700)
rows = [("C", "Capacitor", "C1201", lambda x, y: smd(x, y, 44, 22)), ("R", "Resistor", "R2003", lambda x, y: smd(x, y, 40, 20, "#212121")), ("L", "Coil / inductor", "L1101", lambda x, y: coil(x + 4, y - 6, 34)),
        ("U", "IC / chip", "U1101", lambda x, y: chip(x - 6, y - 8, 56, 36, "", 10)), ("D", "Diode / TVS", "D1301", lambda x, y: smd(x, y, 40, 20, "#37474f") + R(x + 26, y, 5, 20, "#cfd8dc", "none", 0)),
        ("F", "Fuse", "F1201", lambda x, y: smd(x, y, 44, 20, "#6d4c41")), ("J / CN", "Connector", "J1101", lambda x, y: R(x - 8, y - 6, 62, 32, "#37474f", "none", 3) + "".join(R(x - 2 + i * 9, y, 5, 20, PAD if False else "#d4af37", "none", 1) for i in range(6))),
        ("Q", "Transistor / MOSFET", "Q1501", lambda x, y: R(x, y, 30, 22, "#212121", "none", 2) + R(x + 4, y + 22, 6, 6, "#cfd8dc", "none", 0) + R(x + 20, y + 22, 6, 6, "#cfd8dc", "none", 0) + R(x + 12, y - 6, 6, 6, "#cfd8dc", "none", 0)),
        ("Y / X", "Crystal", "X1101", lambda x, y: R(x, y - 2, 44, 26, "url(#metal)", "#78909c", 4, 1.5)), ("FL", "Filter", "FL1401", lambda x, y: R(x, y, 40, 22, "#90a4ae", "#546e7a", 3, 1.5))]
for i, (l, n, ex, draw) in enumerate(rows):
    x = 40 + (i % 2) * 570; y = 115 + (i // 2) * 106
    d.add(R(x, y, 550, 88, "#fff", "#dfe5ec", 16, 2, True), R(x, y, 96, 88, NAVY, "none", 16), R(x + 80, y, 16, 88, NAVY, "none", 0), T(x + 48, y + 54, l, 26 if len(l) < 3 else 20, "#fff", 800, "middle"))
    d.add(T(x + 120, y + 40, n, 20, NAVY, 700), T(x + 120, y + 66, "e.g. " + ex, 15.5, MUTED))
    d.add(R(x + 420, y + 14, 110, 60, "url(#pcb)", "none", 8), draw(x + 452, y + 34))
d.add(T(40, 670, "C1201 and C1202 sit close together and appear on the same schematic page.", 15, MUTED))
d.save()

# ---------- PCB layers ----------
d = Fig("s5_pcb_layers", "How a phone board is built: many thin layers", "A cross-section through a motherboard. Phone boards often have 8 to 12 copper layers.", 1200, 580, "A track can run inside the board where you cannot see it. That is why a line can be broken with no visible damage.")
lay = [("Solder mask (green)", "#2e7d32", 22), ("Top copper: pads and tracks", "url(#copper)", 22), ("Insulation (fibreglass)", "#e7dccf", 30), ("Inner copper: power plane", "#ffb74d", 22), ("", "#e7dccf", 30),
       ("Inner copper: ground plane", "#bcaaa4", 22), ("", "#e7dccf", 30), ("Inner copper: signals", "#ffcc80", 22), ("", "#e7dccf", 30), ("Bottom copper", "url(#copper)", 22), ("Solder mask", "#2e7d32", 22)]
y = 230; k = 0
for lab, c, h in lay:
    d.add(R(80, y, 700, h, c, "#5d4037", 0, .6))
    if lab:
        ly = 214 + k * 40; d.add(P(f"M780 {y+h/2} L800 {y+h/2} L830 {ly} L845 {ly}", stroke="#90a4ae", sw=1.5), T(852, ly + 5, lab, 15.5, "#263238", 600)); k += 1
    y += h
d.add(T(830, 230 + 14 + 11 + 5, "", 1))
# component on top
d.add(R(160, 190, 90, 40, "#8d6e4a", "#4e342e", 3, 2), R(160, 190, 18, 40, "#cfd8dc", "none", 2), R(232, 190, 18, 40, "#cfd8dc", "none", 2), T(205, 178, "capacitor", 14, INK, 600, "middle"))
d.add(R(420, 186, 160, 44, "#263238", "none", 4), T(500, 214, "chip", 14, "#cfd8dc", 700, "middle"))
for i in range(6): d.add(C(435 + i * 26, 232, 6, "#cfd8dc", "#78909c", 1))
# vias
d.add(R(320, 230, 16, y - 230, "url(#metal)", "#546e7a", 2, 1.5), T(328, y + 26, "through via", 14, INK, 700, "middle"))
d.add(R(640, 230, 16, 86, "url(#metal)", "#546e7a", 2, 1.5), T(648, 220 - 50, "", 1), T(690, 330, "blind via", 14, INK, 700))
d.add(note(80, 120, 700, 46, "Vias are tiny copper tubes that join one layer to another.", BLUE, 15, "i"))
d.save()

# ---------- Figure 5.1 power on ----------
d = Fig("s5_fig1", "Figure 5.1  How power flows when you press the power key", "A fault at any arrow stops the chain: dead phone, vibrates with no display, or stuck on the logo.", 1200, 640)
d.add(battery(50, 250, 170, 92, "3.7–4.2 V"), T(135, 375, "Battery", 17, NAVY, 700, "middle"))
d.add(arrow(232, 296, 312, 296, RED, 4), T(272, 284, "VBAT", 14, RED, 700, "middle"))
d.add(R(320, 230, 200, 130, "#fff3e0", ORANGE, 16, 3, True), chip(370, 262, 100, 56, "PMIC", 15), T(420, 345, "power manager", 13, ORANGE, 600, "middle"))
d.add(R(330, 470, 180, 90, "#fff", "#cfd8dc", 16, 2, True), R(380, 495, 80, 40, "url(#metal)", "#78909c", 8, 2), T(420, 590, "Power key", 16, NAVY, 700, "middle"), arrow(420, 466, 420, 366, GREEN, 3), T(430, 420, "start signal", 14, GREEN, 600))
rails = [("CPU core", "≈ 0.6 – 1.2 V", BLUE), ("Logic I/O", "1.8 V", PURPLE), ("Camera / sensors", "2.8 – 3.3 V", TEAL)]
for i, (n, v, c) in enumerate(rails):
    y = 150 + i * 120
    d.add(P(f"M524 295 C560 295 560 {y+38} 600 {y+38}", stroke=c, sw=3, arrow=True), R(606, y, 200, 76, TINT[c], LINE[c], 14, 2), T(706, y + 32, n, 16, c, 700, "middle"), T(706, y + 56, v, 15, "#37474f", 600, "middle"))
d.add(P("M806 188 C850 188 850 270 880 270", stroke=BLUE, sw=3, arrow=True), P("M806 308 C840 308 850 300 880 300", stroke=PURPLE, sw=3, arrow=True))
d.add(R(886, 230, 130, 110, "#e3f2fd", BLUE, 16, 3, True), chip(910, 255, 82, 56, "CPU", 15))
d.add(arrow(1020, 285, 1060, 285, NAVY, 3), phone(1066, 200, 90, 170, "#4fc3f7"), T(1111, 395, "display\n+ logo", 14, NAVY, 600, "middle"))
d.add(arrow(951, 344, 951, 440, NAVY, 3), R(880, 446, 142, 80, "#fff", "#cfd8dc", 14, 2, True), chip(905, 466, 92, 40, "eMMC/UFS", 11), T(951, 548, "loads the system", 13, MUTED, 400, "middle"))
d.save()

# ---------- Figure 5.2 charging path ----------
d = Fig("s5_fig2", "Figure 5.2  The charging path", "Power from the charger passes through each part in turn. A fault anywhere stops charging.", 1200, 520)
items = [("Charger", "5 V (9–12 V fast)"), ("USB port", "VBUS pin"), ("Fuse", "F1"), ("OVP IC", "blocks surges"), ("Charging IC", "controls charging")]
for i, (t, s) in enumerate(items):
    x = 40 + i * 190
    d.add(R(x, 190, 160, 130, "#fff" if i < 4 else TINT[BLUE], LINE[BLUE] if i == 4 else "#cfd8dc", 16, 2.5, True))
    if i == 0: d.add(R(x + 50, 210, 60, 50, "url(#dev)", "#90a4ae", 8, 2), R(x + 62, 200, 6, 12, "#90a4ae", "none", 1), R(x + 92, 200, 6, 12, "#90a4ae", "none", 1))
    if i == 1: d.add(usb_c(x + 35, 220, 90, 32))
    if i == 2: d.add(R(x + 45, 222, 70, 26, "#6d4c41", "#3e2723", 3, 2), R(x + 45, 222, 14, 26, "#cfd8dc", "none", 2), R(x + 101, 222, 14, 26, "#cfd8dc", "none", 2))
    if i == 3: d.add(chip(x + 52, 216, 56, 34, "OVP", 11))
    if i == 4: d.add(chip(x + 40, 212, 80, 42, "CHG", 13))
    d.add(T(x + 80, 288, t, 17, NAVY, 700, "middle"), T(x + 80, 308, s, 13.5, MUTED, 400, "middle"))
    if i < 4: d.add(arrow(x + 163, 255, x + 187, 255, RED, 3.5))
d.add(P("M1000 230 C1030 230 1030 160 1060 160", stroke=RED, sw=3.5, arrow=True), P("M1000 280 C1030 280 1030 350 1060 350", stroke=RED, sw=3.5, arrow=True))
d.add(battery(1062, 125, 110, 70, "VBAT"), R(1062, 315, 110, 70, TINT[GREEN], LINE[GREEN], 12, 2), T(1117, 348, "System", 15, GREEN, 700, "middle"), T(1117, 368, "power", 14, GREEN, 600, "middle"))
d.add(note(40, 410, 1120, 64, "Good port and battery but still not charging? Check the fuse, the OVP IC, the charging IC and VBUS for a short.", RED, 16))
d.save()

# ---------- rail voltages ----------
d = Fig("s5_rail_voltages", "Typical voltage levels on a phone board", "A general guide. Always confirm with the schematic for the model you are repairing.", 1200, 640, "LCD bias (±5.5 V) and backlight (15–25 V) are higher, and only appear when the screen is on.")
rails = [("VBUS (charger)", 5.0, RED), ("VBAT / VPH_PWR", 4.0, ORANGE), ("Camera / sensor LDO", 2.8, TEAL), ("Logic I/O (1.8 V)", 1.8, BLUE), ("Memory rail", 1.1, PURPLE), ("CPU core (buck)", 0.8, GRAY)]
for v in range(6): d.add(L(340 + v * 150, 120, 340 + v * 150, 552, "#e3e8ef", 1, dash="4 6"), T(340 + v * 150, 568, f"{v} V", 13, MUTED, 400, "middle"))
for i, (n, v, c) in enumerate(rails):
    y = 130 + i * 70
    d.add(T(320, y + 32, n, 17, "#263238", 700, "end"), R(340, y + 6, v * 150, 40, c, "none", 20), T(340 + v * 150 + 14, y + 34, f"{v:g} V", 18, c, 800))
d.save()

# ---------- Ch6 short concept ----------
d = Fig("s6_short_concept", "What a short circuit does", "A shorted capacitor gives the current a shortcut straight to ground.", 1200, 600)
for i, (t, c) in enumerate([("NORMAL", GREEN), ("SHORTED CAPACITOR", RED)]):
    x = 40 + i * 570
    d.add(R(x, 110, 550, 450, "#fff", LINE[c], 20, 2, True), T(x + 275, 152, t, 22, c, 800, "middle"))
    d.add(L(x + 50, 240, x + 440, 240, RED, 4), T(x + 50, 228, "VBAT", 15, RED, 700), PL([(x + 440, 240), (x + 440, 300)], RED, 4), R(x + 380, 300, 120, 90, "#fff3e0", ORANGE, 12, 2.5), chip(x + 405, 325, 70, 40, "PMIC", 12))
    cx = x + 220
    d.add(L(cx, 240, cx, 300, INK, 3), R(cx - 24, 300, 48, 70, "#8d6e4a", "#4e342e", 4, 2), R(cx - 24, 300, 48, 14, "#cfd8dc", "none", 2), R(cx - 24, 356, 48, 14, "#cfd8dc", "none", 2), L(cx, 370, cx, 410, INK, 3), gnd(cx, 410))
    if i == 0:
        d.add(arrow(x + 270, 224, x + 400, 224, GREEN, 3.5), T(x + 335, 212, "current", 14, GREEN, 700, "middle"), T(x + 275, 500, "Current goes to the PMIC.\nA capacitor blocks DC, so none flows to ground.", 16, "#263238", 400, "middle"))
    else:
        d.add(P(f"M{cx-60} 228 C{cx-30} 228 {cx-34} 300 {cx-34} 400", stroke=RED, sw=4, arrow=True), f'<circle cx="{cx}" cy="335" r="52" fill="#ff7043" opacity=".22"/>', flame(cx + 46, 320, .9), T(cx + 70, 300, "HOT", 18, RED, 800))
        d.add(L(cx - 16, 318, cx + 16, 352, "#ffca28", 4), T(x + 275, 500, "Current takes the shortcut to ground.\nThe supply hits its limit and the part heats up.", 16, "#263238", 400, "middle"))
d.save()

# ---------- Ch6 diode compare ----------
d = Fig("s6_diode_compare", "Confirming a short: compare with a good board", "Battery disconnected. Red probe on ground, black probe on the line.", 1200, 560)
for i, (val, t, c) in enumerate([("0.412", "Good board: VBAT reads about 0.4", GREEN), ("0.002", "Faulty board: near 0 = SHORT", RED)]):
    x = 40 + i * 570
    d.add(R(x, 110, 550, 400, "#fff", LINE[c], 20, 2, True))
    d.add(multimeter(x + 30, 140, val, "DIODE", 1.0), pcb(x + 230, 170, 290, 180), R(x + 250, 200, 250, 18, "url(#copper)", "none", 3), T(x + 260, 194, "VBAT", 13, "#fff", 700))
    d.add(R(x + 360, 230, 22, 50, "#8d6e4a", "#4e342e", 2, 1.5), R(x + 360, 230, 22, 10, "#cfd8dc", "none", 1), R(x + 360, 270, 22, 10, "#cfd8dc", "none", 1), L(x + 371, 218, x + 371, 230, "#d4af37", 4), L(x + 371, 280, x + 371, 310, "#bdbdbd", 4), R(x + 250, 310, 250, 14, "#9e9e9e", "none", 3), T(x + 260, 340, "GND", 12, "#fff", 700))
    d.add(meter_lead(x + 68, 345, x + 371, 230, INK, 40), meter_lead(x + 105, 345, x + 470, 310, RED, 30))
    d.add((check if c == GREEN else cross)(x + 50, 466, 18), T(x + 80, 473, t, 19, c, 700))
d.save()

# ---------- Figure 6.1 voltage injection ----------
d = Fig("s6_fig1", "Figure 6.1  Finding a short with voltage injection", "Start low (about 1 V) and never go above the line's normal voltage. The shorted part heats first.", 1200, 640, "Find the hot part with rosin, a thermal camera, alcohol or your fingertip.")
d.add(psu(60, 160, "1.00", "1.000", 1.25), T(185, 148, "Current limit about 1 A", 15, MUTED, 400, "middle"))
d.add(pcb(400, 130, 760, 420), R(430, 200, 700, 22, "url(#copper)", "none", 3), T(440, 190, "shorted line (e.g. VBAT)", 16, "#fff", 700), R(430, 460, 700, 18, "#9e9e9e", "none", 3), T(440, 500, "GROUND", 15, "#fff", 700))
for i, x in enumerate([560, 700, 840, 980]):
    hot = i == 2
    d.add(L(x, 222, x, 290, "#d4af37", 4), R(x - 18, 290, 36, 100, "#e65100" if hot else "#8d6e4a", "#4e342e", 3, 2), R(x - 18, 290, 36, 16, "#cfd8dc", "none", 2), R(x - 18, 374, 36, 16, "#cfd8dc", "none", 2), L(x, 390, x, 460, "#bdbdbd", 4))
d.add(f'<circle cx="840" cy="340" r="70" fill="#ff7043" opacity=".25"/>', flame(890, 300, 1), T(900, 270, "HOT!", 20, "#ffca28", 800))
d.add(P("M117 303 C117 400 330 330 520 211", stroke=RED, sw=4), C(520, 211, 6, RED), T(300, 395, "red → line", 16, RED, 700, "middle"))
d.add(P("M180 303 C180 560 420 560 560 470", stroke=INK, sw=4), C(560, 470, 6, INK), T(160, 470, "black → ground", 16, INK, 700, "middle"))
d.save()

# ---------- Ch6 isolation ----------
d = Fig("s6_isolation", "Isolation method: split the line to find which side is shorted", "Lift a coil or 0 Ω link in the middle, then measure both sides in diode mode.", 1200, 560, "Keep splitting the bad side until only one part is left.")
d.add(pcb(40, 110, 1120, 290))
d.add(R(70, 170, 1060, 18, "url(#copper)", "none", 3), T(80, 162, "shorted line (e.g. VDD_1V8)", 16, "#fff", 700))
for x in [150, 270, 390, 770, 890, 1010]:
    d.add(L(x, 188, x, 240, "#d4af37", 4), R(x - 14, 240, 28, 70, "#8d6e4a", "#4e342e", 3, 2), R(x - 14, 240, 28, 12, "#cfd8dc", "none", 2), R(x - 14, 298, 28, 12, "#cfd8dc", "none", 2), L(x, 310, x, 350, "#bdbdbd", 4))
d.add(R(70, 350, 1060, 14, "#9e9e9e", "none", 3))
d.add(R(520, 158, 160, 64, "#fff", "none", 0, 0, False, 0), R(540, 150, 120, 50, "#455a64", "#263238", 6, 2), C(600, 175, 14, "#607d8b"), P("M560 130 L650 222", stroke=ORANGE, sw=6), T(600, 250, "lift the coil", 17, "#ffcc80", 800, "middle"))
d.add(R(70, 420, 520, 80, TINT[RED], LINE[RED], 14, 2), T(330, 468, "Left side still shorted? The fault is on the left.", 17, RED, 700, "middle"))
d.add(R(610, 420, 520, 80, TINT[RED], LINE[RED], 14, 2), T(870, 468, "Right side shorted? The fault is on the right.", 17, RED, 700, "middle"))
d.save()
render_all()

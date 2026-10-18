from sv import *
def ant(x, y, c=INK): return L(x, y, x, y + 50, c, 3) + P(f"M{x-20} {y} L{x+20} {y} L{x} {y+26} Z", stroke=c, sw=3, fill="#fff")

# ---------- Figure 12.1 RF section ----------
d = Fig("s12_fig1", "Figure 12.1  The network (RF) section of a phone", "Real phones have several power amplifiers and filters for different bands, but the idea is the same.", 1200, 720)
d.add(box(40, 220, 180, 150, "CPU with\nbuilt-in modem\n(baseband)", NAVY, 15), box(290, 220, 180, 150, "RF\ntransceiver", "#37474f", 17))
d.add(L(222, 295, 288, 295, INK, 3), box(560, 150, 190, 90, "Power amplifier\n(transmit)", "#5d4037", 15), box(560, 300, 190, 90, "Filters + LNA\n(receive)", TEAL, 15))
d.add(arrow(472, 270, 556, 205, INK, 3), arrow(556, 345, 472, 320, INK, 3), box(820, 220, 160, 120, "Antenna\nswitch", "#455a64", 16), arrow(752, 195, 816, 250, INK, 3), arrow(816, 300, 752, 340, INK, 3))
d.add(PL([(655, 150), (655, 100)], RED, 3.5), T(645, 116, "VBAT (high current)", 13, RED, 800, "end"))
d.add(PL([(900, 220), (900, 170)], INK, 3), ant(900, 120), T(900, 106, "Main antenna", 14, NAVY, 800, "middle"))
d.add(PL([(980, 300), (1080, 300), (1080, 170)], INK, 3, dash="8 6"), ant(1080, 120), T(1080, 106, "Diversity antenna", 14, NAVY, 800, "middle"), T(1030, 290, "coax", 13, MUTED, 600, "middle"))
d.add(box(40, 470, 180, 100, "SIM card\nreader", PURPLE, 16), PL([(130, 370), (130, 470)], PURPLE, 3), T(152, 430, "VCC, RST,\nCLK, I/O", 13, PURPLE, 700))
d.add(box(560, 480, 230, 100, "Wi-Fi / Bluetooth /\nGPS chip", BLUE, 15), PL([(380, 370), (380, 530), (560, 530)], BLUE, 3, dash="6 6"), PL([(790, 530), (950, 530), (950, 460)], INK, 3), ant(950, 410), T(950, 396, "Wi-Fi / BT / GPS antennas", 14, NAVY, 800, "middle"))
for n, (x, y) in enumerate([(130, 420), (500, 300), (760, 150), (990, 220), (800, 470)], 1): d.add(badge(x, y, n))
d.add(T(40, 640, "1 SIM reader and its lines   2 Transceiver   3 Power amplifier (a common short after liquid)   4 Antenna switch, coax and antenna contacts   5 Wi-Fi / BT / GPS", 14.5, "#37474f", 600))
d.save()

# ---------- Figure 12.2 SIM pins ----------
d = Fig("s12_fig2", "Figure 12.2  SIM card contacts and what to measure", "Contact side of the SIM (cut corner at top left).", 1200, 640)
d.add(P("M90 160 L150 110 H400 Q414 110 414 124 V520 Q414 534 400 534 H104 Q90 534 90 520 Z", fill="#ffe082", stroke="#c49000", sw=3))
pads = [("C1", "VCC", 120, 160), ("C2", "RST", 120, 270), ("C3", "CLK", 120, 380), ("C5", "GND", 270, 160), ("C6", "VPP", 270, 270), ("C7", "I/O", 270, 380)]
for n, s, x, y in pads: d.add(R(x, y, 110, 90, "url(#copper)", "#8d6e1a", 14, 2), T(x + 55, y + 40, n, 16, "#3e2723", 800, "middle"), T(x + 55, y + 64, s, 15, "#3e2723", 700, "middle"))
rows = [("C1  VCC", "SIM power: 1.8 V or 3 V, briefly at start-up or SIM read", RED), ("C2  RST", "Reset signal from the modem", BLUE), ("C3  CLK", "Clock signal from the modem", BLUE),
        ("C5  GND", "Ground", INK), ("C6  VPP", "Not used on most phones (some NFC SIMs use it)", GRAY), ("C7  I/O", "Data line between the SIM and the phone", BLUE)]
for i, (a, b, c) in enumerate(rows):
    y = 130 + i * 56
    d.add(R(470, y, 690, 46, TINT[c] if c != INK else TINT[GRAY], "none", 10), T(490, y + 29, a, 16, c, 800), T(600, y + 29, b, 14.5, "#263238"))
d.add(note(470, 480, 690, 120, "On the board: check each reader pin in diode mode against a good board.\nA short on VCC, CLK, RST or I/O, or a corroded pin, gives 'No SIM'.\nMany readers also have a SIM-detect switch: if it is bent, the phone\nnever looks for the SIM.", ORANGE, 15))
d.save()

# ---------- symptoms ----------
d = Fig("s12_symptoms", "Network symptoms and where to look", "Network faults are easy to confuse with carrier or account problems: always test with a known-good SIM first.", 1200, 560)
rows = [("No SIM / SIM not detected", "SIM tray, reader pins, the SIM card, SIM lines", RED), ("No service, SIM detected", "Antenna, coax, RF section, baseband, IMEI", ORANGE), ("Weak or dropping signal", "Antenna contacts, coax, PA, metal case or cover", BLUE),
        ("Wi-Fi or Bluetooth won't turn on", "Wi-Fi/BT chip, its power line, software", PURPLE), ("Calls fail, data works (or the reverse)", "Network settings, carrier, software", TEAL)]
for i, (s, c_, col) in enumerate(rows):
    y = 120 + i * 82
    d.add(R(40, y, 1120, 68, "#fff", LINE[col], 14, 2, True), R(40, y, 430, 68, col, "none", 14), R(450, y, 20, 68, col, "none", 0), T(64, y + 42, s, 17.5, "#fff", 800), arrow(480, y + 34, 520, y + 34, col, 3), T(536, y + 41, c_, 17, "#263238", 600))
d.save()

# ---------- simple checks ----------
d = Fig("s12_simple_checks", "Simple checks before opening the phone", "Most 'no service' complaints are solved here, without opening the phone.", 1200, 460)
checks = [("Known-good SIM", "rules out the card\nand the carrier", "SIM"), ("Airplane mode\noff / on", "forces a fresh\nnetwork search", "✈"), ("Check IMEI\n*#06#", "blank or 0000 =\nbaseband problem", "#"), ("Network mode\n2G / 4G / 5G", "wrong mode = no\nservice in some areas", "4G"), ("Reset network\nsettings", "clears bad APN\nand settings", "↺")]
for i, (t, s, ic) in enumerate(checks):
    x = 40 + i * 228; c = ORANGE if i == 2 else BLUE
    d.add(R(x, 120, 208, 280, "#fff", LINE[c], 18, 2, True), C(x + 104, 186, 42, TINT[c]), T(x + 104, 198, ic, 26 if len(ic) < 3 else 20, c, 800, "middle"))
    d.add(T(x + 104, 264, t, 17, NAVY, 800, "middle", 1.25), T(x + 104, 336, s, 14.5, "#37474f", 400, "middle"))
d.save()

# ---------- dBm ----------
d = Fig("s12_dbm_scale", "Reading signal strength in dBm", "Settings → About phone → Status → SIM status. The number is negative: closer to 0 is stronger.", 1200, 500, "Values are a general guide for 4G. 2G and 5G use slightly different ranges.")
segs = [(.4, "#2e7d32", "Excellent"), (.13, "#7cb342", "Good"), (.13, "#f9a825", "Fair"), (.13, "#ef6c00", "Poor"), (.21, "#c62828", "No usable signal")]
x = 60
for f, c, t in segs: w = 1080 * f; d.add(R(x, 190, w, 60, c, "#fff", 0, 3), T(x + w / 2, 227, t, 16, "#fff", 800, "middle")); x += w
for v, xx in [(-50, 60), (-80, 492), (-90, 632), (-100, 773), (-110, 913), (-125, 1140)]: d.add(L(xx, 180, xx, 260, INK, 2), T(xx, 172, str(v), 16, INK, 800, "middle"))
for i in range(5): d.add(R(80 + i * 26, 160 - i * 0 - (i + 1) * 0, 1, 1, "none"))
d.add(G([R(i * 18, 40 - i * 10, 12, 10 + i * 10, "#2e7d32" if i < 4 else "#cfd8dc", "none", 2) for i in range(5)], 1070, 18))
d.add(note(60, 300, 1080, 90, "Compare with a good phone on the same network in the same place. If the good phone reads –85\nand yours reads –115, the problem is your phone's antenna or RF path, not the area.", BLUE, 16, "i"))
d.save()

# ---------- antenna path ----------
d = Fig("s12_antenna_path", "Antenna path: from the RF chip to the antenna", "Most weak-signal repairs are mechanical: a coax that came off after a screen job (1), or a dirty or bent contact (2).", 1200, 440)
d.add(pcb(40, 140, 760, 220))
d.add(chip(80, 200, 130, 80, "RF", 16), chip(270, 200, 120, 80, "PA", 16), chip(450, 200, 120, 80, "SWITCH", 13))
d.add(trace([(210, 240), (270, 240)]), trace([(390, 240), (450, 240)]), trace([(570, 240), (620, 240)]))
d.add(C(632, 240, 14, "url(#copper)", "#8d6e1a", 2), T(632, 290, "coax socket", 13, "#e8f5e9", 700, "middle"))
d.add(P("M646 240 C720 240 760 200 860 200", stroke="#795548", sw=7), T(812, 248, "coax cable", 14, "#5d4037", 800))
d.add(R(860, 186, 30, 28, "url(#copper)", "#8d6e1a", 4, 2), P("M875 186 v-14 q0 -10 10 -10 h20", stroke="#8d6e1a", sw=4), T(880, 240, "spring contact", 13, INK, 700, "middle"))
d.add(PL([(905, 162), (1120, 162), (1120, 330)], RED, 6), T(1010, 150, "antenna (frame or flex)", 15, RED, 800, "middle"))
d.add(badge(720, 260, 1), badge(875, 280, 2))
d.save()

# ---------- Figure 13.1 corrosion ----------
d = Fig("s13_fig1", "Figure 13.1  Why liquid destroys a powered board (corrosion)", "", 1200, 640)
stages = [("1. Dry", "Dry board: no path\nbetween the pads", "Normal", GREEN), ("2. Wet and powered", "Current flows through\nthe liquid (leakage)", "Minutes to hours", ORANGE), ("3. Corrosion", "Metal dissolves: green and\nwhite crust grows between pads", "Days to weeks", RED)]
for i, (t, s, tm, c) in enumerate(stages):
    x = 40 + i * 390
    d.add(R(x, 100, 360, 360, "#fff", LINE[c], 18, 2, True), T(x + 180, 140, t, 20, c, 800, "middle"), T(x + 180, 176, s, 14.5, "#37474f", 400, "middle"))
    d.add(R(x + 30, 300, 300, 70, "url(#pcb)", "#123d22", 8, 2), R(x + 70, 280, 80, 22, "url(#copper)", "none", 3), R(x + 210, 280, 80, 22, "url(#copper)", "none", 3), T(x + 110, 344, "VBAT +", 14, "#fff", 800, "middle"), T(x + 250, 344, "GND –", 14, "#fff", 800, "middle"))
    if i >= 1: d.add(f'<ellipse cx="{x+180}" cy="282" rx="140" ry="34" fill="#81d4fa" opacity=".55" stroke="#29b6f6" stroke-width="2"/>')
    if i == 1:
        for k in range(4): d.add(L(x + 152, 270 + k * 6, x + 208, 270 + k * 6, "#ff7043", 2.5))
        d.add(arrow(x + 150, 250, x + 210, 250, "#ff5722", 2.5))
    if i == 2:
        import random; random.seed(5)
        for k in range(30): d.add(C(x + 120 + random.random() * 120, 262 + random.random() * 30, 4 + random.random() * 4, random.choice(["#66bb6a", "#a5d6a7", "#fff", "#4caf50"]), "#2e7d32", 1))
    d.add(T(x + 180, 420, tm, 16, MUTED, 700, "middle"))
    if i < 2: d.add(arrow(x + 362, 335, x + 388, 335, NAVY, 3))
d.add(note(40, 490, 1120, 110, "The battery keeps powering the board even when the phone looks off. Every minute it stays\nconnected, corrosion gets worse. That is why the first rule of liquid damage is:\ndisconnect the battery as soon as possible.", RED, 16))
d.save()

# ---------- Figure 13.2 water workflow ----------
d = Fig("s13_fig2", "Figure 13.2  Water damage repair workflow", "Tell the customer liquid damage can return later, and give a shorter warranty or none on liquid-damaged phones.", 1200, 480)
items = ["Disconnect\nbattery", "Open fully,\nremove\nshields", "Inspect\nunder the\nmicroscope", "Clean:\nIPA + brush,\nultrasonic", "Dry fully\n(warm air,\nnever rice)", "Check shorts\n(diode mode),\nthen PSU", "Replace\nfailed parts,\ntest all"]
d.add(flow(40, 140, items, 138, 150, 26, [RED, "#5d4037", "#455a64", BLUE, TEAL, NAVY, GREEN], 14))
d.add(note(40, 340, 1120, 110, "Never: charge or power on a wet phone · put it in rice and wait · use a hair dryer on high heat\n· skip cleaning under shields and connectors.", RED, 16))
d.save()

# ---------- timeline ----------
d = Fig("s13_timeline", "Liquid damage gets worse with time: act fast", "Tell the customer: switch off, do not charge, do not use rice or a hair dryer, bring it in quickly.", 1200, 380)
d.add(R(60, 236, 1080, 10, "#e3e8ef", "none", 5))
pts = [(100, "0 min", "liquid enters,\nshorts while ON", BLUE), (340, "minutes", "current flows,\nparts burn", ORANGE), (600, "hours", "corrosion starts\nunder chips", "#8d6e4a"), (860, "days", "green and white crust,\ntracks eaten away", RED), (1100, "weeks", "pads and lines\ndestroyed", "#4e342e")]
for i in range(4): d.add(R(pts[i][0], 236, pts[i + 1][0] - pts[i][0], 10, pts[i + 1][3], "none", 0, 0, False, .7))
for x, t, s, c in pts: d.add(C(x, 241, 24, c, "#fff", 4), T(x, 196, t, 18, c, 800, "middle"), T(x, 300, s, 15, "#263238", 400, "middle"))
d.save()

# ---------- cleaning ----------
d = Fig("s13_cleaning", "Cleaning a liquid-damaged board", "", 1200, 460)
d.add(flow(40, 120, ["Remove\nshields", "IPA 99 %", "Soft brush", "Ultrasonic\nbath", "Rinse +\ninspect"], 192, 100, 30, [TEAL] * 5, 17,
           ["corrosion hides\nunder them", "never tap water or\nlow-grade alcohol", "work gently under\nchips and connectors", "3–5 min in IPA or\nboard cleaner", "fresh IPA, then a\nmicroscope check"], 14.5))
d.add(note(40, 340, 1120, 90, "Never put the battery, screen, speaker, mic or cameras in the ultrasonic bath.\nThey can be damaged, or their membranes torn.", RED, 16))
d.save()

# ---------- drying ----------
d = Fig("s13_drying", "Drying properly before power", "Powering a board that is still wet can burn the parts you just cleaned.", 1200, 420)
for i, (t, s, c, ic) in enumerate([("Air or fan", "1–2 hours at room temperature,\nafter IPA (it dries fast)", GREEN, "≋"), ("Warm plate or oven", "40–60 °C for 30–60 min.\nNever above 70 °C.", ORANGE, "♨"), ("Check under chips", "No liquid left under BGA\nchips or connectors", BLUE, "⌕")]):
    x = 40 + i * 380
    d.add(R(x, 120, 360, 240, "#fff", LINE[c], 18, 2, True), C(x + 180, 186, 40, TINT[c]), T(x + 180, 200, ic, 34, c, 700, "middle"), T(x + 180, 262, t, 19, c, 800, "middle"), T(x + 180, 296, s, 15, "#263238", 400, "middle"))
d.save()

# ---------- hotspots ----------
d = Fig("s13_hotspots", "Where liquid damage usually shows up", "Connectors and ports corrode first because they carry voltage and trap liquid. Look there before anywhere else.", 1200, 700)
d.add(pcb(60, 110, 480, 560, 26))
for (x, y, w, h) in [(90, 140, 120, 80), (380, 150, 120, 70), (240, 270, 140, 110), (90, 430, 130, 60), (380, 430, 120, 90), (230, 580, 140, 60)]: d.add(R(x, y, w, h, "url(#shield)", "#90a4ae", 6, 1.5, False, .9))
spots = [(150, 180, "Charging port and sub-board flex"), (440, 185, "SIM reader"), (310, 325, "Backlight and display circuit"), (155, 460, "Battery connector"), (440, 475, "Power key and flex connectors"), (300, 610, "Speaker and mic mesh")]
for i, (x, y, t) in enumerate(spots):
    d.add(f'<circle cx="{x}" cy="{y}" r="48" fill="#4fc3f7" opacity=".28"/>', badge(x, y, i + 1, ORANGE, 18, 16))
    d.add(R(600, 120 + i * 88, 560, 70, "#fff", "#dfe5ec", 14, 2, True), badge(636, 155 + i * 88, i + 1, ORANGE, 18, 16), T(670, 162 + i * 88, t, 18, "#263238", 600))
d.save()
render_all()

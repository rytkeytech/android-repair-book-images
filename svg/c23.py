from sv import *

# ---------- Ch2: water analogy ----------
d = Fig("s2_water", "Voltage, current and resistance: the water pipe idea", "Electricity behaves like water in pipes. Learn this picture and Ohm's law makes sense.", 1200, 720)
# tank
d.add(R(60, 130, 150, 260, "#eceff1", "#90a4ae", 14, 3), R(66, 190, 138, 194, "url(#water)", "none", 8), P("M66 190 q35 -10 69 0 t69 0", stroke="#bbdefb", sw=3))
d.add(T(135, 125, "", 1), softbox(55, 400, 160, 66, "Tank height", BLUE, 16, "= VOLTAGE (V)"))
# pipe wide - narrow - wide
d.add(R(204, 300, 240, 56, "url(#water)", "#1565c0", 6, 2), R(444, 316, 180, 24, "url(#water)", "#1565c0", 4, 2), R(624, 300, 240, 56, "url(#water)", "#1565c0", 6, 2))
for x in (230, 300, 370, 650, 720, 790): d.add(arrow(x, 328, x + 46, 328, "#ffffff", 3))
d.add(arrow(460, 328, 600, 328, "#ffffff", 2))
d.add(softbox(234, 196, 180, 66, "Flow of water", BLUE, 16, "= CURRENT (A)"), softbox(444, 196, 180, 66, "Narrow pipe", ORANGE, 16, "= RESISTANCE (Ω)"))
d.add(L(534, 262, 534, 312, ORANGE, 2, dash="5 5"))
# wheel at end
d.add(C(905, 328, 42, "#fff", "#1565c0", 4), P("M905 286 V370 M863 328 H947 M875 298 L935 358 M935 298 L875 358", stroke="#1565c0", sw=3), T(905, 400, "does work", 14, MUTED, 400, "middle"))
# circuit below
d.add(T(60, 520, "The same idea as a circuit:", 17, NAVY, 700))
d.add(PL([(110, 598), (110, 560), (440, 560)], INK, 3), res_sym(440, 560, 80, ORANGE), PL([(520, 560), (840, 560), (840, 650), (110, 650), (110, 612)], INK, 3))
d.add(L(86, 598, 134, 598, INK, 4), L(98, 612, 122, 612, INK, 4), T(146, 610, "battery = voltage", 15, BLUE, 600))
d.add(T(480, 542, "resistor = resistance", 15, ORANGE, 600, "middle"), arrow(640, 548, 760, 548, BLUE, 2.5), T(700, 538, "current", 14, BLUE, 600, "middle"))
d.add(note(870, 108, 300, 120, "More voltage pushes more\ncurrent. More resistance\nallows less current.", BLUE, 15.5, "i"))
d.add(R(880, 470, 280, 120, NAVY, "none", 16, 0, True), T(1020, 520, "V = I × R", 34, "#fff", 800, "middle"), T(1020, 560, "Ohm's law", 16, "#c5cfe0", 400, "middle"))
d.save()

# ---------- Ch2: Ohm triangle ----------
d = Fig("s2_ohm", "Ohm's law triangle and a worked example", "Cover the value you want to find. What is left shows the formula.", 1200, 660)
d.add(f'<g filter="url(#sh)"><path d="M300 120 L520 500 L80 500 Z" fill="#fff" stroke="{NAVY}" stroke-width="4"/></g>')
d.add(f'<path d="M300 120 L410 310 L190 310 Z" fill="{TINT[BLUE]}"/>', f'<path d="M190 310 L300 310 L300 500 L80 500 Z" fill="{TINT[ORANGE]}"/>', f'<path d="M300 310 L410 310 L520 500 L300 500 Z" fill="{TINT[GREEN]}"/>')
d.add(P("M300 120 L520 500 L80 500 Z", stroke=NAVY, sw=4), L(190, 310, 410, 310, NAVY, 4), L(300, 310, 300, 500, NAVY, 4))
d.add(T(300, 270, "V", 64, BLUE, 800, "middle"), T(225, 445, "I", 60, ORANGE, 800, "middle"), T(375, 445, "R", 60, GREEN, 800, "middle"))
d.add(T(300, 290, "volts", 14, BLUE, 600, "middle"), T(225, 470, "amps", 14, ORANGE, 600, "middle"), T(375, 470, "ohms", 14, GREEN, 600, "middle"))
for i, (f, s, c) in enumerate([("V = I × R", "voltage = current × resistance", BLUE), ("I = V ÷ R", "current = voltage ÷ resistance", ORANGE), ("R = V ÷ I", "resistance = voltage ÷ current", GREEN)]):
    y = 140 + i * 78
    d.add(R(600, y, 560, 62, TINT[c], LINE[c], 12, 2), T(624, y + 40, f, 26, c, 800), T(800, y + 38, s, 16, "#37474f"))
d.add(R(600, 390, 560, 200, "#fff", LINE[ORANGE], 16, 2, True), R(600, 390, 8, 200, ORANGE, "none", 4))
d.add(T(630, 428, "Worked example", 18, ORANGE, 700), T(630, 462, "A 3.8 V supply is connected across a 10 Ω resistor.", 16), T(630, 500, "I = V ÷ R = 3.8 ÷ 10 = 0.38 A (380 mA)", 19, NAVY, 700, mono=True),
      T(630, 540, "A short circuit has almost no resistance,", 16, RED, 600), T(630, 563, "so the current becomes very large.", 16, RED, 600))
d.save()

# ---------- Ch3: meter modes ----------
d = Fig("s3_meter_modes", "Multimeter modes used in phone repair", "Five settings do almost all the work. Set the dial before the probes touch the board.", 1200, 720)
d.add(multimeter(80, 120, "0.512", "DIODE", 1.9))
modes = [("V", "DC voltage", "Is power present? Board ON.", BLUE), ("Ω", "Resistance", "Resistors, speakers, NTC. Board OFF.", GREEN), ("▶|", "Diode mode", "Find shorts, compare lines. Board OFF.", ORANGE),
         ("•))", "Continuity", "Fuses, coils, tracks, flex. Board OFF.", PURPLE), ("A", "Current", "Rarely used. Read the PSU display instead.", RED)]
for i, (sym, n, s, c) in enumerate(modes):
    y = 130 + i * 108
    d.add(R(470, y, 690, 88, "#fff", LINE[c], 16, 2, True), R(470, y, 88, 88, TINT[c], "none", 16), R(540, y, 18, 88, TINT[c], "none", 0))
    d.add(T(514, y + 56, sym, 28 if len(sym) < 3 else 22, c, 800, "middle"), T(584, y + 38, n, 21, c, 700), T(584, y + 66, s, 16, "#37474f"))
d.save()

# ---------- Ch3: cold & hot test ----------
d = Fig("s3_cold_hot", "Cold test and hot test", "Two ways to measure a board. Always do the cold test first.", 1200, 560, "Measuring resistance or diode mode with power ON gives false readings and can damage the meter.")
for i, (t, s, c, modes, finds) in enumerate([("COLD TEST", "Battery and power OFF", BLUE, "Diode mode, continuity,\nresistance", "Shorts, open fuses and coils,\nbroken tracks, wrong resistors"),
                                               ("HOT TEST", "Board powered ON", RED, "DC voltage,\nPSU current", "Missing power lines,\nwrong voltages, lines\nthat never switch on")]):
    x = 40 + i * 570
    d.add(R(x, 110, 550, 380, "#fff", LINE[c], 20, 2, True), f'<path d="M{x} {128} Q{x} 110 {x+18} 110 H{x+532} Q{x+550} 110 {x+550} 128 V190 H{x} Z" fill="{TINT[c]}"/>')
    d.add(T(x + 30, 152, t, 26, c, 800), T(x + 30, 178, s, 16, "#37474f"))
    d.add(pcb(x + 40, 230, 220, 140), chip(x + 110, 275, 70, 50, "PMIC"), smd(x + 70, 250), smd(x + 200, 330))
    if i == 0:
        d.add(R(x + 290, 250, 110, 56, "url(#batt)", "none", 8), L(x + 285, 245, x + 405, 311, RED, 5), L(x + 405, 245, x + 285, 311, RED, 5), T(x + 345, 330, "no battery", 14, RED, 600, "middle"))
        d.add(T(x + 420, 260, "❄", 44, BLUE, 400, "middle"))
    else:
        d.add(psu(x + 290, 240, "4.00", "0.180", .62), P(f"M{x+320} {x*0+330} C{x+320} 380 {x+250} 380 {x+250} 340", stroke=RED, sw=3), flame(x + 470, 300, 1))
    d.add(T(x + 40, 420, "Modes:", 16, NAVY, 700), T(x + 40, 446, modes, 16, "#263238", 400), T(x + 300, 420, "Finds:", 16, NAVY, 700), T(x + 300, 446, finds, 16, "#263238", 400))
d.save()

# ---------- Ch3: continuity ----------
d = Fig("s3_continuity", "Continuity mode: testing a fuse or coil", "Battery disconnected. A beep means the part conducts; silence means it is open.", 1200, 560, "Continuity also checks coils, tracks, flex cables and coax cables.")
for i, (val, c, txt, broken) in enumerate([("0.4 Ω", GREEN, "BEEP: good fuse (connected)", False), ("OL", RED, "No beep: fuse is open (blown)", True)]):
    x = 60 + i * 570
    d.add(multimeter(x, 130, val, "•)) CONT", 1.05))
    d.add(pcb(x + 210, 210, 300, 150), trace([(x + 230, 285), (x + 300, 285)]), trace([(x + 420, 285), (x + 490, 285)]))
    d.add(R(x + 300, 268, 120, 34, "#6d4c41", "#3e2723", 4, 2), R(x + 300, 268, 22, 34, "#cfd8dc", "none", 2), R(x + 398, 268, 22, 34, "#cfd8dc", "none", 2), T(x + 360, 291, "FUSE", 13, "#fff", 700, "middle"))
    if broken: d.add(P(f"M{x+345} 262 L{x+362} 285 L{x+352} 290 L{x+372} 310", stroke="#ffca28", sw=4))
    d.add(meter_lead(x + 40, 345, x + 311, 268, INK, 40), meter_lead(x + 79, 345, x + 409, 268, RED, 70))
    d.add((check if not broken else cross)(x + 30, 470, 18), T(x + 58, 477, txt, 19, c, 700))
    d.add(T(x + 280, 400, "♪ beep" if not broken else "silence", 18, c, 700, "middle", italic=True))
d.save()

# ---------- Ch3: diode scale ----------
d = Fig("s3_diode_scale", "What diode-mode readings mean on a phone board", "Red probe on ground, black probe on the line. Compare with the same point on a good board.", 1200, 560, "Exact values differ by model. The pattern is what matters: near zero is a short, OL is open.")
d.add(scale_bar(60, 200, 1080, [(.14, RED, "0.000–0.050", "SHORT\nto ground"), (.14, "#f9a825", "0.05–0.25", "Low: suspect,\ncompare"),
                                 (.36, GREEN, "0.25 – 0.90", "Normal for most power\nand signal lines"), (.2, "#42a5f5", "0.90 – 1.3", "Higher: normal\nfor data lines"), (.16, "#78909c", "OL", "Open: broken\nor not connected")], 70))
for x, v in [(60, "0.00"), (211, "0.05"), (362, "0.25"), (751, "0.90"), (967, "1.30")]: d.add(L(x, 180, x, 200, INK, 2), T(x, 172, v, 15, INK, 600, "middle"))
d.add(note(60, 380, 1080, 84, "A reading of 0.000 on VBAT or VPH_PWR means a short. Current from the battery or power\nsupply will rush into it and the faulty part will heat up.", RED, 16))
d.save()

# ---------- Ch3: voltage probes ----------
d = Fig("s3_voltage_probes", "Voltage mode: where to put the probes", "Black probe on a good ground (a shield or screw hole). Red probe on the point you want to measure.", 1200, 640)
d.add(multimeter(70, 150, "1.802", "V DC", 1.3))
d.add(pcb(380, 120, 760, 400), R(420, 170, 260, 160, "url(#shield)", "#90a4ae", 8, 2), T(550, 255, "shield = GROUND", 16, "#455a64", 700, "middle"))
d.add(C(1080, 470, 16, "#cfd8dc", "#90a4ae", 3), C(1080, 470, 7, "#455a64"), T(1080, 505, "screw hole (GND)", 13, "#e8f5e9", 600, "middle"))
d.add(chip(760, 200, 110, 80, "PMIC"), trace([(870, 240), (980, 240), (980, 380)]), smd(965, 380, vertical=True), T(1005, 400, "C2100\n1.8 V line", 14, "#e8f5e9", 600))
d.add(meter_lead(122, 440, 560, 320, INK, 70), meter_lead(167, 440, 980, 398, RED, 120))
d.add(T(330, 590, "black → ground", 18, INK, 700), T(700, 590, "red → test point", 18, RED, 700))
d.save()

# ---------- Figure 3.1 capacitor diode mode ----------
d = Fig("s3_fig1", "Figure 3.1  Testing a filter capacitor in diode mode", "Battery removed. Red probe on ground, black probe on each end of the capacitor.", 1200, 700)
d.add(pcb(60, 130, 640, 440))
d.add(R(90, 200, 580, 26, "url(#copper)", "none", 4), T(100, 190, "VBAT line", 17, "#fff", 700))
d.add(R(90, 470, 580, 26, "#9e9e9e", "none", 4), T(100, 460, "GROUND", 17, "#fff", 700))
for i, x in enumerate([200, 380, 560]):
    d.add(L(x, 226, x, 300, "#d4af37", 5), smd(x - 12, 300, 44, 24, vertical=True) if False else R(x - 14, 300, 28, 90, "#8d6e4a", "#4e342e", 3, 1.5), R(x - 14, 300, 28, 18, "#cfd8dc", "none", 2), R(x - 14, 372, 28, 18, "#cfd8dc", "none", 2), L(x, 390, x, 470, "#bdbdbd", 5), T(x + 22, 350, f"C{i+1}", 15, "#fff", 700))
d.add(multimeter(860, 130, "0.412", "DIODE", 1.3))
d.add(meter_lead(912, 420, 560, 304, INK, 60), meter_lead(957, 420, 640, 470, RED, 30))
d.add(R(60, 600, 1100, 72, "#fff", "none", 0))
for i, (t, c) in enumerate([("Line end 0.300 – 0.700 = normal", GREEN), ("Ground end 0.000 = normal (it is ground)", BLUE), ("Line end 0.000 = the line is SHORTED", RED)]):
    d.add(R(60 + i * 370, 600, 350, 60, TINT[c], LINE[c], 12, 2), T(235 + i * 370, 636, t, 15.5, c, 700, "middle"))
d.save()

# ---------- Figure 3.2 series / parallel ----------
d = Fig("s3_fig2", "Figure 3.2  Series and parallel circuits on a phone board", "", 1200, 640)
d.add(R(40, 100, 540, 500, "#fff", LINE[BLUE], 18, 2, True), R(620, 100, 540, 500, "#fff", LINE[GREEN], 18, 2, True))
d.add(T(70, 145, "SERIES: one path, same current", 21, BLUE, 700))
d.add(T(70, 250, "VBUS", 16, RED, 700), PL([(125, 245), (165, 245)], INK, 3), res_sym(165, 245, 70, INK, "F (fuse)"), PL([(235, 245), (275, 245)], INK, 3), coil_sym(275, 245, 4, INK, "L (coil)"), PL([(347, 245), (390, 245)], INK, 3), box(390, 215, 150, 60, "Charging IC", NAVY, 15))
d.add(arrow(130, 300, 470, 300, BLUE, 3), T(300, 325, "current flows through each part in turn", 14, BLUE, 600, "middle"))
d.add(T(70, 395, "R total = R1 + R2 + R3", 20, NAVY, 700, mono=True))
d.add(note(70, 430, 480, 120, "If the fuse or coil OPENS,\nnothing after it gets power:\nthe phone will not charge.", RED, 16))
d.add(T(650, 145, "PARALLEL: many paths, same voltage", 21, GREEN, 700))
d.add(L(680, 210, 1120, 210, "#d4af37", 6), T(680, 196, "VBAT line", 16, "#b8892e", 700), L(680, 400, 1120, 400, "#9e9e9e", 6), T(680, 430, "GROUND", 16, "#757575", 700))
for i, x in enumerate([740, 840, 940, 1040]):
    d.add(L(x, 210, x, 285, INK, 2.5), cap_sym(x, 285, INK, f"C{i+1}"), L(x, 325, x, 400, INK, 2.5))
d.add(L(915, 280, 965, 340, RED, 6), L(965, 280, 915, 340, RED, 6))
d.add(T(650, 480, "1/R total = 1/R1 + 1/R2 + ...", 20, NAVY, 700, mono=True))
d.add(T(650, 520, "C3 shorted: the WHOLE VBAT line", 17, RED, 700), T(650, 545, "reads 0.000 at every capacitor.", 17, RED, 700))
d.save()
render_all()

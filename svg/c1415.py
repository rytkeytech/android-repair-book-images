from sv import *

def joint_scene(x, y, kind):
    o = [R(x, y + 40, 200, 24, "url(#pcb)", "#123d22", 4, 1.5), R(x + 18, y + 32, 50, 9, "url(#copper)", "none", 2), R(x + 132, y + 32, 50, 9, "url(#copper)", "none", 2)]
    body = R(x + 50, y, 100, 32, "#8d6e4a", "#4e342e", 3, 1.5)
    if kind == "good": o += [body, P(f"M{x+20} {y+32} Q{x+42} {y+30} {x+52} {y+4} L{x+52} {y+32} Z", fill="#cfd8dc", stroke="#78909c", sw=1.5), P(f"M{x+180} {y+32} Q{x+158} {y+30} {x+148} {y+4} L{x+148} {y+32} Z", fill="#cfd8dc", stroke="#78909c", sw=1.5)]
    if kind == "much": o += [body, C(x + 40, y + 12, 26, "#cfd8dc", "#78909c", 1.5), C(x + 160, y + 12, 26, "#cfd8dc", "#78909c", 1.5)]
    if kind == "cold": o += [R(x + 50, y - 10, 100, 32, "#8d6e4a", "#4e342e", 3, 1.5), P(f"M{x+24} {y+32} L{x+44} {y+22} L{x+52} {y+30} Z", fill="#9e9e9e", stroke="#757575", sw=1.5), P(f"M{x+176} {y+32} L{x+156} {y+22} L{x+148} {y+30} Z", fill="#9e9e9e", stroke="#757575", sw=1.5)]
    if kind == "bridge": o += [R(x + 18, y + 18, 164, 16, "#cfd8dc", "#78909c", 6, 1.5), body]
    if kind == "tomb": o += [P(f"M{x+140} {y+32} L{x+83} {y-25} L{x+106} {y-47} L{x+163} {y+9} Z", fill="#8d6e4a", stroke="#4e342e", sw=1.5), P(f"M{x+150} {y+32} Q{x+166} {y+30} {x+172} {y+12} L{x+182} {y+32} Z", fill="#cfd8dc", stroke="#78909c", sw=1.5)]
    return "".join(o)

# ---------- tools ----------
d = Fig("s14_tools", "Basic soldering tools and what each is for", "", 1200, 640)
tools = [("Soldering iron", "joints, pins,\njumper wires", ORANGE, lambda x, y: iron(x - 80, y, -20, .9)), ("Hot-air station", "chips, connectors,\nshields", RED, lambda x, y: nozzle(x, y + 20, .9)),
         ("Microscope", "see joints and\nbridges", BLUE, lambda x, y: R(x - 30, y + 20, 60, 22, "#455a64", "none", 6) + R(x - 8, y - 40, 16, 64, "#37474f", "none", 4) + C(x, y - 44, 24, "url(#dev)", "#78909c", 2) + C(x - 10, y - 56, 7, "#263238") + C(x + 10, y - 56, 7, "#263238")),
         ("Flux", "helps solder flow,\nstops oxidation", TEAL, lambda x, y: R(x - 12, y - 50, 24, 90, "#fff59d", "#f9a825", 6, 2) + R(x - 4, y - 66, 8, 18, "#f9a825", "none", 2) + T(x, y, "FLUX", 9, "#795548", 800, "middle")),
         ("Solder wire + paste", "0.3–0.5 mm wire,\nlow-temp paste", GRAY, lambda x, y: C(x, y - 6, 36, "url(#metal)", "#78909c", 2) + C(x, y - 6, 12, "#fff", "#78909c", 2) + P(f"M{x+30} {y+14} q30 10 40 40", stroke="#9e9e9e", sw=4)),
         ("Desoldering wick", "removes extra\nsolder from pads", "#8d6e4a" if False else ORANGE, lambda x, y: C(x, y - 6, 34, "#ffe082", "#c49000", 2) + R(x + 20, y - 4, 50, 12, "url(#copper)", "none", 2)),
         ("Tweezers", "fine tips,\nanti-static", PURPLE, lambda x, y: P(f"M{x-40} {y-40} L{x+40} {y+20} M{x-40} {y-30} L{x+40} {y+22}", stroke="#78909c", sw=5)),
         ("IPA + brush", "clean flux after\nevery job", GREEN, lambda x, y: R(x - 30, y - 50, 40, 90, "#e3f2fd", "#64b5f6", 8, 2) + T(x - 10, y, "IPA", 12, BLUE, 800, "middle") + R(x + 20, y - 40, 10, 70, "#a1887f", "none", 3) + R(x + 16, y + 26, 18, 18, "#212121", "none", 2))]
for i, (t, s, c, draw) in enumerate(tools):
    x = 40 + (i % 4) * 285; y = 110 + (i // 4) * 260
    d.add(R(x, y, 265, 240, "#fff", LINE[c], 18, 2, True), R(x, y, 265, 120, TINT[c], "none", 18), R(x, y + 100, 265, 20, TINT[c], "none", 0), draw(x + 132, y + 74))
    d.add(T(x + 132, y + 160, t, 18, c, 800, "middle"), T(x + 132, y + 190, s, 14.5, "#37474f", 400, "middle"))
d.save()

# ---------- melting ----------
d = Fig("s14_melting", "Melting points: why the right solder matters", "Adding leaded solder to factory lead-free joints lowers their melting point, so parts come off with less heat.", 1200, 480)
items = [("Low-temp paste (Sn-Bi)", 138, TEAL), ("Leaded solder (Sn63/Pb37)", 183, BLUE), ("Lead-free (SAC305), factory", 217, ORANGE), ("Typical iron setting", 330, RED)]
for i, (n, v, c) in enumerate(items):
    y = 130 + i * 76
    d.add(T(370, y + 34, n, 17, "#263238", 700, "end"), R(390, y + 6, v * 2.0, 44, c, "none", 22), T(400 + v * 2.0, y + 36, f"{v} °C", 19, c, 800))
d.save()

# ---------- Figure 14.1 solder joints ----------
d = Fig("s14_fig1", "Figure 14.1  Good and bad solder joints (side view of a small component)", "", 1200, 480)
kinds = [("Good joint", "good", GREEN, "Smooth, shiny, concave\nfillet; pad fully wetted"), ("Too much solder", "much", RED, "Ball-shaped; may hide a\nbad joint or a bridge"), ("Cold / dry joint", "cold", RED, "Dull, grainy, not wetted;\nintermittent faults"),
         ("Solder bridge", "bridge", RED, "Solder joins two pads:\na short circuit"), ("Tombstone", "tomb", RED, "One end lifted; uneven\nheat or paste")]
for i, (t, k, c, s) in enumerate(kinds):
    x = 40 + i * 228
    d.add(R(x, 100, 210, 330, "#fff", LINE[c], 16, 2, True), (check if c == GREEN else cross)(x + 105, 138, 16), T(x + 105, 182, t, 16.5, c, 800, "middle"), joint_scene(x + 5, 250, k), T(x + 105, 366, s, 13.5, "#37474f", 400, "middle"))
d.save()

# ---------- hot air ----------
d = Fig("s14_hot_air", "Hot air technique: height, movement and shielding", "", 1200, 600)
d.add(R(60, 470, 560, 30, "url(#pcb)", "#123d22", 4, 2), R(260, 446, 160, 24, "#263238", "none", 3), R(90, 456, 110, 14, "#ffcc80", "#e65100", 2, 1.5), T(145, 412, "Kapton / foil\nshield", 14, ORANGE, 700, "middle"), T(340, 530, "board", 14, MUTED, 600, "middle"))
d.add(nozzle(340, 300, 1.6), P("M250 260 a90 30 0 1 0 180 0", stroke=GRAY, sw=2.5, arrow=True, dash="6 5"), T(340, 150, "move in small circles", 16, GRAY, 700, "middle"))
d.add(L(480, 380, 480, 440, NAVY, 2.5, arrow=True), L(480, 440, 480, 380, NAVY, 2.5, arrow=True), T(494, 418, "2–3 cm", 17, NAVY, 800))
rows = [("Small parts (capacitors, resistors)", "300–330 °C, low airflow"), ("Connectors", "330–360 °C, shield the plastic"), ("Shields (metal cans)", "350–380 °C, heat the edges evenly"), ("Chips (BGA)", "preheat the board, then 350–400 °C")]
d.add(T(680, 140, "Starting points (adjust for your station)", 18, NAVY, 800))
for i, (a, b) in enumerate(rows): d.add(R(680, 160 + i * 92, 480, 76, TINT[ORANGE] if i % 2 == 0 else "#fff", LINE[ORANGE], 12, 2), T(700, 192 + i * 92, a, 17, ORANGE, 800), T(700, 218 + i * 92, b, 15.5, "#263238"))
d.save()

# ---------- small parts ----------
d = Fig("s14_small_parts", "Replacing a small component (capacitor, resistor, coil)", "Measure the replaced line in diode mode before you power the phone.", 1200, 380)
d.add(flow(40, 140, ["Flux", "Heat both\nends", "Lift off", "Clean\npads", "Place new\npart", "Reflow +\ncheck"], 160, 96, 32, [BLUE, ORANGE, BLUE, TEAL, BLUE, GREEN], 17,
           ["on both ends", "tweezers, two irons\nor hot air", "do not drag\nor push", "wick, then\nfresh flux", "same value and size,\nright direction", "shiny fillets,\nno bridges"], 14))
d.save()

# ---------- Figure 14.2 jumper wire ----------
d = Fig("s14_fig2", "Figure 14.2  Repairing a broken track with a jumper wire", "", 1200, 760)
d.add(pcb(40, 100, 1120, 340))
d.add(trace([(120, 300), (480, 300)], 8), trace([(640, 300), (1080, 300)], 8), R(470, 286, 180, 28, "#1b5631", "none", 0), P("M480 300 l14 -10 l16 18 l18 -16 l18 14", stroke="#d4af37", sw=4), C(560, 300, 60, "none", "#ff7043", 3), T(560, 400, "broken track\n(corrosion or a scratch)", 15, "#ffccbc", 700, "middle"))
d.add(R(180, 284, 70, 32, "#8d6e4a", "#4e342e", 3, 2), R(180, 284, 16, 32, "#cfd8dc", "none", 2), R(234, 284, 16, 32, "#cfd8dc", "none", 2), T(215, 270, "C1", 16, "#fff", 800, "middle"))
d.add(R(940, 284, 70, 32, "#212121", "none", 3, 2), R(940, 284, 16, 32, "#cfd8dc", "none", 2), R(994, 284, 16, 32, "#cfd8dc", "none", 2), T(975, 270, "R7", 16, "#fff", 800, "middle"))
d.add(P("M242 300 C400 140 800 140 948 300", stroke="#ffb300", sw=4.5), C(242, 300, 9, "#cfd8dc", "#78909c", 2), C(948, 300, 9, "#cfd8dc", "#78909c", 2), T(595, 172, "enamelled copper jumper wire", 18, "#ffe082", 800, "middle"))
d.add(T(150, 200, "solder to the nearest\npad on the same net", 14, "#e8f5e9", 700, "middle"))
steps = ["Find the break: continuity mode from point to point along the line, using the schematic or board view.", "Choose the two nearest good points on the same net (component pads or test points), not the damaged track itself.",
         "Cut a thin enamelled wire to length. Scrape or burn off the enamel only at the ends, and tin the ends with solder.", "Solder each end with flux and a fine tip. Check continuity end to end, and that there is no short to nearby parts.", "Fix the wire in place with UV solder mask or glue so it cannot move or break when the phone is reassembled."]
for i, s in enumerate(steps): d.add(badge(60, 486 + i * 48, i + 1, ORANGE, 15, 14), T(88, 492 + i * 48, s, 15.5, "#263238"))
d.save()

# ---------- good vs bad joints (alt) ----------
d = Fig("s14_joints", "Good and bad solder joints", "Check every joint under the microscope. Cold joints and bridges cause most 'repair did not work' returns.", 1200, 460)
for i, (t, k, c, s) in enumerate([("GOOD", "good", GREEN, "smooth, shiny,\nconcave fillet"), ("COLD", "cold", ORANGE, "dull, grainy,\nballed up"), ("BRIDGE", "bridge", RED, "solder joins\ntwo pads"), ("TOO MUCH", "much", PURPLE, "hides the joint,\nmay bridge")]):
    x = 40 + i * 285
    d.add(R(x, 110, 265, 300, "#fff", LINE[c], 16, 2, True), T(x + 132, 152, t, 21, c, 800, "middle"), joint_scene(x + 32, 230, k), T(x + 132, 350, s, 15, "#37474f", 400, "middle"))
d.save()

# ---------- Ch15 chip faulty ----------
d = Fig("s15_chip_faulty", "Before you remove a chip: is it really the chip?", "Expensive and risky chip work should be the last step, not the first.", 1200, 600)
qs = ["Are its power lines present (correct voltage)?", "Is its clock or crystal working?", "Do its enable and control signals arrive?", "Is nothing shorted around it?"]
for i, q in enumerate(qs):
    y = 120 + i * 92
    d.add(R(40, y, 560, 70, TINT[BLUE], LINE[BLUE], 14, 2, True), badge(76, y + 35, i + 1, BLUE, 16, 15), T(104, y + 42, q, 17, NAVY, 700), arrow(606, y + 35, 660, y + 35, RED, 3), T(672, y + 42, "NO → fix that first; the chip may be fine", 16, RED, 700))
d.add(R(40, 500, 560, 70, GREEN, "none", 14, 0, True), T(320, 543, "All YES, still no output", 18, "#fff", 800, "middle"), arrow(606, 535, 660, 535, GREEN, 3), T(672, 542, "Now suspect the chip: reflow or replace", 16, GREEN, 800))
d.save()

# ---------- Figure 15.1 BGA section ----------
d = Fig("s15_fig1", "Figure 15.1  A BGA chip: why the joints are hidden (cross-section)", "You cannot see or touch these joints. Drops, heat and corrosion are the main causes of BGA joint failure.", 1200, 600)
d.add(R(60, 410, 1080, 80, "url(#pcb)", "#123d22", 6, 2, True), T(600, 460, "MOTHERBOARD", 18, "#fff", 800, "middle"))
d.add(R(200, 230, 800, 100, "#263238", "#111", 8, 2, True), R(200, 330, 800, 16, "#546e7a", "none", 0), T(600, 290, "CHIP  (PMIC, CPU, eMMC/UFS, Wi-Fi ...)", 18, "#cfd8dc", 800, "middle"))
for i in range(12):
    x = 240 + i * 66
    bad = i == 7
    d.add(R(x - 16, 346, 32, 6, "url(#copper)", "none", 1), R(x - 16, 404, 32, 6, "url(#copper)", "none", 1), C(x, 378, 24, "#ffcdd2" if bad else "#cfd8dc", RED if bad else "#78909c", 3 if bad else 1.5))
    if bad: d.add(P(f"M{x-10} 364 l8 10 l-6 6 l10 12", stroke=RED, sw=2.5))
d.add(P("M180 300 L200 346 L200 410 L170 410 Z", fill="#ffe082", stroke="#c49000", sw=1.5, op=.85), P("M1020 300 L1000 346 L1000 410 L1030 410 Z", fill="#ffe082", stroke="#c49000", sw=1.5, op=.85))
d.add(leader(306, 378, 140, 170, 1, "Solder balls", "hundreds, under the chip", BLUE, 17) if False else "")
d.add(P("M306 378 L240 180", stroke=BLUE, sw=2), T(240, 168, "solder balls (hundreds, under the chip)", 15, BLUE, 700, "middle"))
d.add(P("M702 378 L760 170", stroke=RED, sw=2), T(760, 140, "cracked or lifted ball:", 15, RED, 800, "middle"), T(760, 160, "intermittent or dead", 15, RED, 600, "middle"))
d.add(P("M1012 330 L1060 190", stroke="#b8892e", sw=2), T(1060, 170, "underfill glue", 15, "#b8892e", 800, "middle"), T(1060, 186, "(on some chips)", 13, "#b8892e", 600, "middle"))
d.add(P("M240 407 L150 540", stroke=GREEN, sw=2), T(150, 560, "board pads", 15, GREEN, 800, "middle"))
d.save()

# ---------- removing ----------
d = Fig("s15_removing", "Removing a BGA chip safely", "If underfill (glue) is under the chip, soften it and remove it slowly. Prying lifts the pads.", 1200, 380)
d.add(flow(40, 140, ["Back up\ndata", "Shield\nparts", "Preheat", "Flux\naround", "Heat\nevenly", "Lift\ngently"], 160, 96, 32, [ORANGE, BLUE, BLUE, BLUE, RED, GREEN], 17,
           ["memory or storage?\nask the customer", "Kapton or foil on\nnearby plastic", "board to\n150–180 °C", "soak the edges\nof the chip", "hot-air circles,\nabout 350–400 °C", "when it 'floats',\ndon't force it"], 14))
d.save()

# ---------- pads ----------
d = Fig("s15_pads", "Preparing the board: what the pads should look like", "", 1200, 520)
for i, (t, c) in enumerate([("GOOD: flat, shiny, all present", GREEN), ("BAD: torn or missing pads, old glue", RED)]):
    x = 40 + i * 570
    d.add(R(x, 100, 550, 380, "#fff", LINE[c], 18, 2, True), R(x + 40, 140, 470, 250, "url(#pcb)", "#123d22", 10, 2))
    for r in range(5):
        for k in range(10):
            px, py = x + 80 + k * 44, 175 + r * 44
            if i == 1 and (r, k) in ((1, 3), (3, 7)): d.add(C(px, py, 11, "#1b5631", "#0d3b1e", 2)); continue
            if i == 1 and (r, k) == (2, 8): d.add(P(f"M{px-6} {py+6} L{px+10} {py-12}", stroke="#e0c068", sw=6)); continue
            d.add(C(px, py, 11, "#e8c96e"))
    if i == 1:
        d.add(R(x + 60, 300, 120, 80, "#d7ccc8", "none", 6, 0, False, .85), T(x + 120, 346, "old glue", 14, "#5d4037", 800, "middle"))
        d.add(C(x + 212, 219, 22, "none", "#ff7043", 3), T(x + 212, 132, "missing pad", 14, ORANGE, 800, "middle"), L(x + 212, 138, x + 212, 196, ORANGE, 2), C(x + 432, 263, 22, "none", "#ff7043", 3), T(x + 432, 132, "torn pad", 14, ORANGE, 800, "middle"), L(x + 432, 138, x + 432, 240, ORANGE, 2))
    d.add((check if c == GREEN else cross)(x + 44, 430, 16), T(x + 70, 437, t, 18, c, 800))
d.save()

# ---------- Figure 15.2 reballing ----------
d = Fig("s15_fig2", "Figure 15.2  Reballing a BGA chip, step by step", "Finally: clean the board pads, add flux, align the chip exactly (dot or corner mark) and reflow until it settles by itself.", 1200, 760)
steps = [("Remove the chip", "hot air + flux; lift when free"), ("Clean the pads", "wick + flux: pads flat and clean"), ("Apply thin flux", "a thin, even layer"), ("Fit the stencil", "line the holes up over the pads"), ("Add paste or balls", "spread paste into every hole"), ("Reflow and inspect", "heat until balls form; every ball\nround and equal")]
for i, (t, s) in enumerate(steps):
    x = 40 + (i % 3) * 380; y = 110 + (i // 3) * 310
    d.add(R(x, y, 360, 290, "#fff", "#dfe5ec", 18, 2, True), badge(x + 34, y + 36, i + 1, ORANGE, 17, 15), T(x + 62, y + 43, t, 18, NAVY, 800), T(x + 180, y + 80, s, 14, MUTED, 400, "middle"))
    cx = x + 180; base = y + 200
    if i == 0: d.add(R(cx - 110, base + 20, 220, 22, "url(#pcb)", "none", 3), R(cx - 70, base - 30, 140, 22, "#263238", "none", 3), *[C(cx - 60 + k * 20, base - 2, 7, "#cfd8dc", "#78909c", 1) for k in range(7)], nozzle(cx, base - 56, .6))
    else:
        d.add(R(cx - 110, base, 220, 34, "#263238", "none", 4), T(cx, base + 22, "chip (upside down)", 12, "#cfd8dc", 600, "middle"))
        for k in range(7):
            px = cx - 72 + k * 24
            if i in (1, 2, 3, 4): d.add(R(px - 8, base - 6, 16, 6, "url(#copper)", "none", 1))
            if i == 5: d.add(C(px, base - 10, 9, "#cfd8dc", "#78909c", 1.5))
        if i == 1: d.add(R(cx - 100, base - 40, 200, 10, "url(#copper)", "none", 3), T(cx, base - 52, "wick", 12, "#8d6e1a", 700, "middle"))
        if i == 2: d.add(R(cx - 90, base - 14, 180, 8, "#ffe082", "none", 3, 0, False, .8))
        if i in (3, 4):
            d.add(R(cx - 100, base - 22, 200, 14, "#b0bec5", "#78909c", 2, 1.5))
            for k in range(7): d.add(R(cx - 78 + k * 24, base - 22, 12, 14, "#fff" if i == 3 else "#cfd8dc", "none", 6 if i == 4 else 1))
d.save()

# ---------- align ----------
d = Fig("s15_align", "Fitting the chip: let surface tension align it", "Never press the chip down. A gentle nudge to check it 'floats' and springs back is enough.", 1200, 440)
for i, (t, off) in enumerate([("1. Place close to the marks", 26), ("2. Heat: the solder melts", 12), ("3. The chip pulls itself into place", 0)]):
    x = 40 + i * 390
    d.add(R(x, 100, 360, 280, "#fff", "#dfe5ec", 18, 2, True), T(x + 180, 350, t, 17, NAVY, 800, "middle"))
    d.add(R(x + 40, 270, 280, 30, "url(#pcb)", "none", 4))
    for k in range(6): d.add(R(x + 62 + k * 44, 262, 26, 8, "url(#copper)", "none", 2))
    d.add(R(x + 50 + off, 196, 260, 40, "#263238", "none", 4))
    for k in range(6): d.add(C(x + 75 + off + k * 44 - (off * .5 if i == 1 else 0), 248 + (2 if i == 1 else 0), 11 if i != 1 else 12, "#cfd8dc", "#78909c", 1.5))
    if i == 0: d.add(P(f"M{x+52} 170 l10 -18 l10 18 z", fill=ORANGE, stroke=ORANGE, sw=1), T(x + 62, 146, "corner mark", 12, ORANGE, 700, "middle"))
    if i == 1: d.add(P(f"M{x+150} 180 l20 -10 l20 10", stroke="#ff7043", sw=3), P(f"M{x+190} 180 l20 -10 l20 10", stroke="#ff7043", sw=3))
    if i < 2: d.add(arrow(x + 364, 240, x + 386, 240, ORANGE, 3))
d.save()
render_all()

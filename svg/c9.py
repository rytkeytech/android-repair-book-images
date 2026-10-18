from sv import *

# ---------- symptoms ----------
d = Fig("s9_symptoms", "Charging symptoms and their usual causes", "Always start with the cheapest checks: clean the port, try a known-good cable and charger, then a good battery.", 1200, 600)
syms = [("Not charging at all", "Port, cable, fuse, OVP, charging IC", RED), ("Charging slowly", "Dirty port, weak cable, fake charger, CC pins", ORANGE), ("Charges only at an angle", "Worn or loose port, cracked solder joint", ORANGE),
        ("Shows charging, % not rising", "Bad battery, BTEMP / BSI line, fuel gauge", PURPLE), ("Charging icon on and off", "Port, cable, OVP, liquid damage", BLUE), ("Phone hot while charging", "Short on VBUS or VBAT, battery, charging IC", RED)]
for i, (s, c_, col) in enumerate(syms):
    x = 40 + (i % 2) * 570; y = 120 + (i // 2) * 150
    d.add(R(x, y, 550, 128, "#fff", LINE[col], 18, 2, True), R(x, y, 12, 128, col, "none", 6))
    d.add(C(x + 62, y + 64, 32, TINT[col]), P(f"M{x+58} {y+44} l-10 22 h12 l-6 20 l18 -26 h-12 l8 -16 z", fill=col, stroke=col, sw=1))
    d.add(T(x + 112, y + 54, s, 20, col, 700), T(x + 112, y + 86, c_, 15.5, "#263238"))
d.save()

# ---------- Figure 9.1 charging check points ----------
d = Fig("s9_fig1", "Figure 9.1  The charging path and where to measure", "Follow the numbers from the port to the battery. The first missing voltage is your fault area.", 1200, 760)
blocks = [(50, "Charging\nport", "#546e7a"), (230, "Fuse", "#6d4c41"), (390, "OVP\n(protection)", "#455a64"), (590, "Charging IC\n(or PMIC)", NAVY), (830, "Coil", "#6d4c41"), (990, "Battery\nconnector", "#37474f")]
for x, t, c in blocks:
    w = 170 if "Charging IC" in t else (130 if "port" in t or "OVP" in t or "Battery" in t else 100)
    d.add(box(x, 160 if "Charging IC" not in t else 140, w, 90 if "Charging IC" not in t else 130, t, c, 15))
d.add(L(180, 205, 230, 205, RED, 4), L(330, 205, 390, 205, RED, 4), L(520, 205, 590, 205, RED, 4), L(760, 205, 830, 205, RED, 4), L(930, 205, 990, 205, RED, 4))
d.add(T(205, 194, "VBUS", 12, RED, 800, "middle"), T(555, 194, "VCHG", 12, RED, 800, "middle"), T(960, 194, "VBAT", 12, RED, 800, "middle"))
d.add(PL([(115, 250), (115, 330), (680, 330), (680, 270)], BLUE, 3), T(400, 320, "D+ / D–  (charger handshake, fast charge)", 14, BLUE, 700, "middle"))
d.add(PL([(95, 250), (95, 370), (715, 370), (715, 270)], PURPLE, 3), T(400, 362, "CC1 / CC2  (USB-C only: detects cable and charger)", 14, PURPLE, 700, "middle"))
d.add(PL([(1055, 250), (1055, 400), (750, 400), (750, 270)], GREEN, 3), T(900, 424, "NTC / BAT_ID (battery temperature and type)", 14, GREEN, 700, "middle"))
for n, (x, y) in enumerate([(205, 230), (360, 230), (555, 230), (960, 230), (115, 290), (1055, 330)], 1): d.add(badge(x, y, n))
steps = ["VBUS at the port: about 5 V with a charger (9 V or more with some fast chargers).", "After the fuse: same as 1. If 0 V, the fuse is open: check VBUS for a short first.",
         "After the OVP: same as 1. If 5 V goes in but nothing comes out, the OVP is faulty or blocking a fault.", "VBAT should rise slowly while charging. Check the coil if the charging IC has output but VBAT does not.",
         "Data and CC lines: diode-mode readings compared with a good board. A short here can stop charging.", "NTC line: missing or damaged makes the phone think the battery is too hot or too cold."]
for i, s in enumerate(steps): d.add(badge(64, 470 + i * 44, i + 1, ORANGE, 14, 13), T(92, 476 + i * 44, s, 15.5, "#263238"))
d.save()

# ---------- Figure 9.2 port pinouts ----------
d = Fig("s9_fig2", "Figure 9.2  Charging port pins (looking into the phone's port)", "Pin colours: red = power, blue = data, purple = configuration (CC), green = ID. Check a schematic for the exact phone.", 1200, 700)
d.add(R(40, 110, 360, 540, "#fff", "#dfe5ec", 18, 2, True), T(70, 150, "Micro-USB (5 pins)", 20, NAVY, 700))
d.add(R(80, 190, 280, 90, "url(#metal)", "#607d8b", 14, 2), R(100, 210, 240, 50, "#263238", "none", 6))
cols5 = [("VBUS", RED), ("D–", BLUE), ("D+", BLUE), ("ID", GREEN), ("GND", INK)]
for i, (n, c) in enumerate(cols5):
    x = 118 + i * 46
    d.add(R(x, 222, 30, 26, "#d4af37", "none", 3), T(x + 15, 304, str(i + 1), 15, INK, 700, "middle"), T(x + 15, 330, n, 14, c, 800, "middle"))
for i, s in enumerate(["Pin 1  VBUS: 5 V from the charger", "Pins 2, 3  D–, D+: data and charger detection", "Pin 4  ID: OTG detection (often unused)", "Pin 5  GND: ground"]): d.add(T(70, 400 + i * 34, s, 15.5, "#263238"))
d.add(R(420, 110, 740, 540, "#fff", "#dfe5ec", 18, 2, True), T(450, 150, "USB-C (24 pins in two rows)", 20, NAVY, 700))
d.add(R(450, 180, 680, 200, "url(#metal)", "#607d8b", 100, 2), R(500, 262, 580, 34, "#37474f", "none", 17))
top = [("GND", INK), ("TX1+", GRAY), ("TX1–", GRAY), ("VBUS", RED), ("CC1", PURPLE), ("D+", BLUE), ("D–", BLUE), ("SBU1", GRAY), ("VBUS", RED), ("RX2–", GRAY), ("RX2+", GRAY), ("GND", INK)]
bot = [("GND", INK), ("RX1+", GRAY), ("RX1–", GRAY), ("VBUS", RED), ("SBU2", GRAY), ("D–", BLUE), ("D+", BLUE), ("CC2", PURPLE), ("VBUS", RED), ("TX2–", GRAY), ("TX2+", GRAY), ("GND", INK)]
for i in range(12):
    x = 520 + i * 47
    d.add(R(x, 232, 26, 22, "#d4af37", "none", 3), R(x, 304, 26, 22, "#d4af37", "none", 3))
    d.add(T(x + 13, 222, top[i][0], 11.5, top[i][1], 800, "middle"), T(x + 13, 344, bot[11 - i][0], 11.5, bot[11 - i][1], 800, "middle"))
    d.add(T(x + 13, 246 + 0, f"A{i+1}", 9, "#5d4037", 700, "middle"), T(x + 13, 319, f"B{12-i}", 9, "#5d4037", 700, "middle"))
for i, (s, c) in enumerate([("VBUS (A4, A9, B4, B9): 5 V, or up to 20 V with fast charging", RED), ("GND (A1, A12, B1, B12): ground", INK), ("CC1, CC2: tell the phone a cable and charger are connected", PURPLE),
                            ("D+, D–: data and older charger detection", BLUE), ("TX / RX / SBU: high-speed data, often unused on budget phones", GRAY)]):
    d.add(C(462, 420 + i * 40, 7, c), T(480, 426 + i * 40, s, 15.5, "#263238"))
d.save()

# ---------- Figure 9.3 battery communication ----------
d = Fig("s9_fig3", "Figure 9.3  How the battery talks to the phone (typical modern battery)", "Older phones may have only BAT+, BAT–, NTC and ID. Pin names differ by brand: always confirm with the schematic.", 1200, 760)
d.add(R(40, 110, 560, 590, "#f5f7f9", "#cfd8dc", 20, 2, True), T(70, 148, "BATTERY PACK", 18, NAVY, 800))
d.add(R(70, 180, 130, 230, GREEN, "none", 16, 0, True), T(135, 280, "Li-ion\ncell", 18, "#fff", 800, "middle"), T(135, 340, "3.8 V\nnominal", 14, "#e8f5e9", 600, "middle"))
d.add(R(250, 180, 160, 110, "#37474f", "none", 14, 0, True), T(330, 225, "Protection", 15, "#fff", 700, "middle"), T(330, 247, "IC + MOSFETs", 14, "#cfd8dc", 400, "middle"))
d.add(R(250, 340, 160, 110, NAVY, "none", 14, 0, True), T(330, 385, "Fuel gauge /", 15, "#fff", 700, "middle"), T(330, 407, "auth chip", 14, "#cfd8dc", 400, "middle"))
d.add(R(250, 510, 70, 90, "#ffcc80", "#e65100", 8, 2), T(285, 625, "NTC", 14, ORANGE, 800, "middle"), R(340, 510, 70, 90, "#e1bee7", PURPLE, 8, 2), T(375, 625, "ID", 14, PURPLE, 800, "middle"))
d.add(R(470, 160, 60, 520, "#cfd8dc", "#90a4ae", 8, 2), T(500, 150, "connector", 13, NAVY, 700, "middle"))
pins = [(210, "BAT+  (VBAT)", RED, "PMIC / charging IC (power in)", "charges and receives power"), (290, "SDA  (data)", BLUE, None, None), (330, "SCL  (clock)", BLUE, "CPU / PMIC I2C bus", "reads %, health, cycles, genuine or not"),
        (410, "BTEMP / NTC", ORANGE, "ADC in the PMIC / charging IC", "reads battery temperature"), (470, "BSI / BAT_ID", PURPLE, None, None), (640, "BAT–  (GND)", INK, "Ground", "")]
for y, n, c, dst, note_ in pins:
    d.add(R(482, y - 10, 36, 20, "#ffd54f", "#c49000", 3, 1.5), L(530, y, 700, y, c, 3), T(540, y - 8, n, 14, c, 800))
d.add(PL([(200, 230), (250, 230)], RED, 3), PL([(410, 230), (440, 230), (440, 210), (482, 210)], RED, 3))
d.add(PL([(410, 380), (450, 380), (450, 290), (482, 290)], BLUE, 3), PL([(410, 410), (460, 410), (460, 330), (482, 330)], BLUE, 3))
d.add(PL([(285, 510), (285, 480), (440, 480), (440, 410), (482, 410)], ORANGE, 3), PL([(375, 510), (375, 495), (455, 495), (455, 470), (482, 470)], PURPLE, 3))
d.add(PL([(135, 410), (135, 640), (482, 640)], INK, 3))
d.add(L(700, 290, 700, 330, BLUE, 3), L(700, 410, 700, 470, PURPLE, 3) if False else "")
dsts = [(180, 60, "PMIC / charging IC", "power in, charges the cell", NAVY, 210), (290, 76, "CPU / PMIC  I2C bus", "reads %, health, cycles,\ngenuine or not", NAVY, 310), (400, 76, "ADC in PMIC /\ncharging IC", "reads temperature and\nbattery type (resistor)", "#5d4037", 440), (612, 56, "Ground", "", "#616161", 640)]
for y, h, t, s, c, ly in dsts:
    d.add(R(700, y, 200, h, c, "none", 12, 0, True), T(800, y + h / 2 + 5 - (t.count("\n")) * 9, t, 14.5, "#fff", 700, "middle", 1.25), T(920, y + h / 2 - (s.count("\n")) * 9 + 4, s, 13.5, MUTED, 400, lh=1.3))
d.add(PL([(700, 410), (700, 470), (530, 470)], PURPLE, 3) if False else "")
d.save()

# ---------- Figure 9.4 USB detection ----------
d = Fig("s9_fig4", "Figure 9.4  How a charger knows a phone is connected", "", 1200, 800)
d.add(T(40, 108, "A.  USB-C to USB-C", 21, NAVY, 800))
d.add(R(40, 130, 320, 300, TINT[GRAY], LINE[GRAY], 18, 2, True), T(200, 166, "CHARGER (source)", 16, NAVY, 800, "middle"))
d.add(R(840, 130, 320, 300, TINT[BLUE], LINE[BLUE], 18, 2, True), T(1000, 166, "PHONE (sink)", 16, NAVY, 800, "middle"))
d.add(T(70, 224, "5 V", 16, RED, 800), L(105, 218, 140, 218, RED, 3), C(144, 218, 5, "#fff", INK, 2), L(148, 216, 182, 200, INK, 3), C(186, 218, 5, "#fff", INK, 2), L(190, 218, 880, 218, RED, 3.5), T(520, 206, "VBUS", 15, RED, 800, "middle"), T(890, 224, "→ OVP → charging IC", 14, "#263238", 600))
d.add(T(165, 260, "VBUS switch\n(OFF until the\nphone is found)", 13, MUTED, 400, "middle"))
d.add(L(250, 218, 250, 300, PURPLE, 2.5), R(240, 300, 20, 56, "#fff", PURPLE, 2, 2.5), T(270, 334, "Rp", 14, PURPLE, 700), PL([(250, 356), (250, 390), (920, 390)], PURPLE, 3.5), T(560, 380, "CC (one wire in the cable)", 15, PURPLE, 800, "middle"))
d.add(L(920, 390, 990, 390, PURPLE, 3.5), res_sym(990, 390, 60, PURPLE), L(1050, 390, 1080, 390, PURPLE, 3), L(1080, 390, 1080, 396, PURPLE, 2.5), gnd(1080, 396, PURPLE), T(1020, 370, "Rd 5.1 kΩ", 14, PURPLE, 700, "middle"), T(890, 412, "CC1", 14, PURPLE, 800))
d.add(T(1000, 330, "", 1))
steps = ["The charger keeps VBUS OFF and watches the CC wire through its pull-up resistor Rp.", "The phone's Rd (5.1 kΩ to ground) pulls the CC voltage down. The charger now knows a phone is there.",
         "The charger switches VBUS on at 5 V. Rp also tells the phone how much current it may draw.", "Fast charging (USB PD): both sides talk over the CC wire and agree on 9 V, 12 V or more."]
for i, s in enumerate(steps): d.add(badge(60, 470 + i * 38, i + 1, PURPLE, 13, 13), T(84, 476 + i * 38, s, 15.5, "#263238"))
d.add(T(40, 642, "If the phone's Rd or the CC line is damaged, the charger never sees the phone and VBUS stays at 0 V.", 15.5, RED, 700))
d.add(L(40, 670, 1160, 670, "#e3e8ef", 2), T(40, 708, "B.  USB-A charger (micro-USB cable, or A-to-C cable)", 21, NAVY, 800))
for i, s in enumerate(["VBUS 5 V is always on. There is no CC check, so a phone with a damaged CC line may still charge from an A-to-C cable but not from C-to-C.",
                       "The phone checks D+ and D–: a wall charger shorts D+ to D– (up to about 1.5 A); a computer port gives about 0.5 A.", "Older fast charging (Quick Charge and similar) uses voltages on D+ and D– to ask for 9 V or 12 V."]):
    d.add(C(52, 742 + i * 34, 5, NAVY), T(66, 747 + i * 34, s, 15, "#263238"))
d.save()

# ---------- port steps ----------
d = Fig("s9_port_steps", "Replacing a soldered charging port: the key steps", "On many phones the port sits on a small sub-board: just swap the board, no soldering needed.", 1200, 420)
d.add(flow(40, 140, ["Protect", "Flux +\nheat", "Lift the\nold port", "Clean the\npads", "Fit the\nnew port", "Check +\ntest"], 160, 96, 32, [BLUE, ORANGE, RED, TEAL, BLUE, GREEN], 17,
           ["Kapton on nearby\nplastic and parts", "flux on all pins,\nhot air ≈ 350 °C", "when the solder\nmelts, lift straight up", "wick + flux,\nflat shiny pads", "align, solder the\nshell legs, then pins", "no bridges, diode\nmode VBUS, charge"], 14))
d.save()
render_all()

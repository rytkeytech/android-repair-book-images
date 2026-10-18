from sv import *
SC = "#1a237e"

def card(x, y, name, mode, mc, probes, good, bad, icon):
    o = [R(x, y, 360, 316, "#fff", "#dfe5ec", 18, 2, True), R(x, y, 360, 112, "#f5f7fa", "none", 18), R(x, y + 94, 360, 18, "#f5f7fa", "none", 0), G(icon, x + 180, y + 58)]
    o += [T(x + 20, y + 142, name, 19, NAVY, 800), R(x + 236, y + 122, 108, 28, TINT[mc], "none", 14), T(x + 290, y + 141, mode, 13.5, mc, 800, "middle")]
    o += [T(x + 20, y + 174, probes, 14, "#37474f", 400, lh=1.3)]
    yy = y + 218 if "\n" not in probes else y + 232
    o += [check(x + 30, yy - 5, 11), T(x + 50, yy, good, 14.5, GREEN, 700), cross(x + 30, yy + 34, 11), T(x + 50, yy + 39, bad, 14.5, RED, 700, lh=1.3)]
    return "".join(o)

def resistor(): return smd(-40, -12, 80, 24, "#212121") + T(0, 6, "103", 12, "#fff", 700, "middle")
def capacitor(): return smd(-40, -14, 80, 28, "#8d6e4a")
def coilic(): return R(-30, -30, 60, 60, "#455a64", "#263238", 6, 2) + C(0, 0, 18, "#607d8b") + T(0, 5, "2R2", 11, "#eceff1", 700, "middle")
def fuse(): return smd(-40, -12, 80, 24, "#6d4c41") + T(0, 5, "F", 12, "#fff", 800, "middle")
def diode(): return R(-36, -14, 72, 28, "#37474f", "none", 3) + R(18, -14, 8, 28, "#cfd8dc", "none", 0) + L(-70, 0, -36, 0, "#9e9e9e", 4) + L(36, 0, 70, 0, "#9e9e9e", 4) + T(-60, -14, "A", 12, SC, 800, "middle") + T(60, -14, "K", 12, SC, 800, "middle")
def tvs(): return diode() + T(0, 34, "TVS on VBUS / VBAT", 11, MUTED, 700, "middle")
def npn(): return R(-26, -22, 52, 36, "#212121", "none", 3) + R(-20, 14, 10, 12, "#cfd8dc", "none", 1) + R(10, 14, 10, 12, "#cfd8dc", "none", 1) + R(-5, -34, 10, 12, "#cfd8dc", "none", 1) + T(-15, 40, "B", 11, SC, 800, "middle") + T(15, 40, "E", 11, SC, 800, "middle") + T(0, -38, "C", 11, SC, 800, "middle")
def mosfet(): return R(-30, -24, 60, 40, "#212121", "none", 3) + R(-24, 16, 10, 12, "#cfd8dc", "none", 1) + R(14, 16, 10, 12, "#cfd8dc", "none", 1) + R(-5, -36, 10, 12, "#cfd8dc", "none", 1) + T(-19, 42, "G", 11, SC, 800, "middle") + T(19, 42, "S", 11, SC, 800, "middle") + T(0, -40, "D", 11, SC, 800, "middle")
def crystal(): return R(-42, -18, 84, 36, "url(#metal)", "#78909c", 6, 2) + T(0, 5, "32.768K", 11, "#37474f", 700, "middle")
def led(): return R(-24, -16, 48, 32, "#fffde7", "#f9a825", 4, 2) + C(0, 0, 9, "#fff59d") + L(18, -22, 30, -34, ORANGE, 2.5, arrow=True) + L(26, -14, 38, -26, ORANGE, 2.5, arrow=True)
def speaker(): return R(-56, -26, 112, 52, "#37474f", "#263238", 12, 2) + R(-46, -18, 92, 36, "#90a4ae", "none", 8) + R(-10, 26, 8, 10, "#d4af37", "none", 1) + R(6, 26, 8, 10, "#d4af37", "none", 1)
def mic(): return R(-26, -22, 52, 44, "#b0bec5", "#546e7a", 6, 2) + C(0, 0, 9, "#263238")
def motor(): return C(0, 0, 32, "url(#metal)", "#78909c", 2) + C(0, 0, 12, "#90a4ae") + L(22, 22, 40, 36, RED, 3) + L(14, 28, 30, 42, INK, 3)
def key(): return R(-50, -18, 100, 36, "#cfd8dc", "#90a4ae", 8, 2) + R(-20, -28, 40, 14, "url(#metal)", "#78909c", 5, 1.5) + L(-50, 0, -66, 0, "#d4af37", 4) + L(50, 0, 66, 0, "#d4af37", 4)
def ntc(): return smd(-30, -11, 60, 22, "#8d6e4a") + T(0, 34, "NTC (BTEMP)", 11, MUTED, 700, "middle")
def batt(): return R(-60, -26, 120, 52, "url(#batt)", "#0d1115", 8, 2) + R(-46, -16, 64, 32, ORANGE, "none", 4) + R(60, -10, 8, 20, "#37474f", "none", 2)
def flex(): return R(-70, -14, 140, 28, "#ff9800", "#e65100", 4, 1.5, False, .85) + R(40, -18, 34, 36, "#263238", "none", 3) + "".join(R(44 + i * 7, -12, 4, 24, "#d4af37", "none", 1) for i in range(4))
def ic(): return chip(-40, -26, 80, 52, "IC", 14)

PAGES = [("s3_test1", "How to test components (1 of 3): basic parts", "Battery removed. On the board, other parts can change the reading: compare with a good board.", [
    ("Resistor", "Ω mode", GREEN, "Probes on both ends.", "Close to its value", "0 Ω = shorted · OL = open", resistor()),
    ("Capacitor", "Diode mode", ORANGE, "Red on ground, black\non the line end.", "Same as the line (0.3–0.7)", "0.000 = shorted", capacitor()),
    ("Coil (inductor)", "Continuity", PURPLE, "Probes on both ends.", "Beeps, near 0 Ω", "No beep (OL) = open coil", coilic()),
    ("Fuse", "Continuity", PURPLE, "Probes on both ends.", "Beeps, near 0 Ω", "No beep (OL) = blown", fuse()),
    ("Diode", "Diode mode", ORANGE, "Red on A (anode),\nblack on K (cathode).", "0.2–0.7 one way, OL back", "0 both ways = shorted\nOL both ways = open", diode()),
    ("TVS / Zener diode", "Diode mode", ORANGE, "Test both ways, like a\nnormal diode.", "Reads one way only", "0 both ways = shorted\n(common after a bad charger)", tvs())]),
    ("s3_test2", "How to test components (2 of 3): switching and signal parts", "Battery removed. Remove the part from the board if the readings look strange.", [
    ("Transistor (NPN)", "Diode mode", ORANGE, "Red on B, black on E,\nthen black on C.", "About 0.6 both, OL reversed", "0 on any pair = shorted\n(PNP: swap the probes)", npn()),
    ("MOSFET", "Diode mode", ORANGE, "Red on S, black on D.\nThen gate to each pin.", "0.4–0.7 S→D, gate OL", "0 between D and S = shorted", mosfet()),
    ("Crystal", "Ω mode + eyes", BLUE, "Across both pins.\nLook for cracks or rust.", "OL (no connection)", "0 Ω = shorted. Best test:\nfit a good crystal", crystal()),
    ("LED", "Diode mode", ORANGE, "Red on anode,\nblack on cathode.", "Glows faintly one way", "Dark both ways = open\n(white LEDs may read OL)", led()),
    ("Speaker / earpiece", "Ω mode", GREEN, "Probes on the two pads.", "Speaker 6–8 Ω, ear 16–32 Ω", "OL = open coil · 0 = shorted", speaker()),
    ("Microphone", "DC volts", BLUE, "Phone on, recording.\nBlack on GND, red on VDD.", "About 1.8–2.2 V", "0 V = no power to the mic\nPower OK, no sound = bad mic", mic())]),
    ("s3_test3", "How to test components (3 of 3): other parts", "Check the simple parts first. They fail more often than chips.", [
    ("Vibration motor", "Ω mode / PSU", GREEN, "Probes on both pads, or\n2–3 V from the PSU.", "10–40 Ω, spins on 3 V", "OL = open · no spin = bad", motor()),
    ("Power / volume key", "Continuity", PURPLE, "Probes across the key.", "Beeps only when pressed", "Always beeps = stuck\nNever beeps = broken", key()),
    ("NTC thermistor", "Ω mode", GREEN, "Probes on both ends.", "About 10 kΩ at room temp", "0 or OL = faulty\n(value drops when warm)", ntc()),
    ("Battery", "DC volts", BLUE, "Red on +, black on –.", "3.7–4.4 V", "Below 3.0 V = very flat\nSwollen = replace", batt()),
    ("Flex / connector", "Continuity", PURPLE, "Pin to pin, end to end.\nLook at every pin.", "Every line beeps", "No beep = broken line\nBent or burnt pin = replace", flex()),
    ("IC (chip)", "Volts + diode", BLUE, "You cannot test it alone.\nCheck around it.", "Power, clock, enable OK", "All OK but no output =\nsuspect the chip (Ch. 15)", ic())]),
]
for name, title, sub, cards in PAGES:
    d = Fig(name, title, sub, 1200, 810)
    for i, c in enumerate(cards):
        d.add(card(40 + (i % 3) * 380, 110 + (i // 3) * 336, *c))
    d.save()
render_all()

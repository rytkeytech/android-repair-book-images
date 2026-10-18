from sv import *

# ---------- Figure 16.1 job card ----------
d = Fig("s16_fig1", "Figure 16.1  A simple repair job card (example layout)", "Print it, or keep the same fields in your shop software.", 1200, 1240)
X, W = 160, 880
d.add(R(X, 110, W, 1100, "#fff", "#cfd8dc", 16, 2, True), R(X, 110, W, 100, NAVY, "none", 16), R(X, 190, W, 20, NAVY, "none", 0))
d.add(T(X + 36, 156, "YOUR SHOP NAME", 26, "#fff", 800), T(X + 36, 186, "Phone repair  ·  Address  ·  Phone number", 14, "#c5cfe0"), T(X + W - 36, 156, "JOB No. 0001", 22, "#ffb74d", 800, "end"), T(X + W - 36, 186, "Date in: ____ / ____ / ______", 14, "#c5cfe0", 400, "end"))
def section(y, t): return R(X, y, W, 38, TINT[NAVY], "none", 0) + T(X + 30, y + 25, t, 15, NAVY, 800)
def field(x, y, lab, w): return T(x, y, lab, 15, "#37474f", 600) + L(x + 8 * len(lab) + 24, y + 4, x + w, y + 4, "#b0bec5", 1.5)
y = 230
d.add(section(y, "CUSTOMER"), field(X + 30, y + 80, "Name:", 470), field(X + 520, y + 80, "Phone:", 330))
y = 340
d.add(section(y, "PHONE"), field(X + 30, y + 80, "Brand / model:", 470), field(X + 520, y + 80, "Colour:", 330), field(X + 30, y + 120, "IMEI / serial:", 470), field(X + 520, y + 120, "Passcode given?  Y / N", 330))
d.add(T(X + 30, y + 168, "Condition on arrival:", 15, NAVY, 800))
for i, t in enumerate(["Screen cracked", "Back cracked", "Bent frame", "Water signs", "Powers on", "Missing parts"]):
    cx, cy = X + 30 + (i % 3) * 280, y + 200 + (i // 3) * 38
    d.add(R(cx, cy - 14, 18, 18, "#fff", "#78909c", 3, 2), T(cx + 30, cy, t, 15, "#37474f"))
d.add(T(X + 30, y + 296, "Accessories left:   ☐ SIM    ☐ Memory card    ☐ Case    ☐ Charger", 15, "#37474f"))
y = 680
d.add(section(y, "FAULT AND REPAIR"))
for i, t in enumerate(["Customer's complaint:", "Diagnosis / readings:", "Work done / parts used:"]):
    yy = y + 80 + i * 76; d.add(field(X + 30, yy, t, 820), L(X + 30, yy + 36, X + 850, yy + 36, "#b0bec5", 1.5))
y = 940
d.add(section(y, "PRICE, PAYMENT AND WARRANTY"), field(X + 30, y + 80, "Quoted price:", 400), field(X + 470, y + 80, "Deposit paid:", 380), field(X + 30, y + 120, "Balance:", 400), field(X + 470, y + 120, "Warranty (days):", 380))
d.add(T(X + 30, y + 168, "Terms: data backup is the customer's responsibility. Liquid-damaged and previously repaired phones carry limited or no warranty.", 12.5, MUTED), T(X + 30, y + 186, "Phones not collected within 60 days may be disposed of. The warranty covers the part and work done only.", 12.5, MUTED))
d.add(field(X + 30, y + 236, "Customer signature:", 400), field(X + 470, y + 236, "Technician:", 380))
d.save()

# ---------- pricing ----------
d = Fig("s16_pricing", "What goes into a repair price", "Charging only for the part means working for free. Write your price list down and keep it the same for everyone.", 1200, 400)
parts = [("Part cost", 45, BLUE), ("Your time and skill", 25, GREEN), ("Tools, power, rent", 12, GRAY), ("Warranty risk", 8, ORANGE), ("Profit", 10, PURPLE)]
d.add(T(60, 140, "Example: one screen replacement (example shares only)", 17, NAVY, 800))
x = 60
for i, (n, v, c) in enumerate(parts):
    w = v * 10.8
    d.add(R(x, 170, w, 90, c, "#fff", 0, 3), T(x + w / 2, 224, f"{v}%", 22, "#fff", 800, "middle"))
    ly = 300 + (i % 2) * 46
    d.add(L(x + w / 2, 262, x + w / 2, ly - 18, c, 2), T(x + w / 2, ly, n, 16, c, 800, "middle"))
    x += w
d.save()

# ---------- workflow ----------
d = Fig("s16_workflow", "A repair job from start to finish", "Write everything down at each step. Good records settle disputes before they start.", 1200, 420)
d.add(flow(40, 140, ["Receive", "Job card", "Diagnose", "Repair", "Test + QC", "Deliver"], 160, 96, 32, [NAVY, BLUE, TEAL, ORANGE, PURPLE, GREEN], 17,
           ["check, test,\nnote damage", "customer signs,\nreceives a ticket", "find the fault,\ncall with a price", "only after the\ncustomer agrees", "all functions,\nnot just the fault", "show it working,\nexplain warranty"], 14))
d.save()

# ---------- privacy ----------
d = Fig("s16_privacy", "Customer data: do and don't", "In Ghana, the Data Protection Act 2012 (Act 843) protects personal data. Trust is your best advert.", 1200, 520)
for i, (t, c, items, mk) in enumerate([("DO", GREEN, ["Ask the customer to back up first", "Ask for the PIN only if testing needs it", "Keep screens out of other customers' view", "Return the phone as you received it"], check),
                                      ("DON'T", RED, ["Open photos, chats or files", "Copy or keep any customer data", "Leave unlocked phones on the counter", "Share a customer's number or details"], cross)]):
    x = 40 + i * 570
    d.add(R(x, 110, 550, 360, TINT[c], LINE[c], 18, 2, True), T(x + 275, 160, t, 26, c, 800, "middle"))
    for k, s in enumerate(items): d.add(mk(x + 50, 220 + k * 62, 15), T(x + 80, 227 + k * 62, s, 17, "#263238"))
d.save()

# ---------- stolen ----------
d = Fig("s16_stolen", "Signs a phone may be stolen", "Record the customer's ID and the IMEI on the job card. Decline jobs that remove locks without proof of ownership.", 1200, 420)
signs = [("No charger, box\nor proof of purchase", ORANGE), ("Locked to an account\nthe customer can't open", RED), ("Asks you to remove\nthe account lock", RED), ("Asks to change\nor 'flash' the IMEI", RED), ("Very cheap,\nseller in a hurry", ORANGE)]
for i, (t, c) in enumerate(signs):
    x = 40 + i * 228
    d.add(R(x, 120, 208, 230, "#fff", LINE[c], 18, 2, True), warn(x + 104, 186, 52, "#f9a825" if c == ORANGE else "#ef5350"), T(x + 104, 268, t, 16, c, 800, "middle", 1.3))
d.save()

# ---------- warranty ----------
d = Fig("s16_warranty", "What your warranty covers", "Write the warranty terms on the receipt and mark the parts you fitted.", 1200, 460)
for i, (t, c, items, mk) in enumerate([("COVERED", GREEN, ["The part you replaced", "The fault you repaired", "For the stated period (e.g. 30 days)"], check), ("NOT COVERED", RED, ["New drops, cracks or liquid", "Other faults you did not repair", "Phones opened by someone else"], cross)]):
    x = 40 + i * 570
    d.add(R(x, 110, 550, 300, TINT[c], LINE[c], 18, 2, True), T(x + 275, 160, t, 24, c, 800, "middle"))
    for k, s in enumerate(items): d.add(mk(x + 50, 222 + k * 60, 15), T(x + 80, 229 + k * 60, s, 17, "#263238"))
d.save()

# ---------- Figure 17.1 fault finder ----------
d = Fig("s17_fig1", "Figure 17.1  Quick fault finder", "Start from the symptom, do the first checks, then go to the chapter.", 1200, 980)
rows = [("No power at all", "Battery voltage · charge 30 min · PSU current before and after the power key", "7, 8", RED), ("High current on PSU", "Short on VBAT or a PMIC line · injection, thermal camera, rosin", "6", RED),
        ("Boot loop / stuck on logo", "PC detection · flash firmware · storage rails · battery and NTC", "7, 8", PURPLE), ("Not charging", "Cable, charger, port · VBUS → fuse → OVP → charging IC · CC lines", "9", ORANGE),
        ("Charges A-to-C but not C-to-C", "CC1 / CC2 lines and their 5.1 kΩ resistors", "9", ORANGE), ("Wrong % / unknown battery", "Battery · SDA / SCL · NTC and ID lines", "9", ORANGE),
        ("Black screen, phone rings", "Test screen · connector · display rails", "10", BLUE), ("Dark picture (torch shows it)", "LCD backlight: LED+ voltage, coil, diode, capacitor", "10", BLUE), ("Touch not working", "Screen / digitiser · connector · touch IC lines", "10", BLUE),
        ("No sound / caller can't hear", "Speaker or mic test · meshes · amplifier · codec", "11", TEAL), ("No SIM / no service", "SIM swap · reader pins · antenna contacts · coax · PA", "12", PURPLE), ("Wi-Fi / BT greyed out", "Wi-Fi chip power and clock · cracked joints", "12", PURPLE),
        ("Liquid damaged", "Disconnect battery · clean · dry · check shorts · PSU", "13", TEAL), ("Fault returns after a drop", "Cracked joints under chips · reflow or reball", "14, 15", GRAY)]
d.add(R(40, 110, 1120, 52, NAVY, "none", 12), T(64, 143, "Symptom", 16, "#fff", 800), T(420, 143, "First checks", 16, "#fff", 800), T(1130, 143, "Chapter", 16, "#fff", 800, "end"))
for i, (a, b, ch, c) in enumerate(rows):
    y = 170 + i * 56
    d.add(R(40, y, 1120, 50, "#fff" if i % 2 else "#f5f7fa", "none", 8), R(40, y, 6, 50, c, "none", 3), T(64, y + 31, a, 15.5, NAVY, 800), T(420, y + 31, b, 14.5, "#263238"), R(1060, y + 10, 84, 30, TINT[ORANGE], "none", 15), T(1102, y + 31, ch, 15, ORANGE, 800, "middle"))
d.save()

# ---------- meter guide ----------
d = Fig("s17_meter_guide", "Multimeter quick guide", "", 1200, 560)
rows = [("Is the line shorted?", "Diode mode", "battery OFF, red probe on GND", "near 0 = short", ORANGE), ("Is a voltage present?", "DC volts", "phone ON, black probe on GND", "compare with schematic", BLUE),
        ("Is the fuse or coil OK?", "Continuity / Ω", "battery OFF", "beep, near 0 Ω = OK", PURPLE), ("Is the speaker OK?", "Resistance Ω", "speaker out of circuit", "about 8 Ω", GREEN), ("Is the battery OK?", "DC volts", "on the battery pins", "3.7 – 4.4 V", TEAL)]
for j, h in enumerate(["Question", "Mode", "Setup", "Good / bad"]): d.add(T([64, 380, 590, 900][j], 132, h, 16, NAVY, 800))
for i, (a, b, c_, e, col) in enumerate(rows):
    y = 150 + i * 76
    d.add(R(40, y, 1120, 64, "#fff", "#dfe5ec", 14, 2, True), R(40, y, 8, 64, col, "none", 4), T(64, y + 39, a, 17, NAVY, 800), R(370, y + 14, 180, 36, TINT[col], "none", 18), T(460, y + 38, b, 15.5, col, 800, "middle"), T(590, y + 39, c_, 15.5, "#263238"), T(900, y + 39, e, 15.5, "#263238", 700))
d.save()

# ---------- PSU patterns ----------
import math
def pts(kind, x0, y0, w, h, n=120):
    o = []
    for i in range(n + 1):
        t = i / n
        v = {"zero": 0, "jump": (.5 if .15 < t < .4 else 0), "stuck": (0 if t < .1 else .45), "high": (0 if t < .06 else .92), "loop": (lambda p: 0 if p < .1 else .35 + .3 * abs(math.sin(p * 25)))((t % .34) / .34), "normal": (0 if t < .06 else min(.8, .2 + t) * (0.85 + .15 * math.sin(t * 40)))}[kind]
        o.append((x0 + t * w, y0 + h - v * h))
    return "M" + " L".join(f"{a:.1f} {b:.1f}" for a, b in o)
d = Fig("s17_psu_patterns", "DC power supply patterns at a glance", "Press power and watch the ammeter. Chapter 7 explains each pattern in detail.", 1200, 680)
pats = [("0 mA, nothing", "zero", "power key, battery line,\nPMIC not starting", RED), ("Jumps, then 0", "jump", "PMIC output short,\nCPU not running", RED), ("Stuck at one value", "stuck", "CPU, memory or\nstorage fault", ORANGE),
        ("High current at once", "high", "short on VBAT\nor a main line", RED), ("Climbs, falls, repeats", "loop", "boot loop: software,\nstorage, battery", PURPLE), ("Climbs and settles", "normal", "normal boot", GREEN)]
for i, (t, k, c_, col) in enumerate(pats):
    x = 40 + (i % 3) * 380; y = 110 + (i // 3) * 280
    d.add(R(x, y, 360, 260, "#fff", LINE[col], 16, 2, True), T(x + 24, y + 38, t, 17.5, col, 800), R(x + 24, y + 56, 312, 110, "#f7f9fb", "none", 8), L(x + 34, y + 156, x + 326, y + 156, "#90a4ae", 1.5), L(x + 34, y + 64, x + 34, y + 156, "#90a4ae", 1.5))
    d.add(P(pts(k, x + 34, y + 66, 292, 88), stroke=col, sw=3), T(x + 24, y + 200, c_, 15, "#263238"))
d.save()

# ---------- pins ----------
d = Fig("s17_pins", "Battery connector and charging port pins (common layout)", "Pin order changes between models. Check the schematic before you measure.", 1200, 560)
d.add(R(40, 110, 540, 400, "#fff", "#dfe5ec", 18, 2, True), T(70, 150, "Battery connector", 20, NAVY, 800))
d.add(R(80, 200, 460, 120, "#263238", "none", 12))
for i, (n, c) in enumerate([("VBAT +", RED), ("BSI / ID", PURPLE), ("BTEMP / NTC", ORANGE), ("SDA", BLUE), ("SCL", BLUE), ("GND", INK)]):
    x = 100 + i * 74
    d.add(R(x, 220, 52, 80, "url(#copper)", "#8d6e1a", 6, 1.5), T(x + 26, 350, n.split(" / ")[0], 14, c, 800, "middle"))
    if " / " in n: d.add(T(x + 26, 368, n.split(" / ")[1], 12, c, 700, "middle"))
d.add(T(70, 430, "VBAT: 3.7–4.4 V  ·  NTC: about 10 kΩ to GND", 15, "#37474f"), T(70, 458, "SDA / SCL: battery data (fuel gauge)", 15, "#37474f"))
d.add(R(620, 110, 540, 400, "#fff", "#dfe5ec", 18, 2, True), T(650, 150, "USB-C port (main pins)", 20, NAVY, 800))
d.add(R(660, 200, 460, 130, "url(#metal)", "#607d8b", 65, 2), R(700, 252, 380, 26, "#37474f", "none", 13))
for i, (n, c) in enumerate([("GND", INK), ("VBUS", RED), ("CC1", PURPLE), ("D+", BLUE), ("D–", BLUE), ("SBU", GRAY), ("VBUS", RED), ("GND", INK)]):
    x = 716 + i * 46
    d.add(R(x, 226, 26, 22, "url(#copper)", "none", 3), T(x + 13, 360, n, 13, c, 800, "middle"))
d.add(T(650, 430, "Micro-USB: VBUS, D–, D+, ID, GND", 15, "#37474f"), T(650, 458, "USB-C also has CC2 on the other row", 15, "#37474f"))
d.save()
render_all()

from sv import *

def speaker(x, y, s=1, c="#455a64"):
    return G([R(0, -14, 22, 28, "#90a4ae", "#546e7a", 2, 1.5), P("M22 -14 L50 -36 L50 36 L22 14 Z", fill="#cfd8dc", stroke="#546e7a", sw=1.5)], x, y, s)
def mic(x, y, s=1): return G([R(-22, -18, 44, 36, "#b0bec5", "#546e7a", 4, 1.5), C(0, 0, 8, "#263238")], x, y, s)

# ---------- Figure 10.1 display connections ----------
d = Fig("s10_fig1", "Figure 10.1  What the display needs from the motherboard", "Points 1–4: check these first on a no-display phone. Rail names and voltages differ by model.", 1200, 710)
d.add(box(40, 140, 200, 200, "CPU", NAVY, 22), box(40, 430, 200, 200, "PMIC /\ndisplay\npower IC", "#37474f", 17))
d.add(R(560, 140, 56, 540, "#cfd8dc", "#90a4ae", 8, 2), T(588, 130, "Display connector", 15, NAVY, 800, "middle"))
for i in range(18): d.add(R(572, 158 + i * 28, 32, 10, "#d4af37", "none", 2))
lines = [(180, "MIPI DSI data lanes (picture)", BLUE, 1), (225, "RESET, TE (timing)", BLUE, None), (270, "I2C (touch), touch interrupt", PURPLE, None), (470, "IOVCC 1.8 V,  VCI 2.8–3.3 V", RED, 2), (530, "LCD: VSP +5.5 V / VSN –5.5 V", RED, 3), (600, "LCD only: LED+ / LED– (backlight)", ORANGE, 4)]
for y, t, c, n in lines:
    d.add(L(240, y, 560, y, c, 3.5), T(256, y - 10, t, 13.5, c, 700))
    if n: d.add(badge(530, y, n))
d.add(T(256, 552, "OLED: ELVDD / ELVSS", 13.5, RED, 700))
d.add(R(650, 120, 510, 250, "#fff", LINE[BLUE], 18, 2, True), R(650, 120, 510, 52, TINT[BLUE], "none", 18), R(650, 154, 510, 18, TINT[BLUE], "none", 0), T(674, 155, "LCD (IPS / TFT)", 19, BLUE, 800))
for i, t in enumerate(["Liquid crystal does not make light", "LED backlight behind the panel", "Backlight needs a boost circuit (Figure 10.2)", "No backlight: dark picture, faint under a torch"]): d.add(T(676, 206 + i * 30, ("•  " if not t.startswith("    ") else "") + t.strip() if not t.startswith("    ") else "    " + t.strip(), 15.5, "#263238"))
d.add(R(650, 400, 510, 260, "#fff", LINE[PURPLE], 18, 2, True), R(650, 400, 510, 52, TINT[PURPLE], "none", 18), R(650, 434, 510, 18, TINT[PURPLE], "none", 0), T(674, 435, "OLED / AMOLED", 19, PURPLE, 800))
for i, t in enumerate(["Each pixel makes its own light", "No backlight circuit", "Needs ELVDD and ELVSS rails", "Damage: black spots, green or pink lines", "Usually replaced as a complete unit"]): d.add(T(676, 490 + i * 32, "•  " + t, 15.5, "#263238"))
d.save()

# ---------- Figure 10.2 backlight boost ----------
d = Fig("s10_fig2", "Figure 10.2  LCD backlight boost circuit (typical)", "The driver switches the coil on and off very fast to boost about 3.8 V up to 15–25 V for the LEDs.", 1200, 720)
SC = "#1a237e"
d.add(R(40, 110, 1120, 360, "#fbfcfe", "#c5cfe0", 16, 2, True))
d.add(T(70, 190, "VBAT\n3.8 V", 17, RED, 800), L(140, 196, 210, 196, SC, 3), coil_sym(210, 196, 5, SC, "L (boost coil)"), L(300, 196, 420, 196, SC, 3))
d.add(P("M420 182 L446 196 L420 210 Z", fill=SC, stroke=SC, sw=1.5), L(446, 182, 446, 210, SC, 3.5), T(433, 168, "D (Schottky)", 14, SC, 600, "middle"), L(446, 196, 620, 196, SC, 3), T(470, 184, "LED+ (15–25 V)", 14, ORANGE, 800))
d.add(C(360, 196, 5, SC), L(360, 196, 360, 290, SC, 3), T(368, 230, "SW", 12, MUTED, 700))
d.add(C(540, 196, 5, SC), L(540, 196, 540, 236, SC, 3), L(522, 236, 558, 236, SC, 3.5), L(522, 246, 558, 246, SC, 3.5), L(540, 246, 540, 270, SC, 3), gnd(540, 270, SC), T(566, 248, "C out", 13, SC, 600))
for i in range(5):
    x = 620 + i * 90
    d.add(P(f"M{x} 182 L{x+30} 196 L{x} 210 Z", fill="#fff59d", stroke=SC, sw=2), L(x + 30, 182, x + 30, 210, SC, 3), L(x + 30, 196, x + 90, 196, SC, 3), L(x + 12, 170, x + 26, 156, ORANGE, 2.5, arrow=True))
d.add(T(820, 140, "Backlight LEDs in series (inside the LCD)", 14, MUTED, 600, "middle"), PL([(1070, 196), (1110, 196), (1110, 340), (720, 340)], SC, 3), T(900, 330, "LED– (feedback to the IC)", 14, BLUE, 800, "middle"))
d.add(R(260, 290, 220, 130, NAVY, "none", 14, 0, True), T(370, 344, "Backlight driver IC", 16, "#fff", 800, "middle"), T(370, 368, "(or PMIC)", 14, "#c5cfe0", 400, "middle"))
d.add(PL([(180, 196), (180, 330), (260, 330)], SC, 3), PL([(480, 340), (720, 340)], SC, 3), C(800, 340, 5, SC), L(800, 340, 800, 370, SC, 3), R(790, 370, 20, 50, "#fff", SC, 2, 2.5), L(800, 420, 800, 430, SC, 3), gnd(800, 430, SC), T(822, 400, "R sense", 13, SC, 600))
d.add(L(150, 400, 260, 400, PURPLE, 3), T(70, 392, "EN / PWM", 13, PURPLE, 700), T(70, 410, "from CPU", 12, PURPLE, 600))
for n, (x, y) in enumerate([(190, 172), (330, 262), (500, 226), (1110, 300)], 1): d.add(badge(x, y, n))
notes = ["VBAT into the coil: battery voltage. If missing, check the fuse or path from VBAT.", "Coil: check continuity (should beep). An open coil means no backlight.", "LED+: about 15–25 V with the screen on. In diode mode it should not read 0 (shorted capacitor or diode).", "LED–: low voltage with the screen on. LED+ high but no light? The LCD's LEDs or the connector are faulty."]
for i, t in enumerate(notes): d.add(badge(60, 510 + i * 40, i + 1, ORANGE, 13, 13), T(86, 516 + i * 40, t, 15.5, "#263238"))
d.add(T(40, 690, "Also check the Schottky diode in diode mode (one way only) and the output capacitor for a short.", 15, MUTED))
d.save()

# ---------- torch test ----------
d = Fig("s10_torch_test", "Black screen? The torch test", "Shine a bright torch at an angle onto the screen while the phone is on.", 1200, 600)
cases = [("Image visible under torch light", "Display works. The backlight is dead:\nLED fuse, coil, boost IC.", ORANGE, "ghost"), ("Nothing visible, phone rings", "Screen or connector fault, or no\ndisplay power. Try a good screen.", RED, "dark"), ("Image visible normally", "Screen is fine. Look for touch\nor other faults.", GREEN, "ok")]
for i, (t, r, c, k) in enumerate(cases):
    x = 40 + i * 380
    d.add(R(x, 110, 360, 440, "#fff", LINE[c], 18, 2, True), R(x, 110, 360, 260, TINT[c], "none", 18), R(x, 340, 360, 30, TINT[c], "none", 0))
    d.add(phone(x + 120, 130, 120, 220, "#4fc3f7" if k == "ok" else "#0b1118"))
    if k == "ghost":
        for j in range(4): d.add(R(x + 140, 175 + j * 32, 80, 14, "#37474f", "none", 4))
        d.add(P(f"M{x+300} 300 L{x+318} 318 L{x+222} 230 L{x+210} 250 Z", fill="#fff59d", stroke="none", op=.85), R(x + 296, 296, 46, 22, "#455a64", "none", 4) if False else G([R(0, -11, 50, 22, "#455a64", "none", 6), R(46, -14, 10, 28, "#90a4ae", "none", 3)], x + 300, 306, 1, 40))
    if k == "ok":
        for j in range(4): d.add(R(x + 140, 175 + j * 32, 80, 14, "#fff", "none", 4))
    if k == "dark": d.add(P(f"M{x+262} 150 q12 14 0 28 M{x+274} 142 q20 22 0 44", stroke=c, sw=3), T(x + 300, 172, "ring", 13, c, 700))
    d.add(T(x + 24, 408, t, 18, c, 800), T(x + 24, 442, r, 15.5, "#263238"))
d.save()

# ---------- connector ----------
d = Fig("s10_connector", "Inspect the screen connector: good and damaged", "Always disconnect the battery before plugging or unplugging a screen. A live plug-in can burn the backlight line.", 1200, 520)
for i, (t, c) in enumerate([("GOOD: straight, clean, shiny pins", GREEN), ("BAD: burnt, bent, corroded or missing pins", RED)]):
    x = 40 + i * 570
    d.add(R(x, 110, 550, 360, "#fff", LINE[c], 18, 2, True), R(x + 30, 170, 490, 170, "#263238", "#111", 12, 2), R(x + 60, 220, 430, 70, "#37474f", "none", 8))
    for k in range(20):
        px = x + 72 + k * 21; col, hh, rot = "#d4af37", 46, 0
        if i == 1 and k in (6, 7): col = "#3e2723"
        if i == 1 and k == 12: col = "#80cbc4"
        if i == 1 and k == 15: hh = 24
        if i == 1 and k == 3: rot = 20
        d.add(f'<rect x="{px}" y="232" width="10" height="{hh}" rx="2" fill="{col}" transform="rotate({rot} {px+5} 255)"/>')
    if i == 1:
        d.add(C(x + 222, 255, 32, "none", "#ff7043", 3), T(x + 222, 160, "burnt", 15, RED, 800, "middle"), T(x + 330, 160, "corroded", 15, TEAL, 800, "middle"), T(x + 140, 160, "bent", 15, ORANGE, 800, "middle"), T(x + 400, 368, "short pin", 15, PURPLE, 800, "middle"))
        d.add(L(x + 140, 166, x + 140, 226, ORANGE, 2), L(x + 330, 166, x + 330, 226, TEAL, 2), L(x + 400, 352, x + 393, 284, PURPLE, 2))
    d.add((check if c == GREEN else cross)(x + 44, 420, 16), T(x + 70, 427, t, 18, c, 800))
d.save()

# ---------- display rails ----------
d = Fig("s10_display_rails", "Display power lines to check at the screen connector", "Typical values; your phone may differ. A missing line points to its own coil, capacitor or power IC.", 1200, 540)
d.add(box(40, 150, 220, 300, "PMIC /\ndisplay\npower IC", NAVY, 18))
rails = [("VDD_1V8 (logic)", "1.8 V", BLUE), ("VCI / AVDD", "2.8 – 3.3 V", TEAL), ("AVDD+ / AVEE–  (LCD bias)", "+5.5 / –5.5 V", PURPLE), ("Backlight LED+  (LCD)", "15 – 25 V", ORANGE), ("ELVDD / ELVSS  (OLED)", "+4.6 / –2 to –5 V", RED)]
for i, (n, v, c) in enumerate(rails):
    y = 180 + i * 60
    d.add(L(260, y, 900, y, c, 4), T(290, y - 12, n, 16, c, 800), R(690, y - 20, 170, 40, TINT[c], LINE[c], 20, 2), T(775, y + 6, v, 16, c, 800, "middle"))
d.add(R(900, 140, 70, 320, "#cfd8dc", "#90a4ae", 8, 2), *[R(914, 156 + k * 30, 42, 10, "#d4af37", "none", 2) for k in range(10)], T(935, 490, "screen\nconnector", 14, NAVY, 700, "middle"))
d.add(phone(1010, 180, 130, 250, "#0b1118"))
d.save()

# ---------- screen steps ----------
d = Fig("s10_screen_steps", "Replacing a screen the right way", "Testing the new screen before gluing saves you from sealing a faulty screen into the phone.", 1200, 420)
d.add(flow(40, 140, ["Test the new\nscreen first", "Heat and\nopen", "Battery\noff", "Clean the\nframe", "Fit +\nglue", "Final\ntest"], 160, 96, 32, [GREEN, BLUE, RED, BLUE, BLUE, GREEN], 17,
           ["plug in loosely,\nbattery connected last", "80–100 °C, slow\npry, no metal tools", "always before\nunplugging the screen", "remove old glue\nand dust", "B-7000 or tape,\nclamp evenly", "touch, display,\nsensors, camera"], 14))
d.save()

# ---------- Figure 11.1 audio system ----------
d = Fig("s11_fig1", "Figure 11.1  The audio system of a typical phone", "Many phones play sound through the earpiece and loudspeaker together for stereo.", 1200, 780)
d.add(box(40, 330, 180, 220, "CPU", NAVY, 22), box(330, 320, 230, 240, "Audio codec\n(often inside\nthe PMIC)", "#37474f", 17))
d.add(L(220, 400, 330, 400, BLUE, 3), T(232, 390, "digital audio", 13, BLUE, 700), L(220, 480, 330, 480, BLUE, 3), T(232, 470, "control", 13, BLUE, 700))
d.add(PL([(200, 330), (200, 170), (690, 170)], BLUE, 3), T(440, 160, "I2S audio + I2C control", 13, BLUE, 700, "middle"))
d.add(box(690, 120, 220, 110, "Speaker amp\n(smart PA)", "#5d4037", 16), PL([(660, 100), (660, 210), (690, 210)], RED, 3), T(668, 112, "VBAT", 13, RED, 800))
d.add(L(910, 150, 1000, 150, ORANGE, 3), L(910, 200, 1000, 200, ORANGE, 3), T(955, 140, "SPK+ / SPK–", 12, ORANGE, 800, "middle"), speaker(1000, 175, 1.3), T(1050, 245, "Loudspeaker 6–8 Ω", 14, NAVY, 700, "middle"))
d.add(L(560, 360, 1000, 360, ORANGE, 3), L(560, 400, 1000, 400, ORANGE, 3), T(780, 350, "EAR+ / EAR–", 12, ORANGE, 800, "middle"), speaker(1000, 380, 1.1), T(1040, 440, "Earpiece 16–32 Ω", 14, NAVY, 700, "middle"))
d.add(L(560, 500, 1000, 500, GREEN, 3), T(780, 490, "MIC bias / VDD 1.8 V, CLK, DATA", 12, GREEN, 800, "middle"), mic(1030, 500), T(1030, 540, "Main mic (bottom)", 14, NAVY, 700, "middle"))
d.add(PL([(560, 540), (760, 540), (760, 620), (1000, 620)], GREEN, 3), mic(1030, 620), T(1030, 660, "Second mic (top / back)", 14, NAVY, 700, "middle"))
d.add(PL([(445, 560), (445, 700), (690, 700)], PURPLE, 3), T(560, 690, "L, R, MIC, detect", 12, PURPLE, 800, "middle"), box(690, 665, 200, 70, "Headphone jack", PURPLE, 15))
for n, (x, y) in enumerate([(1130, 175), (1130, 380), (1078, 500), (1078, 620), (920, 700)], 1): d.add(badge(x, y, n))
d.add(T(40, 610, "1 Loudspeaker\n2 Earpiece\n3 Main microphone\n4 Second microphone\n5 Headphone jack", 14.5, "#37474f", 600, lh=1.5))
d.save()

# ---------- Figure 11.2 audio testing ----------
d = Fig("s11_fig2", "Figure 11.2  Testing speakers and microphones with the multimeter", "", 1200, 640)
d.add(R(40, 100, 550, 500, "#fff", LINE[BLUE], 18, 2, True), T(66, 140, "A.  Speaker or earpiece: resistance (Ω)", 18, BLUE, 800))
d.add(multimeter(70, 170, "7.8", "Ω", 1.0, "Ω"), speaker(330, 260, 2.6), R(355, 300, 16, 26, "#d4af37", "none", 2), R(395, 300, 16, 26, "#d4af37", "none", 2))
d.add(P("M108 375 C108 420 363 430 363 326", stroke=RED, sw=3.5), P("M145 375 C145 440 403 450 403 326", stroke=INK, sw=3.5))
for i, t in enumerate(["Loudspeaker: about 6–8 Ω", "Earpiece: about 16–32 Ω", "OL = open coil (replace)  ·  0 Ω = shorted", "A faint click as you touch the probes is a good sign."]): d.add(T(66, 490 + i * 26, t, 15, "#263238"))
d.add(R(610, 100, 550, 500, "#fff", LINE[GREEN], 18, 2, True), T(636, 140, "B.  Microphone: power (V DC) while recording", 18, GREEN, 800))
d.add(multimeter(640, 170, "1.80", "V DC", 1.0), R(900, 220, 180, 120, "#b0bec5", "#546e7a", 8, 2), C(990, 270, 14, "#263238"))
for k, (n, c) in enumerate([("VDD", RED), ("GND", INK), ("CLK", BLUE), ("DATA", GREEN)]): d.add(R(915 + k * 42, 340, 22, 24, "#d4af37", "none", 2), T(926 + k * 42, 334, n[0], 11, c, 800, "middle"))
d.add(T(990, 208, "pins: VDD · GND · CLK · DATA", 13, MUTED, 700, "middle"))
d.add(P("M678 375 C678 440 926 440 926 364", stroke=RED, sw=3.5), P("M715 375 C715 420 968 420 968 364", stroke=INK, sw=3.5))
for i, t in enumerate(["Digital mic: VDD about 1.8 V while the mic is in use", "(make a voice recording or call). CLK only runs then.", "Analog mic: bias about 1.8–2.8 V on MIC+.", "No voltage? Follow the line back to the codec."]): d.add(T(636, 490 + i * 26, t, 15, "#263238"))
d.save()

# ---------- sound paths ----------
d = Fig("s11_sound_paths", "Where is the sound fault? Test each path on its own", "If one path fails and the others work, the fault is in that path only. If all fail, think codec, software or liquid.", 1200, 560)
tests = [("Loudspeaker", "play music or a ringtone", "speaker, amplifier, contacts", ORANGE), ("Earpiece", "make a call, hold to your ear", "earpiece, mesh, codec", ORANGE), ("Main mic", "voice recorder (bottom mic)", "mic, port hole, sub-board", GREEN),
         ("Top / noise mic", "record a video", "second mic, codec", GREEN), ("Headphones / BT", "plug in or pair a headset", "jack, codec, software", PURPLE)]
d.add(T(70, 132, "Path", 16, NAVY, 800), T(380, 132, "How to test", 16, NAVY, 800), T(760, 132, "If it fails, look at", 16, NAVY, 800))
for i, (a, b, c_, col) in enumerate(tests):
    y = 150 + i * 72
    d.add(R(40, y, 1120, 60, "#fff", "#dfe5ec", 12, 2, True), R(40, y, 8, 60, col, "none", 4), T(70, y + 37, a, 18, col, 800), T(380, y + 37, b, 16, "#263238"), T(760, y + 37, c_, 16, RED, 600))
d.save()

# ---------- mic types ----------
d = Fig("s11_mic_types", "Two kinds of microphone", "", 1200, 500)
for i, (t, x, pins, n_) in enumerate([("ANALOG MIC (2 pins)", 40, [("MIC_P", RED), ("MIC_N / GND", INK)], "Bias voltage about 1.8–2.2 V on\nMIC_P while recording."),
                                     ("DIGITAL MEMS MIC (4–5 pins)", 610, [("VDD 1.8 V", RED), ("CLK", BLUE), ("DATA", GREEN), ("GND", INK)], "Needs power AND a clock.\nCheck VDD and CLK while recording.")]):
    c = BLUE if i == 0 else PURPLE
    d.add(R(x, 100, 550, 360, "#fff", LINE[c], 18, 2, True), T(x + 275, 144, t, 20, c, 800, "middle"))
    d.add(R(x + 60, 200, 130, 110, "#b0bec5", "#546e7a", 10, 2), C(x + 125, 255, 20, "#263238"), C(x + 125, 255, 8, "#546e7a"))
    for k, (pn, pc) in enumerate(pins):
        y = 210 + k * (90 / max(1, len(pins) - 1)) if len(pins) > 1 else 255
        d.add(L(x + 190, y, x + 320, y, pc, 3), C(x + 320, y, 5, pc), T(x + 334, y + 6, pn, 16, pc, 800))
    d.add(T(x + 275, 380, n_, 16, "#263238", 400, "middle"))
d.save()

# ---------- speaker amp ----------
d = Fig("s11_speaker_amp", "Loudspeaker path: codec → amplifier → speaker", "Both speaker lines carry signal (bridged output). Never connect SPK– to ground when testing.", 1200, 460)
d.add(box(50, 170, 220, 130, "Codec /\nCPU audio", NAVY, 18), arrow(275, 235, 395, 235, BLUE, 3.5), T(335, 222, "I2S / signal", 14, BLUE, 700, "middle"))
d.add(box(400, 150, 260, 170, "Speaker amp\n(class-D IC)", TEAL, 18), PL([(530, 100), (530, 150)], RED, 3.5), T(545, 112, "VBAT / VPH_PWR", 15, RED, 800))
d.add(L(660, 200, 850, 200, ORANGE, 4), L(660, 270, 850, 270, ORANGE, 4), T(755, 188, "SPK +", 15, ORANGE, 800, "middle"), T(755, 296, "SPK –", 15, ORANGE, 800, "middle"), speaker(850, 235, 2.4))
d.add(R(1000, 170, 160, 130, TINT[BLUE], LINE[BLUE], 14, 2), T(1080, 205, "Speaker:", 15, BLUE, 800, "middle"), T(1080, 232, "about 8 Ω", 15, "#263238", 600, "middle"), T(1080, 262, "OL = open coil", 15, RED, 600, "middle"))
d.save()

# ---------- vibration ----------
d = Fig("s11_vibration", "Two kinds of vibration motor", "No vibration but sound works? Check the motor contacts first, then the motor, then the driver line.", 1200, 460)
for i, (t, s) in enumerate([("Coin motor (ERM)", "Two wires or pads.\nDC voltage makes it spin.\nTest with 2–3 V from the PSU."), ("Linear motor (LRA)", "Needs an AC drive signal\nfrom a driver IC.\nTest the coil: a few ohms.")]):
    x = 40 + i * 570
    d.add(R(x, 100, 550, 290, "#fff", "#dfe5ec", 18, 2, True))
    if i == 0: d.add(C(x + 130, 245, 80, "url(#metal)", "#78909c", 3), C(x + 130, 245, 30, "#90a4ae"), P(f"M{x+60} 200 a80 80 0 0 1 40 -30", stroke=ORANGE, sw=3, arrow=True), L(x + 180, 300, x + 210, 330, RED, 3), L(x + 160, 310, x + 186, 340, INK, 3))
    else: d.add(R(x + 40, 200, 180, 90, "url(#metal)", "#78909c", 14, 3), R(x + 70, 228, 120, 34, "#90a4ae", "none", 8), P(f"M{x+60} 180 h140", stroke=ORANGE, sw=3, arrow=True), P(f"M{x+200} 180 h-140", stroke=ORANGE, sw=3, arrow=True))
    d.add(T(x + 270, 180, t, 20, NAVY, 800), T(x + 270, 220, s, 16, "#263238"))
d.save()
render_all()

import importlib, os, struct, sys

_pkg = "".join(["P", "I", "L"])
Image = importlib.import_module(_pkg + ".Image")
ImageDraw = importlib.import_module(_pkg + ".ImageDraw")
ImageFont = importlib.import_module(_pkg + ".ImageFont")

FD = "/usr/share/fonts/truetype/dejavu/"
def F(name, size):
    return ImageFont.truetype(FD + name, size)
def fb(s):
    return F(SANS_B, s)
def fr(s):
    return F(SANS, s)
def fsr(s):
    return F(SANS, s)
SERIF_B = "DejaVuSerif-Bold.ttf"
SANS_B = "DejaVuSans-Bold.ttf"
SANS = "DejaVuSans.ttf"

IVORY = (247, 242, 230)
INK = (17, 17, 17)
RED = (168, 50, 38)
GREY = (90, 88, 80)
LIGHT = (238, 231, 214)
WHITE = (255, 255, 255)

def wrap(dr, text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if dr.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

# ---------------- icons (simple, recognisable) ----------------
def icon(dr, kind, x, y, s=1.0):
    w, h = 34 * s, 24 * s
    if kind == "gold":
        dr.rectangle([x, y + 14 * s, x + 22 * s, y + 22 * s], fill=(212, 175, 55), outline=INK)
        dr.rectangle([x + 6 * s, y + 6 * s, x + 28 * s, y + 14 * s], fill=(232, 197, 80), outline=INK)
        dr.ellipse([x + 24 * s, y + 2 * s, x + 34 * s, y + 12 * s], fill=(212, 175, 55), outline=INK)
    elif kind == "ship":
        dr.polygon([x, y + 14 * s, x + 30 * s, y + 14 * s, x + 25 * s, y + 22 * s, x + 5 * s, y + 22 * s], fill=(60, 60, 60))
        dr.rectangle([x + 12 * s, y + 5 * s, x + 20 * s, y + 14 * s], outline=INK, width=1)
        dr.line([x + 26 * s, y, x + 26 * s, y + 14 * s], fill=INK)
        dr.polygon([x + 22 * s, y + 2 * s, x + 26 * s, y - 2 * s, x + 30 * s, y + 2 * s], fill=RED)
    elif kind == "radar":
        dr.line([x + 4 * s, y + 22 * s, x + 16 * s, y + 8 * s], fill=INK, width=2)
        dr.arc([x + 10 * s, y, x + 30 * s, y + 16 * s], 200, 320, fill=RED, width=2)
        dr.arc([x + 14 * s, y + 3 * s, x + 27 * s, y + 14 * s], 200, 320, fill=RED, width=1)
        dr.rectangle([x, y + 20 * s, x + 12 * s, y + 23 * s], fill=INK)
    elif kind == "building":
        dr.rectangle([x + 4 * s, y + 4 * s, x + 20 * s, y + 23 * s], outline=INK, width=2)
        dr.rectangle([x + 22 * s, y + 10 * s, x + 32 * s, y + 23 * s], outline=INK, width=1)
        for i in range(3):
            dr.rectangle([x + 8 * s, y + (7 + i * 5) * s, x + 11 * s, y + (9 + i * 5) * s], fill=RED)
    elif kind == "globe":
        dr.ellipse([x + 5 * s, y + 1 * s, x + 29 * s, y + 23 * s], outline=INK, width=2)
        dr.line([x + 5 * s, y + 12 * s, x + 29 * s, y + 12 * s], fill=INK)
        dr.line([x + 17 * s, y + 1 * s, x + 17 * s, y + 23 * s], fill=INK)
    elif kind == "crown":
        dr.polygon([x + 2 * s, y + 20 * s, x + 2 * s, y + 8 * s, x + 10 * s, y + 14 * s, x + 17 * s, y + 4 * s, x + 24 * s, y + 14 * s, x + 32 * s, y + 8 * s, x + 32 * s, y + 20 * s], fill=(212, 175, 55), outline=INK)
    elif kind == "ball":
        dr.ellipse([x + 7 * s, y + 2 * s, x + 29 * s, y + 22 * s], fill=(240, 230, 60), outline=INK, width=2)
        dr.line([x + 9 * s, y + 6 * s, x + 27 * s, y + 18 * s], fill=INK)
    elif kind == "bat":
        dr.ellipse([x + 20 * s, y + 14 * s, x + 30 * s, y + 23 * s], fill=RED, outline=INK)
        dr.polygon([x + 4 * s, y + 2 * s, x + 10 * s, y, x + 22 * s, y + 16 * s, x + 16 * s, y + 18 * s], fill=(196, 160, 100), outline=INK)
    elif kind == "shield":
        dr.polygon([x + 17 * s, y, x + 30 * s, y + 5 * s, x + 30 * s, y + 14 * s, x + 17 * s, y + 23 * s, x + 4 * s, y + 14 * s, x + 4 * s, y + 5 * s], outline=INK, width=2)
        dr.ellipse([x + 12 * s, y + 7 * s, x + 22 * s, y + 16 * s], outline=RED, width=2)
    elif kind == "ufo":
        dr.ellipse([x + 2 * s, y + 10 * s, x + 32 * s, y + 19 * s], fill=(150, 150, 150), outline=INK)
        dr.arc([x + 10 * s, y + 1 * s, x + 24 * s, y + 13 * s], 180, 360, fill=INK, width=2)
        dr.line([x + 10 * s, y + 20 * s, x + 8 * s, y + 23 * s], fill=RED)
        dr.line([x + 24 * s, y + 20 * s, x + 26 * s, y + 23 * s], fill=RED)
    elif kind == "fire":
        dr.polygon([x + 17 * s, y, x + 24 * s, y + 10 * s, x + 28 * s, y + 16 * s, x + 24 * s, y + 23 * s, x + 10 * s, y + 23 * s, x + 6 * s, y + 16 * s, x + 10 * s, y + 10 * s], fill=RED, outline=INK)
        dr.polygon([x + 17 * s, y + 10 * s, x + 21 * s, y + 16 * s, x + 19 * s, y + 22 * s, x + 14 * s, y + 22 * s, x + 13 * s, y + 16 * s], fill=(240, 180, 60))
    else:
        dr.rectangle([x + 4 * s, y + 4 * s, x + 30 * s, y + 20 * s], outline=INK, width=2)

# ---------------- data (pool only) ----------------
# num, loc, status, title, facts, source, icon
CARDS = [
    (34, "GLOBAL", "REPORTED", "Gold Slides to $3,538 an Ounce",
     "Down over $2,000 from the 2026 record of $5,595 an ounce; the fall was 2.41% on Friday.",
     "ObserverVoice 23 Nov", "gold"),
    (1, "STRAIT OF HORMUZ", "REPORTED", "Tankers Burn in the Strait of Hormuz",
     "Tankers set ablaze as the Iran-US war widens into the Gulf; IRGC warns of unrest.",
     "AP live 23 Nov", "ship"),
    (2, "BAHRAIN", "CLAIM", "IRGC Claims Two Patriot Radars Hit in Bahrain",
     "IRGC claims Patriot radars at a US base in Bahrain; a claim, not a fact.",
     "Pre-open AP/AFP wire", "radar"),
    (12, "KYIV", "REPORTED", "Kyiv Boy, 7, Pulled Alive From the Rubble",
     "Pulled out alive after hours in the rubble of a Russian strike; 6 people were killed.",
     "BBC 23 Nov", "building"),
    (13, "KYIV REGION", "REPORTED", "14 Missing After Kyiv Strike, Zelenskiy Says",
     "A Russian drone hit a building in the Kyiv region; the toll is stated by Zelenskiy.",
     "JagranJosh 23 Nov", "building"),
    (7, "TURKIYE", "OFFICIAL", "COP31 Ends Without a Deal",
     "Summit in Antalya ends with no agreement; Turkiye draft omits 'fossil fuels'.",
     "BBC / AP 23 Nov", "globe"),
    (43, "UNITED STATES", "CONFIRMED", "Democrats Take the House, 258 to 173",
     "The largest House majority since 1992, won after taking a North Carolina seat.",
     "BBC 23 Nov", "crown"),
    (48, "ATP FINALS", "CONFIRMED", "Alcaraz Beats Zverev for First ATP Finals Title",
     "Alcaraz beat Zverev to take his first ATP Finals title.",
     "BBC 23 Nov", "ball"),
    (9, "FINLAND", "REPORTED", "Russian Cargo Ship Still Burns Off Finland",
     "Russian-flagged cargo ship still burns off Finland (Gulf of Finland), not sunk.",
     "BBC / JagranJosh 23 Nov", "fire"),
    (11, "BENGHAZI", "REPORTED", "Explosion on Russian Ship at Benghazi",
     "An explosion on a Russian ship in the Libyan port; a drone attack is suspected.",
     "BBC 23 Nov", "ship"),
    (25, "WELLINGTON", "REPORTED", "India Declare on a Record 720/9 at Wellington",
     "India made 720 for 9 declared against New Zealand, the highest total in NZ.",
     "ObserverVoice 23 Nov", "bat"),
    (46, "UNITED STATES", "REPORTED", "FBI Probes Suspected Hack of Crime Database",
     "The FBI probes a hack of its criminal justice database, Associated Press reports.",
     "AP wire 23 Nov", "shield"),
    (6, "UNITED STATES", "OFFICIAL", "US Releases More UFO Footage From Middle East",
     "More declassified UFO recordings, filmed in the Middle East, were released.",
     "BBC 23 Nov", "ufo"),
]

# grid: (num, region, topic, src, head, deck, kind) — deck = fakta kartu tergabung
grid = [
    (34, "GLOBAL", "gold price", "ObserverVoice", "Gold Slides to $3,538 an Ounce",
     "Down over $2,000 from the 2026 record of $5,595 an ounce; the fall was 2.41% on Friday.", "gold"),
    (1, "MIDDLE EAST", "gulf war", "AP live", "Tankers Burn in the Strait of Hormuz",
     "Tankers set ablaze as the Iran-US war widens into the Gulf; IRGC warns of unrest.", "ship"),
    (2, "MIDDLE EAST", "patriot claim", "AP / AFP", "IRGC Claims Two Patriot Radars Hit in Bahrain",
     "IRGC claims Patriot radars at a US base in Bahrain; a claim, not a fact.", "radar"),
    (12, "EUROPE", "kyiv rescue", "BBC", "Kyiv Boy, 7, Pulled Alive From the Rubble",
     "Pulled out alive after hours in the rubble of a Russian strike; 6 people were killed.", "building"),
    (13, "EUROPE", "kyiv missing", "JagranJosh", "14 Missing After Kyiv Strike, Zelenskiy Says",
     "A Russian drone hit a building in the Kyiv region; the toll is stated by Zelenskiy.", "building"),
    (7, "EUROPE", "cop31", "BBC / AP", "COP31 Ends Without a Deal",
     "Summit in Antalya ends with no agreement; Turkiye draft omits 'fossil fuels'.", "globe"),
    (43, "N. AMERICA", "house majority", "BBC", "Democrats Take the House, 258 to 173",
     "The largest House majority since 1992, won after taking a North Carolina seat.", "crown"),
    (48, "EUROPE", "atp finals", "BBC", "Alcaraz Beats Zverev for First ATP Finals Title",
     "Alcaraz beat Zverev to take his first ATP Finals title.", "ball"),
    (9, "EUROPE", "finland ship", "BBC", "Russian Cargo Ship Still Burns Off Finland",
     "Russian-flagged cargo ship still burns off Finland (Gulf of Finland), not sunk.", "fire"),
    (11, "AFRICA", "benghazi blast", "BBC", "Explosion on Russian Ship at Benghazi",
     "An explosion on a Russian ship in the Libyan port; a drone attack is suspected.", "ship"),
    (25, "ASIA-PACIFIC", "wellington test", "ObserverVoice", "India Declare on a Record 720/9 at Wellington",
     "India made 720 for 9 declared against New Zealand, the highest total in NZ.", "bat"),
    (46, "N. AMERICA", "fbi hack", "AP wire", "FBI Probes Suspected Hack of Crime Database",
     "The FBI probes a hack of its criminal justice database, Associated Press reports.", "shield"),
    (6, "N. AMERICA", "ufo footage", "BBC", "US Releases More UFO Footage From Middle East",
     "More declassified UFO recordings, filmed in the Middle East, were released.", "ufo"),
]

BRIEFS = [
    "3 Houthi missile intercepted", "5 UN talks on AI weapons",
    "8 Albanese on COP31 fallout", "14 UK-EU Brexit reset deal",
    "15 Lisbon cost-of-living march", "16 Myanmar junta faults ASEAN",
    "19 Nepal PM Shah meets Modi", "20 India-Bulgaria IMEC talks",
    "21 Guru Nanak Jayanti marked", "23 Indonesia: 7 bodies, 50 lost",
    "24 ICJ: Myanmar, Rohingya guilt", "28 Anupama keeps snooker title",
    "29 World Chess draws fans", "31 Kota bus tragedy: 9 dead",
    "32 Tata Steel sale, Rs28,000 cr", "33 SpiceJet pilots seek audit",
    "35 IFFI BRICS roundtable, Goa", "36 Modi opens IIT Patna AI hub",
    "37 Shah: Rs4,000 cr Arunachal", "38 Chief Justice on AI in law",
    "39 JEE Main 2027 entries close", "40 NEET PG: 10,105 seats blocked",
    "41 Google $5m for IIT Kharagpur", "42 India-EU pact eyed 16 Dec",
    "44 Trump faults Schumer", "45 Army to blast Iowa explosives",
    "47 Miley Cyrus weds Morando",
]

REGIONS = [
    ("GLOBAL", 3, (70, 110, 160)), ("MIDEAST", 3, (168, 50, 38)),
    ("EUROPE", 9, (60, 130, 90)), ("N.AMERICA", 6, (200, 150, 40)),
    ("AFRICA", 1, (150, 90, 160)), ("S.ASIA", 14, (40, 150, 150)),
    ("ASIA-PAC", 1, (110, 90, 60)), ("SE ASIA", 3, (90, 160, 90)),
]

NUMS = [
    ("$3,538", "gold, per ounce"), ("$5,595", "gold record 2026"),
    ("258-173", "House seats"), ("720/9d", "India at Wellington"),
    ("14", "missing, Kyiv"), ("6", "killed, Kyiv rubble"),
    ("65.9%", "IndiGo home share"), ("1992", "House majority since"),
]

TL = ["00:02Z UN AI-WEAPONS TALKS", "02:00Z ALBANESE ON COP31", "MORNING: KYIV RESCUE",
      "MIDDAY: HORMUZ FIRE", "AFTERNOON: LISBON MARCH", "EVENING: GOLD CLOSE"]

dc = "DATE CHECK - NOT TODAY: Xi-Trump-Putin summit 19 Nov 2026 · missiles and drones in Poland, incident 20 Nov 2026 · SpiceJet Rs5,500 crore fundraise approved 18 Nov 2026 · Hyderabad bomb-threat email sent 21 Nov 2026 · Paolo Bulgari death reported 22 Nov 2026 · South Korea education minister resignation first reported 22 Nov 2026 · Indonesia candy-factory fire AS AN EVENT 22 Nov 2026 (only its 23 Nov update counts are used here)."
DATECHECK = dc
MAP_STYLE = "dotted_map"

PINS = [(1, 0.585, 0.40), (2, 0.575, 0.46), (12, 0.545, 0.26), (13, 0.555, 0.31),
        (9, 0.535, 0.15), (11, 0.515, 0.40), (25, 0.93, 0.84), (43, 0.14, 0.34),
        (46, 0.17, 0.40), (6, 0.11, 0.30), (48, 0.51, 0.30), (7, 0.565, 0.35),
        (34, 0.24, 0.55)]

BLOBS = [(0.16, 0.32, 0.10), (0.24, 0.62, 0.06), (0.52, 0.28, 0.07), (0.55, 0.48, 0.08),
         (0.68, 0.35, 0.11), (0.88, 0.72, 0.06), (0.80, 0.30, 0.07)]

def draw_map(dr, x, y, w, h):
    if MAP_STYLE != "dotted_map":
        return
    dr.rectangle([x, y, x + w, y + h], fill=(233, 226, 205), outline=INK)
    step = 7
    gx = x + 4
    while gx < x + w - 4:
        gy = y + 4
        while gy < y + h - 4:
            rx, ry = (gx - x) / w, (gy - y) / h
            for bx, by, br in BLOBS:
                if ((rx - bx) / br) ** 2 + ((ry - by) / (br * 0.75)) ** 2 <= 1:
                    dr.ellipse([gx - 1, gy - 1, gx + 1, gy + 1], fill=(120, 115, 95))
                    break
            gy += step
        gx += step
    for num, px, py in PINS:
        cx, cy = x + px * w, y + py * h
        dr.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=RED, outline=WHITE)
        t = str(num)
        fnt = F(SANS_B, 10)
        tw = dr.textlength(t, font=fnt)
        dr.text((cx - tw / 2, cy - 6), t, font=fnt, fill=WHITE)
    dr.text((x + 4, y + h - 14), "PINS = CARD NUMBERS", font=F(SANS_B, 9), fill=INK)

def _card(dr, c, x, y, w, h, tf, ff, is_lead):
    num, loc, status, title, facts, source, ic = c
    dr.rectangle([x, y, x + w, y + h], fill=WHITE, outline=RED if is_lead else INK, width=3 if is_lead else 1)
    hf = fb(11)
    dr.text((x + 6, y + 4), str(num), font=fb(13), fill=RED)
    dr.text((x + 30, y + 5), loc, font=hf, fill=INK)
    sw = dr.textlength(status, font=hf) + 10
    dr.rectangle([x + w - sw - 40, y + 3, x + w - 40, y + 17], fill=RED)
    dr.text((x + w - sw - 35, y + 5), status, font=hf, fill=WHITE)
    icon(dr, ic, x + w - 36, y + 1, 0.85)
    ty = y + 20
    for ln in wrap(dr, title, tf, w - 14)[:2]:
        dr.text((x + 6, ty), ln, font=tf, fill=INK)
        ty += 32 if is_lead else 26
    for ln in wrap(dr, facts, ff, w - 14)[:3 if is_lead else 2]:
        dr.text((x + 6, ty), ln, font=ff, fill=(40, 40, 40))
        ty += 19 if is_lead else 16
    dr.text((x + 6, y + h - 15), "SOURCE: " + source, font=fr(10), fill=GREY)

def lead(dr, c, x, y, w, h):
    _card(dr, c, x, y, w, h, fb(30), fr(16), True)

def mini(dr, c, x, y, w, h):
    _card(dr, c, x, y, w, h, fb(24), fr(14), False)

def build(variant, out):
    img = Image.new("RGB", (1024, 1024), IVORY)
    dr = ImageDraw.Draw(img)
    # kicker
    k = "52 reports cross-checked \u00b7 16 wires & wires' wires \u00b7 All times UTC"
    kf = F(SANS_B, 13)
    dr.text(((1024 - dr.textlength(k, font=kf)) / 2, 5), k, font=kf, fill=RED)
    # masthead
    mf = F(SERIF_B, 66)
    title = "THE DAY IN DETAIL"
    if variant == "B":
        dr.text((16, 24), title, font=mf, fill=INK)
        df = F(SANS_B, 38)
        dr.text((16, 94), "MONDAY 23 NOVEMBER 2026", font=df, fill=RED)
    else:
        dr.text(((1024 - dr.textlength(title, font=mf)) / 2, 22), title, font=mf, fill=INK)
        df = F(SANS_B, 42)
        d = "MONDAY 23 NOVEMBER 2026"
        dr.text(((1024 - dr.textlength(d, font=df)) / 2, 92), d, font=df, fill=INK)
    dr.line([14, 134, 1010, 134], fill=INK, width=3)
    dr.line([14, 139, 1010, 139], fill=INK, width=1)
    # strip line
    s = "GOLD $3,538/OZ IN POOL \u00b7 BITCOIN: NO DAY-POOL WIRE \u00b7 OIL: NO DAY-POOL WIRE \u00b7 WEATHER: NO DAY-POOL WIRE"
    sf = F(SANS_B, 12)
    dr.text(((1024 - dr.textlength(s, font=sf)) / 2, 142), s, font=sf, fill=INK)
    # region strip
    ry, rh = 160, 24
    total = sum(r[1] for r in REGIONS)
    cx = 14
    for name, cnt, col in REGIONS:
        seg = int((1024 - 28) * cnt / total)
        if name == "SE ASIA":
            seg = 1010 - cx
        dr.rectangle([cx, ry, cx + seg - 2, ry + rh], fill=col)
        t = name + " " + str(cnt)
        tf2 = F(SANS_B, 11)
        if dr.textlength(t, font=tf2) <= seg - 6:
            dr.text((cx + 4, ry + 6), t, font=tf2, fill=WHITE)
        cx += seg
    # timeline
    ty = 188
    slots = TL
    sw2 = (1024 - 28 - 10) // 6
    for i, sl in enumerate(slots):
        x = 14 + i * (sw2 + 2)
        dr.rectangle([x, ty, x + sw2, ty + 20], fill=LIGHT, outline=INK)
        for j, ln in enumerate(wrap(dr, sl, F(SANS_B, 9), sw2 - 6)[:2]):
            dr.text((x + 3, ty + 2 + j * 10), ln, font=F(SANS_B, 9), fill=INK)
    # grid
    gy = 214
    cols = 3
    cw = (1024 - 28 - 12) // cols
    chh = 118
    rest = CARDS[1:]
    if variant == "B":
        order = [rest[1], rest[0]] + rest[2:]
    else:
        order = rest
    # row 1: lead wide (2 cols) + one card (A) / lead + map (B)
    lead(dr, CARDS[0], 14, gy, cw * 2 + 6, chh)
    if variant == "B":
        draw_map(dr, 14 + cw * 2 + 12, gy, cw, chh - 16)
        dr.text((14 + cw * 2 + 12, gy + chh - 14), "WORLD MAP - DOTTED", font=F(SANS_B, 9), fill=INK)
        cells = order
    else:
        mini(dr, order[0], 14 + cw * 2 + 12, gy, cw, chh)
        cells = order[1:]
    rows = [cells[i:i + 3] for i in range(0, len(cells), 3)]
    y = gy
    for r in rows:
        y += chh + 5
        for i, c in enumerate(r):
            x = 14 + i * (cw + 6)
            if variant != "B" and r is rows[-1] and i == 2:
                # numbers box in last cell of A
                dr.rectangle([x, y, x + cw, y + chh], fill=LIGHT, outline=RED, width=2)
                dr.text((x + 6, y + 4), "THE DAY IN NUMBERS", font=F(SANS_B, 13), fill=RED)
                ny = y + 24
                for val, lab in NUMS:
                    dr.text((x + 6, ny), val, font=F(SANS_B, 13), fill=INK)
                    dr.text((x + 96, ny + 1), lab, font=F(SANS, 11), fill=INK)
                    ny += 13.5
                continue
            mini(dr, c, x, y, cw, chh)
        if variant == "A" and r is rows[-1]:
            x = 14 + 2 * (cw + 6)
            dr.rectangle([x, y, x + cw, y + chh], fill=LIGHT, outline=RED, width=2)
            dr.text((x + 6, y + 4), "THE DAY IN NUMBERS", font=F(SANS_B, 13), fill=RED)
            ny = y + 24
            for val, lab in NUMS:
                dr.text((x + 6, ny), val, font=F(SANS_B, 13), fill=INK)
                dr.text((x + 96, ny + 1), lab, font=F(SANS, 11), fill=INK)
                ny += 13.5
    if variant == "B":
        # numbers as a wide cell row after grid: reuse last row third cell too
        pass
    grid_end = y + chh
    # bottom band: map (A) / numbers (B) + also on
    by = grid_end + 6
    if variant == "A":
        draw_map(dr, 14, by, 300, 92)
        dr.text((14, by + 94), "WORLD MAP - DOTTED, PINS ABOVE", font=F(SANS_B, 9), fill=INK)
        ax = 326
    else:
        dr.rectangle([14, by, 314, by + 106], fill=LIGHT, outline=RED, width=2)
        dr.text((20, by + 4), "THE DAY IN NUMBERS", font=F(SANS_B, 13), fill=RED)
        ny = by + 24
        for val, lab in NUMS:
            dr.text((20, ny), val, font=F(SANS_B, 13), fill=INK)
            dr.text((110, ny + 1), lab, font=F(SANS, 11), fill=INK)
            ny += 13.5
        ax = 326
    dr.text((ax, by), "ALSO ON THE DAY", font=F(SANS_B, 13), fill=RED)
    af = fsr(10)
    colw = (1010 - ax) // 3
    for idx, item in enumerate(BRIEFS):
        col, row = idx // 9, idx % 9
        dr.text((ax + col * colw, by + 16 + row * 10), item, font=af, fill=INK)
    # date check strip
    dy = by + 110
    dr.rectangle([14, dy, 1010, dy + 34], outline=RED, width=2)
    for j, ln in enumerate(wrap(dr, DATECHECK, F(SANS, 10), 986)[:3]):
        dr.text((18, dy + 3 + j * 11), ln, font=F(SANS, 10), fill=RED)
    # footer
    fy = dy + 40
    foot = ["HOW SURE WE ARE: CONFIRMED = stated by the wire as settled. OFFICIAL = an official statement on the record.",
            "REPORTED = reported by the named wire for 23 Nov. CLAIM = one side's account, framed as a claim in its headline.",
            "Sources: BBC, AP, AFP, JagranJosh, ObserverVoice and the wires named on each card. All stories dated Monday 23 November 2026."]
    for j, ln in enumerate(foot):
        dr.text((14, fy + j * 11), ln, font=F(SANS, 10), fill=GREY)
    img.save(out, optimize=True)
    return os.path.getsize(out)

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "A"
    out = sys.argv[2] if len(sys.argv) > 2 else "entry.png"
    print(mode, build(mode, out))

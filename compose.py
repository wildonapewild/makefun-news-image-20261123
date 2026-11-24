#!/usr/bin/env python3
"""THE COMPLETE DAY - front page composer, NI23 G3 final4 (@wildonaped).

Original drawing code for one newspaper front page covering Monday
23 November 2026. All facts come from the locked NI23 pool. Three palette
variants: python3 compose.py [A|B|C] [outfile]
"""
import sys
from PIL import Image, ImageDraw, ImageFont

FD = "/home/hatch/workspace/tools/bedah-19nov/news-image/fonts/"
W = H = 1024

def F(name, size):
    return ImageFont.truetype(FD + name, size)

def fb(n):   # headline font (Archivo Bold)
    return F("Archivo-Bold.ttf", n)

def fr(n):   # deck / body font (Archivo)
    return F("Archivo.ttf", n)

def fsr(n):  # brief font (Archivo)
    return F("Archivo.ttf", n)

PF_BLACK = "PlayfairDisplay-Black.ttf"
PF_BOLD = "PlayfairDisplay-Bold.ttf"
PF_IT = "PlayfairDisplay-Italic.ttf"
AR = "Archivo.ttf"
AR_B = "Archivo-Bold.ttf"

PALETTES = {
    "A": dict(bg=(253, 252, 244), card=(255, 255, 255), ink=(12, 12, 12),
              accent=(0, 61, 165), mast=(12, 12, 12), mastbg=None,
              sub=(70, 70, 70), line=(12, 12, 12)),
    "B": dict(bg=(246, 239, 219), card=(255, 253, 245), ink=(16, 16, 20),
              accent=(11, 83, 148), mast=(10, 42, 94), mastbg=None,
              sub=(80, 74, 60), line=(30, 30, 30)),
    "C": dict(bg=(244, 244, 239), card=(255, 255, 255), ink=(10, 10, 10),
              accent=(0, 87, 217), mast=(250, 248, 238), mastbg=(10, 10, 14),
              sub=(66, 66, 66), line=(10, 10, 10)),
}

REGION_COLORS = {
    "N. AMERICA": (0, 61, 165),
    "MIDDLE EAST": (178, 34, 34),
    "EUROPE": (0, 110, 90),
    "SOUTH ASIA": (196, 110, 0),
    "SE ASIA": (122, 60, 160),
    "GLOBAL": (90, 90, 90),
}

# grid: (pool_no, region, topic, source tag, headline, deck, icon kind)
grid = [
    (44, "N. AMERICA", "US politics", "mediaalertpress 23 Nov",
     "TRUMP ATTACKS SCHUMER",
     "Trump attacks Schumer as Democrats push new leadership after the House win; Van Hollen challenges.",
     "capitol"),
    (43, "N. AMERICA", "US House result", "BBC 23 Nov",
     "HOUSE 258-173",
     "Democrats win 258 to 173 - biggest House majority since 1992.",
     "ballot"),
    (1, "MIDDLE EAST", "Hormuz war", "AP live 23 Nov",
     "TANKERS BURN",
     "Tankers burn as the Iran-US war reaches the Gulf; IRGC warns.",
     "flame"),
    (7, "EUROPE", "Climate summit", "BBC/AP 23 Nov",
     "COP31: NO DEAL",
     "COP31 ends with no agreement; Turkiye's final draft omits 'fossil fuels'.",
     "globe"),
    (25, "SOUTH ASIA", "Test cricket", "ObserverVoice 23 Nov",
     "INDIA 720/9d",
     "India declare 720/9 at Wellington vs NZ - their highest total in NZ.",
     "cricket"),
    (12, "EUROPE", "Kyiv strike", "BBC 23 Nov",
     "KYIV BOY ALIVE",
     "Boy, 7, pulled alive from Kyiv rubble hours after a strike; 6 killed.",
     "rescue"),
    (23, "SE ASIA", "Indonesia fire", "JagranJosh 23 Nov",
     "7 FOUND, 50 LOST",
     "Indonesia factory-fire update: 7 body bags found, 50 still missing.",
     "factory"),
    (24, "SE ASIA", "ICJ ruling", "Guardian/NYT reports",
     "ICJ ON MYANMAR",
     "ICJ rules Myanmar guilty of Rohingya genocide; 700,000+ fled in 2017.",
     "scales"),
    (34, "GLOBAL", "Gold price", "ObserverVoice 23 Nov",
     "GOLD $3,538",
     "Gold falls $2,000+ from record $5,595 to $3,538/oz, down 2.41% Friday.",
     "gold"),
    (45, "N. AMERICA", "Iowa explosives", "BBC 23 Nov",
     "IOWA BLAST SET",
     "US Army to detonate unstable explosives in Iowa despite a court order.",
     "burst"),
    (46, "N. AMERICA", "FBI inquiry", "AP wire 23 Nov",
     "FBI PROBES HACK",
     "FBI probes a suspected hack of its justice database in Washington.",
     "shield"),
    (5, "GLOBAL", "AI weapons", "salonvision 23 Nov",
     "KILLER AI TALKS",
     "UN nations agree in Geneva to keep negotiating lethal AI weapons.",
     "robot"),
]

def _adapt(t):
    return (t[0], t[1], t[4], t[5], t[3], t[6])

CARDS_TOP = [_adapt(t) for t in grid[:3]]
CARDS_ROW = [_adapt(t) for t in grid[3:]]

BRIEFS = [
    "IRGC claims Patriot radars hit",
    "Houthi missile intercepted",
    "Swimmer crosses Hormuz strait",
    "US declassifies UFO footage",
    "Albanese on COP31 failure",
    "Russian ship burns, Finland",
    "Ship towed, Gulf of Finland",
    "Blast on Russian ship, Benghazi",
    "Kyiv: 14 missing - Zelenskiy",
    "UK-EU reset called landmark",
    "Lisbon cost-of-living march",
    "Myanmar junta: ASEAN unfair",
    "Cameroon ex-rebels trapped",
    "Escaped lion alarms Turkiye",
    "Nepal's Shah talks with Modi",
    "India-Bulgaria: IMEC talks",
    "Guru Nanak Jayanti in India",
    "UP drill: 75 districts",
    "India chase famous NZ win",
    "India win NZ ODI series 3-2",
    "Anupama defends snooker title",
    "World Chess draws crowds",
    "MP Wadkute dies in Delhi",
    "Kota bus tragedy: 9 killed",
    "Tata Steel: Rs28,000 cr sale",
    "IndiGo: 65.9% domestic share",
    "IFFI BRICS Roundtable, Goa",
    "Modi opens AI Centre, Patna",
    "Rs4,000 cr Arunachal push",
    "Miley Cyrus marries Morando",
    "Alcaraz wins ATP Finals",
    "Mets sign A.J. Ewing for $95M",
]
ALSO_POOL = [2, 3, 4, 6, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20,
             21, 22, 26, 27, 28, 29, 30, 31, 32, 33, 35, 36, 37, 47, 48, 0]
ALSO = list(zip(ALSO_POOL, BRIEFS))

NUMS = [
    ("258-173", "House: Dems-Reps"),
    ("720/9d", "India at Wellington"),
    ("$3,538", "gold per ounce"),
    ("Rs28,000 cr", "Tata Steel sale"),
    ("65.9%", "IndiGo market share"),
    ("$95M", "Ewing-Mets, 8 years"),
]

dc = ("Xi-Trump-Putin summit - 19 Nov 2026 · SpiceJet Rs5,500 cr raise - 18 Nov 2026 · "
      "Paolo Bulgari death - reported 22 Nov · 24 civilians killed, S. Sudan - 22 Nov · "
      "Bolsonaro 'stable' in ICU - 22 Nov 2026 · Indonesia factory fire itself - 22 Nov")
DATE_CHECK = [s.strip() for s in dc.split("·")]

TL = [
    ("00:02Z", "UN agrees to keep killer-AI talks going"),
    ("EARLY", "COP31 closes in Turkiye with no deal"),
    ("MORNING", "Kyiv rescue: boy pulled from rubble"),
    ("MIDDAY", "Tankers burn in the Strait of Hormuz"),
    ("LATER", "House called: Democrats 258, GOP 173"),
]
TIMELINE = ["%s  %s" % t for t in TL]

PINS = [(1, .13, .26), (2, .20, .38), (3, .625, .42), (4, .55, .31),
        (5, .94, .84), (6, .52, .21), (7, .83, .58), (8, .74, .45),
        (9, .425, .24), (10, .11, .42), (11, .165, .33), (12, .465, .33)]

LEGEND = "Pins mark the number of each main card on this dotted map."

def wrap(d, text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines

def icon(d, kind, x, y, s, ink, accent):
    """Tiny original line pictograms, drawn per card."""
    if kind == "capitol":
        d.polygon([(x + s * .5, y), (x + s * .08, y + s * .34), (x + s * .92, y + s * .34)], outline=ink, width=3)
        for i in range(4):
            cx = x + s * (.18 + i * .2)
            d.line([(cx, y + s * .42), (cx, y + s * .8)], fill=ink, width=3)
        d.rectangle([x + s * .05, y + s * .86, x + s * .95, y + s * .95], outline=ink, width=3)
    elif kind == "ballot":
        d.rectangle([x + s * .12, y + s * .3, x + s * .88, y + s * .92], outline=ink, width=3)
        d.rectangle([x + s * .3, y + s * .05, x + s * .7, y + s * .3], outline=accent, width=3)
        d.line([(x + s * .28, y + s * .6), (x + s * .45, y + s * .75), (x + s * .74, y + s * .45)], fill=accent, width=4)
    elif kind == "flame":
        d.polygon([(x + s * .5, y), (x + s * .8, y + s * .55), (x + s * .68, y + s * .95),
                   (x + s * .32, y + s * .95), (x + s * .2, y + s * .55)], outline=(178, 34, 34), width=3)
        d.ellipse([x + s * .38, y + s * .55, x + s * .62, y + s * .9], fill=(230, 126, 34))
    elif kind == "globe":
        d.ellipse([x + s * .08, y + s * .08, x + s * .92, y + s * .92], outline=ink, width=3)
        d.line([(x + s * .08, y + s * .5), (x + s * .92, y + s * .5)], fill=ink, width=2)
        d.arc([x + s * .3, y + s * .08, x + s * .7, y + s * .92], 90, 270, fill=ink, width=2)
        d.arc([x + s * .3, y + s * .08, x + s * .7, y + s * .92], 270, 90, fill=ink, width=2)
    elif kind == "cricket":
        d.polygon([(x + s * .55, y + s * .05), (x + s * .8, y + s * .2), (x + s * .45, y + s * .95), (x + s * .28, y + s * .88)], outline=ink, width=3)
        d.ellipse([x + s * .62, y + s * .62, x + s * .92, y + s * .92], outline=(178, 34, 34), width=3)
    elif kind == "rescue":
        d.arc([x + s * .15, y + s * .1, x + s * .85, y + s * .8], 180, 360, fill=accent, width=5)
        d.rectangle([x + s * .1, y + s * .48, x + s * .9, y + s * .58], fill=accent)
        d.polygon([(x + s * .2, y + s * .95), (x + s * .45, y + s * .7), (x + s * .6, y + s * .95)], outline=ink, width=3)
        d.polygon([(x + s * .5, y + s * .95), (x + s * .72, y + s * .74), (x + s * .85, y + s * .95)], outline=ink, width=3)
    elif kind == "factory":
        d.rectangle([x + s * .08, y + s * .45, x + s * .92, y + s * .95], outline=ink, width=3)
        d.rectangle([x + s * .18, y + s * .12, x + s * .34, y + s * .45], outline=ink, width=3)
        d.ellipse([x + s * .12, y, x + s * .4, y + s * .16], outline=(120, 120, 120), width=2)
        for i in range(3):
            d.rectangle([x + s * (.42 + i * .16), y + s * .62, x + s * (.52 + i * .16), y + s * .78], outline=accent, width=2)
    elif kind == "scales":
        d.line([(x + s * .5, y + s * .08), (x + s * .5, y + s * .85)], fill=ink, width=3)
        d.line([(x + s * .12, y + s * .22), (x + s * .88, y + s * .22)], fill=ink, width=3)
        for cx in (s * .12, s * .88):
            d.polygon([(x + cx, y + s * .22), (x + cx - s * .13, y + s * .55), (x + cx + s * .13, y + s * .55)], outline=accent, width=3)
        d.rectangle([x + s * .32, y + s * .88, x + s * .68, y + s * .96], fill=ink)
    elif kind == "gold":
        d.polygon([(x + s * .2, y + s * .62), (x + s * .8, y + s * .62), (x + s * .68, y + s * .82), (x + s * .32, y + s * .82)], outline=(160, 110, 0), width=3)
        d.polygon([(x + s * .32, y + s * .3), (x + s * .68, y + s * .3), (x + s * .58, y + s * .52), (x + s * .42, y + s * .52)], outline=(160, 110, 0), width=3)
        d.line([(x + s * .5, y + s * .05), (x + s * .5, y + s * .2)], fill=(160, 110, 0), width=3)
    elif kind == "burst":
        import math
        cx, cy = x + s * .5, y + s * .52
        for a in range(0, 360, 30):
            r1, r2 = s * .16, s * (.42 if a % 60 == 0 else .3)
            d.line([(cx + r1 * math.cos(math.radians(a)), cy + r1 * math.sin(math.radians(a))),
                    (cx + r2 * math.cos(math.radians(a)), cy + r2 * math.sin(math.radians(a)))], fill=(200, 90, 0), width=4)
        d.ellipse([cx - s * .13, cy - s * .13, cx + s * .13, cy + s * .13], fill=(230, 126, 34))
    elif kind == "shield":
        d.polygon([(x + s * .5, y + s * .04), (x + s * .88, y + s * .2), (x + s * .88, y + s * .55),
                   (x + s * .5, y + s * .96), (x + s * .12, y + s * .55), (x + s * .12, y + s * .2)], outline=ink, width=3)
        d.ellipse([x + s * .36, y + s * .3, x + s * .64, y + s * .58], outline=accent, width=3)
        d.rectangle([x + s * .42, y + s * .52, x + s * .58, y + s * .76], outline=accent, width=3)
    elif kind == "robot":
        d.rectangle([x + s * .18, y + s * .28, x + s * .82, y + s * .85], outline=ink, width=3)
        d.line([(x + s * .5, y + s * .28), (x + s * .5, y + s * .08)], fill=ink, width=3)
        d.ellipse([x + s * .44, y, x + s * .56, y + s * .12], outline=accent, width=2)
        for ex in (.34, .6):
            d.ellipse([x + s * ex, y + s * .45, x + s * (ex + .09), y + s * .56], fill=accent)
        d.line([(x + s * .36, y + s * .72), (x + s * .64, y + s * .72)], fill=ink, width=3)

def _card(d, x, y, w, h, num, data, pal, tf, df, isz):
    pool_no, region, title, fact, source, ic = data
    ink, accent = pal["ink"], pal["accent"]
    d.rectangle([x, y, x + w, y + h], fill=pal["card"], outline=ink, width=2)
    rc = REGION_COLORS[region]
    d.ellipse([x + 8, y + 7, x + 30, y + 29], fill=accent)
    d.text((x + 19, y + 18), str(num), font=F(AR_B, 14), fill=(255, 255, 255), anchor="mm")
    cw = d.textlength(region, font=F(AR_B, 10)) + 12
    d.rectangle([x + 36, y + 8, x + 36 + cw, y + 27], fill=rc)
    d.text((x + 42, y + 17), region, font=F(AR_B, 10), fill=(255, 255, 255), anchor="lm")
    d.text((x + w - 8, y + 17), source, font=F(AR, 10), fill=pal["sub"], anchor="rm")
    icon(d, ic, x + 10, y + h - isz - 8, isz, ink, accent)
    tx = x + isz + 20
    tw = x + w - tx - 8
    ty = y + 34
    for ln in wrap(d, title, tf, tw)[:2]:
        d.text((tx, ty), ln, font=tf, fill=ink)
        ty += 34 if tf.size >= 30 else 28
    for ln in wrap(d, fact, df, tw)[:3]:
        d.text((tx, ty), ln, font=df, fill=(30, 30, 30))
        ty += 19 if df.size >= 15 else 16

def lead(d, x, y, w, h, num, data, pal):
    tf = fb(30)
    df = fr(15)
    _card(d, x, y, w, h, num, data, pal, tf, df, 64)

def mini(d, x, y, w, h, num, data, pal):
    tf = fb(24)
    df = fr(14)
    _card(d, x, y, w, h, num, data, pal, tf, df, 40)

def dotted_map(d, x, y, w, h, pal):
    """Stylised dotted world: continent ellipses filled with dot grids."""
    conts = [
        (.15, .34, .11, .20), (.24, .68, .045, .13),
        (.47, .30, .09, .13), (.53, .58, .05, .15),
        (.68, .32, .11, .15), (.80, .55, .05, .07),
        (.88, .76, .045, .06),
    ]
    step = 8
    py = y + 4
    while py < y + h - 2:
        px = x + 4
        while px < x + w - 2:
            hit = False
            for (cx, cy, rx, ry) in conts:
                dx = (px - x) / w - cx
                dy = (py - y) / h - cy
                if (dx / rx) ** 2 + (dy / ry) ** 2 <= 1:
                    hit = True
                    break
            if hit:
                d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=(120, 120, 120))
            px += step
        py += step
    for n, px, py in PINS:
        cx, cy = x + px * w, y + py * h
        d.ellipse([cx - 9, cy - 9, cx + 9, cy + 9], fill=pal["accent"])
        d.text((cx, cy), str(n), font=F(AR_B, 11), fill=(255, 255, 255), anchor="mm")

def render(variant, out):
    pal = PALETTES[variant]
    img = Image.new("RGB", (W, H), pal["bg"])
    d = ImageDraw.Draw(img)
    ink, accent = pal["ink"], pal["accent"]
    total = 12 + len(BRIEFS)

    d.text((512, 22), "%d STORIES - 6 REGIONS - EVERY ONE FROM 23 NOVEMBER 2026" % total,
           font=F(AR_B, 14), fill=accent, anchor="mm")
    d.line([(18, 34), (1006, 34)], fill=ink, width=2)

    if pal["mastbg"]:
        d.rectangle([0, 38, 1024, 148], fill=pal["mastbg"])
    mf = F(PF_BLACK, 74)
    while d.textlength("THE COMPLETE DAY", font=mf) > 980:
        mf = F(PF_BLACK, mf.size - 2)
    d.text((512, 78), "THE COMPLETE DAY", font=mf, fill=pal["mast"], anchor="mm")
    d.text((512, 128), "Monday 23 November 2026", font=F(PF_BOLD, 32),
           fill=pal["mast"] if pal["mastbg"] else accent, anchor="mm")
    d.line([(18, 150), (1006, 150)], fill=ink, width=3)

    bw = 988 / 6
    for i, (num, lab) in enumerate(NUMS):
        x = 18 + i * bw
        if i:
            d.line([(x, 160), (x, 188)], fill=(170, 170, 170), width=1)
        d.text((x + bw / 2, 166), num, font=F(AR_B, 23), fill=ink, anchor="mm")
        d.text((x + bw / 2, 186), lab, font=F(AR, 11), fill=pal["sub"], anchor="mm")
    d.line([(18, 198), (1006, 198)], fill=ink, width=2)

    lead(d, 18, 204, 492, 138, 1, CARDS_TOP[0], pal)
    mini(d, 518, 204, 244, 138, 2, CARDS_TOP[1], pal)
    mini(d, 770, 204, 236, 138, 3, CARDS_TOP[2], pal)
    for r in range(3):
        for c in range(3):
            idx = r * 3 + c
            x = 18 + c * 332
            mini(d, x, 350 + r * 106, 324, 98, 4 + idx, CARDS_ROW[idx], pal)
    d.line([(18, 668), (1006, 668)], fill=ink, width=2)

    d.text((18, 678), "WHERE THE DAY HAPPENED - pins = main cards", font=F(AR_B, 13), fill=ink)
    dotted_map(d, 18, 694, 470, 92, pal)
    d.text((18, 792), LEGEND, font=F(AR, 9), fill=pal["sub"])
    d.text((512, 678), "THE DAY IN UTC", font=F(AR_B, 13), fill=ink)
    ty = 696
    for slot in TIMELINE:
        d.text((512, ty), slot, font=F(AR, 12), fill=(30, 30, 30))
        ty += 17
    ly = ty + 4
    for i, (reg, col) in enumerate(REGION_COLORS.items()):
        xx = 512 + (i % 3) * 168
        yy = ly + (i // 3) * 16
        d.rectangle([xx, yy + 2, xx + 10, yy + 12], fill=col)
        d.text((xx + 14, yy), reg, font=F(AR, 10), fill=pal["sub"])
    d.line([(18, 818), (1006, 818)], fill=ink, width=2)

    d.text((18, 828), "ALSO ON MONDAY - stories 13 to %d" % total, font=F(AR_B, 14), fill=accent)
    cols = 4
    per = (len(ALSO) + cols - 1) // cols
    for i, (no, head) in enumerate(ALSO):
        cx = 18 + (i // per) * 250
        cy = 848 + (i % per) * 14
        txt = "%d. %s" % (13 + i, head)
        f13 = fsr(13)
        while d.textlength(txt, font=f13) > 244 and len(txt) > 10:
            txt = txt[:-1]
        d.text((cx, cy), txt, font=f13, fill=(25, 25, 25))
    d.line([(18, 966), (1006, 966)], fill=ink, width=1)

    d.rectangle([18, 972, 1006, 1004], outline=(178, 34, 34), width=2)
    d.text((26, 978), "DATE CHECK - checked and left out:", font=F(AR_B, 12), fill=(178, 34, 34))
    dcx = [300, 545, 790]
    for i, item in enumerate(DATE_CHECK):
        d.text((dcx[i % 3], 978 + (i // 3) * 13), item, font=F(AR, 11), fill=(120, 20, 20))

    d.text((512, 1012),
           "Every story happened, or was first reported, on Monday 23 November 2026. "
           "Contested claims are attributed. Original drawings.",
           font=F(PF_IT, 12), fill=pal["sub"], anchor="mm")
    img.save(out, optimize=True)
    print(out, img.size)

if __name__ == "__main__":
    v = sys.argv[1] if len(sys.argv) > 1 else "A"
    o = sys.argv[2] if len(sys.argv) > 2 else "/tmp/ni23g3-final4/var-%s.png" % v
    render(v, o)

#!/usr/bin/env python3
"""Draw entry.png — "THE WORLD IN A DAY", a one-page poster summing up the
world news of Wednesday 18 November 2026.

Every story below was reported on 18 Nov 2026 and cross-checked in at least
two independent news roundups of that day (Reuters / AP / AFP-sourced
briefings; see README.md for the source list).

The poster is drawn at 2x (2048x2048) and downscaled to 1024x1024 so the
text stays crisp. Run:  python3 build_image.py   ->  writes entry.png
"""
from PIL import Image, ImageDraw, ImageFont

S = 2  # supersample factor
W = 1024 * S
PAPER = (246, 241, 231)
CARD = (255, 253, 247)
INK = (16, 28, 41)
BODY = (43, 58, 73)
NAVY = (20, 39, 61)
RED = (179, 49, 42)
BLUE = (29, 78, 121)
TEAL = (15, 106, 92)
PLUM = (109, 42, 93)
GOLD = (154, 123, 20)
GOLD_L = (251, 243, 217)
LINE = (217, 209, 186)
WHITE = (253, 251, 245)

FD = "/usr/share/fonts/truetype/noto/"
SERIF_BLACK = FD + "NotoSerif-Black.ttf"
SERIF_BOLD = FD + "NotoSerif-Bold.ttf"
SANS = FD + "NotoSans-Regular.ttf"
SANS_BOLD = FD + "NotoSans-Bold.ttf"
SANS_BLACK = FD + "NotoSans-Black.ttf"


def F(path, px):
    return ImageFont.truetype(path, px * S)


img = Image.new("RGB", (W, W), PAPER)
d = ImageDraw.Draw(img)


def text_w(txt, font):
    return d.textlength(txt, font=font)


def tracked(txt, cx, y, font, fill, ls):
    """Draw letter-spaced text centred on cx (logical px)."""
    widths = [d.textlength(ch, font=font) for ch in txt]
    total = sum(widths) + ls * S * (len(txt) - 1)
    x = cx * S - total / 2
    for ch, w in zip(txt, widths):
        d.text((x, y * S), ch, font=font, fill=fill)
        x += w + ls * S
    return total / S


def wrap(txt, font, max_w):
    words, lines, cur = txt.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if text_w(t, font) <= max_w * S or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def para(txt, x, y, font, fill, max_w, lh):
    for ln in wrap(txt, font, max_w):
        d.text((x * S, y * S), ln, font=font, fill=fill)
        y += lh
    return y


def rrect(x, y, w, h, fill=None, outline=None, width=1, radius=6):
    d.rounded_rectangle([x * S, y * S, (x + w) * S, (y + h) * S],
                        radius=radius * S, fill=fill, outline=outline,
                        width=width * S)


# ---------------------------------------------------------------- masthead
tracked("ONE DAY · ONE PAGE · THE WHOLE WORLD", 512, 30,
        F(SANS_BOLD, 19), RED, 5)
d.text((512 * S, 58 * S), "THE WORLD IN A DAY", font=F(SERIF_BLACK, 66),
       fill=INK, anchor="ma")
rrect(40, 142, 944, 56, fill=NAVY, radius=4)
tracked("WEDNESDAY · 18 NOVEMBER 2026", 512, 153, F(SANS_BOLD, 30), WHITE, 4)

# ---------------------------------------------------------------- hero
HY = 208
rrect(40, HY, 944, 230, fill=CARD, outline=NAVY, width=2, radius=6)
d.text((64 * S, (HY + 16) * S), "TOP STORY · SHENZHEN, CHINA — APEC SUMMIT",
       font=F(SANS_BOLD, 16), fill=RED)
hy = para("Trump, Xi & Putin Converge on Shenzhen", 64, HY + 42,
          F(SERIF_BLACK, 38), INK, 620, 45)
para("Xi Jinping hosted Vladimir Putin in Shenzhen as Donald Trump arrived "
     "for APEC, setting up the three leaders' first three-way summit — "
     "Ukraine, trade and Iran on the agenda.",
     64, hy + 6, F(SANS, 19), BODY, 620, 27)

pills = [("TRUMP", "UNITED STATES", BLUE), ("XI JINPING", "CHINA", RED),
         ("PUTIN", "RUSSIA", (91, 110, 140))]
px, pw = 716, 244
py = HY + 18
for name, country, col in pills:
    rrect(px, py, pw, 46, fill=col, radius=23)
    d.text(((px + pw / 2) * S, (py + 4) * S), name, font=F(SANS_BOLD, 18),
           fill=WHITE, anchor="ma")
    d.text(((px + pw / 2) * S, (py + 25) * S), country, font=F(SANS, 11),
           fill=(230, 233, 238), anchor="ma")
    py += 54
rrect(px, py + 2, pw, 40, fill=GOLD_L, outline=(201, 162, 39), width=2, radius=6)
d.text(((px + pw / 2) * S, (py + 11) * S), "FIRST THREE-WAY SUMMIT",
       font=F(SANS_BOLD, 14), fill=NAVY, anchor="ma")

# ---------------------------------------------------------------- icons
# Each icon is drawn on its own 100x100 device-px tile (a 50 logical-px box)
# in tile coordinates, then pasted — this keeps every coordinate consistent.
def _tile(draw_fn):
    t = Image.new("RGBA", (100, 100), (0, 0, 0, 0))
    draw_fn(ImageDraw.Draw(t))
    return t


def icon_bridge():
    def f(t):
        t.line([4, 84, 38, 84], fill=BLUE, width=6)
        t.line([62, 84, 96, 84], fill=BLUE, width=6)
        t.line([18, 84, 18, 30], fill=BLUE, width=6)
        t.line([82, 84, 82, 30], fill=BLUE, width=6)
        t.line([4, 22, 96, 22], fill=RED, width=6)
        t.arc([18, 18, 50, 66], 0, 90, fill=BLUE, width=6)
        t.arc([50, 18, 82, 66], 90, 180, fill=BLUE, width=6)
        t.line([44, 62, 52, 78], fill=RED, width=6)
        t.line([56, 62, 48, 78], fill=RED, width=6)
    return _tile(f)


def icon_missile():
    def f(t):
        body = [(58, 6), (84, 18), (90, 42), (64, 68), (42, 56), (50, 30)]
        t.polygon(body, fill=(243, 217, 213), outline=RED, width=6)
        t.line([42, 56, 24, 74], fill=RED, width=6)
        t.line([50, 30, 30, 22], fill=RED, width=6)
        t.line([24, 74, 8, 90], fill=GOLD, width=6)
        t.line([32, 68, 16, 82], fill=GOLD, width=6)
        t.ellipse([60, 22, 74, 36], fill=RED)
    return _tile(f)


def icon_capitol():
    def f(t):
        t.arc([18, 6, 82, 54], 180, 360, fill=NAVY, width=6)
        t.line([50, 2, 50, 10], fill=NAVY, width=6)
        t.line([8, 50, 92, 50], fill=NAVY, width=6)
        for cx in (24, 42, 58, 76):
            t.line([cx, 60, cx, 78], fill=NAVY, width=6)
        t.line([8, 88, 92, 88], fill=NAVY, width=6)
    return _tile(f)


def icon_virus():
    def f(t):
        for dx, dy in [(0, -30), (0, 30), (-30, 0), (30, 0), (-21, -21),
                       (21, -21), (-21, 21), (21, 21)]:
            t.line([50 + dx * 0.55, 50 + dy * 0.55, 50 + dx, 50 + dy],
                   fill=TEAL, width=6)
            t.ellipse([50 + dx - 6, 50 + dy - 6, 50 + dx + 6, 50 + dy + 6],
                      fill=TEAL)
        t.ellipse([32, 32, 68, 68], fill=(216, 239, 233), outline=TEAL,
                  width=6)
        t.ellipse([42, 42, 48, 48], fill=TEAL)
        t.ellipse([54, 52, 60, 58], fill=TEAL)
    return _tile(f)


def icon_shield():
    def f(t):
        pts = [(50, 6), (82, 18), (82, 48), (50, 90), (18, 48), (18, 18)]
        t.polygon(pts, fill=(240, 226, 236), outline=PLUM, width=6)
        t.line([50, 28, 50, 64], fill=RED, width=8)
        t.line([32, 46, 68, 46], fill=RED, width=8)
    return _tile(f)


def icon_chip():
    def f(t):
        for o in (34, 50, 66):
            t.line([o, 24, o, 10], fill=GOLD, width=6)
            t.line([o, 76, o, 90], fill=GOLD, width=6)
            t.line([24, o, 10, o], fill=GOLD, width=6)
            t.line([76, o, 90, o], fill=GOLD, width=6)
        t.rounded_rectangle([24, 24, 76, 76], radius=6, fill=GOLD_L,
                            outline=GOLD, width=6)
        t.rectangle([40, 40, 60, 60], outline=GOLD, width=6)
    return _tile(f)


# ---------------------------------------------------------------- cards
CARDS = [
    (icon_bridge(), BLUE, "UKRAINE · CRIMEA",
     "Strike Collapses Part of the Crimean Bridge",
     "Ukrainian drones and missiles hit the Kerch Bridge for a second day; "
     "a road arch fell into the strait, cars sent to ferries."),
    (icon_missile(), RED, "MIDDLE EAST · THE GULF",
     "Iran Fires on US Sites in Kuwait & Bahrain",
     "Tehran struck back after US jets hit a missile site on Qeshm Island; "
     "air defences reported interceptions, no major damage."),
    (icon_capitol(), BLUE, "UNITED STATES · ALASKA",
     "Peltola Flips Alaska — Senate Goes 56–44",
     "Democrat Mary Peltola beat Republican Dan Sullivan, sealing a 56–44 "
     "Democratic Senate majority."),
    (icon_virus(), TEAL, "AFRICA · HEALTH",
     "Ebola Passes 11,000 Cases in DR Congo",
     "The outbreak centred on Bunia and Beni keeps climbing — children "
     "under five are dying at the highest rates."),
    (icon_shield(), PLUM, "HEALTH · UNITED STATES",
     "US Loses Its Measles-Free Status",
     "After 26 years the US loses measles elimination status: 5,400+ cases "
     "and 10 deaths recorded in 2026."),
    (icon_chip(), GOLD, "BUSINESS · TECHNOLOGY",
     "Nvidia Posts a Record $115.8B Quarter",
     "Revenue more than doubled on AI data-centre demand; the chipmaker "
     "guided to about $130 billion next quarter."),
]
GY, CW, CH, GAP = 448, 466, 146, 12
for i, (icon, kc, kicker, head, body) in enumerate(CARDS):
    cx = 40 + (i % 2) * (CW + GAP)
    cy = GY + (i // 2) * (CH + GAP)
    rrect(cx, cy, CW, CH, fill=CARD, outline=LINE, width=2, radius=6)
    big = icon.resize((120, 120), Image.LANCZOS)
    img.paste(big, (int((cx + 9) * S), int((cy + 13) * S)), big)
    tx = cx + 80
    d.text((tx * S, (cy + 12) * S), kicker, font=F(SANS_BOLD, 14), fill=kc)
    hy = para(head, tx, cy + 32, F(SERIF_BOLD, 22), INK, CW - 96, 26)
    para(body, tx, hy + 3, F(SANS, 16), BODY, CW - 96, 21)

# ---------------------------------------------------------------- ticker
TY = GY + 3 * CH + 2 * GAP + 12
rrect(40, TY, 944, 54, fill=NAVY, radius=4)
ticker = ("ALSO ON WEDNESDAY:  COP31 climate talks open in Antalya, Türkiye  ·  "
          "Russia & Ukraine agree their largest prisoner swap  ·  Voyager 1 "
          "reaches one light-day from Earth  ·  Gold slides 2% to $3,770")
ty = TY + 8
for ln in wrap(ticker, F(SANS, 16), 912):
    d.text((512 * S, ty * S), ln, font=F(SANS, 16), fill=(243, 236, 217),
           anchor="ma")
    ty += 21

# ---------------------------------------------------------------- footer
FY = TY + 64
d.text((40 * S, FY * S), "Sources: Reuters · Associated Press · AFP · BBC · "
       "Alaska Public Media", font=F(SANS, 15), fill=(90, 102, 115))
d.text((984 * S, FY * S), "EVERY STORY REPORTED ON 18 NOV 2026",
       font=F(SANS_BOLD, 15), fill=NAVY, anchor="ra")

img = img.resize((1024, 1024), Image.LANCZOS)
img.save("entry.png", optimize=True)
print("wrote entry.png")

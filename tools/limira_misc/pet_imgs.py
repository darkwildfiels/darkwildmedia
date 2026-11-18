from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
F = "/usr/share/fonts/truetype/google-fonts/"
def lora(sz, it=False, w=600):
    f = ImageFont.truetype(F + ("Lora-Italic-Variable.ttf" if it else "Lora-Variable.ttf"), sz)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
pop = lambda sz, b=False: ImageFont.truetype(F + ("Poppins-Bold.ttf" if b else "Poppins-Regular.ttf"), sz)
CREAM = (251, 246, 238); NAVY = (43, 45, 66); GOLD = (176, 132, 72); TERRA = (178, 92, 66)
S = 2000
LB = "lb/"
STY = {
    "xmas": ("pet_xmas_4_salon.jpg", "Christmas", "Cozy fireplace & tree"),
    "royal": ("pet_royal_4_salon.jpg", "Royal", "Renaissance king or queen"),
    "memorial": ("pet_memorial_4_salon.jpg", "Memorial", "Rainbow bridge & clouds"),
    "water": ("pet_water_4_salon.jpg", "Watercolor", "Soft, airy & minimal"),
}
OUT = "pet_out/"; os.makedirs(OUT, exist_ok=True)

def ctext(d, y, t, f, fill):
    w = d.textlength(t, font=f); d.text(((S - w) / 2, y), t, font=f, fill=fill)

def art(key):
    # crop artwork from mockup (frame ~ x 600-1400, y 240-1440 at 2000px)
    return Image.open(LB + STY[key][0]).convert("RGB").crop((604, 244, 1396, 1436))

def cover(key, title, sub):
    im = Image.open(LB + STY[key][0]).convert("RGB")
    d = ImageDraw.Draw(im, "RGBA")
    d.rounded_rectangle((170, 1530, 1830, 1900), 36, fill=(251, 246, 238, 235))
    ctext(d, 1570, title, lora(84, w=700), NAVY)
    ctext(d, 1690, sub, pop(46), TERRA)
    ctext(d, 1775, "FROM YOUR PHOTO  •  FREE US SHIPPING", pop(40, True), GOLD)
    im.save(OUT + f"{key}_1_cover.jpg", quality=92)

def detail(key):
    a = art(key).resize((1340, 2016))
    im = Image.new("RGB", (S, S), CREAM); d = ImageDraw.Draw(im)
    im.paste(a.crop((0, 300, 1340, 1640)), (330, 330))
    d.rectangle((330, 330, 1670, 1670), outline=GOLD, width=6)
    ctext(d, 95, "Premium canvas, ready to hang", lora(84, it=True), NAVY)
    ctext(d, 1730, "Rich detail  •  Matte gallery wrap  •  Wooden stretcher bars", pop(48), NAVY)
    ctext(d, 1830, "Printed & shipped by our US print partner", pop(40), GOLD)
    im.save(OUT + f"{key}_2_detail.jpg", quality=92)

def how(key):
    im = Image.new("RGB", (S, S), CREAM); d = ImageDraw.Draw(im)
    ctext(d, 110, "How to order", lora(120, w=700), NAVY)
    ctext(d, 270, "Easy, personal and checked by us at every step", pop(46), TERRA)
    steps = [
        ("1", "Choose size & add to cart", "8 sizes, from 20x25 cm / 8x10\"\nto 61x91 cm / 24x36\""),
        ("2", "Upload a clear photo", "Use the photo upload box at checkout.\nAdd the pet's name if you'd like it on the art."),
        ("3", "Approve your preview", "We message you a digital preview in 24-48 h.\nOne free revision is included."),
        ("4", "We print & ship", "Printed on premium canvas after your approval.\nFree shipping to the US."),
    ]
    y = 430
    for n, h, t in steps:
        d.ellipse((220, y, 400, y + 180), fill=NAVY)
        w = d.textlength(n, font=lora(110, w=700)); d.text((310 - w / 2, y + 18), n, font=lora(110, w=700), fill=CREAM)
        d.text((460, y + 8), h, font=pop(64, True), fill=NAVY)
        d.multiline_text((460, y + 95), t, font=pop(42), fill=(90, 90, 100), spacing=10)
        y += 340
    ctext(d, 1830, "Tip: daylight photo, eyes visible, whole pet in frame", pop(40, True), GOLD)
    im.save(OUT + f"{key}_3_how.jpg", quality=92)

def styles(key):
    im = Image.new("RGB", (S, S), CREAM); d = ImageDraw.Draw(im)
    ctext(d, 90, "More styles in our shop", lora(100, w=700), NAVY)
    keys = list(STY)
    for i, k in enumerate(keys):
        x = 150 + (i % 2) * 880; y = 280 + (i // 2) * 800
        a = art(k).resize((500, 752)).crop((0, 0, 500, 640))
        im.paste(a, (x + 140, y))
        if k == key: d.rectangle((x + 132, y - 8, x + 648, y + 648), outline=TERRA, width=10)
        w = d.textlength(STY[k][1], font=pop(50, True))
        d.text((x + 390 - w / 2, y + 665), STY[k][1], font=pop(50, True), fill=NAVY)
    ctext(d, 1900, "Same photo upload & preview process for every style", pop(38), GOLD)
    im.save(OUT + f"{key}_4_styles.jpg", quality=92)

for key, t, s in [
    ("xmas", "Custom Christmas Pet Portrait", "Your dog or cat by the fireplace"),
    ("royal", "Custom Royal Pet Portrait", "Your pet as a Renaissance noble"),
    ("memorial", "Custom Pet Memorial Portrait", "Forever in our hearts"),
    ("water", "Custom Watercolor Pet Portrait", "Soft, timeless & minimal"),
]:
    cover(key, t, s); detail(key); how(key); styles(key)
print("ok")

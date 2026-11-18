"""Full mockup set for one artwork.
usage: python3 mockup2.py ART_2x3.png OUTDIR NAME
Rooms: flat (empty wall, true scale) + blank-canvas scenes (perspective warp).
"""
import sys, os
import numpy as np
from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance
Image.MAX_IMAGE_PIXELS = None
R = "/mnt/user-data/uploads/Documents/etsy-printify/gelen/odalar/"
art_p, OUT, NAME = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(OUT, exist_ok=True)
art = Image.open(art_p).convert("RGB")
UP = 3

# duz duvar odalari: ppi (orijinal px/inc), merkez x, kanvas alt kenari y (orijinal px), kadraj
FLAT = {
    "oda0_kemer": dict(ppi=11.2, cx=610, bottom=1027, size=(24, 36)),
    "oda1_salon": dict(ppi=10.5, cx=620, bottom=938, size=(24, 36)),
    "oda2_yatak": dict(ppi=10.7, cx=552, bottom=800, size=(24, 36)),
    "oda3_giris": dict(ppi=11.0, cx=560, bottom=886, size=(24, 36)),
    "oda4_ofis":  dict(ppi=19.0, cx=560, bottom=812, size=(24, 36)),
}
BLANK = ["oda5_yaslanmis", "oda6_aci_yemek", "oda7_aci_salon"]

def wall_shade(wall):
    lum = wall.mean(2)
    lum = np.asarray(Image.fromarray(np.clip(lum, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(4))).astype(float)
    ref = np.median(lum)
    return np.clip(1.0 + 0.30*(lum/ref - 1), 0.80, 1.08)[..., None]

def put(r, room, k, w_in, h_in, cx, bottom):
    W, H = round(w_in*k), round(h_in*k)
    x0 = round(cx - W/2); y0 = round(bottom - H)
    sh = Image.new("L", r.size, 0); sd = ImageDraw.Draw(sh); off = 0.9*k
    sd.rectangle([x0+off, y0+off*0.6, x0+W+off, y0+H+off], fill=150)
    sh = sh.filter(ImageFilter.GaussianBlur(1.6*k))
    r = Image.composite(Image.new("RGB", r.size, (70, 50, 30)), r, sh.point(lambda v: int(v*0.5)))
    wall = np.asarray(room.crop((x0, y0, x0+W, y0+H))).astype(float)
    a = np.asarray(art.resize((W, H), Image.LANCZOS)).astype(float)
    a = np.clip(a*wall_shade(wall)*np.array([1.0, 0.985, 0.955]), 0, 255).astype(np.uint8)
    cv = Image.fromarray(a); cd = ImageDraw.Draw(cv)
    cd.line([(W-1, 0), (W-1, H)], fill=(0, 0, 0), width=max(1, round(0.08*k)))
    r.paste(cv, (x0, y0))
    return r, (x0, y0, x0+W, y0+H)

def size_room(name, cfg, sizes=((12, 18), (20, 30), (24, 36)), gap_in=7):
    room0 = Image.open(R+name+".png").convert("RGB")
    room = room0.resize((room0.width*UP, room0.height*UP), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 40, 2))
    k = cfg["ppi"]*UP; r = room.copy()
    total = sum(w for w, h in sizes) + gap_in*(len(sizes)-1)
    x = cfg["cx"]*UP - total*k/2; bottom = cfg["bottom"]*UP
    F = "/usr/share/fonts/opentype/inter/"
    boxes = []
    for w, h in sizes:
        r, b = put(r, room, k, w, h, x + w*k/2, bottom); boxes.append((w, h, b)); x += (w+gap_in)*k
    d = ImageDraw.Draw(r)
    ft = ImageFont.truetype(F+"Inter-SemiBold.otf", int(2.6*k))
    for w, h, (x0, y0, x1, y1) in boxes:
        t = f"{w}x{h} in"; tw = d.textlength(t, font=ft)
        cx = (x0+x1)/2; ty = y0 - 4.5*k
        d.rounded_rectangle([cx-tw/2-1.4*k, ty-1.9*k, cx+tw/2+1.4*k, ty+1.9*k], radius=1.9*k, fill=(255, 255, 255))
        d.text((cx, ty), t, font=ft, fill=(40, 34, 28), anchor="mm")
    top = min(b[2][1] for b in boxes) - 15*k
    side = min(r.width, r.height)
    left = max(0, min(r.width-side, round(cfg["cx"]*UP - side/2))); top = max(0, min(r.height-side, round(top)))
    img = r.crop((left, top, left+side, top+side)).resize((2000, 2000), Image.LANCZOS)
    d = ImageDraw.Draw(img); fh = ImageFont.truetype(F+"Inter-SemiBold.otf", 54)
    d.rounded_rectangle([700, 1850, 1300, 1940], radius=45, fill=(255, 255, 255)); d.text((1000, 1895), "SIZE GUIDE", font=fh, fill=(40, 34, 28), anchor="mm")
    return img

def shown_tag(img, txt="Shown: 24x36 in"):
    d = ImageDraw.Draw(img); f = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-Medium.otf", 40)
    tw = d.textlength(txt, font=f)
    d.rounded_rectangle([60, img.height-130, 60+tw+60, img.height-60], radius=35, fill=(255, 255, 255))
    d.text((90, img.height-95), txt, font=f, fill=(40, 34, 28), anchor="lm")
    return img

def flat_room(name, cfg):
    room0 = Image.open(R+name+".png").convert("RGB")
    room = room0.resize((room0.width*UP, room0.height*UP), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 40, 2))
    k = cfg["ppi"]*UP; w_in, h_in = cfg["size"]
    W, H = round(w_in*k), round(h_in*k)
    x0 = round(cfg["cx"]*UP - W/2); y0 = round(cfg["bottom"]*UP - H)
    r = room.copy()
    sh = Image.new("L", r.size, 0); sd = ImageDraw.Draw(sh); off = 0.9*k
    sd.rectangle([x0+off, y0+off*0.6, x0+W+off, y0+H+off], fill=150)
    sh = sh.filter(ImageFilter.GaussianBlur(1.6*k))
    r = Image.composite(Image.new("RGB", r.size, (70, 50, 30)), r, sh.point(lambda v: int(v*0.5)))
    wall = np.asarray(room.crop((x0, y0, x0+W, y0+H))).astype(float)
    a = np.asarray(art.resize((W, H), Image.LANCZOS)).astype(float)
    a = np.clip(a*wall_shade(wall)*np.array([1.0, 0.985, 0.955]), 0, 255).astype(np.uint8)
    cv = Image.fromarray(a); cd = ImageDraw.Draw(cv)
    cd.line([(W-1, 0), (W-1, H)], fill=(0, 0, 0), width=max(1, round(0.08*k)))
    r.paste(cv, (x0, y0))
    # kare kadraj: kanvas yuksekligi ~%60
    side = min(round(H/0.60), r.width, r.height)
    left = min(max(0, round(x0+W/2-side/2)), r.width-side)
    top = min(max(0, round(y0 - side*0.12)), r.height-side)
    hero = r.crop((left, top, left+side, top+side)).resize((2000, 2000), Image.LANCZOS)
    return hero, r

def order_corners(pts):
    pts = np.array(pts, float); s = pts.sum(1); d = np.diff(pts, axis=1)[:, 0]
    return np.array([pts[np.argmin(s)], pts[np.argmin(d)], pts[np.argmax(s)], pts[np.argmax(d)]])  # tl,tr,br,bl

def find_face(img):
    """bos kanvasin on yuzu: notr-parlak en buyuk bilesen -> 4 koseli poligon"""
    import cv2
    from scipy import ndimage
    a = np.asarray(img).astype(int)
    m = ((a.min(2) > 222) & ((a.max(2)-a.min(2)) < 10)).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5*UP, 5*UP), np.uint8))
    lab, k = ndimage.label(m); sizes = ndimage.sum(m, lab, range(1, k+1))
    comp = (lab == np.argmax(sizes)+1).astype(np.uint8)
    cnts, _ = cv2.findContours(comp, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key=cv2.contourArea)
    ap = cv2.approxPolyDP(c, 0.02*cv2.arcLength(c, True), True).reshape(-1, 2)
    if len(ap) != 4:
        ap = cv2.boxPoints(cv2.minAreaRect(c))
    return order_corners(ap), comp

def homography(src, dst):
    A = []
    for (x, y), (u, v) in zip(src, dst):
        A += [[x, y, 1, 0, 0, 0, -u*x, -u*y], [0, 0, 0, x, y, 1, -v*x, -v*y]]
    h = np.linalg.solve(np.array(A, float), np.array(dst, float).reshape(-1))
    return np.append(h, 1).reshape(3, 3)

def blank_room(name):
    room0 = Image.open(R+name+".png").convert("RGB")
    room = room0.resize((room0.width*UP, room0.height*UP), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 40, 2))
    q, m = find_face(room)
    # yuz maskesi = 4 kose poligonu (biraz iceri)
    mask = Image.new("L", room.size, 0); ImageDraw.Draw(mask).polygon([tuple(p) for p in q], fill=255)
    mask = mask.filter(ImageFilter.MinFilter(3))
    # sanat -> dortgen (ters homografi ile)
    aw, ah = 1600, 2400
    src = art.resize((aw, ah), Image.LANCZOS)
    Hm = homography(q, [(0, 0), (aw, 0), (aw, ah), (0, ah)])  # dst->src
    coeffs = (Hm/Hm[2, 2]).reshape(-1)[:8]
    warped = src.transform(room.size, Image.PERSPECTIVE, tuple(coeffs), Image.BICUBIC)
    # sahnenin isigini koru: bos kanvasin parlakligi -> carpan
    base = np.asarray(room).astype(float)
    lum = base.mean(2, keepdims=True); ref = np.percentile(lum[np.asarray(mask) > 0], 90)
    shade = np.clip(lum/ref, 0.55, 1.08)
    tint = base/np.maximum(lum, 1)
    w = np.asarray(warped).astype(float)
    out = np.clip(w*shade*(0.88+0.12*tint), 0, 255).astype(np.uint8)
    r = Image.composite(Image.fromarray(out), room, mask)
    # kenar (yan yuz) boyamasi: tasarimin kenara tasan rengi (gallery wrap) -> kenar maskesini kanvasin ortalama kenar rengine yaklastir
    return r.resize((2000, round(2000*r.height/r.width)), Image.LANCZOS)

seq = {}
seq["oda0_kemer"], _ = flat_room("oda0_kemer", FLAT["oda0_kemer"])
seq["oda5_yaslanmis"] = blank_room("oda5_yaslanmis")
seq["oda7_aci_salon"] = blank_room("oda7_aci_salon")
seq["sizeroom"] = size_room("oda2_yatak", FLAT["oda2_yatak"])
# detay
aw, ah = art.size; cw = int(aw*0.86)
g0 = np.asarray(art.convert("L").resize((aw//40, ah//40))).astype(float)
ink = np.abs(g0 - np.median(g0))
c = cw//40; best, bx, by = -1, 0, 0
for yy in range(0, g0.shape[0]-c+1):
    for xx in range(0, g0.shape[1]-c+1):
        win = ink[yy:yy+c, xx:xx+c]
        sc = win.sum() - 3*ink[yy:yy+c, [xx, xx+c-1]].sum() - 3*ink[[yy, yy+c-1], xx:xx+c].sum()
        if sc > best: best, bx, by = sc, xx, yy
crop = art.crop((bx*40, by*40, bx*40+cw, by*40+cw)).resize((2000, 2000), Image.LANCZOS)
g = np.arange(2000)
weave = (np.sin(g[None, :]*1.6)*0.5 + np.sin(g[:, None]*1.6)*0.5)*3 + np.random.default_rng(1).normal(0, 2.5, (2000, 2000))
seq["detail"] = Image.fromarray(np.clip(np.asarray(crop).astype(float)+weave[..., None], 0, 255).astype(np.uint8))
order = [("01", "ana_gorsel", shown_tag(seq["oda0_kemer"])), ("02", "boyut_rehberi", seq["sizeroom"]), ("03", "yaslanmis", seq["oda5_yaslanmis"]),
         ("04", "detay", seq["detail"]), ("05", "aci_salon", seq["oda7_aci_salon"])]
for no, lab, im in order:
    im.convert("RGB").save(f"{OUT}/{no}_{NAME}_{lab}.jpg", quality=88)
print("ok", NAME)

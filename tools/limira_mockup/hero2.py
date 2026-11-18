"""Yeni 01 (yakin salon) ve 05 (yemek odasi). usage: hero2.py ART OUTDIR NAME"""
import sys
MODE = sys.argv[4] if len(sys.argv) > 4 else "crop"
src = open("mockup5.py").read().split("seq = {}")[0]
src = src.replace("art = Image.open(art_p).convert(\"RGB\")",
  "art = ImageEnhance.Contrast(ImageEnhance.Color(Image.open(art_p).convert('RGB')).enhance(1.10)).enhance(1.04)")
exec(src)
def blank_full(name):
    room0 = Image.open(R+name+".png").convert("RGB")
    room = room0.resize((room0.width*UP, room0.height*UP), Image.LANCZOS).filter(ImageFilter.UnsharpMask(2, 40, 2))
    q, m = find_face(room)
    mask = Image.new("L", room.size, 0); ImageDraw.Draw(mask).polygon([tuple(p) for p in q], fill=255)
    mask = mask.filter(ImageFilter.MinFilter(3))
    fw = (np.linalg.norm(q[1]-q[0])+np.linalg.norm(q[2]-q[3]))/2; fh = (np.linalg.norm(q[3]-q[0])+np.linalg.norm(q[2]-q[1]))/2
    ra = fw/fh; A = art; w0, h0 = A.size
    if MODE == "pad":
        nw = round(h0*ra); bg = A.getpixel((4, 4)); c = Image.new("RGB", (max(nw, w0), h0), bg); c.paste(A, ((c.width-w0)//2, 0)); A = c
    else:
        nh = round(w0/ra); y = max(0, (h0-nh)//2); A = A.crop((0, y, w0, y+min(nh, h0)))
    ah = 3000; aw = round(ah*ra)
    s = A.resize((aw, ah), Image.LANCZOS)
    Hm = homography(q, [(0, 0), (aw, 0), (aw, ah), (0, ah)])
    warped = s.transform(room.size, Image.PERSPECTIVE, tuple((Hm/Hm[2, 2]).reshape(-1)[:8]), Image.BICUBIC)
    base = np.asarray(room).astype(float); lum = base.mean(2, keepdims=True)
    ref = np.percentile(lum[np.asarray(mask) > 0], 90)
    shade = np.clip(lum/ref, 0.70, 1.05)          # daha az soldurma
    w = np.asarray(warped).astype(float)
    out = np.clip(w*(0.25+0.75*shade), 0, 255).astype(np.uint8)
    comp = np.asarray(Image.composite(Image.fromarray(out), room, mask)).astype(float)
    # yan kenarlar: yuzun yanindaki notr-parlak (beyaz kanvas) pikselleri -> en yakin yuz pikselinin rengi * golge orani
    from scipy import ndimage
    fm = np.asarray(mask) > 0
    fw_px = max(q[:, 0].max()-q[:, 0].min(), 1)
    near = ndimage.binary_dilation(fm, iterations=int(fw_px*0.09)) & ~fm
    b = base
    neutral = (b.min(2) > 90) & ((b.max(2)-b.min(2)) < 0.17*b.max(2))
    side = near & neutral
    lab, n = ndimage.label(side)
    if n:
        sz = ndimage.sum(side, lab, range(1, n+1))
        side = np.isin(lab, [i+1 for i, v in enumerate(sz) if v > 0.002*fm.sum()])
    side = ndimage.binary_closing(side, iterations=3) & near
    yy, xx = np.mgrid[0:side.shape[0], 0:side.shape[1]]
    (x1_, y1_), (x2_, y2_) = q[1], q[2]
    t = np.clip((yy - y1_)/max(y2_-y1_, 1), 0, 1); xr = x1_ + t*(x2_-x1_)
    side &= (xx > xr - 2) & (xx < xr + fw_px*0.07) & (yy > y1_ - 5) & (yy < y2_ + 5)
    _, (iy, ix) = ndimage.distance_transform_edt(~fm, return_indices=True)
    ys, xs = np.nonzero(side)
    ny, nx = iy[ys, xs], ix[ys, xs]
    ratio = (b[ys, xs].mean(1) / np.maximum(b[ny, nx].mean(1), 1))[:, None]
    # ayna: kenardan disari mesafe kadar iceriden ornekle
    my = np.clip(ny - (ys-ny)*2, 0, comp.shape[0]-1); mx = np.clip(nx - (xs-nx)*2, 0, comp.shape[1]-1)
    ok = fm[my, mx]; my = np.where(ok, my, ny); mx = np.where(ok, mx, nx)
    comp[ys, xs] = np.clip(comp[my, mx] * np.clip(ratio*1.05, 0.45, 1.0) * 0.9, 0, 255)
    thin = ndimage.binary_dilation(fm, iterations=max(2, int(fw_px*0.012))) & ~fm & ~side & (b.min(2) > 200) & ((b.max(2)-b.min(2)) < 0.08*b.max(2))
    ys, xs = np.nonzero(thin); ny, nx = iy[ys, xs], ix[ys, xs]
    comp[ys, xs] = np.clip(comp[ny, nx]*0.8, 0, 255)
    return Image.fromarray(comp.astype(np.uint8)), q
r, q = blank_full("oda7_aci_salon")
x0, y0 = q[:, 0].min(), q[:, 1].min(); x1, y1 = q[:, 0].max(), q[:, 1].max()
H = y1 - y0; side = int(min(H/0.70, r.width, r.height))
cx = (x0+x1)/2; left = int(min(max(0, cx - side*0.56), r.width-side)); top = int(max(0, min(y0 - side*0.07, r.height-side)))
r.crop((left, top, left+side, top+side)).resize((2000, 2000), Image.LANCZOS).save(f"{OUT}/01_{NAME}_ana_gorsel.jpg", quality=92)
r6, q6 = blank_full("oda6_aci_yemek")
r6.resize((2000, round(2000*r6.height/r6.width)), Image.LANCZOS).save(f"{OUT}/05_{NAME}_yemek_odasi.jpg", quality=90)
if MODE == "crop":
    w0, h0 = art.size; nh = round(w0*1.5); y = max(0, (h0-nh)//2); art = art.crop((0, y, w0, y+min(nh, h0)))
h3, _ = flat_room("oda0_kemer", FLAT["oda0_kemer"])
h3.save(f"{OUT}/03_{NAME}_kemer_oda.jpg", quality=90)
print("ok", NAME)

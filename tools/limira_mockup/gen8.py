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
    _c = q.mean(0); q = _c + (q-_c)*np.array([1.012, 1.018])
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
    b = base; H_, W_ = fm_shape = b.shape[:2]
    fm = np.asarray(mask) > 0
    fw_px = max(q[:, 0].max()-q[:, 0].min(), 1)
    D = int(fw_px*0.09)
    # sag yan yuz: her satirda yuz kenarindan duvara kadar
    (x1_, y1_), (x2_, y2_) = q[1], q[2]
    for y in range(int(min(y1_, y2_))-int(fw_px*0.012), int(max(y1_, y2_))+int(fw_px*0.012)):
        if y < 0 or y >= H_: continue
        rows_f = np.nonzero(fm.any(1))[0]
        yc = int(np.clip(y, rows_f.min(), rows_f.max()))
        xs_ = np.nonzero(fm[yc])[0]
        xr = xs_.max() if len(xs_) else int(x1_)
        ref = np.median(b[y, min(W_-1, xr+int(D*1.3)):min(W_, xr+int(D*1.8))], axis=0) if xr+int(D*1.8) < W_ else None
        if ref is None: continue
        end = xr
        for x in range(xr+1, min(W_, xr+D)):
            if np.abs(b[y, x]-ref).sum() < 24 and np.abs(b[y, min(W_-1, x+2)]-ref).sum() < 24: break
            end = x
        if end <= xr or not len(xs_): continue
        for x in range(xr+1, end+1):
            px = b[y, x]
            if not ((px.max()-px.min()) < 0.12*px.max() and px.min() > 120): continue
            d = x - xr; sx = max(xs_.min(), xr - d*2)
            comp[y, x] = comp[yc, sx]*0.80
    from scipy import ndimage
    painted = fm.copy()
    diff = np.abs(comp - b).sum(2) > 1
    painted |= diff
    whitec = (b.min(2) > 190) & ((b.max(2)-b.min(2)) < 0.07*b.max(2))
    for it in range(3):
        ring = ndimage.binary_dilation(painted, iterations=max(3, int(fw_px*0.03))) & ~painted
        tgt = ring & whitec
        if not tgt.any(): break
        _, (iy, ix) = ndimage.distance_transform_edt(~painted, return_indices=True)
        ys, xs = np.nonzero(tgt); ny, nx = iy[ys, xs], ix[ys, xs]
        comp[ys, xs] = comp[ny, nx]*0.85
        painted[ys, xs] = True
    return Image.fromarray(comp.astype(np.uint8)), q

def sq(img, side=2000): return img.resize((side, side), Image.LANCZOS) if img.width==img.height else img
def crop_sq(r, q, frac=0.66):
    x0, y0 = q[:, 0].min(), q[:, 1].min(); x1, y1 = q[:, 0].max(), q[:, 1].max()
    H = y1-y0; side = int(min(H/frac, r.width, r.height)); cx=(x0+x1)/2
    left = int(min(max(0, cx-side*0.55), r.width-side)); top = int(max(0, min(y0-side*0.08, r.height-side)))
    return r.crop((left, top, left+side, top+side)).resize((2000, 2000), Image.LANCZOS)
out = {}
r, q = blank_full("oda7_aci_salon"); out["1_salon_yakin"] = crop_sq(r, q, 0.70)
r6, q6 = blank_full("oda6_aci_yemek"); out["7_yemek"] = crop_sq(r6, q6, 0.55)
# duz odalar icin 2:3 sanat
if MODE == "crop":
    w0, h0 = art.size; nh = round(w0*1.5); y = max(0, (h0-nh)//2); art = art.crop((0, y, w0, y+min(nh, h0)))
else:
    w0, h0 = art.size; nw = round(h0/1.5)
    if nw > w0:
        c = Image.new("RGB", (nw, h0), art.getpixel((4, 4))); c.paste(art, ((nw-w0)//2, 0)); art = c
out["2_boyut"] = size_room("oda2_yatak", FLAT["oda2_yatak"])
for key, room in [("3_kemer", "oda0_kemer"), ("4_salon", "oda1_salon"), ("5_giris", "oda3_giris"), ("6_ofis", "oda4_ofis")]:
    out[key], _ = flat_room(room, FLAT[room])
aw, ah = art.size; cw = int(aw*0.80)
g0 = np.asarray(art.convert("L").resize((aw//40, ah//40))).astype(float); ink = np.abs(g0-np.median(g0)); c = cw//40; best, bx, by = -1, 0, 0
for yy in range(0, g0.shape[0]-c+1):
    for xx in range(0, g0.shape[1]-c+1):
        sc = ink[yy:yy+c, xx:xx+c].sum()
        if sc > best: best, bx, by = sc, xx, yy
crop = art.crop((bx*40, by*40, bx*40+cw, by*40+cw)).resize((2000, 2000), Image.LANCZOS)
g = np.arange(2000); weave = (np.sin(g[None, :]*1.6)*0.5+np.sin(g[:, None]*1.6)*0.5)*2.5
out["8_detay"] = Image.fromarray(np.clip(np.asarray(crop).astype(float)+weave[..., None], 0, 255).astype(np.uint8))
for k, im in out.items():
    im.convert("RGB").save(f"{OUT}/{k}.jpg", quality=93)
print("ok", NAME, len(out))

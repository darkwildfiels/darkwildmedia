from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys
SH=int(sys.argv[1]); Y1=int(sys.argv[2])
F="/usr/share/fonts/truetype/google-fonts/"
def lora(sz,w=500,italic=False):
    f=ImageFont.truetype(F+("Lora-Italic-Variable.ttf" if italic else "Lora-Variable.ttf"),sz)
    try:f.set_variation_by_axes([w])
    except:pass
    return f
pop=lambda sz,b=False: ImageFont.truetype(F+("Poppins-Bold.ttf" if b else "Poppins-Regular.ttf"),sz)
S=2; W,H=3360*S,840*S
BG=(244,237,227); INK=(52,44,38); ACC=(160,120,84); LINE=(196,176,150)
b=Image.new("RGB",(W,H),BG); d=ImageDraw.Draw(b)
top,bot=230*S,742*S; gap=26*S; side=40*S
pw=(W-2*side-3*gap)//4; ph=bot-top; r=pw/ph
def room(k):
    import numpy as np
    src=Image.open(f'lb/{k}.jpg').convert('RGB'); a=np.asarray(src).astype(float)
    sw=int(SH*r); pad=max((sw-2000)//2,0)
    def fill(strip):
        m=strip.mean(1)  # per-row mean
        from scipy.ndimage import uniform_filter1d
        m=uniform_filter1d(m,9,axis=0)
        blk=np.repeat(m[:,None,:],pad,1)
        noise=np.random.default_rng(1).normal(0,2.2,blk.shape)
        return np.clip(blk+noise,0,255)
    L=fill(a[:,545:575]); R=fill(a[:,-30:])
    # soft blend 60px
    out=np.concatenate([L,a,R],1)
    for j in range(60):
        t=j/60
        out[:,pad+j]=out[:,pad+j]*t+L[:,-1]*(1-t)
        out[:,pad+1999-j]=out[:,pad+1999-j]*t+R[:,0]*(1-t)
    im=Image.fromarray(out.astype('uint8'))
    x0=(im.width-sw)//2
    return im.crop((x0,Y1-SH,x0+sw,Y1))
PICKS=[('pet_royal_4_salon','PERSONALIZED'),('1_4_salon',None),('pet_water_4_salon','FROM YOUR PHOTO'),('voltaire_4_salon',None)]
for i,(k,badge) in enumerate(PICKS):
    crop=room(k).resize((pw,ph),Image.LANCZOS)
    m=Image.new("L",(pw,ph),0); md=ImageDraw.Draw(m); rad=pw//2
    md.rectangle([0,rad*0.55,pw,ph],fill=255); md.ellipse([0,0,pw,rad*1.1],fill=255)
    x=side+i*(pw+gap)
    sh_=m.filter(ImageFilter.GaussianBlur(14*S))
    b.paste(Image.new("RGB",(pw,ph),(170,150,128)),(x+6*S,top+10*S),sh_.point(lambda v:int(v*0.45)))
    b.paste(crop,(x,top),m)
    if badge:
        fb=pop(22*S,True); bw=d.textlength(badge,font=fb)+60*S; bx=x+pw-bw-28*S; by=bot-70*S
        d.rounded_rectangle([bx,by,bx+bw,by+46*S],radius=23*S,fill=(160,120,84)); d.text((bx+30*S,by+8*S),badge,font=fb,fill=(250,245,238))
t1="Limira"; t2="Collection"; f1=lora(120*S,500); f2=lora(120*S,500,italic=True)
w1=d.textlength(t1,font=f1); w2=d.textlength(" "+t2,font=f2); x=(W-(w1+w2))/2
d.text((x,22*S),t1,font=f1,fill=INK); d.text((x+w1,22*S)," "+t2,font=f2,fill=ACC)
tag="   ".join(" ".join(w) for w in "CUSTOM PET PORTRAITS & CANVAS WALL ART".split()); ft=pop(25*S); tw=d.textlength(tag,font=ft); ty=176*S
d.text(((W-tw)/2,ty),tag,font=ft,fill=INK)
d.line([((W-tw)/2-260*S,ty+17*S),((W-tw)/2-40*S,ty+17*S)],fill=LINE,width=2*S)
d.line([((W+tw)/2+40*S,ty+17*S),((W+tw)/2+260*S,ty+17*S)],fill=LINE,width=2*S)
d.rectangle([0,bot+10*S,W,H],fill=(236,226,212))
feats=["CUSTOM FROM YOUR PHOTO","FREE SHIPPING","PREMIUM CANVAS, READY TO HANG","PERFECT GIFT"]
ff=pop(24*S); cy=bot+(H-bot)/2+4*S; seg=W/4
for i,f_ in enumerate(feats):
    cx=seg*i+seg/2; txt="   ".join(" ".join(w) for w in f_.split()); fw=d.textlength(txt,font=ff); dx=cx-fw/2
    ix=dx-34*S; d.polygon([(ix,cy),(ix+10*S,cy-10*S),(ix+20*S,cy),(ix+10*S,cy+10*S)],outline=ACC,width=3*S)
    d.text((dx,cy-17*S),txt,font=ff,fill=INK)
    if i: d.line([(seg*i,cy-20*S),(seg*i,cy+20*S)],fill=LINE,width=2*S)
b.resize((3360,840),Image.LANCZOS).save('limira_banner_v2.jpg',quality=93)

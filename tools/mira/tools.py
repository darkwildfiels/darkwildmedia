"""Mira Digital product tools: clean line art, colorize preview, build PDFs and listing images."""
import sys, os, random, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy import ndimage
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

CREAM=(251,246,238); INK=(43,45,66); CORAL=(224,122,95); SAGE=(129,178,154); MUST=(242,204,143); LAV=(181,167,214)
PASTELS=[(244,170,150),(160,205,180),(246,214,150),(196,184,228),(170,200,230),(240,190,210),(205,225,160),(250,230,190),(180,215,215)]
F="/usr/share/fonts/truetype/google-fonts/"
HERE=os.path.dirname(os.path.abspath(__file__))
def lora(sz,w=700):
    f=ImageFont.truetype(F+"Lora-Variable.ttf",sz)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
def pop(sz,b=False): return ImageFont.truetype(F+("Poppins-Bold.ttf" if b else "Poppins-Regular.ttf"),sz)

# ---------- cleaning ----------
def clean(src, dst, H=3300):
    im=Image.open(src).convert("L")
    # trim outer white
    a=np.array(im); mask=a<200
    ys,xs=np.where(mask)
    if len(xs):
        pad=int(0.02*max(a.shape))
        im=im.crop((max(0,xs.min()-pad),max(0,ys.min()-pad),min(a.shape[1],xs.max()+pad),min(a.shape[0],ys.max()+pad)))
    s=H/im.height
    im=im.resize((round(im.width*s),H),Image.LANCZOS).filter(ImageFilter.GaussianBlur(1.2))
    b=im.point(lambda v:0 if v<150 else 255).convert("L")
    b.save(dst,optimize=True)
    return dst

# ---------- colored preview ----------
def colorize(src, dst, seed=1, frac=0.75):
    rnd=random.Random(seed)
    a=np.array(Image.open(src).convert("L"))
    white=a>128
    lab,n=ndimage.label(white)
    sizes=ndimage.sum(white,lab,range(1,n+1))
    # background = region touching border
    border=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))
    out=np.stack([a,a,a],-1).astype(np.uint8)
    total=white.size
    lut=np.zeros((n+1,3),np.uint8); use=np.zeros(n+1,bool)
    for i in range(1,n+1):
        if i in border: continue
        sz=sizes[i-1]
        if sz<total*0.00008: continue
        if rnd.random()<frac:
            lut[i]=rnd.choice(PASTELS); use[i]=True
    m=use[lab]
    out[m]=lut[lab][m]
    Image.fromarray(out).save(dst,quality=92)
    return dst

# ---------- PDF ----------
def pdf(pages, dst, size="letter", title="Coloring Pages", logo=os.path.join(HERE,"mira_logo_1000.png")):
    ps=letter if size=="letter" else A4
    W,Hh=ps; c=canvas.Canvas(dst,pagesize=ps); c.setTitle(title); c.setAuthor("Mira Digital")
    # cover
    c.setFillColorRGB(*[v/255 for v in CREAM]); c.rect(0,0,W,Hh,fill=1,stroke=0)
    c.drawImage(ImageReader(logo),W/2-90,Hh-260,180,180,mask='auto')
    c.setFillColorRGB(*[v/255 for v in INK]); c.setFont("Helvetica-Bold",24)
    for k,line in enumerate(wrap(title,32)): c.drawCentredString(W/2,Hh-320-k*30,line)
    c.setFont("Helvetica",12)
    y=Hh-320-len(wrap(title,32))*30-20
    for t in [f"{len(pages)} printable coloring pages","Print at 100% (actual size) or 'fit to page'.","Tip: thicker paper or cardstock works great for markers.","","For personal, non-commercial use only. Please do not resell or share the files.","Thank you for supporting our small studio!  -  Mira Digital"]:
        c.drawCentredString(W/2,y,t); y-=20
    c.showPage()
    m=36
    for p in pages:
        im=Image.open(p); iw,ih=im.size
        s=min((W-2*m)/iw,(Hh-2*m-14)/ih); dw,dh=iw*s,ih*s
        c.drawImage(ImageReader(im),(W-dw)/2,(Hh-dh)/2+7,dw,dh)
        c.setFont("Helvetica",7); c.setFillColorRGB(.6,.6,.6)
        c.drawCentredString(W/2,16,"© Mira Digital  ·  personal use only")
        c.showPage()
    c.save(); return dst

def wrap(t,n):
    w=t.split(); lines=[]; cur=""
    for x in w:
        if len(cur)+len(x)+1>n: lines.append(cur); cur=x
        else: cur=(cur+" "+x).strip()
    lines.append(cur); return lines

# ---------- listing images (2000x2000 -> saved 2000x1600 4:5? Etsy prefers 2000x2000 / 4:3) ----------
LW,LH=2700,2025  # 4:3 landscape, Etsy thumbnail friendly
def paper(img, w, shadow=True, rot=0):
    im=Image.open(img).convert("RGB") if isinstance(img,str) else img.convert("RGB")
    h=round(w*11/8.5)
    pg=Image.new("RGB",(w,h),(255,255,255))
    s=min((w*0.9)/im.width,(h*0.9)/im.height); t=im.resize((round(im.width*s),round(im.height*s)),Image.LANCZOS)
    pg.paste(t,((w-t.width)//2,(h-t.height)//2))
    pg=pg.convert("RGBA")
    if rot: pg=pg.rotate(rot,expand=True,resample=Image.BICUBIC)
    if not shadow: return pg
    sh=Image.new("RGBA",(pg.width+80,pg.height+80),(0,0,0,0))
    alpha=pg.split()[3].point(lambda v:90 if v>0 else 0)
    blk=Image.new("RGBA",pg.size,(40,30,20,255)); blk.putalpha(alpha)
    sh.paste(blk,(50,55),blk); sh=sh.filter(ImageFilter.GaussianBlur(18))
    sh.paste(pg,(30,30),pg); return sh

def bg():
    b=Image.new("RGB",(LW,LH),CREAM); d=ImageDraw.Draw(b); rnd=random.Random(3)
    for _ in range(70):
        x,y=rnd.randint(0,LW),rnd.randint(0,LH); r=rnd.randint(6,16)
        if 230<x<LW-230 and 110<y<LH-110: continue
        d.ellipse([x-r,y-r,x+r,y+r],fill=rnd.choice([CORAL,SAGE,MUST,LAV]))
    return b

def badge(d,x,y,text,fill=CORAL,fg=CREAM,size=60):
    f=pop(size,True); w=d.textlength(text,font=f)
    d.rounded_rectangle([x,y,x+w+80,y+size+50],radius=(size+50)//2,fill=fill); d.text((x+40,y+18),text,font=f,fill=fg)
    return w+80

def cover(pages, title, sub, dst, count_label=None, colored=None):
    b=bg(); d=ImageDraw.Draw(b)
    imgs=list(pages)[:5]
    n=len(imgs); pw=760
    xs=[LW/2-pw/2+(i-(n-1)/2)*330 for i in range(n)]
    rots=[8,4,0,-4,-8][:n] if n==5 else [6*(i-(n-1)/2)*-1 for i in range(n)]
    order=sorted(range(n),key=lambda i:-abs(i-(n-1)/2))
    for i in order:
        src=colored[i] if (colored and i==(n-1)//2) else imgs[i]
        p=paper(src,pw,rot=rots[i]); b.paste(p,(int(xs[i]-40),int(400+abs(i-(n-1)/2)*40)),p)
    # header band
    d.rectangle([0,0,LW,400],fill=CREAM)
    f=lora(130); tl=wrap(title,30)
    y=40
    for line in tl[:2]:
        w=d.textlength(line,font=f); d.text(((LW-w)/2,y),line,font=f,fill=INK); y+=140
    f2=pop(62); w=d.textlength(sub,font=f2); d.text(((LW-w)/2,y+10),sub,font=f2,fill=CORAL)
    # badges bottom
    d.rectangle([0,LH-190,LW,LH],fill=INK)
    items=[count_label or f"{len(pages)} PAGES","INSTANT DOWNLOAD","US LETTER + A4","PRINT AT HOME"]
    f3=pop(56,True); tot=sum(d.textlength(t,font=f3) for t in items)+ (len(items)-1)*140
    x=(LW-tot)/2
    for k,t in enumerate(items):
        d.text((x,LH-135),t,font=f3,fill=CREAM); x+=d.textlength(t,font=f3)
        if k<len(items)-1: d.ellipse([x+55,LH-105,x+85,LH-75],fill=MUST); x+=140
    b.save(dst,quality=90); return dst

def single(img, dst, caption, colored=None):
    b=bg(); d=ImageDraw.Draw(b)
    if colored:
        p1=paper(img,980,rot=4); p2=paper(colored,980,rot=-3)
        b.paste(p1,(170,170),p1); b.paste(p2,(1450,190),p2)
        f=pop(64,True); d.text((640-d.textlength("Print it",font=f)/2,1640),"Print it",font=f,fill=INK); t2="Color it your way"; d.text((1960-d.textlength(t2,font=f)/2,1640),t2,font=f,fill=CORAL)
    else:
        p=paper(img,1250); b.paste(p,((LW-p.width)//2,50),p)
    f=lora(70); w=d.textlength(caption,font=f)
    if not colored: d.rounded_rectangle([(LW-w)/2-50,LH-150,(LW+w)/2+50,LH-40],radius=55,fill=CREAM); d.text(((LW-w)/2,LH-140),caption,font=f,fill=INK)
    b.save(dst,quality=90); return dst

def grid(pages, dst, title):
    b=bg(); d=ImageDraw.Draw(b)
    f=lora(110); w=d.textlength(title,font=f); d.text(((LW-w)/2,50),title,font=f,fill=INK)
    n=len(pages); cols=3 if n<=6 else (5 if n<=10 else 6); rows=math.ceil(n/cols)
    cw=(LW-200)/cols; ch=(LH-300)/rows; pw=int(min(cw*0.9,ch*0.88*8.5/11))
    for i,p in enumerate(pages):
        r,cc=divmod(i,cols); im=paper(p,pw)
        x=100+cc*cw+(cw-im.width)/2; y=230+r*ch+(ch-im.height)/2
        b.paste(im,(int(x),int(y)),im)
        f2=pop(40,True); (d.text((x+40,y+im.height-30),str(i+1),font=f2,fill=CORAL) if n<=15 else d.text((x+45,y+35),str(i+1),font=pop(34,True),fill=CORAL))
    b.save(dst,quality=90); return dst

def info(dst, lines_title, rows):
    b=bg(); d=ImageDraw.Draw(b)
    f=lora(120); w=d.textlength(lines_title,font=f); d.text(((LW-w)/2,110),lines_title,font=f,fill=INK)
    y=420
    for k,(h,t) in enumerate(rows):
        d.ellipse([300,y,440,y+140],fill=[CORAL,SAGE,MUST,LAV][k%4]); f2=pop(70,True); s=str(k+1); ww=d.textlength(s,font=f2); d.text((370-ww/2,y+25),s,font=f2,fill=CREAM)
        d.text((520,y),h,font=pop(66,True),fill=INK); d.text((520,y+85),t,font=pop(48),fill=INK)
        y+=330
    b.save(dst,quality=90); return dst

def before_after(photo, page, dst, caption="Printable line art of your pet", title="Your photo, made into a coloring page", colored=None):
    b=bg(); d=ImageDraw.Draw(b)
    f=lora(100); w=d.textlength(title,font=f); d.text(((LW-w)/2,60),title,font=f,fill=INK)
    ph=Image.open(photo).convert("RGB"); ph.thumbnail((1050,1400))
    fr=Image.new("RGB",(ph.width+40,ph.height+40),(255,255,255)); fr.paste(ph,(20,20)); fr=fr.rotate(3,expand=True,fillcolor=CREAM)
    b.paste(fr,(140,330))
    p=paper(colored or page,1050,rot=-2); b.paste(p,(LW-p.width-120,250),p)
    # arrow
    ax=1290; ay=1150; d.polygon([(ax-80,ay-60),(ax+60,ay),(ax-80,ay+60)],fill=CORAL)
    d.rectangle([ax-200,ay-22,ax-70,ay+22],fill=CORAL)
    f2=pop(52,True); d.text((260,LH-150),"Example photo",font=f2,fill=INK); t=caption; d.text((LW-d.textlength(t,font=f2)-180,LH-150),t,font=f2,fill=CORAL)
    b.save(dst,quality=90); return dst

def custom_pdf(dst, kind="pet"):
    W,Hh=letter; c=canvas.Canvas(dst,pagesize=letter); c.setTitle("Thank you - Mira Digital"); c.setAuthor("Mira Digital")
    c.setFillColorRGB(*[v/255 for v in CREAM]); c.rect(0,0,W,Hh,fill=1,stroke=0)
    c.drawImage(ImageReader(os.path.join(HERE,"mira_logo_1000.png")),W/2-80,Hh-230,160,160,mask='auto')
    c.setFillColorRGB(*[v/255 for v in INK]); c.setFont("Helvetica-Bold",24); c.drawCentredString(W/2,Hh-280,"Thank you for your order!")
    what="your pet" if kind=="pet" else "your family or home"
    lines=["Your custom coloring page is made just for you, so it will be",
           "sent to you through Etsy (Messages / Purchases) - not in this file.","",
           "What happens next:",
           f"1. Send us a clear, well-lit photo of {what} through Etsy Messages",
           "   (if you haven't already), plus any name or date you'd like added.",
           "2. We send you a preview within 24-48 hours.",
           "3. One round of edits is included free.",
           "4. You receive your printable PDF (US Letter + A4) through Etsy.","",
           "Questions? Message us any time - we usually reply within 24 hours.","",
           "Your photo is used only for your order and deleted 30 days after completion.",
           "Personal, non-commercial use only.  -  Mira Digital"]
    c.setFont("Helvetica",12.5); y=Hh-330
    for t in lines: c.drawString(90,y,t); y-=21
    c.showPage(); c.save(); return dst

def cover2(pages, title, sub, dst, count_label=None, colored=None, items=None):
    """Big-hero cover: center page (colored) fills most of the height; 2 side pages peek."""
    b=bg(); d=ImageDraw.Draw(b)
    imgs=list(pages)[:5]; n=len(imgs); mid=(n-1)//2
    left=imgs[0] if n>1 else None; right=imgs[-1] if n>1 else None
    hero=(colored[mid] if colored and colored[mid] is not None else imgs[mid])
    top=255; bottom=LH-150
    hw=int((bottom-top-40)*8.5/11)
    sw=int(hw*0.78)
    if left is not None:
        p=paper(left,sw,rot=7); b.paste(p,(int(LW/2-hw/2-sw*0.72),top+90),p)
    if right is not None:
        p=paper(right,sw,rot=-7); b.paste(p,(int(LW/2+hw/2-sw*0.28),top+90),p)
    p=paper(hero,hw); b.paste(p,(int(LW/2-p.width/2),top+10),p)
    d.rectangle([0,0,LW,top],fill=CREAM)
    f=lora(112); line=wrap(title,40)[0]
    w=d.textlength(line,font=f); d.text(((LW-w)/2,22),line,font=f,fill=INK)
    f2=pop(56); w=d.textlength(sub,font=f2); d.text(((LW-w)/2,160),sub,font=f2,fill=CORAL)
    d.rectangle([0,LH-150,LW,LH],fill=INK)
    items=items or [count_label or f"{len(pages)} PAGES","INSTANT DOWNLOAD","US LETTER + A4","PRINT AT HOME"]
    f3=pop(50,True); tot=sum(d.textlength(t,font=f3) for t in items)+(len(items)-1)*130
    x=(LW-tot)/2
    for k,t in enumerate(items):
        d.text((x,LH-108),t,font=f3,fill=CREAM); x+=d.textlength(t,font=f3)
        if k<len(items)-1: d.ellipse([x+50,LH-82,x+80,LH-52],fill=MUST); x+=130
    b.save(dst,quality=90); return dst

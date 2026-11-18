from PIL import Image, ImageDraw, ImageFont
import math
CREAM=(251,246,238); INK=(43,45,66); CORAL=(224,122,95); SAGE=(129,178,154); MUST=(242,204,143); LAV=(181,167,214)
F="/usr/share/fonts/truetype/google-fonts/"
def lora(sz,w=600):
    f=ImageFont.truetype(F+"Lora-Variable.ttf",sz)
    try: f.set_variation_by_axes([w])
    except Exception: pass
    return f
def pop(sz,b=False): return ImageFont.truetype(F+("Poppins-Bold.ttf" if b else "Poppins-Regular.ttf"),sz)

def flower(d,cx,cy,r,lw,fills):
    # 6 petals; some filled (colored-in), rest outline only => "coloring page" idea
    for i in range(6):
        a=math.radians(i*60-90)
        px,py=cx+math.cos(a)*r*0.62,cy+math.sin(a)*r*0.62
        pr=r*0.40
        bb=[px-pr,py-pr,px+pr,py+pr]
        if fills[i]: d.ellipse(bb,fill=fills[i])
    for i in range(6):
        a=math.radians(i*60-90)
        px,py=cx+math.cos(a)*r*0.62,cy+math.sin(a)*r*0.62
        pr=r*0.40
        d.ellipse([px-pr,py-pr,px+pr,py+pr],outline=INK,width=lw)
    cr=r*0.30
    d.ellipse([cx-cr,cy-cr,cx+cr,cy+cr],fill=MUST,outline=INK,width=lw)

def pencil(d,x,y,L,w,ang,col,lw):
    a=math.radians(ang); ux,uy=math.cos(a),math.sin(a); nx,ny=-uy,ux
    def P(t,s): return (x+ux*t+nx*s, y+uy*t+ny*s)
    body=[P(0,-w/2),P(L*0.78,-w/2),P(L*0.78,w/2),P(0,w/2)]
    d.polygon(body,fill=col,outline=INK); d.line(body+[body[0]],fill=INK,width=lw)
    tip=[P(L*0.78,-w/2),P(L,0),P(L*0.78,w/2)]
    d.polygon(tip,fill=(240,215,180)); d.line(tip+[tip[0]],fill=INK,width=lw)
    lead=[P(L*0.93,-w*0.16),P(L,0),P(L*0.93,w*0.16)]
    d.polygon(lead,fill=INK)
    d.line([P(0,0),P(L*0.78,0)],fill=INK,width=max(1,lw//2))

# ---------- LOGO 500 (draw at 2000) ----------
S=2000; im=Image.new("RGB",(S,S),CREAM); d=ImageDraw.Draw(im)
d.ellipse([60,60,S-60,S-60],outline=INK,width=22)
d.ellipse([110,110,S-110,S-110],outline=INK,width=8)
flower(d,S/2,700,430,20,[CORAL,None,SAGE,None,LAV,None])
f=lora(330,700); t="Mira"; w=d.textlength(t,font=f); d.text(((S-w)/2,1130),t,font=f,fill=INK)
f2=pop(118,True); t2="D I G I T A L"; w2=d.textlength(t2,font=f2); d.text(((S-w2)/2,1520),t2,font=f2,fill=CORAL)
im.resize((500,500),Image.LANCZOS).save("mira_logo_500.png")
im.resize((1000,1000),Image.LANCZOS).save("mira_logo_1000.png")

# ---------- BANNER 3360x840 (draw 2x) ----------
W,H=6720,1680; b=Image.new("RGB",(W,H),CREAM); d=ImageDraw.Draw(b)
# soft dots
import random; random.seed(7)
for _ in range(90):
    x=random.randint(0,W); y=random.randint(0,H); r=random.randint(10,26)
    c=random.choice([CORAL,SAGE,MUST,LAV])
    if 1300<x<5400 and 250<y<1500: continue
    d.ellipse([x-r,y-r,x+r,y+r],fill=c)
# left: flowers half-colored
flower(d,720,760,450,22,[CORAL,None,SAGE,None,None,LAV])
flower(d,1180,1400,190,14,[None,MUST,None,CORAL,None,None])
# right: pencils
pencil(d,5480,1180,1100,150,-28,SAGE,14)
pencil(d,5560,1390,1030,150,-28,CORAL,14)
pencil(d,5640,1600,960,150,-28,LAV,14)
# text centre
f=lora(560,700); t="Mira Digital"; w=d.textlength(t,font=f); d.text(((W-w)/2,330),t,font=f,fill=INK)
f2=pop(118); t2="Printable coloring pages  ·  Custom pet & family coloring art"
w2=d.textlength(t2,font=f2); d.text(((W-w2)/2,1050),t2,font=f2,fill=INK)
f3=pop(120,True); t3="INSTANT DOWNLOAD"; w3=d.textlength(t3,font=f3)
x3=(W-w3)/2; d.rounded_rectangle([x3-60,1270,x3+w3+60,1450],radius=90,fill=CORAL); d.text((x3,1288),t3,font=f3,fill=CREAM)
b.resize((3360,840),Image.LANCZOS).save("mira_banner_3360x840.jpg",quality=92)
# mini banner 1600x213
m=Image.new("RGB",(3200,426),CREAM); d=ImageDraw.Draw(m)
flower(d,260,213,170,10,[CORAL,None,SAGE,None,None,LAV])
flower(d,2950,213,150,10,[None,MUST,None,CORAL,None,None])
f=lora(170,700); t="Mira Digital"; w=d.textlength(t,font=f); d.text(((3200-w)/2,40),t,font=f,fill=INK)
f2=pop(64); t2="Printable coloring pages · Instant download"; w2=d.textlength(t2,font=f2); d.text(((3200-w2)/2,270),t2,font=f2,fill=CORAL)
m.resize((1600,213),Image.LANCZOS).save("mira_mini_banner_1600x213.jpg",quality=92)

import json,os
from PIL import Image,ImageDraw,ImageFont,ImageFilter
F="/usr/share/fonts/truetype/google-fonts/"
S=json.load(open('/mnt/user-data/outputs/seo_v4.json'))
H={"d23":"Christmas Eve by the Fire","d24":"Home for the Holidays","d25":"The Light in the Storm","d26":"Dawn in the Winter Pines","d27":"The Perfect Rainy Evening","d28":"Rainy Days in Paris","d29":"Peonies in the Dark","d30":"An Evening in Paris","d31":"Moonlight Magic","d32":"A Very Cozy Christmas","d33":"Old Fashioned Christmas","d34":"A Victorian Christmas","d35":"When the Music Stops","d36":"First Light at the Lake","d37":"Coming Home at Dawn","d38":"Home is Where Love Is","d39":"The Winter Express","d40":"Highland Mornings","d41":"Golden Hour on the Farm","d42":"Slow Sunny Mornings","d43":"Love in the Snow","d44":"Under the Cherry Moon","d45":"Grace in the Moonlight","d46":"Peace on Earth","d47":"The Best Gift of All"}
for k,h in H.items():
    src=f'/mnt/user-data/uploads/Documents/etsy-printify/yeni2/raw/{k}.png'
    mock=f'/home/claude/prev/y2out/{k}/1_salon_yakin.jpg'
    W,Hh=1000,1500; c=Image.new('RGB',(W,Hh),(251,246,238))
    m=Image.open(mock).convert('RGB'); s=W/m.width; m=m.resize((W,int(m.height*s))); c.paste(m,(0,250))
    d=ImageDraw.Draw(c)
    f1=ImageFont.truetype(F+"Lora-Variable.ttf",64); f2=ImageFont.truetype(F+"Poppins-Regular.ttf",30); f3=ImageFont.truetype(F+"Poppins-Bold.ttf",28)
    while d.textlength(h,font=f1)>W-80: f1=ImageFont.truetype(F+"Lora-Variable.ttf",f1.size-4)
    d.text(((W-d.textlength(h,font=f1))/2,70),h,font=f1,fill=(43,45,66))
    sub="Canvas Wall Art  ·  Ready to Hang  ·  8 Sizes"
    d.text(((W-d.textlength(sub,font=f2))/2,165),sub,font=f2,fill=(224,122,95))
    d.rectangle([0,Hh-250,W,Hh],fill=(43,45,66))
    g=[x for x in S[k]['t'].split(',') if 'Gift' in x]; gl=(g[0].strip() if g else 'A gift they will remember')
    d.text(((W-d.textlength(gl,font=f2))/2,Hh-190),gl,font=f2,fill=(251,246,238))
    b="LimiraCollection on Etsy"; d.text(((W-d.textlength(b,font=f3))/2,Hh-120),b,font=f3,fill=(242,204,143))
    c.save(f'pins/{k}_pin.jpg',quality=88)
print(len(os.listdir('pins')))

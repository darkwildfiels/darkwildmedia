D={
"memorial":("Pet Memorial Portrait Canvas from Photo, Custom Dog Memorial Gift, Rainbow Bridge Angel Wings Painting, Pet Loss Sympathy Gift, Cat Memorial",
 "pet memorial gift,dog memorial gift,cat memorial gift,pet loss gift,rainbow bridge gift,dog remembrance gift,pet portrait canvas,custom dog portrait,pet sympathy gift,loss of dog gift,pet painting,angel wings dog,in loving memory",
 "🌈 Forever In Your Heart 🌈\n\nSome friends leave paw prints that never fade. This custom memorial portrait turns your favorite photo into a gentle painting of your dog or cat with soft angel wings above the clouds and a rainbow beyond, printed on premium gallery canvas. A loving way to remember them, and a deeply thoughtful sympathy gift for someone who is grieving."),
"royal":("Custom Royal Pet Portrait Canvas from Photo, Renaissance Dog Portrait, Funny Regal Cat Painting, Personalized Dog Mom Gift, Pet Lover Gift",
 "royal pet portrait,custom dog portrait,pet painting,renaissance pet,regal dog portrait,funny pet gift,dog mom gift,dog lover gift,cat lover gift,pet portrait canvas,custom cat portrait,dog dad gift,personalized pet",
 "👑 Turn Your Best Friend Into Royalty 👑\n\nYour pet already rules the house, so make it official. This custom portrait turns your favorite photo into a classic Renaissance style oil painting of your dog or cat in royal robes, printed on premium gallery canvas. Funny, impressive and guaranteed to be a conversation piece."),
"water":("Custom Watercolor Pet Portrait Canvas from Photo, Custom Dog Portrait, Minimalist Cat Painting, Personalized Pet Lover Gift, Dog Mom Gift",
 "custom dog portrait,watercolor pet,pet painting,custom cat portrait,pet portrait canvas,dog mom gift,dog lover gift,cat lover gift,personalized pet,minimalist pet art,dog dad gift,new puppy gift,pet memorial gift",
 "🎨 Your Pet, Painted In Soft Watercolor 🎨\n\nLight, airy and timeless. This custom portrait turns your favorite photo into a soft watercolor style painting of your dog or cat on a clean white background, printed on premium gallery canvas. It suits any room and any decor style."),
"xmas":("Custom Christmas Pet Portrait Canvas from Photo, Personalized Dog Christmas Gift, Cozy Fireplace Cat Portrait, Pet Painting, Dog Mom Gift",
 "custom dog portrait,christmas pet gift,pet painting,dog christmas gift,pet portrait canvas,dog mom gift,dog lover gift,cat lover gift,custom cat portrait,personalized pet,christmas gift mom,dog dad gift,holiday pet portrait",
 "🎄 Your Pet's Own Christmas Portrait 🎄\n\nThe coziest gift under the tree. This custom portrait turns your favorite photo into a warm classic painting of your dog or cat beside a glowing fireplace and Christmas tree, printed on premium gallery canvas. A keepsake you will bring out every December."),
}
REST="""

🐾 How It Works
1️⃣ Choose your canvas size
2️⃣ Upload 1 to 3 clear photos of your pet and type their name (or "no name") before adding to cart
3️⃣ Within 24 to 48 hours we send you a free digital preview through Etsy messages
4️⃣ Love it? We print it. Want a change? One free revision is included ✏️

🛡️ Our Promise
💛 Free preview before printing: you approve it first
🔤 Your pet's name is shown in the preview, so the spelling is always right
🖼️ Real 1.25" gallery wrapped canvas with printed edges, ready to hang
🎄 For Christmas delivery in the US, please order by December 7

📏 Sizes (inches / cm)
• 8 x 10 in (20 x 25 cm)
• 11 x 14 in (28 x 36 cm)
• 12 x 18 in (30 x 46 cm)
• 16 x 20 in (41 x 51 cm)
• 16 x 24 in (41 x 61 cm)
• 20 x 30 in (51 x 76 cm)
• 24 x 30 in (61 x 76 cm)
• 24 x 36 in (61 x 91 cm)

🚚 Production & Shipping
• Preview: 24 to 48 hours after your order
• Production: 2 to 5 business days after you approve the preview
• US: FREE shipping, 2 to 5 business days after dispatch
• International: 10 to 30 business days after dispatch

📸 Photo Tips
Bright natural light, face clearly visible, eyes in focus. Phone photos work great. One pet per portrait.

🤖 Please Note
Portraits are digitally created from your photo with the help of AI tools and are reviewed and adjusted by us before printing. They are not hand painted. The sample pet in the listing photos shows the style; your portrait will show your own pet. Colors may vary slightly between screens.

🔄 Returns
Because every portrait is made just for you, we cannot accept change of mind returns. If your canvas arrives damaged, send us a photo and we will send a free replacement.

Thank you for supporting our small shop 🤍
LimiraCollection"""
for k,(t,g,h) in D.items():
    tags=[x.strip() for x in g.split(',')]
    assert len(t)<=140 and len(set(tags))==13 and all(len(x)<=20 for x in tags),(k,len(t),[x for x in tags if len(x)>20])
    open(f'/home/claude/lm/limira/pet/seo_{k}.txt','w').write(f"###TITLE###\n{t}\n###TAGS###\n{g}\n###DESCRIPTION###\n{h}{REST}\n###END###\n")
print('ok')

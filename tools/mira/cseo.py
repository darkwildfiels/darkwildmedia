C={
"CN":("Personalized Christmas Coloring Page with Name, Custom Kids Christmas Coloring Sheet, Printable Name Activity, Stocking Stuffer PDF",
"personalized gift,custom coloring page,name coloring page,kids christmas,christmas coloring,personalized kids,stocking stuffer,christmas activity,classroom gift,kids name gift,custom printable,toddler coloring,holiday coloring",
"""🎄 A Christmas coloring page made just for your child, with their name in big, fun letters they can color in! Choose a cute design (teddy bear, reindeer, snowman, penguins, trucks, nativity and more) or let us pick one, and we'll add "Merry Christmas" and your child's name.

🎁 WHAT YOU GET
✏️ 1 personalized Christmas coloring page with your child's name in hollow, colorable letters
📄 Printable PDF in US Letter (8.5 x 11 in) and A4
👀 Sent to you through Etsy Messages within 24-48 hours
🔁 Need it fixed? One free change if something isn't right

✨ HOW TO ORDER
1️⃣ Type your child's name in the personalization box at checkout (and the design you'd like, if you have a favorite)
2️⃣ We create your page and send the PDF through Etsy Messages within 24-48 hours
3️⃣ Print at home and color!

💡 Want the same page for siblings or a whole class? Message us before ordering for multi-name pricing.""",
"stockings, Christmas Eve boxes, classroom parties, grandkids, Advent activities and kids' tables"),
"CP":("Custom Christmas Pet Coloring Page from Your Photo, Personalized Dog or Cat Coloring Sheet with Santa Hat, Pet Lover Gift Printable PDF",
"custom pet portrait,pet coloring page,christmas pet gift,dog coloring page,cat coloring page,pet lover gift,custom coloring page,personalized gift,dog mom gift,cat mom gift,christmas coloring,pet memorial gift,stocking stuffer",
"""🐾 Turn your dog or cat into a one-of-a-kind Christmas coloring page! Send us a photo and we'll draw your pet as clean, printable line art, with a Santa hat, scarf, Christmas tree or cozy fireplace if you'd like. A sweet, personal gift for pet lovers of every age.

🎁 WHAT YOU GET
✏️ 1 custom Christmas coloring page of your pet, drawn from your photo
🎅 Optional extras: pet's name, Santa hat, scarf, tree, fireplace or presents
📄 Printable PDF in US Letter (8.5 x 11 in) and A4
👀 A preview within 24-48 hours and one free round of edits

✨ HOW TO ORDER
1️⃣ Upload a clear, well-lit photo of your pet at checkout (or send it in Etsy Messages)
2️⃣ Tell us your pet's name and any Christmas extras you'd like
3️⃣ We send a preview, you approve it, and we deliver your PDF through Etsy

📸 PHOTO TIPS: one pet per photo works best; face the camera, good light, no heavy filters. Multiple pets? Message us first.""",
"dog moms, cat dads, grandparents, Christmas cards, pet memorials, stockings and family coloring nights"),
}
NOTE="""

📌 PLEASE NOTE
• This is a DIGITAL, made-to-order item. No physical product will be shipped.
• Colors in the preview images are examples only; you receive black and white line art.
• For personal, non-commercial use only.
• Because each page is made just for you, returns are not accepted, but we will always fix anything that isn't right.
• Our studio creates these pages with the help of digital and AI tools, and every page is checked by hand before it is sent.
• Your photo is used only for your order.

💝 GREAT FOR
Perfect for {g}.

Thank you for supporting our small studio! 🤍 Mira Digital"""
for k,(t,tg,d,g) in C.items():
    tags=[x.strip() for x in tg.split(',')]
    assert len(t)<=140 and len(tags)==13 and all(len(x)<=20 for x in tags),(k,len(t),[x for x in tags if len(x)>20])
    open(f'seo_{k}.txt','w').write(f"###TITLE###\n{t}\n###TAGS###\n{tg}\n###DESCRIPTION###\n{d}{NOTE.format(g=g)}\n###END###\n")
print('ok')

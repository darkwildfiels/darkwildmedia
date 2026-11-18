G = {
"G1": ("Christmas Picture Bingo 30 Cards Printable, Christmas Party Game for Kids and Family, Classroom Holiday Bingo with Calling Cards PDF",
 "christmas bingo,picture bingo,christmas game,christmas party game,kids bingo,family game night,classroom game,holiday bingo,printable bingo,xmas bingo cards,school party game,christmas activity,bingo cards pdf",
 "🎄 A colorful picture bingo game everyone can play, no reading needed! 30 different 5x5 bingo cards filled with cute Christmas pictures (snowmen, gnomes, gingerbread, ornaments, puppies in sweaters and more) plus matching calling cards. Just print, cut and play.",
 ["🎯 30 unique 5x5 picture bingo cards with a FREE center space", "🃏 Calling cards with every picture (cut apart and draw from a bowl)", "📋 How-to-play instructions page"],
 "classroom Christmas parties, family game night, kids' parties, church groups, office parties and senior centers", "30 bingo cards + calling cards"),
"G2": ("Large Print Christmas Bingo for Seniors, 20 Big 3x3 Picture Bingo Cards, Dementia Friendly Holiday Activity, Printable PDF Game",
 "bingo for seniors,large print bingo,christmas bingo,dementia activities,memory care,senior activities,nursing home game,christmas game,picture bingo,elderly activities,printable bingo,holiday activity,alzheimers activity",
 "❄️ Christmas bingo made easy to see and easy to play. 20 large print 3x3 picture bingo cards with big, bold pictures and a FREE center, plus extra-large calling cards. A calm, joyful holiday activity for seniors, memory care and anyone who prefers a simpler game.",
 ["🎯 20 unique 3x3 large print picture bingo cards", "🃏 Extra-large calling cards (6 per page)", "📋 Simple how-to-play page"],
 "nursing homes, assisted living, memory care, adult day programs, grandparents' visits and young kids", "20 bingo cards + calling cards"),
"G3": ("Christmas Word Search Puzzles, 10 Printable Holiday Word Find Pages with Answer Keys, Kids and Adults Christmas Activity PDF",
 "xmas word search,word search pdf,christmas activity,word find,christmas puzzle,holiday puzzles,kids activity sheet,classroom activity,christmas printable,winter break fun,senior activities,christmas party game,brain games",
 "🔎 10 cozy Christmas word search puzzles to keep minds busy all season. Themes include Santa's reindeer, the nativity, Christmas treats, winter wonderland and more, with a full answer key for every puzzle.",
 ["🧩 10 themed word search puzzles (10 words each)", "✅ 10 answer key pages", "🎄 Themes: Merry Christmas, Deck the Halls, Winter Wonderland, Holiday Treats, The Nativity, Santa's Reindeer, Christmas Eve, Gift Giving, Christmas Tree, Jolly Holidays"],
 "classrooms, homeschool, waiting rooms, holiday travel, seniors, family gatherings and quiet time", "10 puzzles + answer keys"),
"G4": ("Christmas Trivia Game Printable, 50 Christmas Trivia Question Cards with Answers, Family Party Game for Kids and Adults PDF",
 "christmas trivia,trivia game,christmas party game,family game night,christmas game,holiday trivia,trivia cards,office party game,classroom game,christmas printable,xmas games,kids and adults,game night",
 "🎅 How well do you know Christmas? 50 printable trivia cards with fun questions about traditions, songs, the nativity story, reindeer, treats and more. The answer is printed on each card, so anyone can be the host.",
 ["❓ 50 Christmas trivia question cards (8 per page) with answers", "📋 How-to-play page with team rules"],
 "family Christmas parties, office parties, classrooms, youth groups, Zoom calls and game nights", "50 trivia cards"),
"G5": ("Christmas Would You Rather Game for Kids, 40 Printable Question Cards, Family Christmas Party Game, Classroom Holiday Activity PDF",
 "would you rather,christmas game,kids christmas game,christmas party game,family game,classroom game,conversation cards,christmas printable,holiday game,kids party game,xmas games,christmas activity,winter break fun",
 "☃️ Get everyone laughing with 40 silly and sweet Christmas Would You Rather questions! Would you rather have a pet reindeer or a pet penguin? Great for breaking the ice at parties, family dinners and classrooms.",
 ["💬 40 Christmas Would You Rather cards (8 per page)", "📋 How-to-play page"],
 "kids' parties, family dinners, classrooms, road trips, youth groups and holiday get-togethers", "40 question cards"),
"G6": ("Christmas Party Games Bundle Printable, Christmas Bingo, Word Search, Trivia and Would You Rather, Family and Kids Holiday Games PDF",
 "christmas games,party games bundle,christmas bingo,christmas trivia,word search,would you rather,family game night,christmas party game,classroom party,office party game,kids christmas game,holiday games,christmas printable",
 "🎁 Everything you need for a fun Christmas party in one download: 4 printable games for kids, families, classrooms and office parties. Print what you need and play again and again.",
 ["🎯 Christmas Picture Bingo: 30 cards + calling cards", "🔎 Christmas Word Search: 10 puzzles + answer keys", "❓ Christmas Trivia: 50 question cards with answers", "💬 Christmas Would You Rather: 40 question cards"],
 "Christmas parties, classrooms, family game nights, office parties, church groups and senior centers", "4 games in 1 PDF"),
}
TPL = """{hook}

🎁 WHAT'S INCLUDED

{items}

✨ Your digital download includes:
✅ 2 high-resolution PDF files: US Letter (8.5 x 11 in) and A4
✅ {what}
✅ Instant digital download
✅ Print as many copies as you need for your own party, family or classroom

🖍️ HOW IT WORKS
🛒 Step 1: Purchase this digital game from Mira Digital.
📥 Step 2: After payment, download your files from your Etsy account (Purchases and Reviews).
🖨️ Step 3: Choose the PDF that matches your paper size and print.
🎉 Step 4: Cut, play and have fun!

🖨️ PRINTING TIPS
📄 Print at 100% (actual size) or choose "fit to page".
✨ Cardstock makes sturdy, reusable cards.

💝 GREAT FOR
Perfect for {great}.

📌 PLEASE NOTE
• This is a DIGITAL item. No physical product will be shipped.
• For personal and classroom use only. Please do not resell or share the files.
• Due to the nature of digital downloads, returns are not accepted, but please message us if anything is wrong with your files and we will make it right.
• The pictures were created by our studio with the help of digital and AI tools, and every page is checked by hand.

Thank you for supporting our small studio! 🤍 Mira Digital"""
for k, (t, g, h, items, gr, what) in G.items():
    tags = [x.strip() for x in g.split(',')]
    assert len(t) <= 140 and len(tags) == 13 and all(len(x) <= 20 for x in tags), (k, len(t), [x for x in tags if len(x) > 20])
    desc = TPL.format(hook=h, items="\n".join(items), great=gr, what=what)
    open(f'seo_{k}.txt', 'w').write(f"###TITLE###\n{t}\n###TAGS###\n{g}\n###DESCRIPTION###\n{desc}\n###END###\n")
print('ok')

G2_ = {"AB": ("Kids Christmas Activity Book Printable, 42 Pages of Coloring, Word Search and Would You Rather, Winter Break Activity Pack PDF",
 "kids activity book,christmas activity,kids christmas,activity pack,word search,coloring pages,would you rather,winter break fun,classroom activity,christmas printable,travel activity,kids party game,stocking stuffer",
 "🎄 Keep kids busy and happy all Christmas break with one printable activity book! 42 pages of cute coloring pages, Christmas word search puzzles and silly Would You Rather cards for ages 4 to 9. Print what you need, again and again.",
 ["🖍️ 15 coloring pages: cute Christmas animals, snowmen and the nativity", "🔎 10 Christmas word searches + 10 answer keys", "💬 40 Christmas Would You Rather cards + how-to page"],
 "winter break, classroom parties, Sunday school, restaurants, road trips, flights and kids' tables", "42 pages in one PDF")}
for k, (t, g, h, items, gr, what) in G2_.items():
    tags = [x.strip() for x in g.split(',')]
    assert len(t) <= 140 and len(tags) == 13 and all(len(x) <= 20 for x in tags), (k, len(t), [x for x in tags if len(x) > 20])
    open(f'seo_{k}.txt', 'w').write(f"###TITLE###\n{t}\n###TAGS###\n{g}\n###DESCRIPTION###\n{TPL.format(hook=h, items=chr(10).join(items), great=gr, what=what)}\n###END###\n")

from gseo import TPL
G = {
"GB": ("Christmas Games Mega Bundle Printable, 10 Family Party Games, Bingo, Trivia, Charades, Pictionary, Word Search, Kids and Adults PDF",
 "christmas games,party games bundle,christmas bingo,christmas trivia,christmas charades,pictionary game,family game night,christmas party game,office party game,classroom party,holiday games,xmas games,christmas printable",
 "🎁 The only Christmas game download you'll need! 10 printable party games in one bundle, enough for every family gathering, classroom party and office celebration this season.",
 ["🎯 Picture Bingo (30 cards) + Word Bingo (30 cards)", "❓ Christmas Trivia (50 cards)", "🎭 Charades (60 cards) + ✏️ Pictionary (60 cards)", "🤔 This or That (50) + 💬 Would You Rather (40)", "🔎 Word Search (10) + 🔤 Word Scramble (5 sheets)", "🗣️ Conversation Cards (50)"],
 "Christmas parties, family game nights, classrooms, office parties, church groups and senior centers", "10 games, 136 pages"),
"KA": ("Kids Christmas Activity Mega Pack Printable, 107 Pages of Mazes, Sudoku, Santa Letter, Coloring and Games, Winter Break Activities PDF",
 "kids activity pack,christmas activity,kids christmas,activity book,mazes for kids,sudoku for kids,letter to santa,coloring pages,winter break fun,busy book,travel activity,homeschool christmas,stocking stuffer",
 "🎄 107 pages of Christmas fun to keep kids happy all winter break! Mazes, kid sudoku, word scramble, a letter to Santa kit, a 25-day countdown, jokes, a scavenger hunt and cute coloring pages, all in one download.",
 ["🧩 20 mazes + 30 sudoku + word scramble", "🎅 Letter to Santa kit with Nice List certificate", "📅 25-day Christmas countdown cards", "😂 40 joke cards + 🔦 scavenger hunts", "🖍️ 10 coloring pages (animals and trucks)"],
 "winter break, homeschool, road trips, flights, restaurants and grandparents' houses", "107 pages"),
"CR": ("Christmas Classroom Party Pack Printable, Word Bingo, Mazes, Word Search, This or That, Countdown Cards, Teacher Holiday Activities PDF",
 "classroom party,christmas classroom,teacher printable,christmas bingo,word bingo,mazes for kids,word search,classroom game,christmas activity,school party game,morning meeting,early finisher,holiday activity",
 "🍎 Teachers, your Christmas party is planned! Whole-class games, early-finisher puzzles and a December countdown in one printable pack. Print what you need, as many times as you need for your class.",
 ["🎯 Word Bingo (30 cards + calling list)", "🤔 This or That (50 cards) + 😂 Jokes (40 cards)", "🧩 20 mazes + 🔎 10 word searches + 🔤 word scramble", "📅 25 countdown activity cards"],
 "classroom Christmas parties, the last week before winter break, morning meetings, sub plans and early finishers", "7 activities, 116 pages"),
"SP": ("Christmas Activity Pack for Seniors Printable, Large Print Bingo, Word Search, Trivia and Coloring, Dementia Friendly Holiday Activities",
 "senior activities,activities seniors,large print bingo,dementia activities,memory care,nursing home game,christmas activity,large print coloring,word search,christmas trivia,elderly activities,assisted living,holiday activity",
 "❄️ A complete Christmas activity pack made for seniors: big, clear and easy to enjoy. Large print bingo, word searches, trivia, conversation cards and bold coloring pages for a joyful holiday season in memory care, assisted living or at home.",
 ["🎯 Large Print Christmas Bingo (20 cards)", "🔎 10 Christmas word searches", "❓ 50 trivia cards + 💬 50 conversation cards", "🖍️ 15 large print and bold coloring pages"],
 "nursing homes, assisted living, memory care, activity directors, caregivers and grandparents", "7 activities"),
}
for k, (t, g, h, items, gr, what) in G.items():
    tags = [x.strip() for x in g.split(',')]
    assert len(t) <= 140 and len(tags) == 13 and all(len(x) <= 20 for x in tags), (k, len(t), [x for x in tags if len(x) > 20])
    open(f'seo_{k}.txt', 'w').write(f"###TITLE###\n{t}\n###TAGS###\n{g}\n###DESCRIPTION###\n{TPL.format(hook=h, items=chr(10).join(items), great=gr, what=what)}\n###END###\n")
print('ok')

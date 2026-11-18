import json
COL_NOTE = """📌 PLEASE NOTE
• This is a DIGITAL item. No physical product will be shipped.
• Colors shown in the preview images are examples only; the pages are black and white line art.
• For personal, non-commercial use only. Please do not resell or share the files.
• Due to the nature of digital downloads, returns are not accepted, but please message us if anything is wrong with your files and we will make it right.
• These designs were created by our studio with the help of digital and AI tools, and every page is checked by hand.

Thank you for supporting our small studio! 🤍 Mira Digital"""
GAME_NOTE = """📌 PLEASE NOTE
• This is a DIGITAL item. No physical product will be shipped.
• For personal and classroom use only. Please do not resell or share the files.
• Due to the nature of digital downloads, returns are not accepted, but please message us if anything is wrong with your files and we will make it right.
• Designed by our studio with the help of digital tools, and every page is checked by hand.

Thank you for supporting our small studio! 🤍 Mira Digital"""

def col(hook, n, items, great, extra=""):
    lst = "\n".join(items)
    return f"""{hook}

🎁 WHAT'S INCLUDED

You'll receive {n} printable coloring pages:

{lst}
{extra}
✨ Your digital download includes:
✅ 2 high-resolution PDF files
✅ US Letter size (8.5 x 11 inches)
✅ A4 size for international printing
✅ {n} coloring pages + 1 cover page
✅ Instant digital download
✅ Print again and again for personal use

🖍️ HOW IT WORKS
🛒 Step 1: Purchase this digital set from Mira Digital.
📥 Step 2: After payment, download your files from your Etsy account (Purchases and Reviews).
🖨️ Step 3: Choose the PDF that matches your paper size.
🎨 Step 4: Print and start coloring!

🖨️ PRINTING TIPS
📄 Print at 100% (actual size) or choose "fit to page".
✨ Use high quality print settings for crisp lines.
🖍️ Thicker paper or cardstock works great for markers.

💝 GREAT FOR
{great}

{COL_NOTE}"""

def game(hook, items, great, n_files="2 high-resolution PDF files: US Letter (8.5 x 11 in) and A4"):
    lst = "\n".join(items)
    return f"""{hook}

🎁 WHAT'S INCLUDED

{lst}

✨ Your digital download includes:
✅ {n_files}
✅ Instant digital download
✅ Print as many copies as you need for your own party, family or classroom

🎲 HOW IT WORKS
🛒 Step 1: Purchase this digital game from Mira Digital.
📥 Step 2: After payment, download your files from your Etsy account (Purchases and Reviews).
🖨️ Step 3: Choose the PDF that matches your paper size and print.
🎉 Step 4: Cut, play and have fun!

🖨️ PRINTING TIPS
📄 Print at 100% (actual size) or choose "fit to page".
✨ Cardstock makes sturdy, reusable cards.

💝 GREAT FOR
{great}

{GAME_NOTE}"""

S = {}
S["VK"] = ("Valentines Day Coloring Pages for Kids, 5 Printable Cute Animal Valentine Coloring Sheets, Classroom Valentine Activity PDF",
 "valentine coloring,valentines day kids,kids valentine,classroom valentine,valentine activity,kids coloring pages,toddler coloring,cute animal coloring,preschool activity,valentine printable,heart coloring page,valentine party,easy coloring page",
 col("💕 Five sweet Valentine's Day coloring pages full of cuddly animals and big hearts! Thick outlines and simple shapes make them perfect for little hands ages 3 to 8. An easy, screen-free Valentine activity for home or the classroom.", 5,
 ["🧸 Teddy Bear Hug: a bear hugging a big heart", "🐶 Puppy Love: two puppies sharing a heart cookie", "🎈 Heart Balloons: a kitten with a bunch of balloons", "🦄 Love Cloud: a unicorn with a heart-shaped cloud", "🐧 Penguin Pals: a penguin couple holding a heart"],
 "Perfect for Valentine's Day parties, classrooms, daycare, preschool, Valentine cards and cozy afternoons at home."))
S["VA"] = ("Valentines Coloring Pages for Adults, 5 Bold and Easy Printable Love Coloring Sheets, Hearts, Roses and Love Birds, Seniors Activity",
 "valentine coloring,bold and easy,adult coloring page,valentines day,large print coloring,coloring for seniors,heart coloring page,love coloring,printable coloring,relaxing coloring,galentines gift,dementia activity,rose coloring page",
 col("❤️ Five romantic, relaxing Valentine coloring pages with bold lines and big spaces. Hearts, roses, love birds and cozy coffee for two. Easy on the eyes, fun to finish and perfect for adults, seniors and teens.", 5,
 ["🌹 Heart of Roses: a big heart filled with roses", "🐦 Love Birds: two birds on a flowering branch", "💌 Love Letters: a vintage mailbox full of hearts", "☕ Coffee for Two: heart latte, cookies and flowers", "🌷 Tulip Wreath: a heart-shaped wreath with ribbons"],
 "Perfect for Galentine's parties, senior centers, memory care, date night at home, gifts for mom or grandma and calm evenings."))
S["KF"] = ("Kawaii Food Coloring Pages for Kids, 5 Printable Cute Boba, Sushi, Donut and Ice Cream Coloring Sheets, Easy Kids Activity PDF",
 "kawaii coloring,cute food coloring,kids coloring pages,boba coloring page,sushi coloring,donut coloring,ice cream coloring,kawaii printable,toddler coloring,easy coloring page,rainy day activity,kids activity,birthday party",
 col("🧋 The cutest food you'll ever color! Five smiling kawaii treats: bubble tea, sushi, donuts, ice cream and pancakes. Big friendly faces and thick outlines that kids absolutely love.", 5,
 ["🧋 Happy Boba: a smiling bubble tea with pearls", "🍣 Sushi Friends: smiling sushi and onigiri", "🍩 Donut Stack: sprinkled donuts piled high", "🍦 Triple Scoop: an ice cream cone with a cherry", "🥞 Pancake Party: a stack with syrup and berries"],
 "Perfect for kawaii lovers, birthday parties, restaurants, road trips, quiet time, classrooms and rainy days."))
S["BB"] = ("Baby Animals Coloring Pages, 5 Bold and Easy Printable Cute Animal Coloring Sheets for Adults, Seniors and Kids, Large Print PDF",
 "baby animals,bold and easy,cute animal coloring,large print coloring,coloring for seniors,adult coloring page,dementia activity,easy coloring page,animal printable,relaxing coloring,kids coloring pages,printable coloring,nursery coloring",
 col("🐘 Five adorable baby animals drawn in a bold and easy style: big shapes, thick lines and no tiny details. Relaxing for adults and seniors, and simple enough to share with the grandkids.", 5,
 ["🐘 Baby Elephant: sitting in a flower meadow", "🦊 Sleepy Fox: curled up under a tree", "🐼 Baby Panda: munching on bamboo", "🐰 Bunny Basket: a bunny with daisies", "🦌 Little Fawn: in tall grass with butterflies"],
 "Perfect for seniors, memory care, beginners, low-vision colorists, grandparents and kids coloring together."))
S["OC"] = ("Ocean Animals Coloring Pages for Kids, 5 Printable Under the Sea Coloring Sheets, Whale, Octopus and Sea Turtle, Preschool Activity",
 "ocean coloring,under the sea,sea animals,kids coloring pages,whale coloring page,octopus coloring,sea turtle coloring,preschool activity,toddler coloring,ocean party,easy coloring page,summer activity,kids printable",
 col("🐳 Dive under the sea with five happy ocean friends! A smiling whale, a waving octopus, a sea turtle, clownfish and a crab on the sandy floor. Thick lines and big spaces for kids ages 3 to 8.", 5,
 ["🐳 Happy Whale: swimming with bubbles", "🐙 Octopus Hello: waving among the coral", "🐢 Sea Turtle: gliding over seaweed", "🐠 Clownfish: around a sea anemone", "🦀 Crab and Starfish: on the ocean floor"],
 "Perfect for ocean birthday parties, classrooms, aquarium trips, beach vacations, homeschool and quiet time."))
S["FL"] = ("Large Print Flower Coloring Pages for Seniors, 5 Bold and Easy Printable Sunflower, Rose and Tulip Coloring Sheets, Dementia Activity",
 "large print coloring,coloring for seniors,bold and easy,flower coloring page,dementia activity,simple coloring,sunflower coloring,rose coloring page,memory care,easy coloring page,adult coloring page,elderly activity,relaxing coloring",
 col("🌻 Big, beautiful flowers with extra-bold outlines and large open spaces. Five calming pages designed to be easy to see and satisfying to finish. Ideal for seniors, memory care and anyone who loves simple coloring.", 5,
 ["🌻 Sunflower: one large bloom with leaves", "🌷 Tulip Vase: a vase of tulips on a table", "🌹 Big Rose: a single rose with leaves", "🌼 Window Daisies: a pot of daisies on a sill", "🐦 Hummingbird: with big simple flowers"],
 "Perfect for seniors, assisted living, memory care activities, low vision, stroke recovery, beginners and gifts for grandma."))
S["MF"] = ("Cottagecore Mushroom and Frog Coloring Pages, 5 Printable Detailed Adult Coloring Sheets, Whimsical Forest Toadstool Coloring",
 "cottagecore,frog coloring page,mushroom coloring,adult coloring page,whimsical coloring,forest coloring,toadstool art,fairycore,goblincore,detailed coloring,printable coloring,relaxing coloring,stress relief",
 col("🍄 A cozy little world of frogs and mushrooms! Five detailed cottagecore coloring pages with toadstools, ferns, snails and fireflies. Lots of tiny areas to color for a calm, cozy evening.", 5,
 ["🐸 Under the Mushroom: a frog in a mossy forest", "☂️ Leaf Umbrella: a frog among toadstools and ferns", "🏡 Mushroom Cottage: round door, flowers and snails", "📖 Bookworm Frog: reading on a mushroom", "✨ Fairy Ring: mushrooms, fireflies and a little frog"],
 "Perfect for cottagecore and goblincore lovers, relaxing evenings, journaling, mindfulness and gifts for nature lovers."))
S["FH"] = ("Fairy House Coloring Pages for Adults, 5 Printable Detailed Whimsical Coloring Sheets, Teapot, Treehouse and Pumpkin Fairy Homes",
 "fairy house,fairy coloring page,adult coloring page,whimsical coloring,detailed coloring,fantasy coloring,cottagecore,fairy garden,treehouse coloring,printable coloring,relaxing coloring,stress relief,magical coloring",
 col("🧚 Step into a tiny magical world. Five detailed fairy homes: a teapot cottage, a hollow tree with a spiral staircase, a pumpkin house, a lily pad cottage and a treehouse village. Hours of peaceful, detailed coloring.", 5,
 ["🫖 Teapot Cottage: flowers and a tiny door", "🌳 Hollow Tree: spiral stairs and lanterns", "🎃 Pumpkin House: in a garden", "🪷 Lily Pad Cottage: with dragonflies", "🌉 Treehouse Village: tiny bridges and lanterns"],
 "Perfect for fantasy lovers, adults and teens, relaxing weekends, art journaling and cozy gifts."))
S["SX"] = ("Space Coloring Pages for Kids, 5 Printable Astronaut, Rocket and Planets Coloring Sheets, Outer Space Activity for Boys and Girls",
 "space coloring page,astronaut coloring,rocket coloring,planet coloring page,kids coloring pages,outer space party,boys coloring,preschool activity,toddler coloring,easy coloring page,science activity,homeschool,kids printable",
 col("🚀 3, 2, 1... blast off! Five out-of-this-world space coloring pages with a waving astronaut, a rocket, a friendly alien, smiling planets and a space dog. Bold lines and big spaces for kids ages 3 to 8.", 5,
 ["👩‍🚀 Moon Walk: an astronaut waving on the moon", "🚀 Rocket Ride: flying past planets and stars", "👽 Friendly Alien: in a flying saucer", "🪐 Smiling Planets: Saturn and friends", "🐶 Space Pup: floating with an astronaut"],
 "Perfect for space-themed birthdays, science units, homeschool, classrooms, road trips and little explorers."))
S["ME"] = ("Mermaid Coloring Pages for Kids, 5 Printable Cute Mermaid Coloring Sheets, Under the Sea Girls Activity, Mermaid Party Favor PDF",
 "mermaid coloring,mermaid party,under the sea,kids coloring pages,girls coloring,mermaid printable,ocean coloring,toddler coloring,preschool activity,party favor,easy coloring page,birthday activity,kids printable",
 col("🧜‍♀️ Five magical mermaid coloring pages for little dreamers! Mermaids with seashells, a happy dolphin, coral reef friends, an underwater castle and a baby mermaid with a giant pearl.", 5,
 ["🐚 Seashell Rock: a mermaid on a rock", "🐬 Dolphin Friend: swimming together", "🐠 Coral Reef: playing with fish", "🏰 Sea Castle: a castle under the sea", "🦪 Pearl Princess: a baby mermaid in a clam shell"],
 "Perfect for mermaid birthday parties, party favors, beach trips, classrooms and quiet time."))
S["CT"] = ("Cozy Cat Coloring Pages, 5 Bold and Easy Printable Cat Coloring Sheets for Adults and Seniors, Cats with Books, Plants and Tea",
 "cat coloring page,cozy coloring,bold and easy,cat lover gift,adult coloring page,coloring for seniors,large print coloring,hygge coloring,relaxing coloring,printable coloring,cat mom gift,easy coloring page,dementia activity",
 col("🐈 Five cozy cats in their favorite spots: napping on books, among house plants, in an armchair with a blanket, with a ball of yarn and on the kitchen counter. Bold, easy and so relaxing.", 5,
 ["📚 Book Nap: a cat asleep on a stack of books", "🪴 Plant Corner: a cat among house plants", "🛋️ Armchair Snuggle: blanket and mug", "🧶 Yarn Basket: a cat playing with yarn", "🫖 Tea Time: teapot and cookies"],
 "Perfect for cat lovers, cat moms, seniors, beginners, cozy evenings and little gifts for friends."))
S["DG"] = ("Dog Breeds Coloring Pages, 5 Bold and Easy Printable Dog Coloring Sheets, Golden Retriever, Corgi, Dachshund, Frenchie and Beagle",
 "dog coloring page,dog breeds,bold and easy,dog lover gift,adult coloring page,coloring for seniors,golden retriever,corgi coloring,dachshund coloring,frenchie coloring,large print coloring,dog mom gift,easy coloring page",
 col("🐕 Five favorite dog breeds in a bold and easy style: a golden retriever, a dachshund, a corgi, a French bulldog and a beagle puppy. Big shapes and thick lines for relaxing, happy coloring.", 5,
 ["🎾 Golden Retriever: with a ball", "🌭 Dachshund: on a cozy rug", "🌼 Corgi: sitting with flowers", "🦴 French Bulldog: with a bone", "🌱 Beagle Puppy: playing in the grass"],
 "Perfect for dog lovers, dog moms and dads, seniors, kids and adults coloring together, and small gifts."))
S["BF"] = ("Butterfly Garden Coloring Pages for Adults, 5 Printable Detailed Butterfly and Flower Coloring Sheets, Relaxing Floral Coloring PDF",
 "butterfly coloring,flower coloring page,adult coloring page,garden coloring,detailed coloring,floral coloring,relaxing coloring,stress relief,printable coloring,mindfulness,rose coloring page,hummingbird,gift for mom",
 col("🦋 Five detailed butterfly garden pages: ornate wings, roses and peonies, a blooming lily, a rose-covered garden gate and a hummingbird. Fine lines and lots of little spaces for a calming coloring session.", 5,
 ["🦋 Ornate Butterfly: patterned wings among flowers", "🌸 Rose Garden: butterflies over roses and peonies", "🌺 Lily Bloom: a butterfly resting on a lily", "🚪 Garden Gate: climbing roses and butterflies", "🐦 Hummingbird Vine: flowers and butterflies"],
 "Perfect for adults and teens, mindfulness, stress relief, spring decor, Mother's Day and gifts for flower lovers."))
S["SD"] = ("Snow Day Coloring Pages for Kids, 5 Printable Winter Fun Coloring Sheets, Snowman, Sledding and Hot Cocoa, January Activity PDF",
 "snow day,winter coloring,kids coloring pages,january activity,snowman coloring,winter break,sledding coloring,hot cocoa coloring,preschool activity,toddler coloring,easy coloring page,winter printable,classroom activity",
 col("☃️ Snow day! Five happy winter coloring pages for kids: building a snowman, sledding, a skating polar bear, a penguin making snow angels and hot cocoa by the window. Bold lines for ages 3 to 8.", 5,
 ["⛄ Snowman Team: kids building a snowman", "🛷 Sled Ride: zooming down a snowy hill", "🐻‍❄️ Skating Bear: on a frozen pond", "🐧 Snow Angels: a happy penguin", "☕ Cocoa Time: marshmallows by the window"],
 "Perfect for snow days, January classrooms, winter break, daycare, homeschool and cozy afternoons."))
S["LN"] = ("Lunar New Year Coloring Pages for Kids, 5 Printable Chinese New Year Coloring Sheets, Lanterns, Dragon Dance and Dumplings",
 "lunar new year,chinese new year,kids coloring pages,new year coloring,dragon dance,lantern coloring,classroom activity,preschool activity,cultural activity,kids printable,easy coloring page,homeschool,year of the goat",
 col("🏮 Celebrate the Lunar New Year with five joyful coloring pages: a little goat with lanterns, a dragon dance, cute dumplings, a panda with a red envelope and a lion dance. Bold lines for kids ages 3 to 8.", 5,
 ["🐐 Little Goat: celebrating with red lanterns", "🐉 Dragon Dance: lanterns and fireworks", "🥟 Dumpling Friends: with chopsticks", "🧧 Lucky Panda: red envelope and lanterns", "🦁 Lion Dance: drums and firecrackers"],
 "Perfect for Lunar New Year classroom celebrations, cultural lessons, homeschool, family parties and preschool."))
S["PR"] = ("Princess Coloring Pages for Kids, 5 Printable Cute Princess and Castle Coloring Sheets, Girls Birthday Party Activity, Party Favor",
 "princess coloring,castle coloring page,girls coloring,princess party,kids coloring pages,birthday activity,party favor,toddler coloring,preschool activity,fairy tale coloring,easy coloring page,pony coloring page,kids printable",
 col("👑 Five sweet princess coloring pages for little royals! A princess by her castle, a pony ride, a teddy bear tea party, story time under a tree and a fairy-tale castle with a rainbow. Original designs, bold lines, ages 3 to 8.", 5,
 ["🏰 Castle Princess: in a ball gown with a crown", "🐴 Pony Ride: through a flower meadow", "🫖 Tea Party: with teddy bears", "📖 Story Time: reading under a tree", "🌈 Rainbow Castle: towers and flags"],
 "Perfect for princess birthday parties, party favors, playdates, classrooms and quiet time."))
S["VB"] = ("Valentines Day Coloring Bundle, 10 Printable Valentine Coloring Pages for Kids and Adults, Classroom and Family Valentine Activity",
 "valentine coloring,valentines bundle,valentines day kids,classroom valentine,adult coloring page,bold and easy,valentine activity,family activity,heart coloring page,valentine printable,coloring for seniors,galentines party,kids coloring pages",
 col("💝 Ten Valentine coloring pages for the whole family in one download: five cute animal pages for kids and five bold and easy love pages for adults and seniors. Color together and share the love!", 10,
 ["🧸 5 kids pages: teddy bear, puppies, kitten, unicorn and penguins", "🌹 5 bold and easy pages: roses, love birds, love letters, coffee for two and a tulip wreath"],
 "Perfect for Valentine's classrooms, family nights, grandparents and grandkids, Galentine's parties and senior centers."))
S["CY"] = ("Cottagecore Coloring Book for Adults, 20 Printable Pages, Mushrooms, Frogs, Fairy Houses, Butterflies and Cozy Cats Coloring Bundle",
 "cottagecore,coloring book,adult coloring page,fairy house,mushroom coloring,frog coloring page,butterfly coloring,cat coloring page,whimsical coloring,printable coloring,relaxing coloring,gift for her,coloring bundle",
 col("🌿 A whole cozy cottagecore coloring book in one download: 20 pages of frogs and mushrooms, fairy houses, butterfly gardens and cozy cats. A mix of detailed and bold-and-easy pages for any mood.", 20,
 ["🍄 5 Mushroom and Frog pages", "🧚 5 Fairy House pages", "🦋 5 Butterfly Garden pages", "🐈 5 Cozy Cat pages (bold and easy)"],
 "Perfect for cottagecore lovers, relaxing weekends, self-care, birthday gifts for her and long winter evenings."))

S["TG1"] = ("Thanksgiving Bingo Game Printable, 30 Word Bingo Cards with Calling List, Classroom and Family Thanksgiving Party Game PDF",
 "thanksgiving bingo,thanksgiving game,bingo cards,classroom game,family game,thanksgiving party,kids thanksgiving,printable game,friendsgiving game,fall party game,thankful activity,word bingo,group game",
 game("🦃 The easiest Thanksgiving game to set up! 30 different word bingo cards plus a calling list. Print, grab some corn kernels for markers and play while the turkey roasts.",
 ["🎯 30 unique 5x5 Thanksgiving word bingo cards", "📋 1 calling list with all 40 words", "📖 Simple how-to-play page"],
 "Perfect for Thanksgiving dinner, Friendsgiving, classroom parties, senior centers, church groups and family game night."))
S["TG2"] = ("Thanksgiving Trivia Game Printable, 40 Question Cards with Answers, Family Thanksgiving Party Game, Kids and Adults Trivia PDF",
 "thanksgiving trivia,thanksgiving game,trivia cards,family game,friendsgiving game,thanksgiving party,printable game,kids thanksgiving,classroom game,fall party game,trivia game,table game,group game",
 game("🥧 How well does your family know Thanksgiving? 40 fun trivia cards about turkeys, Pilgrims, parades, pie and more, with answers right on each card. Easy for kids, fun for grown-ups.",
 ["❓ 40 Thanksgiving trivia question cards", "✅ Answers printed on every card", "📖 How-to-play page with team rules"],
 "Perfect for Thanksgiving dinner, Friendsgiving, classrooms, office parties and family game night."))
S["TG3"] = ("Thanksgiving Would You Rather Game for Kids, 30 Printable Question Cards, Family Thanksgiving Party Game, Classroom Activity",
 "would you rather,thanksgiving game,kids thanksgiving,family game,classroom game,thanksgiving party,printable game,conversation game,friendsgiving game,fall party game,kids table game,funny questions,group game",
 game("😂 Pumpkin pie for dinner or turkey for dessert? 30 silly Thanksgiving would you rather cards that get everyone talking and laughing, from the kids' table to the grown-ups.",
 ["🤔 30 Thanksgiving would you rather cards", "📖 Simple how-to-play page"],
 "Perfect for the kids' table, Thanksgiving dinner, classrooms, car rides to grandma's and family game night."))
S["TG4"] = ("Thanksgiving Gratitude Cards Printable, 40 Table Talk Conversation Starters, Thanksgiving Dinner Game, Family Gratitude Activity",
 "gratitude cards,table talk,thanksgiving game,conversation cards,thanksgiving dinner,family activity,gratitude activity,thankful cards,friendsgiving game,dinner game,thanksgiving table,kids thanksgiving,printable cards",
 game("🍂 Turn Thanksgiving dinner into the most meaningful conversation of the year. 40 gratitude and memory questions to pass around the table: easy for kids, heartfelt for grandparents.",
 ["💬 40 Thanksgiving gratitude conversation cards", "📖 How-to-use page"],
 "Perfect for Thanksgiving dinner tables, Friendsgiving, family reunions, classrooms and church groups."))
S["TG5"] = ("Thanksgiving Word Search Puzzles, 8 Printable Fall Word Find Pages with Answer Keys, Kids Thanksgiving Activity, Classroom PDF",
 "word search,thanksgiving puzzle,turkey day fun,kids thanksgiving,classroom activity,word find,fall activity,printable puzzle,early finisher,thanksgiving kids,senior activity,fall word search,homeschool",
 game("🍁 Keep kids busy while dinner cooks! 8 Thanksgiving and fall word searches with answer keys: feast foods, harvest, giving thanks, Pilgrims, desserts and more.",
 ["🔎 8 Thanksgiving word search puzzles", "🔑 8 answer keys"],
 "Perfect for the kids' table, classrooms, early finishers, seniors, waiting rooms and travel days."))
S["TG6"] = ("Thanksgiving Games Bundle Printable, 6 Party Games, Bingo, Trivia, Charades, Would You Rather, Gratitude Cards and Word Search",
 "thanksgiving games,thanksgiving bundle,family game,thanksgiving party,friendsgiving game,thanksgiving bingo,thanksgiving trivia,kids thanksgiving,classroom game,printable game,charades game,fall party game,group game",
 game("🦃 Everything you need for a fun Thanksgiving in one download! 6 printable games for kids and adults: bingo, trivia, charades, would you rather, gratitude cards and word search.",
 ["🎯 Word Bingo: 30 cards + calling list", "❓ Trivia: 40 cards with answers", "🎭 Charades: 40 act-it-out cards", "🤔 Would You Rather: 30 cards", "💬 Gratitude Table Talk: 40 cards", "🔎 Word Search: 8 puzzles + answer keys"],
 "Perfect for Thanksgiving dinner, Friendsgiving, family reunions, classrooms and holiday parties."))
S["NY1"] = ("New Years Eve Bingo Game Printable, 30 Word Bingo Cards with Calling List, Family New Year Party Game for Kids and Adults",
 "new years eve game,new year bingo,bingo cards,family game,kids new year,new years party,printable game,nye game,classroom game,new year fun,word bingo,party game,group game",
 game("🎉 Count down to midnight with a game everyone can play! 30 different New Year's Eve word bingo cards plus a calling list. Print, play and celebrate together.",
 ["🎯 30 unique 5x5 New Year's Eve bingo cards", "📋 1 calling list with all 40 words", "📖 Simple how-to-play page"],
 "Perfect for family New Year's Eve parties, kids' countdowns, sleepovers, classrooms in January and senior centers."))
S["NY2"] = ("New Years Eve Trivia Game Printable, 40 Question Cards with Answers, Family New Year Party Game, Traditions Around the World",
 "new years trivia,new years eve game,trivia cards,family game,new years party,printable game,nye game,kids new year,party game,trivia game,new year fun,group game,classroom game",
 game("🥂 How much do you know about New Year's? 40 trivia cards about countdowns, traditions around the world, fireworks and more, with answers on every card.",
 ["❓ 40 New Year's trivia question cards", "✅ Answers printed on every card", "📖 How-to-play page with team rules"],
 "Perfect for New Year's Eve parties, family game night, classrooms, office parties and friends' get-togethers."))
S["NY3"] = ("New Years Eve Would You Rather Game, 30 Printable Question Cards for Kids and Family, New Year Party Game, Fun Countdown Activity",
 "would you rather,new years eve game,kids new year,family game,new years party,printable game,nye game,conversation game,party game,funny questions,new year fun,classroom game,group game",
 game("🎆 Stay up until midnight or wake up for the sunrise? 30 funny New Year's Eve would you rather cards to keep the party going until the countdown.",
 ["🤔 30 New Year's Eve would you rather cards", "📖 Simple how-to-play page"],
 "Perfect for family New Year's Eve, kids' countdown parties, sleepovers, classrooms and road trips."))
S["NY4"] = ("New Year Reflection Cards Printable, 40 Year in Review Conversation Questions, New Years Eve Family Game, Goal Setting Activity",
 "year in review,new year cards,reflection questions,new years eve game,conversation cards,family activity,goal setting,new year goals,new years party,table talk,journal prompts,couples game,printable cards",
 game("✨ End the year with the best conversation of the night. 40 year-in-review and dreams-for-next-year questions to share with family, friends or your partner.",
 ["💬 40 year in review conversation cards", "📖 How-to-use page"],
 "Perfect for New Year's Eve dinner, couples, families, journaling, small groups, classrooms and reflection nights."))
S["NY5"] = ("New Years Eve Word Search Puzzles, 8 Printable Word Find Pages with Answer Keys, Kids New Year Activity, January Classroom PDF",
 "word search,new year puzzle,new years eve,kids new year,classroom activity,word find,january activity,printable puzzle,early finisher,winter activity,senior activity,new year fun,homeschool",
 game("🕛 Eight New Year word searches to fill the hours before midnight, or the first week back at school: countdown, party time, fireworks, fresh start, traditions around the world and more.",
 ["🔎 8 New Year's word search puzzles", "🔑 8 answer keys"],
 "Perfect for New Year's Eve with kids, January classrooms, early finishers, seniors and travel days."))
S["NY6"] = ("New Years Eve Games Bundle Printable, 6 Family Party Games, Bingo, Trivia, Would You Rather, Reflection Cards, Goals and Word Search",
 "new years eve games,new year bundle,family game,new years party,nye game,kids new year,new year bingo,new years trivia,printable game,party game,goal setting,new year fun,group game",
 game("🎉 Your whole New Year's Eve party in one download! 6 printable games and activities for kids and adults: bingo, trivia, would you rather, year in review cards, goal cards and word search.",
 ["🎯 Word Bingo: 30 cards + calling list", "❓ Trivia: 40 cards with answers", "🤔 Would You Rather: 30 cards", "💬 Year in Review: 40 conversation cards", "🎯 Goal Cards: 30 ready-made goals", "🔎 Word Search: 8 puzzles + answer keys"],
 "Perfect for family New Year's Eve parties, kids' countdowns, friends' nights in and January classrooms."))

for k, (t, g, d) in S.items():
    tags = [x.strip() for x in g.split(',')]
    assert len(t) <= 140, (k, len(t)); assert len(tags) == 13, (k, len(tags)); assert all(len(x) <= 20 for x in tags), (k, [x for x in tags if len(x) > 20])
    open(f'seo_{k}.txt', 'w').write(f"###TITLE###\n{t}\n###TAGS###\n{','.join(tags)}\n###DESCRIPTION###\n{d}\n###END###\n")
print(len(S))

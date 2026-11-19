import json
S = {
"MO": ["a big monster truck jumping over a dirt ramp", "a monster truck crushing old cars at a stadium show", "a monster truck with huge tires driving through mud", "a smiling monster truck with flames on the side", "two monster trucks racing side by side"],
"CV": ["a happy excavator digging in the dirt", "a dump truck unloading rocks at a construction site", "a bulldozer pushing a pile of sand", "a tall crane lifting steel beams over a building", "a cement mixer truck on a city road"],
"RC": ["a race car speeding on a race track with checkered flag", "a vintage race car with a big number on the side", "go-kart racing kids with helmets", "a race car pit stop with tools and tires", "a fast sports car on a mountain road"],
"RB": ["a friendly robot waving with antenna and buttons", "a robot dog playing with a ball", "a big robot building with blocks", "a cute robot watering flowers in a garden", "a robot rocket ship with a robot pilot"],
"PI": ["a pirate ship sailing on the ocean waves", "a kid pirate with a hat and a parrot on his shoulder", "a treasure chest full of gold coins on a beach", "a pirate treasure map with an island and palm trees", "a friendly octopus with a pirate hat on a ship deck"],
"SH": ["a kid superhero with a cape flying over the city", "a girl superhero lifting a car with a big smile", "a superhero dog with a mask and cape", "two kid superheroes standing on a rooftop at night", "a kid superhero saving a kitten from a tree"],
"KD": ["a brave knight in armor with a shield", "a friendly dragon sitting next to a castle", "a knight riding a horse toward a castle", "a baby dragon hatching from an egg", "a princess knight and a dragon friend having a picnic"],
"SO": ["a kid kicking a soccer ball into a goal", "a kid shooting a basketball into a hoop", "a kid hitting a baseball with a bat", "a football player running with the ball", "sports balls and a trophy together"],
"DX": ["a cute t-rex wearing a santa hat next to a Christmas tree", "a dinosaur decorating a Christmas tree with ornaments", "a baby dinosaur opening a Christmas present", "a dinosaur pulling a sleigh full of gifts", "a dinosaur building a snowman"],
"XU": ["a cute unicorn with a Christmas wreath around its neck", "a unicorn in a snowy forest with Christmas lights", "a unicorn with a santa hat and a candy cane", "a unicorn sleigh ride under the stars", "a baby unicorn opening presents by the fireplace"],
"FU": ["a cute fairy sitting on a mushroom", "a fairy flying with a magic wand and stars", "a fairy house in a garden with flowers", "a fairy riding a butterfly", "a fairy having a tea party with a bunny"],
"BL": ["a little ballerina dancing on stage", "a ballerina in a tutu doing a pirouette", "two ballerinas holding hands", "ballet shoes and a tutu with bows", "a ballerina bunny dancing"],
"AX": ["a cute smiling axolotl swimming with bubbles", "an axolotl wearing a little crown", "an axolotl eating a strawberry", "two axolotl friends hugging", "an axolotl in a teacup"],
"SL": ["a cute sloth hanging from a tree branch", "a sloth sleeping in a hammock", "a sloth hugging a cup of hot cocoa", "a sloth reading a book", "a baby sloth on its mother's back"],
"LL": ["a cute llama with a flower crown", "a llama wearing a cozy scarf", "a llama next to a cactus", "a baby llama with balloons", "a llama with sunglasses at the beach"],
"ZO": ["a giraffe and a zebra at the zoo", "a lion family resting", "a cute monkey hanging from a branch", "a happy hippo in the water", "a panda bear eating bamboo"],
"JG": ["a cute tiger cub in the jungle", "a toucan on a tropical branch", "a smiling crocodile in the river", "an elephant spraying water", "a jungle with leaves, a parrot and a frog"],
"IN": ["a smiling ladybug on a leaf", "a happy bee flying near flowers", "a cute caterpillar eating a leaf", "a snail with a decorated shell", "a dragonfly over a pond"],
"PU": ["a cute puppy sitting with a bone", "a puppy playing with a ball", "a puppy in a basket with a bow", "a puppy splashing in a puddle", "a sleepy puppy on a pillow"],
"KT": ["a cute kitten playing with a ball of yarn", "a kitten in a teacup", "a kitten sleeping in a box", "a kitten chasing a butterfly", "two kittens sharing a fish"],
"CM": ["a tent and campfire in the forest", "kids roasting marshmallows by the campfire", "a bear cub camping with a lantern", "a canoe on a lake with mountains", "camping gear with a backpack and map"],
"HB": ["a big birthday cake with candles", "a cute bear holding birthday balloons", "presents with bows and confetti", "a birthday party hat and cupcakes", "a unicorn with a birthday cake"],
}
KID = "Black and white line art only, cute kawaii cartoon style for kids ages 3-8, very thick clean outlines and large simple open spaces to color, original characters, pure white background, no shading, no gray, no color fill, no text, no border. Portrait orientation (2:3)."
out = {}
for k, items in S.items():
    for i, s in enumerate(items, 1): out[f"{k}{i}"] = s
json.dump(out, open("p7_prompts.json", "w"), indent=0)
print(len(out))

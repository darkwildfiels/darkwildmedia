import json
KID = "Black and white line art only, cute kawaii cartoon style for kids ages 3-8, very thick clean outlines and large simple open spaces to color, pure white background, no shading, no gray, no color fill, no text, no border. Portrait orientation (2:3)."
BOLD = "Black and white line art only, bold and easy style with thick clean outlines and large open spaces to color, great for adults and seniors, pure white background, no shading, no gray, no color fill, no text, no border. Portrait orientation (2:3)."
DET = "Black and white line art only, detailed and intricate adult coloring book style with fine clean outlines and many small areas to color, pure white background, no shading, no gray, no color fill, no text, no border. Portrait orientation (2:3)."
S = {
"VK": (KID, ["a cute teddy bear hugging a big heart", "two cute puppies sharing a heart-shaped cookie", "a happy kitten holding a bunch of heart balloons", "a cute unicorn with a heart-shaped cloud and little hearts around", "a cute penguin couple holding a heart in the snow"]),
"VA": (BOLD, ["a big heart filled with roses and leaves", "two love birds sitting on a branch with hearts and flowers", "a vintage mailbox with love letters and hearts", "a coffee cup with heart latte art, cookies and a little bouquet", "a heart-shaped wreath of tulips and ribbons"]),
"KF": (KID, ["a cute smiling bubble tea cup with tapioca pearls and a straw", "cute smiling sushi rolls and onigiri on a plate", "cute smiling donuts with sprinkles stacked together", "a cute smiling ice cream cone with three scoops and a cherry", "cute smiling pancakes stack with butter and syrup and strawberries"]),
"BB": (BOLD, ["a baby elephant sitting in a meadow with flowers", "a baby fox curled up sleeping under a tree", "a baby panda eating bamboo", "a baby bunny in a basket with daisies", "a baby deer standing in tall grass with butterflies"]),
"OC": (KID, ["a happy whale swimming with bubbles", "a cute octopus waving with coral around", "a smiling sea turtle swimming over seaweed", "cute clownfish swimming around sea anemone", "a cute crab and starfish on the sandy ocean floor with shells"]),
"FL": (BOLD, ["a large simple sunflower with leaves", "a vase of tulips on a table", "a big rose with leaves", "a pot of daisies on a window sill", "a hummingbird with large simple flowers"]),
"MF": (DET, ["a cute frog sitting under a big mushroom in a mossy forest", "a frog holding a leaf umbrella among toadstools and ferns", "a mushroom cottage with a round door, flowers and snails", "a frog reading a book on a mushroom with wildflowers", "a ring of mushrooms with fireflies, ferns and a little frog"]),
"FH": (DET, ["a fairy house inside a teapot with flowers and a tiny door", "a fairy house in a hollow tree trunk with a spiral staircase and lanterns", "a fairy house made of a giant pumpkin in a garden", "a fairy cottage on a lily pad pond with dragonflies", "a fairy treehouse village with tiny bridges and lanterns"]),
"SX": (KID, ["a cute astronaut waving on the moon with stars", "a cute rocket ship flying past planets and stars", "a cute alien in a flying saucer smiling", "Saturn and other cute smiling planets in space", "a cute astronaut floating with a little space dog"]),
"ME": (KID, ["a cute little mermaid sitting on a rock with seashells", "a mermaid swimming with a happy dolphin", "a mermaid playing with fish around a coral reef", "a mermaid castle under the sea with bubbles", "a cute baby mermaid holding a big pearl in a clam shell"]),
"CT": (BOLD, ["a cat sleeping on a stack of books by a window", "a cat sitting among potted house plants", "a cat curled up in a cozy armchair with a blanket and a mug", "a cat playing with a ball of yarn in a basket", "a cat sitting on a kitchen counter with teapot and cookies"]),
"DG": (BOLD, ["a golden retriever sitting with a ball", "a dachshund lying on a cozy rug", "a corgi sitting with flowers", "a french bulldog sitting with a bone", "a beagle puppy playing in the grass"]),
"BF": (DET, ["a large butterfly with ornate patterned wings among flowers", "butterflies flying around a garden of roses and peonies", "a butterfly resting on a blooming lily with leaves", "a garden gate covered in climbing roses with butterflies", "a hummingbird and butterflies around a flowering vine"]),
"SD": (KID, ["kids building a big snowman together", "a cute kid sledding down a snowy hill", "a cute polar bear ice skating on a frozen pond", "a cute penguin making snow angels", "a cozy kid drinking hot cocoa with marshmallows by the window"]),
"LN": (KID, ["a cute little goat celebrating Lunar New Year with red lanterns", "a cute dragon dance with lanterns and fireworks", "a bowl of dumplings and chopsticks with cute faces", "a cute panda holding a red envelope and lanterns", "a cute lion dance head with drums and firecrackers"]),
"PR": (KID, ["a cute princess in a ball gown with a crown in front of a castle", "a princess riding a cute pony in a flower meadow", "a princess having a tea party with teddy bears", "a princess reading a book under a tree with birds", "a fairy-tale castle with towers, flags and a rainbow"]),
}
out = {}
for k, (st, items) in S.items():
    for i, s in enumerate(items, 1):
        out[f"{k}{i}"] = f"Create a printable coloring page: {s}. {st}"
json.dump(out, open("p6_prompts.json", "w"), indent=0)
print(len(out))

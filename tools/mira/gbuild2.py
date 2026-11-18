import os, sys
from reportlab.lib.pagesizes import letter, A4
from pypdf import PdfWriter, PdfReader
import games, games2, tools
import content2 as C
from gbuild import prev, HOW_DL

def two(key, fname, fn):
    o = f'out/{key}'; os.makedirs(o, exist_ok=True)
    p = fn(f'{o}/MiraDigital_{fname}_US-Letter.pdf', letter); fn(f'{o}/MiraDigital_{fname}_A4.pdf', A4); return p

def imgs(key, pdf, title, sub, label, cover_p, grid_p, single_p, how=HOW_DL):
    o = f'out/{key}'; cv = prev(pdf, cover_p, key)
    tools.cover2(cv, title, sub, f'{o}/01_cover.jpg', count_label=label)
    tools.grid(prev(pdf, grid_p, key), f'{o}/02_inside.jpg', "What's inside")
    tools.single(prev(pdf, [single_p], key)[0], f'{o}/03_page.jpg', sub)
    tools.info(f'{o}/04_how.jpg', "How it works", how)

def n_pages(p): return len(PdfReader(p).pages)

def G7():
    p = two('G7', 'Christmas_Scavenger_Hunt', games2.scavenger); imgs('G7', p, "Christmas Scavenger Hunt", "Indoor + Christmas lights hunts for kids", "2 HUNTS", [1, 0, 2], [0, 1, 2, 3], 0)
def G8():
    p = two('G8', 'Christmas_Charades', lambda d, ps: games2.simple_cards(d, ps, "Christmas Charades", C.CHARADES, ["Print the cards and cut them apart.", "Take turns picking a card and acting it out - no talking!", "Your team has 1 minute to guess.", "1 point for each correct guess. Most points wins!", f"{len(C.CHARADES)} cards for kids, families and parties."], label="ACT IT OUT"))
    imgs('G8', p, "Christmas Charades", f"{len(C.CHARADES)} act-it-out cards for all ages", f"{len(C.CHARADES)} CARDS", [2, 1, 3], [0, 1, 2, 3, 4, 5], 1)
def G9():
    p = two('G9', 'Christmas_Pictionary', lambda d, ps: games2.simple_cards(d, ps, "Christmas Pictionary", C.PICTIONARY, ["Print the cards and cut them apart.", "Draw a card and sketch the word - no letters or numbers!", "Your team has 1 minute to guess.", "Use paper, a whiteboard or a chalkboard.", f"{len(C.PICTIONARY)} easy words, perfect for kids and families."], label="DRAW IT", per=(3, 5)))
    imgs('G9', p, "Christmas Pictionary", f"{len(C.PICTIONARY)} drawing game word cards", f"{len(C.PICTIONARY)} CARDS", [2, 1, 3], [0, 1, 2, 3, 4], 1)
def G10():
    p = two('G10', 'Christmas_This_or_That', lambda d, ps: games2.simple_cards(d, ps, "Christmas This or That", C.THISTHAT, ["Print the cards and cut them apart.", "Read a card aloud and everyone picks one side.", "Move to the left or right side of the room, or raise your hand!", "Explain your choice for bonus laughs.", f"{len(C.THISTHAT)} questions for kids, classrooms and families."], label="THIS OR THAT"))
    imgs('G10', p, "Christmas This or That", f"{len(C.THISTHAT)} fun question cards", f"{len(C.THISTHAT)} CARDS", [2, 1, 3], [0, 1, 2, 3, 4, 5], 1)
def G11():
    p = two('G11', 'Christmas_Word_Bingo', games2.word_bingo); imgs('G11', p, "Christmas Word Bingo", "30 cards + calling list, great for classrooms", "30 CARDS", [2, 1, 3], [0, 1, 2, 3, 4, 31], 1)
def G12():
    p = two('G12', 'Christmas_Mazes', games2.mazes); imgs('G12', p, "Christmas Mazes for Kids", "20 mazes, easy to hard, with answer keys", "20 MAZES", [5, 0, 15], [0, 5, 10, 15, 19, 20], 5)
def G13():
    p = two('G13', 'Christmas_Sudoku', games2.sudoku); imgs('G13', p, "Christmas Sudoku", "30 puzzles 4x4, 6x6 and 9x9 with answers", "30 PUZZLES", [6, 1, 12], [0, 1, 6, 11, 15, 16], 6)
def G14():
    p = two('G14', 'Christmas_Word_Scramble', games2.scramble); imgs('G14', p, "Christmas Word Scramble", "5 puzzle sheets + answer key", "50 WORDS", [1, 0, 2], [0, 1, 2, 3, 4, 5], 0)
def G15():
    p = two('G15', 'Letter_to_Santa_Kit', games2.santa_kit); imgs('G15', p, "Letter to Santa Kit", "Letter, wish list, nice list certificate & reply", "4 PAGES", [2, 0, 3], [0, 1, 2, 3], 2)
def G16():
    tags = [f'colored/{k}.png' for k in ['K1', 'K2', 'B1', 'B3', 'V1', 'V3', 'S1', 'S2', 'T1', 'I1', 'H1', 'Z1', 'V5', 'K4', 'S4', 'B5', 'N1', 'U3', 'I3', 'H2', 'K3', 'S3', 'T3', 'V2']]
    import games as g
    g.icon_pool([os.path.basename(t)[:-4] for t in tags])
    cl = []
    from build import cl as clean
    for t in tags:
        k = os.path.basename(t)[:-4]; cl.append(clean(k))
    p = two('G16', 'Christmas_Coloring_Gift_Tags', lambda d, ps: games2.gift_tags(d, ps, cl)); imgs('G16', p, "Christmas Coloring Gift Tags", "24 color-your-own printable tags", "24 TAGS", [1, 0, 1], [0, 1], 0)
def G17():
    p = two('G17', 'Christmas_Countdown_Activities', games2.advent); imgs('G17', p, "Christmas Countdown Activity Cards", "25 days of family fun + coloring chart", "25 DAYS", [1, 2, 3], [0, 1, 2, 3], 1)
def G18():
    p = two('G18', 'Christmas_Conversation_Cards', lambda d, ps: games2.simple_cards(d, ps, "Christmas Conversation Cards", C.CONVO, ["Print the cards and cut them apart.", "Place them in a bowl on the dinner table.", "Take turns drawing a card and answering it.", "A sweet way to share memories and laugh together.", f"{len(C.CONVO)} questions for families, couples and friends."], label="TABLE TALK"))
    imgs('G18', p, "Christmas Conversation Cards", f"{len(C.CONVO)} table talk questions for families", f"{len(C.CONVO)} CARDS", [2, 1, 3], [0, 1, 2, 3, 4, 5], 1)
def G19():
    p = two('G19', 'Christmas_Jokes_for_Kids', lambda d, ps: games2.simple_cards(d, ps, "Christmas Jokes for Kids", C.JOKES, ["Print the cards and cut them apart.", "Read the joke, let everyone guess, then reveal the punchline!", "Perfect for lunchboxes, stockings and Christmas crackers.", f"{len(C.JOKES)} clean, kid-friendly jokes."], label="JOKE", two=True))
    imgs('G19', p, "Christmas Jokes for Kids", f"{len(C.JOKES)} lunchbox and cracker joke cards", f"{len(C.JOKES)} JOKES", [2, 1, 3], [0, 1, 2, 3, 4, 5], 1)

def bundle(key, fname, parts, title, sub, label, what_rows, cover_srcs, price_note=None):
    o = f'out/{key}'; os.makedirs(o, exist_ok=True)
    for sz in ['US-Letter', 'A4']:
        w = PdfWriter()
        for f in parts:
            for pg in PdfReader(f.replace('{sz}', sz)).pages: w.add_page(pg)
        w.write(f'{o}/MiraDigital_{fname}_{sz}.pdf')
    n = n_pages(f'{o}/MiraDigital_{fname}_US-Letter.pdf')
    pv = [prev(f.replace('{sz}', 'US-Letter'), [pg], key + str(i))[0] for i, (f, pg) in enumerate(cover_srcs)]
    tools.cover2(pv[:3], title, sub, f'{o}/01_cover.jpg', items=[label or f"{n} PAGES", "INSTANT DOWNLOAD", "US LETTER + A4", "PRINT AT HOME"])
    tools.grid(pv, f'{o}/02_inside.jpg', "What's inside")
    tools.info(f'{o}/03_what.jpg', "What's included", what_rows)
    tools.info(f'{o}/04_how.jpg', "How it works", HOW_DL)
    return n


def P(k, n): return f'out/{k}/MiraDigital_{n}_{{sz}}.pdf'
def GB():
    parts = [P('G1','Christmas_Picture_Bingo'), P('G11','Christmas_Word_Bingo'), P('G3','Christmas_Word_Search'), P('G4','Christmas_Trivia'), P('G5','Christmas_Would_You_Rather'), P('G8','Christmas_Charades'), P('G9','Christmas_Pictionary'), P('G10','Christmas_This_or_That'), P('G14','Christmas_Word_Scramble'), P('G18','Christmas_Conversation_Cards')]
    bundle('GB', 'Christmas_Games_Mega_Bundle', parts, "Christmas Games Mega Bundle", "10 printable party games for the whole family", "10 GAMES",
        [("Bingo x2", "Picture bingo + word bingo, 60 cards"), ("Cards & Talk", "Trivia, charades, pictionary, this or that, conversation"), ("Puzzles", "Word search, word scramble, would you rather")],
        [(parts[0], 1), (parts[5], 1), (parts[2], 0), (parts[3], 1), (parts[6], 1), (parts[1], 1)])
def KA():
    parts = [P('G12','Christmas_Mazes'), P('G13','Christmas_Sudoku'), P('G14','Christmas_Word_Scramble'), P('G7','Christmas_Scavenger_Hunt'), P('G15','Letter_to_Santa_Kit'), P('G17','Christmas_Countdown_Activities'), P('G19','Christmas_Jokes_for_Kids'), 'out/V/MiraDigital_V_{sz}.pdf', 'out/Z/MiraDigital_Z_{sz}.pdf']
    bundle('KA', 'Kids_Christmas_Activity_Mega_Pack', parts, "Kids Christmas Activity Mega Pack", "Mazes, sudoku, games, Santa letter & coloring", None,
        [("Puzzles", "20 mazes, 30 sudoku, word scramble"), ("Christmas Fun", "Santa letter kit, 25-day countdown, jokes, scavenger hunt"), ("Coloring", "10 cute animal and truck pages")],
        [(parts[0], 5), (parts[4], 2), (parts[7], 2), (parts[1], 1), (parts[5], 1), (parts[3], 0)])
def CR():
    parts = [P('G11','Christmas_Word_Bingo'), P('G12','Christmas_Mazes'), P('G14','Christmas_Word_Scramble'), P('G10','Christmas_This_or_That'), P('G17','Christmas_Countdown_Activities'), P('G19','Christmas_Jokes_for_Kids'), P('G3','Christmas_Word_Search')]
    bundle('CR', 'Christmas_Classroom_Party_Pack', parts, "Christmas Classroom Party Pack", "Bingo, mazes, word games & countdown for teachers", "7 ACTIVITIES",
        [("Whole-class games", "30-card word bingo, this or that, jokes"), ("Early finishers", "20 mazes, word search, word scramble"), ("December countdown", "25 daily activity cards")],
        [(parts[0], 1), (parts[1], 5), (parts[6], 0), (parts[3], 1), (parts[4], 1), (parts[2], 0)])
def SP():
    parts = [P('G2','Large_Print_Christmas_Bingo'), P('G3','Christmas_Word_Search'), P('G4','Christmas_Trivia'), P('G18','Christmas_Conversation_Cards'), 'out/L/MiraDigital_L_{sz}.pdf', 'out/S/MiraDigital_S_{sz}.pdf', 'out/BI/MiraDigital_BI_{sz}.pdf']
    bundle('SP', 'Christmas_Activity_Pack_for_Seniors', parts, "Christmas Activity Pack for Seniors", "Large print bingo, puzzles, trivia & coloring", "7 ACTIVITIES",
        [("Games", "Large print bingo, trivia, conversation cards"), ("Puzzles", "10 Christmas word searches"), ("Coloring", "15 large print and bold & easy pages")],
        [(parts[0], 1), (parts[4], 2), (parts[1], 0), (parts[2], 1), (parts[6], 2), (parts[5], 2)])

if __name__ == '__main__':
    for k in sys.argv[1:]: globals()[k](); print(k, sorted(os.listdir(f'out/{k}')))

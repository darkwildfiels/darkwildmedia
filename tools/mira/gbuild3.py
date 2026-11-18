import os, sys, random
from reportlab.lib.pagesizes import letter, A4
from pypdf import PdfWriter, PdfReader
import games, games2, tools
import content3 as C
from games import header, footer, _wrap, INK, CREAM
from gbuild import prev, HOW_DL
from gbuild2 import two, imgs, n_pages, bundle

PAL = {"TG": ((0.72, 0.33, 0.10), (0.40, 0.45, 0.18)), "NY": ((0.12, 0.16, 0.38), (0.76, 0.58, 0.18))}
def pal(t):
    r, g = PAL[t]
    for m in (games, games2): m.RED = r; m.GREEN = g

def word_bingo(dst, ps, words, title, head, n=30, seed=3):
    rnd = random.Random(seed); c, W, H = games2._new(dst, ps, title)
    games2._howto(c, W, H, title, ["Print one card per player and the calling list.", "The caller reads a word from the list and crosses it off.",
        "Players mark the word if it is on their card.", "First to complete a row, column or diagonal shouts BINGO!", f"{n} different cards included. Great for reading practice too!"])
    for ci in range(n):
        pick = rnd.sample(words, 24); c.setFillColorRGB(*CREAM); c.rect(0, 0, W, H, fill=1, stroke=0)
        header(c, W, H, head, f"Card {ci + 1}"); m = 50; cell = (W - 2 * m) / 5; top = H - 120
        c.setFont("PopB", 34); c.setFillColorRGB(*games.RED)
        for j, L in enumerate("BINGO"): c.drawCentredString(m + cell * j + cell / 2, top - 38, L)
        top -= 50; it = iter(pick)
        for r in range(5):
            for col in range(5):
                x = m + col * cell; y = top - (r + 1) * cell
                c.setFillColorRGB(1, 1, 1); c.setStrokeColorRGB(*games.GREEN); c.setLineWidth(2.5); c.rect(x, y, cell, cell, fill=1, stroke=1)
                if r == 2 and col == 2: c.setFillColorRGB(*games.RED); c.setFont("PopB", 22); c.drawCentredString(x + cell / 2, y + cell / 2 - 8, "FREE"); continue
                w = next(it); c.setFillColorRGB(*INK); fs = 15 if len(w) < 9 else 11.5
                _wrap(c, w, x + 6, y + cell / 2, cell - 12, "PopB", fs, center=True)
        footer(c, W); c.showPage()
    header(c, W, H, "Calling List", "Cross off each word as you call it"); c.setFont("PopB", 15); c.setFillColorRGB(*INK)
    for i, w in enumerate(sorted(words)):
        c.drawString(80 + (i % 2) * 240, H - 140 - (i // 2) * 27, "[ ]  " + w)
    footer(c, W); c.showPage(); c.save(); return dst

def ws_pdf(dst, ps, puzzles, title):
    games.wordsearch_pdf(dst, puzzles, pagesize=ps, title=title); return dst

HOWC = lambda n, what: ["Print the cards and cut them apart.", "Place them in a bowl on the table.", "Take turns drawing a card and answering it.", "A sweet way to share memories and laugh together.", f"{n} {what}."]

def gen(t, pre):
    pal(t); B = getattr(C, t + "_BINGO"); TR = getattr(C, t + "_TRIVIA"); WY = getattr(C, t + "_WYR"); CV = getattr(C, t + "_CONVO"); WS = getattr(C, t + "_WS")
    name = {"TG": "Thanksgiving", "NY": "New Years Eve"}[t]; disp = {"TG": "Thanksgiving", "NY": "New Year's Eve"}[t]
    k = f"{t}1"; p = two(k, f"{name.replace(' ', '_')}_Word_Bingo", lambda d, ps: word_bingo(d, ps, B, f"{disp} Word Bingo", f"{disp.upper()} BINGO"))
    imgs(k, p, f"{disp} Word Bingo", "30 cards + calling list, great for classrooms", "30 CARDS", [2, 1, 3], [0, 1, 2, 3, 4, 31], 1)
    k = f"{t}2"; p = two(k, f"{name.replace(' ', '_')}_Trivia", lambda d, ps: games.cards_pdf(d, f"{disp} Trivia", TR, pagesize=ps, kind="trivia"))
    imgs(k, p, f"{disp} Trivia Game", f"{len(TR)} question cards with answers", f"{len(TR)} CARDS", [2, 1, 3], [0, 1, 2, 3, 4, 5], 1)
    k = f"{t}3"; p = two(k, f"{name.replace(' ', '_')}_Would_You_Rather", lambda d, ps: games.cards_pdf(d, f"{disp} Would You Rather", WY, pagesize=ps, kind="wyr"))
    imgs(k, p, f"{disp} Would You Rather", f"{len(WY)} silly question cards for all ages", f"{len(WY)} CARDS", [2, 1, 3], [0, 1, 2, 3, 4], 1)
    k = f"{t}4"
    if t == "TG":
        p = two(k, "Thanksgiving_Gratitude_Conversation_Cards", lambda d, ps: games2.simple_cards(d, ps, "Thanksgiving Table Talk", CV, HOWC(len(CV), "gratitude questions for families and friends"), label="GRATITUDE"))
        imgs(k, p, "Thanksgiving Gratitude Cards", f"{len(CV)} table talk questions for the dinner table", f"{len(CV)} CARDS", [2, 1, 3], [0, 1, 2, 3, 4, 5], 1)
    else:
        p = two(k, "New_Year_Reflection_Conversation_Cards", lambda d, ps: games2.simple_cards(d, ps, "Year in Review Questions", CV, HOWC(len(CV), "reflection questions for families, friends and couples"), label="YEAR IN REVIEW"))
        imgs(k, p, "New Year Reflection Cards", f"{len(CV)} year in review questions for the family", f"{len(CV)} CARDS", [2, 1, 3], [0, 1, 2, 3, 4, 5], 1)
    k = f"{t}5"; p = two(k, f"{name.replace(' ', '_')}_Word_Search", lambda d, ps: ws_pdf(d, ps, WS, f"{disp} Word Search"))
    imgs(k, p, f"{disp} Word Search", f"{len(WS)} puzzles with answer keys", f"{len(WS)} PUZZLES", [1, 0, 2], [0, 1, 2, 3, 8, 9], 0)
    # extra part for bundle
    if t == "TG":
        ex = two("TGx", "Thanksgiving_Charades", lambda d, ps: games2.simple_cards(d, ps, "Thanksgiving Charades", C.TG_CHARADES, ["Print the cards and cut them apart.", "Take turns picking a card and acting it out - no talking!", "Your team has 1 minute to guess.", "1 point for each correct guess. Most points wins!", f"{len(C.TG_CHARADES)} cards for kids, families and parties."], label="ACT IT OUT"))
        exn = "Thanksgiving_Charades"
    else:
        ex = two("NYx", "New_Year_Goal_Cards", lambda d, ps: games2.simple_cards(d, ps, "New Year Goal Cards", C.NY_GOALS, ["Print the cards and cut them apart.", "Pick the goals that feel right for you this year.", "Stick them on the fridge, a mirror or in your planner.", "Check in once a month and celebrate your progress!", f"{len(C.NY_GOALS)} ready-made goals for kids, teens and families."], label="MY GOAL"))
        exn = "New_Year_Goal_Cards"
    P = lambda kk, n: f'out/{kk}/MiraDigital_{n}_{{sz}}.pdf'
    N = name.replace(' ', '_')
    parts = [P(f"{t}1", f"{N}_Word_Bingo"), P(f"{t}2", f"{N}_Trivia"), P(f"{t}3", f"{N}_Would_You_Rather"),
             P(f"{t}4", "Thanksgiving_Gratitude_Conversation_Cards" if t == "TG" else "New_Year_Reflection_Conversation_Cards"), P(f"{t}5", f"{N}_Word_Search"), P(f"{t}x", exn)]
    if t == "TG":
        bundle("TG6", "Thanksgiving_Party_Games_Bundle", parts, "Thanksgiving Games Bundle", "6 printable games for the whole family", "6 GAMES",
               [("Bingo + Charades", "30 bingo cards, 40 act-it-out cards"), ("Trivia + Would You Rather", "40 trivia + 30 silly questions"), ("Gratitude + Word Search", "40 table talk cards, 8 puzzles")],
               [(parts[0], 1), (parts[5], 1), (parts[4], 0), (parts[1], 1), (parts[3], 1), (parts[2], 1)])
    else:
        bundle("NY6", "New_Years_Eve_Party_Games_Bundle", parts, "New Year's Eve Games Bundle", "6 printable games & activities for the family", "6 GAMES",
               [("Bingo + Trivia", "30 bingo cards, 40 trivia questions"), ("Would You Rather + Reflection", "30 silly questions, 40 year in review cards"), ("Puzzles + Goals", "8 word searches, 30 goal cards")],
               [(parts[0], 1), (parts[1], 1), (parts[4], 0), (parts[5], 1), (parts[3], 1), (parts[2], 1)])

if __name__ == '__main__':
    for t in sys.argv[1:]: gen(t, None); print(t, 'ok')

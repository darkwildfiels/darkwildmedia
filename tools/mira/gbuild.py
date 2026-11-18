import os, sys, subprocess
from reportlab.lib.pagesizes import letter, A4
from pypdf import PdfWriter, PdfReader
import games, tools
from games_content import TRIVIA, WYR, WS

XMAS = [f'{s}{i}' for s in 'ABHIKST' for i in range(1, 6)]
SENIOR = [f'{s}{i}' for s in 'SLK' for i in range(1, 6)] + ['H1', 'H2', 'I1', 'I2', 'T1', 'T2', 'B1', 'B3', 'A1', 'A3']

def pdfs(key, fname, fn):
    o = f'out/{key}'; os.makedirs(o, exist_ok=True)
    L = fn(f'{o}/{fname}_US-Letter.pdf', letter); fn(f'{o}/{fname}_A4.pdf', A4); return L

def prev(pdf, pages, key):
    out = []
    for p in pages:
        dst = f'/tmp/pv_{key}_{p}.png'; games.pdf_preview(pdf, p, dst, w=1400); out.append(dst)
    return out

def images(key, pdf, title, sub, label, cover_pages, grid_pages, how, single_page):
    o = f'out/{key}'
    cv = prev(pdf, cover_pages, key)
    tools.cover2(cv, title, sub, f'{o}/01_cover.jpg', count_label=label)
    tools.grid(prev(pdf, grid_pages, key), f'{o}/02_inside.jpg', "What's inside")
    tools.single(prev(pdf, [single_page], key)[0], f'{o}/03_page.jpg', sub)
    tools.info(f'{o}/04_how.jpg', "How it works", how)

HOW_DL = [("Buy & download", "Instant PDF download - US Letter and A4"), ("Print at home", "Any home printer, or a local print shop"),
          ("Play & enjoy", "Perfect for parties, classrooms and family night")]

def G1():
    ic = games.icon_pool(XMAS)
    f = lambda d, ps: games.bingo_pdf(d, ic, 30, pagesize=ps)
    p = pdfs('G1', 'MiraDigital_Christmas_Picture_Bingo', f)
    images('G1', p, "Christmas Picture Bingo", "30 printable bingo cards + calling cards", "30 CARDS", [2, 1, 3], [1, 2, 3, 4, 5, 31], HOW_DL, 1)

def G2():
    ic = games.icon_pool(SENIOR)
    f = lambda d, ps: games.bingo_pdf(d, ic, 20, grid=3, title="CHRISTMAS BINGO", pagesize=ps, big=True, seed=11)
    p = pdfs('G2', 'MiraDigital_Large_Print_Christmas_Bingo', f)
    images('G2', p, "Large Print Christmas Bingo", "Big, simple 3x3 cards for seniors", "20 CARDS", [2, 1, 3], [1, 2, 3, 4, 21, 22],
           [("Big pictures", "Large 3x3 cards, easy to see and mark"), ("Easy to play", "Great for seniors, memory care and kids"), ("Print & play", "US Letter and A4 PDF, print as many as you need")], 1)

def G3():
    f = lambda d, ps: games.wordsearch_pdf(d, WS, pagesize=ps)
    p = pdfs('G3', 'MiraDigital_Christmas_Word_Search', f)
    images('G3', p, "Christmas Word Search", "10 puzzles with answer keys", "10 PUZZLES", [1, 0, 2], [0, 1, 2, 3, 4, 10], HOW_DL, 0)

def G4():
    f = lambda d, ps: games.cards_pdf(d, "Christmas Trivia", TRIVIA, pagesize=ps, kind="trivia")
    p = pdfs('G4', 'MiraDigital_Christmas_Trivia', f)
    images('G4', p, "Christmas Trivia Game", "50 question cards with answers", "50 CARDS", [2, 1, 3], [0, 1, 2, 3, 4, 5], HOW_DL, 1)

def G5():
    f = lambda d, ps: games.cards_pdf(d, "Christmas Would You Rather", WYR, pagesize=ps, kind="wyr")
    p = pdfs('G5', 'MiraDigital_Christmas_Would_You_Rather', f)
    images('G5', p, "Christmas Would You Rather", "40 fun question cards for kids & family", "40 CARDS", [2, 1, 3], [0, 1, 2, 3, 4, 5], HOW_DL, 1)

def G6():
    o = 'out/G6'; os.makedirs(o, exist_ok=True)
    for sz in ['US-Letter', 'A4']:
        w = PdfWriter()
        for k, n in [('G1', 'Christmas_Picture_Bingo'), ('G3', 'Christmas_Word_Search'), ('G4', 'Christmas_Trivia'), ('G5', 'Christmas_Would_You_Rather')]:
            for pg in PdfReader(f'out/{k}/MiraDigital_{n}_{sz}.pdf').pages: w.add_page(pg)
        w.write(f'{o}/MiraDigital_Christmas_Party_Games_Bundle_{sz}.pdf')
    pv = [prev(f'out/{k}/MiraDigital_{n}_US-Letter.pdf', [p], k)[0] for k, n, p in
          [('G3', 'Christmas_Word_Search', 0), ('G1', 'Christmas_Picture_Bingo', 1), ('G5', 'Christmas_Would_You_Rather', 1)]]
    tools.cover2(pv, "Christmas Party Games Bundle", "Bingo, word search, trivia & would you rather", f'{o}/01_cover.jpg', count_label="4 GAMES")
    gp = [prev(f'out/{k}/MiraDigital_{n}_US-Letter.pdf', [p], k)[0] for k, n, p in
          [('G1', 'Christmas_Picture_Bingo', 1), ('G1', 'Christmas_Picture_Bingo', 31), ('G3', 'Christmas_Word_Search', 0), ('G3', 'Christmas_Word_Search', 10), ('G4', 'Christmas_Trivia', 1), ('G5', 'Christmas_Would_You_Rather', 1)]]
    tools.grid(gp, f'{o}/02_inside.jpg', "4 games in one download")
    tools.info(f'{o}/03_what.jpg', "What's included", [("Picture Bingo", "30 cards + calling cards"), ("Word Search", "10 puzzles + answer keys"), ("Trivia + Would You Rather", "50 trivia + 40 would you rather cards")])
    tools.info(f'{o}/04_how.jpg', "How it works", HOW_DL)

if __name__ == '__main__':
    for k in sys.argv[1:]: globals()[k](); print(k, sorted(os.listdir(f'out/{k}')))

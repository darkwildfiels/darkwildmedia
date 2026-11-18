import random
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from games import header, footer, _wrap, RED, GREEN, INK, CREAM, GOLD, word_search
import content2 as C

def _new(dst, ps, title):
    c = canvas.Canvas(dst, pagesize=ps); c.setTitle(title); c.setAuthor("Mira Digital"); return c, ps[0], ps[1]

def _howto(c, W, H, title, lines):
    header(c, W, H, title, "How to play"); c.setFillColorRGB(*INK); c.setFont("Pop", 12.5); y = H - 130
    for t in lines: c.drawString(70, y, t); y -= 24
    footer(c, W); c.showPage()

def simple_cards(dst, ps, title, items, how, label=None, two=False, per=(2, 4)):
    """items: str or (a,b). two=True -> joke/answer or this/that."""
    c, W, H = _new(dst, ps, title); _howto(c, W, H, title, how)
    cols, rows = per; cw = (W - 70) / cols; ch = (H - 120) / rows
    for s in range(0, len(items), cols * rows):
        c.setFillColorRGB(*CREAM); c.rect(0, 0, W, H, fill=1, stroke=0); header(c, W, H, title, None, 22)
        for i, it in enumerate(items[s:s + cols * rows]):
            x = 35 + (i % cols) * cw; y = H - 90 - (i // cols + 1) * ch
            c.setFillColorRGB(1, 1, 1); c.setStrokeColorRGB(*GREEN); c.setLineWidth(2); c.roundRect(x + 6, y + 6, cw - 12, ch - 12, 12, fill=1, stroke=1)
            c.setFillColorRGB(*RED); c.setFont("PopB", 10); c.drawString(x + 20, y + ch - 30, f"#{s + i + 1}" + (f"  {label}" if label else ""))
            c.setFillColorRGB(*INK)
            if label == "THIS OR THAT":
                a, b = it; yy = _wrap(c, a, x + 20, y + ch - 70, cw - 40, "PopB", 15, center=True)
                c.setFillColorRGB(*RED); c.setFont("PopB", 13); c.drawCentredString(x + cw / 2, yy - 6, "OR")
                c.setFillColorRGB(*INK); _wrap(c, b, x + 20, yy - 32, cw - 40, "PopB", 15, center=True)
            elif two:
                q, a = it; _wrap(c, q, x + 20, y + ch - 56, cw - 40, "PopB", 13, center=True)
                c.setFillColorRGB(*GREEN); _wrap(c, a, x + 20, y + 34, cw - 40, "Pop", 11.5, center=True)
            else:
                _wrap(c, it, x + 20, y + ch / 2 + 6, cw - 40, "PopB", 17, center=True)
        footer(c, W); c.showPage()
    c.save(); return dst

def word_bingo(dst, ps, n=30, seed=3, title="CHRISTMAS WORD BINGO"):
    rnd = random.Random(seed); c, W, H = _new(dst, ps, title.title())
    _howto(c, W, H, title.title(), ["Print one card per player and the calling list.", "The caller reads a word from the list and crosses it off.",
        "Players mark the word if it is on their card.", "First to complete a row, column or diagonal shouts BINGO!", f"{n} different cards included. Great for reading practice too!"])
    for ci in range(n):
        pick = rnd.sample(C.WORD_BINGO, 24); c.setFillColorRGB(*CREAM); c.rect(0, 0, W, H, fill=1, stroke=0)
        header(c, W, H, "CHRISTMAS BINGO", f"Card {ci + 1}"); m = 50; cell = (W - 2 * m) / 5; top = H - 120
        c.setFont("PopB", 34); c.setFillColorRGB(*RED)
        for j, L in enumerate("BINGO"): c.drawCentredString(m + cell * j + cell / 2, top - 38, L)
        top -= 50; it = iter(pick)
        for r in range(5):
            for col in range(5):
                x = m + col * cell; y = top - (r + 1) * cell
                c.setFillColorRGB(1, 1, 1); c.setStrokeColorRGB(*GREEN); c.setLineWidth(2.5); c.rect(x, y, cell, cell, fill=1, stroke=1)
                if r == 2 and col == 2: c.setFillColorRGB(*RED); c.setFont("PopB", 22); c.drawCentredString(x + cell / 2, y + cell / 2 - 8, "FREE"); continue
                w = next(it); c.setFillColorRGB(*INK); fs = 15 if len(w) < 9 else 11.5
                _wrap(c, w, x + 6, y + cell / 2, cell - 12, "PopB", fs, center=True)
        footer(c, W); c.showPage()
    header(c, W, H, "Calling List", "Cross off each word as you call it"); c.setFont("PopB", 15); c.setFillColorRGB(*INK)
    for i, w in enumerate(sorted(C.WORD_BINGO)):
        c.drawString(80 + (i % 2) * 240, H - 140 - (i // 2) * 27, "□  " + w)
    footer(c, W); c.showPage(); c.save(); return dst

def _maze(n, rnd):
    vis = [[False] * n for _ in range(n)]; walls = {}
    def key(a, b): return tuple(sorted([a, b]))
    st = [(0, 0)]; vis[0][0] = True; opened = set()
    while st:
        r, cc = st[-1]; nb = [(r + dr, cc + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)) if 0 <= r + dr < n and 0 <= cc + dc < n and not vis[r + dr][cc + dc]]
        if nb: q = rnd.choice(nb); opened.add(key((r, cc), q)); vis[q[0]][q[1]] = True; st.append(q)
        else: st.pop()
    # solve
    from collections import deque
    prev = {(0, 0): None}; dq = deque([(0, 0)])
    while dq:
        u = dq.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            v = (u[0] + dr, u[1] + dc)
            if v in prev or not (0 <= v[0] < n and 0 <= v[1] < n) or key(u, v) not in opened: continue
            prev[v] = u; dq.append(v)
    path = []; u = (n - 1, n - 1)
    while u: path.append(u); u = prev[u]
    return opened, path[::-1]

def mazes(dst, ps, count=20, seed=5):
    rnd = random.Random(seed); c, W, H = _new(dst, ps, "Christmas Mazes")
    names = ["Help the elf find the present", "Help Santa reach the chimney", "Help the reindeer find the carrot", "Help the snowman find his hat", "Help the penguin find the igloo"]
    sols = []
    for i in range(count):
        n = 8 + (i * 12) // count; op, path = _maze(n, rnd); sols.append((n, op, path))
        header(c, W, H, f"Maze {i + 1}", names[i % len(names)] + ("  -  Easy" if n < 11 else "  -  Medium" if n < 15 else "  -  Hard"))
        _draw_maze(c, W, H, n, op, None); footer(c, W); c.showPage()
    for i, (n, op, path) in enumerate(sols):
        header(c, W, H, f"Answer Key - Maze {i + 1}"); _draw_maze(c, W, H, n, op, path); footer(c, W); c.showPage()
    c.save(); return dst

def _draw_maze(c, W, H, n, opened, path):
    size = min(W - 120, H - 230); cs = size / n; x0 = (W - size) / 2; y0 = H - 140
    def key(a, b): return tuple(sorted([a, b]))
    c.setStrokeColorRGB(*INK); c.setLineWidth(3 if n < 12 else 2.2); c.setLineCap(1)
    for r in range(n):
        for col in range(n):
            x = x0 + col * cs; y = y0 - r * cs
            if r == 0 and col != 0: c.line(x, y, x + cs, y)
            if col == 0 and r != 0: c.line(x, y, x, y - cs)
            if col == n - 1 and r != n - 1: c.line(x + cs, y, x + cs, y - cs)
            if r == n - 1 and col != n - 1: c.line(x, y - cs, x + cs, y - cs)
            if col < n - 1 and key((r, col), (r, col + 1)) not in opened: c.line(x + cs, y, x + cs, y - cs)
            if r < n - 1 and key((r, col), (r + 1, col)) not in opened: c.line(x, y - cs, x + cs, y - cs)
    c.setFillColorRGB(*GREEN); c.setFont("PopB", 13); c.drawString(x0 - 4, y0 + 8, "START")
    c.setFillColorRGB(*RED); c.drawRightString(x0 + size + 4, y0 - size - 22, "FINISH")
    if path:
        c.setStrokeColorRGB(*RED); c.setLineWidth(max(2, cs * 0.25))
        pts = [(x0 + q[1] * cs + cs / 2, y0 - q[0] * cs - cs / 2) for q in path]
        for a, b in zip(pts, pts[1:]): c.line(a[0], a[1], b[0], b[1])

def _sudoku(n, rnd, holes):
    import itertools
    br, bc = (2, 2) if n == 4 else (2, 3) if n == 6 else (3, 3)
    base = [[(bc * (r % br) + r // br + col) % n for col in range(n)] for r in range(n)]
    sym = list(range(1, n + 1)); rnd.shuffle(sym)
    g = [[sym[v] for v in row] for row in base]
    puz = [row[:] for row in g]; cells = [(r, col) for r in range(n) for col in range(n)]; rnd.shuffle(cells)
    for r, col in cells[:holes]: puz[r][col] = 0
    return puz, g, br, bc

def sudoku(dst, ps, seed=9):
    rnd = random.Random(seed); c, W, H = _new(dst, ps, "Christmas Sudoku")
    _howto(c, W, H, "Christmas Sudoku", ["Fill every row, column and box so each number appears once.", "4x4 puzzles use numbers 1-4 (great for kids 5+).", "6x6 puzzles use 1-6, and 9x9 puzzles use 1-9.", "Answer keys are at the back. 30 puzzles in all!"])
    allp = []
    for n, k, holes in ((4, 10, 8), (6, 10, 16), (9, 10, 45)):
        for i in range(k): allp.append((n,) + _sudoku(n, rnd, holes))
    def draw(items, ans=False):
        for s in range(0, len(items), 2):
            header(c, W, H, "Christmas Sudoku" + (" - Answers" if ans else ""))
            for j, (n, puz, sol, br, bc) in enumerate(items[s:s + 2]):
                size = min(W - 200, (H - 200) / 2 - 40); cs = size / n; x0 = (W - size) / 2; y0 = H - 120 - j * (size + 60)
                c.setFillColorRGB(*RED); c.setFont("PopB", 12); c.drawString(x0, y0 + 6, f"Puzzle {s + j + 1}  ({n}x{n})")
                for r in range(n):
                    for col in range(n):
                        x = x0 + col * cs; y = y0 - (r + 1) * cs; c.setStrokeColorRGB(*INK); c.setLineWidth(0.8); c.rect(x, y, cs, cs)
                        v = (sol if ans else puz)[r][col]
                        if v: c.setFillColorRGB(*(INK if puz[r][col] else GREEN)); c.setFont("PopB", cs * 0.5); c.drawCentredString(x + cs / 2, y + cs * 0.3, str(v))
                c.setLineWidth(2.6)
                for r in range(0, n + 1, br): c.line(x0, y0 - r * cs, x0 + size, y0 - r * cs)
                for col in range(0, n + 1, bc): c.line(x0 + col * cs, y0, x0 + col * cs, y0 - size)
            footer(c, W); c.showPage()
    draw(allp); draw(allp, True); c.save(); return dst

def scramble(dst, ps, seed=4):
    rnd = random.Random(seed); c, W, H = _new(dst, ps, "Christmas Word Scramble"); keys = []
    for name, words in C.SCRAMBLE:
        header(c, W, H, "Christmas Word Scramble", name); y = H - 140; out = []
        for i, w in enumerate(words):
            s = list(w)
            while ''.join(s) == w: rnd.shuffle(s)
            c.setFillColorRGB(*RED); c.setFont("PopB", 20); c.drawString(80, y, f"{i + 1}.  {''.join(s)}")
            c.setStrokeColorRGB(*GREEN); c.setLineWidth(1.5); c.line(330, y - 4, W - 80, y - 4); y -= (H - 230) / 10; out.append(w)
        keys.append((name, out)); footer(c, W); c.showPage()
    header(c, W, H, "Answer Key"); y = H - 130
    for name, out in keys:
        c.setFillColorRGB(*RED); c.setFont("PopB", 13); c.drawString(70, y, name); c.setFillColorRGB(*INK); c.setFont("Pop", 11.5)
        c.drawString(70, y - 18, ", ".join(out)); y -= 60
    footer(c, W); c.showPage(); c.save(); return dst

def santa_kit(dst, ps):
    c, W, H = _new(dst, ps, "Letter to Santa Kit")
    def border():
        c.setStrokeColorRGB(*RED); c.setLineWidth(6); c.rect(25, 25, W - 50, H - 50); c.setStrokeColorRGB(*GREEN); c.setLineWidth(2); c.rect(35, 35, W - 70, H - 70)
    def lines(y0, n, gap=30, x0=70):
        c.setStrokeColorRGB(0.75, 0.75, 0.75); c.setLineWidth(1)
        for i in range(n): c.line(x0, y0 - i * gap, W - 70, y0 - i * gap)
    # 1 letter
    border(); header(c, W, H, "Dear Santa,", "A letter from me to the North Pole")
    c.setFillColorRGB(*INK); c.setFont("Pop", 14); y = H - 140
    for t in ["My name is _____________________________   I am _______ years old.", "This year I have been very  □ good   □ nice   □ mostly nice!", "The kindest thing I did this year was:"]:
        c.drawString(70, y, t); y -= 34
    lines(y - 6, 3); y -= 120; c.drawString(70, y, "For Christmas I would really love:"); lines(y - 36, 5); y -= 210
    c.drawString(70, y, "Love,  ___________________________"); footer(c, W); c.showPage()
    # 2 wish list
    border(); header(c, W, H, "My Christmas Wish List"); c.setFont("PopB", 16)
    for i in range(10):
        y = H - 150 - i * 52; c.setFillColorRGB(*RED); c.drawString(80, y, f"{i + 1}."); c.setStrokeColorRGB(0.75, 0.75, 0.75); c.line(110, y - 4, W - 80, y - 4)
    footer(c, W); c.showPage()
    # 3 nice list certificate (landscape-feel inside portrait)
    border(); c.setFillColorRGB(*GOLD); c.setFont("Lora", 46); c.drawCentredString(W / 2, H - 170, "Official Nice List")
    c.setFillColorRGB(*RED); c.setFont("Lora", 30); c.drawCentredString(W / 2, H - 215, "Certificate")
    c.setFillColorRGB(*INK); c.setFont("Pop", 16); c.drawCentredString(W / 2, H - 300, "This certifies that")
    c.setStrokeColorRGB(*INK); c.line(140, H - 360, W - 140, H - 360)
    for i, t in enumerate(["has been checked twice and is officially", "on Santa's NICE LIST this year", "for kindness, helpfulness and holiday cheer!"]):
        c.drawCentredString(W / 2, H - 410 - i * 26, t)
    c.setFont("Pop", 12); c.drawString(110, 170, "Date: ________________"); c.drawRightString(W - 110, 170, "Signed: Santa Claus")
    c.setFillColorRGB(*RED); c.circle(W / 2, 140, 38, fill=1, stroke=0); c.setFillColorRGB(1, 1, 1); c.setFont("PopB", 11); c.drawCentredString(W / 2, 143, "NORTH"); c.drawCentredString(W / 2, 129, "POLE")
    c.showPage()
    # 4 reply letter
    border(); header(c, W, H, "A Letter from Santa", "Fill in the blanks to make it personal")
    c.setFillColorRGB(*INK); c.setFont("Pop", 14); txt = ["Dear ____________________,", "", "Ho ho ho! Thank you for your wonderful letter. The elves and I", "have been watching, and I am so proud of you this year,", "especially when you _____________________________________.", "", "Mrs. Claus says hello, and the reindeer are practicing their", "flying for the big night. ________________ is my favorite helper!", "", "Remember to be kind, to share, and to go to sleep early on", "Christmas Eve. I'll see you very soon!", "", "Love,", "Santa Claus"]
    y = H - 150
    for t in txt: c.drawString(80, y, t); y -= 28
    footer(c, W); c.showPage(); c.save(); return dst

def gift_tags(dst, ps, imgs):
    c, W, H = _new(dst, ps, "Christmas Coloring Gift Tags"); cols, rows = 3, 4; cw = (W - 60) / cols; ch = (H - 110) / rows
    for p in range(0, len(imgs), cols * rows):
        header(c, W, H, "Color-Your-Own Gift Tags", "Cut along the dashed lines", 24)
        for i, im in enumerate(imgs[p:p + cols * rows]):
            x = 30 + (i % cols) * cw; y = H - 95 - (i // cols + 1) * ch
            c.setDash(4, 4); c.setStrokeColorRGB(0.5, 0.5, 0.5); c.roundRect(x + 6, y + 6, cw - 12, ch - 12, 14); c.setDash()
            c.circle(x + cw / 2, y + ch - 22, 5)
            c.drawImage(ImageReader(im), x + 18, y + 48, cw - 36, ch - 86, preserveAspectRatio=True, mask='auto')
            c.setFillColorRGB(*INK); c.setFont("Pop", 9.5); c.drawString(x + 18, y + 32, "To: ________________"); c.drawString(x + 18, y + 16, "From: ______________")
        footer(c, W); c.showPage()
    c.save(); return dst

def advent(dst, ps):
    c, W, H = _new(dst, ps, "Christmas Countdown Activity Cards")
    _howto(c, W, H, "25 Days of Christmas Fun", ["Print and cut out the 25 activity cards.", "Fold them, number side out, and place them in a jar, envelopes or a calendar.", "Open one card each day from December 1 to 25.", "Color in the countdown chart as you go!"])
    simple = C.ADVENT; cols, rows = 3, 5; cw = (W - 60) / cols; ch = (H - 110) / rows
    for p in range(0, 25, 15):
        header(c, W, H, "25 Days of Christmas Fun", None, 22)
        for i, t in enumerate(simple[p:p + 15]):
            x = 30 + (i % cols) * cw; y = H - 85 - (i // cols + 1) * ch
            c.setFillColorRGB(1, 1, 1); c.setStrokeColorRGB(*GREEN); c.setLineWidth(2); c.roundRect(x + 5, y + 5, cw - 10, ch - 10, 10, fill=1, stroke=1)
            c.setFillColorRGB(*RED); c.setFont("PopB", 26); c.drawCentredString(x + cw / 2, y + ch - 42, str(p + i + 1))
            c.setFillColorRGB(*INK); _wrap(c, t, x + 14, y + ch / 2 - 6, cw - 28, "Pop", 11, center=True)
        footer(c, W); c.showPage()
    header(c, W, H, "My Christmas Countdown", "Color one ornament each day!")
    for i in range(25):
        x = 95 + (i % 5) * ((W - 190) / 4); y = H - 190 - (i // 5) * 115
        c.setStrokeColorRGB(*INK); c.setLineWidth(2.5); c.circle(x, y, 40); c.rect(x - 9, y + 40, 18, 10)
        c.setFillColorRGB(*INK); c.setFont("PopB", 22); c.drawCentredString(x, y - 8, str(i + 1))
    footer(c, W); c.showPage(); c.save(); return dst

def scavenger(dst, ps):
    c, W, H = _new(dst, ps, "Christmas Scavenger Hunt")
    for title, items in (("Indoor Christmas Scavenger Hunt", C.SCAVENGER_INDOOR), ("Christmas Lights Scavenger Hunt", C.SCAVENGER_OUTDOOR)):
        for copy in range(2):
            header(c, W, H, title, "Check off everything you find!" if copy == 0 else "Team 2 - Who can find them all first?")
            c.setFont("PopB", 15)
            for i, t in enumerate(items):
                x = 70 + (i % 2) * ((W - 140) / 2); y = H - 150 - (i // 2) * 52
                c.setStrokeColorRGB(*GREEN); c.setLineWidth(2); c.rect(x, y - 4, 20, 20); c.setFillColorRGB(*INK); c.drawString(x + 32, y, t)
            footer(c, W); c.showPage()
    c.save(); return dst

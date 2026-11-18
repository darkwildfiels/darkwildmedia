"""Mira printable Christmas games: bingo (picture), word search, trivia, would you rather. Letter + A4 PDFs."""
import os, random, sys, math
from PIL import Image
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
HERE = os.path.dirname(os.path.abspath(__file__))
F = "/usr/share/fonts/truetype/google-fonts/"
pdfmetrics.registerFont(TTFont("Pop", F + "Poppins-Regular.ttf"))
pdfmetrics.registerFont(TTFont("PopB", F + "Poppins-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Lora", F + "Lora-Variable.ttf"))
RED = (0.70, 0.16, 0.18); GREEN = (0.13, 0.40, 0.27); INK = (0.17, 0.18, 0.26); CREAM = (0.98, 0.96, 0.93); GOLD = (0.85, 0.65, 0.25)

def icon_pool(keys, colored_dir="colored"):
    """Colorized coloring pages cropped to content -> square PIL icons."""
    os.makedirs(colored_dir, exist_ok=True)
    import tools
    out = []
    for k in keys:
        cp = f"{colored_dir}/{k}.png"
        if not os.path.exists(cp):
            src = f"clean/{k}.png" if os.path.exists(f"clean/{k}.png") else None
            if src is None:
                os.makedirs("clean", exist_ok=True); tools.clean(f"raw/{k}.png", f"clean/{k}.png"); src = f"clean/{k}.png"
            tools.colorize(src, cp, seed=sum(map(ord, k)))
        im = Image.open(cp).convert("RGB")
        g = im.convert("L").point(lambda v: 255 if v < 235 else 0)
        bb = g.getbbox() or (0, 0, im.width, im.height)
        im = im.crop(bb); s = max(im.size); sq = Image.new("RGB", (s, s), "white"); sq.paste(im, ((s - im.width) // 2, (s - im.height) // 2))
        sq.thumbnail((700, 700)); out.append((k, sq))
    return out

def header(c, W, H, title, sub=None, size=30):
    c.setFillColorRGB(*RED); c.setFont("Lora", size); c.drawCentredString(W / 2, H - 62, title)
    if sub: c.setFillColorRGB(*GREEN); c.setFont("Pop", 12); c.drawCentredString(W / 2, H - 82, sub)

def footer(c, W):
    c.setFillColorRGB(0.6, 0.6, 0.6); c.setFont("Pop", 8); c.drawCentredString(W / 2, 22, "Mira Digital  -  personal use only")

def bingo_pdf(dst, icons, n_cards=30, grid=5, title="CHRISTMAS BINGO", pagesize=letter, big=False, seed=7):
    rnd = random.Random(seed)
    W, H = pagesize; c = canvas.Canvas(dst, pagesize=pagesize); c.setTitle(title.title()); c.setAuthor("Mira Digital")
    letters = "BINGO"[:grid] if grid == 5 else None
    # instructions page
    header(c, W, H, title.title(), "How to play")
    c.setFillColorRGB(*INK); c.setFont("Pop", 12.5); y = H - 130
    lines = ["1. Print the bingo cards (one per player) and the calling cards.",
             "2. Cut the calling cards apart and place them in a bowl or hat.",
             "3. The caller draws one card at a time and shows the picture.",
             "4. Players cover or mark that picture on their card.",
             f"5. The first player to complete a line (across, down or diagonal) shouts BINGO!",
             "", "Tips: use candy, buttons or mini marshmallows as markers.",
             "Play again for a full card, the four corners, or the letter X.", "",
             f"This file includes {n_cards} different bingo cards and the calling cards."]
    for t in lines: c.drawString(70, y, t); y -= 22
    footer(c, W); c.showPage()
    names = [k for k, _ in icons]; imgs = {k: ImageReader(im) for k, im in icons}
    need = grid * grid - (1 if grid % 2 else 0)
    for ci in range(n_cards):
        pick = rnd.sample(names, need)
        c.setFillColorRGB(*CREAM); c.rect(0, 0, W, H, fill=1, stroke=0)
        header(c, W, H, title, f"Card {ci + 1}")
        m = 50; gw = W - 2 * m; cell = gw / grid; top = H - 120
        if letters:
            c.setFont("PopB", 34); c.setFillColorRGB(*RED)
            for j, L in enumerate(letters): c.drawCentredString(m + cell * j + cell / 2, top - 38, L)
            top -= 50
        y0 = top - cell * grid
        it = iter(pick)
        for r in range(grid):
            for col in range(grid):
                x = m + col * cell; y = top - (r + 1) * cell
                c.setFillColorRGB(1, 1, 1); c.setStrokeColorRGB(*GREEN); c.setLineWidth(2.5); c.rect(x, y, cell, cell, fill=1, stroke=1)
                if grid % 2 and r == grid // 2 and col == grid // 2:
                    c.setFillColorRGB(*RED); c.setFont("PopB", 22 if not big else 26); c.drawCentredString(x + cell / 2, y + cell / 2 - 8, "FREE")
                    continue
                k = next(it); p = cell * 0.12
                c.drawImage(imgs[k], x + p, y + p, cell - 2 * p, cell - 2 * p, preserveAspectRatio=True, mask='auto')
        footer(c, W); c.showPage()
    # calling cards
    per = 12 if not big else 6; cols = 3 if not big else 2; rows = per // cols
    for s in range(0, len(names), per):
        header(c, W, H, "Calling Cards", "Cut along the lines")
        cw = (W - 80) / cols; ch = (H - 150) / rows
        for i, k in enumerate(names[s:s + per]):
            x = 40 + (i % cols) * cw; y = H - 110 - (i // cols + 1) * ch
            c.setDash(4, 4); c.setStrokeColorRGB(0.6, 0.6, 0.6); c.rect(x, y, cw, ch); c.setDash()
            p = 14; c.drawImage(imgs[k], x + p, y + p, cw - 2 * p, ch - 2 * p, preserveAspectRatio=True, mask='auto')
        footer(c, W); c.showPage()
    c.save(); return dst

def word_search(words, size=13, seed=1):
    rnd = random.Random(seed)
    for attempt in range(200):
        g = [[None] * size for _ in range(size)]; placed = []
        dirs = [(0, 1), (1, 0), (1, 1), (-1, 1), (0, -1), (1, -1)]
        ok = True
        for w in sorted(words, key=len, reverse=True):
            W = w.replace(" ", "").upper(); done = False
            for _ in range(300):
                dr, dc = rnd.choice(dirs); r = rnd.randrange(size); c = rnd.randrange(size)
                rr, cc = r + dr * (len(W) - 1), c + dc * (len(W) - 1)
                if not (0 <= rr < size and 0 <= cc < size): continue
                if all(g[r + dr * i][c + dc * i] in (None, W[i]) for i in range(len(W))):
                    cells = []
                    for i in range(len(W)): g[r + dr * i][c + dc * i] = W[i]; cells.append((r + dr * i, c + dc * i))
                    placed.append((w, cells)); done = True; break
            if not done: ok = False; break
        if ok:
            ans = [row[:] for row in g]
            for r in range(size):
                for c in range(size):
                    if g[r][c] is None: g[r][c] = rnd.choice("ABCDEFGHIJKLMNOPRSTUVWY")
            return g, placed
    raise RuntimeError("no fit")

def wordsearch_pdf(dst, puzzles, pagesize=letter, title="Christmas Word Search"):
    W, H = pagesize; c = canvas.Canvas(dst, pagesize=pagesize); c.setTitle(title); c.setAuthor("Mira Digital")
    sols = []
    for i, (name, words) in enumerate(puzzles):
        size = 13 if max(len(w.replace(' ', '')) for w in words) <= 13 else 15
        g, placed = word_search(words, size=size, seed=100 + i); sols.append((name, g, placed))
        header(c, W, H, name, f"Puzzle {i + 1}  -  find all {len(words)} words")
        gw = W - 120; cell = gw / size; top = H - 120
        c.setStrokeColorRGB(*GREEN); c.setLineWidth(2); c.roundRect(60 - 8, top - cell * size - 8, gw + 16, cell * size + 16, 12)
        c.setFillColorRGB(*INK); c.setFont("PopB", cell * 0.55)
        for r in range(size):
            for cc in range(size):
                c.drawCentredString(60 + cc * cell + cell / 2, top - (r + 1) * cell + cell * 0.3, g[r][cc])
        y = top - cell * size - 50; c.setFont("Pop", 13); cols = 3; colw = (W - 120) / cols
        for j, w in enumerate(sorted(words)):
            c.drawString(60 + (j % cols) * colw, y - (j // cols) * 22, "□  " + w.upper())
        footer(c, W); c.showPage()
    for i, (name, g, placed) in enumerate(sols):
        size = len(g); header(c, W, H, "Answer Key", f"Puzzle {i + 1}: {name}")
        gw = W - 160; cell = gw / size; top = H - 120
        c.setStrokeColorRGB(*RED); c.setLineWidth(cell * 0.55); c.setLineCap(1)
        c.setStrokeAlpha(0.35)
        for w, cells in placed:
            (r0, c0), (r1, c1) = cells[0], cells[-1]
            c.line(80 + c0 * cell + cell / 2, top - r0 * cell - cell / 2, 80 + c1 * cell + cell / 2, top - r1 * cell - cell / 2)
        c.setStrokeAlpha(1); c.setFillColorRGB(*INK); c.setFont("PopB", cell * 0.5)
        for r in range(size):
            for cc in range(size):
                c.drawCentredString(80 + cc * cell + cell / 2, top - (r + 1) * cell + cell * 0.3, g[r][cc])
        footer(c, W); c.showPage()
    c.save(); return dst

def cards_pdf(dst, title, items, pagesize=letter, kind="trivia"):
    """items: trivia -> (q, a); wyr -> (a, b). 8 cards per page, answers on card back side page (trivia) or none."""
    W, H = pagesize; c = canvas.Canvas(dst, pagesize=pagesize); c.setTitle(title); c.setAuthor("Mira Digital")
    header(c, W, H, title, "How to play")
    c.setFillColorRGB(*INK); c.setFont("Pop", 12.5); y = H - 130
    how = (["Print the cards and cut them apart.", "Split into teams. Take turns reading a question to the other team.",
            "Correct answer = 1 point. The team with the most points wins!", "Answers are printed at the bottom of each card (fold it under, or cover it with a finger).",
            f"{len(items)} questions included, great for all ages."] if kind == "trivia" else
           ["Print the cards and cut them apart.", "Take turns drawing a card and reading it aloud.", "Everyone picks an answer and explains why!",
            "No right or wrong answers - just lots of laughs.", f"{len(items)} questions included, great for kids, families and parties."])
    for t in how: c.drawString(70, y, t); y -= 24
    footer(c, W); c.showPage()
    cols, rows = 2, 4; cw = (W - 70) / cols; ch = (H - 120) / rows
    for s in range(0, len(items), cols * rows):
        c.setFillColorRGB(*CREAM); c.rect(0, 0, W, H, fill=1, stroke=0)
        header(c, W, H, title, None, 22)
        for i, it in enumerate(items[s:s + cols * rows]):
            x = 35 + (i % cols) * cw; y = H - 90 - (i // cols + 1) * ch
            c.setFillColorRGB(1, 1, 1); c.setStrokeColorRGB(*GREEN); c.setLineWidth(2); c.roundRect(x + 6, y + 6, cw - 12, ch - 12, 12, fill=1, stroke=1)
            c.setFillColorRGB(*RED); c.setFont("PopB", 10); c.drawString(x + 20, y + ch - 30, f"#{s + i + 1}")
            c.setFillColorRGB(*INK)
            if kind == "trivia":
                q, a = it; _wrap(c, q, x + 20, y + ch - 52, cw - 40, "PopB", 12.5)
                c.setFillColorRGB(*GREEN); c.setFont("Pop", 10.5); c.drawString(x + 20, y + 22, "Answer: " + a)
            else:
                a, b = it; c.setFont("PopB", 11); c.setFillColorRGB(*GREEN); c.drawCentredString(x + cw / 2, y + ch - 52, "Would you rather...")
                c.setFillColorRGB(*INK); yy = _wrap(c, a, x + 20, y + ch - 78, cw - 40, "PopB", 12.5, center=True)
                c.setFillColorRGB(*RED); c.setFont("PopB", 12); c.drawCentredString(x + cw / 2, yy - 6, "OR")
                c.setFillColorRGB(*INK); _wrap(c, b, x + 20, yy - 28, cw - 40, "PopB", 12.5, center=True)
        footer(c, W); c.showPage()
    c.save(); return dst

def _wrap(c, text, x, y, w, font, size, center=False):
    c.setFont(font, size); words = text.split(); line = ""; lines = []
    for wd in words:
        t = (line + " " + wd).strip()
        if c.stringWidth(t, font, size) > w: lines.append(line); line = wd
        else: line = t
    lines.append(line)
    for l in lines:
        if center: c.drawCentredString(x + w / 2, y, l)
        else: c.drawString(x, y, l)
        y -= size + 5
    return y

def pdf_preview(pdf, page, dst, w=1200):
    import subprocess, glob
    base = dst[:-4]
    subprocess.run(["pdftoppm", "-png", "-r", "110", "-f", str(page + 1), "-l", str(page + 1), "-singlefile", pdf, base], check=True)
    im = Image.open(base + ".png").convert("RGB"); im.thumbnail((w, w * 2)); im.save(dst); return dst

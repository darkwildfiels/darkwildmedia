import os, shutil
from PIL import Image, ImageDraw, ImageFont
import tools
from tools import LW, LH, CREAM, INK, CORAL, SAGE, MUST, LAV, pop, lora, paper, bg
from build import cl, col
F = "/usr/share/fonts/truetype/google-fonts/"

def name_page(src, name, dst, top="Merry Christmas"):
    """Kid coloring page + hollow outlined greeting & name (colorable letters)."""
    im = Image.open(src).convert("L")
    W, H = 2550, 3300
    pg = Image.new("L", (W, H), 255)
    art = im.copy(); art.thumbnail((W - 300, H - 1050))
    pg.paste(art, ((W - art.width) // 2, H - art.height - 160))
    d = ImageDraw.Draw(pg)
    def hollow(text, size, y):
        f = ImageFont.truetype(F + "Poppins-Bold.ttf", size)
        while d.textlength(text, font=f) > W - 260: size -= 10; f = ImageFont.truetype(F + "Poppins-Bold.ttf", size)
        w = d.textlength(text, font=f)
        d.text(((W - w) / 2, y), text, font=f, fill=255, stroke_width=max(8, size // 22), stroke_fill=0)
    hollow(top, 230, 150)
    hollow(name, 420, 470)
    pg.convert("RGB").save(dst); return dst

def colorize_any(src, dst, seed):
    tools.colorize(src, dst, seed=seed); return dst

def build_cn():
    o = 'out/CN'; os.makedirs(o, exist_ok=True); os.makedirs('/tmp/cn', exist_ok=True)
    ex = [('V1', 'Emma'), ('Z1', 'Liam'), ('K1', 'Olivia'), ('V3', 'Noah'), ('N1', 'Grace')]
    pages = [name_page(cl(k), n, f'/tmp/cn/{k}_{n}.png') for k, n in ex]
    colored = colorize_any(pages[0], '/tmp/cn/col0.png', 5)
    tools.cover2(pages[1:3] and [pages[1], pages[0], pages[2]], "Personalized Christmas Coloring Page", "With your child's name - pick any design",
                 f'{o}/01_cover.jpg', count_label="CUSTOM NAME", colored=[None, colored, None], items=["YOUR CHILD'S NAME","MADE FOR YOU","US LETTER + A4","PRINT AT HOME"])
    tools.single(pages[0], f'{o}/02_compare.jpg', "", colored=colored)
    tools.grid(pages, f'{o}/03_examples.jpg', "Example designs with names")
    tools.info(f'{o}/04_how.jpg', "How it works", [("Add your child's name", "Type the name in the personalization box at checkout"),
               ("Pick a design (optional)", "Kids animals, snowmen, trucks, nativity - or let us choose"),
               ("We make your page", "Your PDF arrives in Etsy Messages within 24-48 hours"),
               ("Print & color", "US Letter + A4, print as many as you like")])
    shutil.copy('out/CB/05_tips.jpg', f'{o}/05_tips.jpg') if os.path.exists('out/CB/05_tips.jpg') else None
    tools.custom_pdf(f'{o}/MiraDigital_CN_Order-Info.pdf', kind="name") if False else None
    return sorted(os.listdir(o))

def build_cp():
    o = 'out/CP'; os.makedirs(o, exist_ok=True)
    pages = [cl(k) for k in ['T2', 'U1', 'T4']]
    colored = [None, col('U1', seed=9), None]
    tools.cover2(pages, "Custom Christmas Pet Coloring Page", "From your pet's photo - Santa hat optional", f'{o}/01_cover.jpg', count_label="FROM YOUR PHOTO", colored=colored, items=["FROM YOUR PHOTO","PREVIEW FIRST","US LETTER + A4","PRINT AT HOME"])
    shutil.copy('out/P/02_compare.jpg', f'{o}/02_compare.jpg')
    tools.grid([cl(k) for k in ['T1', 'T3', 'T5', 'U1', 'E2', 'T2']], f'{o}/03_styles.jpg', "Christmas style examples")
    tools.info(f'{o}/04_how.jpg', "How it works", [("Upload your pet's photo", "Add a clear photo at checkout (or send it in Messages)"),
               ("Tell us the extras", "Name, Santa hat, scarf, tree or fireplace"),
               ("Approve your preview", "Preview within 24-48 hours, one free edit"),
               ("Print & color", "US Letter + A4 PDF sent through Etsy")])
    if os.path.exists('out/P/04_tips.jpg'): shutil.copy('out/P/04_tips.jpg', f'{o}/05_tips.jpg')
    return sorted(os.listdir(o))

if __name__ == '__main__':
    print(build_cn()); print(build_cp())

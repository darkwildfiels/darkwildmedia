import os
from pypdf import PdfWriter, PdfReader
import tools, games
from build import cl, col
o='out/AB'; os.makedirs(o,exist_ok=True)
keys=[f'{s}{i}' for s in 'VKN' for i in range(1,6)]
for sz,ps in [('US-Letter','letter'),('A4','a4')]:
    tools.pdf([cl(k) for k in keys], f'/tmp/ab_col_{sz}.pdf', ps, 'Kids Christmas Activity Book')
    w=PdfWriter()
    for f in [f'/tmp/ab_col_{sz}.pdf', f'out/G3/MiraDigital_Christmas_Word_Search_{sz}.pdf', f'out/G5/MiraDigital_Christmas_Would_You_Rather_{sz}.pdf']:
        for p in PdfReader(f).pages: w.add_page(p)
    w.write(f'{o}/MiraDigital_Kids_Christmas_Activity_Book_{sz}.pdf')
n=len(PdfReader(f'{o}/MiraDigital_Kids_Christmas_Activity_Book_US-Letter.pdf').pages); print('pages',n)
ws=games.pdf_preview('out/G3/MiraDigital_Christmas_Word_Search_US-Letter.pdf',0,'/tmp/ab_ws.png',1400)
wy=games.pdf_preview('out/G5/MiraDigital_Christmas_Would_You_Rather_US-Letter.pdf',1,'/tmp/ab_wy.png',1400)
tools.cover2([ws, cl('V3'), wy], "Kids Christmas Activity Book", "Coloring pages, word search & would you rather", f'{o}/01_cover.jpg', colored=[None,col('V3',seed=4),None], items=[f"{n} PAGES","INSTANT DOWNLOAD","US LETTER + A4","AGES 4-9"])
tools.grid([cl('V1'),cl('K2'),cl('N3'),ws,wy,games.pdf_preview('out/G3/MiraDigital_Christmas_Word_Search_US-Letter.pdf',10,'/tmp/ab_k.png',1400)], f'{o}/02_inside.jpg', "What's inside")
tools.info(f'{o}/03_what.jpg',"What's included",[("15 coloring pages","Cute animals, snowmen and the nativity"),("10 word searches","Christmas themes + answer keys"),("40 would you rather cards","Silly questions for family fun")])
tools.single(cl('V2'), f'{o}/04_page.jpg', "", colored=col('V2',seed=12))
tools.info(f'{o}/05_how.jpg',"How it works",[("Buy & download","Instant PDF - US Letter and A4"),("Print what you need","Print again for every kid"),("Keep kids happy","Perfect for winter break and travel")])
print(sorted(os.listdir(o)))

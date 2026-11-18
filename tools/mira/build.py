import json, sys, os, tools
P=json.load(open('products.json'))
os.makedirs('out',exist_ok=True); os.makedirs('clean',exist_ok=True)
def cl(k):
    d=f'clean/{k}.png'
    if not os.path.exists(d): tools.clean(f'raw/{k}.png',d)
    return d
def col(k,seed=7):
    d=f'clean/{k}_col.jpg'
    if not os.path.exists(d): tools.colorize(cl(k),d,seed=seed)
    return d
HOW=[("Buy & download","Your files are ready right after checkout"),("Print at home","US Letter and A4 PDFs included"),("Color & relax","Print as many copies as you like"),("Need help?","Message us - we reply within 24 hours")]
def build(key):
    p=P[key]; o=f'out/{key}'; os.makedirs(o,exist_ok=True)
    pages=[cl(k) for k in p['pages']]
    n=len(pages)
    if n<=5:
        fan=pages; mid=(len(fan)-1)//2
        cols=[None]*len(fan); cols[mid]=col(p['pages'][mid])
    else:
        idx=[0,n//4,n//2,3*n//4,n-1]; fan=[pages[i] for i in idx]; cols=[None,None,col(p['pages'][idx[2]]),None,None]
    imgs=[]
    imgs.append(tools.cover(fan,p['name'].split(' - ')[0],p['sub'],f'{o}/01_cover.jpg',count_label=f"{n} PAGES",colored=cols))
    imgs.append(tools.single(pages[0],f'{o}/02_compare.jpg',"",colored=col(p['pages'][0],seed=11)))
    imgs.append(tools.grid(pages if n<=15 else pages,f'{o}/03_inside.jpg',"What's inside" if n<=15 else f"All {n} pages"))
    for j,k in enumerate(p['pages'][1:3] if n<=5 else [p['pages'][n//3],p['pages'][2*n//3]]):
        imgs.append(tools.single(cl(k),f'{o}/0{4+j}_page.jpg',"Bold lines, big spaces" if key in 'ACDEX' else "Print, color, enjoy"))
    imgs.append(tools.info(f'{o}/06_how.jpg',"How it works",HOW))
    tools.pdf(pages,f'{o}/MiraDigital_{key}_US-Letter.pdf','letter',p['name'])
    tools.pdf(pages,f'{o}/MiraDigital_{key}_A4.pdf','a4',p['name'])
    return imgs
if __name__=='__main__':
    for k in sys.argv[1:]: print(k, build(k))

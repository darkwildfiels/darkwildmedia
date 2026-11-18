import json,sys,tools
from build import P,cl,col
for key in sys.argv[1:]:
    p=P[key]; pages=[cl(k) for k in p['pages']]; n=len(pages)
    if n<=5: fan=pages; cols=[None]*n; cols[(n-1)//2]=col(p['pages'][(n-1)//2])
    else:
        idx=[0,n//4,n//2,3*n//4,n-1]; fan=[pages[i] for i in idx]; cols=[None,None,col(p['pages'][idx[2]]),None,None]
    tools.cover2(fan,p['name'].split(' - ')[0],p['sub'],f'out/{key}/01_cover.jpg',count_label=f"{n} PAGES",colored=cols)
    print('ok',key)

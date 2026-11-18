import sys
from PIL import Image
ks=sys.argv[2:]; ims=[Image.open(f'raw/{k}.png').convert('RGB') for k in ks]
for i in ims:i.thumbnail((400,600))
c=Image.new('RGB',(400*len(ims),600),'white')
for n,i in enumerate(ims):c.paste(i,(n*400,0))
c.save(sys.argv[1])

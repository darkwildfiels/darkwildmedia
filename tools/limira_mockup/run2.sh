for k in "$@"; do
  n=$(ls y2out/$k 2>/dev/null | wc -l); [ "$n" = 8 ] && continue
  src=/mnt/user-data/uploads/Documents/etsy-printify/yeni2/raw/$k.png; [ -f $src ] || continue
  python3 -c "from PIL import Image;Image.open('$src').convert('RGB').resize((2400,3600),Image.LANCZOS).save('y2in/$k.png')"
  mkdir -p y2out/$k; python3 gen8.py y2in/$k.png y2out/$k $k crop > y2out/$k.log 2>&1
done
echo DONE >> y2out/_done

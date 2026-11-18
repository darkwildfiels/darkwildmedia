# usage: bash cyc.sh KEY... ; builds sets whose 5 raw pages exist
cd /home/claude/mira
cp -n /mnt/user-data/uploads/Documents/etsy-printify/mira6/*.png raw/ 2>/dev/null
ok=()
for k in "$@"; do
  [ -f out/$k/06_how.jpg ] && continue
  pages=$(python3 -c "import json;print(' '.join(json.load(open('products.json'))['$k']['pages']))")
  miss=0; for p in $pages; do [ -f raw/$p.png ] || miss=1; done
  [ $miss = 1 ] && continue
  timeout 600 python3 build.py $k >/dev/null 2>&1 && timeout 200 python3 cover2run.py $k >/dev/null 2>&1 && ok+=($k)
done
echo "BUILT ${ok[@]}"

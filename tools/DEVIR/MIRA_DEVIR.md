# MIRA DIGITAL STORE — DEVİR DOSYASI (Claude → Claude)
Son güncelleme: 18 Kasım 2026, 22:30 (TR). Bu dosyayı yazan Claude, MiraDigitalStore'u 12 Kasım'daki açılışından beri yönetiyordu.

> **Yeni Claude'a not:** Bu dosyayı baştan sona oku, sonra kullanıcıyla kaldığımız yerden devam et.
> - Kullanıcı Türkçe konuşur, raporları da Türkçe ister.
> - Gereksiz soru sorma; işi yap, sonra kısa rapor ver.
> - Ortak altyapı (Mac, GitHub, tarayıcı, ChatGPT kuyruğu, kurallar) kardeş dosya `LIMIRA_DEVIR.md`'de daha ayrıntılı anlatılıyor. Önce onun §0 (kurulum) ve §2 (değişmez kurallar) bölümlerini oku; aynen burada da geçerli.

---

## 0. İLK 10 DAKİKA: KURULUM

1. **Masaüstü uygulaması** (`mcp__remote-devices__*`): Mac'te Documents ve Downloads klasörleri bağlı olmalı.
2. **GitHub:** `darkwildfiels/darkwildmedia` deposunu `push` yetkisiyle ekle, `limira-media` dalını klonla:
   ```bash
   git clone -b limira-media --single-branch https://github.com/darkwildfiels/darkwildmedia /home/claude/lm
   ```
3. **Tarayıcı paneli:**
   - Etsy'de **MiraDigitalStore** hesabına kullanıcı kendisi giriş yapar.
   - Aynı panelde aynı anda tek Etsy oturumu açık olabilir; Limira ile çalışırken kullanıcıdan hesap değiştirmesini iste.
   - ChatGPT açık olmalı.
4. **Mira kodunu konteynere geri yükle** (bkz. §4.1).

---

## 1. MAĞAZA BİLGİLERİ

- **Etsy:** https://www.etsy.com/shop/MiraDigitalStore
  - Limira'dan ayrı bir Etsy hesabı.
  - Para birimi USD. Fiyatlar Türkiye'den bakılınca %20 KDV'li görünür (4.99 → 5.99); bu normal.
- **Marka:** "Mira Digital".
  - Renkler: krem #FBF6EE, lacivert #2B2D42, mercan #E07A5F, adaçayı #81B29A, hardal #F2CC8F, lavanta #B5A7D6.
  - Fontlar: Lora (başlık), Poppins (metin).
  - Logo ve banner: `tools/mira/mira_*.jpg/png`.
- **Ürünler:** dijital boyama sayfaları, parti/aktivite oyunları ve kişiye özel boyama sayfaları.
  - Hepsi "Digital", kategori "Coloring Books" (oyunlar "Party Games").
  - "With an AI generator" işaretli.
- **Bölüm (section) id'leri:**

  | Bölüm | Id |
  |---|---|
  | Kids | 61426958 |
  | Seasonal | 61441647 |
  | Bold & Easy | 61441929 |
  | Adult | 61442407 |
  | Bundles | 61427018 |

  Ayrıca bir "Custom Coloring Pages" bölümü var.
- **Fiyatlar:**
  - 5 sayfalık setler: çocuk $3.99, bold/adult $4.99.
  - Paketler: 10 sayfa $6.99, 15 sayfa $6.99–9.99, 20 sayfa $8.99, 30–50 sayfa $9.99–14.99.
  - Oyunlar: $2.99–4.99. Oyun paketleri $7.99–12.99.
  - Kişiye özel ürünler: $6.99–24.99.
- **İNDİRİM YOK.** Kullanıcı bütün indirimleri kaldırttı. Sahte "eski fiyat" de kullanılmaz.
- **Dürüstlük:**
  - Her açıklamada AI beyanı var.
  - Lisanslı karakter yok (Disney, Frozen, Grinch, Snoopy, Bluey vb.).
  - Prensesler tamamen özgün tasarım.

### 1.1 Mevcut ilanlar (105 adet, hepsi yayında)

Tam liste: Mac `~/Documents/etsy-printify/DEVIR/mira_ilanlar_key.csv` (key, etsy_id, başlık). Key, GitHub'daki `mira/<key>/` klasörü ve `mira/seo_<key>.txt` dosyasıyla eşleşir.

**Seri 1 (12 Kasım, ilk 10 ilan):**

| Key | Ürün | Etsy id |
|---|---|---|
| A | Cozy Christmas | 4615842206 |
| B | Kids Christmas | 4615851390 |
| C | Winter Cottage | 4615839369 |
| D | Dogs | 4615847465 |
| E | Cats | 4615862148 |
| F | Mandala | 4615855609 |
| X | Christmas Bundle 15s | 4615853268 |
| Y | Mega 30s | 4615856779 |
| P | Custom Pet (kişiye özel) | 4615842571 |
| Q | Custom House/Family (kişiye özel) | 4615859407 |

**Seri 2 (13 Kasım):**
- Ürünler: W Thanksgiving, G Santa's Workshop, H Gnome, I Gingerbread, J Winter Animals, O Cozy Winter, K Snowman, S Large Print Ornaments, T Christmas Dogs, R Christmas Village.
- **R = 4616536249.** Bu ilan yeni boyama ilanları için kopya kaynağı olarak kullanılıyor.

**Seri 3 (14 Kasım):**
- Paketler: BA 50 sayfa $12.99, BC, BS, BK, BG, BM, BD.
- Setler: M Mandala, L Large Print.
- **CB:** Personalized Coloring Book from Photos, $24.99, kişiye özel. Etsy id 4617362491.

**Seri 4 (14 Kasım gece):**
- Oyunlar G1–G6. **G1 = 4617388418.** Bu ilan oyun ilanları için kopya kaynağı.
- Boyama setleri: N Nativity, V Christmas Animals, U Christmas Cats, Z Trucks.
- Paketler: KB, CC, AB.
- Kişiye özel: CP Custom Christmas Pet $14.99, CN Personalized Name $6.99.

**Seri 5 (16–17 Kasım):**
- Boyama setleri: UN, DI, FA, NB, WF, HA, CH, WD, CK, BI.
- Paketler: CA, CX, WA.
- Oyunlar: G7–G19.
- Oyun paketleri: GB, KA, CR, SP.

**Seri 6 (18 Kasım, son iş):** ayrıntısı §2'de.

---

## 2. SON YAPILAN İŞ: 6. SERİ (18 Kasım), 30 İLAN

Kullanıcının isteği: "mira mağazasına 30 hook ve algoritma listing yap".

Strateji:
- Noel ağırlıklı mağazaya yeni arama trafiği getirmek.
- Şükran Günü oyunları (26 Kasım'a kadar çok aranıyor).
- Yılbaşı gecesi oyunları.
- Yıl boyu satan boyama nişleri.
- Sevgililer Günü ve Çin Yeni Yılı ilanlarını erken açmak; böylece aramalarda indekslenmeye vakit kalıyor.

Hepsi herkese açık sayfada kontrol edildi:
- Boyama ilanlarında 6 görsel, oyun ilanlarında 4 görsel var.
- Hepsi Digital ve fiyatlar doğru.

**Oyunlar** (kaynak G1 4617388418; `gbuild3.py` + `content3.py`):

| Key | Ürün | Fiyat | Etsy id |
|---|---|---|---|
| TG1 | Thanksgiving Word Bingo (30 kart) | 3.99 | 4619911323 |
| TG2 | Thanksgiving Trivia (40 soru) | 3.99 | 4619920602 |
| TG3 | Thanksgiving Would You Rather (30) | 3.99 | 4619912159 |
| TG4 | Thanksgiving Gratitude cards (40) | 3.99 | 4619912571 |
| TG5 | Thanksgiving Word Search (8) | 2.99 | 4619940376 |
| TG6 | Thanksgiving Games Bundle (+ Charades) | 7.99 | 4619913947 |
| NY1 | New Year's Eve Word Bingo | 3.99 | 4619914329 |
| NY2 | New Year's Eve Trivia | 3.99 | 4619914705 |
| NY3 | New Year's Eve Would You Rather | 3.99 | 4619924060 |
| NY4 | New Year's Eve Reflection cards | 3.99 | 4619924464 |
| NY5 | New Year's Eve Word Search | 2.99 | 4619924846 |
| NY6 | New Year's Eve Bundle (+ 30 Goal Cards) | 7.99 | 4619925244 |

**Boyama** (kaynak R 4616536249; görseller ChatGPT):

| Key | Set | Fiyat | Bölüm | Etsy id |
|---|---|---|---|---|
| VK | Valentine's kids | 3.99 | Kids | 4619916763 |
| VA | Valentine bold | 4.99 | Bold | 4619926056 |
| KF | Kawaii food | 3.99 | Kids | 4619926442 |
| BB | Baby animals | 4.99 | Bold | 4619927500 |
| OC | Ocean | 3.99 | Kids | 4619927912 |
| FL | Large print flowers | 4.99 | Bold | 4619919375 |
| MF | Mushroom & frog | 4.99 | Adult | 4619920819 |
| FH | Fairy houses | 4.99 | Adult | 4619930136 |
| SX | Space | 3.99 | Kids | 4619931894 |
| ME | Mermaids | 3.99 | Kids | 4619932274 |
| CT | Cozy cats | 4.99 | Bold | 4619932682 |
| DG | Dog breeds | 4.99 | Bold | 4619925389 |
| BF | Butterfly garden | 4.99 | Adult | 4619927693 |
| SD | Snow day | 3.99 | Kids | 4619936718 |
| LN | Lunar New Year | 3.99 | Seasonal | 4619929651 |
| PR | Princess (özgün) | 3.99 | Kids | 4619929975 |
| VB | Valentine bundle (10 sayfa) | 6.99 | Bundles | 4619918123 |
| CY | Cottagecore book (20 sayfa) | 8.99 | Bundles | 4619930427 |

**Kullanılmış key'ler** (yeni key seçerken çakıştırma):
A AB B BA BB BC BD BF BG BI BK BM BS C CA CB CC CH CK CN CP CR CT CX CY D DG DI E F FA FH FL G G1–G19 GB H HA I J K KA KB KF L LN M ME MF N NB NY1–NY6 O OC P PR Q R S SD SP SX T TG1–TG6 U UN V VA VB VK W WA WD WF X Y Z

---

## 3. BEKLEYEN VE FİKİR LİSTESİ

- **Sezon takvimi:**
  - Şükran Günü 26 Kasım'da biter. Sonrasında TG ilanlarını kapatma; seneye tekrar satar.
  - Noel aramaları 25 Aralık'a kadar sürer. Yılbaşı oyunları 31 Aralık'a kadar.
  - Sevgililer Günü (VK, VA, VB) ve Çin Yeni Yılı (LN, 6 Şubat 2027) Ocak–Şubat'ta satar.
- **Sonraki iyi nişler** (henüz yapılmadı):
  - Easter (Mart)
  - St. Patrick's (Mart)
  - Anneler Günü kartları/boyama
  - Bible verse coloring: metin kendi fontumuzla eklenmeli; ChatGPT yazıyı bozar.
  - Affirmation coloring
  - Teacher appreciation
  - Birthday party coloring
  - Classroom end of year
  - Dinosaur bold & easy (adult)
  - Mandala kişiye özel
- **Marketplace Insights** (14 Kasım, 30 günlük veri):

  | Arama | Aylık arama | Rakip | Yorum |
  |---|---|---|---|
  | christmas coloring pages | 5.9k | 61k | |
  | custom coloring book | 2.4k | 27k | yüksek dönüşüm |
  | personalized coloring book | 1.3k | 13k | çok yüksek dönüşüm |
  | dementia activities printable | 655 | 7k | |

- **Kişiye özel siparişler** (P, Q, CP, CN, CB):
  1. Müşteri foto/isim gönderir.
  2. ChatGPT ile line art yapılır.
  3. 24–48 saatte önizleme mesajı gider. Mesaj taslağını sen yaz, **kullanıcı onaylamadan gönderme**.
  4. 1 revizyon hakkı var.
  5. "Complete order" ile Letter ve A4 PDF teslim edilir.
- **Henüz sipariş yok.** İlk siparişte kullanıcıya haber ver.

---

## 4. YENİ İLAN HATTI (adım adım)

### 4.1 Konteyneri hazırla (her yeni sohbette bir kez)
```bash
git clone -b limira-media --single-branch https://github.com/darkwildfiels/darkwildmedia /home/claude/lm   # yoksa
mkdir -p /home/claude/mira/raw /home/claude/mira/out /home/claude/mira/clean
cp /home/claude/lm/tools/mira/* /home/claude/mira/
cp /home/claude/lm/tools/mira_raw/*.png /home/claude/mira/raw/      # 242 eski sayfa (gri tonlu kopya) - paketleri yeniden kurmak için
# fontlar: games.py / tools.py şu yolları bekler
mkdir -p /usr/share/fonts/truetype/google-fonts && cp /home/claude/lm/tools/fonts/Poppins-*.ttf /home/claude/lm/tools/fonts/Lora-Variable.ttf /usr/share/fonts/truetype/google-fonts/ 2>/dev/null
python3 -c "import reportlab, pypdf, PIL, numpy; print('ok')"
# cyc.sh içindeki yol: /mnt/user-data/uploads/Documents/etsy-printify/mira6/*.png -> raw/
```
- Eski setlerin hazır çıktıları zaten GitHub'da (`mira/<key>/`). Yeniden üretmen gerekmez.
- Raw sayfaların renkli PNG asılları Mac'te `~/Documents/etsy-printify/mira6/` (6. seri) ve `~/Documents/etsy-printify/mira/raw/` (eski seriler) altında.

### 4.2 Ürünleri planla
- `products.json` içine her set için bir kayıt ekle:
  ```json
  "XX": {"name":"Kapakta görünen ad","price":3.99,"pages":["XX1","XX2","XX3","XX4","XX5"],"section":"Kids Coloring Pages","sub":"Kapak alt satırı","brief":""}
  ```
- Paket = başka setlerin sayfa listesi (örnek: `"pages":["VK1",…,"VA5"]`).
- Prompt örnekleri ve 3 stil (K kawaii çocuk, B bold & easy, D detaylı yetişkin) `tools/mira/p6_prompts.py` içinde.
- Bir set = 5 sayfa. Her sayfa için kısa bir konu cümlesi yaz.

### 4.3 Sayfaları ChatGPT'de çiz (iki sekme paralel)
1. Her chatgpt.com sekmesinde (yeni sohbet) `javascript_tool` ile sırayla yapıştır:
   1. `tools/chatgpt/helpers_core.js`
   2. `tools/chatgpt/pr_mira.js`
2. Kuyruğu başlat:
   ```js
   const RQ={"XX1":["K","a cute ..."],"XX3":["K","..."]};
   window.__Q={}; for(const [k,[c,t]] of Object.entries(RQ)) __Q[k]='Create a printable coloring page: '+t+'. '+__STY[c];
   __LOG.push('---'); __run(null); 'ok'
   ```
   Key'leri iki sekmeye böl (örneğin tek sayılar bir sekmede, çift sayılar diğerinde).
3. İzleme: `Object.entries(__SZ).map(([k,v])=>k+'='+v).join(' ')`.
   - Sayfa başına ~1,5–3 dk sürer. Biten sekmede log'a `ALLDONE` yazılır.
   - `SKIP` görürsen o key'i sonra tekrar kuyruğa al.
4. **"Görsel kullanılamıyor"** hatasında sekme takılabilir:
   - Kalan kuyruğu kaydet: `localStorage.__remQ=JSON.stringify(kalan)`.
   - Yeni sohbet aç, helper'ları yeniden yapıştır.
   - Kuyruğu geri yükle: `window.__Q=JSON.parse(localStorage.__remQ); __run(null)`.
5. Downloads'a inen dosyalar bazen gizli ve uzantısız olur. Toplama betiği bunları boyuta göre bulur (aşağıda).

### 4.4 Topla, stage et, derle
```bash
# Mac
cd $HOME/mnt/Documents/etsy-printify/mira6 && bash collect.sh XX1=<bayt> XX2=<bayt> ...
```
- `collect.sh` önce `mira_<k>*.png` adıyla arar. Bulamazsa aynı boyutta ve belirli tarihten yeni dosyayı arar; gizli `.Q6L2SF6YDW…` dosyaları da bulur.
- **Yeni günde script içindeki `-newermt` tarihini güncelle.** Saatler UTC.

Sonra:
1. `device_stage_files` ile `~/Documents/etsy-printify/mira6/XX1.png …` dosyalarını konteynere al.
2. Sayfaları kontak sayfası halinde görsel olarak kontrol et (kalite, yazı/filigran olmamalı, karakter özgün olmalı).
3. Derle:
   ```bash
   cd /home/claude/mira && bash cyc.sh XX YY      # 5 sayfası tamam olan setleri build.py + cover2run.py ile derler -> out/XX/
   ```
4. Çıktıyı kontrol et (01_cover ve 02_compare'e bak).

Her boyama setinin çıktısı:
- `01_cover.jpg` (büyük hero kapak, cover2)
- `02_compare.jpg` (siyah-beyaz ve renkli karşılaştırma)
- `03_inside.jpg`
- `04_page.jpg`
- `05_page.jpg`
- `06_how.jpg`
- `MiraDigital_XX_US-Letter.pdf` ve `MiraDigital_XX_A4.pdf`

### 4.5 SEO dosyası (`seo_XX.txt`)
Biçim:
```
###TITLE###
<başlık, en fazla 140 karakter, ":" yok>
###TAGS###
<13 etiket, virgülle ayrılmış, her biri en fazla 20 karakter, tekrar yok>
###DESCRIPTION###
<açıklama>
###END###
```
- Üretim scripti: `tools/mira/seo6.py`.
  - `col()` boyama açıklama şablonu (hook → içerik listesi → teslim → nasıl çalışır → baskı ipuçları → kime uygun → not).
  - `game()` oyun açıklama şablonu.
  - Assert'ler kuralları kontrol eder.
- Açıklamanın sonunda mutlaka "📌 PLEASE NOTE" bloğu olmalı (dijital ürün, kişisel kullanım, iade yok, AI beyanı).
- Başlık kalıbı: "<Konu> Coloring Pages for <Kitle>, <N> Printable <...> Coloring Sheets, <kullanım/hediye>".

### 4.6 Oyun ürünleri (görsel gerektirmez)
- `games.py` (bingo, kelime avı, kart PDF), `games2.py` (basit kartlar, sudoku, labirent vb.), `gbuild*.py` (paketleme ve görseller).
- İçerik dosyaları: `content2.py`, `content3.py`.
- Yeni tema için `content3.py` örneğini izle (BINGO 40 kelime, WS 8 bulmaca, TRIVIA 40, WYR 30, CONVO 40). Sonra `gbuild3.py` içindeki `gen(t)` kalıbını kopyala.
- Renk paleti: `PAL` (tema başına iki renk).
- Oyun görselleri: `01_cover`, `02_inside`, `03_page` (paketlerde `03_what`), `04_how`.

### 4.7 GitHub'a it
```bash
cd /home/claude/lm && for k in XX YY; do mkdir -p mira/$k && cp /home/claude/mira/out/$k/* mira/$k/ && cp /home/claude/mira/seo_$k.txt mira/; done
git add mira && git commit -m "Mira XX YY" && git push origin HEAD:limira-media
git rev-parse --short HEAD     # helper'ı bu SHA ile yükleyeceksin
```

### 4.8 Etsy'ye yükle (Mira girişli tarayıcı)
1. Bir sekmede `https://www.etsy.com/your/shops/me/tools/listings` aç ve sekmeyi öne getir (`tabs_select`). Arka planda çok yavaşlıyor.
2. Sürücüyü ve yardımcıyı yükle:
   ```js
   const g=u=>{const x=new XMLHttpRequest();x.open('GET',u,false);x.send();return x.responseText;};
   eval(g('https://raw.githubusercontent.com/darkwildfiels/darkwildmedia/0ac491e5217c/mira/mdrv.js'));
   window.__H=g('https://raw.githubusercontent.com/darkwildfiels/darkwildmedia/<SON_SHA>/mira/etsy_helper.js');
   localStorage.__mdrv='[]';
   // boyama seti:
   window.__CI=['01_cover.jpg','02_compare.jpg','03_inside.jpg','04_page.jpg','05_page.jpg','06_how.jpg'];
   window.__co=(k,p,s)=>[{k,imgs:__CI,pdfs:['MiraDigital_'+k+'_US-Letter.pdf','MiraDigital_'+k+'_A4.pdf'],price:p,section:s},'4616536249'];
   __madd(__H, __co('XX',3.99,'61426958'), __co('YY',4.99,'61441929'));
   // oyun (kaynak G1, bölüm verme):
   __madd(__H, [{k:'TG1',imgs:['01_cover.jpg','02_inside.jpg','03_page.jpg','04_how.jpg'],pdfs:['MiraDigital_Thanksgiving_Word_Bingo_US-Letter.pdf','MiraDigital_Thanksgiving_Word_Bingo_A4.pdf'],price:3.99},'4617388418']);
   ```
3. Sürücü her ilan için şunları yapar:
   - kaynak ilanın "copy" sayfasını gizli bir iframe'de açar,
   - görselleri ve PDF'leri değiştirir,
   - başlık, etiket ve açıklamayı `seo_<k>.txt`'den yazar,
   - fiyatı ve bölümü ayarlar, kontrol eder ve yayınlar.
4. Log: `__MQ.length+' '+localStorage.__mdrv`. Başarı: `"... check imgs=9 pdfs=2 tags=13,dlg Publish,published?"`. Kuyruk bitince `IDLE`.
   - Oyunlarda `imgs=7` görünür, normal.
   - İlan başına ~1,5–3 dk sürer.
5. **`tags=-1, ABORT check failed`** görürsen sayfa geç yüklenmiştir. O ilanı `wait:30000` ekleyerek tekrar kuyruğa al:
   ```js
   const o=__co('CY',8.99,'61427018'); o[0].wait=30000; __madd(__H,o)
   ```
   Not: `__madd` yardımcıyı ilk çağrıda `window.__MH`'ye kaydeder; sonraki çağrılarda `__MH` de kullanılabilir.
6. **DOĞRULAMA:**
   - Mağaza sayfasını (`/shop/MiraDigitalStore?sort_order=date_desc`) XHR ile çek; yeni ilanların id'lerini al.
   - Her ilanın herkese açık sayfasında `il_fullxfull` görsel sayısını (boyama 6, oyun 4), "Digital download" ifadesini ve fiyatı kontrol et.
   - Bir ilan eksik çıkarsa log'da ABORT arayıp tekrar kuyruğa al.

### 4.9 Rapor
Kullanıcıya kısa bir Türkçe rapor ver: kaç ilan yayında, hangi konular, doğrulama sonucu. İlan id'lerini kendi notuna kaydet.

---

## 5. ÖĞRENİLEN DERSLER (Mira'ya özel)
- **ChatGPT:**
  - 3 sekme aynı anda çalışınca üretim limiti doluyor; 2 sekme sorunsuz.
  - "Santa Claus" ve buz pateni istemleri bir kez politika uyarısı aldı. İfadeyi değiştirince geçti.
- **Kopyalar:** ChatGPT bazen aynı görseli tekrar verir (iki key aynı boyutta çıkar). O key'i yeniden üret.
  - Örnek: CK3, CK2'nin kopyası çıktı ve yerine farklı bir sayfa kullanıldı.
- **Sudoku 6x6 kutu formülü düzeltildi** (`games2._sudoku`). Eski sürüme dönme.
- **"□" glifi** Poppins'te yok; "[ ]" kullan.
- **Kapak stili:** yeni setlerde `cover2run.py` (cover2 "hero") kullan. 18 eski ilanın kapağı da v2'ye çevrildi.
- **Sayfa alt metni:** `build.py` içinde "Bold lines, big spaces" (A, C, D, E, X için) ya da "Print, color, enjoy".
- **PDF boyutu:** Etsy dijital dosya sınırı 20 MB. 20 sayfalık CY ~6 MB. 50 sayfalık BA da sığdı; daha büyük paketlerde boyutu kontrol et.

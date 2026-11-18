# LIMIRA COLLECTION — DEVİR DOSYASI (Claude → Claude)
Son güncelleme: 18 Kasım 2026, 22:30 (TR). Bu dosyayı yazan Claude, LimiraCollection mağazasını 9 Kasım'dan beri yönetiyordu.

> **Yeni Claude'a not:** Bu dosyayı baştan sona oku, sonra kullanıcıyla kaldığımız yerden devam et. Kullanıcı Türkçe konuşur ve raporları Türkçe ister. Gereksiz soru sorma; işi yap, sonra kısa rapor ver. Aşağıdaki **DEĞİŞMEZ KURALLAR** bölümü kullanıcının kesin talimatlarıdır.
>
> Kardeş dosya `MIRA_DEVIR.md`, dijital boyama mağazasını anlatır. İki dosyadaki ortak altyapı (Mac klasörü, GitHub, tarayıcı paneli, ChatGPT kuyruğu) aynıdır.

---

## 0. İLK 10 DAKİKA: KURULUM KONTROL LİSTESİ

Yeni hesapta çalışmaya başlamadan önce şunları sırayla kontrol et. Eksik olanı kullanıcıdan iste.

1. **Claude masaüstü uygulaması bağlı mı?** `mcp__remote-devices__*` araçları olmalı: `device_bash`, `device_stage_files`, `device_commit_files`, `Claude_Browser__*`.
   - Kullanıcının Mac'inde **Documents** ve **Downloads** klasörleri bağlı olmalı.
   - `device_bash` içinde bunlar `$HOME/mnt/Documents` ve `$HOME/mnt/Downloads` olarak görünür.
   - Bağlı değilse: kullanıcı sohbeti masaüstü uygulamasında açmalı ve Documents ile Downloads klasörlerini eklemeli.
2. **GitHub bağlantısı:** depo `darkwildfiels/darkwildmedia`, dal **`limira-media`**.
   - `add_repo(owner="darkwildfiels", repo="darkwildmedia", access="push")` ile ekle.
   - Klonla: `git clone -b limira-media --single-branch <url> /home/claude/lm` (büyük bir depo, birkaç dakika sürer).
   - Commit mesajlarının sonuna sistemin verdiği attribution satırlarını ekle.
   - Kullanıcının yeni hesabında GitHub bağlı değilse claude.ai → Settings → Connectors'dan bağlaması gerekir.
3. **Tarayıcı paneli (built-in browser):**
   - Etsy'de **LimiraCollection** hesabına kullanıcı kendisi giriş yapar. Şifreyi asla sen girme.
   - ChatGPT (chatgpt.com) da kullanıcının hesabıyla açık olmalı. Görselleri ChatGPT ile üretiyoruz.
   - Aynı tarayıcıda aynı anda tek Etsy oturumu olur. Mira ile Limira arasında geçiş gerekirse kullanıcıdan iste: "tarayıcı panelinde Limira'ya geçer misin?"
4. **Printify token:** Mac'te `~/Documents/etsy-printify/.env` içinde `PRINTIFY_TOKEN=...` olarak duruyor.
   - **Asla ekrana basma**, asla okuma çıktısında gösterme.
   - `pf.py` token'ı kendisi okur.
5. **Konteyner kodunu geri yükle** (ayrıntısı §6.1'de). Mockup üretimi ve bazı scriptler bu sohbetin geçici konteynerindeydi. Hepsi GitHub'a yedeklendi: `tools/` klasörü (commit `e777cd9` ve öncesi).

---

## 1. İŞ BAĞLAMI

- **Sahipler:** kullanıcı ve iki ortağı (toplam 3 ortak). Kâr üçe bölünüyor. Kullanıcı Türkiye'de, saat dilimi Europe/Istanbul.
- **İki Etsy mağazası:**
  - **LimiraCollection:** kanvas duvar tablosu, Printify ile print-on-demand. Bu dosyanın konusu.
  - **MiraDigitalStore:** dijital boyama sayfaları ve oyunlar (bkz. `MIRA_DEVIR.md`).
- **Printify:** shop id **29663597**. Ürün tipi: blueprint **1159**, provider **99**. Kanvas, 1.25" gallery wrap, kenarlar `mirror`.
- **Durum (18 Kasım):**
  - Printify'da 160 ürün var, 156'sı Etsy'de yayında.
  - 4'ü yayınlanmamış taslak (biri "ZZ HELPER STUDIO - do not publish"); bunlara dokunma.
  - Satış hâlâ 0. Ziyaret çok düşük; Etsy aramasından trafik neredeyse yok. Mağaza 6–7 Kasım'da açıldı.
- **Kullanıcının hedefi:** ziyaret ve satış artırmak.
  - Her gün yeni "hook"lu ilan, yani duygusal ve hediye odaklı.
  - Pinterest ve Etsy Ads.

---

## 2. DEĞİŞMEZ KURALLAR (kullanıcının açık talimatları)

1. **KARGO AYARINA ASLA DOKUNMA.** Kullanıcının sözleri:
   - "kargo şuan nasılsa öyle kalsın her zaman değiştirme hiç"
   - "abd ücretsiz 2-7 gün ve altında da heryer ücretsiz 2-7 gün olarak var. Bu böyle kalsın elleme"

   Sadece kontrol et ve raporla. Printify'dan yeni yayınlanan ilanlar Etsy'de **320264294296** numaralı kargo profiline düşüyor. Bunu her turda kullanıcıya hatırlat; kontrolü kullanıcı yapar.
2. **İNDİRİM YOK.** "İndirim yok. Bütün indirimleri kaldır."
   - LAUNCH20 ve WELCOME20 kaldırıldı. Yeni indirim açma.
   - "2 katı fiyat yazıp %50 indirim" taktiğini **reddettik**, çünkü yanıltıcı fiyatlama. Yine isterse kibarca ama net reddet.
3. **Şifre girme.** Kullanıcı kendisi giriş yapar. Ödeme ve kart bilgisi de girme.
4. **Printify token'ı asla gösterme.**
5. **Mac'te dosya silme.** Gerekirse `_to_delete/` klasörüne taşı. Mac'te zaten `~/Documents/etsy-printify/_to_delete` var.
6. **Müşteri mesajları:** taslağı sen hazırla, kullanıcı onaylamadan gönderme.
7. **Dürüstlük:**
   - Açıklamalarda AI beyanı olmalı ("designed by our studio with the help of digital and AI tools").
   - "Hand-painted" deme, sahte yorum yazma, lisanslı karakter kullanma (Disney, Pixar, Grinch, Snoopy vb.), sahte fiyat kullanma.
8. **Gereksiz soru sorma.** "Bana soru sorma" dedi. İşi yap, sonunda kısa Türkçe rapor ver.
9. **Görsel stili (17 Kasım'dan itibaren):** "realistic görseller olsun gerçekle ayırt edilemesin çizgi film gibi değil. aşırı 4k realistic"
   - Yeni Limira görselleri **ultra-gerçekçi fotoğraf** olmalı. Yağlı boya, illüstrasyon ya da çizgi film olmamalı.
   - SEO başlıklarında "Painting" yerine "Art" kullan.
10. **Etsy Ads:** kullanıcı **günde $1** ve **en güçlü 15 ilan** için onay verdi. Yeni mağazalarda 15 gün bekleme var; **21 Kasım'dan itibaren açılabilir** (§5).

---

## 3. FİYAT, VARYANT VE KÂR

8 varyant var. Printify variant id → fiyat (cent):

| Boy | Printify variant | Fiyat | Yaklaşık ABD net kârı |
|---|---|---|---|
| 8x10 | 101413 | $44.99 | ~$13 |
| 11x14 | 91641 | $54.99 | ~$16 |
| 12x18 | 91644 | $82.99 | ~$33 |
| 16x20 | 91646 | $90.99 | ~$36 |
| 16x24 | 91647 | $105.99 | ~$42 |
| 20x30 | 91650 | $118.99 | ~$48 |
| 24x30 | 101411 | $149.99 | ~$60 |
| 24x36 | 91653 | $150.99 | ~$60 |

- **2:3 oranlı görsel:** 12x18, 16x24, 20x30, 24x36 (`V23=[91644,91647,91650,91653]`).
- **4:5 oranlı görsel:** 8x10, 11x14, 16x20, 24x30 (`V45=[91646,101411,101413,91641]`).
- **Fiyat formülü:** `fiyat = (maliyet + ABD kargo + 0.663) / (0.82612 − kâr oranı)`.
  - 12x18 ve üstünde kâr oranı ~%40.
  - Küçük boylar bilinçli olarak düşük kârlı giriş fiyatı.
- **ABD kargosu fiyata gömülü**, bu yüzden ABD kargo ücretsiz olmalı. Kullanıcı ayarı zaten böyle.
- **Etsy'de varyant adları cm'li:** "20x25 cm / 8x10"", "28x36 cm / 11x14"" vb. `__cmcode` ile yapılır.
  - **Printify'da `variants:true` ile yeniden publish edersen adlar inch'e döner.** Mevcut ürünlerde publish'i `variants:false` ile yap.

---

## 4. NEREDE NE VAR

### 4.1 Mac: `~/Documents/etsy-printify/` (device_bash'te `$HOME/mnt/Documents/etsy-printify`)

**Ana dosyalar:**

| Dosya | Ne işe yarar |
|---|---|
| `.env` | Printify token (gizli) |
| `pf.py` | Printify API yardımcısı: `api(method, path, body)`, `SHOP=29663597` |
| `hizli_buyut.py` | FSRCNN x4 büyütme (`modeller/FSRCNN_x4.pb`), opencv. `python3 hizli_buyut.py in.png out.jpg` |
| `yeni/desc_tpl2.txt` | **Güncel açıklama şablonu** (aşağıda) |

**`yeni2/` klasörü (güncel yeni ilan hattı):**

| Dosya | Ne işe yarar |
|---|---|
| `collect.sh` | `bash yeni2/collect.sh d95=2836022 d96=...` → Downloads'ta o boyuttaki dosyayı `yeni2/raw/<k>.png` olarak kopyalar. `-newermt "2026-11-16 12:00"` filtresi var; yeni dönemde tarihi güncelle (Downloads saatleri UTC). |
| `taslak3.py` | Görsel → Printify ürünü (aşağıda) |
| `yayinla.py` | Publish (aşağıda) |
| `ext.py` | Etsy id'lerini çeker (aşağıda) |
| `taslak.json` | key → `{id, etsy, pub, ship}`, 102 kayıt: c01–c08, d01–d94 |
| `seo.json` | key → `{t, g, a}`, 102 key. Yedekler `seo_bak_v3/v4/v5.json` |
| `raw/` | Ham görseller |
| `up/` | Büyütülmüş görseller |
| `retitle_v1.json`, `retitle_run.py`, `retitle_log.json` | 58 eski ilanın hediye başlıklı yeniden yazımı (bitti) |

`taslak3.py` ayrıntısı:
- Komut: `timeout 165 python3 yeni2/taslak3.py d95 d96 ...` (yaklaşık 130 sn sonra kendini durdurur; kalanlar için tekrar çalıştır).
- `raw/<k>.png` → `up/<k>.jpg` (hizli_buyut) → 2:3 ve 4:5 kırpım.
- Printify upload → ürün oluşturur: 8 varyant, fiyatlar, `seo.json`'dan başlık/etiket, `desc_tpl2.txt`'deki `{ABOUT}` yerine `seo[k]['a']`.
- Sonucu `yeni2/taslak.json`'a yazar. Kaldığı yerden devam eder.

`yayinla.py` ayrıntısı:
- Komut: `python3 yeni2/yayinla.py d95 d96 ...`
- Publish bayrakları: title/description/images/variants/tags/keyFeatures/shipping_template hepsi True.
- Yeni ürün için bu doğru. Eski ürünü yeniden publish ederken **variants False** yap.

`ext.py` ayrıntısı:
- Komut: `timeout 160 python3 yeni2/ext.py`
- Printify'dan Etsy id ve kargo profilini çekip `taslak.json`'a yazar.
- Yayından 2–10 dk sonra id gelir; `None` dönenler için birkaç dk sonra tekrar çalıştır.

**Diğer klasörler:**

| Yol | İçerik |
|---|---|
| `gelen/odalar/` | Mockup oda fotoğrafları: `oda0_kemer, oda1_salon, oda2_yatak, oda3_giris, oda4_ofis, oda5_yaslanmis, oda6_aci_yemek, oda7_aci_salon` (.png). Mockup üretimi bunları kullanır. |
| `pinterest/` | `pinterest_pins.csv`, `.json` ve 45 pin görseli |
| `meta/pub_all.json` | İlk 28 ilan. Diğer meta dosyaları eski. |
| `kucuk_boy.py` | 8x10 ve 11x14 ekleme. Bitti, **tekrar çalıştırma.** |
| `portre/`, `portre_ilan/`, `pet_ornek/` | Kişiye özel evcil hayvan portresi hazırlığı. 4 portre ilanı yayında. |

**`DEVIR/` klasörü (bu devir için hazırlandı):**

| Dosya | İçerik |
|---|---|
| `limira_ilanlar_taslak3.csv` | key, printify_id, etsy_id, title (c01–d94) |
| `limira_tum_printify_urunleri.csv` | 160 Printify ürünü ve Etsy id'leri |
| `etsy_localstorage_dump.json` | Etsy sayfasında kullandığımız JS yardımcılarının yedeği (§6.4) |
| `kod_yedek_tools.tgz` | GitHub `tools/` klasörünün yedeği (scriptler, fontlar) |
| `LIMIRA_DEVIR.md`, `MIRA_DEVIR.md` | Bu dosyalar |

### 4.2 GitHub: `darkwildfiels/darkwildmedia`, dal `limira-media`

| Yol | İçerik |
|---|---|
| `limira/yeni/<k>/` | Her ilanın 8 mockup'ı: `1_salon_yakin.jpg 2_boyut.jpg 3_kemer.jpg 4_salon.jpg 5_giris.jpg 6_ofis.jpg 7_yemek.jpg 8_detay.jpg`. Etsy sürücüsü buradan çeker. |
| `limira/limira_size_guide.jpg` | Ölçü rehberi (9. görsel) |
| `limira/limira_studio_video_5sn.mp4` | İlan videosu |
| `limira/drv.js` | Etsy medya + cm sürücüsü. Commit SHA ile yükle: `97e53100aa71` |
| `limira/pins/<k>_pin.jpg` | 45 Pinterest pin görseli (1000x1500) |
| `limira/pinterest/pq.js`, `pq.json` | Pin kuyruğu (başlık, açıklama, board, link) |
| `tools/limira_mockup/` | `mockup5.py`, `gen8.py`, `run2.sh` (+ eski `mockup2.py`, `hero2.py`) |
| `tools/limira_misc/` | `seo_d3/d4/d5.py` (SEO üretim örnekleri), `pins.py`, `pins2.py` (pin görseli üretimi), `d3/d4/d5/d5r_prompts.json` (prompt arşivi), `banner.py`, `pet_*.py` |
| `tools/chatgpt/` | `helpers_core.js`, `pr_limira.js`, `pr_mira.js` (ChatGPT kuyruğu) |
| `tools/etsy_js/` | `__nwcode.js`, `__cmcode.js`, `__sgcode.js`, `__vupcode.js` ve diğerleri; ayrıca `drv.js`, `mdrv.js`, `etsy_helper.js` |
| `tools/pinterest_pin.js` | Pin atma yardımcısı. Yeniden yazıldı; önce 1 pinle test et. |
| `tools/fonts/` | Poppins, Lora, Inter |

### 4.3 Claude projesi (eski hesapta)
"etsy" adlı projede günlük notlar vardı: `claude/limira-*.md`. Yeni hesap bunları göremez. Gerekli her şey bu dosyada.

---

## 5. ŞU ANKİ DURUM VE BEKLEYEN İŞLER

### 5.1 Son yapılan iş (17–18 Kasım)
25 gerçekçi fotoğraf ilanı (+2 yağlı boya) yayında ve doğrulandı. Her birinde 9 görsel (8 mockup + ölçü rehberi), video ve 8 cm seçeneği var.

| Key | Konu | Etsy id |
|---|---|---|
| d93 | black lab rainbow bridge (gerçekçi) | 4619627161 |
| d94 | German shepherd (gerçekçi) | 4619627345 |
| d70 | beagle | 4619627529 |
| d71 | dachshund | 4619627723 |
| d72 | Frenchie | 4619627911 |
| d73 | orange cat | 4619635196 |
| d74 | horse | 4619635364 |
| d75 | black cat moon | 4619628495 |
| d76 | Christmas morning | 4619637769 |
| d77 | snowman | 4619635716 |
| d78 | cardinals | 4619635844 |
| d79 | Star of Bethlehem | 4619628881 |
| d80 | toy shop | 4619643008 |
| d81 | Christmas train | 4619635825 |
| d82 | corgi | 4619636003 |
| d83 | tree farm | 4619643520 |
| d84 | workshop | 4619643670 |
| d85 | eagle | 4619643872 |
| d86 | bison | 4619644046 |
| d87 | Tuscany | 4619644206 |
| d88 | Santorini | 4619636981 |
| d89 | lavender | 4619644508 |
| d90 | sunflower | 4619637239 |
| d91 | koi | 4619637423 |
| d92 | cliff cottage | 4619637593 |
| d68 | black lab (yağlı boya, ekstra) | 4619617119 |
| d69 | German shepherd (yağlı boya, ekstra) | 4619624432 |

**Sonraki boş key: `d95`.** Yeni turda d95, d96, … kullan.

### 5.2 Daha önceki turlar (özet)
- **c01–c08, d01–d22:** 13–14 Kasım ilanları; Noel, kış ve hayvan konuları.
- **d23–d47 (15 Kasım):** sinematik yağlı boya, hediye odaklı: golden retriever şömine, kırmızı kamyonet, deniz feneri, geyik, kütüphane, Paris, şakayık, kara kedi + dolunay, dachshund Noel, at kızağı, Viktorya pazarı, piyano balo salonu, alp gölü, balıkçı teknesi, tilki ailesi, buharlı tren, highland inek, ayçiçeği + ahır, limonlu mutfak, karda iki at, kiraz çiçeği + ay, kuğu, Noel meleği, golden yavru.
- **d48–d67 (16 Kasım):** "hook" ilanları; Noel ve evcil hayvan anısı ağırlıklı.
- Tam liste `DEVIR/limira_ilanlar_taslak3.csv` içinde; başlıklar `yeni2/seo.json` içinde.
- 58 eski ilanın başlığı hediye odaklı yapıldı ve açıklamaları hikâyeyle başlayacak şekilde yeniden yazıldı (15 Kasım).
- 4 kişiye özel evcil hayvan portresi ilanı var.

### 5.3 BEKLEYEN İŞLER
1. **Etsy Ads (21 Kasım veya sonrası):**
   - Etsy → Marketing → Etsy Ads. Günlük bütçe **$1**.
   - Sadece şu 15 ilan reklamda olsun:

   | Key | Etsy id |
   |---|---|
   | d48 | 4618636766 |
   | d49 | 4618636884 |
   | d50 | 4618637076 |
   | d52 | 4618639454 |
   | d53 | 4618632665 |
   | d54 | 4618639792 |
   | d59 | 4618636757 |
   | d63 | 4618643346 |
   | d51 | 4618632387 |
   | d66 | 4618644048 |
   | d23 | 4617947695 |
   | d47 | 4617966055 |
   | d32 | 4617963676 |
   | d55 | 4618632947 |
   | d14 | 4617334420 |

   - Diğer ilanları reklamdan çıkar.
   - Bu bir ödeme ayarıdır. Kullanıcı açıkça "$1 reklam aç 15 ilana" dedi; yine de son adımda bütçeyi ve ilanları teyit eden kısa bir mesaj at.
2. **Kargo profili kontrolü:** yeni ilanlar 320264294296 profiline düşüyor. Kullanıcıya hatırlat, sen değiştirme.
3. **Pinterest:**
   - Hesap `etsyshopet`, işletme hesabı, görünen ad LimiraCollection.
   - 8 pano açık, 45 pin atıldı (d23–d67).
   - Yeni ilanlar (d68–d94) için pin henüz yapılmadı. İstenirse `pins2.py` ile pin görseli üret, GitHub `limira/pins/`'e koy, `tools/pinterest_pin.js` ile at.
   - Board id'leri (hepsi `2533979852233235` + 2 hane):

   | Pano | Board id |
   |---|---|
   | Christmas Wall Art & Decor | …534 |
   | Pet Memorial Gifts | …535 |
   | Cozy Cabin & Winter Decor | …536 |
   | Coastal & Ocean Wall Art | …537 |
   | Romantic & Paris Wall Art | …538 |
   | Dark Academia Decor | …539 |
   | Farmhouse & Animal Wall Art | …540 |
   | Nursery & Kids Room Art | …541 |

   - Tarayıcı panelinde tr.pinterest.com ve pinterest.com için site izni verilmişti.
   - Pinterest bir Etsy mağazasını "claim" edemiyor; bunu kullanıcıya söyledik.
4. **Featured ürünler:** 4 güçlü ilanı "featured" yap. Video hover'ı yalnızca arama ve featured ürünlerde oynar. Henüz yapılmadı; düşük öncelik.
5. **İlk siparişte:** Printify "Other orders" sekmesine düşerse elle eşleştir (cm'li varyant adları yüzünden). Portre siparişlerinde Printify onayı manuel olmalı.
6. **Sezon takvimi:**
   - Noel ilanlarını en geç ~5 Aralık'a kadar ekle. Açıklamada "US orders by December 8" notu var.
   - Ocak'ta Noel ilanlarını pasife al.
   - Sevgililer Günü ilanları 20 Aralık–Ocak, Anneler Günü Mart–Nisan.

---

## 6. YENİ İLAN HATTI (adım adım)

Kullanıcı genelde "limira listing başla 25 tane" der. Tam akış:

### 6.1 Konteyneri hazırla (her yeni sohbette bir kez)
```bash
# 1) depo
git clone -b limira-media --single-branch https://github.com/darkwildfiels/darkwildmedia /home/claude/lm
# 2) mockup kodu
mkdir -p /home/claude/prev/y2in /home/claude/prev/y2out
cp /home/claude/lm/tools/limira_mockup/{mockup5.py,gen8.py,run2.sh} /home/claude/prev/
# 3) fontlar (konteynerde yoksa)
mkdir -p /usr/share/fonts/truetype/google-fonts /usr/share/fonts/opentype/inter
cp /home/claude/lm/tools/fonts/Poppins-*.ttf /home/claude/lm/tools/fonts/Lora-Variable.ttf /usr/share/fonts/truetype/google-fonts/ 2>/dev/null
cp /home/claude/lm/tools/fonts/Inter-*.otf /usr/share/fonts/opentype/inter/ 2>/dev/null
python3 -c "import numpy, scipy, PIL; print('ok')"   # gen8 numpy + scipy + PIL ister
```
4) **Oda fotoğraflarını stage et.** `mockup5.py` bunları `R="/mnt/user-data/uploads/Documents/etsy-printify/gelen/odalar/"` yolundan okur:
`device_stage_files(paths=["~/Documents/etsy-printify/gelen/odalar/oda0_kemer.png", … oda7_aci_salon.png])` (8 dosya).

### 6.2 Konu ve prompt seç
- Duygusal, hediye odaklı ve "hook"lu konular seç. En iyi giden temalar:
  - evcil hayvan anısı (rainbow bridge, "in loving memory")
  - Noel nostaljisi
  - kır evi ve sıcak ev hissi
  - romantik seyahat (Toskana, Santorini, Paris)
  - vahşi doğa (kartal, bizon)
  - çiçek ve mutfak
- Lisanslı karakter kullanma. İnsan yüzlü portre yapma; sahnelerde "no people" ekle.
- Prompt yalnızca konuyu anlatır; stil ekini `pr_limira.js` kendisi ekler.
- Örnek konu cümlesi: `"a real black labrador retriever walking happily toward the camera on a glowing rainbow-colored wooden bridge among soft golden clouds, sun rays from above, real wildflowers along the bridge edges"`
- Arşiv: `tools/limira_misc/d5r_prompts.json` (son gerçekçi 25), `d4_prompts.json`, `d3_prompts.json`.

### 6.3 Görselleri ChatGPT'de üret (iki sekme paralel)
1. Tarayıcı panelinde iki chatgpt.com sekmesi aç (tab-1, tab-2), ikisi de **yeni sohbet** olsun.
2. Her sekmede `javascript_tool` ile sırayla çalıştır:
   1. `tools/chatgpt/helpers_core.js` içeriğini olduğu gibi yapıştır. CSP yüzünden dışarıdan yüklenemez, satır içi yapıştırılmalı.
   2. `tools/chatgpt/pr_limira.js` içeriğini yapıştır.
   3. Kuyruğu başlat: `window.__Q={"d95":"<konu>","d97":"<konu>",...}; __LOG.push('---'); __run(null); 'ok'`. Key'leri böl: tek sayılar bir sekmede, çift sayılar diğerinde.
3. İlerlemeyi izle: `JSON.stringify(__SZ)+' '+__LOG.slice(-2).join('|')`. `__SZ` içinde `key=bayt` çiftleri olur. Görsel başına ~1,5–3 dk sürer; bitince log'da `ALLDONE` yazar.
4. **İndirme tuhaflığı:**
   - Arka plandaki sekmeden yapılan indirmeler `~/Downloads` içinde gizli bir dosya olarak kalabilir (`.Q6L2SF6YDW.com.anthropic.claudefordesktop.XXXX`, uzantısız).
   - `collect.sh` boyuta göre aradığı için bunları da bulur. Bu yüzden her görselin **bayt boyutunu** `__SZ`'den al.
5. ChatGPT bazen eski bir görseli tekrar gösterir. İki key aynı boyuttaysa biri kopyadır; o key'i yeniden üret.
6. "Görsel kullanılamıyor" ya da politika hatası alırsan:
   - `__done` bunu FAIL sayar, log'a `SKIP <key>` yazar ve devam eder.
   - Atlananları sonra yeni bir sohbette tekrar kuyruğa al.
7. Uzun sohbetlerde gönderme takılırsa yeni sohbet aç, kalan key'leri yeniden kuyruğa al.
   - Kalan kuyruğu saklamak için: `localStorage.__remQ=JSON.stringify(kalan)`.
   - Sayfa yenilendikten sonra helper'ları tekrar yapıştır, sonra `window.__Q=JSON.parse(localStorage.__remQ); __run(null)`.
8. Her görsele mutlaka bak:
   - Mac'te küçük bir kontak sayfası (sheet) oluştur, stage et ve Read ile görüntüle.
   - Kalite, gerçekçilik, yazı, filigran ve garip anatomi kontrol et.

### 6.4 Toplama → Printify → yayın (Mac)
```bash
cd $HOME/mnt/Documents/etsy-printify
bash yeni2/collect.sh d95=<bayt> d96=<bayt> ...        # "ok dXX" görmelisin
# SEO'yu önce yeni2/seo.json'a ekle (6.5)
timeout 165 python3 yeni2/taslak3.py d95 d96 ...      # "ok dXX <printify_id>"; bitmeyenler için tekrar
python3 yeni2/yayinla.py d95 d96 ...                  # "pub dXX"
sleep 120; timeout 160 python3 yeni2/ext.py           # "dXX <etsy_id> 320264294296"
```

### 6.5 SEO kuralları (`seo.json` formatı: `{"dXX":{"t":..., "g":[13], "a":...}}`)
- **t (başlık):**
  - En fazla 140 karakter, **":" yok**.
  - Kalıp: "<Konu> Canvas Wall Art, <ayrıntı> Art, <Hediye/duygu>, <oda/kullanım>".
  - Örnek: "Black Lab Memorial Canvas Wall Art, Labrador Crossing the Rainbow Bridge Art, Dog Loss Sympathy Gift, In Loving Memory of Dog".
  - Gerçekçi görsellerde "Painting" yerine **"Art"** kullan.
- **g (etiketler):**
  - **Tam 13 etiket**, her biri **en fazla 20 karakter**, tekrar yok, küçük harf.
  - Hediye ve duygu kelimeleri ekle: pet loss gift, sympathy gift, gift for him/her/mom, christmas gift.
- **a (hikâye paragrafı):**
  - 2–3 cümle. Duygusal bir açılış, sahnenin anlatımı ve kime hediye olduğu.
  - `desc_tpl2.txt`'deki `{ABOUT}` yerine geçer.
- Tüm kuralları assert ile kontrol et. Örnek script: `tools/limira_misc/seo_d5.py`. Bu script `seo_v6.json`/`seo_v7.json` üretiyordu; konteynerde hazırlayıp `device_commit_files` ile `~/Documents/etsy-printify/yeni2/seo.json` üzerine yazdık (`force:true`). Üzerine yazmadan önce Mac'te yedek al: `cp seo.json seo_bak_vN.json`.

### 6.6 Mockup üretimi (konteyner)
1. `device_stage_files` ile `~/Documents/etsy-printify/yeni2/raw/dXX.png` dosyalarını stage et. Hepsi `/mnt/user-data/uploads/Documents/etsy-printify/yeni2/raw/` altına düşer.
2. Mockup'ları üret:
   ```bash
   cd /home/claude/prev && (timeout 3500 bash run2.sh d95 d96 ... > /tmp/log 2>&1 &)
   # her ilan ~1-2 dk; y2out/<k>/ içinde 8 jpg olur
   ```
3. GitHub'a it:
   ```bash
   cd /home/claude/lm && for k in d95 d96; do mkdir -p limira/yeni/$k && cp /home/claude/prev/y2out/$k/* limira/yeni/$k/; done
   git add limira/yeni && git commit -m "limira mockups ..." && git push origin HEAD:limira-media
   ```
4. Bir ilan için örnek mockup'a bak (1_salon_yakin.jpg).

### 6.7 Etsy'ye mockup, ölçü rehberi, video ve cm ekle (tarayıcı, Limira girişli)
1. Bir sekmede `https://www.etsy.com/your/shops/me/tools/listings` aç. Sekmeyi öne getir (`tabs_select`); arka planda çok yavaşlıyor.
2. **localStorage'da kod var mı kontrol et:** `!!localStorage.__nwcode && !!localStorage.__cmcode`.
   - false ise GitHub'dan geri yükle:
     ```js
     const g=u=>{const x=new XMLHttpRequest();x.open('GET',u,false);x.send();return x.responseText;};
     const B='https://raw.githubusercontent.com/darkwildfiels/darkwildmedia/e777cd9/tools/etsy_js/';
     ['__nwcode','__cmcode','__sgcode','__vupcode'].forEach(k=>localStorage[k]=g(B+k+'.js')); 'ok'
     ```
3. Sürücüyü yükle ve kuyruğa ekle:
   ```js
   const x=new XMLHttpRequest();x.open('GET','https://raw.githubusercontent.com/darkwildfiels/darkwildmedia/97e53100aa71/limira/drv.js',false);x.send();eval(x.responseText);
   localStorage.__drvlog='[]';
   __add(['d95','<etsyId>'],['d96','<etsyId>'], ...)
   ```
   - Her ilan için `__nwcode(k)` çalışır: eski görselleri siler, 8 mockup + ölçü rehberini ve videoyu yükler, yayınlar.
   - Ardından `__cmcode` çalışır: varyant adlarını cm'li yapar.
   - Log: `JSON.parse(localStorage.__drvlog)`. Başarı görünümü: `"dXX nw ok 1->10->9 v"` ve `"dXX cm ok 8"`. Kuyruk bitince `IDLE`.
   - Ön planda ilan başına ~1,5 dk sürer.
4. **Aynı sekmede iki sürücü çalıştırma**, iframe'ler çakışır. Hızlandırmak için **ikinci bir Etsy sekmesinde** ayrı sürücü çalıştırabilirsin (aynı localStorage). Kuyruğu böl: `__JQ.splice(...)`.
5. Mac uyursa veya bağlantı koparsa sürücü yarıda kalır. Sekmeyi yenile, sürücüyü tekrar yükle, kalanları ekle. Fazla görsel olduysa `__nwcode` tekrar çalışınca düzeltir.
6. **DOĞRULAMA (her ilan):** herkese açık sayfayı XHR ile çek ve say. Her ilan `200/9/8/v` olmalı.
   ```js
   const chk=async(k,id)=>{const h=await new Promise(r=>{const x=new XMLHttpRequest();x.open('GET','https://www.etsy.com/listing/'+id+'?_='+Date.now());x.onload=()=>r(x.status+'|'+x.responseText);x.send();});
    const imgs=new Set(h.match(/il_fullxfull\.(\d+)_/g)||[]).size; const d=new DOMParser().parseFromString(h,'text/html');
    const cm=[...d.querySelectorAll('select option')].filter(o=>/cm/.test(o.textContent)).length;
    return k+':'+h.split('|')[0]+'/'+imgs+'/'+cm+'/'+(/\.mp4/.test(h)?'v':'-');};
   ```
   - 9 görsel, 8 cm seçeneği ve video olmalı.
   - 19–20 görsel çıkarsa Printify'ın varsayılan görselleri kalmış demektir; o ilan için sürücüyü tekrar çalıştır.

### 6.8 Rapor
Kullanıcıya kısa bir Türkçe rapor ver:
- kaç ilan yayında, konular,
- doğrulama sonucu,
- kargo profili hatırlatması.

---

## 7. ÖĞRENİLEN DERSLER VE TUZAKLAR
- **chatgpt.com CSP:** eval yok, dışarıdan script yok; kodu satır içi yapıştır. Etsy'de XHR + eval çalışır.
- **GitHub raw önbelleği:** yeni dosya yolları sorun çıkarmaz. Değişen bir JS dosyasını **commit SHA'lı URL** ile yükle, `limira-media` dal adıyla yükleme.
- **Printify publish takılırsa** ("locked"): `publishing_failed` çağrısı + yeniden publish. Bu bir kez Etsy'de kopya ilan yarattı (4617973871, deaktive edildi). Yeniden publish'ten önce Etsy'de var mı kontrol et.
- **`taslak3.py`:** ~130 sn sınırı var (device_bash 180 sn). Uzun işleri parçala.
- **Etsy fetch** bazen başarısız oluyor; XHR kullan.
- **İndirmeler:** arka plan sekmesinden yapılanlar gizli dosya olarak kalır. Tarih filtresi UTC.
- **Mac uykusu:** tarayıcı sürücüleri ve ChatGPT kuyruğu durur. Kullanıcıya "Mac'i uyutma" de.
- **Gerçekçi görsel stili kullanıcı isteğidir.** Yağlı boyaya dönme.

---

## 8. İLETİŞİM TARZI
- Türkçe, kısa ve net yaz. İşe başlarken tek cümleyle ne yapacağını söyle, sonra yap.
- Bitince sonucu birkaç cümleyle özetle: ne yayında, ne eksik, kullanıcının yapması gereken (örneğin hesap geçişi, kargo kontrolü).
- Uzun işlerde ara durum mesajı at (örneğin "görseller çiziliyor, X/25").
- Kullanıcı kısa komutlar verir: "limira listing başla 25 tane", "durum ne", "devam", "bana bir rapor ver".

// Pinterest pin yükleme (pinterest.com sekmesinde, kullanıcı giriş yapmışken). 17 Kasım'da bu yaklaşımla 45 pin atıldı.
// YENİDEN YAZILDI (orijinal satır içi koddu) -> önce TEK pin ile dene, pinterest.com'da kontrol et.
window.__pp=async(path,data)=>{const csrf=(document.cookie.match(/csrftoken=([^;]+)/)||[])[1];
 const body='source_url='+encodeURIComponent('/')+'&data='+encodeURIComponent(JSON.stringify({options:data,context:{}}));
 const r=await fetch('/resource/'+path+'/',{method:'POST',headers:{'X-CSRFToken':csrf,'X-Requested-With':'XMLHttpRequest','Content-Type':'application/x-www-form-urlencoded'},body,credentials:'include'});
 return r.status+' '+(await r.text()).slice(0,300);};
// tek pin: k=ilan anahtarı, board=board id, t=başlık, d=açıklama, link=etsy linki
window.__pin=(k,board,t,d,link)=>__pp('PinResource/create',{board_id:board,image_url:'https://raw.githubusercontent.com/darkwildfiels/darkwildmedia/limira-media/limira/pins/'+k+'_pin.jpg',title:t,description:d,link:link,method:'uploaded'});
// kuyruk (spam riskine karşı 1.5-3 dk ara): window.__PQ=[[k,board,t,d,link],...] (limira/pinterest/pq.js formatı)
window.__pinrun=async()=>{const L=[];for(const [k,b,t,d,l] of __PQ){L.push(k+' '+await __pin(k,b,t,d,l));localStorage.__pinlog=JSON.stringify(L);await new Promise(r=>setTimeout(r,90000+Math.random()*90000));}L.push('PINDONE');localStorage.__pinlog=JSON.stringify(L);};
'pin ok';

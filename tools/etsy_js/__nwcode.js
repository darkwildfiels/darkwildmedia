async(K)=>{const gx=u=>new Promise((res,rej)=>{const x=new XMLHttpRequest();x.open('GET',u);x.responseType=u.endsWith('.txt')||u.includes('.txt?')?'text':'blob';x.onload=()=>x.status==200?res(x.response):rej('st'+x.status);x.onerror=()=>rej('xhrerr '+u);x.send();});const S=ms=>new Promise(r=>setTimeout(r,ms));for(let i=0;i<25&&!document.querySelector('input[name=listing-media-upload]');i++)await S(1000);await S(2500);
const cnt=()=>[...document.querySelectorAll('img')].filter(i=>/Listing image|Primary listing/.test(i.alt)).length;
const del=()=>[...document.querySelectorAll('[data-testid=image-delete-button]')];
for(let k=0;k<30;k++){const b=del();if(b.length<=1)break;const t=b[b.length-1];(t.shadowRoot?.querySelector('button')||t).click();await S(400);}
const n0=cnt();
const B='https://raw.githubusercontent.com/darkwildfiels/darkwildmedia/limira-media/limira/';
const N=['1_salon_yakin','2_boyut','3_kemer','4_salon','5_giris','6_ofis','7_yemek','8_detay'];
const files=[];for(let i=0;i<8;i++){const b=await gx(B+'yeni/'+K+'/'+N[i]+'.jpg');if(b.size<10000)return 'fetchfail '+N[i];files.push(new File([b],'canvas-wall-art-'+(i+1)+'.jpg',{type:'image/jpeg'}));}
const sg=await gx(B+'limira_size_guide.jpg');files.push(new File([sg],'canvas-size-guide-inches-cm.jpg',{type:'image/jpeg'}));
const inp=document.querySelector('input[name=listing-media-upload]');let dt=new DataTransfer();files.forEach(f=>dt.items.add(f));inp.files=dt.files;inp.dispatchEvent(new Event('change',{bubbles:true}));
for(let i=0;i<40&&cnt()<n0+9;i++)await S(1500);const n1=cnt();if(n1<n0+9)return 'imgfail '+n0+'->'+n1;
const d0=del()[0];(d0.shadowRoot?.querySelector('button')||d0).click();await S(1500);
let vid='skip';if(!document.querySelector('video')){const vb=await gx(B+'limira_studio_video_5sn.mp4');const inp2=document.querySelector('input[name=listing-media-upload]');dt=new DataTransfer();dt.items.add(new File([vb],'limira-studio-canvas-wall-art.mp4',{type:'video/mp4'}));inp2.files=dt.files;inp2.dispatchEvent(new Event('change',{bubbles:true}));for(let i=0;i<15&&!document.querySelector('video');i++)await S(2000);vid=document.querySelector('video')?'v':'vfail';}
await S(2500);const n2=cnt();const p=[...document.querySelectorAll('button')].find(x=>x.innerText.trim()==='Publish changes');if(!p)return 'nopublish';localStorage.setItem('__nwres','ok '+n0+'->'+n1+'->'+n2+' '+vid);p.click();await S(6000);return 'ok '+n0+'->'+n1+'->'+n2+' '+vid;}
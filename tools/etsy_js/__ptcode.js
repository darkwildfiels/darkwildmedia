async(k)=>{const gx=u=>new Promise((res,rej)=>{const x=new XMLHttpRequest();x.open('GET',u);x.responseType=u.endsWith('.txt')||u.includes('.txt?')?'text':'blob';x.onload=()=>x.status==200?res(x.response):rej('st'+x.status);x.onerror=()=>rej('xhrerr '+u);x.send();});const S=ms=>new Promise(r=>setTimeout(r,ms));const L=m=>localStorage.setItem('__ptres',m);try{
for(let i=0;i<30&&!document.querySelector('input[name=listing-media-upload]');i++)await S(1000);await S(3000);
const cnt=()=>[...document.querySelectorAll('img')].filter(i=>/Listing image|Primary listing/.test(i.alt)).length;
const del=()=>[...document.querySelectorAll('[data-testid=image-delete-button]')];
for(let j=0;j<30;j++){const b=del();if(b.length<=1)break;const t=b[b.length-1];(t.shadowRoot?.querySelector('button')||t).click();await S(400);}
const n0=cnt();const B='https://raw.githubusercontent.com/darkwildfiels/darkwildmedia/limira-media/limira/';
const N=[k+'_1_salon_yakin',' before_after'.trim(),k+'_3_how',k+'_4_salon',k+'_8_detay','promise',k+'_4_styles',k+'_2_boyut'];
const files=[];for(let i=0;i<N.length;i++){const b=await gx(B+'pet/'+N[i]+'.jpg');if(b.size<10000){L('fetchfail '+N[i]);return;}files.push(new File([b],'custom-pet-portrait-canvas-'+(i+1)+'.jpg',{type:'image/jpeg'}));}
const sg=await gx(B+'limira_size_guide.jpg');files.push(new File([sg],'canvas-size-guide-inches-cm.jpg',{type:'image/jpeg'}));
const inp=document.querySelector('input[name=listing-media-upload]');const dt=new DataTransfer();files.forEach(f=>dt.items.add(f));inp.files=dt.files;inp.dispatchEvent(new Event('change',{bubbles:true}));
for(let i=0;i<40&&cnt()<n0+9;i++)await S(1500);const n1=cnt();if(n1<n0+9){L('imgfail '+n0+'->'+n1);return;}
const d0=del()[0];(d0.shadowRoot?.querySelector('button')||d0).click();await S(1500);
const setv=(el,v)=>{const proto=el.tagName==='TEXTAREA'?HTMLTextAreaElement.prototype:HTMLInputElement.prototype;Object.getOwnPropertyDescriptor(proto,'value').set.call(el,v);el.dispatchEvent(new Event('input',{bubbles:true}));el.dispatchEvent(new Event('change',{bubbles:true}));el.dispatchEvent(new Event('blur',{bubbles:true}));};
const t=await gx(B+'pet/seo_'+k+'.txt?'+Date.now());const g=(a,b)=>t.split(a)[1].split(b)[0].trim();
const title=g('###TITLE###','###TAGS###'),tags=g('###TAGS###','###DESCRIPTION###').split(',').map(s=>s.trim()).filter(s=>s&&s.length<=20).slice(0,13),desc=g('###DESCRIPTION###','###END###');
setv(document.getElementById('listing-title-input'),title);setv(document.getElementById('listing-description-textarea'),desc);await S(500);
for(let j=0;j<20;j++){const b=[...document.querySelectorAll('button')].find(b=>/^Delete tag /.test(b.getAttribute('aria-label')||''));if(!b)break;b.click();await S(250);}
const ti=document.getElementById('listing-tags-input');for(const tg of tags){setv(ti,tg);await S(300);[...document.querySelectorAll('button')].find(b=>b.innerText.trim()==='Add'&&b.offsetParent).click();await S(400);}
const ntag=[...document.querySelectorAll('button')].filter(b=>/^Delete tag /.test(b.getAttribute('aria-label')||'')).length;
[...document.querySelectorAll('input')].filter(i=>/controls\.sku/.test(i.name)).forEach(i=>setv(i,''));await S(500);
const addf=async(kind,title,ins,nf)=>{[...document.querySelectorAll('button')].find(b=>b.innerText.trim()==='Add field').click();await S(1500);[...document.querySelectorAll('[role=menuitem],button,li')].filter(e=>e.offsetParent&&e.innerText.trim().startsWith(kind)).pop().click();await S(2500);const q=document.getElementById('field-personalizationQuestions-questionText');q.focus();document.execCommand('insertText',false,title);await S(400);if(nf){const sel=document.getElementById('field-personalizationQuestions-numberOfFiles');Object.getOwnPropertyDescriptor(HTMLSelectElement.prototype,'value').set.call(sel,nf);sel.dispatchEvent(new Event('change',{bubbles:true}));await S(300);}const ie=document.getElementById('field-personalizationQuestions-instructions');ie.focus();document.execCommand('insertText',false,ins);await S(500);const dl=[...document.querySelectorAll('[role=dialog]')].filter(e=>e.offsetParent).pop();[...dl.querySelectorAll('button')].find(b=>b.innerText.trim()==='Done').click();await S(1500);};
await addf('File upload','Pet photo','Clear, bright photo with the face visible. Up to 3 photos.','3');
await addf('Text box',"Pet's name (or write: no name)",'Name to show on the portrait. You can also add dates or a short note.',null);
const bt=document.body.innerText;const pers=/Pet photo/.test(bt)&&/Pet's name/.test(bt);
const skus=[...document.querySelectorAll('input')].filter(i=>/controls\.sku/.test(i.name)).map(i=>i.value).join('');
L('ready imgs='+cnt()+' tags='+ntag+' pers='+pers+' sku=['+skus+'] title='+document.getElementById('listing-title-input').value.length+' ship='+((bt.match(/average costs, (\d+)/)||[])[1]));}catch(e){L('ERR '+e);}}
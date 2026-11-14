window.gx=(u,type='blob')=>new Promise((res,rej)=>{const x=new XMLHttpRequest();x.open('GET',u+(u.includes('?')?'':'?t='+Date.now()));x.responseType=type;x.onload=()=>x.status<300?res(x.response):rej('HTTP '+x.status+' '+u);x.onerror=()=>rej('xhr err '+u);x.send();});
window.__sl=ms=>new Promise(r=>setTimeout(r,ms));
window.__RAW='https://raw.githubusercontent.com/darkwildfiels/darkwildmedia/limira-media/mira/';
window.__setv=(el,v)=>{const proto=el.tagName=='TEXTAREA'?HTMLTextAreaElement.prototype:HTMLInputElement.prototype;Object.getOwnPropertyDescriptor(proto,'value').set.call(el,v);el.dispatchEvent(new Event('input',{bubbles:true}));el.dispatchEvent(new Event('change',{bubbles:true}));};
window.__btn=(txt,root=document)=>[...root.querySelectorAll('button')].filter(b=>b.innerText.trim()==txt);
window.__files=async(input,list)=>{const dt=new DataTransfer();for(const [u,name,type] of list){const b=await gx(u);dt.items.add(new File([b],name,{type}));}input.files=dt.files;input.dispatchEvent(new Event('change',{bubbles:true}));};
window.__near=(id,txt,lv)=>{let p=document.getElementById(id),b=null;for(let k=0;k<lv&&!b&&p;k++){p=p.parentElement;b=[...p.querySelectorAll('button')].find(x=>x.innerText.trim()==txt);}return b;};
window.__dlgBtn=(txt)=>[...document.querySelectorAll('button')].find(b=>b.offsetParent&&b.innerText.trim()==txt&&b.closest('[role=dialog],[role=alertdialog]'));
window.__fin=(after)=>{const t=document.querySelector('textarea[name=title]');const L=[...document.querySelectorAll('input[type=file]')];return after?L.find(e=>t.compareDocumentPosition(e)&4):L.filter(e=>t.compareDocumentPosition(e)&2).pop();};
window.__log=(m)=>{const a=JSON.parse(localStorage.__gfres||'[]');a.push(m);localStorage.__gfres=JSON.stringify(a);};
window.__gf=async(o)=>{localStorage.__gfres='[]';try{
 __log('start '+o.k);
 const seo=await gx(__RAW+'seo_'+o.k+'.txt','text');
 const T=seo.split('###TITLE###\n')[1].split('\n###TAGS###')[0].trim(), G=seo.split('###TAGS###\n')[1].split('\n###DESCRIPTION###')[0].trim().split(',').map(s=>s.trim()), D=seo.split('###DESCRIPTION###\n')[1].split('\n###END###')[0];
 if(o.cat){const sp=[...document.querySelectorAll('span')].find(e=>e.children.length==0&&e.textContent.trim()=='Change');if(sp){let p=sp;while(p&&p.getAttribute('role')!='button'&&p.tagName!='BUTTON')p=p.parentElement;(p||sp).click();await __sl(1200);}
  const i=document.getElementById('listing-editor_category-search-typeahead');i.click();i.focus();__setv(i,'');__setv(i,o.catq||o.cat);await __sl(2500);
  const op=[...document.querySelectorAll('[role=option]')].filter(e=>e.offsetParent).find(e=>e.textContent.trim().startsWith(o.cat));if(op){op.click();__log('cat ok');}else __log('CAT FAIL');await __sl(1500);}
 const da=__btn('Delete all')[0], tda=__near('listing-tags-input','Delete all',9);
 if(da&&da!==tda){da.click();await __sl(1200);const c=__dlgBtn('Delete all')||__dlgBtn('Delete');if(c)c.click();await __sl(1800);}
 await __files(__fin(false),o.imgs.map(n=>[__RAW+o.k+'/'+n,n,'image/jpeg']));__log('imgs sent');
 if(o.pdfs&&o.pdfs.length)for(const b of [...document.querySelectorAll('button[aria-label=Remove]')]){b.click();await __sl(600);}
 await __sl(800);
 if(o.pdfs&&o.pdfs.length){await __files(__fin(true),o.pdfs.map(n=>[__RAW+o.k+'/'+n,n,'application/pdf']));__log('pdfs sent');}
 __setv(document.querySelector('textarea[name=title]'),T);
 __setv(document.querySelector('textarea[name=description]'),D);
 const dt=__near('listing-tags-input','Delete all',9);if(dt){dt.click();await __sl(1000);const c=__dlgBtn('Delete all');if(c)c.click();await __sl(1000);}
 const ti=document.getElementById('listing-tags-input');
 for(const g of G){__setv(ti,g);await __sl(150);__near('listing-tags-input','Add',6).click();await __sl(250);}
 if(o.price)__setv(document.getElementById('listing-price-input'),String(o.price));
 if(o.section){const s=document.getElementById('shop-section-select');s.value=o.section;s.dispatchEvent(new Event('change',{bubbles:true}));}
 await __sl(o.wait||15000);
 const nimg=[...document.querySelectorAll('img')].filter(i=>document.querySelector('textarea[name=title]').compareDocumentPosition(i)&2&&i.offsetParent&&/etsystatic/.test(i.src)).length;
 const nf=(o.pdfs||[]).filter(n=>document.body.innerText.includes(n)).length;
 const t=document.body.innerText;const a=t.indexOf('Add up to 13 tags');const ntag=(t.slice(a,a+700).match(/All 13 used/)?13:-1);
 __log(`check imgs=${nimg} pdfs=${nf} tags=${ntag}`);
 if(o.publish===false){__log('NOPUB');return;}
 if(nimg<o.imgs.length||(o.pdfs&&nf<o.pdfs.length)||ntag!=13){__log('ABORT check failed');return;}
 const pb=[...document.querySelectorAll('button')].find(b=>b.offsetParent&&/^Publish/.test(b.innerText.trim())&&!b.closest('[role=dialog],[role=alertdialog]'));pb.click();await __sl(4000);
 for(let k=0;k<4;k++){const b=__dlgBtn('Publish')||__dlgBtn('Skip and continue')||__dlgBtn('Activate');if(!b)break;__log('dlg '+b.innerText.trim());b.click();await __sl(4000);}
 __log('published?');
}catch(e){__log('ERR '+e);}};
'helper ok';

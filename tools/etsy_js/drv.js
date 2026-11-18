window.__ifr=(url)=>new Promise(res=>{let f=document.getElementById('__drv');if(f)f.remove();f=document.createElement('iframe');f.id='__drv';f.style.cssText='position:fixed;left:0;top:0;width:1400px;height:900px;opacity:0.01;z-index:-1';f.onload=()=>res(f);f.src=url;document.body.appendChild(f);});
window.__lg=m=>{const a=JSON.parse(localStorage.__drvlog||'[]');a.push(m);localStorage.__drvlog=JSON.stringify(a.slice(-120));};
window.__job=async(k,id)=>{
 let f=await __ifr('https://www.etsy.com/your/shops/me/listing-editor/edit/'+id); await new Promise(r=>setTimeout(r,4000));
 let r; try{ r=await f.contentWindow.eval('('+localStorage.__nwcode+')')(k);}catch(e){r='ERR '+e;} __lg(k+' nw '+r);
 await new Promise(r=>setTimeout(r,8000));
 f=await __ifr('https://www.etsy.com/your/shops/me/listing-editor/edit/'+id); await new Promise(r=>setTimeout(r,5000));
 try{ r=await f.contentWindow.eval('('+localStorage.__cmcode+')')();}catch(e){r='ERR '+e;} __lg(k+' cm '+r); await new Promise(r=>setTimeout(r,6000)); };
window.__JQ=window.__JQ||[];
window.__add=(...items)=>{__JQ.push(...items); if(!window.__running){window.__running=true;(async()=>{while(__JQ.length){const [k,id]=__JQ.shift(); try{await __job(k,id);}catch(e){__lg(k+' JOBERR '+e);} } window.__running=false; __lg('IDLE');})();} return 'q '+__JQ.length;};
'drv ok';

window.__mlg=m=>{const a=JSON.parse(localStorage.__mdrv||'[]');a.push(m);localStorage.__mdrv=JSON.stringify(a.slice(-150));};
window.__mifr=(url)=>new Promise(res=>{let f=document.getElementById('__mdrvf');if(f)f.remove();f=document.createElement('iframe');f.id='__mdrvf';f.style.cssText='position:fixed;left:0;top:0;width:1400px;height:900px;opacity:0.01;z-index:-1';f.onload=()=>res(f);f.src=url;document.body.appendChild(f);});
window.__mjob=async(o,src,helper)=>{
 const f=await __mifr('https://www.etsy.com/your/shops/me/listing-editor/copy/'+src); await new Promise(r=>setTimeout(r,5000));
 f.contentWindow.eval(helper);
 const p=f.contentWindow.__gf(o);
 const t0=Date.now(); let last='';
 while(Date.now()-t0<240000){await new Promise(r=>setTimeout(r,4000)); last=localStorage.__gfres||''; if(/published\?|ABORT|ERR|NOPUB/.test(last))break;}
 await new Promise(r=>setTimeout(r,6000));
 let path=''; try{path=f.contentWindow.location.pathname}catch(e){}
 __mlg(o.k+' '+last.replace(/[\[\]"]/g,'').slice(-90)+' @'+path);
};
window.__MQ=window.__MQ||[];
window.__madd=(helper,...items)=>{window.__MH=helper;__MQ.push(...items);if(!window.__mrun){window.__mrun=true;(async()=>{while(__MQ.length){const [o,src]=__MQ.shift();try{await __mjob(o,src,__MH);}catch(e){__mlg(o.k+' JOBERR '+e);}}window.__mrun=false;__mlg('IDLE');})();}return 'q '+__MQ.length;};
'mdrv ok';

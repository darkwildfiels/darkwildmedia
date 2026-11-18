// Mira (boyama sayfası) - s zaten "Create a printable coloring page: <konu>. <STİL>" şeklinde tam prompt
window.__PFX='mira_';
window.__PR=function(s,k){return "New separate image, completely unrelated to the previous ones. "+s;};
window.__STY={
 K:"Black and white line art only, cute kawaii cartoon style for kids ages 3-8, very thick clean outlines and large simple open spaces to color, pure white background, no shading, no gray, no color fill, no text, no border. Portrait orientation (2:3).",
 B:"Black and white line art only, bold and easy style with thick clean outlines and large open spaces to color, great for adults and seniors, pure white background, no shading, no gray, no color fill, no text, no border. Portrait orientation (2:3).",
 D:"Black and white line art only, detailed and intricate adult coloring book style with fine clean outlines and many small areas to color, pure white background, no shading, no gray, no color fill, no text, no border. Portrait orientation (2:3)."};
// kullanım: const RQ={"XX1":["K","konu"],...}; window.__Q={}; for(const [k,[c,t]] of Object.entries(RQ)) __Q[k]='Create a printable coloring page: '+t+'. '+__STY[c]; __run(null);
'pr mira ok';

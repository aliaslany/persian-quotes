const DATA = 'https://cdn.jsdelivr.net/gh/aliaslany/persian-quotes@main/data';
const WIKI = 'https://en.wikipedia.org/api/rest_v1/page/summary/';
let poets = [];
let currentQuote = null;
const $ = (id) => document.getElementById(id);

async function getJSON(url){const res=await fetch(url);if(!res.ok)throw new Error(`HTTP ${res.status}`);return res.json()}
function random(arr){return arr[Math.floor(Math.random()*arr.length)]}
function escapeHtml(value){return String(value).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]))}

async function poetImage(poet){
  try{
    const page=await getJSON(`${WIKI}${encodeURIComponent(poet.name_en.replace(/ /g,'_'))}`);
    return page.thumbnail?.source || page.originalimage?.source || null;
  }catch{return null}
}

async function loadPoets(){
  poets=await getJSON(`${DATA}/poets.json`);
  $('poetCount').textContent=`${poets.length} شاعر`;
  $('poetGrid').innerHTML=poets.map(p=>`<button class="poet" data-slug="${escapeHtml(p.slug)}"><span class="poet-avatar" data-avatar="${escapeHtml(p.slug)}"><span>${escapeHtml(p.name_fa.charAt(0))}</span></span><span class="poet-info"><strong>${escapeHtml(p.name_fa)}</strong><small>${escapeHtml(p.name_en)} · ${p.died}</small></span></button>`).join('');
  const cards=[...document.querySelectorAll('.poet')];
  cards.forEach(el=>el.addEventListener('click',()=>loadQuote(el.dataset.slug)));
  await Promise.all(poets.map(async p=>{
    const image=await poetImage(p);
    if(image){const avatar=document.querySelector(`[data-avatar="${CSS.escape(p.slug)}"]`);if(avatar)avatar.innerHTML=`<img src="${escapeHtml(image)}" alt="تصویر ${escapeHtml(p.name_fa)}" loading="lazy" referrerpolicy="no-referrer">`;}
  }));
}

async function loadQuote(slug){
  try{
    const poet=poets.find(p=>p.slug===slug)||random(poets);
    const quotes=await getJSON(`${DATA}/all/${poet.slug}.json`);
    const q=random(quotes);
    currentQuote=q;
    $('quoteText').textContent=q.text;
    $('author').textContent=`— ${q.author||poet.name_fa}`;
    $('authorEn').textContent=q.author_en||poet.name_en;
    $('category').textContent=q.category_fa||'سخن فارسی';
    $('quoteId').textContent=`#${q.id}`;
    document.title=`${poet.name_fa} | گنجینهٔ سخن`;
  }catch(e){$('quoteText').textContent='دریافت داده ممکن نشد. دوباره تلاش کنید.';console.error(e)}
}

$('randomBtn').addEventListener('click',()=>loadQuote());
$('copyBtn').addEventListener('click',async()=>{
  if(!currentQuote)return;
  const text=`${currentQuote.text}\n\n— ${currentQuote.author||''}`;
  try{await navigator.clipboard.writeText(text);$('copyBtn').textContent='کپی شد ✓';setTimeout(()=>$('copyBtn').textContent='کپی',1400)}catch{}
});

(async()=>{try{await loadPoets();await loadQuote()}catch(e){$('quoteText').textContent='بارگذاری داده‌ها ناموفق بود.';console.error(e)}})();

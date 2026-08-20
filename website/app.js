const DATA = 'https://cdn.jsdelivr.net/gh/aliaslany/persian-quotes@main/data';
let poets = [];
let currentQuote = null;
const $ = (id) => document.getElementById(id);

async function getJSON(url){const res=await fetch(url);if(!res.ok)throw new Error(`HTTP ${res.status}`);return res.json()}
function random(arr){return arr[Math.floor(Math.random()*arr.length)]}

async function loadPoets(){
  poets=await getJSON(`${DATA}/poets.json`);
  $('poetCount').textContent=`${poets.length} شاعر`;
  $('poetGrid').innerHTML=poets.map(p=>`<button class="poet" data-slug="${p.slug}"><strong>${p.name_fa}</strong><small>${p.name_en} · ${p.died}</small></button>`).join('');
  document.querySelectorAll('.poet').forEach(el=>el.addEventListener('click',()=>loadQuote(el.dataset.slug)));
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
  }catch(e){$('quoteText').textContent='دریافت داده ممکن نشد. دوباره تلاش کنید.';console.error(e)}
}

$('randomBtn').addEventListener('click',()=>loadQuote());
$('copyBtn').addEventListener('click',async()=>{
  if(!currentQuote)return;
  const text=`${currentQuote.text}\n\n— ${currentQuote.author||''}`;
  try{await navigator.clipboard.writeText(text);$('copyBtn').textContent='کپی شد ✓';setTimeout(()=>$('copyBtn').textContent='کپی',1400)}catch{}
});

(async()=>{try{await loadPoets();await loadQuote()}catch(e){$('quoteText').textContent='بارگذاری داده‌ها ناموفق بود.';console.error(e)}})();

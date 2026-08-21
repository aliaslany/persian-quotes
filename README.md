# persian-quotes

A large, categorized dataset of classical Persian poetry — packaged as static
JSON so any app can fetch a random quote with zero backend, zero API key,
and zero rate limits.

**43,564 quotes** (couplets/beyts) from **38 classical Persian poets**
(Hafez, Rumi, Saadi, Khayyam, Ferdowsi, Attar, Jami, Rudaki, and more),
tagged into 6 themes.

🔗 **Live site & docs:** `https://USERNAME.github.io/persian-quotes/`

Every poet included died more than 175 years ago, so the underlying text is
public domain worldwide. See [LICENSE.md](LICENSE.md) for details and for
how to extend this dataset with modern (still-copyrighted) poets yourself.

## Fetch a random quote — no server needed

Because this is just static JSON on GitHub, you can serve it straight from
jsDelivr's CDN (fast, cached, free) and pick a random entry client-side:

```js
const res = await fetch(
  "https://cdn.jsdelivr.net/gh/USERNAME/persian-quotes@main/data/quotes.json"
);
const quotes = await res.json();
const quote = quotes[Math.floor(Math.random() * quotes.length)];
console.log(quote.text, "—", quote.author);
```

> Replace `USERNAME` with your GitHub username once you push this repo.
> `raw.githubusercontent.com/USERNAME/persian-quotes/main/data/quotes.json`
> works the same way (no CDN caching, but always up to date).

Full endpoint reference, curl/Python examples, and a live in-browser demo
are on the docs site — see `docs/index.html`, published via GitHub Pages.

## Data layout

```
data/
  quotes.json            # all 43,564 quotes (~12MB)
  featured.json          # 90-quote curated sample, used by the docs site demo
  poets.json             # metadata for all 38 poets
  quotes/                # split by theme
    eshgh.json            عشق      love         (4,313)
    hekmat.json            حکمت      wisdom       (22,641)
    zendegi.json           زندگی      life         (2,699)
    erfan.json              عرفان      mysticism    (9,679)
    marg.json                مرگ و هستی mortality    (1,053)
    tabiat.json              طبیعت      nature       (3,179)
  all/
    hafez.json, rumi.json, saadi.json, ... # split by poet, one file each
```

Each quote object looks like:

```json
{
  "id": 20001,
  "text": "پس هم به دو چشم مست ساقی\nمی آن نظری به چشم اجمل",
  "author": "فخرالدین عراقی",
  "author_en": "Fakhr al Din Iraqi",
  "category": "erfan",
  "category_fa": "عرفان"
}
```

`text` is a full beyt (two mesras joined by `\n`) rather than a single
half-line, since a lone mesra is usually not a complete thought in
classical Persian poetry.

## Fetch by category or by poet

```js
// only wisdom quotes
const wisdom = await fetch(
  "https://cdn.jsdelivr.net/gh/USERNAME/persian-quotes@main/data/quotes/hekmat.json"
).then(r => r.json());

// only Rumi
const rumi = await fetch(
  "https://cdn.jsdelivr.net/gh/USERNAME/persian-quotes@main/data/all/rumi.json"
).then(r => r.json());
```

## JS/TS helper (optional)

`src/index.js` wraps this into a couple of convenience functions — see
[src/README.md](src/README.md) if you want to publish it to npm.

```js
import { getRandomQuote, getRandomQuoteByCategory } from "./src/index.js";

const q = await getRandomQuote("USERNAME");
const wise = await getRandomQuoteByCategory("USERNAME", "hekmat");
```

## The docs site (GitHub Pages)

`docs/index.html` is a static one-page site: a live random-quote demo up
top, then a full API reference for developers (endpoints, JS/curl/Python
snippets, category and poet tables). To publish it:

1. Push this repo to GitHub.
2. Repo Settings → Pages → Deploy from branch → `main` / `/docs`.
3. Your site is live at `https://USERNAME.github.io/persian-quotes/`.

## Regenerating / extending the dataset

The full pipeline is reproducible — see `scripts/build.py`. It reads a
plain-text corpus (one line per mesra, two mesras per beyt) and produces
all the JSON files above.

```bash
git clone https://github.com/amnghd/Persian_poems_corpus.git
python3 scripts/build.py \
  --source Persian_poems_corpus/original \
  --out data \
  --cap 1200   # max quotes kept per poet, for balance
```

To add more poets, add an entry to the `POETS` dict in `scripts/build.py`
with the source filename, English/Persian name, and death year — and check
[LICENSE.md](LICENSE.md) first if the poet died less than ~150–175 years ago.

Category tagging in `categorize()` is a simple keyword heuristic, not a
real classifier — patches that improve it are welcome.

## Contributing

PRs adding more public-domain poets, fixing OCR/transcription glitches, or
improving the category heuristic are welcome. Please keep modern
(post-1900) poets out of `data/` unless you've confirmed the rights
situation for your target audience — see LICENSE.md.

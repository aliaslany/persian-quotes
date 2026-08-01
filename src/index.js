const BASE = (user, ref = "main") =>
  `https://cdn.jsdelivr.net/gh/${user}/persian-quotes@${ref}/data`;

async function fetchJson(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`persian-quotes: failed to fetch ${url} (${res.status})`);
  return res.json();
}

function pickRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}

/**
 * Fetch a random quote from the full dataset.
 * @param {string} githubUser - GitHub username hosting the repo fork.
 * @param {{ ref?: string }} [opts]
 */
export async function getRandomQuote(githubUser, opts = {}) {
  const quotes = await fetchJson(`${BASE(githubUser, opts.ref)}/quotes.json`);
  return pickRandom(quotes);
}

/**
 * Fetch a random quote from one theme.
 * Valid categories: eshgh (love), hekmat (wisdom), zendegi (life),
 * erfan (mysticism), marg (mortality), tabiat (nature).
 */
export async function getRandomQuoteByCategory(githubUser, category, opts = {}) {
  const quotes = await fetchJson(`${BASE(githubUser, opts.ref)}/quotes/${category}.json`);
  return pickRandom(quotes);
}

/**
 * Fetch a random quote from one poet (use the slug, e.g. "hafez", "rumi").
 * See data/poets.json for the full list of slugs.
 */
export async function getRandomQuoteByPoet(githubUser, poetSlug, opts = {}) {
  const quotes = await fetchJson(`${BASE(githubUser, opts.ref)}/all/${poetSlug}.json`);
  return pickRandom(quotes);
}

/** Fetch metadata for all 38 poets (name, death year, source file). */
export async function getPoets(githubUser, opts = {}) {
  return fetchJson(`${BASE(githubUser, opts.ref)}/poets.json`);
}

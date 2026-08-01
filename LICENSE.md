# License & provenance

This repo has two different things in it, licensed differently.

## Code (`scripts/`, `src/`)

MIT License — see below. Do whatever you want with the build script and
the JS helper.

## Text data (`data/`)

The quotes are couplets from **classical Persian poets who all died more
than 175 years ago** (the most recent, Hatef Esfahani, died in 1783). Under
every major jurisdiction's copyright term (life + 50 to life + 100 years),
work this old is in the public domain — the poetry itself is free to use,
copy, and redistribute, commercially or otherwise.

**Provenance:** the raw text was originally digitized by
[ganjoor.net](https://ganjoor.net), Iran's open digital archive of Persian
literature, and this dataset was built on top of a pre-scraped corpus from
[amnghd/Persian_poems_corpus](https://github.com/amnghd/Persian_poems_corpus).
That upstream repo doesn't carry an explicit license file itself, so if
you're using this data in a commercial product it's worth being aware
that while the *poetry* is unambiguously public domain, the specific
transcription/formatting choices in that upstream corpus theoretically
could carry a thin database-compilation right in some jurisdictions
(this doesn't apply in the US, but may in the EU). This repo's own
`scripts/build.py` re-derives and re-normalizes the text independently,
which mitigates but may not fully eliminate that concern — if it matters
for your use case, consult a lawyer or re-derive the beyts directly from
ganjoor.net's own API instead.

**If you extend this dataset with 20th-century or living poets**
(Shahriar, Farrokhi Yazdi, Parvin Etesami, Forough Farrokhzad, etc.), be
aware their work is very likely still under copyright in many countries,
and you'd need to handle permissions/licensing for those separately —
don't just drop them into `data/` assuming the same public-domain status.

---

MIT License

Copyright (c) 2026 contributors to this repository

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.

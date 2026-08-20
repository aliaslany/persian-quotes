# OpenQuotes / Persian Quotes

> A multilingual, open-source, structured quote database built from Wikiquote and other public sources, with a dedicated Persian poetry dataset and web experience.

![License](https://img.shields.io/badge/license-CC--BY--SA-blue)
![Status](https://img.shields.io/badge/status-active-success)
![Languages](https://img.shields.io/badge/languages-growing-brightgreen)

**🌐 [Open the Persian Quotes website](https://aliaslany.github.io/persian-quotes/)** · **[فارسی: README.fa.md](README.fa.md)**

---

## Vision

OpenQuotes aims to become the largest structured multilingual quotation database available as open-source.

Unlike traditional quote repositories that simply store text, OpenQuotes treats quotations as structured knowledge.

Every quote is connected to:

* its author
* verified sources
* translations
* professions
* tags
* categories
* historical metadata
* Wikidata
* Wikipedia

The long-term objective is to provide an open dataset that developers, researchers, translators, AI systems, educational platforms, and quote applications can build upon.

---

# Persian Quotes Website

The repository now includes a lightweight, RTL Persian website in `website/` and an automated GitHub Pages deployment workflow.

The website provides:

* Random Persian quote
* Poet explorer
* Persian RTL interface
* Quote copying
* Category and author metadata
* Responsive dark interface
* No backend required

The site reads the dataset through a CDN, so the frontend remains static and suitable for GitHub Pages.

---

# Project Goals

## Short Term

* Normalize Wikiquote output
* Build multilingual architecture
* Maintain a GitHub Pages showcase
* Add Persian translations
* Stable JSON schemas
* Automatic validation

## Mid Term

* Search engine
* REST API
* GraphQL API
* Daily quote generator
* AI-assisted translation
* GitHub Actions automation

## Long Term

Become a major multilingual quotation database supporting many languages, verified references, public APIs, SDKs, educational datasets, and responsibly licensed AI datasets.

---

# Repository Architecture

```text
OpenQuotes/
├── parser/
├── data/
├── schemas/
├── scripts/
├── website/
├── api/
├── docs/
├── tests/
├── output/
├── src/
└── .github/
```

The Persian dataset is primarily stored under `data/`, with poet metadata in `data/poets.json` and per-poet records under `data/all/`.

---

# JavaScript API

The package exposes helpers for consuming the dataset without a backend:

```js
import {
  getRandomQuote,
  getRandomQuoteByCategory,
  getRandomQuoteByPoet,
  getPoets
} from './src/index.js';

const quote = await getRandomQuote('aliaslany');
const hafez = await getRandomQuoteByPoet('aliaslany', 'hafez');
const poets = await getPoets('aliaslany');
```

---

# Data Architecture

The repository follows a normalized model for the broader OpenQuotes project.

## authors

Stores one record per person.

## quotes

Stores quote metadata and provenance.

## translations

Stores one record per quote per language.

## tags

Topics such as Life, Science, Love, Education, Leadership, and Philosophy.

## professions

Examples include Physicist, Philosopher, Writer, Poet, Economist, Engineer, and Psychologist.

## sources

Every quote should have traceable provenance whenever possible.

---

# Website Deployment

The website is deployed from `website/` using `.github/workflows/deploy-pages.yml`.

The workflow uses GitHub's Pages Actions and deploys on pushes to `main`.

After enabling **Settings → Pages → Source: GitHub Actions**, the project is available at:

**https://aliaslany.github.io/persian-quotes/**

---

# Contribution Workflow

```text
Fork
↓
Branch
↓
Develop
↓
Run Validation
↓
Create Pull Request
↓
Automatic CI
↓
Review
↓
Merge
```

---

# Licensing

The parser code and the dataset may have different licensing requirements.

The project must preserve attribution and comply with the licensing of upstream sources such as Wikiquote and MediaWiki content. Contributors should ensure redistributed content retains required notices and attribution.

---

# Roadmap

## Phase 1

* Normalize parser output
* Define schemas
* Create website foundation
* GitHub Pages deployment

## Phase 2

* Search
* Author pages
* Quote cards
* Statistics
* Dark mode
* Persian translations

## Phase 3

* API
* GraphQL
* Search indexing
* Daily quotes
* AI-assisted translation
* Contributor dashboard

## Phase 4

* Additional languages
* Mobile application
* Desktop application
* Browser extension
* SDKs
* Public API service

---

# Future Ideas

* AI semantic search
* Quote similarity graph
* Knowledge graph integration
* Wikidata synchronization
* Citation verification
* OCR ingestion for public-domain texts
* Interactive quote maps
* Historical timelines
* Reading lists
* Educational collections
* Telegram bot
* Discord bot
* Slack integration
* VS Code extension
* Offline dataset releases
* Monthly data snapshots
* Community translation portal
* Contributor leaderboard

---

**Persian documentation:** [README.fa.md](README.fa.md)

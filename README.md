# OpenQuotes

> A multilingual, open-source, structured quote database built from Wikiquote and other public sources.

![License](https://img.shields.io/badge/license-CC--BY--SA-blue)
![Status](https://img.shields.io/badge/status-active-success)
![Languages](https://img.shields.io/badge/languages-growing-brightgreen)

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

# Why this project exists

Most quote repositories suffer from one or more of these problems:

* duplicated author information
* only one language
* poor metadata
* no source verification
* inconsistent JSON formats
* impossible to maintain
* difficult searching
* no translation workflow
* no automated updates

OpenQuotes addresses these issues through a normalized architecture and automated pipelines.

---

# Project Goals

## Short Term

* Normalize Wikiquote output
* Build multilingual architecture
* Build GitHub Pages showcase
* Add Persian translations
* Stable JSON schemas
* Automatic validation

---

## Mid Term

* Search engine
* REST API
* GraphQL API
* Daily quote generator
* AI-assisted translation
* GitHub Actions automation

---

## Long Term

Become the largest multilingual quotation database on GitHub.

Support

* 100+ languages
* millions of translations
* verified references
* contributor ecosystem
* public APIs
* SDKs
* educational datasets
* AI training datasets (respecting licensing)

---

# Repository Architecture

```
OpenQuotes/

├── parser/
│
├── data/
│
├── schemas/
│
├── scripts/
│
├── website/
│
├── api/
│
├── docs/
│
├── tests/
│
├── output/
│
└── .github/
```

---

# Data Architecture

The repository follows a normalized model.

No duplicated information.

## authors

Stores one record per person.

Contains

* unique id
* slug
* Wikidata ID
* Wikipedia links
* multilingual names
* birth/death years
* nationality
* image
* aliases

---

## quotes

Stores quote metadata only.

Contains

* author id
* source id
* original language
* verification state
* timestamps

The quote text itself is NOT stored here.

---

## translations

Stores one record per quote per language.

Supports

* English
* Persian
* Arabic
* Turkish
* French
* German
* etc.

Metadata

* translator
* reviewer
* translation status
* quality score
* update history

---

## tags

Topics such as

* Life
* Science
* Love
* Education
* Leadership
* Philosophy

---

## professions

Examples

* Physicist
* Philosopher
* Writer
* Poet
* Economist
* Engineer
* Psychologist

---

## sources

Every quote should have traceable provenance whenever possible.

Examples

* Wikiquote
* Books
* Interviews
* Speeches
* Scientific publications
* Letters

---

# Canonical Storage Format

Canonical datasets use JSON Lines (`.jsonl`).

Advantages:

* scalable
* streamable
* merge-friendly
* cleaner Git history
* efficient processing

Optional export formats:

* JSON
* CSV
* SQLite
* DuckDB
* Parquet

---

# Website

The website serves as the public showcase of the dataset.

Technology

* React
* Vite
* TypeScript
* Tailwind CSS
* Framer Motion

Main features

* Beautiful landing page
* Random quote
* Daily quote
* Instant search
* Author pages
* Category pages
* Statistics
* Responsive design
* Dark mode
* Language switching
* Share buttons
* Copy quote
* Favorites (local storage)

---

# Future Website Features

## Quote Comparison

Display multiple translations side by side.

---

## Quote Timeline

View quotes chronologically.

---

## Author Explorer

Interactive author profiles.

---

## Search

Search by

* text
* author
* language
* profession
* nationality
* century
* category

---

## Quote Collections

Examples

* Women in Science
* Ancient Philosophy
* Startup Founders
* Persian Literature
* Nobel Prize Winners

---

# API

Future REST API

```
GET /quotes/random

GET /quotes/{id}

GET /authors

GET /authors/{slug}

GET /search

GET /languages

GET /tags

GET /daily
```

Future GraphQL endpoint

```
/graphql
```

---

# Translation Workflow

```
Original Quote

↓

Language Detection

↓

Machine Translation

↓

Human Review

↓

Verification

↓

Publication
```

Translation states

* machine
* reviewed
* verified

---

# Parser Workflow

```
Wikiquote Dump

↓

Parser

↓

Raw JSON

↓

Normalizer

↓

Validation

↓

JSONL Dataset

↓

Website Build

↓

GitHub Pages
```

---

# Data Validation Workflow

Every commit validates

* schema
* duplicate IDs
* duplicate slugs
* missing authors
* orphan translations
* broken references
* invalid dates
* invalid language codes

---

# GitHub Actions

## validate.yml

Runs

* JSON schema validation
* lint
* tests

---

## normalize.yml

Converts parser output into canonical dataset.

---

## build-search.yml

Creates optimized search indexes.

---

## translate.yml

Processes new untranslated records.

---

## deploy-pages.yml

Builds website.

Deploys GitHub Pages.

---

## statistics.yml

Calculates

* quote counts
* author counts
* translation coverage
* contributor statistics

---

## backup.yml

Creates scheduled snapshots.

---

# Search Index

Generate optimized indexes.

Examples

```
author_index.json

tag_index.json

search_index.json

language_index.json
```

---

# Quality Levels

Each translation receives a quality level.

```
machine

↓

reviewed

↓

verified

↓

expert
```

---

# Stable IDs

Quotes never use sequential IDs.

Instead

```
qt_8abf03d7
```

Advantages

* immutable
* merge-friendly
* synchronization-safe

---

# Licensing

The parser code and the dataset may have different licensing requirements.

The project must preserve attribution and comply with the licensing of upstream sources (such as Wikiquote content and MediaWiki licensing). Contributors should ensure that redistributed content retains the required notices and attribution.

---

# Contribution Workflow

```
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

# Coding Standards

* TypeScript preferred
* Python for ETL scripts
* JSON Schema for validation
* Conventional Commits
* Semantic Versioning
* Automated formatting
* Unit tests for parsers and validators

---

# Roadmap

## Phase 1

* Normalize parser output
* Define schemas
* Create website foundation
* GitHub Pages deployment

---

## Phase 2

* Search
* Author pages
* Quote cards
* Statistics
* Dark mode
* Persian translations

---

## Phase 3

* API
* GraphQL
* Search indexing
* Daily quotes
* AI-assisted translation
* Contributor dashboard

---

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
* Speech-to-text quote extraction from public-domain recordings where legally permitted
* Interactive quote maps
* Historical timelines
* Reading lists
* Educational collections
* Telegram bot
* Discord bot
* Slack integration
* VS Code extension
* Browser extension
* Offline dataset releases
* Monthly data snapshots
* Community translation portal
* Contributor leaderboard

---

# Our Mission

OpenQuotes is not just another quote repository.

It is an attempt to build an open, structured, multilingual knowledge base of humanity's most influential quotations—carefully organized, verifiable where possible, and designed to remain useful for decades.

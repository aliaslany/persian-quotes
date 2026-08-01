#!/usr/bin/env python3
"""
Builds the Persian Quotes dataset from the amnghd/Persian_poems_corpus
(itself scraped from ganjoor.net's public-domain classical poetry archive).

Only poets who died 175+ years ago are included, so every text used here
is unambiguously in the public domain worldwide. Modern 20th-century poets
(Bahar, Farrokhi, Iqbal, Parvin, Rahi, Shahriar, etc.) are intentionally
excluded since their work may still be under copyright in some countries.

Usage:
    python3 build.py --source /path/to/Persian_poems_corpus/original --out ../data --cap 3000
"""
import argparse
import json
import os
import random
import re
import unicodedata

random.seed(42)

# filename -> (id_slug, name_en, name_fa, death_year_ce)
POETS = {
    "roodaki.txt":     ("roodaki",     "Rudaki",            "رودکی",              941),
    "ferdousi.txt":    ("ferdowsi",    "Ferdowsi",          "فردوسی",             1020),
    "onsori.txt":      ("onsori",      "Unsuri",            "عنصری بلخی",         1040),
    "manoochehri.txt": ("manoochehri", "Manuchehri",        "منوچهری دامغانی",    1040),
    "asadi.txt":       ("asadi",       "Asadi Tusi",        "اسدی توسی",          1073),
    "abusaeed.txt":    ("abusaeed",    "Abu Said Abul Kheayr","ابوسعید ابوالخیر", 1049),
    "naserkhosro.txt": ("naserkhosro", "Nasir Khusraw",     "ناصر خسرو",          1088),
    "amir.txt":        ("moezi",       "Amir Muizzi",       "امیرمعزی",           1127),
    "khayyam.txt":     ("khayyam",     "Omar Khayyam",      "عمر خیام",           1131),
    "sanaee.txt":      ("sanaee",      "Sanai",             "سنایی غزنوی",        1131),
    "gilani.txt":      ("gilani",      "Abdul Qadir Gilani","عبدالقادر گیلانی",   1166),
    "khaghani.txt":    ("khaghani",    "Khaqani",           "خاقانی",             1199),
    "zahir.txt":       ("zahir",       "Zahir ad Din Faryabi","ظهیرالدین فاریابی",1201),
    "attar.txt":       ("attar",       "Attar of Nishapur", "عطار نیشابوری",      1221),
    "kamal.txt":       ("kamal",       "Kamal od-Din Esmail","کمال الدین اسماعیل",1237),
    "babaafzal.txt":   ("babaafzal",   "Afdal al-Din Kashani","افضل الدین کاشانی",1266),
    "saadi.txt":       ("saadi",       "Saadi Shirazi",     "سعدی شیرازی",        1292),
    "moulavi.txt":     ("rumi",        "Rumi",              "مولانا",             1273),
    "eraghi.txt":      ("eraghi",      "Fakhr al Din Iraqi","فخرالدین عراقی",     1289),
    "salman.txt":      ("salman",      "Masoud Sad Salman", "مسعود سعد سلمان",    1121),
    "khosro.txt":      ("khosrow",     "Amir Khusrow",      "امیر خسرو",          1325),
    "shabestari.txt":  ("shabestari",  "Mahmoud Shabestari","محمود شبستری",       1320),
    "seyf.txt":         ("seyf",        "Saif Farghani",     "صیف فرغانی",         1348),
    "khajoo.txt":      ("khajoo",      "Khwaju Kermani",    "خواجوی کرمانی",      1352),
    "obeyd.txt":       ("obeyd",       "Ubayd Zakani",      "عبید زاکانی",        1370),
    "hafez.txt":       ("hafez",       "Hafez",             "حافظ شیرازی",        1390),
    "shahnematollah.txt": ("shahnematollah", "Shah Nimatullah Wali", "شاه نعمت‌الله ولی", 1431),
    "jami.txt":        ("jami",        "Jami",              "جامی",               1492),
    "helali.txt":      ("helali",      "Badridin Hilali",   "بدرالدین هلالی",     1529),
    "vahshi.txt":      ("vahshi",      "Vahshi Bafqi",      "وحشی بافقی",         1583),
    "orfi.txt":        ("orfi",        "Orfi Shirazi",      "عرفی شیرازی",        1591),
    "bahaee.txt":      ("bahaee",      "Bahaidin Amili",    "شیخ بهایی",          1621),
    "feyz.txt":        ("feyz",        "Feyz Kashani",      "فیض کاشانی",         1680),
    "saeb.txt":        ("saeb",        "Saib Tabrizi",      "صائب تبریزی",        1676),
    "hatef.txt":       ("hatef",       "Hatef",             "هاتف اصفهانی",       1783),
    "bidel.txt":       ("bidel",       "Abdul Qadir Bedil", "بیدل دهلوی",         1720),
    "nezari.txt":      ("nezari",      "Nizari Quhistani",  "نزاری قهستانی",      1320),
    "anvari.txt":      ("anvari",      "Awhad ad Din Anvari","اوحد الدین انوری",  1189),
}

CATEGORIES = {
    "eshgh":   {"fa": "عشق",     "en": "love",     "kw": ["عشق", "یار", "معشوق", "وصل", "دلبر", "دلدار", "عاشق"]},
    "hekmat":  {"fa": "حکمت",    "en": "wisdom",   "kw": ["خرد", "عقل", "حکمت", "دانش", "دانا", "بخرد"]},
    "zendegi": {"fa": "زندگی",   "en": "life",     "kw": ["زندگ", "عمر", "روزگار", "جهان", "دنیا", "زمانه"]},
    "erfan":   {"fa": "عرفان",   "en": "mysticism","kw": ["صوفی", "عارف", "می", "ساقی", "میخانه", "رند", "پیر مغان"]},
    "marg":    {"fa": "مرگ و هستی", "en": "mortality","kw": ["مرگ", "خاک", "گور", "فنا", "نیستی"]},
    "tabiat":  {"fa": "طبیعت",   "en": "nature",   "kw": ["گل", "بلبل", "باغ", "بهار", "باد", "سرو", "چمن"]},
}

def categorize(text: str) -> str:
    best, best_score = "hekmat", 0
    for cat_id, cat in CATEGORIES.items():
        score = sum(text.count(kw) for kw in cat["kw"])
        if score > best_score:
            best, best_score = cat_id, score
    return best if best_score > 0 else "hekmat"

def normalize(line: str) -> str:
    line = unicodedata.normalize("NFC", line).strip()
    line = re.sub(r"\s+", " ", line)
    line = line.replace("ي", "ی").replace("ك", "ک")
    return line

def read_beyts(path: str):
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = [normalize(l) for l in f.readlines()]
    lines = lines[2:]
    lines = [l for l in lines if l]
    beyts = []
    for i in range(0, len(lines) - 1, 2):
        m1, m2 = lines[i], lines[i + 1]
        if 8 <= len(m1) <= 90 and 8 <= len(m2) <= 90:
            beyts.append(f"{m1}\n{m2}")
    return beyts

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--cap", type=int, default=3000)
    args = ap.parse_args()

    os.makedirs(f"{args.out}/all", exist_ok=True)
    os.makedirs(f"{args.out}/quotes", exist_ok=True)

    all_quotes = []
    per_category = {c: [] for c in CATEGORIES}
    qid = 1

    for fname, (slug, name_en, name_fa, death) in POETS.items():
        fpath = os.path.join(args.source, fname)
        if not os.path.exists(fpath):
            print(f"skip missing: {fname}")
            continue
        beyts = read_beyts(fpath)
        beyts = list(dict.fromkeys(beyts))
        if len(beyts) > args.cap:
            beyts = random.sample(beyts, args.cap)

        poet_quotes = []
        for text in beyts:
            cat = categorize(text)
            entry = {
                "id": qid,
                "text": text,
                "author": name_fa,
                "author_en": name_en,
                "category": cat,
                "category_fa": CATEGORIES[cat]["fa"],
            }
            qid += 1
            poet_quotes.append(entry)
            all_quotes.append(entry)
            per_category[cat].append(entry)

        with open(f"{args.out}/all/{slug}.json", "w", encoding="utf-8") as f:
            json.dump(poet_quotes, f, ensure_ascii=False, indent=2)
        print(f"{slug:15s} ({name_en:20s}) -> {len(poet_quotes)} quotes")

    with open(f"{args.out}/quotes.json", "w", encoding="utf-8") as f:
        json.dump(all_quotes, f, ensure_ascii=False, indent=2)

    for cat_id, items in per_category.items():
        with open(f"{args.out}/quotes/{cat_id}.json", "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=2)

    poets_meta = [
        {"slug": s, "name_en": e, "name_fa": f, "died": d, "file": f"data/all/{s}.json"}
        for s, e, f, d in POETS.values()
    ]
    with open(f"{args.out}/poets.json", "w", encoding="utf-8") as f:
        json.dump(poets_meta, f, ensure_ascii=False, indent=2)

    print(f"\nTOTAL: {len(all_quotes)} quotes across {len(POETS)} poets")
    print("By category:")
    for cat_id, items in per_category.items():
        print(f"  {cat_id:10s} ({CATEGORIES[cat_id]['en']:10s}): {len(items)}")

if __name__ == "__main__":
    main()

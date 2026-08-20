# گنجینهٔ سخن فارسی

> مجموعه‌ای ساخت‌یافته و قابل استفادهٔ برنامه‌نویسی از اشعار و سخنان شاعران کلاسیک فارسی.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/website-GitHub%20Pages-brightgreen)](https://aliaslany.github.io/persian-quotes/)

## 🌐 وب‌سایت

**[مشاهدهٔ گنجینهٔ سخن](https://aliaslany.github.io/persian-quotes/)**

وب‌سایت پروژه یک رابط فارسی و راست‌به‌چپ دارد و می‌تواند از میان داده‌های موجود، سخن یا شعر تصادفی نمایش دهد و شاعران را مرور کند.

## 📚 دربارهٔ پروژه

این مخزن داده‌های شعر و سخن فارسی را در قالب‌های ساده و قابل استفاده برای پروژه‌های نرم‌افزاری نگهداری می‌کند. داده‌ها برای استفاده در اپلیکیشن‌ها، پژوهش، آموزش، ربات‌ها و پروژه‌های پردازش متن مناسب هستند.

در حال حاضر داده‌ها شامل آثار **۳۸ شاعر** هستند؛ از جمله:

- رودکی
- فردوسی
- خیام
- عطار
- سعدی
- مولانا
- حافظ
- جامی
- صائب تبریزی
- بیدل دهلوی
- و شاعران کلاسیک دیگر

فهرست کامل شاعران در [`data/poets.json`](data/poets.json) قرار دارد.

## 🗂 ساختار داده

```text
persian-quotes/
├── data/
│   ├── all/          # داده‌های هر شاعر
│   ├── quotes/       # داده‌های دسته‌بندی‌شده
│   ├── poets.json    # فهرست شاعران و اطلاعات پایه
│   └── quotes.json   # مجموعهٔ کامل نقل‌قول‌ها
├── src/
│   └── index.js      # API سادهٔ JavaScript برای دسترسی به داده‌ها
├── scripts/          # ابزارهای پردازش داده
├── website/          # وب‌سایت GitHub Pages
├── .github/
│   └── workflows/    # استقرار خودکار وب‌سایت
├── README.md
└── README.fa.md
```

## 🚀 استفاده در JavaScript

این پروژه یک کلاینت ساده برای دریافت داده‌ها دارد:

```js
import {
  getRandomQuote,
  getRandomQuoteByCategory,
  getRandomQuoteByPoet,
  getPoets
} from './src/index.js';

const quote = await getRandomQuote('aliaslany');
console.log(quote.text);
```

برای دریافت سخن از یک شاعر:

```js
const quote = await getRandomQuoteByPoet('aliaslany', 'hafez');
```

و برای دریافت فهرست شاعران:

```js
const poets = await getPoets('aliaslany');
```

کلاینت فعلی داده‌ها را مستقیماً از CDN دریافت می‌کند و به backend نیاز ندارد.

## 🏷 دسته‌بندی‌ها

داده‌های فعلی از دسته‌هایی مانند این‌ها استفاده می‌کنند:

- عشق
- زندگی
- حکمت
- عرفان
- مرگ و هستی
- طبیعت

## 🖥 وب‌سایت و GitHub Pages

وب‌سایت در پوشهٔ `website/` قرار دارد و workflow موجود در `.github/workflows/deploy-pages.yml` آن را با GitHub Pages منتشر می‌کند.

پس از فعال‌سازی **Settings → Pages → Source: GitHub Actions** در تنظیمات مخزن، هر push به `main` باعث اجرای استقرار می‌شود.

## 🤝 مشارکت

برای مشارکت:

1. مخزن را Fork کنید.
2. یک branch برای تغییر خود بسازید.
3. داده یا کد را اضافه یا اصلاح کنید.
4. تغییرات را بررسی و تست کنید.
5. یک Pull Request ایجاد کنید.

## ⚖️ مجوز و منابع

کد و داده‌های این پروژه ممکن است شرایط مجوز متفاوتی داشته باشند. هنگام بازتوزیع داده‌ها، شرایط مجوز و attribution منبع اصلی، از جمله Wikiquote و منابع وابسته، باید رعایت شود.

## 🎯 هدف آینده

هدف پروژه تبدیل شدن به یک مجموعهٔ فارسی ساخت‌یافته، قابل جست‌وجو و قابل استفاده برای توسعه‌دهندگان و پژوهشگران است؛ با امکاناتی مانند جست‌وجوی سریع، صفحات شاعران، API عمومی، ترجمه، اعتبارسنجی منابع و نسخه‌های دادهٔ منظم.

---

**نسخهٔ فارسی README** | [English README](README.md) | [وب‌سایت](https://aliaslany.github.io/persian-quotes/)

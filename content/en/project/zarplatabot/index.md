---
title: "ZarplataBot — Telegram Bot for Shift, Bar, and Report Management"
date: 2025-06-09
author: "Hovik"
description: "A multifunctional Telegram bot that automates shift tracking, income and expense accounting, and generates reports. Built with Python, Airtable, and deployed on Railway."
tags: ["Telegram Bot", "Python", "Airtable", "Automation", "Fintech", "Railway", "Backend"]
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com)'
---

## 🔍 About the Project

**ZarplataBot** is a Telegram bot designed to automate financial tracking in small teams such as baristas, shift workers, support staff, and administrators. It replaces manual spreadsheet entries and helps track:

- 💼 Work shifts (day and night)  
- 🍷 Bar income with dynamic percentages  
- 💸 Expenses with comments  
- 🚫 Fines and deductions  
- 📊 Monthly reports with filtering  

The project was developed as a personal internal automation solution but can scale to any team.

---

## 💡 Why I created this?

Working in a team where tracking was often done manually, I noticed:  

- Shift records were forgotten  
- Expenses got lost  
- Income was estimated roughly  
- Reports had to be collected piecemeal  

To remove routine and errors, I decided to automate the process via Telegram, which everyone uses daily.

---

## 🔧 Features

- 🕑 Adding shifts: day or night (with fixed rates)  
- 🍷 Bar accounting: income percentage depends on the amount (dynamic)  
  - up to 3500 — 5%  
  - 3500 to 4000 — 6%  
  - 4000 to 4500 — 7%  
  - …  
  - from 10,000 — 15%  
- 💸 Entering expenses with comments (e.g., "300 food")  
- 🚫 Fines with explanations ("500 late")  
- 📊 Monthly reports — current, previous, and manually selected  
- 🗃 All data stored in Airtable — easy manual editing  
- ⏱ Instant response — via Telegram bot, no need to open spreadsheets  

---

## 🔌 Integrations

- **Telegram Bot API** — user communication  
- **Airtable API** — database editable manually if needed  
- **SQLite** — local storage fallback  
- **Railway** — deployment and 24/7 uptime  
- **GitHub** — project storage and updates  

---

## 🚀 Deployment

The bot is deployed on [Railway](https://railway.app), allowing 24/7 operation without relying on local machines. Code updates are done by `git push` to GitHub, and Railway automatically rebuilds and restarts the bot.

---

## 🖼 Interface

Users interact with the bot via buttons:  

- ▶️ Start  
- 🕑 Day / 🌙 Night shift  
- 🍷 Bar  
- 💸 Expense  
- 🚫 Fine  
- 📊 Report  

Each action is accompanied by confirmations and interactive messages. The interface is adapted to Telegram UX.

---

## 🛠 Technologies Used

| Area           | Technologies                      |
|----------------|---------------------------------|
| Language       | Python 3.11                     |
| Framework      | Aiogram 3                      |
| APIs           | Telegram Bot API, Airtable REST |
| Hosting        | Railway                        |
| Storage        | SQLite + Airtable              |
| CI/CD          | GitHub + Railway Integration    |

---

## 📦 Project Repository

Code available on GitHub:  

👉 [github.com/adjabkhanian/zarplata-bot](https://github.com/adjabkhanian/zarplata-bot)

---

## 📈 Future Plans

- User authorization  
- Google Sheets integration  
- PDF reports  
- Analytics with charts  
- Admin panel via web interface  

---

## 💬 Conclusion

ZarplataBot is not just a bot but a working tool for accounting and transparency. It removes chaos and makes routine pleasant.

If you want to adapt this bot for your team — contact me 😉
---
title: "RealtyHelpReBot — Telegram Bot for Real Estate Assistance"
date: 2025-10-10
author: "Hovik"
description: "A Telegram bot that helps clients select real estate by city and type, while sending ready applications to the manager. Built with Python (Aiogram) and integrated with Google Sheets."
tags: ["Telegram Bot", "Python", "Google Sheets", "Automation", "Real Estate", "Backend"]
---

## 🏙 About the Project

**RealtyHelpReBot** is a Telegram bot designed to automate real estate selection and handle client applications.  
It allows users to choose a city, property type, receive up-to-date offers, and submit applications directly to the manager.

---

## 💡 Project Idea

Instead of long phone calls and manual forms, the bot simplifies the process:  
clients select their preferences, and the bot automatically generates and sends the application to Google Sheets, where the manager can immediately view it.  

The project was developed on a client request for a real estate agency to reduce routine work and speed up client interactions.

---

## 🔧 Core Features

- 🏘 Select city and property type  
- 📩 Submit application to Google Sheets  
- 🧠 Smart welcome message — admins can change text and photo via JSON  
- 👨‍💼 Notify manager about new applications  
- ⚙️ Flexible welcome message configuration without changing code

---

## ⚙️ Technologies Used

| Area            | Technologies                         |
|-----------------|--------------------------------------|
| Programming     | Python 3.9                           |
| Framework       | Aiogram 3                             |
| Database/API    | Google Sheets API (via gspread)      |
| Hosting         | Local server / Railway                |
| Configuration   | JSON + dotenv                         |

---

## 📁 Project Structure

```
realtyhelprebot/
│
├── main.py            # Main bot logic
├── config.py          # Settings and tokens
├── data/start_data.json  # Dynamic welcome message (text + photo)
├── utils/
│   └── google_api.py  # Google Sheets integration
└── requirements.txt   # Dependencies
```

---

## 🔗 Bot Link

👉 [@AN_MowKznRussia_bot](https://t.me/AN_MowKznRussia_bot)

---

## 🧩 Code Preview

The main bot logic can be found here:  
**[`main.py`](main.py)** — contains the implementation of all bot scenarios, including dynamic welcome messages, form processing, and Google Sheets integration.

---

## 💬 Conclusion

**RealtyHelpReBot** is a practical tool for real estate agencies.  
It saves managers time and makes client communication smooth and modern.

The bot can be easily adapted for other niches — from rentals to consultations.  
If you want a similar project for your business, just contact me 😉
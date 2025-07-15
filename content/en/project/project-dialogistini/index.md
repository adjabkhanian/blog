---
title: "Telegram Bot “Dialog of Truth”"
date: 2025-07-15
author: "Hovik"
description: "A bot for collecting contacts, religious surveys, and admin broadcasts, integrated with Airtable."
tags: ["TELEGRAM BOT", "Education", "Python", "Airtable", "Automation"]
image:
  caption: 'AI-generated preview'
  focal_point: "center"
---

### 🧠 Project Idea

This Telegram bot was developed for the spiritual and educational initiative “Dialog of Truth” to:

- Automate contact collection from Instagram users  
- Understand participant motivation through a short survey  
- Enable admins to broadcast messages to the entire database  
- Seamlessly integrate with Airtable

---

### 🔍 What Does the Bot Do?

1. A user joins the bot via a link from Instagram  
2. They are asked to provide:
   - 📱 Phone number (via a button)
   - 📧 Email address
   - 👤 First and last name
   - ❓ Answer to: “Do you want religious knowledge?”
3. The bot saves all the data to Airtable  
4. Sends a link to the main Telegram channel  
5. The admin can send a broadcast with the `/sendall` command

---

### 📊 Survey Inside the Bot

> **Do you want religious knowledge?**  
> • To receive and apply it for myself  
> • To receive, apply, and share it with others  
> • I just want to observe for now

All responses are also saved in Airtable.

---

### 🛠 Technologies Used

- **Python 3.11**
- **Aiogram 3.x** — asynchronous Telegram bot framework  
- **Airtable** — external database for storing structured user data  
- **Railway** — deployment without exposing tokens (via ENV)  
- **GitHub** — source code is private, available upon request

---

### 🖼 Project Cover

![Project Cover](https://raw.githubusercontent.com/adjabkhanian/dialogistini2/main/dialogistini-preview.jpg)

---

### 📂 Airtable Data Structure

- Telegram ID  
- Username  
- Phone  
- Email  
- First Name  
- Last Name  
- Survey Answer  
- Registration Date

---

### 📦 Admin Features

- ✅ `/sendall Hello!` — sends a message to all users  
- 🔐 Only specified Telegram IDs can broadcast  
- 🧑‍💻 All collected data is stored in Airtable and can be exported easily

---

### 💡 Who Is This For?

- Online schools and educational communities  
- Projects growing from Instagram or Telegram  
- Small teams without complex CRM systems

---

### 📥 How to Deploy

1. Create an Airtable base with the required fields  
2. Add secret variables in Railway:
   - `BOT_TOKEN`  
   - `AIRTABLE_API_KEY`  
   - `AIRTABLE_BASE_ID`  
   - `AIRTABLE_TABLE_NAME`  
3. Deploy the bot on Railway  
4. Connect a domain and share the link in your Instagram bio

---

### 🎯 Results

- A clean Telegram-based form that acts as a mini landing page  
- All user data in Airtable for future communication and analysis  
- Quick survey for audience segmentation

---

### 📎 Want to Collaborate?

If you want to create a custom Telegram bot for your project —  
[Contact me →](https://t.me/adjabkhanyan)

---

### 🛠 Additional Resources

- [Aiogram Documentation](https://docs.aiogram.dev/en/latest/)  
- [Airtable API Reference](https://airtable.com/api)  
- [Railway Hosting](https://railway.app)
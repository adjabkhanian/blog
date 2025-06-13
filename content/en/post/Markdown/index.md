---

title: "📘 What is Markdown and Why Use It?"
summary: "In the third lab on computer architecture, we got familiar with a lightweight and convenient markup language — **Markdown**. Its goal is to simplify formatting reports and documentation without the complexity of Word or LaTeX."
date: 2025-03-23
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com)'
authors:
  -Admin
tags:
  - markdown
  - report
  - pandoc

---

In the third lab on computer architecture, we got familiar with a lightweight and convenient markup language — **Markdown**. Its goal is to simplify formatting reports and documentation without the complexity of Word or LaTeX.

---

## 🛠 What I Learned

**Markdown allows you to:**

- Create headings using `#`, `##`, `###`, and so on  
- Format text: `**bold**`, `*italic*`, `***bold italic***`
- Make lists:
  - Bulleted
  - And numbered:
    1. First item  
    2. Second item
- Add **links**:  
  `[link example](https://example.com)`
- Insert **images**:
  `![caption](/path/to/image.jpg "tooltip")`
- Write **formulas** (like in LaTeX):  
  `$\sin^2(x) + \cos^2(x) = 1$`
- Add **code blocks**:
  ```bash
  git pull
  make
  ```

---

## ⚙️ How We Used Markdown in Practice

During the lab, I:

1. Navigated to the target directory in the terminal:
   ```bash
   cd ~/work/study/2023-2024/"Computer Architecture"/labs/lab03/report
   ```

2. Pulled the latest changes from the remote repository:
   ```bash
   git pull
   ```

3. Compiled the report template using `make`, which generated `.pdf` and `.docx` files:
   ```bash
   make
   ```

4. Filled out the report in Markdown format (`report.md`) and recompiled it:
   ```bash
   make clean
   make
   ```

5. Uploaded the result to GitHub:
   ```bash
   git add .
   git commit -m "feat: add lab3 report in Markdown"
   git push
   ```

---

## 📸 Along the Way...

- I added **screenshots** to the report  
- Included **links** to documentation  
- Wrote **formulas** and formatted them nicely  
- Used **code blocks** to show commands  

Markdown makes all of this simple, readable, and clean.

---

## 🧠 What I Got From It

- I learned how **Markdown** makes documentation easier.
- I found it works great with **Git** and **Pandoc**.
- With **Makefile**, I can automate report generation — saves tons of time.
- I improved my skills with the **terminal** and **Git** — essential tools for any developer.

---

## 📚 Tip for Students

> Everyone writing reports, articles, or blogs should learn Markdown.

It’s a fast, simple, and universal way to format text that works **everywhere**:  
from GitHub and Notion to Tilda and Hugo.

---

🧑‍💻 *Lab work completed by Hovik, first-year programming student*
```
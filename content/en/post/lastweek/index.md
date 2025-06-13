---
title: "Weekly Report: Version Control (Git)"
summary: "Introduction:
This week, I actively studied **Git version control system**. In this post, I will discuss Git setup, working with repositories, and essential commands, along with presenting my lab report."
date: 2025-03-19
authors:
  - admin
tags:
  - Git
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com)'
---


## Introduction

This week, I actively studied **Git version control system**. In this post, I will discuss Git setup, working with repositories, and essential commands, along with presenting my lab report.

---

## 📌 Git Basics

Git is a **distributed version control system** (VCS) that allows tracking file changes, managing different project versions, and collaborating on software development.

🔹 **Key Terms:**
- **Repository** — a project storage with a change history.
- **Commit** — a saved state of files with a description of changes.
- **Branch** — an isolated code version for working on new functionality.
- **Merge** — integrating changes from different branches.
- **Remote Repository** — a repository on a server (e.g., [GitHub](https://github.com/)).

## ⚙️ Git Setup

### 🔑 Generating SSH Key

To work with remote repositories without entering a password, create an **SSH key**:

```sh
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Add the key to the SSH agent:

```sh
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```

Copy the key and add it to GitHub:

```sh
cat ~/.ssh/id_rsa.pub
```

📌 **Add key to GitHub:** [Go to SSH key settings](https://github.com/settings/keys)

---

### 🛠️ Basic Git Configuration

Set up name and email:

```sh
git config --global user.name "Hovik Adjabkhanyan"
git config --global user.email "your_email@example.com"
```

Enable convenient encoding for Russian language support:

```sh
git config --global core.quotepath false
```

---

## 📂 Working with Repositories

### 🏗️ Creating a New Repository

Create a local repository and link it to GitHub:

```sh
mkdir my_project && cd my_project
git init
git remote add origin git@github.com:username/my_project.git
```

Add files and make the first commit:

```sh
echo "# My Project" > README.md
git add .
git commit -m "Initial commit"
git push -u origin main
```

📌 **GitHub Repository:** [Open Project](https://github.com/username/my_project)

---

### 🔄 Cloning an Existing Repository

```sh
git clone git@github.com:username/my_project.git
```

---

### 🌿 Working with Branches

Create a new branch:

```sh
git checkout -b feature-branch
```

Merge a branch:

```sh
git checkout main
git merge feature-branch
```

Delete a branch:

```sh
git branch -d feature-branch
```

---

## 📜 Lab Report

### 🔹 Course Directory Setup

📸 **Creating Project Structure:**

```sh
mkdir -p ~/work/study/2023-2024/Computer_Architecture
cd ~/work/study/2023-2024/Computer_Architecture
git clone --recursive git@github.com:username/study_2023-2024_arch-pc.git archpc
```

🖼️ **Created Structure:**

![Workspace Setup](images/workspace.png)

### 🔹 Independent Work Assignment

Add files to the repository:

```sh
git add .
git commit -m "feat: added lab report"
git push origin main
```

📌 **View Repository:** [GitHub Repository](https://github.com/username/study_2023-2024_arch-pc)

---

## 🎯 Conclusion

During the lab work, I:
✅ Set up Git and GitHub
✅ Created an SSH key for secure connection
✅ Organized the repository and learned essential commands

---

## 🔗 Useful Links

📖 [Official Git Documentation](https://git-scm.com/doc)
📚 [GitHub Docs](https://docs.github.com/en)

---

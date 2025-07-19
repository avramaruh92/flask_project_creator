# 📚 Flask Project Creator – Module Guide

This documentation explains how the four Python modules work together.

---

## 🧩 1. `create_project.py`

- CLI launcher
- Parses target path
- Calls `setup_project(path)`

---

## 📁 2. `structure.py`

- Defines:
  - `folders`: All directories to generate
  - `files`: Key file templates (HTML, SCSS, JS, config)

> You can customize the generated structure here.

---

## 🧰 3. `utils.py`

Reusable helpers:
- `run_command()` — Run shell commands safely
- `safe_write()` — Only create file if it doesn’t exist
- `check_tool_installed()` — Ensure tools like `python` and `npm` are available

---

## ⚙ 4. `setup.py`

Handles the full setup:
- Creates folders
- Writes files
- Initializes Python venv
- Installs pip packages
- Sets up npm, installs Sass/Prettier/ESLint
- Modifies `package.json` to include `sass` watch script

---

## 🛠 Customize & Extend

You can:
- Add auth templates to `structure.py`
- Write more helpers in `utils.py`
- Expand `setup.py` to support Docker or testing

---

## 🧠 Tip

Use this script as a template for:
- Flask + API backends
- Full-stack starter kits
- Teaching and workshops
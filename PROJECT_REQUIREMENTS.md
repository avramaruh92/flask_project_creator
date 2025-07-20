Here is your complete and **paste-ready `PROJECT_REQUIREMENTS.md`** file:

---

````markdown
# 📦 Project Requirements

This document outlines the required tools, dependencies, and environment setup for running a Flask project generated using the custom project generator script.

---

## ✅ System Requirements

| Tool | Version | Purpose |
|------|---------|---------|
| **Python** | 3.8+ | Backend web server |
| **Node.js** | 16+ recommended | For Sass compilation |
| **npm** | Bundled with Node.js | Package manager for frontend |
| **Git** | Optional | Version control |
| **VS Code** | Recommended | IDE with automation support |

---

## 🐍 Python Requirements

All Python dependencies are installed into a virtual environment.

### Required Python Packages

| Package | Purpose |
|---------|---------|
| `flask` | Web framework |
| `python-dotenv` | Load config from `.env` file |

### Optional / Recommended Packages

You can extend functionality with:

| Package | Purpose |
|---------|---------|
| `flask-wtf` | Form handling |
| `flask-login` | User authentication |
| `flask-sqlalchemy` | ORM |
| `flask-migrate` | DB migrations |
| `flask-cors` | Cross-origin resource sharing |
| `flask-restful` | REST API endpoints |

---

## 🌐 Frontend Requirements

### npm Packages

These are installed automatically during project generation.

| Package | Usage |
|---------|-------|
| `sass` | Compile SCSS to CSS |

**Install manually (if needed):**

```bash
npm install sass --save-dev
````

---

## 🧰 VS Code Extensions (Optional but Recommended)

| Extension | Description                    |
| --------- | ------------------------------ |
| Python    | Language support and debugging |
| Prettier  | Code formatting                |
| ESLint    | JavaScript linting             |
| DotENV    | Syntax highlighting for `.env` |
| Sass      | SCSS highlighting & validation |

---

## ⚙️ Configuration Files

Make sure the following files are present:

| File                 | Description                        |
| -------------------- | ---------------------------------- |
| `.env`               | Flask runtime config               |
| `requirements.txt`   | Python dependency lock             |
| `package.json`       | npm scripts and Sass dependency    |
| `.vscode/tasks.json` | VS Code task runner (Flask + Sass) |

---

## ✅ Post-Setup Checklist

After generating your project:

```bash
# Activate the virtual environment
venv\Scripts\activate

# Install frontend dependencies
npm install

# Optional: run Sass and Flask server
npm run sass
flask run
```

Ensure the generated `main.css` exists and your home page loads correctly.

---

## 📌 Notes

* `.env` is **not committed** to Git (should be in `.gitignore`)
* Make sure your system PATH includes Python and Node binaries
* Sass must be installed in the project directory to use `npm run sass`

---
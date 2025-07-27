# 🧪 Flask Project Generator

This is a plug-and-play **Flask project generator** that scaffolds a full-featured web app with:

- ✅ Blueprint-based Flask structure  
- ✅ Modular SCSS (Sass) setup  
- ✅ Auto-generated folder hierarchy  
- ✅ Jinja2 templates  
- ✅ `.env` config file support  
- ✅ VS Code task automation  
- ✅ Ready-to-run home page and static asset setup  

---

## 🚀 How to Generate a Project

From your terminal:

```bash
python "Your_full_script_path(inside quotation marks)" "The_path_you_want_your_project_to_be_created(inside quotation marks)"
````

Then:

```bash
cd G:\Projects\MyFlaskApp
venv\Scripts\activate
npm install
npm run sass
flask run
```

Or use VS Code’s Task Runner:

```
Ctrl + Shift + B → select “Run Flask App” or “Watch SCSS”
```

---

## 📁 What Gets Generated

```
MyFlaskApp/
├── app/
│   ├── __init__.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── models/
│   │   └── __init__.py
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   └── static/
│       ├── css/
│       │   └── main.css
│       └── js/
│           └── main.js
├── scss/
│   ├── main.scss
│   ├── abstracts/_variables.scss
│   └── base/_base.scss
├── .env
├── run.py
├── package.json
└── .vscode/tasks.json
```

---

## 📦 Requirements

### ✅ Runtime Tools

* Python 3.8+
* Node.js (16+ recommended)
* npm
* VS Code (recommended)
* Git (optional)

### ✅ Python Packages

Installed in the virtual environment:

* `flask`
* `python-dotenv`

*Optional extensions you can add:*

* `flask-wtf` – Form handling
* `flask-sqlalchemy` – ORM
* `flask-migrate` – DB migrations
* `flask-login` – Authentication

### ✅ npm Packages

Installed in the generated project:

```bash
npm install sass --save-dev
```

---

## 🧠 Project Structure

| Folder     | Description                                        |
| ---------- | -------------------------------------------------- |
| `app/`     | Main application logic (routes, templates, models) |
| `scss/`    | Modular SCSS files compiled to CSS                 |
| `static/`  | JS and compiled CSS                                |
| `.env`     | Flask environment + secrets                        |
| `.vscode/` | VS Code automation tasks                           |

---

## 🛠️ Development Tips

* Edit `scss/main.scss` to import new style modules
* Use Jinja2 inside `templates/`
* Add view logic in `routes/main.py`
* Reference static assets via `url_for('static', filename='...')`

---

## 🔁 VS Code Automation

Tasks are pre-configured in `.vscode/tasks.json`.

To launch Flask + SCSS compilation:

```bash
Ctrl + Shift + B
```

Choose:

* ✅ Run Flask App
* ✅ Watch SCSS

They can run in parallel from the terminal or VS Code.

---

## 🧪 Test Your Setup

```bash
cd G:\Projects\MyFlaskApp
venv\Scripts\activate
npm run sass
flask run --debug
```

Visit:
`http://localhost:5000`

You should see:

* ✔️ Homepage rendered
* ✔️ CSS loaded
* ✔️ Working routing and layout

---

## 🧱 How to Extend

* Add Blueprints (e.g. `auth`, `admin`, `api`)
* Add SCSS modules inside `scss/` and import in `main.scss`
* Add Jinja templates in `app/templates`
* Add models in `models/` and connect SQLAlchemy

---




from utils import load_template

folders = [
    "app/routes",
    "app/models",
    "app/templates",
    "app/static/css",
    "app/static/js",
    "scss/abstracts",
    "scss/base",
    ".vscode"
]

files = {
    # Environment variables
    ".env": """FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
OPENAI_API_KEY=
""",

    # App entry point
    "run.py": """from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
""",

    # App factory
    "app/__init__.py": """from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "your-secret-key"

    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
""",

    # ROUTES
    "app/routes/__init__.py": "# This file makes 'routes' a package\n",
    "app/routes/main.py": """from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')
""",

    # MODELS
    "app/models/__init__.py": "# This file makes 'models' a package\n",

    # HTML templates
    "app/templates/base.html": load_template("base.html"),
    "app/templates/index.html": load_template("index.html"),

    # JavaScript
    "app/static/js/main.js": load_template("main.js"),

    # SCSS partials + entry point
    "scss/abstracts/_variables.scss": load_template("_variables.scss"),
    "scss/base/_base.scss": load_template("_base.scss"),
    "scss/main.scss": "@use 'abstracts/variables';\n@use 'base/base';",

    # Placeholder CSS file to prevent 404 before Sass compiles
    "app/static/css/main.css": "/* Compiled CSS will be written here by Sass */",

    # VS Code task automation
    ".vscode/tasks.json": """{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run Flask App",
      "type": "shell",
      "command": "venv\\\\Scripts\\\\python",
      "args": ["-m", "flask", "run", "--reload"],
      "options": {
        "env": {
          "FLASK_APP": "run.py",
          "FLASK_ENV": "development"
        }
      },
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "problemMatcher": []
    },
    {
      "label": "Watch SCSS",
      "type": "npm",
      "script": "sass",
      "isBackground": true,
      "group": "build"
    }
  ]
}"""
}

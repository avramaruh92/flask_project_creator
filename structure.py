folders = [
    "app/routes", "app/models", "app/utils", "app/templates/auth",
    "app/static/css", "app/static/js", "scss/abstracts", "scss/base",
    "migrations", ".vscode"
]

files = {
    "app/templates/base.html": r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{% block title %}Flask App{% endblock %}</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
</head>
<body>

  {% block content %}
  <h1>Hello, world!</h1>
  {% endblock %}

  <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
""",
    "app/static/js/main.js": "console.log('JS loaded');",
    "scss/main.scss": "@use 'abstracts/variables';",
    ".eslintrc.json": """{
  "env": { "browser": true, "es2021": true },
  "extends": "eslint:recommended",
  "parserOptions": { "ecmaVersion": "latest", "sourceType": "module" },
  "rules": {}
}""",
    ".prettierrc": '{ "semi": true, "singleQuote": true }'
}

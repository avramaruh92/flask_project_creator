import shutil
import os
import json
from pathlib import Path
from structure import folders, files
from utils import run_command, safe_write, check_tool_installed

def setup_project(path):
    base_path = Path(path).resolve()
    is_windows = os.name == "nt"

    print(f"\n📁 Setting up project at: {base_path}")

    # Tool checks
    check_tool_installed("python")
    check_tool_installed("npm")

    # Handle existing directory
    if base_path.exists():
        print(f"⚠️ Directory already exists: {base_path}")
        if input("Overwrite it? [y/N]: ").lower() != 'y':
            print("Aborted.")
            return
        if input("Type 'YES' to confirm: ") != "YES":
            print("❌ Confirmation failed.")
            return
        shutil.rmtree(base_path)

    # Create folders
    for folder in folders:
        (base_path / folder).mkdir(parents=True, exist_ok=True)

    # Create files
    for path, content in files.items():
        safe_write(base_path / path, content)

    # Create virtual environment
    print("🐍 Creating virtual environment...")
    run_command("python -m venv venv", cwd=base_path)

    pip = base_path / "venv" / ("Scripts" if is_windows else "bin") / "pip"
    run_command(f"{pip} install Flask Flask-WTF Flask-SQLAlchemy Flask-Migrate Flask-Login python-dotenv libsass", cwd=base_path)
    run_command(f"{pip} freeze > requirements.txt", cwd=base_path)

    # JS/SCSS tools
    print("📦 Setting up npm and tools...")
    run_command("npm init -y", cwd=base_path)
    run_command("npm install sass eslint prettier --save-dev", cwd=base_path)

    package_path = base_path / "package.json"
    pkg = json.loads(package_path.read_text())
    pkg.setdefault("scripts", {})["sass"] = "sass --watch scss:app/static/css"
    package_path.write_text(json.dumps(pkg, indent=2))

    print(f"\n✅ Project created successfully at: {base_path}")
    print("👉 Next steps:")
    print(f"  cd {base_path}")
    print("  venv\\Scripts\\activate  # or source venv/bin/activate")
    print("  npm run sass")
    print("  flask run")

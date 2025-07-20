import subprocess
import sys
import shutil
from pathlib import Path

def load_template(filename, subdir="template_files"):
    """Load external template content from a file relative to the script location"""
    return (Path(__file__).parent / subdir / filename).read_text(encoding="utf-8")

def run_command(command, cwd=None):
    print(f"> {command}")
    result = subprocess.run(command, shell=True, cwd=cwd)
    if result.returncode != 0:
        print(f"❌ Failed: {command}")
        sys.exit(1)

def safe_write(filepath, content):
    if not filepath.exists():
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(content.strip(), encoding='utf-8')
    else:
        print(f"⚠️ Skipped (exists): {filepath}")

def check_tool_installed(tool):
    if shutil.which(tool) is None:
        print(f"❌ Required tool '{tool}' is not installed.")
        sys.exit(1)

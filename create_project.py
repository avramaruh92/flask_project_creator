import argparse
from setup import setup_project

parser = argparse.ArgumentParser(description="Generate a new Flask + SCSS + JS project")
parser.add_argument("path", nargs="?", default="myapp", help="Target project folder name")
args = parser.parse_args()

setup_project(args.path)

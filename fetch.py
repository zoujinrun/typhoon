# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///

"""
Fetch the Wikipedia page for a Pacific typhoon season and save it raw to data/.
"""

from pathlib import Path
import sys
import requests

HERE = Path(__file__).parent
DATA = HERE / "data"
DATA.mkdir(exist_ok=True)

# 默认抓取 2025 年
YEAR = 2025
URL = f"https://en.wikipedia.org/wiki/{YEAR}_Pacific_typhoon_season"
TARGET = DATA / f"typhoons-{YEAR}.html"

def main():
    if TARGET.exists():
        print(f"Raw data already exists at {TARGET.relative_to(HERE)}, skipping fetch.")
        return

    print(f"Fetching from {URL}...")
    headers = {"User-Agent": "StudentDataVisualisationProject/1.0 (educational use)"}
    
    try:
        response = requests.get(URL, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)

    TARGET.write_text(response.text, encoding="utf-8")
    print(f"Wrote {TARGET.relative_to(HERE)} ({len(response.text)} bytes)")

if __name__ == "__main__":
    main()
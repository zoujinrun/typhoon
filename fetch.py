# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "beautifulsoup4"]
# ///

"""
Fetch the Wikipedia page for the Pacific typhoon season and save it raw to data/.
"""

from pathlib import Path
import requests

HERE = Path(__file__).parent
DATA = HERE / "data"
DATA.mkdir(exist_ok=True)

# 维基百科太平洋台风季页面网址
URL = "https://en.wikipedia.org/wiki/2025_Pacific_typhoon_season"
TARGET = DATA / "typhoons-2025.html"

def main():
    if TARGET.exists():
        print(f"Raw data already exists at {TARGET.relative_to(HERE)}, skipping fetch.")
        return

    print(f"Fetching from {URL}...")
    headers = {"User-Agent": "StudentDataVisualisationProject/1.0 (educational use)"}
    response = requests.get(URL, headers=headers)
    response.raise_for_status()

    TARGET.write_text(response.text, encoding="utf-8")
    print(f"Wrote {TARGET.relative_to(HERE)} ({len(response.text)} bytes)")

if __name__ == "__main__":
    main()
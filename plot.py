# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "beautifulsoup4"]
# ///

"""
Parse the saved Wikipedia HTML and plot typhoon wind speed vs. central pressure.
"""

import re
from pathlib import Path
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

HERE = Path(__file__).parent
DATA = HERE / "data"
OUT = HERE / "out"
OUT.mkdir(exist_ok=True)

SOURCE = DATA / "typhoons-2025.html"

def extract_number(text, unit):
    """从文本中提取出指定单位前的数字，例如 '215 km/h' -> 215.0"""
    if not text:
        return None
    match = re.search(r'([\d,]+\.?\d*)\s*' + unit, text)
    if match:
        try:
            return float(match.group(1).replace(',', ''))
        except ValueError:
            return None
    return None

def main():
    if not SOURCE.exists():
        raise FileNotFoundError(f"Missing source file {SOURCE.relative_to(HERE)}. Run fetch.py first.")

    html = SOURCE.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")

    wind_speeds = []
    pressures = []

    # 遍历维基百科表格中的每一行
    for row in soup.select("table.wikitable.sortable tr"):
        cells = row.find_all(["th", "td"])
        if len(cells) < 6:
            continue
        
        # 假设风速和气压在特定的列（根据维基百科表格结构调整，通常风速在某列，气压在另一列）
        # 这里我们遍历单元格尝试提取数值
        row_text = " ".join([cell.get_text(strip=True) for cell in cells])
        
        speed = extract_number(row_text, "km/h")
        pressure = extract_number(row_text, "hPa")

        if speed and pressure:
            wind_speeds.append(speed)
            pressures.append(pressure)

    print(f"Extracted {len(wind_speeds)} valid typhoon data points.")

    # 画散点图：气压 vs 风速
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(pressures, wind_speeds, color="#d6591d", alpha=0.7, edgecolors="none")
    
    ax.set_title("2025 Pacific Typhoons: Pressure vs. Wind Speed", fontsize=11)
    ax.set_xlabel("Central Pressure (hPa)")
    ax.set_ylabel("Peak Wind Speed (km/h)")
    ax.grid(True, linestyle="--", alpha=0.5)

    target = OUT / "plot.png"
    fig.savefig(target, dpi=150, bbox_inches="tight")
    print(f"Wrote {target.relative_to(HERE)}")
    
    plt.show()

if __name__ == "__main__":
    main()
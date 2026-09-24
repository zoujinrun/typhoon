# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "beautifulsoup4"]
# ///

"""
Parse saved Wikipedia HTML and plot typhoon wind speed vs. central pressure,
color-coded by chronological order (time progression through the season).
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
        
        row_text = " ".join([cell.get_text(strip=True) for cell in cells])
        
        speed = extract_number(row_text, "km/h")
        pressure = extract_number(row_text, "hPa")

        if speed and pressure:
            wind_speeds.append(speed)
            pressures.append(pressure)

    print(f"Extracted {len(wind_speeds)} valid typhoon data points.")
    
    if not wind_speeds:
        print("Warning: No data points found. Please check the HTML table structure.")
        return

    # 打印一些基础统计洞察
    print(f"-> 本季记录到的最高风速: {max(wind_speeds)} km/h")
    print(f"-> 本季记录到的最低气压: {min(pressures)} hPa")

    # 画散点图：气压 vs 风速（按时间顺序用渐变色展示）
    fig, ax = plt.subplots(figsize=(7, 6))
    
    # 用数据出现的先后顺序（索引）作为时间演变轴
    time_sequence = range(len(wind_speeds))
    
    scatter = ax.scatter(
        pressures, wind_speeds, 
        c=time_sequence, cmap="plasma", 
        s=60, alpha=0.85, edgecolors="none"
    )
    
    # 添加颜色条（已修复转义字符问题）
    cbar = plt.colorbar(scatter)
    cbar.set_label("Season Progression (Early -> Late)", fontsize=10)

    ax.set_title("2025 Pacific Typhoons: Pressure vs. Wind Speed", fontsize=12, pad=12)
    ax.set_xlabel("Central Pressure (hPa)", fontsize=10)
    ax.set_ylabel("Peak Wind Speed (km/h)", fontsize=10)
    ax.grid(True, linestyle="--", alpha=0.4)

    target = OUT / "plot.png"
    fig.savefig(target, dpi=150, bbox_inches="tight")
    print(f"Wrote {target.relative_to(HERE)}")
    
    plt.show()

if __name__ == "__main__":
    main()
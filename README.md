# 2025 Pacific Typhoon Season Analysis

## The phenomenon
This project analyzes the **2025 Pacific Typhoon Season**, focusing on the physical relationship between the peak wind speeds and the central barometric pressures of tropical cyclones recorded throughout the season.

## The source
The raw data is fetched directly from the Wikipedia page for the **2025 Pacific typhoon season**, saved locally as an immutable HTML file to ensure full reproducibility without requiring live network access:
- **Source URL**: `https://en.wikipedia.org/wiki/2025_Pacific_typhoon_season`
- **Local Storage**: `data/typhoons-2025.html`

## What the picture shows
The generated scatter plot (`out/plot.png`) visualizes 36 valid data points extracted from the season's storm tables. It maps **Central Pressure (hPa)** against **Peak Wind Speed (km/h)**. 

- **What it shows**: The expected inverse physical correlation—lower central barometric pressure (indicating a more intense storm) generally corresponds to higher peak wind speeds.
- **What it hides**: It hides individual storm trajectories, geographical locations, lifespan durations, and temporal sequencing (when each storm occurred during the season).

- ![Pacific Typhoon Season Scatter Plot](out/plot.png)

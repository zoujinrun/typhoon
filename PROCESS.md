## Process
1. Selected the 2025 Pacific Typhoon Season from Wikipedia as the project phenomenon.
2. Wrote `fetch.py` to download and cache the raw HTML page locally into `data/typhoons-2025.html`.
3. Developed `plot.py` using BeautifulSoup to extract valid wind speed and central pressure data points.
4. Generated a scatter plot visualizing the inverse physical relationship between pressure and wind speed, saving it to `out/plot.png`.

## Tools
- **Python**: Core programming language.
- **uv**: Dependency management and script runner.
- **BeautifulSoup**: HTML parsing and data extraction.
- **Matplotlib**: Data visualization and scatter plotting.
- **Git & GitHub**: Version control and remote repository hosting.

## Kept
- **Local Raw Data Caching**: Kept the raw HTML file in `data/` to guarantee full reproducibility and offline execution.
- **Iterative Commit History**: Maintained a clear commit structure separating data acquisition from visualization.

## Rejected
- **Live Scraping on Every Run**: Rejected fetching the webpage dynamically during plotting, as Wikipedia pages change daily and external network reliance breaks reproducibility.
- **Unrelated Open Datasets**: Discarded template default CSV files (like Hong Kong temperature) to keep the repository strictly focused on the typhoon theme.# Process

<!-- Same as assignment 1, same honesty. Which tools you used and for what; one
thing you kept and why it was good; one thing you rejected and why it was wrong.
"I did not use any" is fine if it is true.

If a model wrote most of plot.py, which is likely and allowed, the interesting part
is what you had to correct: did it invent a column name, use pandas where a list
would do, silently drop the rows it could not parse? -->

## Tools

## Kept

## Rejected

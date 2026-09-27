# BRICS Summit & Member Economics Analytics

A data analytics project examining the 18-edition history of BRICS summits (2009–2026)
and the economic profile of its current 11 member countries — built around the
18th BRICS Summit hosted by India in New Delhi (September 2026).

## What this project does

- Cleans and structures two datasets (summit history, member country economics) with **pandas**
- Runs exploratory analysis: host-country frequency, membership growth over time,
  GDP/population correlation, regional GDP breakdown
- Generates five publication-ready charts with **matplotlib** + **seaborn**
- Includes a self-contained **HTML/JS dashboard** (Chart.js) as an interactive, shareable view of the same data

## Project structure

```
brics_summit_analytics/
├── data/
│   ├── brics_summits.csv       # 18 summits: year, host, city, theme, format
│   └── brics_countries.csv     # 11 members: GDP, population, growth, region
├── src/
│   ├── data_loader.py          # CSV loading + type cleaning
│   ├── analysis.py             # pandas groupbys, stats, correlations
│   └── visualize.py            # matplotlib/seaborn chart generation
├── output/                     # generated charts + exported JSON (created on run)
├── dashboard.html              # standalone interactive dashboard
├── main.py                     # runs the full pipeline
├── requirements.txt
└── README.md
```

## How to run

```bash
pip install -r requirements.txt
python main.py
```

This prints the full analysis report to the console and saves five charts to `/output`:
- `gdp_by_country.png`
- `population_vs_gdp.png`
- `membership_growth.png`
- `host_frequency.png`
- `gdp_growth_rate.png`

Then open `dashboard.html` directly in a browser (no server needed) for the interactive version.

## Sample insights

- BRICS grew from 4 founding members (2009) to 11 by 2025, with the largest single
  expansion in 2024 (5 new members admitted at once).
- Russia, Brazil, and India have each hosted the summit 4 times — more than any other member.
- GDP and population show a moderate positive correlation (~0.77) across members,
  but per-capita GDP varies enormously (from ~$1,200 to ~$52,000), showing the bloc
  spans very different stages of economic development.
- China and India together account for over 70% of the bloc's combined population
  but a more modest share of combined GDP, reflecting lower GDP-per-capita relative to member average.

## Tech stack

Python · pandas · matplotlib · seaborn · HTML/CSS/JavaScript · Chart.js

## Data sources & notes

Compiled from public reporting (IMF/World Bank figures, PIB and official BRICS summit
records, and 2025–2026 news coverage of BRICS expansion). Economic figures are
recent-year approximations for portfolio/demonstration purposes, not official
real-time statistics — for production use, swap `data/brics_countries.csv` for a
live pull from the World Bank or IMF API.

## Possible extensions (good "future work" talking points in an interview)

- Pull live GDP/trade data via the World Bank API instead of the static CSV
- Add a time series of each member's GDP across all 18 summit years
- NLP-based theme analysis across the 18 summit themes (common keywords/topics)
- Deploy the dashboard with a small Flask/FastAPI backend for live data refresh

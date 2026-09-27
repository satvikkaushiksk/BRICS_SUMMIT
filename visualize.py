"""
visualize.py
Generates all chart images (saved to /output) using matplotlib + seaborn.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from data_loader import load_summits, load_countries
from analysis import membership_growth, host_country_frequency, region_breakdown

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "output"
sns.set_theme(style="whitegrid")


def plot_gdp_by_country(countries):
    plt.figure(figsize=(9, 5))
    data = countries.sort_values("gdp_billion_usd", ascending=False)
    sns.barplot(data=data, x="gdp_billion_usd", y="country", hue="country", palette="crest", legend=False)
    plt.title("BRICS Member GDP (Billion USD)")
    plt.xlabel("GDP (Billion USD)")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "gdp_by_country.png", dpi=150)
    plt.close()


def plot_population_vs_gdp(countries):
    plt.figure(figsize=(7, 6))
    sns.scatterplot(
        data=countries, x="population_millions", y="gdp_billion_usd",
        hue="region", s=140
    )
    for _, row in countries.iterrows():
        plt.text(row["population_millions"] + 10, row["gdp_billion_usd"], row["country"], fontsize=8)
    plt.title("Population vs GDP across BRICS Members")
    plt.xlabel("Population (millions)")
    plt.ylabel("GDP (Billion USD)")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "population_vs_gdp.png", dpi=150)
    plt.close()


def plot_membership_growth(countries):
    growth = membership_growth(countries)
    plt.figure(figsize=(8, 5))
    sns.lineplot(data=growth, x="joined_year", y="cumulative_members", marker="o")
    plt.title("BRICS Membership Growth Over Time")
    plt.xlabel("Year")
    plt.ylabel("Cumulative Member Count")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "membership_growth.png", dpi=150)
    plt.close()


def plot_host_frequency(summits):
    freq = host_country_frequency(summits)
    plt.figure(figsize=(7, 5))
    sns.barplot(x=freq.values, y=freq.index, hue=freq.index, palette="flare", legend=False)
    plt.title("Number of Times Each Country Hosted a BRICS Summit")
    plt.xlabel("Summits Hosted")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "host_frequency.png", dpi=150)
    plt.close()


def plot_gdp_growth_rate(countries):
    plt.figure(figsize=(8, 5))
    data = countries.sort_values("gdp_growth_pct", ascending=False)
    sns.barplot(data=data, x="gdp_growth_pct", y="country", hue="country", palette="mako", legend=False)
    plt.title("GDP Growth Rate by BRICS Member (%)")
    plt.xlabel("GDP Growth (%)")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "gdp_growth_rate.png", dpi=150)
    plt.close()


def generate_all():
    OUTPUT_DIR.mkdir(exist_ok=True)
    summits = load_summits()
    countries = load_countries()

    plot_gdp_by_country(countries)
    plot_population_vs_gdp(countries)
    plot_membership_growth(countries)
    plot_host_frequency(summits)
    plot_gdp_growth_rate(countries)

    print(f"Charts saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    generate_all()

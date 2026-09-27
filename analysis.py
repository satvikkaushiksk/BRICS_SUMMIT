"""
analysis.py
Core analytical routines over the BRICS datasets: summary stats,
groupings, and derived insights used in the final report.
"""

import pandas as pd
from data_loader import load_summits, load_countries


def host_country_frequency(summits: pd.DataFrame) -> pd.Series:
    """How many times has each country hosted the summit?"""
    return summits["host_country"].value_counts()


def membership_growth(countries: pd.DataFrame) -> pd.DataFrame:
    """Cumulative member count by the year each country joined."""
    growth = (
        countries.groupby("joined_year")
        .size()
        .rename("new_members")
        .reset_index()
        .sort_values("joined_year")
    )
    growth["cumulative_members"] = growth["new_members"].cumsum()
    return growth


def economic_summary(countries: pd.DataFrame) -> pd.DataFrame:
    """Key economic stats per country, sorted by GDP descending."""
    cols = ["country", "region", "gdp_billion_usd", "population_millions",
            "gdp_per_capita_usd", "gdp_growth_pct"]
    return countries[cols].sort_values("gdp_billion_usd", ascending=False).reset_index(drop=True)


def bloc_totals(countries: pd.DataFrame) -> dict:
    """Aggregate bloc-wide totals: combined GDP, population, avg growth."""
    return {
        "total_gdp_billion_usd": round(countries["gdp_billion_usd"].sum(), 1),
        "total_population_millions": round(countries["population_millions"].sum(), 1),
        "avg_gdp_growth_pct": round(countries["gdp_growth_pct"].mean(), 2),
        "member_count": len(countries),
    }


def region_breakdown(countries: pd.DataFrame) -> pd.DataFrame:
    """GDP and population aggregated by region."""
    return (
        countries.groupby("region")[["gdp_billion_usd", "population_millions"]]
        .sum()
        .sort_values("gdp_billion_usd", ascending=False)
    )


def gdp_population_correlation(countries: pd.DataFrame) -> float:
    """Pearson correlation between GDP and population across members."""
    return round(countries["gdp_billion_usd"].corr(countries["population_millions"]), 3)


def print_report():
    summits = load_summits()
    countries = load_countries()

    print("=" * 60)
    print("BRICS SUMMIT & MEMBER ECONOMICS — ANALYSIS REPORT")
    print("=" * 60)

    print("\n--- Host country frequency ---")
    print(host_country_frequency(summits))

    print("\n--- Membership growth over time ---")
    print(membership_growth(countries))

    print("\n--- Economic summary (sorted by GDP) ---")
    print(economic_summary(countries).to_string(index=False))

    print("\n--- Bloc-wide totals ---")
    for k, v in bloc_totals(countries).items():
        print(f"{k}: {v}")

    print("\n--- GDP by region ---")
    print(region_breakdown(countries))

    print(f"\nGDP vs Population correlation: {gdp_population_correlation(countries)}")


if __name__ == "__main__":
    print_report()

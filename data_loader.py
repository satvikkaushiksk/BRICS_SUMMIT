"""
data_loader.py
Loads and lightly cleans the BRICS datasets used across the project.
"""

import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def load_summits() -> pd.DataFrame:
    """Load the BRICS summit history dataset."""
    df = pd.read_csv(DATA_DIR / "brics_summits.csv")
    df["year"] = df["year"].astype(int)
    return df


def load_countries() -> pd.DataFrame:
    """Load the BRICS member country economic/demographic dataset."""
    df = pd.read_csv(DATA_DIR / "brics_countries.csv")
    numeric_cols = [
        "population_millions",
        "gdp_billion_usd",
        "gdp_growth_pct",
        "gdp_per_capita_usd",
    ]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


if __name__ == "__main__":
    print(load_summits().head())
    print(load_countries().head())

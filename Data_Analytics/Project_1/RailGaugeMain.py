# Railway Gauge code for Data Analytics.




"""
Railway Gauge Data Analytics
Run: python main.py
Place railway_gauges.csv in the same folder as this script.
Required: pandas, numpy, matplotlib, seaborn
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

BASE = Path(__file__).resolve().parent
GRAPH_DIR = BASE / "graphs"
GRAPH_DIR.mkdir(exist_ok=True)
CSV_PATH = BASE / "railway_gauges.csv"
REQUIRED = ["Year", "Broad Gauge", "Metre Gauge", "Narrow Gauge", "Total"]
GAUGES = ["Broad Gauge", "Metre Gauge", "Narrow Gauge"]

def main():
    # SCENARIO 1: Load, inspect, clean, convert
    df = pd.read_csv(CSV_PATH)
    print("\\n--- SCENARIO 1: DATA LOADING & CLEANING ---")
    print("First five rows:\\n", df.head())
    print("\\nColumn names:", df.columns.tolist())
    print("\\nMissing values before cleaning:\\n", df.isna().sum())
    df = df[REQUIRED].copy()
    df = df.fillna(0)
    for col in REQUIRED[1:]:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    df["Year"] = df["Year"].astype(str)
    print("\\nData types after conversion:\\n", df.dtypes)
    print("\\nMissing values after cleaning:\\n", df.isna().sum())
    df.to_csv(BASE / "railway_gauges_cleaned.csv", index=False)

    sns.set_theme(style="whitegrid")

    # SCENARIO 2: Total track growth line graph
    print("\\n--- SCENARIO 2: TOTAL RAILWAY GROWTH ---")
    plt.figure(figsize=(11, 5.8))
    plt.plot(df["Year"], df["Total"], marker="o")
    plt.title("Total Railway Track Length Over Time")
    plt.xlabel("Financial Year"); plt.ylabel("Track Length (dataset units)")
    plt.xticks(rotation=65, ha="right"); plt.tight_layout()
    plt.savefig(GRAPH_DIR / "01_total_growth_line.png", dpi=180); plt.close()
    direction = "increasing" if df["Total"].iloc[-1] > df["Total"].iloc[0] else "decreasing"
    print(f"Overall total-track trend: {direction}")

    # SCENARIO 3: Filter years after 2000 and grouped bar chart
    print("\\n--- SCENARIO 3: POST-2000 GAUGE COMPARISON ---")
    year_start = pd.to_numeric(df["Year"].str[:4], errors="coerce")
    recent = df.loc[year_start > 2000].copy()
    x = np.arange(len(recent)); width = 0.26
    plt.figure(figsize=(12, 6))
    for i, col in enumerate(GAUGES):
        plt.bar(x + (i-1)*width, recent[col], width=width, label=col)
    plt.title("Railway Gauge Comparison After 2000")
    plt.xlabel("Financial Year"); plt.ylabel("Track Length (dataset units)")
    plt.xticks(x, recent["Year"], rotation=55, ha="right")
    plt.legend(); plt.tight_layout()
    plt.savefig(GRAPH_DIR / "02_post_2000_grouped_bar.png", dpi=180); plt.close()
    if not recent.empty:
        print("Dominant gauge after 2000 (highest average):", recent[GAUGES].mean().idxmax())

    # SCENARIO 4: Gauge totals and pie chart
    print("\\n--- SCENARIO 4: CUMULATIVE GAUGE CONTRIBUTION ---")
    gauge_totals = df[GAUGES].sum()
    print(gauge_totals)
    plt.figure(figsize=(8, 7))
    plt.pie(gauge_totals.values, labels=gauge_totals.index, autopct="%1.1f%%",
            startangle=90, explode=[0.06 if c == gauge_totals.idxmax() else 0 for c in GAUGES])
    plt.title("Cumulative Gauge Contribution Across Yearly Records")
    plt.tight_layout()
    plt.savefig(GRAPH_DIR / "03_gauge_contribution_pie.png", dpi=180); plt.close()

    # SCENARIO 5: Feature engineering, np.diff, percentage line and stacked chart
    print("\\n--- SCENARIO 5: ADVANCED ANALYSIS ---")
    for col, label in zip(GAUGES, ["% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]):
        df[label] = np.where(df["Total"] != 0, df[col] / df["Total"] * 100, 0)
    yearly_growth = np.diff(df["Total"].to_numpy())
    df["Yearly Growth"] = np.r_[np.nan, yearly_growth]
    df.to_csv(BASE / "railway_gauges_analysis.csv", index=False)

    plt.figure(figsize=(11, 6))
    for label in ["% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]:
        plt.plot(df["Year"], df[label], marker="o", label=label)
    plt.title("Gauge Percentage Composition Over Time")
    plt.xlabel("Financial Year"); plt.ylabel("Share of Total (%)")
    plt.xticks(rotation=65, ha="right"); plt.legend(); plt.tight_layout()
    plt.savefig(GRAPH_DIR / "04_gauge_percentage_trend.png", dpi=180); plt.close()

    plt.figure(figsize=(12, 6))
    plt.bar(df["Year"], df["Broad Gauge"], label="Broad Gauge")
    plt.bar(df["Year"], df["Metre Gauge"], bottom=df["Broad Gauge"], label="Metre Gauge")
    plt.bar(df["Year"], df["Narrow Gauge"],
            bottom=df["Broad Gauge"] + df["Metre Gauge"], label="Narrow Gauge")





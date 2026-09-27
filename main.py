"""
main.py
Entry point: runs the full BRICS Summit Analytics pipeline —
loads data, prints the analysis report, and generates all charts.
"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "src"))

from analysis import print_report
from visualize import generate_all

if __name__ == "__main__":
    print_report()
    print("\nGenerating charts...")
    generate_all()
    print("Done. See the /output folder for all visualizations.")

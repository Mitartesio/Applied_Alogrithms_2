#!/usr/bin/env python3
import csv
from typing import Dict, List
import numpy as np
import matplotlib.pyplot as plt

def read_results(filename: str) -> Dict[int, List[float]]:
    results: Dict[int, List[float]] = {}
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            m = int(row["m"])
            value = float(row["Number Of Distinct Elements"])
            # Compute estimation error: (estimated - true) / true
            estimation_error = (value - 1_000_000) / 1_000_000
            if m not in results:
                results[m] = []
            results[m].append(estimation_error)
    return results

if __name__ == '__main__':
    results = read_results('Results.csv')
    ms = sorted(results.keys())
    num_ms = len(ms)
    # Define bins for the histograms
    bins = np.arange(-0.15, 0.16, 0.01)
    fig, axs = plt.subplots(1, num_ms, figsize=(15, 5), sharey=True)
    for i, m in enumerate(ms):
        estimation_errors = results[m]
        ax = axs[i]
        ax.hist(estimation_errors, bins=bins, edgecolor='black')
        ax.set_title(f'm = {m}')
        ax.set_xlabel('Estimation Error')
        if i == 0:
            ax.set_ylabel('Frequency')
        ax.set_xlim(-0.15, 0.15)
    plt.tight_layout()
    fig.savefig("estimation.png")

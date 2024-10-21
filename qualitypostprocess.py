#!/usr/bin/env python3

import csv
from typing import Dict, List
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore




def read_results(filename: str) -> Dict[str, np.ndarray]:
    results: Dict[str, np.ndarray] = {}
    
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        numbers = []
        leading_zeros = []
        
        for row in reader:
            number: int = int(row["number"])
            zeros: int = int(row["Leading zeros"])
            numbers.append(number)
            leading_zeros.append(zeros)

        results["data"] = np.array(list(zip(numbers, leading_zeros)))
    
    return results



def read_pfunction_results(filename: str) -> Dict[str, np.ndarray]:
    results: Dict[str, np.ndarray] = {}
    
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        numbers = []
        pfunction_values = []
        
        for row in reader:
            number: int = int(row["number"])
            p_value: float = float(row["chance"])  
            numbers.append(number)
            pfunction_values.append(p_value)


        results["data"] = np.array(list(zip(numbers, pfunction_values)))
    
    return results
        
    
    
    
def plot_results(data: Dict[str, np.ndarray], pfunction_data: Dict[str, np.ndarray], filename: str):
    (fig, ax) = plt.subplots()

    ns = data["data"][:, 0] 
    values = data["data"][:, 1] 

    ax.bar(ns, values, color='skyblue', label='Leading Zeros')

    p_ns = pfunction_data["data"][:, 0] 
    p_values = pfunction_data["data"][:, 1]


    ax.plot(p_ns, p_values, color='red', marker='o', linestyle='-', label="P Function")

    ax.set_xlabel('Number')
    ax.set_ylabel('Values (Leading Zeros / P Function)')
    ax.set_title('Leading Zeros Distribution and P Function Line')

    ax.set_xscale('linear')  
    ax.set_yscale('log')  

    ax.legend()

    fig.savefig(filename)
    


if __name__ == '__main__':
    raw_resultsHashedValues = read_results("QualityTest.csv")
    raw_resultsExpectedValues = read_pfunction_results("PFunctionResults.csv")
    plot_results(raw_resultsHashedValues,raw_resultsExpectedValues, "QualityTestHistogram.png")
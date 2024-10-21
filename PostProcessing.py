#!/usr/bin/env python3
import csv
from typing import Dict, List
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

def read_results(filename: str)-> \
    Dict[str,list[float]]:
        results: Dict[str, list[float]] = {}
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                method = row["method"]
                value = float(row["Number Of Distinct Elements"])
                
                if method not in results:
                    results[method] = []
                results[method].append(value)
        return results

def getY(filename: str):
    listofY : List[int] = []
    with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                listofY.append(row["n"])
            return list(dict.fromkeys(listofY))
                    
    
def plotAlgorithms(results: Dict[str, List[float]], yvalues: List[int]):
    fig, ax = plt.subplots(figsize=(15, 11))
    
    methods = list(results.keys())  
    num_methods = len(methods) 
    
    x = 10**6 
    width = 0.8 / num_methods  
    
    for i, (method, value) in enumerate(results.items()):
        ax.bar(x + i * width, value, width=width, label=method)
    
    
    plt.ticklabel_format(axis='y', style='plain')
    plt.xticks(rotation=45, ha='right')
    
    ax.plot(x,yvalues,color="black",linewidth=5, label="Correct number of distinct elements")
    
    ax.set_xticks(x + (num_methods - 1) * width / 2)
    ax.set_xticklabels(yvalues, fontsize=14)
  
    plt.xlabel("n values", fontsize=14)
    plt.ylabel("Number of distinct elements", fontsize=14)
    plt.title("Comparison of algorithms", fontsize=16)
    plt.legend(fontsize=12)
    plt.show()






if __name__ == '__main__':
    raw_results: Dict[str,List[float]] = \
        read_results('Results.csv')
    yValues: list[int] = \
        getY('Results.csv')
    plotAlgorithms(raw_results, yValues)
    
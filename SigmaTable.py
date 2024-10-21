
import csv
from typing import Dict, List
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
from typing import Tuple
import math



def read_Results(filename: str) -> Dict[str, np.array]:
    results: Dict[str, np.array] = {}
    
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile) 
        m_values = []
        cardinality = []
        
        for row in reader:
            m_value = int(row["m"])
            distinct_elements = float(row["Number Of Distinct Elements"])
            
            m_values.append(m_value)
            cardinality.append(distinct_elements)
        
    results["m"] = np.array(m_values)  
    results["cardinality"] = np.array(cardinality)
        
    return results


# def calculate_upper_lower_bounds1(n:int,m:int) -> Tuple[float,float]:
#     sigma = (1.04/math.sqrt(m))
    
#     lowerBound = n*(1-sigma)
#     upperbound = n*(1+sigma)
    
#     return (lowerBound,upperbound)


# def calculate_upper_lower_bounds2(n:int,m:int) -> Tuple[float,float]:
#     sigma = (1.04/math.sqrt(m))
    
#     lowerbound = n*(1-2*sigma)
#     upperbound = n*(1+2*sigma)
    
#     return (lowerbound,upperbound)




def calculate_counts_per_m(data: Dict[str, np.array]) -> Dict[int, Dict[str, float]]:
    m_values = data["m"]
    cardinalities = data["cardinality"]

    results = {}
    unique_m_values = np.unique(m_values)
    n = 1_000_000  # Constant value for n

    for m in unique_m_values:
        indices = np.where(m_values == m)[0]
        cardinalities_m = cardinalities[indices]

        total_n = len(cardinalities_m)
        within_sigma = 0
        within_2sigma = 0

        for c in cardinalities_m:
            sigma = 1.04 / math.sqrt(m)
            lower1 = n * (1 - sigma)
            upper1 = n * (1 + sigma)
            lower2 = n * (1 - 2 * sigma)
            upper2 = n * (1 + 2 * sigma)

            if lower1 <= c <= upper1:
                within_sigma += 1
            if lower2 <= c <= upper2:
                within_2sigma += 1

        percentage_sigma = (within_sigma / total_n) * 100 if total_n > 0 else 0
        percentage_2sigma = (within_2sigma / total_n) * 100 if total_n > 0 else 0

        results[m] = {
            'total_n': total_n,
            'within_sigma': within_sigma,
            'percentage_sigma': percentage_sigma,
            'within_2sigma': within_2sigma,
            'percentage_2sigma': percentage_2sigma
        }
    return results



def write_latex_summary_table(results: Dict[int, Dict[str, float]], filename: str):
    with open(filename, 'w') as f:
        f.write(r'\begin{table}[htbp]' + '\n')
        f.write(r'\centering' + '\n')
        f.write(r'\caption{Summary of Counts and Percentages for Each $m$}' + '\n')
        f.write(r'\begin{tabular}{rrrrrr}' + '\n')
        f.write(r'\toprule' + '\n')
        f.write(r'$m$ & Total $n$ & Within $n(1 \pm \sigma)$ & Percentage (\%) & Within $n(1 \pm 2\sigma)$ & Percentage (\%)' + r'\\' + '\n')
        f.write(r'\midrule' + '\n')
        for m in sorted(results.keys()):
            res = results[m]
            total_n = res['total_n']
            within_sigma = res['within_sigma']
            percentage_sigma = res['percentage_sigma']
            within_2sigma = res['within_2sigma']
            percentage_2sigma = res['percentage_2sigma']
            fields = [
                str(m),
                str(total_n),
                str(within_sigma),
                f'{percentage_sigma:.2f}',
                str(within_2sigma),
                f'{percentage_2sigma:.2f}'
            ]
            f.write(' & '.join(fields) + r'\\' + '\n')
        f.write(r'\bottomrule' + '\n')
        f.write(r'\end{tabular}' + '\n')
        f.write(r'\label{tab:summary_counts}' + '\n')
        f.write(r'\end{table}' + '\n')

       
        


if __name__ == "__main__":
    filename = 'Results.csv'
    data = read_Results(filename)
    
    results = calculate_counts_per_m(data)
    write_latex_summary_table(results, 'summary_table.tex')
        
    
    # for each n get upper and lower for 1 and 2 done
    # check if they're within and if they are, increment 1. done
    # make tabular. in prograss done
    

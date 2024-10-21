import csv
from typing import Dict, List, Tuple
import numpy as np # type: ignore
import subprocess


def run_java(jar: str, arg: str, input: str)->str:
    p = subprocess.Popen(['java','-jar',jar,arg], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE)
    (output,_) = p.communicate(input.encode('utf-8'))
    return output.decode('utf-8')

def createRandomInput(randomSeed: int, length: int)\
    -> set[int]:
    rng = np.random.default_rng(randomSeed)
    setOfRandomIntegers = set()
    while len(setOfRandomIntegers) < length:
        setOfRandomIntegers.add(rng.integers(1, 2**28))
    return setOfRandomIntegers
    
    
def benchmark(input: list[set[int]], algorithm, jar)->list[float]:
    results = []
    for set in input:
        input_string: str = f'{len(set)}\n' + \
            ' '.join(map(str,set))
        result: float = run_java(jar, algorithm, input_string)
        results.append(result) 
    return results

INSTANCES: List[Tuple[str,str]] = [
    ('HyperLogLog512', 'hyperloglogmethod/app/build/libs/app.jar'),
    ('HyperLogLog1024', 'hyperloglogmethod/app/build/libs/app.jar'),
    ('HyperLogLog2048', 'hyperloglogmethod/app/build/libs/app.jar')
]


if __name__ == '__main__':
    number = 10**6 #this is the smallest input
    # randomSeed = 68473
    listOfInput = []
    
    rng = np.random.default_rng(68473)
    
    for x in range(100):
        setOfRandomIntegers = set()
        while len(setOfRandomIntegers) < number:
            setOfRandomIntegers.add(rng.integers(1, 2**28))
        listOfInput.append(setOfRandomIntegers)
        
    with open('Results.csv','w') as f:
        writer = csv.DictWriter(f,fieldnames=["method", "m", "Number Of Distinct Elements"])
        writer.writeheader()
        for algorithm, jar in INSTANCES:
            m_value = int(''.join(filter(str.isdigit, algorithm)))
            resultList = benchmark(listOfInput, algorithm, jar)
            for number in resultList:
                    writer.writerow({ 
                        "method": algorithm,
                        "m":  m_value,
                        "Number Of Distinct Elements" : number.strip()
                    })
        

        
        
# For i=0; i<10^6 i++
# do Hash(i+1);
# make plot with that, with 
# 32 different outcomes. 
# How many outcomes did we have with 32 zero's
# How many outcomes did we have with 31 zero's
# How many outcomes did we have with 30 zero's
# etc etc etc


            
    
    
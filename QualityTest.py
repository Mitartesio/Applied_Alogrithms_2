import csv
import subprocess
# from typing import List


def run_java(jar: str, arg: str, input: str)->str:
    p = subprocess.Popen(['java','-jar',jar, arg], 
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE)
    (output,_) = p.communicate(input.encode('utf-8'))
    return output.decode('utf-8')

# def benchMark()-> list[int]:
#     ResultList = []
#     j = 0
#     for n in listOfNumbers:
#         n = format(n, '08x')
#         n = '0x'+n
#         inputString = f"1\n{n}"
#         result: str = run_java("hyperloglogmethod/app/build/libs/app.jar", "HyperLogLog" ,inputString)
#         result = result.strip()
#         print(j)
#         j += 1
#         result = int(result)
#         ResultList.append(result)
#     return ResultList    

# listOfNumbers = []
# for number in range(1,10**6):
#     listOfNumbers.append(number)

def benchMark():
    restultDict = {}
    outputString = run_java("hyperloglogmethod/app/build/libs/app.jar", "HyperLogLogTest", "").split("\n")
    outputString = outputString[:-1]
    for line in outputString:
        number, result = line.split()
        restultDict[number] = result
    return restultDict

def createPlotData():
    pResults = {}
    for n in range(1,32):
        pResults[n] = (2**(-n))*10**6
    return pResults
        

if __name__ == '__main__':
    with open("QualityTest.csv","w") as f:
        writer = csv.DictWriter(f,fieldnames=["number", "Leading zeros"])
        writer.writeheader()
        QualityResults = benchMark()
        for number, result in QualityResults.items():
            writer.writerow(
                {
                    "number": number,
                    "Leading zeros": result
                }
            )
    with open("PFunctionResults.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames = ["number", "chance"])
        writer.writeheader()
        pFunctionResults = createPlotData()
        for number, chance in pFunctionResults.items():
            writer.writerow(
                {
                    "number": number,
                    "chance": chance
                }
            )
    
    


        
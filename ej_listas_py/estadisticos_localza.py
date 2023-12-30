#media aritmetica, armonica, mediana, moda
from collections import Counter

def arithmetic_means(data):
    sum_list=sum(data)
    result=sum_list/len(data)
    return result

def harmonic_mean(data):
    sum_02 = sum(1 / i for i in data)
    result = len(data) / sum_02
    return result

def median(data):
    ordely=sorted(data)
    length=len(ordely)
    if length % 2 == 0:
        index1 = length // 2 - 1
        index2 = length // 2
        result = (ordely[index1] + ordely[index2]) / 2
    else:
        result = ordely[length // 2]
    return result

def fashion(data):
    counts = Counter(data)
    max_frequency = max(counts.values())
    result= [value for value, frequency in counts.items() if frequency == max_frequency]
    return result

def create_list(cant):
    list_n=[]
    print("Enter: ")
    for i in range(0,cant):
        data=int(input())
        list_n.append(data)
    return list_n

n=int(input("How many numbers will you enter? "))
list_num=create_list(n)

result_aritmethic=arithmetic_means(list_num)
result_harmonic=harmonic_mean(list_num)
result_median=median(list_num)
result_fashion=fashion(list_num)

if result_aritmethic>0 and result_harmonic>0 and result_median>0 and result_fashion>0:
    print(f"Arithmetic mean: {result_aritmethic}")
    print(f"Harmonic mean: {result_harmonic}")
    print(f"Median: {result_median}")
    print(f"Moda: {result_fashion}")
else:
    print(f"Arithmetic mean: {result_aritmethic}")
    print(f"Median: {result_median}")
    print(f"Moda: {result_fashion}")














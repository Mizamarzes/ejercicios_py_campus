import random
import math
    
def list_num(n):
    list_r=[]
    for i in range(n):
        num_random=random.uniform(-100,100)
        list_r.append(num_random)
    
    return list_r

def average(list_numbers):
    total=sum(list_numbers)
    avg=total/len(list_numbers)
    return avg

def substract(numbers, avg_result):
    prom_cuadrado=[]
    for i in numbers:
        total=i-avg_result
        result=total**2
        prom_cuadrado.append(result)
    return prom_cuadrado

def sum_substract_raiz(result_promCuadrad, n):
    result_sum_substract=sum(result_promCuadrad)
    total=result_sum_substract/n
    final_total=math.sqrt(total)
    return final_total
    

n = int(input("How many numbers?: "))
numbers = list_num(n)
avg_result = average(numbers)
result_promCuadrad = substract(numbers, avg_result)
final_result=sum_substract_raiz(result_promCuadrad, n)

print(final_result)



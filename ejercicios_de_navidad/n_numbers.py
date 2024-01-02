
total_num=0
average_pares=0; total_pares=0; sum_pares=0
average_impares=0; total_impares=0; sum_impares=0
num_less_than_10=0
num_between_20_50=0
num_majors_100=0
summation=0;cont=0
while True:
    print("Enter")
    num=int(input())

    if num<0:
        break
    
    total_num+=1

    if num<10:
        num_less_than_10+=1

    if num>=20 and num<=50:
        num_between_20_50+=1
    
    if num>100:
        num_majors_100+=1

    if num % 2 == 0:
        total_pares += 1
        sum_pares += num
    else:
        total_impares += 1
        sum_impares += num

average_pares = sum_pares / total_pares if total_pares > 0 else 0
average_impares = sum_impares / total_impares if total_impares > 0 else 0

print("Registro: ")
print(f"Total numeros ingresados: {total_num}")
print(f"Total pares: {total_pares}")
print(f"Promedio pares: {average_pares}")
print(f"Promedio impares: {average_impares}")
print(f"Numeros menores que 10: {num_less_than_10}")
print(f"Numeros estan entre 20 y 50: {num_between_20_50}")
print(f"Numeros mayores a 100: {num_majors_100}")
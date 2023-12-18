#histograma de numeros negativos y positivos
n=1
sumPositivos=0
sumNegativos=0
while True:
    n=int(input("Ingrese:"))
    
    if n>0:
        sumPositivos+=1
    elif n<0:
        sumNegativos+=1

    if n==0:
        break

print("POSITIVOS: ", "*"*sumPositivos)
print("NEGATIVOS: ", "*"*sumNegativos)
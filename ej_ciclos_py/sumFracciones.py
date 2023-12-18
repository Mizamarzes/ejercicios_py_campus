#suma de fracciones de la potencia de 2**?
rta=0
sum=0
tabla=0
total=0
while True:
    sum+=1
    rta=1/2**sum
    total+=rta
    if tabla==0:
        print("Potencia---Fraccion---Suma")
        tabla=1

    print(sum,"---",rta,"---",total)

    if (rta<=0.000001):
        break

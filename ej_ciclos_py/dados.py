#combinaciones de puntaje con dados de 1 a 6 puntos, xd

puntaje=int(input("Ingrese el puntaje: "))
comb=0    

for n1 in range(1, 7):
    for n2 in range(1, 7):
        if n1 + n2 == puntaje:
            comb += 1

print("Hay ",comb ," para obtener el puntaje de: ",puntaje)


















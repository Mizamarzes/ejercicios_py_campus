#formar una figura con astericos
altura=int(input("INGRESE LA ALTURA: "))
ancho=int(input("INGRESE EL ANCHO: "))
for i in range(altura-1):
    print("*")
    for j in range(ancho-1):
        print("*",end="")
    
print("")

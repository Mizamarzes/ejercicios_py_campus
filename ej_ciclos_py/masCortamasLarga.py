#palabras mas larga y mas corta
n=0
longitud=0
longMasLarga=0
LongMasCorta=100000
n=int(input("Ingrese cantidad de palabras: "))
for i in range(0,n,1):
    word=str(input("Palabra:"))
    longitud=len(word)

    if longitud>longMasLarga:
        longMasLarga=longitud
    
    if longitud<LongMasCorta:
        LongMasCorta=longitud

print("Palabra mas larga es de: ", longMasLarga)
print("Palabra mas corta es de: ", LongMasCorta)
    

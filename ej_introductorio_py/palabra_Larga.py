#palabra mas larga
a=str(input("INGRESE UNA PALABRA: "))
b=str(input("INGRESE OTRA PALABRA: "))
c=len(a)          #longitud palabra a
d=len(b)          #longitud palabra b
if c>d:
    z=c-d
    print("LA PALABRA ", a, "TIENE ", z, " LETRAS MAS QUE ",b)
else:
    z=d-c
    print("LA PALABRA ", b, "TIENE ", z, " LETRAS MAS QUE ",a)
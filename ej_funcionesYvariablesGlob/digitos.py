#determinar la cantidad de digitos de un numero entero
def calcDigitos(n):
    long=len(n)
    print(n," tiene ",long, " digitos")

n=str(input("Ingrese numero: "))
calcDigitos(n)
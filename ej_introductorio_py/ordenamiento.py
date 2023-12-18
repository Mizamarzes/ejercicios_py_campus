# Ordenamiento de cuatro números
numero1 = int(input("Ingrese numero: "))
numero2 = int(input("Ingrese numero: "))
numero3 = int(input("Ingrese numero: "))
numero4 = int(input("Ingrese numero: "))

# Ordenar los números de menor a mayor
if numero1 > numero2:
    numero1, numero2 = numero2, numero1
if numero2 > numero3:
    numero2, numero3 = numero3, numero2
if numero3 > numero4:
    numero3, numero4 = numero4, numero3
if numero1 > numero2:
    numero1, numero2 = numero2, numero1
if numero2 > numero3:
    numero2, numero3 = numero3, numero2
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

# Mostrar los números ordenados
print(numero1, numero2, numero3, numero4)
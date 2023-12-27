def equals(lista):
    return all(elemento == lista[0] for elemento in lista)

def different(lista):
    return len(set(lista)) == len(lista)

lista = []
cant=int(input("How many numbers, you want for you list: "))

for i in range(cant):
    n = int(input("Enter a number: "))
    lista.append(n)

selection = int(input("Enter 1 for equals or 2 for different: "))

if selection == 1:
    if equals(lista):
        print("True")
    else:
        print("False")
elif selection == 2:
    if different(lista):
        print("True")
    else:
        print("False")
else:
    print("Invalid selection")

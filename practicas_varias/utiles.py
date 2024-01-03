def ingresarDatoNumerico(enunciado):
    while True:
        dato=input(enunciado)
        if dato.isdigit():
            return dato
            break
        else:
            print("Error, the dato is not string")

def ingresarDatoCadena(enunciado):
    while True:
        dato=input(enunciado)
        if dato.isalpha():
            return dato
            break
        else:
            print("Error, the dato is not string")

def ingresarDatoPositivo(enunciado):
    while True:
        dato=input(enunciado)
        if dato.isdigit():
            dato_num=int(dato)
            if dato_num>=0:
                return int(dato_num)
                break
            else:
                print("Error, Enter a positive number ")
        else:
            print("Error, enter a number")
            
def ingresarrangos(enunciado):
    while True:
        dato=input(enunciado)
        if dato.isdigit():
            dato_num=int(dato)
            if dato_num>=43 and dato_num<=98:
                return dato_num
                break
            else:
                print("Error, Enter again")
        else:
            print("Error, enter a number")
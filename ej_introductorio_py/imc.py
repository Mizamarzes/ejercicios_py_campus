#indice de masa corporal
edad=int(input("Ingrese su edad: "))
peso=float(input("Ingrese su peso: "))    #peso
altura=float(input("Ingrese su altura en metros(separado por coma): ")) 
imc=peso/(altura*altura)

if(edad<45 and imc<22.0):
    print("Riesgo bajo")
elif(edad<45 and imc>=22.0):
    print("Riesgo medio")
elif(edad>=45 and imc<22.0):
    print("Riesgo medio")
elif(edad>=45 and imc>=22.0):
    print("Riesgo alto")
    
#alza del dollar
def alza(days):
    maxAlza=0
    temp=0
    cont=0
    for i in range(0,days,1):
        cont+=1
        print("Dia ",cont,":")
        price=float(input())

        if cont > 1:
            dif = price - temp

            if dif > maxAlza:
                maxAlza = dif
        temp = price
    return maxAlza
  
days=int(input("Ingrese la cantidad de dias: "))
result=alza(days)
if result>0:
    print("La mayor alza fue de: ", round(result, 2), " pesos")
else:
    print("Incorrecto")   
        
        














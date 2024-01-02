def index(peso,altura):
    imc=peso/(altura*altura)
    return imc

def classifi(indice, normal_suma, sobrepeso_suma, obesidad_i, obesidad_ii, obesidad_iii):
    
    if indice>=18.5 and indice<=24.9:
        result="Normal"
        normal_suma+=1
    elif indice>=25 and indice<=29.9:
        result="Sobrepeso"
        sobrepeso_suma+=1
    elif indice>=30 and indice<=34.9:
        result="Obesidad I"
        obesidad_i+=1
    elif indice>=35 and indice<=39.9:
        result="Obesidad II"
        obesidad_ii+=1
    elif indice>=40:
        result="Obesidad III"
        obesidad_iii+=1
    else:
        print("Invalid")
    return result, normal_suma, sobrepeso_suma, obesidad_i, obesidad_ii, obesidad_iii

normal_suma=0;sobrepeso_suma=0;obesidad_i=0;obesidad_ii=0;obesidad_iii=0
print("Body mass index")
n=int(input("How many students: "))
for i in range(n):
    name=str(input("Enter your name: "))
    age=int(input("Enter your age: "))
    weight=float(input("Enter your weight in kg: "))
    height=float(input("Enter your height in meters: "))
    result_imc=index(weight,height)
    result_clasif, normal_suma, sobrepeso_suma, obesidad_i, obesidad_ii, obesidad_iii = classifi(
        result_imc, normal_suma, sobrepeso_suma, obesidad_i, obesidad_ii, obesidad_iii
    )
    print(f"Name: {name}, age: {age}, IMC: {result_imc}, state: {result_clasif}")

print("Cumulative counts:")
print("Normal:", normal_suma)
print("Sobrepeso:", sobrepeso_suma)
print("Obesidad I:", obesidad_i)
print("Obesidad II:", obesidad_ii)
print("Obesidad III:", obesidad_iii)







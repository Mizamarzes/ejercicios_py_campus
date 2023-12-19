#definir que numeros son mayores que el promedioo, ingresar cantidad de datos
t=0
z=0
sum=0
prom=0
cont=0
datos=[]
def formar_list():
    global t
    for i in range(0,n,1):
        t+=1
        print("Dato ",t,":")
        n1=float(input())
        datos.append(n1)

def promedio():    
    global z,sum,prom
    for i in datos:
       z+=1 
       sum+=i
       prom=sum/t

def mayores():
    global prom,cont
    for i in datos:
        if i>prom:
            cont+=1
        
       
n=int(input("Cuantos datos va a ingresar: "))
formar_list()
promedio()
mayores()
print(cont," datos son mayores que el promedio de: ",prom)



    
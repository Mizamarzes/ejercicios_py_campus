#Digito verficcador, invertir numero, multiplicar los digitos por la secuencia 2,3,4,5,6,7
n=int(input("Ingrese digito: "))
invert=(str(n)[::-1])
j=1
k=1
sum=0
cant=0
for i in invert:
    j+=1
    if(j>=2 and j<=7):
        op=int(i)*j
        sum+=op
    elif j>7:
       k+=1 
       op=int(i)*k
       sum+=op

mod=sum%11
rest=11-mod
print("DIGITO VERIFICADOR: ",n,"-",rest) 
 



    





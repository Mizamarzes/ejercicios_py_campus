#Numeros palindromos, indicar si el numero es palindromo o no
invert=int(0)
n=int(input("Ingrese digito: "))
invert=(str(n)[::-1])    
j=0
cont=0
n=str(n)
for i in invert:
    if i!=n[j]:
       cont+=1
    j+=1
    
if cont==0:
    print("El numero es palindromo")
else:
    print("El numero no es palindromo")
    
        
        

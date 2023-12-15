def generarPi(n):
    sum=0
    signo=1
    
    for i in range(n):
        term=1/(2*i+1)
        sum=sum+signo*term
        signo*=-1
        
    estmPi=4*sum
    return estmPi

n=int(input("Ingrese el numero del termino para estimar pi: "))

print(generarPi(n))














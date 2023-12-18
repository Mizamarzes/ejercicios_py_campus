#set de tennis
#ganar set 6 juegos y 2 mas que su compañero
# set empatado a 5 juegos, el ganador el primero que llegue a 7
# si el set esta empatado a 6 juegos, gana el que gane el siguiente set

m=int(input("JUEGOS GANADOS POR JUGADOR A: "))
n=int(input("JUEGOS GANADOR POR JUGADOR B: "))

if(m>n):
    dif=m-n
elif(n>m):
    dif=n-m

if(m>n and m<=7 and dif==2):
    print("Jugador A gano")
elif(n>m and n<=7 and dif==2):
    print("Jugador B gano")
elif(m<=6 and n<=6 and dif<2):
    print("El set no ha terminado")
elif(m>=7 or n>=7 and dif>2):
    print("Resultado invalido")

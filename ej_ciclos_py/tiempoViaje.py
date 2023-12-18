#tiempo de viaje, tramos en minutos
horas=0
minutos=0

while True:
    dur=int(input("Duracion del tramo: "))
    if dur==0:
        break

    minutos += dur
    horas=minutos//60
    minutos=minutos%60

print(f"Tiempo total de viaje: {horas}:{minutos:02} horas")



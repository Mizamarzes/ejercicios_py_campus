#edad cumpleanos
diaAct=14
mesAct=12
anoAct=2023
dia=int(input("ingrese su dia de nacimiento: "))
mes=int(input("ingrese su mes de nacimiento: "))
ano=int(input("ingrese su ano de nacimiento: "))

anosrta=anoAct-ano
if(mes>mesAct and dia>diaAct):
    anosrta=anosrta+1
print("EDAD: ",anosrta)
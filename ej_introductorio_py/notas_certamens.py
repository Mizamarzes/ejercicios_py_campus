#que nota necesito

c1=float(input("INGRESE NOTA PRIMER CERTAMEN: "))
c2=float(input("INGRESE NOTA SEGUNDO CERTAMEN: "))
nl=float(input("INGRESE NOTA LABORATORIO: "))

nc=(60-(nl*0.3))/0.7
sum=(c1+c2)/3
rta=(nc-sum)*3
print("NECESITA NOTA DE: ", rta, " EN EL CERTAMEN 3")


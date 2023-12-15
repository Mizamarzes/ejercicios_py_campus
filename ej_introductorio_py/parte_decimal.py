#parte decimal
import math
a=float(input("INGRESE UN NUMERO DECIMAL: "))      #decimal
decim, enter=math.modf(a)         #sacar parte entera y decimal
print("Parte decimal: {} y su parte entera: {}".format(decim, enter))

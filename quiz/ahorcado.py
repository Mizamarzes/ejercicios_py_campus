# cantidad de partes del cuerpo: 6
# 6 intentos y si pasan los 6 intentos pierde

def mostrar(letras_adv,secreto):
    resultado=""
    for letra in secreto:
        if letra in letras_adv:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()


def completar():
    secreto=str(input("Ingrese la palabra: ")).lower()
    letras_adv=[]
    intentos_max=6
    intentos=0
    
    print("Palabra actual:", mostrar(letras_adv, secreto))
    
    while True:
        letra=str(input("Ingrese letra: ")).lower()  
        
        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, ingresa una única letra válida.")
            continue
        
        if letra in letras_adv:
            print("Ingresa otra letra ")
            continue
        
        letras_adv.append(letra)
        
        if letra not in secreto:
            intentos+=1
            print("Incorrecto has perdido una parte de tu cuerpo ")
            print("Te quedan: ", intentos_max-intentos, " intentos")
            if intentos == intentos_max:
                print("Perdiste")
                break
        else:
            palabraAct=mostrar(letras_adv, secreto)
            print("Correcto",palabraAct)
            
            if palabraAct.replace(" ","")==secreto:
                print("Ganaste")
                break
            
if __name__ == "__main__":
    completar() 




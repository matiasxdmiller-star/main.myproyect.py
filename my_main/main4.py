from ast import If


nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}! Bienvenido al juego.")
edad = int(input("¿Cuántos años tienes? "))

if edad >= 18: continuar = input(f"¡Hola {nombre}! eres mayor de edad, ¿quieres continuar jugando? (sí/no) ")
if edad >= 18 and continuar.lower() != "sí":
    if continuar.lower() == "no": 
        exit()
    print("¡entendido gracias continuemos con el juego!")
    
elif edad < 18: print(f"¡Hola {nombre}! eres menor de edad, el juego es para mayores de edad, ¡lo siento! ¡Hasta luego!") 
exit()



 
 
color_favorito = input("¿Cuál es tu color favorito? ")

print(f"¡Genial! Tu nombre es {nombre}, tienes {edad} años tu color favorito es {color_favorito}. ¡Vamos a jugar!")
print("¡Perfecto! Empecemos el juego.") 

import random 

numero_secreto = random.randint(1, 100)
intentos = 0

print("Bienvenido al juego de adivinar el número secreto entre 1 y 100")
while True:
    intento = int(input("Introduce tu intento: "))
    intentos += 1
    if intento < numero_secreto:
        print("Demasiado bajo, intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto, intenta de nuevo.")
    else:
        print(f"¡Felicidades! Has adivinado el número secreto {numero_secreto} en {intentos} intentos.")
import random

nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}! Bienvenido al juego.")

edad = int(input("¿Cuántos años tienes? "))

if edad < 18:
    print(f"¡Hola {nombre}! eres menor de edad, el juego es para mayores de edad. ¡Hasta luego!")
    exit()

continuar = input(f"¡Hola {nombre}! eres mayor de edad, ¿quieres continuar jugando? (sí/no) ")

if continuar.lower() == "no":
    print("Está bien, ¡hasta luego!")
    exit()

print("¡Perfecto! Continuemos con el juego.")

color_favorito = input("¿Cuál es tu color favorito? ")

print(f"¡Genial! Tu nombre es {nombre}, tienes {edad} años y tu color favorito es {color_favorito}.")
print("¡Empecemos el juego!")

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
        print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        break
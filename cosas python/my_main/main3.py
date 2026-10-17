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


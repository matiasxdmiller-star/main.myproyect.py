
import random
print("bienvenido a ppt o adivinar el numero")

print("antes de comenzar el juego tengo que saber tu edad")
edad = int(input("¿Cuantos años tienes? "))

if edad < 18:

    print("Lo siento, no puedes jugar porque eres menor de edad.")
    exit()
elif edad >= 18:
    print("¡Genial! Puedes jugar.")
    
    nombre = input("¿Cómo te llamas? ")
    
    print(f"¡Hola, {nombre}! Vamos a jugar.")
    print("¿Qué juego te gustaría jugar? (ppt/adivinar/salir)")
    
    juego = input("Elige tu juego: ").lower()
  
    if juego == "adivinar":
        print("¡Genial! Vamos a jugar a adivinar el número.")
        
        numero_secreto = random.randint(1, 100)
        intentos = 0
        
        while True:
            intento = int(input("Introduce tu intento: "))
            intentos += 1
            
            if intento < numero_secreto:
                print("Demasiado bajo, intenta de nuevo.")
            elif intento > numero_secreto:
                print("Demasiado alto, intenta de nuevo.")
            else:
                print(f"¡Felicidades! Has adivinado el número secreto {numero_secreto} en {intentos} intentos.")
                break
            print("¿Quieres seguir jugando? o ppt u irse? (adivinar/ppt/salir) ")
            seguir_jugando = input("Elige tu opción: ").lower()
            if seguir_jugando == "salir":
                print("¡Gracias por jugar!")
                break
            elif seguir_jugando == "adivinar":
                continue
            elif seguir_jugando == "ppt":
                pass
    elif juego == "ppt":    
        print("¡Genial! Vamos a jugar a piedra, papel o tijeras.")
        
        opciones = ["piedra", "papel", "tijeras"]
        
        while True:
            jugador = input("Elige piedra, papel o tijeras: ").lower()
            computadora = random.choice(opciones)
            
            print(f"La computadora eligió: {computadora}")
            
            if jugador == computadora:
                print("¡Empate!")
            elif (jugador == "piedra" and computadora == "tijeras") or (jugador == "papel" and computadora == "piedra") or (jugador == "tijeras" and computadora == "papel"):
                print("¡Ganaste!") 
            else:
                print("¡Perdiste!")
            print("¿Quieres seguir jugando? o adivinar u irse? (ppt/adivinar/salir) ")
            seguir_jugando = input("Elige tu opción: ").lower()
            if seguir_jugando == "salir":
                print("¡Gracias por jugar!")
                break
            elif seguir_jugando == "ppt":
                continue
            elif seguir_jugando == "adivinar":
                pass
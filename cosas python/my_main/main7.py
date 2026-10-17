import random

opciones = ["piedra", "papel", "tijeras"] 

elige = input("Elige piedra, papel o tijeras: ").lower()

if elige not in opciones:
    print("Opción no válida. Por favor, elige piedra, papel o tijeras.")
    exit() 
    
computadora = random.choice(opciones)
print(f"La computadora eligió: {computadora}")
print(f"Tú elegiste: {elige}")

if elige == computadora:
    print("¡Empate!")
    
elif (elige == "piedra" and computadora == "tijeras") or \
     (elige == "papel" and computadora == "piedra") or \
     (elige == "tijeras" and computadora == "papel"):
    print("¡Felicidades! Has ganado.")
    
if (elige == "piedra" and computadora == "papel") or \
   (elige == "papel" and computadora == "tijeras") or \
   (elige == "tijeras" and computadora == "piedra"):
    print("¡Lo siento! Has perdido.")
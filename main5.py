
print("¡Bienvenido al juego de adivinanza!")
print("Antes de comenzar, me gustaría conocerte un poco más.")  

nombre = input("¿Cuál es tu nombre? ")

edad = int(input("¿Cuántos años tienes? "))

if edad >= 18: continuar = input(f"¡Hola {nombre}! eres mayor de edad, ¿quieres continuar jugando? (sí/no) ")

if edad >= 18 and continuar.lower() != "sí":
    print("¡Entendido! Gracias por tu interés. Continuemos con el juego.")

elif edad < 18: print(f"¡Hola {nombre}! eres menor de edad, el juego es para mayores de edad, ¡lo siento! ¡Hasta luego!")
exit()
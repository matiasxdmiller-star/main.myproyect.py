# pida un numero y detecte si es par o impar y saber si es positivo o negativo
ENTRADA = int(input("Ingrese un número: "))

if ENTRADA % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

if ENTRADA > 0:
    print("El número es positivo")
elif ENTRADA < 0:
    print("El número es negativo")
else:
    print("El número es cero")
    
    
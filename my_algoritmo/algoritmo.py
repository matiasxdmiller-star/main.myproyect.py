# encontrar la mayor diferencia con el menor numero ingresado

while True:
    try:
        entrada = int(input("que cuantos numeros quieres ingresar:"))
    except ValueError:
        print("Error: por favor ingresa un numero valido")
        continue

    numeros_ingresados = []
    
    menor_hasta_ahora = None
    mayor_diferencia = None
    
    for i in range(entrada):
        
        try:
            numero = int(input(f"Ingresa el numero {i+1}:"))
            numeros_ingresados.append(numero)
            if menor_hasta_ahora is None or numero < menor_hasta_ahora:
                menor_hasta_ahora = numero
            if mayor_diferencia is None or numero > mayor_diferencia:
                mayor_diferencia = numero
        except ValueError:
            print("Error: por favor ingresa un numero valido")
            continue
        
    resultado = mayor_diferencia - menor_hasta_ahora
    print(f"{resultado}")

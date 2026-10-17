#Dado un arreglo de números enteros, escribe un algoritmo que calcule la suma de todos los números pares.
entrada = input("Ingresa un arreglo de números enteros separados por comas: ")
numeros = list(map(int, entrada.split(",")))
suma_pares = sum(num for num in numeros if num % 2 == 0)
print(f"La suma de los números pares es: {suma_pares}")
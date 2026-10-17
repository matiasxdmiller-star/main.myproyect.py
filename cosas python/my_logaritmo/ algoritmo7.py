# indicar el numero mayo en la serie de números ingresados
entrada = input("Ingrese una serie de numeros separados por comas: ").split(",")
entrada = [int(x) for x in entrada]
mayor = max(entrada)


conteo={}
for numero in entrada:
    if numero in conteo:
        conteo[numero] += 1
    else:
        conteo[numero] = 1

print("El número mayor es:", mayor, "y su frecuencia es:", conteo[mayor])


sa
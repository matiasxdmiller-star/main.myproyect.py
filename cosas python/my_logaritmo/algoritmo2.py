#ordenanr palabras alfabeticamente y cuantas veces aparece cada una
entrada = input("Ingresa una frase: ")
palabras = entrada.split()
palabras.sort()
conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1
for palabra, cantidad in conteo.items():
    print(f"{palabra}: {cantidad}")
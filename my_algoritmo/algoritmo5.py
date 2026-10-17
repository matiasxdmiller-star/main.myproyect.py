# La racha más larga positiva
entrada = input("Ingresa un arreglo de números enteros separados por comas: ")
entrada = entrada.split(",")

racha_mas_larga = None
racha_actual = None

for num_str in entrada:
    num = int(num_str)
    if num > 0:
        if racha_actual is None:
            racha_actual = 1
        else:
            racha_actual += 1
        if racha_mas_larga is None or racha_actual > racha_mas_larga:
            racha_mas_larga = racha_actual
    else:
        racha_actual = None
print(f"La racha más larga positiva es: {racha_mas_larga}")
# Escribe un algoritmo que determine si una palabra o frase es un palíndromo 
# (se lee igual de izquierda a derecha que de derecha a izquierda), ignorando espacios, mayúsculas y signos de puntuación.
entrada = input("ingrese una palabra o frase:")
entrada = entrada.lower()
entrada = "".join(c for c in entrada if c.isalnum())
if entrada == entrada[::-1]:
    print("La palabra o frase es un palíndromo.")
else:
    print("La palabra o frase no es un palíndromo.")
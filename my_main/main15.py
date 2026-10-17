
import math as m
from typing import Callable

print("¡Bienvenido al sistema de notas!")
cantidad_notas = int(input("¿Cuántas notas deseas ingresar? "))
notas = []

for i in range(cantidad_notas):
    nota = float(input(f"Ingresa la nota {i + 1} (20-70): "))
    if nota < 20 or nota > 70:
        print("Nota inválida. Por favor, ingresa una nota entre 20 y 70")
        break
    notas.append(nota)
else:
    promedio = sum(notas) / len(notas)
    promediofinal = m.floor(promedio / 10) 
    print(f"Tu promedio es: {promediofinal}")
    
 
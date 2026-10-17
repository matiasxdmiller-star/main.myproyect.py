import random

numeros =random.randint(1,7)

print(numeros) 

if numeros == 7:
    print("maxima calificacion")
    
elif numeros == 6 or numeros == 5 or numeros == 4:
    print("puede mejorar")
    
elif numeros == 3 or numeros == 2 or numeros == 1:
    print("reprobado")
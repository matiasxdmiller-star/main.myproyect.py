# calculadora basica muy basica que realiza operaciones de suma, resta, multiplicacion y division

print("bienvenido a mi calculadora")

while True:
    try:
        print("eliga que tipo de operacion desea realizar")

        print("1. suma")
        print("2. resta")
        print("3. multiplicacion")
        print("4. division") 
        print("5. salir")
    
        
        operacion = input("ingrese el numero de la operacion que desea realizar: ").lower()
        if operacion == "1" or operacion == "suma":
            
            numeros = input("ingrese los numeros a sumar separados por un espacio: ")
            numeros = numeros.split() 
            
        
            
            suma = (sum(int(num) for num in numeros))
            print(f"el resultado de la suma es: {suma}")
            
        elif operacion == "2" or operacion == "resta":
            numeros = input("ingrese los numeros en orde que desee para restar separados por un espacio: ")
            numeros = numeros.split()
            
            resta = int(numeros[0]) - sum(int(num) for num in numeros[1:])
            
            print(f"el resultado de la resta es: {resta}")
        elif operacion == "3" or operacion == "multiplicacion":
            
            numeros = input("ingrese los numeros a multiplicar separados por un espacio: ")
            numeros = numeros.split()
            
            multiplicacion = 1
            
            for num in numeros:
                
                multiplicacion *= int(num)
                
            print(f"el resultado de la multiplicacion es: {multiplicacion}")
            
        elif operacion == "4" or operacion == "division":
            numeros = input("ingrese los numeros en orden que desee para dividir separados por un espacio: ")
            numeros = numeros.split()
            
            division = int(numeros[0])
            
            for num in numeros[1:]:
                division /= int(num)
            print(f"el resultado de la division es: {division}")
            
        elif operacion == "5" or operacion == "salir":
            print("gracias por usar mi calculadora")
            break
        
    except  ValueError:
        print("error: por favor ingrese solo numeros validos")
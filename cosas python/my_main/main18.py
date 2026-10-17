# PAGINA O APP : FORMATO BACKEND

# AGREGAR TAREAS .-1: CALENDARIO O  (CALENDARIO DE TAREAS)
# agregar duracion de tareas

guardados = []

print("hola :D, ¿quieres agregar una tarea para hoy?")
print("o tal vez ver tus tareas?")

while True:
    try:
        opcion = input("ingrese lo que quiera ver hoy: ")

        if opcion == "agregar tarea":
            tarea_new = input("ingrese la nueva tarea: ")
            duracion = input("ingrese la duracion de la tarea: ")

            if tarea_new.strip() == "":
                print("la tarea no puede estar vacía")
            else:
                guardados.append({
                    "tarea": tarea_new,
                    "duracion": duracion,
                    "completada": False 
                })

                print(f"tarea agregada: {tarea_new} con duracion: {duracion}")

        elif opcion == "ver tareas":
            print("tareas para hoy:")

            if not guardados:
                print("no hay tareas para hoy")                   
            else:
                for tarea in guardados:
                    estado = "completada" if tarea["completada"] else "pendiente" # nuevo
                    print(f"- {tarea['tarea']} (duracion: {tarea['duracion']}) - estado: {estado}")
                    
        elif opcion == "marcar tarea":
        
            print("tareas disponibles:")
            for i in range(len(guardados)):
                print(f"{i + 1}. {guardados[i]['tarea']} (duracion: {guardados[i]['duracion']})")

            try:
                seleccion = int(input("ingrese el numero de la tarea a marcar como completada: "))
                if 1 <= seleccion <= len(guardados):
                    guardados[seleccion - 1]['completada'] = True
                    print(f"tarea marcada como completada: {guardados[seleccion - 1]['tarea']}")
               
                else:
                    print("numero de tarea invalido")
            except ValueError:
                print("error: por favor, ingrese un valor válido")

        elif opcion == "salir":
            print("gracias por usar mi app de tareas")
            break

    except ValueError:
        print("error: por favor, ingrese un valor válido")

    except Exception as e:
        print(f"error inesperado: {e}")
        
    
    
    
        
         


    

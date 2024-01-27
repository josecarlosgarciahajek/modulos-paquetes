from tareas import *

while True:

    print("Bienvenido al gestor de tareas")
    print("")
    print("1. Agregar nueva tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Salir")
    print("")
    try:
        opc = int(input("Seleccione una opción (1/2/3/4): "))
    except ValueError:
        print("Se esperaba un número")
        break
    
    if opc == 1:
        add_job(input("Ingrese tarea: "))
    elif opc == 2:
        try:
            end_jobs()
        except ValueError:
            print("Se esperaba una opción numérica")
    elif opc == 3:
        list_jobs()
    else:
        print("Adiós")
        break
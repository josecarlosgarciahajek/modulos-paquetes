lista = []
lista_num = []
lista_completada = []
cont = 0
complete = "[X]"
complete2 = ("(Completada)")
no_complete = "[ ]"
def add_job(tarea):
    global cont
    cont = cont + 1
    lista.append(tarea)
    lista_num.append(cont)
    print("Tarea añadida correctamente")
def end_jobs():
    lc = int(input("Escriba el ID de la tarea que desea marcar como completada: "))
    lista_completada.append(lc)
    print("Tarea marcada como completada con éxito")
def list_jobs():
    print("Lista de tareas:")
    global lista
    global lista_num
    for i in range(len(lista)):
        if lista_num[i] in lista_completada:
            print("-", complete, "ID:" ,lista_num[i], " - ", lista[i], complete2)
        else:
            print("-", no_complete, "ID:" ,lista_num[i], " - ", lista[i])
import operaciones

print("Bienvenido a la Calculadora de operaciones Básicas")
print("")
print("1. Suma")
print("2. Resta")
print("3. Multipicación")
print("4. División")

opc = input("Ingresa el número de la operación deseada: ")

if opc in ("1", "2", "3", "4"):
        numero1 = int(input("Dame un número: "))
        numero2 = int(input("Dame otro número: "))
        if opc == "1":
            print("El resultado es: ", operaciones.suma(numero1, numero2))
        elif opc == "2":
            print("El resultado es: ", operaciones.resta(numero1, numero2))
        elif opc == "3":
            print("El resultado es: ", operaciones.multiplicar(numero1, numero2))
        elif opc == "4":
            print("El resultado es: ", operaciones.dividir(numero1, numero2))
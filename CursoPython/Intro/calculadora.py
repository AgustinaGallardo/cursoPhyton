print("Bienvenido a la calculadora en python")
print("Para salir ingrese salir")
print("Las operaciones son suma, resta, multi, div")

resultado = ""
while True:
    if not resultado:
        resultado = input("Ingrese un numero con el que quiera operar: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    operar = input("Que tipo de operacion quiere realizar: ")
    if operar.lower() == "salir":
        break
    num2 = input("Ingrese el segundo numero con el que desea operar: ")

    if num2.lower() == "salir":
        break
    num2 = int(num2)
    if operar.upper() == "SUMA":
        resultado += num2
    elif operar.upper() == "RESTA":
        resultado -= num2
    elif operar.upper() == "MULTI":
        resultado *= num2
    elif operar.upper() == "DIV":
        resultado /= num2
    else:
        print("Operacion no valido")
        break

    print(f"El resultado es: {resultado}")

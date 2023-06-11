numeros = [22, 32, 3, 44, 135, 6, 27, 8, 9, 10]

numeros.sort()  # ordena LA MISMA LISTA
numeros.sort(reverse=True)  # ordena descendente
numeros2 = sorted(numeros, reverse=True)  # devulve UNA NUEVA LISTA


print(numeros)
print(numeros2)


usuarios = [
    ["Pulga", 4],
    ["Canto", 5],
    ["Mamita", 8]
]


# def ordena(elemento):    con lambda esto no haria falta
#    return elemento[1]


# FUNCIONES ANONIMAS : LAMBDA
# con lambda nos ahorramos pasar nombre de funcion y los parentesis con los param
usuarios.sort(key=lambda el: el[1], reverse=True)
# Ordena siempre y cuando tengo un ordenable al comienzo, o avisarle a sort donde tiene que ordenar
print(usuarios)

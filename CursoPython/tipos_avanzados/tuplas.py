"""
Las tuplas, es una lista, la diferencia es que no se puede modificar.-
No podes acgregar ni quitar ni modificarpero si podes crear otras tuplas de otras ya existentes
Se puede realizar todas las operacion de las listas
"""

numeros = (2, 3, 4, 5, 6) + (4, 5, 6)

print(numeros)

punto = tuple([1, 2])  # convierto cualquier iterable en una tupla
print(punto)
menosNumeros = numeros[:2]
# desempaquetar tuplas
primero, segundo, tercero, *otros = numeros
print(primero, segundo, otros)  # devulve una lista

for n in numeros:
    print(n)

# para poder cambiar un elemento hicimos una lista nueva
listNumeros = list(numeros)
listNumeros[0] = "ramona"
print(listNumeros)

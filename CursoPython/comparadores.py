buscar = 10
# Range = ITERABLE (cualquier cosa q nosotros podamos iterar) JUNTO CON LAS LISTAS TUPLAS STRINGS
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Numero encontrado ", buscar)
        break
else:
    print("No encontre el numero buscado")

for char in "Ultimate python":
    print(char)

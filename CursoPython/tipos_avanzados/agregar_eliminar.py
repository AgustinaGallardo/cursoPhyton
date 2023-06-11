mascotas = [
    "pulga",
    "roma",
    "ramona",
    "rolo",
    "ramona",
    "pulga"
]

mascotas.insert(1, "mora")
mascotas.append("juli")  # me lo guarda al ultimo
# solo elimina la primera ocurrencia, el primer elemento
mascotas.remove("pulga")
# elimina el ultimo sin indice...si lleva indice borra el indice
mascotas.pop(1)
del mascotas[1]  # elimina
mascotas.clear()  # elimina todo

print(mascotas)

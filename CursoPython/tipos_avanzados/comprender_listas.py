usuarios = [
    ["Pulga", 4],
    ["Canto", 5],
    ["Mamita", 8]
]
"""
nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])
print(nombres)

# MAP
nombres = [usuario[0] for usuario in usuarios]

# filtrar || FILTER
nombres = [usuario for usuario in usuarios if usuario[1] > 7]

# filtrar y transformar ||
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 7]

"""

# MAP
nombres = list(map(lambda usuario: usuario[0], usuarios))

# FILTER

menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)

lista = [1, 2, 3, 4]  # con lista
tupla = (2, 3, 4)
print(*lista)
print(*tupla)

lista2 = [5, 6]
combinada = ["hola", *lista2, "bueno", *lista]

print(combinada)

"""
igual pero con diccionarios
"""
punto1 = {"x": 2, "y": 4}
punto2 = {"y": 1}

nuevoPunto = {**punto1, "lala": "hola", **punto2}
print(nuevoPunto)

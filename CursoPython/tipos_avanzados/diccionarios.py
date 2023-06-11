"""
DICCIONARIOS = son una coleccion de datos q se agrupan por una llave y un valor

como llave solo string
el de derecha cualquier cosa
"""

punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])
punto["z"] = 30
punto["lala"] = 20
print(punto)
if "lala" in punto:
    print("encontre lala: ", punto["lala"])

print(punto.get("x"))
print(punto.get("j", "97"))

del punto["x"]  # eliminar
del (punto["y"])  # elimina


for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():  # devuelve tuplas
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "chanchito"},
    {"id": 2, "nombre": "agustina"},
    {"id": 3, "nombre": "paco"},
    {"id": 4, "nombre": "pluma"}
]

for usuario in usuarios:
    print("Nombre: ", usuario["nombre"])

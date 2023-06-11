mascotas = ["pulga", "ramona", "roma", "rolo"]

print(mascotas[1])
mascotas[0] = "Mora"

print(mascotas)
print(mascotas[0:3])
print(mascotas[:3])
print(mascotas[2:])
print(mascotas[-1])  # EL FINAL DE LA LISTA
print(mascotas[::2])  # SALTA DE DOS EN DOS
print(mascotas[1::2])


numeros = list(range(21))
print(numeros)
print(numeros[::2])  # pares // impares == numeros = list(range(1,21))
print(numeros[1::2])  # impares

import math


print(round(1.3))  # te redondea donde este mas cerca (devuelve 1)
print(round(1.7))  # devuelve 2
print(round(1.5))  # devuelve 2

print(abs(-55))  # saca el valor absoluto. devuelve 55

# Phyton no tiene muchas funciones nativas, pero viene con un modulo
# includio de forma nativa que podemos importar, para que podamos trabajar con numeros,
# un modulo es otro archivo que viene con codigo de python. (math.py)

print(math.ceil(1.1))  # devuelve el numero mas cercano para arriba. devuelve 2
# devuelve el numero mas cercano para abajo. devuelve 1
print(math.floor(1.999))
print(math.isnan(1.999))  # Booleano NO es un numero--false
# print(math.isnan("1.999"))
print(math.pow(2, 4))  # eleva a la potencia
print(math.sqrt(9))  # raiz cuadrada

# set = grupo o conjunto
# coleccion de datos que No permiten repetir elementos, y tampooc esta ordenada

primero = {1, 2, 3, 4, 4, 4, 4, 5, 0, 78, 345}
primero.add(6)
primero.remove(4)
print(primero)

segundo = [4, 5, 6, 9, 20, 1]
segundo = set(segundo)

print(primero | segundo)  # UNION
print(primero & segundo)  # INTERSECCION
print(primero - segundo)  # DIFERENCIA (quita los elemntos al primer set)
print(primero ^ segundo)  # DIFERENCIA SIMETRICA

if 5 in segundo:
    print("Hola mundo")

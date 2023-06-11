animal = " chanchito feliz  "
print(animal.upper())
print(animal.lower())
print(animal.strip().capitalize())
print(animal.title())
print(animal.strip())  # Borra los espacio
print(animal.lstrip())  # A la izq.
print(animal.rstrip())

print(animal.find("ch"))
print(animal.find("xv"))
print(animal.replace("ch", "Ya"))

print("ch" in animal)  # Devuelve boolean si esta el string
print("ch" not in animal)

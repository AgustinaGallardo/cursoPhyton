def sinEspacios(text):
    sinEspacio = ""
    for char in text:
        if char != " ":
            sinEspacio += char
    return sinEspacio


def darLaVuelta(text):
    vuelta = ""
    for char in text:
        vuelta = char + vuelta
    return vuelta


def es_palindromo(text):
    text = sinEspacios(text)
    invertida = darLaVuelta(text)
    return text.lower() == invertida.lower()


print("amo la paloma: ", es_palindromo("amo la paloma"))
print("Reconocer", es_palindromo("Reconocer"))
print("Hola Mundo", es_palindromo("Hola Mundo"))
print("Somos o no Somos", es_palindromo("Somos o no Somos"))

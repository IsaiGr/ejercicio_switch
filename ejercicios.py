

def no_space(texto):
    neuvo_texto = ""
    for char in texto:
        if char != " ":
            neuvo_texto += char
    return neuvo_texto
        

def revers(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves.lower() == texto_al_reves.lower()

def es_palindromo(texto):
    texto = no_space(texto)
    texto_alreves = revers(texto)
    print (texto_alreves)

es_palindromo("amo la paloma")
es_palindromo("reconocer")
es_palindromo("somos o no somos")
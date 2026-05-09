meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY": "Algo aterrador o siniestro",
            "ROFL": "una respuesta a una broma",
            "SHEESH": "ligera desaprobación",
            "MAMBO": "Personaje salido de Uma Musume Pretty Derby (nombre real (Matikanetannhauser)"
            }

#No c me ocurre mas :v

nombre = input("hola, ecriba su nombre: ")
print("Mucho gusto", nombre,)
word = input("escriba una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(word + ": " + meme_dict[word])
else:
    print(word + " lo siento, no está en el diccionario.")

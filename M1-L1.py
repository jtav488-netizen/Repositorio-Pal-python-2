colombianadas_dict = {
            "Tinto": "Cafe negro",
            "Parce": "Amigo o compañero",
            "Ñapa": "Regalo extra",
            "Luca": "Mil pesos colombianos"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in colombianadas_dict:
    print(colombianadas_dict[word])

else:
    print("Esa palabra no esta en el diccionario, hijito")

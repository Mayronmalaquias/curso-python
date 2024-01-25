nome = "Curso de Pythom"
valor = range(10)

print(nome)
print(valor)

lista = list(range(10))
print(lista)

lista2 = list("Curso de Pythom")
print(lista2)

lista3 = ["gato", "cachorro", "peixe", "cavalo", "tubarão", "viado"]

elemento = 8

if elemento in lista:
    print("este elemento está dentro da lista")

print(lista3)
lista3[1] = "cavalo"
print(lista3)

lista3[1:4] = ["aguia", "morcego", "elefante"]
print(lista3)

lista3[1] = ["leão", "macaco"]
print(lista3)

lista3[1:4] = ["tubarão"]
print(lista3)


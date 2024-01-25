#index      0       1         2
#lista = ["carro", "barco", "avião"]
#print(lista)

#for x in range(len(lista)):
#    print(x, lista[x])

#texto = "meunome@gmail.com"
#lista2 = list(texto)
#print(lista2)

#texto = texto.split('@')
#lista2 = list(texto)
#print (lista2)

#lista.append(["moto", "bicicleta"]) #função append adiciona elementos ao final da lista
#uma lista dentro de outra lista
#print(lista)

#for x in range(len(lista)):
#    print(x, lista[x])

#lista.insert(1, "bicicleta", "navio") #adiciona valor no index 
#lista.extend(["bicicleta", "navio"]) #elemento adicionado separadamente
#rint(lista)

#tupla = ("item1", "item2")
#print(tupla)
#tupla = ("item3", "item4")
#print(tupla)

tupla = ("item1", "item2")
lista = list(tupla)
print(tupla)
print(lista)
lista.append("item5")
lista.append("item3")
print(lista)
lista.pop()
print(lista)
tupla = tuple(lista)
print(lista)
print(tupla)
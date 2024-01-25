lista = ["carro", "barco", "avião"]
print(lista)

#lista.pop(0) #remove o elemento do index
#lista.remove("barco") #remove o elemento barco

#del lista #deleta a lista
del lista[0]

#carrinho_de_compras = ["pão", "carne", "verduras", "alface"]
#carrinho_de_compras.sort()
# sort #ordenação ordem alfabetica e numeros
#carrinho_de_compras.clear() #apaga todos os elementos mas n apaga a lista
#print(carrinho_de_compras)

#for x in range(len(carrinho_de_compras)):
#    print(x, carrinho_de_compras[x])

lista = [1, 50, 32, 45 , 29]
lista.sort(reverse = True)
#função exemplo lista.reverse seria igual a [29, 45, 32, 50, 1] porem n ordenado
for x in range(len(lista)):
    print(x, lista[x])
lista2 = ["Ana", "Pedro", "Marta", "Clarice", "beatriz"]
print(lista2)
lista2.sort()
print(lista2)

#lista.extend(lista2)
#print(lista)

#lista = lista + lista2

#for x in lista2:
#    lista.append(x)
#print(lista)
print(lista)
lista3 = lista.copy() #copia de forma independente
#lista3 = lista
print(lista3)

lista3.append("d")
lista.append("e")
print(lista)
print(lista3)
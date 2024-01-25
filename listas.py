

lista = ["chicago", "queens", "salvador", "pernambuco"]
print(lista)

lista2 = [2, 3, 7, 8, 10]
print(lista2)

lista3 = [2.0, 3.5, 6,3]
print(lista3)

lista2 = lista2 + lista3
print(lista2)

lista4 = [True, False]
print(lista4)
#index    -5     -4        -3    -2   -1
#index     0      1         2     3    4    = 5 elementos
lista5 = [True, "chicago", 2.5, False, 4]
print(lista5)

print(type(lista5)) #class 'list' - tipo de dado interavel possui index
#listas são um dos 4 tipos de dados incluido em pythom

print(lista5[1]) #chicago
print(lista5[-1]) # elemento 4

#Slicing

print(lista5[::]) #imprime tudo
print(lista5[1:]) #ignora o index 1 até o fim da lista
print(lista5[2:]) #ignora o index 2 até o fim da lista
print(lista5[:3]) # retorna do começo da lista até o index -1
print(lista5[1:4]) #retorna do index destacado até o index -1
print(lista5[1:4:2])#retorna do index destacado até o index -1 em 2 em 2
print(len(lista)) #len = tamanho da lista
nome5 = "Mayron"

#Funções que só conseguem ser utilizados com tipos de dados numericos

print(sum(lista2)) #somatoria dos elementos das listas
print(max(lista2)) #elemento de maior valor na lista
print(min(lista2)) #elemento com menor valor na lista

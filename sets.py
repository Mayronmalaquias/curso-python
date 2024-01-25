#Listas: Coleção ordenada, mutável e que permite valores duplicados
#Tuplas: Coleção ordenada, imutavel e que permite valores duplicados
#Dicionario: Coleção não ordenada, mutável e que não permite valores duplicados
#sets: coleção não ordenada, imutável e que não permite valores duplicados

#os sets tambem são conhecidos como conjuntos

#conjunto = {"item1", "item2", "item3"}
#print(type(conjunto))
#print(conjunto)
#print(len(conjunto))

#tupla = (3, 7, 9, 5)
#conjunto = set(tupla) #eh igual a conjunto = set((3, 7, 9, 5))
#print(conjunto)
#conjunto = {3, 7, 9, 5}
#for x in conjunto:
#    print(x)

#set1 = {"item1", "item2", "item3"}
#print(set1)
#set1.add("item5")
#print(set1)
#set1.add(8)
#set1.add(True)
#print(set1)

#adicionou elementos

#set1 = {4, 5, 7, 8, 9, 1}
#set2 = {"item3", "item5", "item1"}
#set1.update(set2) #aceita listas tb set1.update([1,2,3,4,4,5,6, "item1"])
#print(set1)

#removendo elementos

#set1 = {4, 5, 7, 8, 9, 1, "item3", "item5", "item1"}
#set1.pop() remove "aleatiorio um  numero"
#set1.remove("item1") #se remover um item q n existe acontece um erro
#set1.discard("item5") #se remover um item q n existe n acontece um erro
#print(set1)
#set1.clear() #esvazia o set
#print(set1)

#Union, different funções principais dos sets

#conjunto1 = {1, 2, 3, 4, 5}
#conjunto2 = {6, 7, 8, 9, 0}#
#conjunto3 = conjunto1.union(conjunto2) #união do conjunto 1 com o 2
#print(conjunto3)

#conjunto1 = {1, 2, 3, 4, 5}
#conjunto2 = {1, 7, 3}
#conjunto3 = conjunto1.intersection(conjunto2) #ou conjunto1.intersection_update
#print(conjunto3) #print(conjunto1)

conjunto1 = {1, 2, 3, 4}
conjunto2 = {1, 7, 3}
conjunto3 = conjunto1.symmetric_difference(conjunto2) # ou conjunto1.symmetric_difference_update(conjunto2)
print(conjunto3)
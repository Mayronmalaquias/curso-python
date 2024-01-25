#Listas: Coleção ordenada, mutável e que permite valores duplicados
#Tuplas: Coleção ordenada, imutavel e que permite valores duplicados
#Dicionario: Coleção não ordenada, mutável e que não permite valores duplicados

#chave:valor
dicio = {"chave1": "Gabriel", "Chave2": "1993", "chave3": True}

#index    0        1
lista =["item1", "item2"]
tupla = ("item1", "item2")

print(dicio)

dicionario = {    #outra fomra de declarar
    "nome": "bruna",   #não pode ter 2 valores em uma chave
    "idade" : 27,
    "nacionalidade" : "brasileira"
}

print(dicionario)
print(dicionario["nome"])
print(dicionario.get("idade")) #outra forma de declarar

print(dicionario.keys())
print(len(dicionario))
print(dicionario.values())

if "idade" in dicionario:
    print("A chave idade existe")

print(dicionario.items())
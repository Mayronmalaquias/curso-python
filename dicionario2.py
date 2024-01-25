#index     0         1
lista = ["item1", "item2"]
tupla = ("item1", "item2")

#chave : valor
dados = {"nome" : "Gabriel", "ano" : 1993, "valor_logico": True}
print(dados)
dados["nome"] = "pedro"
print(dados)

dados.update({"nome":"ana"})
print(dados)

dados.update({"estado":"Rio de janeiro"})
print(dados)

#dados.popitem() #elimina ultimo item do dicionario apenas da versão 3.7 e acima
#print(dados)

#dados.pop("valor_logico") #remove item expecifico 
#print(dados)

#del dados["ano"] #del deleta variavel
#print(dados)

#dados.clear() #apaga todos os items
#for x in dados:
#    print(dados[x])

#for x in dados.values():
#    print(x)
#for x in dados.keys():
#    print(x)
#for x, y in dados.items():
#    print(x, y)
dicio = dados.copy()
print(dicio)

dicio2 = dict(dados)
print(dicio2)
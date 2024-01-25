#Argumentos Arbitrario *atgs - Essa função recebe argumentos que serão atribuidos em uma tupla

def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem = None, *telefones):
    print("-"*30)
    print("Titulo: ", nomeImovel)
    print("Quartos: ", n_quartos)
    if vagasGaragem != None:
        print("Vagas na garagem: ", vagasGaragem)
    print("telefones: ", telefones)

imprimir_imovel("Loja comercial", 2, 5, "61 5555-5555", "21 55555- 55555")


def imprimir_nomes(*nomes):
    print(nomes)


lista = ["ana", "beatriz", "pedro", "joao"]
imprimir_nomes(*lista) #desempacota a lista e transforma em tupla
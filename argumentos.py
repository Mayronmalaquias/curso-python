#Argumentos nomeados

#def imprimir_nome(nome, sobrenome, idade):
#    print("nome:", nome)
#    print("sobrenome", sobrenome)
#    print("idade", idade)


#sobrenome = "clara"
#idade = 25
#imprimir_nome(nome = "maria", sobrenome = sobrenome, idade = idade)

#parametro padrão define argumentos não obrigatorios

#def imprimir_nome(nome = "nome", sobrenome = "sobrenome", idade= "idade"):
#    print("nome:", nome)
#    print("sobrenome:", sobrenome)
#    print("idade:", idade)


#def imprimir_nome(nome = None, sobrenome = None, idade= None):  #None para opcional
##    if nome != None:
#        print("nome:", nome)
#        print("sobrenome:", sobrenome)
#        print("idade:", idade)
#        print("-"*30)
 #   else:
 #       print("Insira seus dados")
 #       print("-"*30)


#print()
#imprimir_nome()
#imprimir_nome("maria", "clara", 35)

def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem = None):
    print("-"*30)
    print("Titulo: ", nomeImovel)
    print("Quartos: ", n_quartos)
    if vagasGaragem != None:
        print("Vagas na garagem: ", vagasGaragem)


print()
#Exemplos de nº de argumentos <0 nº dos parametros
imprimir_imovel("Casa 3 quartos = SP", 3)
imprimir_imovel("Apartamentos = MG", 2, 1)
#exemplo de nº de argumentos > nº dos parametos
#imprimir_imovel("Loja comercial", 2, 5, "desconto")


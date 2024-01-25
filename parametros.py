#parâmetros de uma função

#def minha_funcao(): #função sem parametro
#    var = "maria"
#    return var


#var = minha_funcao()
#print(var)

def nome_da_funcao(parametro): #parametro é o nome dado aos valores utilizados na definição de uma função
    #corpo da função
    print("ola ", parametro)


nome = input("qual o seu nome?\n")
nome_da_funcao(nome) #argumento é o nome dado aos valores utilizados na chamada de uma função

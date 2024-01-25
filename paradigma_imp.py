#paradigma imperativo
#não citada por ser natural 
#imperare - comandar

#Caracteristicas - variaveis, atribuições e sequencia
#C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2

#bloco externo
nome = "Gabriel" #variavel global
#def é usado para criar funções

def minha_funcao():
    #bloco interno *bloco interno de uma função é conhecido como corpo da função
    #variavel local
    nome = "Ana"
    tupla = 2, 3, 5, 7, 9
    print(nome)
    print(tupla)
    if nome == "Ana":
        print("impressão do bloco interno da condição if")
    for x in tupla: 
        print(x)


minha_funcao()
print(nome)




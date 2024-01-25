#Argumentos arbitrario **Kwargs - Keyword arguments
#Essa função recebe argumentos que serão atribuidos em um dicionario

def imprimir_nome(nomes):
    print(f"{nomes['nome']} {nomes['sobrenome']}")


dicio = {'nome' : 'ana', 'sobrenome': 'julia'}
imprimir_nome(dicio)

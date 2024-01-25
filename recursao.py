#Função recursiva
numeroInt = 5

#def reduzirnumero(numeroInt):
#    while numeroInt > 0:
#        print(numeroInt)
#        numeroInt -= 1

#reduzirnumero(10)

#1º - Checar se o nosso numero não é igual a 0
#2º - se ele não for igual a 0 - reduzie 1 unidade
#5
# 4 (5 - 1)
#  3 (4 - 1)
#   2 (3 - 1)
#    1 (2 - 1)
#     0 (1 - 1) e fechou

#def reduzirNumero(numeroInt):
#    print(numeroInt)
#    if numeroInt > 0:
#        # N - 1
#        reduzirNumero(numeroInt - 1)


#retorno = reduzirNumero(5)
#print(retorno)

#fatorial sem recursão
def fatorialS(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for x in range(1, numero + 1):
            fatorial *= x
        return fatorial 
    

print(fatorialS(3))

#Fatorial - solução recursiva

def fatorialR(numero):
    if numero == 0: #Criterio de parada
        return 1
    else:
        # Parâmetro da chamada recursiva
        return numero * fatorialR(numero - 1)
    

print(fatorialR(3))

#3! = 3*2*1
#   = 3*2!
#   = 3*2*1!
#2! = 2*1
#   = 2*1
#1! = 1
#0! = 1
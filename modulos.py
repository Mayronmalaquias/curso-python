#import primo

#print(primo.primo(9))
#import random 1º forma
#from random import choice 2 º forma
#from random import ( random,choice) 3 º forma
#import random as rd 4º forma

#print(random())

#lista = ["pedra", "papel", "tesoura"]
#print(choice(lista))

#from random import ( random as rd,choice as ch)
#lista = ["pedra", "papel", "tesoura"]
#print(rd.random())
#print(ch.choice(lista))

#from random import *
#print(randint(1,5))

#   Modulos - arquivos com extensão .pt - ou seja - arquivos python
#   Pacotes - diretorios contendo um conjunto de modulos - pastas com varios arqiovos python

#from pacote.sub_diretorio import outro as modulo

#print(modulo.cubica(3))

from pacote.sub_diretorio.outro import cubica

print(cubica(2))
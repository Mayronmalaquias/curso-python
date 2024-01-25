#estruturas de repetição - loops em python
#while
#for
#do while* não existe do while em python

#WHILE

#a = 0
#while a <= 5:
#    print(a)
#    print(a <= 5)
#    a = a + 1
#else: 
#    print(f"a não eh menor ou igual a 5, valor de a: {a}")

#   if a == 3:
#       break #quebra o loop

#FOR é diferente das outras linguagens

#s = "pernambuco"

#for x in s: #verificou se x estava em s e imprimiu de P a 0
#    print(x)

#for x in range(6): #range(6) significa que começamos do 0 até temos 6 digitos
#    print(x)

#for x in range(5,8):
#    print(x)

#for x in range(2,10,3):
#    print(x)

#for x in range(6): #for (x=0; x<=5;x++)
#    print(x)
#else:
#    print("chegamos ao fim")

#DO WHILE EM PYTHON
#CODIGO PARA ADIVINHAR NUMERO

from random import randint

palpite = 5
numero = randint(1, 10)

#print("Qual o numero correto?")
#palpite = int(input())

while True: #condições sempre verdadeira se assemelhando ao do while
    palpite = int(input("chute um numero!\n"))
    if palpite == numero: #verificando o codigo
        print("parabens vc acertou")
        break
    else:
        print("vc errou!")
else: #erro para o programador caso haja erro no sistema
    print("erro na aplicação") #usuario n ve essa impressão
    print(bool(palpite))

#print(bool(palpite)) #False
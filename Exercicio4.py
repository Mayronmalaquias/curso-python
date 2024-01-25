#Exercicio 1

#def MaiorMenor(X, Y):
#    if X > Y:
#        print(f"{X} é maior que {Y}")
#    elif X < Y:
#        print(f"{Y} é maior que {X}")
#    else:
#        print(f"{X} é igual a {Y}")
#
#def MediaAritimetica(X, Y):
#    media = (X + Y) / 2
#    return media
#
#x = float(input("Digite o valor de X: "))
#y = float(input("Digite o valor de Y: "))
#MaiorMenor(x,y)
#media = MediaAritimetica(x, y)
#print(f"A media aritimetica deles eh {media}")

#EXERCICIO 2 

#def potencia(base, expoente):
#    if expoente == 0:
#        return 1
#    else:
#        return base * potencia(base, expoente - 1)


#print(potencia(3, 0))
#4 ---- 3
# 4 * 4 * 4

#Exercicio 3


def potencia():
    print("Dgite valores de 0 a 9")
    numero = int(input("digite o valor do numero: "))
    numero *= numero
    print(f"valor da potencia eh {numero}")


def raiz():
    print("Dgite valores de 0 a 9")
    numero = int(input("digite o valor do numero: "))
    numero **= 0.5     # raiz de y = x // y = x^2
    print(f"valor da raiz eh {numero}")


def divisão_por_x():
    print("Dgite valores de 0 a 9")
    numero = int(input("digite o valor do numero: "))
    numero = 1 / numero
    print(f"a divisão de 1 pelo numero eh {numero}")


def soma():
    print("Dgite valores de 0 a 9")
    numero = int(input("digite o valor do 1º numero: "))
    numero2 = int(input("digite o valor do 2º numero: "))
    numero += numero2
    print(f"valor da soma eh {numero}")


def subtracao():
    print("Dgite valores de 0 a 9")
    numero = int(input("digite o valor do 1º numero: "))
    numero2 = int(input("digite o valor do 2º numero: "))
    numero -= numero2
    print(f"valor da subtração eh {numero}")


def multiplicacao():
    print("Dgite valores de 0 a 9")
    numero = int(input("digite o valor do 1º numero: "))
    numero2 = int(input("digite o valor do 2º numero: "))
    numero *= numero2
    print(f"valor da multiplicação eh {numero}")


def divisão():
    print("Dgite valores de 0 a 9")
    numero = int(input("coloque o valor do dividendo: "))
    numero2 = int(input("coloque o valor do divisor: "))
    numero /= numero2
    print(f"valor da divisão eh {numero}")


def resto():
    print("Dgite valores de 0 a 9")
    numero = int(input("coloque o valor do dividendo: "))
    numero2 = int(input("coloque o valor do divisor: "))
    numero %= numero2
    print(f"O resto da divisão eh {numero}")


while True:
    print("Bem vindo a calculadora")
    print("nessa calculadora nos calculamos: potencia, soma, subtracao, raiz, multiplicacao, divisao, divisao_por_x, restp")
    operacao = input("fale que operação você deseja fazer: ")
    operacao = operacao.lower()
    if operacao == "potencia":
        potencia()
    elif operacao == "soma":
        soma()
    elif operacao == "subtracao":
        subtracao()
    elif operacao == "raiz":
        raiz()
    elif operacao == "subtracao":
        subtracao()
    elif operacao == "multiplicacao":
        multiplicacao()
    elif operacao == "divisao":
        divisão()
    elif operacao == "divisao_por_x":
        divisão_por_x()
    elif operacao == "resto":
        resto()
    else:
        print("Operação invalida")
        pass
    opcao_jogador = input("Continuar a calculadora? ")
    if opcao_jogador in ["Sim", "sim", "S", "s", "SIM"]:
        pass
    else:
        break

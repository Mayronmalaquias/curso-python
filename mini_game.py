import random #importando um função para gerar numeros aleatorios entre 0 e 2


def vencedor(x, y):
    if x == "pedra":
        if y == "pedra":
            return "empate"
        elif y == "papel":
            return "derrota"
        elif y == "tesoura":
            return "vitoria"
    elif x == "papel":
        if y == "pedra":
            return "vitoria"
        elif y == "papel":
            return "empate"
        elif y == "tesoura":
            return "derrota"
    elif x == "tesoura":
        if y == "pedra":
            return "derrota"
        elif y == "papel":
            return "vitoria"
        elif y == "tesoura":
            return "empate"


while True:
    print("Vamos jogar pedra papel ou tesoura")
    jogada = input("De o seu fale sua jogada:")
    jogada.lower()
    if jogada != ("pedra", "papel", "tesoura"):
        print("valor invalido")
        continue
    maquina = random.randint(0, 2)
    if maquina == 0:
        valor = "pedra"
    elif maquina == 1:
        valor = "papel"
    elif maquina == 2:
        valor = "tesoura"
    print("maquina jogou:", valor)
    retorno = vencedor(jogada,valor)
    print(retorno)


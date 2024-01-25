from random import choice

jogador_vitoria = 0
maq_vitoria = 0

def Opcao_Jogador():
    esc_jogador = input("Escolha Pedra, Papel ou Tesoura: ")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador 
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        Opcao_Jogador()


def Opcao_Maquina():
    esc_maquina = choice(["pedra", "papel", "tesoura"])
    return esc_maquina


while True:

    print("-"*30)
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maquina()
    print("-"*30)

    if(esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra") \
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
        print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina}" 
              "Resultado: Voce ganhou")
        jogador_vitoria += 1
    elif esc_jogador == esc_maquina:
        print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina}" 
              "Resultado: Empate")
    else:
        print(f"Jogador escolheu {esc_jogador} e a maquina escolheu {esc_maquina}" 
              "Resultado: Voce perdeu")
        maq_vitoria += 1
        

    print("-"*30)
    print(f"Vitoria do jogador: {jogador_vitoria}")
    print(f"vitorias maquina {maq_vitoria}")
    print("-"*30)

    esc_jogador = input("Voce quer joga novamente?: ")
    if esc_jogador in ["SIM", "sim", "Sim", "s", "S"]:
        pass
    elif esc_jogador in ["NAO", "nao", "Nao", "n", "N"]:
        break
    else: 
        break
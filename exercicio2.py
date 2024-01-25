#Implemente um programa que receba a idade de uma pessoa e imprima mensagem de
#acordo com os critérios:
idade = input("Quantos anos vc tem?\n")
if int(idade) < 16:
    print("Menor de idade")
elif int(idade) <= 7:
    print("Infantil A")
elif int(idade) <= 10:
    print("Infantil B")
elif int(idade) <= 13:
    print("Infantil C")
elif int(idade) <= 17:
    print("Infantil D")
elif int(idade) <= 18:
    print("emancipado")
elif int(idade) > 18:
    print("de maior")

#Pratica02
idade = input("Quantos anos vc tem?\n")
if int(idade) <= 7:
    print("Infantil A")
elif int(idade) <= 10:
    print("Infantil B")
elif int(idade) <= 13:
    print("Infantil C")
elif int(idade) <= 17:
    print("Infantil D")


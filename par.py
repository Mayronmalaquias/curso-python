#COMO DESCOBRIR SE VALOR É IMPAR OU PAR

while True:
    print(20 * "-")
    numero = int(input("Qual o numero desejado?\n"))

    if numero % 2 == 0:
        print(f'numero {numero} eh par')
    else:
        print(f'numero {numero} eh impar')
    
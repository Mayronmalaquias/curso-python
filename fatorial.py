#fatorial de um numero

numero = int(input("Digite um numero inteiro para o fatorial!\n"))
fatorial = numero
if numero < 0:
    print("fatorial negativo n existe")
elif numero == 0:
    print("fatorial de 0 é 1 ")
else:
    for x in range(1, numero + 1):
        fatorial *= x



#numero1 = numero
#valor = numero1
#if numero < 0:
#    print("fatorial negativo n existe")
#elif numero == 0:
#    print("fatorial de 0 é 1 ")
#else:
#    while numero1 > 1:
#        valor = valor * (numero1 -1)
#        numero1 = numero1 - 1
#        print (f"{numero1 + 1} x {numero1} = {valor}")
#    print(f"o numero {numero}! eh:  {valor}")


# 3 x 2 x 1
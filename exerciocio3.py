#Escreva um programa que leia 5 valores e encontre o maior e o menor deles. Mostre o
#resultado.

a = int(input("Digite o 1º valor: "))

variavel_nula = a
var = a

for x in range (2, 6):
    valor = int(input(f"Digite o {x}º valor: "))
    if (variavel_nula < valor):
        variavel_nula = valor
    elif var > valor:
        var = valor
print(f"valor maior eh {variavel_nula} e valor menor eh {var}")

S = 3/40 + 32 /39 + 33 /38 + 34 /37 + 340/1
print(S)

S = 480/2 + 475/22 + 470/23 + 465/24 + 460/25
dendo = 460
sor = 25
for x in range(20):
    dendo -= 5
    sor += 1
    divde = dendo / sor
    S += divde
print(S)

S = 1/2 + 3/23 + 7/25 + 15/27 + 31/29
dedo = 31
sor = 29
for x in range(15):
    dendo = (dendo * 2) + 1
    sor = sor + 2
    div = dendo / sor
    S += div
print(S)

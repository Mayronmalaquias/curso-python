
#   idx 0123456
nome = input("Digite um numero\n")

troca = ""
print(nome[4])
tamanho = -1

for x in nome:
    tamanho += 1
print(tamanho)

for x in range(tamanho, -1, -1):
    troca += nome[x]
print(troca)

for x in nome:
    print (x, end=" ") #A função end coloca um caracter no final de outro por exemplo v[x] = a // x, end = "H" = aH

x = 5
y = 0
x, y = y, x
print(x)
print(y)
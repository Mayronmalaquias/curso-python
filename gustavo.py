
# Escreva um programa que leia 5 valores
# e ordene decrescentemente esse valores

valores = []

for x in range(5):
    valor = float(input(f"Digite o {x+1}° valor:"))
    valores.append(valor)
valores.sort(reverse=True)

print("Valores em ordem decrescente:")
for valor in valores:
    print(valor)


alfabeto = []
for y in range(5):
    letra = str(input(f"digite o {y+1} valor: "))
    alfabeto.append(letra)
alfabeto.sort(reverse=True)# Ordenando decrescentemente

print("Valores em ordem decrescente:")
for letra in alfabeto:
    print(letra)    
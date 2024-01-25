#maiuculas e minusculas
#simbolos e espaços

#Security = chave
#5ecurt1ty = senha
#regra dos hexadecimais

chave = input("digite a base da sua senha")

senha = ""
for letra in chave:
    if letra in "Aa": senha = senha + "1"
    elif letra in "Bb": senha = senha + "@"
    elif letra in "Cc": senha = senha + "2"
    elif letra in "Dd": senha = senha + "3"
    elif letra in "Ee": senha = senha + "4"
    elif letra in "Ff": senha = senha + "5"
    elif letra in "Rr": senha = senha + "#"
    elif letra in "Ss": senha = senha + "%"
    elif letra in "Mm": senha = senha + "$"
    else: senha = senha + letra
print(senha)
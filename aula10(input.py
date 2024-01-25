#função imput() - função para receber do usuario

#primeira forma:

print("Qual o seu nome?")
nome = input()
print("seu nome é ", nome)
#ou

idade = input("Qual a sua idade?")
print("sua idade eh ?", idade)

#segunda forma

nome = input("qual é o seu nome? ")
idade = input("qual a sua idade? ")

print("seu nome eh: {0} e sia idade eh {1}".format(nome,idade)) #uso format para ler nome(string)

#terceira forma:

nome = input("qual é o seu nome?")
idade = input("qual a sua idade?")

print (f"seu nome é {nome} e sua idade é {idade}") #uso format para ler nome(string) porem dessa vez eu uso f antes oq torna o codigo mais limpo!

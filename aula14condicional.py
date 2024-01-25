#Comandos condicional

# if, else e elif -> (else if)

#x = 8
#y = 8

#if y > x:
#    print("y eh maior que x")
#    print("Codigo dentro no codigo condicional if")
#else:    
#    print("y eh menor ou igual a x")
#elif y < x:
#    print("y eh menor que x")
#elif y == x:
#    print("y eh igual a x")    
#print("Codigo fora do bloco condicional")
#print(y>x)

a = 9
b = 8
c = 2

#if b > a: print("b eh maior que a") -> encurtação
#print("codigo fora do bloco")

#print("B") if b > a else print("A") #Operador ternario em python // expressões condicionais

if a > b:  #Alinhamento de if
    if a > c:
        print("A eh maior que b e c")
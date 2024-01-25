tupla = ("item1",)
tupla2 = ("item2", "item3", "item4")
tupla = tupla + tupla2 #concatenação de tuplas
print(tupla)

#(x, y, z)= tupla
#print(x, y , z)

(x, *y, z) = tupla #x recebe item1 e y recebe o resto
print(x)
print(y)
print(z)

#for variavel in tupla: #imprime atributos
#    print(variavel)

#for x in range(len(tupla)): #imprime index
#    print(x, tupla[x])
notas=[0,0,0,0,0,0,0] 
soma=0
x=0
while x<7:
    notas[x]=float(input("Nota %d:" % x))
    if notas[x]<0 or notas[x]>10:
        while notas[x]<0 or notas[x]>10:
            print("Nota inválida, digite novamente")
            notas[x]=float(input("Nota %d:" % x))           
    soma += notas[x]
    x+=1
x=0 
while x<7: 
    print("Nota %d: %6.2f" % (x, notas[x]))
    x+=1
print("Média: %5.2f" % (soma/x))
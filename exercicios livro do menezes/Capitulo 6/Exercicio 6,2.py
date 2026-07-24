lista_um = []
lista_dois = []
x = 0
while x < 5:
    valor = int(input("Digite um valor para a lista um: "))
    lista_um.append(valor)
    x += 1
x = 0
while x < 5:
    valor = int(input("Digite um valor para a lista dois: "))
    lista_dois.append(valor)
    x += 1
print("A lista tres é %s" % (lista_um + lista_dois))

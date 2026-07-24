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
x = 0
lista_tres = []
x = 0
while x < len(lista_um):
    if lista_um[x] not in lista_tres:
        lista_tres.append(lista_um[x])
    x += 1

x = 0
while x < len(lista_dois):
    if lista_dois[x] not in lista_tres:
        lista_tres.append(lista_dois[x])
    x += 1

print("Lista três sem repetidos:", lista_tres)
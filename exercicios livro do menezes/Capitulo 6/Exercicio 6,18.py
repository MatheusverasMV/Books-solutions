L = {}
while True:
    chave = input("Digite a chave (fim para sair):")
    if chave == "fim":
        break
    valor = input("Digite o valor:")
    L[chave] = valor
print("Dicionário:\n")
for chave, valor in L.items():
    print("Chave: ", chave + " - Valor: ", valor)
print(L)
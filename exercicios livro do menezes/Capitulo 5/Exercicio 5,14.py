soma = 0
quantidade = 0
while True:
    n = int(input("Diga o numero para somar(digite 0 para sair):"))
    if n == 0:
        break
    soma = soma+n
    quantidade = quantidade+1
print("Quantidade de números digitados:", quantidade)
print("Soma: ", soma)
print(f"Média: {soma/quantidade:1.2f}")

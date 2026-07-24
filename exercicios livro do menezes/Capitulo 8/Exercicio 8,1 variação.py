def maior(a, b):
    if a < b:
        return b
    else:
        return a
L = []
while True:
    num1 = int(input("Digite o primeiro numero (ou digite 0 para sair): "))
    if num1 == 0:
        break
    else: 
        num2 = int(input("Digite o segundo numero: "))
        L.append([num1, num2])
        
for par in L:    
    print(f"O maior entre {par[0]} e {par[1]} é: {maior(par[0], par[1])}")
    
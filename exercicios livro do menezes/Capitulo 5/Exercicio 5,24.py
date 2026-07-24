quantidade_primos = int(input("Digite a quantidade de números primos que deseja exibir: "))
if quantidade_primos < 0:
    print("Número inválido. Digite apenas valores positivos")
else:
    if quantidade_primos >= 1:
        print(2)
    primos_gerados = 1
    proximo_primo = 3
    while primos_gerados < quantidade_primos:
        é_primo = True
        divisor = 2
        while divisor <= proximo_primo // 2:
            if proximo_primo % divisor == 0:
                é_primo = False
                break
            divisor += 1
        if é_primo:
            print(proximo_primo)
            primos_gerados += 1
        proximo_primo += 2

km_percorrido = int(input("Diga a quantidade de quilometro percorridos: "))
dias = int(input("Diga a quantidade de dias alugados: "))
print("O valor a pagar é R$ %3.2f"%(dias*60+0.15*km_percorrido))
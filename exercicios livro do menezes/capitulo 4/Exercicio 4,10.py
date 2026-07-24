kwh = int(input("Diga a quantidade de kWh consumido: "))
instalaçao = input("É uma instalação industrial(i), residencial(r) ou comercial(c): ")

if instalaçao == "r":
    if kwh <=500:
        print(f"Você deve pagar R$ {kwh*0.4}")
    else:
        print(f"Você deve pagar R$ {kwh*0.65}")
elif instalaçao == "i":
    if kwh <= 5000:
        print(f"Você deve pagar R$ {kwh*0.55}")
    else:
        print(f"Você deve pagar R$ {kwh*0.6}")
elif instalaçao == "c":
    if kwh <=1000:
        print(f"Você deve pagar R$ {kwh*0.55}")
    else:
        print(f"Você deve pagar R$ {kwh*0.6}")
else:
    print("Você selecionou uma opção não validade")


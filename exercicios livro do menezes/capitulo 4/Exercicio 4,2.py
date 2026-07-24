velocidade = int(input("Qual é a velocidade do carro: "))
if velocidade > 80:
    multa = (velocidade-80)*5
    print("Você foi multado em R$ %3.2f"%multa)
if velocidade < 80:
    print("Você não foi multado.")    
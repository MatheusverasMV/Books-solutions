valor_casa = float(input("Informe o valor da casa: "))
salario = float(input("Informe seu salario: "))
anos_pagar = int(input("Diga em quantos anos pretende pagar: "))

if salario*0.3 < (valor_casa/(anos_pagar*12)):
    print("Seu salario é insuficiente para aprovar o emprestimo nesse periodo, aumento o periodo para ter chance de empresto!")
    print((valor_casa/(anos_pagar*12)))

else:
    print("Sua prestação será de R$ %6.2f por mês" %(valor_casa/(anos_pagar*12)) )


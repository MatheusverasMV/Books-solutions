divida = float(input("Qual é o valor da divida: "))
taxa = float(input("Qual é o juros mensal: "))
pagamento = float(input("Qual é o valor mensal pago: "))
mes = 1
if divida*(taxa/100)>pagamento:
    print("Sua divida nunca será paga pois os juros são maiores que o pagamento")
else:
    saldo = divida
    juros_pago = 0
    while saldo >pagamento:
        juros = saldo*taxa/100
        saldo=saldo+juros-pagamento
        juros_pago=juros+juros_pago
        print(f"Saldo da dívida no mês {mes} é de R${saldo:6.2f}.")
        mes = mes+1
    print(f"Para pagar uma dívida de R${divida:8.2f}, a {taxa:5.2f} % de juros,")
    print(
        f"você precisará de {mes - 1} meses, pagando um total de R${juros_pago:8.2f} de juros."
    )
    print(f"No último mês, você teria um saldo residual de R${saldo:8.2f} a pagar.")
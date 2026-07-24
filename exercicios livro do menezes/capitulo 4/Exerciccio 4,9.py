valor_casa = int(input("Diga o valor da casa a comprar: "))
salario = int(input("Diga o seu salario: "))
anos = int(input("Diga os anos a pagar: "))
prestação = valor_casa/(12*anos)
if prestação > 0.3*salario:
    print("O emprestimo não foi aprovado")
else:
    print("O emprestimo  foi aprovado")
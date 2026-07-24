num1 = float(input("Diga o primeiro numero: "))
num2 = float(input("Diga o segundo numero: "))
operaçao = input("Você quer somar, multiplicar, dividar ou subtrair: ")
if operaçao == "somar":
    print(f'a soma é {num1+num2}')
elif operaçao == "subtrair":
    print(f'a subtração é {num1-num2}')
elif operaçao == "dividir":
    print(f'a divisão é {num1/num2}')
elif operaçao == "multiplicar":
    print(f'a multiplicação é {num1*num2}')
else:
    print("Operação invalidade")
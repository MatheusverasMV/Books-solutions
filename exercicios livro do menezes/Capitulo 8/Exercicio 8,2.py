def multiplo(a, b):
    if a % b == 0:
        return f"{a} é múltiplo de {b}"
    else:
        return f"{a} não é múltiplo de {b}"

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(multiplo(num1, num2))
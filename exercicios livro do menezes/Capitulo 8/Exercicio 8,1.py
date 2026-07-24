def ordinalidade(a, b):
    if a < b:
        return f"{b} é maior que {a}" 
    elif a > b:
        return f"{a} é maior que {b}"
    else:
        return f"{a} é igual a {b}"
    
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
print(ordinalidade(num1, num2))
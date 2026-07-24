def area_triangulo(base, altura):
    return (base * altura) / 2

a = float(input("Digite a base do triângulo: "))
b = float(input("Digite a altura do triângulo: "))
print(f"A área do triângulo é: {area_triangulo(a, b)}")
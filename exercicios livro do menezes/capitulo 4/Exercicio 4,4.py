salario = int(input("Qual é o seu salario: "))
if salario >1250:
    aumento = salario*0.1
    print(f'seu aumento foi de R${aumento}')
    print(f'seu salario atual é R${salario+aumento}')
else:
    aumento = salario *0.15
    print(f'seu aumento foi de R${aumento}')
    print(f'Seu salario atual é R${salario+aumento}')

n = int(input("Tabuada de: "))
inicio =int(input("Inicio da tabuada: "))
fim = int(input("Fim da tabuada: "))
x = inicio
while x <= fim:
    print(f'{n} x {x}= {n*x}')
    x=x+1
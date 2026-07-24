distancia = int(input("Qual é a distancia que vocÊ vai percorrer(em Km): "))
if distancia <= 200:
    print("A passagem é R$%6.2f" %(distancia*0.5))
else:
    print("A passagem é %6.2f"%(distancia*0.45))

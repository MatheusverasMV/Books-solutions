import random
n=random.randint(1,10)
i = 1
while i <= 3:
    x=int(input("Escolha um número entre 1 e 10: "))
    if (x==n):
        print("Você acertou!")
        break
    else:
        print("Você errou.")
    i += 1

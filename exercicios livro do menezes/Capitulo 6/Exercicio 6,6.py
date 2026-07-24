último = 10
fila_um = list(range(1, último + 1))
fila_dois = list(range(1, último + 1))
while True:
    print(f"\nExistem {len(fila_um)} clientes na fila um e {len(fila_dois)} clientes na fila dois")
    print("Fila um atual:", fila_um)
    print("Fila dois atual:", fila_dois)
    print("Digite F para adicionar um cliente ao fim da fila um e G para a fila dois,")
    print("ou A para realizar o atendimento na fila um e B para o atendimento na fila dois. S para sair.")
    operação = input("Operação (F ou G, A ou B ou S):").upper()
    x = 0
    sair = False
    while  x < len(operação):
        if operação == "A":
            if len(fila_um) > 0:
                atendido = fila_um.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação == "B":
            if len(fila_dois) > 0:
                atendido = fila_dois.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação == "F":
            último += 1  # Incrementa o ticket do novo cliente
            fila_um.append(último)
        elif operação == "G":
            último += 1  # Incrementa o ticket do novo cliente
            fila_dois.append(último)
        elif operação == "S":
            sair = True
            break
        else:
            print(
                f"Operação inválida: {operação[x]} na posição {x}! Digite apenas F, A ou S!"
            )
        x = x + 1
    if sair == True:
        break
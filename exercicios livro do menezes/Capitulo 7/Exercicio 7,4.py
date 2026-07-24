string = "TTAAC"
vistos = []

for i in string:
    if i not in vistos:
        qtd = string.count(i)
        print(f"Caractere '{i}' aparece {qtd} vezes")
        vistos.append(i)
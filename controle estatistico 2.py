lista = [
    498, 501, 500, 503, 499, 502,
    500, 497, 501, 502, 499, 500,
    501, 498, 500, 502, 499, 503
]

frequencia = {}

for elemento in lista:
    if elemento in frequencia:
        frequencia[elemento] += 1
    else:
        frequencia[elemento] = 1

for elemento in sorted(frequencia):
    print(elemento, ":", frequencia[elemento])
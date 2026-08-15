import matplotlib.pyplot as plt
import statistics as stats

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

print("Media:", stats.mean(lista))
print("Mediana:", stats.median(lista))
print("Moda:", stats.mode(lista))
print("Desvio Padrão:", stats.stdev(lista))
print("Amplitude:", max(lista) - min(lista))

# Gráfico de barras
plt.bar(frequencia.keys(), frequencia.values())
plt.title("Frequência dos Valores")
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.xticks(sorted(frequencia.keys()))
plt.show()
from collections import Counter
import statistics
import matplotlib.pyplot as plt

lista = [
    498, 501, 500, 503, 499, 502,
    500, 497, 501, 502, 499, 500,
    501, 498, 500, 502, 499, 503
]

# Frequência de cada valor
frequencia = Counter(lista)

# Média
media = statistics.mean(lista)

# Desvio padrão amostral
desvio_padrao = statistics.stdev(lista)

# Amplitude
amplitude = max(lista) - min(lista)

print("Frequência:")
for valor, freq in sorted(frequencia.items()):
    print(f"{valor}: {freq}")

print(f"\nMédia: {media:.4f}")
print(f"Desvio padrão amostral: {desvio_padrao:.4f}")
print(f"Amplitude: {amplitude}")

# Gráfico de barras
plt.bar(frequencia.keys(), frequencia.values())
plt.title("Frequência dos Valores")
plt.xlabel("Valores")
plt.ylabel("Frequência")
plt.xticks(sorted(frequencia.keys()))
plt.show()
import numpy as np
import matplotlib.pyplot as plt

dados = [
    0.1020,
    0.1005,
    0.0985,
    0.1005,
    0.0987,
    0.0994,
    0.0998,
    0.1001,
    0.0997,
    0.1000,
    0.1015,
    0.1005,
    0.1009,
    0.1010,
    0.1013,
    0.0995,
    0.1005,
    0.1018,
    0.1004,
    0.1014,
    0.0999,
    0.1002,
    0.1002,
    0.1010,
    0.0986,
    0.0994,
    0.1013,
    0.1007,
    0.1011,
    0.0980,
    0.1012,
    0.0997,
    0.1000,
    0.0977,
    0.0999,
    0.1009,
    0.1005,
    0.0994,
    0.0986,
    0.0991,
    0.0984,
    0.0992,
    0.0997,
    0.0985,
    0.1008,
    0.1003,
    0.1003,
    0.1001,
    0.0999,
    0.1006
]
a = 0

print("Média: ", np.mean(dados))
print("Desvio Padrão: ", np.std(dados, ddof=1))
print("Mediana: ", np.median(dados))

q1 = np.percentile(dados, 25)
print("1º Quartil: ", q1)

q3 = np.percentile(dados, 75)
print("3º Quartil: ", q3)

plt.boxplot(dados)
plt.title("Boxplot dos Dados")
plt.ylabel("Valores")
plt.xlabel("Observações")
plt.show()
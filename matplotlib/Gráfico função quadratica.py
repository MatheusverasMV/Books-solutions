import numpy as np
import matplotlib.pyplot as plt

# Função
def f(y):
    return y**2 - 6*y + 5

# Valores para o gráfico
y = np.linspace(-1, 7, 400)
fy = f(y)

# Raízes
raizes = [1, 5]

plt.figure()

# Eixos
plt.axhline(0)
plt.axvline(0)

# Gráfico da função
plt.plot(y, fy, label="f(y) = y² - 6y + 5")

# Marcar raízes
plt.scatter(raizes, [0, 0])

# Rotular raízes
plt.text(1, 0, '  (1,0)')
plt.text(5, 0, '  (5,0)')

# Marcar regiões com + e -
for i in range(0, len(y), 40):
    if fy[i] > 0:
        plt.text(y[i], fy[i], '+')
    else:
        plt.text(y[i], fy[i], '-')

plt.title("Gráfico de f(y) = y² - 6y + 5")
plt.xlabel("y")
plt.ylabel("f(y)")
plt.legend()

plt.show()
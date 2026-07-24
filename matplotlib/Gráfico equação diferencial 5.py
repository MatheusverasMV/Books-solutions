import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
M = 100
C = 80
k = 0.2

# Função
def P(t):
    return M - C*np.exp(-k*t)

# Intervalo de tempo
t = np.linspace(0, 20, 400)

# Valores da função
P_vals = P(t)

# Plot
plt.figure()
plt.plot(t, P_vals, label="P(t) = M - Ce^(-kt)")

# Linha do valor limite M
plt.axhline(M)

plt.title("Gráfico de P(t) = M - Ce^(-kt)")
plt.xlabel("t")
plt.ylabel("P(t)")
plt.legend()

plt.show()
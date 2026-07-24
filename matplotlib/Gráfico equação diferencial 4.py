import numpy as np
import matplotlib.pyplot as plt

# Parâmetro
k = 0.3

# Função
def T(t):
    return 20 + 75*np.exp(-k*t)

# Intervalo de tempo
t = np.linspace(0, 20, 400)

# Calculando valores
T_vals = T(t)

# Plotando
plt.figure()
plt.plot(t, T_vals, label="T(t) = 20 + 75e^(-kt)")

# Linha da temperatura ambiente
plt.axhline(20)

plt.title("Gráfico de T(t) = 20 + 75e^(-kt)")
plt.xlabel("t")
plt.ylabel("T(t)")
plt.legend()

plt.show()
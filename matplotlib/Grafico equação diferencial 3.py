import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Definindo a equação diferencial
def dydt(t, y):
    return np.exp(t) * (y - 1)**2

# Intervalo de tempo maior
t_span = (-2, 4)
t_eval = np.linspace(-2, 4, 400)

# Condição inicial
y0 = [0.5]

# Resolvendo a EDO
sol = solve_ivp(dydt, t_span, y0, t_eval=t_eval)

# Plotando o gráfico
plt.figure()
plt.plot(sol.t, sol.y[0], label="Solução y(t)")
plt.axhline(1)

plt.title("Solução da EDO dy/dt = e^t (y-1)^2")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend()

plt.show()
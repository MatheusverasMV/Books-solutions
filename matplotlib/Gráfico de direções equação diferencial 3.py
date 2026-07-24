import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Equação diferencial
def dydt(t, y):
    return np.exp(t) * (y - 1)**2

# Grade para o campo de direções
t_vals = np.linspace(0, 2, 20)
y_vals = np.linspace(-1, 3, 20)

T, Y = np.meshgrid(t_vals, y_vals)

# Inclinação dy/dt
S = np.exp(T) * (Y - 1)**2

# Normalizando para melhor visualização
dt = 1
dy = S
norm = np.sqrt(dt**2 + dy**2)
dt = dt / norm
dy = dy / norm

# Plot do campo de direções
plt.figure()
plt.quiver(T, Y, dt, dy)

# Resolver uma solução específica
t_span = (0, 2)
t_eval = np.linspace(0, 2, 200)
y0 = [0.5]

sol = solve_ivp(dydt, t_span, y0, t_eval=t_eval)

# Plot da solução
plt.plot(sol.t, sol.y[0], linewidth=2, label="Solução y(t)")

plt.title("Campo de direções da EDO dy/dt = e^t (y-1)^2")
plt.xlabel("t")
plt.ylabel("y")
plt.legend()

plt.show()
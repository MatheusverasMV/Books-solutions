import numpy as np
import matplotlib.pyplot as plt

# Criando uma grade de pontos
x = np.linspace(-5, 5, 50)
y = np.linspace(0, 5, 50)   # y >= 0
z = np.linspace(-5, 5, 50)

X, Y, Z = np.meshgrid(x, y, z)

# Condição do domínio: x >= 2z
mask = X >= 2 * Z

# Filtrando pontos válidos
X_valid = X[mask]
Y_valid = Y[mask]
Z_valid = Z[mask]

# Plotando
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X_valid, Y_valid, Z_valid, s=1)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Domínio de f(x,y,z) = sqrt(y) - sqrt(x - 2z)')

plt.show()
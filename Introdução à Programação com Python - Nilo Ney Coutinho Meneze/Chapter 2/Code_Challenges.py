import numpy as np
import matplotlib.pyplot as plt

v = np.array([1,2])
plt.plot([0,v[0]],[0,v[1]])

initial = 0
while initial < 10:
    scalar = np.random.rand()
    v_scaled = scalar * v
    plt.plot([0,v_scaled[0]],[0,v_scaled[1]])
    initial += 1

plt.grid(True)
plt.show()
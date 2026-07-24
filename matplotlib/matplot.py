import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2, 2, 200)
y = x**3
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y= x^3')
plt.title('y = x^3')
plt.show()
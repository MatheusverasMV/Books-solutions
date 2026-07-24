import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np  

plt.style.use('classic') #estilo do gráfico, nesse caso o estilo ggplot, que é um estilo inspirado no software de visualização de dados ggplot2 do R

x= np.linspace(0, 2*np.pi, 100)
c= np.cos(x)
s = np.sin(x)

plt.figure("gráficos trigonometricos",figsize=(10,5))
plt.subplots_adjust(wspace=0.3)

ax1= plt.subplot(1,2,1)
ax1.plot(x,c, label='cosseno', color='blue')
ax1.set_title('Gráfico do cosseno')
ax1.set_xlabel('x')
ax1.set_ylabel('cos(x)')
ax1.legend()
plt.grid()  

ax2= plt.subplot(1,2,2)
ax2.plot(x,s, label='seno', color='red')
ax2.set_title('Gráfico do seno')
ax2.set_xlabel('x')
ax2.set_ylabel('sin(x)')
ax2.legend()
plt.grid()

plt.show()
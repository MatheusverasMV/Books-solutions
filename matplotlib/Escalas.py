######################################################################################################################################
#Esse codigo tem como objetivo explicar a customização de escalas de gráficos no matplotlib###########################################
######################################################################################################################################

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot') #estilo do gráfico, nesse caso o estilo ggplot, que é um estilo inspirado no software de visualização de dados ggplot2 do R

x= np.linspace(0, 2*np.pi, 500)
y = np.sin(x)

fig, axe = plt.subplots(figsize=(7,4)) #figsize é o tamanho da figura, nesse caso 7 polegadas de largura e 4 polegadas de altura
axe.plot(x, y)

axe.set_title('Gráfico do seno',fontsize=16 ) #fontzie determina o tamanho da fonte do título
axe.set_xlabel('x',fontsize=12) 
axe.set_ylabel('sin(x)',fontsize=12)

plt.xticks(np.arange(0, 2*np.pi+1, 0.5)), #np.arange é uma função que gera um array de números, nesse caso de 0 a 2*pi com um passo de pi/2
plt.yticks(np.arange(-1, 1.5, 0.2)) #np.arange é uma função que gera um array de números, nesse caso de -1 a 1.5 com um passo de 0.5           

plt.grid(True) #grid é uma função que adiciona uma grade ao gráfico
plt.show()
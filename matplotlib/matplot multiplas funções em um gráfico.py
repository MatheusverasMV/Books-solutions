###################################################################################
# Matplotlib - Matplot múltiplas funções em um gráfico
###################################################################################    

#Importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt

#Parametro inicial da concentração de A
A0 = 10

#Constantes de taxa para as reações de primeira ordem
k = [0.2, 0.5, 1]

#Criando um array de tempo de 0 a 10 segundos, com 30 pontos
t = np.linspace(0, 10, 30)

#Calculando a concentração de A para cada constante de taxa e plotando os resultados
rate_constants = [0.2, 0.5, 1]

#Calculando a concentração de A para cada constante de taxa e plotando os resultados
for k in rate_constants:
    A = A0 * np.exp(-k * t)
    plt.plot(t, A, marker='o', label=f'k ={k:.1f} s-1'.format(k))

# Configurando o gráfico
plt.title('Decomposição de A em função do tempo')    
plt.xlabel('t /s')
plt.ylabel('[A] /mol.dm^-3')
plt.legend()
plt.show()
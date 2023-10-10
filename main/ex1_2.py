from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

# IMPORTANDO DADOS
mat = loadmat('./TransferFunction12.mat')

# VARIAVEIS
# Du = 12
# Dy = 23,92
# T1 = 23,3% * Dy = 6,7690 -> 2,655
# T2 = 63,2% * Dy = 15,117 -> 5,970
# K = Dy/Du = 1,993
# T = 1.5(T2 - T1) = 4,972
# Theta = T2 - T = 0,998

degrau = mat.get('degrau')
saida = mat.get('saida')
t1 = mat.get('t')

plot1 = plt.plot(t1.T, saida, label='Saída')
plot2 = plt.plot(t1.T, degrau, label='degrau de entrada')
plt.xlabel(' t [ s ] ')
plt.ylabel('Amplitude')
plt.legend(loc="upper left")

plt.grid()
plt.show()

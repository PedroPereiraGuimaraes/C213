import numpy as np
import control as cnt
import matplotlib.pyplot as plt
from scipy.io import loadmat

# IMPORTANDO DADOS
mat = loadmat('./TransferFunction12.mat')

# VARIAVEIS
k = 1.993
tau = 4.972
Theta = 0.998

# FUN TRANSF
num = np.array([k])
den = np.array([tau, 1])
H = cnt.tf(num, den)

n_pade = 20
(num_pade, den_pade) = cnt.pade(Theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H, H_pade)

# TEMPO SIMULACAO
t = np.linspace(0, 30, 1000)

# RESPOSTA EM DEGRAU
time, y = cnt.step_response(12*Hs, T=t)

# ERRO EM MALHA ABERTA -> 12-24 = -12
# ERRO EM MALHA FECHADA -> 12-8 = 4

plt.plot(time, y)
plt.xlabel('Tempo')
plt.ylabel('Amplitude')
plt.title('Smith')
plt.grid(True)


degrau = mat.get('degrau')
saida = mat.get('saida')
t1 = mat.get('t')

plot1 = plt.plot(t1.T, saida, label='Saída')
plot2 = plt.plot(t1.T, degrau, label='degrau de entrada')


plt.tight_layout()  # NEGA SOBREPOSICAO DE GRAFICOS
plt.show()

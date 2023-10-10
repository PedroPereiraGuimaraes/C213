import numpy as np
import control as cnt
import matplotlib.pyplot as plt

# VARIAVEIS
k = 1.993
tau = 4.972
Theta = 0.998

num = np. array([k])
den = np. array([tau, 1])
H = cnt.tf(num, den)
n_pade = 20
(num_pade, den_pade) = cnt.pade(Theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H, H_pade)

Hmf = cnt.feedback(Hs, 1)

t = np . linspace(0, 30, 100)
(t, y) = cnt.step_response(12 * Hmf, t)
plt.plot(t, y)
plt.xlabel(' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('Malha fechada')

plt.grid()
plt.show()

import numpy as np
import control as cnt
import matplotlib.pyplot as plt

# VARIAVEIS
k = 0.5
tau = 4.972
Theta = 0.998
lambida = 0.7984

# PARAMETROS CONTROLADOR
kp = (((2*tau) + Theta)/(k*(2*lambida)+Theta))
Ti = (tau+(Theta/2))
Td = ((tau*Theta)/((2*tau)+Theta))

print(kp, Ti, Td)

# FUNC TRANF PLANTA
num = np. array([k])
den = np. array([tau, 1])
H = cnt.tf(num, den)
n_pade = 20
(num_pade, den_pade) = cnt.pade(Theta, n_pade)
H_pade = cnt.tf(num_pade, den_pade)
Hs = cnt.series(H, H_pade)

# CONTROLADOR PROPORCIONAL
numkp = np. array([kp])
denkp = np. array([1])

# INTEGRAL
numki = np. array([kp])
denki = np. array([Ti, 0])

# DERIVATIVO
numkd = np. array([kp*Td, 0])
denkd = np. array([1])

# CONTROLADOR PID
Hkp = cnt.tf(numkp, denkp)
Hki = cnt.tf(numki, denki)
Hkd = cnt.tf(numkd, denkd)
Hctrl1 = cnt.parallel(Hkp, Hki)
Hctrl = cnt.parallel(Hctrl1, Hkd)
Hdel = cnt.series(Hs, Hctrl)

# REALIMENTACAO
Hcl = cnt.feedback(Hdel, 1)

t = np . linspace(0, 40, 100)
(t, y) = cnt.step_response(12 * Hcl, t)
plt.plot(t, y)
plt.xlabel(' t [ s ] ')
plt.ylabel('Amplitude')
plt.title('Controle PID')

plt.grid()
plt.show()

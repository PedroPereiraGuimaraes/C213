import numpy as np
import control as cnt
import matplotlib.pyplot as plt


def imc(k, tau, Theta, lambida):
    # PARAMETROS CONTROLADOR
    kp = (((2*tau) + Theta)/(k*(2*lambida)+Theta))
    Ti = (tau+(Theta/2))
    Td = ((tau*Theta)/((2*tau)+Theta))

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


def int_erro(k, tau, Theta):
    # PARAMETROS CONTROLADOR
    kp = (1/((Theta/tau)+0.2)/k)
    Ti = (((0.3*(Theta/tau)) + 1.2)/((Theta/tau)+0.08))*Theta
    Td = (1/(90*(Theta/tau))) * Theta

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


def interface():

    print("Entre com os valores de:")

    # ENTRADA DE VALORES DAS VARIAVEIS
    Du = input("Delta U: ")
    Dy = input("Delta Y: ")
    T1 = input("T1: ")
    T2 = input("T2: ")
    K = float(Dy)/float(Du)
    T = (1.5*(float(T2) - float(T1)))
    Theta = float(T2) - float(T)

    # ESCOLHA DO TIPO DE TECNICA
    op = input("Escolha o tipo de técnica: \n 1-IMC \n 2-Integral de erro\n")
    if op == "1":
        lambida = Theta*0.8
        imc(K, T, Theta, float(lambida))
    elif op == "2":
        int_erro(K, T, Theta)


on = input("Deseja iniciar? 1-Sim 2-Não\n")
while on == "1":
    interface()
    on = input("Deseja refazer? 1-Sim 2-Não\n")

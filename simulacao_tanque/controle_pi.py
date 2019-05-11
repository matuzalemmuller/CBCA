# UFSC - 2019/1
# PPGEAS - CBCA
# Matuzalem Muller dos Santos
# Controle proporcional integral
import matplotlib.pyplot as plt
import numpy as n

# Parametros de tempo
step = 0.1
stop = 1200
t = n.linspace(0,step*stop, stop)

# Entrada reservatorio
ki = 1                  # Constante de abertura de entrada
ai = n.zeros(stop)      # Abertura de entrada

# Saida reservatorio
a0 = 1                  # Abertura de saida
k0 = 1                  # Constante de abertura de saida

# Parametros reservatorio
A = 10                  # Area
kp = 10                 # Constante ganho
Ti = 5
Ie = n.zeros(stop)      # Integral do erro
e = n.zeros(stop)       # Erro
h = n.zeros(stop)       # Altura do liquido no reservatorio
hr = 50                 # Altura de referencia

for i in range(1,len(t)):
    Ie[i] = Ie[i-1] + (e[i-1] * step)
    e[i] = hr - h[i-1]
    ai[i] = kp * e[i] + (kp/Ti) * Ie[i]
    # if ai[i] > 1:
    #     ai[i] = 1
    # if ai[i] < 0:
    #     ai[i] = 0
    dfi = (1/A) * ((ki*ai[i]) - (k0 * a0 * h[i-1]))
    h[i] = h[i-1] + (dfi * step)

plt.figure("Controle autom"u'á'"tico de Tanque")
plt.plot(t, h)
plt.xlabel('Tempo')
plt.ylabel('Nivel Tanque')
plt.title("Controle PI")
plt.grid()
plt.show()

plt.figure("Erro")
plt.plot(t, e)
plt.xlabel('Tempo')
plt.ylabel('Erro')
plt.title("Erro")
plt.grid()
plt.show()

plt.figure("Abertura de entrada")
plt.plot(t, (hr*kp)-ai)
plt.xlabel('Tempo')
plt.ylabel('ai(t)')
plt.title("Abertura de entrada")
plt.grid()
plt.show()
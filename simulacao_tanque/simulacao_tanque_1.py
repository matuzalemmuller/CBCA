import numpy as np
import matplotlib.pyplot as plt

# Parametros tanque
A = 10          # area do tanque
h0 = 0          # altura inicial
h_t = []        # altura em instante de tempo "t"

# Entrada tanque
ai = 0.5        # abertura de entrada
Ki = 100        # constante de abertura de entrada
Fi = ai * Ki    # vazão de entrada

# Saída tanque
ao = 1          # abertura de saida
Ko = 1          # constante de abertura de saida
Fo = ao * Ko    # vazão de saida

stop = 120      # tempo de simulacao
step = 1        # intervalo de tempo entre amostras ( "delta t" )
t = np.linspace(0,stop,stop)

for i in range(len(t)):
    h = h0 + (1/A) * (Fi - ( Fo * h0 )) * step
    h0 = h
    h_t.append(h)

plt.plot(t,h_t)
plt.grid()
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Parametros tanque
A = 10          # area do tanque
h0 = 0          # altura inicial
h_t = []        # altura em instante de tempo "t"

# Entrada tanque
ai = 1        # abertura de entrada
Ki = 100        # constante de abertura de entrada
Fi = ai * Ki    # vazão de entrada

# Saída tanque
ao = 1          # abertura de saida
Ko = 1          # constante de abertura de saida
Fo = ao * Ko    # vazão de saida

stop = 120      # tempo de simulacao
step = 1        # intervalo de tempo entre amostras ( "delta t" )
t = np.linspace(0,stop,stop)

h_j = 0
h_i = 0

for i in range(len(t)):
    h_j = h0
    h = h0 + (1/A) * (Fi - ( Fo * h0 )) * step
    h_i = h
    if h_i == h_j:
        print("Nível de equilíbrio: " + str(h_i))
        print("Instante: " + str(i))
    h0 = h
    h_t.append(h)

plt.plot(t,h_t)
plt.xlabel("Tempo")
plt.ylabel("Nível da coluna do líquido")
plt.grid()
plt.show()
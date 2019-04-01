import numpy as np
import matplotlib.pyplot as plt

A = 10
h0 = 0
h_t = []
h_e = 0

# Entrada
ai = 0.5
Ki = 100
Fi = ai * Ki

# Saída
ao = 1
Ko = 1
Fo = ao * Ko

stop = 120
step = 1
t = np.linspace(0,stop,stop)

for i in range(len(t)):
    h = h0 + (1/A) * (Fi - ( Fo * h0 )) * step
    h0 = h
    h_t.append(h)

plt.plot(t,h_t)
plt.grid()
plt.show()
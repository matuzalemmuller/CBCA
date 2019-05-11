# UFSC - 2019/1
# PPGEAS - CBCA
# Matuzalem Muller dos Santos
# Controle proporcional
import matplotlib.pyplot as plt
import numpy

# Parametros tanque
area=10         # area do tanque
hr=50           # altura referencia
dt=120          # tempo de simulacao

# Entrada tanque
ai=1            # abertura de entrada
ki=1            # constante de abertura de entrada

# Saida tanque
ao=1            # abertura de saida
ko=1            # constante de abertura de saida
ht = 0

val_graph = numpy.zeros(dt)
for i in range(1,dt):
    Fi = ai*ki*(hr-ht)
    Fo = ao*ko*ht
    ht += (1/area)*(Fi-Fo)
    val_graph[i] = ht


t = range(0,len(val_graph))
plt.figure("Controle autom"u'á'"tico de Tanque")
plt.plot(t, val_graph)
plt.xlabel('Tempo')
plt.ylabel('Nivel Tanque')
plt.title("Controle Proporcional")
plt.grid()
plt.show()
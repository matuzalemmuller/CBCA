import matplotlib.pyplot as plt
import numpy

# Parametros tanque
area=30         # area do tanque
hr=90           # altura referencia
dt=120          # tempo de simulacao

# Entrada tanque
ai=0.3          # abertura de entrada
ki=1.5          # constante de abertura de entrada

# Saida tanque
ao=0.3          # abertura de saida
ko=1.0          # constante de abertura de saida


def controle_proporcional():
	ht = 0
	val_graph = numpy.zeros(dt)
	for i in range(1,dt):
		Fi = ai*ki*(hr-ht)
		Fo = ao*ko*ht
		ht += (1/area)*(Fi-Fo)
		val_graph[i] = ht
	return val_graph


def controle_proporcional_integral():
	ht = 0
	ai_tmp = 0
	Fi = 0
	val_graph = numpy.zeros(dt)
	for i in range(1,dt):
		ai_tmp += ai
		Fi = ai_tmp*ki*(hr-ht)
		Fo = ao*ko*ht
		ht += (1/area)*(Fi-Fo)
		val_graph[i] = ht
	return val_graph


def main():
    graph1 = controle_proporcional()
    graph2 = controle_proporcional_integral()
    t = range(0,dt)
    plt.figure("Controle autom"u'á'"tico de Tanque")
    plt.subplot(211)
    plt.subplots_adjust(hspace =0.5)
    plt.plot(t, graph1)
    plt.xlabel('Tempo')
    plt.ylabel('Nivel Tanque')
    plt.title("Controle Proporcional")
    plt.grid()
    plt.subplot(212)
    plt.xlabel('Tempo')
    plt.ylabel('Nivel Tanque')
    plt.title("Controle Proporcional Integral")
    plt.plot(t, graph2)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
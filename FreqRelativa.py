import pandas as pd
import matplotlib.pyplot as plt 

km = pd.Series([4,6,6,7,11,13,18,21,24,26,27,35,36,36,42,43,45,49])
#ticks = [4,13,22,31,40,49]

def calcula_ticks(lista,barras):
	menor_valor = lista[0] # Pega o primeiro valor da lista
	maior_valor = lista[-1] # Pega o ultimo valor da lista
	intervalo = (maior_valor - menor_valor)/barras #Intervalo do histograma
	ticks = [menor_valor]
	ultimo = menor_valor + intervalo
	ticks.append(ultimo)
	for x in range(barras-1):
		ultimo += intervalo
		ticks.append(ultimo)
	return ticks

def frequencia_relativa(total,yticks):
	freq_rel = []
	for item in yticks:
		x = item/total
		freq_rel.append("{0:.2f}%%".format(x*100))
	return freq_rel

lista = km.values
barras = 5
ax = km.plot.hist(bins=barras, rwidth = 0.95)

yticks = ax.get_yticks()
total = len(lista)
freq_rel = frequencia_relativa(total,yticks)
ax.set_yticklabels(freq_rel)

ticks = calcula_ticks(lista,barras)
plt.xticks(ticks)
plt.title('Distância da Casa para o Trabalho')
plt.xlabel('KM')
plt.ylabel('Frequência')
plt.grid(axis='y')

plt.show()
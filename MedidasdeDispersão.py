import pandas as pd
import matplotlib.pyplot as plt 

data = pd.read_csv(r'C:\Users\Marti\Documents\Udemy\weight-height.csv')
#ticks = [4,13,22,31,40,49]

def calcula_ticks(lista,barras):
	lista.sort()
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

def gera_histograma(barras,data_series, titulo, unidade):

	lista = data_series.values
	ax = data_series.plot.hist(bins=barras, rwidth = 0.75)

	yticks = ax.get_yticks()
	total = len(lista)
	freq_rel = frequencia_relativa(total,yticks)
	ax.set_yticklabels(freq_rel)

	fig = plt.gcf()
	fig.set_size_inches(10,5)
	fig.set_dpi(50)

	ticks = calcula_ticks(lista,barras)
	plt.xticks(ticks)
	plt.title(titulo)
	plt.xlabel(unidade)
	plt.ylabel('Frequência')
	plt.grid(axis='y')

data['Altura cm'] = data['Height']*2.54

data['Altura cm'] = data['Altura cm'].round(0)

altura_mulheres = data.loc[data['Gender'] == 'Female']['Altura cm']

gera_histograma(9,altura_mulheres, 'Altura Mulheres', 'cm' )

plt.show()
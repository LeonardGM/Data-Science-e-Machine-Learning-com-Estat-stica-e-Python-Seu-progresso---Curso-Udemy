import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_csv(r'C:\Users\Marti\Documents\Udemy\train.csv')


data.columns = ['IdPassageiro', 'Sobreviveu', 'Classe', 'Nome', 'Sexo', 'Idade',
				'IrmaosConuge', 'PaisFilhos', 'Bilhete', 'Tarifa', 'Cabine', 'Embarque']

data['Sexo'].replace({'male': 'homem', 'female': 'mulher'}, inplace = True)

data['Cabine'] = data['Cabine'].apply(lambda x: x[0] if pd.notna(x) else np.nan)



#Countplot e Pie

f, ax = plt.subplots(1,2, figsize = (10,5))
data['Classe'].value_counts().plot.pie(ax=ax[0], explode = [0.02, 0.02, 0.02], autopct='%0.2f%%')
ax[0].set_ylabel('')

sns.countplot('Sobreviveu', data = data, ax = ax[1])
ax[1].set_ylabel('')

# CountPlot e Hue 

sns.countplot('Sobreviveu', hue = 'Sexo', data = data) #Separação/Comparar

# Box Plot

plt.figure(figsize = (5,3), dpi = 100)
sns.boxplot(x ='Classe', y = 'Idade', hue = 'Sexo', data = data)
plt.show()

# Violin Plot

plt.figure(figsize = (5,3), dpi = 100)
sns.violinplot(x = 'Classe', y = 'Idade', hue = 'Sexo', data = data)


#Facet Grid 

g = sns.FacetGrid(data, col = 'Sobreviveu')
g.map(plt.hist, 'Idade', bins = 18)

g = sns.FacetGrid(data, row = 'Embarque', col = 'Sobreviveu')
g.map(sns.barplot, 'Sexo', 'Tarifa', alpha = 0.4, ci = None)
fig = plt.gcf()
fig.set_size_inches(10,6)

#Facet Grid com distplot

g = sns.FacetGrid(data, col = 'Sobreviveu', row = 'Classe', height = 1.8, aspect = 2.2)
g.map(sns.distplot, 'Idade', bins = 20)

# Catplot do tipo 'Point'

sns.catplot('Embarque', 'Sobreviveu', data = data, kind = 'point')

# FacetGrid com pointplot

g = sns.FacetGrid(data, row = 'Embarque', height = 1.8, aspect = 2.2)
g.map(sns.pointplot, 'Classe', 'Sobreviveu', 'Sexo')
g.add_legend()


#Heatmap de Dados Ausentes

sns.heatmap(data.isnull(), yticklabel = False, cbar = False, cmap = 'magma')


#Relplot

sns.relplot(x = 'Tarifa', y = 'Idade', hue = 'Sexo', data = data, size = 'Tarifa', sizes = (40,400),
			alpha = 0.8, palette = 'magma')


#Scatterplot

sns.scatterplot(x = 'Idade', y = 'Tarifa', hue = 'Embarque', size = 'Idade',
				palette = 'magma', data = data, sizes = (10,200))



#Pairplot

sns.pairplot(data[['Tarifa', 'Idade', 'Classe', 'Sexo', 'Embarque']], hue = 'Classe')

#Jointplot = Onde os dados estão concentrados


#sns.jointplot('Idade', 'Tarifa', data = data, kind = 'kde', color = 'g')
#sns.jointplot('Idade', 'Tarifa', data = data, kind = 'reg', color = 'g')

sns.kdeplot(data['Idade'].loc[data['Classe']==1], shade = True, color = 'g', label = '1ª Classe', alpha = 0.10)
sns.kdeplot(data['Idade'].loc[data['Classe']==2], shade = True, color = 'deeppink', label = '2ª Classe', alpha = 0.4)
sns.kdeplot(data['Idade'].loc[data['Classe']==3], shade = True, color = 'dodgerblue', label = '3ª Classe', alpha = 0.7)
sns.catplot('Sobreviveu', col = 'Cabine', data = data[['Sobreviveu', 'Cabine']].dropna(),kind = 'count', height = 3.5, aspect = 0.4, col_wrap = 4)

#hetmap corr()

plt.figure(figsize = (10,7))
sns.heatmap(data[['Classe', 'Idade', 'Sobreviveu', 'Tarifa', 'Embarque']].corr(), cmap = 'Blues', annot = True)
plt.show()

#Plot

x = np.random.normal(10,1,15) # Criando 15 elementos com média 10 e desvio padrão 1
plt.plot(x)
plt.show()

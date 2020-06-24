import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 


data = pd.read_csv(r'C:\Users\Marti\Documents\Udemy\train.csv')

data.columns = ['IdPassageiro', 'Sobreviveu', 'Classe', 'Nome', 'Sexo', 'Idade',
				'IrmaosConuge', 'PaisFilhos', 'Bilhete', 'Tarifa', 'Cabine', 'Embarque']

data['Sexo'].replace({'male': 'homem', 'female': 'mulher'}, inplace = True)

data['Cabine'] = data['Cabine'].apply(lambda x: x[0] if pd.notna(x) else np.nan)


'''

plt.hist(data['Idade'].dropna(), bins = 10)
plt.title('Distribuição das Idades')
plt.ylabel('Pessoas')
plt.xlabel('Idades')
plt.show()


plt.hist(data['Classe'])
plt.title('Distribuição das Classes')
plt.ylabel('Pessoas')
plt.xlabel('Classes')
plt.show()

## SUB PLOT 1 

plt.subplot(1, 2, 1) # 1 linha, 2 colunas, plot 1
plt.hist(data['Idade'].dropna())
plt.title('Distribuição das Idades')

plt.subplot(1, 2, 2) # 1 linha, 2 colunas, plot 1
plt.hist(data['Classe'])
plt.title('Distribuição das Classes')
plt.tight_layout()
plt.show()

'''
## SUB PLOT 2

f, ax = plt.subplots(1,2, figsize = (10,5), dpi = 100) # f = figura - ax = grafico # 1 linha , 2 colunas
ax[0].hist(data['Idade'].dropna())
ax[0].set_title('Distribuição das Idades')

ax[1].hist(data['Classe'])
ax[1].set_title('Distribuição das Classes')

plt.tight_layout()
plt.show()




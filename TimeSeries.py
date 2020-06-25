import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import datetime
import locale

#locale.setlocale(locale.LC_ALL, 'pt-BR')

# Tempo de agora

datetime.datetime.now()

# Diferença de tempo TimeDelta

antes = datetime.datetime.now()
depois = datetime.datetime.now()
diferenca = depois - antes 

#Conversão de String para data e hora convencional do python

str_data_hora = '09/17/20 13:26:35'

convertida_para_datetime = datetime.datetime.strptime(str_data_hora, '%m/%d/%y %H:%M:%S') 
print(convertida_para_datetime)

#Conversão de data String para data convencional do python

str_data = '17-09-2020'
data = datetime.datetime.strptime(str_data, '%d-%m-%Y').date() 
print(data)

#Conversão de string de tempo para tempo convencional do python

str_tempo = '14:45:38'
tempo = datetime.datetime.strptime(str_tempo, '%H:%M:%S').time() 
print(tempo)

start = '01/01/2020'
end = '31/12/2020'

x = pd.date_range(start, end, freq = 'MS')#.strftime('%d/%b/%Y')
print(x)

y = np.random.normal(10, 1, 12) # 12 elementos com média 10 com desvio padrão 1
f, ax = plt.subplots(dpi = 100)
plt.plot(x,y)
f.autofmt_xdate()

data = pd.DataFrame({'Datas': x, 'Valores': y})

'''
data['Datas'] = ['2020-01-01T00:00:00.000000000', '2020-02-01T00:00:00.000000000',
 '2020-03-01T00:00:00.000000000', '2020-04-01T00:00:00.000000000',
 '2020-05-01T00:00:00.000000000', '2020-06-01T00:00:00.000000000',
 '2020-07-01T00:00:00.000000000', '2020-08-01T00:00:00.000000000',
 '2020-09-01T00:00:00.000000000', '2020-10-01T00:00:00.000000000',
 '2020-11-01T00:00:00.000000000', '2020-12-01T00:00:00.000000000']
'''
 
data['Datas'] = pd.DatetimeIndex(data['Datas'])

data.set_index('Datas', inplace = True)

data['Data String'] = data.index.strftime('%d/%b/%y')

data['Data String'] = pd.to_datetime(data['Data String'], format = '%d/%b/%y')
print(data)

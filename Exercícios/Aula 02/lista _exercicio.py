import pandas as pd
import numpy as np
from datetime import datetime
#import plotly.express as px

path = 'C:/Users/emerson eduardo/Desktop/Engenharia Civil/Cursos/Python do zero ao DS/Curso-Python-do-zero-ao-DS/Exercícios/Projeto de Insights/DataSets/kc_house_data.csv'

data = pd.read_csv(path, encoding='UTF-8')


# 1 - Crie uma nova coluna chamada: "house_age"
data['house_age'] = ""


#   - Se o valor da coluna "date" for maior que 2014-01-01 --> "new_house"


data['date'] = pd.to_datetime(data['date'])
dataref = pd.to_datetime('20140101')
data.loc[data['date'] > dataref, 'house_age'] = 'new_house'


#   -Se o valor da coluna "date" for menor que 2014-01-01 --> "old_house"
data.loc[data['date'] < dataref, 'house_age'] = 'old_house'



# 2 - Crie uma nova coluna chamada: "dormitory_type"
data['dormitory_type'] = ""

#   - Se o valor da coluna "bedrooms" for igual à 1 --> "studio"

data.loc[data['bedrooms'] == 1, 'dormitory_type']  = 'studio'
# print(data[data['bedrooms'] == 1] [['bedrooms', 'dormitory_type']])

#   - Se o valor da coluna "bedrooms" for igual à 2 --> "apartament"

data.loc[data['bedrooms'] == 2, 'dormitory_type']  = 'apartment'


#   - Se o valor da coluna "bedrooms" for maior que 2 --> "house"

data.loc[data['bedrooms'] > 2, 'dormitory_type']  = 'house'


# 3 - Crie uma nova coluna chamada: "condition_type"
data['condition_type'] = ""

#   - Se o valor da coluna "condition" for menor ou igual à 2 --> "bad"
data.loc[data['condition'] <= 2, 'condition_type']  = 'bad'

#   - Se o valor da coluna "condition" for menor ou igual à 3 ou 4 --> "regular"
data.loc[(data['condition'] >=3) | (data['condition'] <= 4) , 'condition_type']  = 'regular'

#   - Se o valor da coluna "condition" for maior ou igual à 5 --> "good"
data.loc[data['condition'] >= 5, 'condition_type']  = 'good'

# print(data.loc[0:50, ['condition', 'condition_type']])


# 4 - Modifique o tipo da coluna "condition" para string

# data['condition'] = data['condition'].astype(str)


# 5 - Delete as colunas: "sqrf_living15" e "sqft_lot15"

# data = data.drop(columns = ['sqft_living15', 'sqft_lot15'])


# 6 - Modifique o tipo da coluna "yr_built" para Date

data['yr_built'] = pd.to_datetime(data['yr_built'], format = '%Y')


# 7 - Modifique o tipo da coluna "yr_renovated" para date
# data['yr_renovated'] = pd.to_datetime(data['yr_renovated'], format = '%Y')

''' Não consegui converter para data. erro. '''



# 8 - Qual a data mais antiga de construção de um imóvel?
# print(data.sort_values('yr_built', ascending = True))


# 9 - Qual a data mais antiga de renovação de um imóvel?

''' Não consegui transformar para data   '''

# 10 - Quantos imóveis tem 02 andares?

# print(data[data['floors']==2].shape)

# 11 - Quantos imóveis está com a condição igual a "regular"?

# print(data[data['condition_type']=='regular'].shape)

# 12 - Quantos imóveis estão com a condição igual a "bad" e possuem "vista para a água"?

# print(data[(data['condition_type'] == 'bad') & (data['waterfront'] == 1)].shape)

# print(data.head())
''' Não existe nenhum imóvel que atenda este critério'''


# print(data[data['waterfront'] == 1])







# 13 - Quantos imóveis estão com a condição igual a "good" e são "new_house"?
 
# print(data[(data['condition_type'] == 'good') & (data['house_age'] == 'new_house')].shape)




# 14 - Qual o valor do imóvel mais caro do tipo "studio"?

# data_condition = data[data['dormitory_type'] == 'studio']
# data_condition = data_condition.sort_values('price', ascending = False)

# print(data_condition.head())

''' O valor do imóvel mas caro é R$ 1.247.000,00 '''



# 15 - Quantos imóveis do tipo "apartment" foram reformados em 2015?

# print(data[(data['yr_renovated'] == 2015) & (data['dormitory_type'] == 'apartment')])
# print(data[data['yr_renovated']==2015].shape)

''' Nenhum apartamento foi reformado em 2015  '''

# 16 - Qual o maior número de quartos que um imóvel do tipo "house" possui?



# data_house = data[data['dormitory_type'] == 'house']
# data_house = data_house.sort_values('bedrooms', ascending = False)
# print(data_house.head())

''' 33 quartos '''


# 17 - Quantos imóveis "new_house" foram reformados no ano de 2014?

# print(data[(data['yr_renovated'] == 2014) & (data['house_age'] == 'new_house')].shape)

''' 91 imóveis '''


# 18 - Selecione as colunas: "id", "date", "price", "floors", "zipcode" pelo método:

#   18.1 Direto pelo nome das colunas

# print(data[['id', 'date', 'price', 'floors', 'zipcode']])


#   18.2 Pelos índices
# print(data.iloc[:, [0, 1, 2, 7, 16] ])
# print(data.head())

#   18.3 Pelos índices das linhas e o nome das colunas

# columns = ['id', 'date', 'price', 'floors', 'zipcode']

# print(data.loc[: , columns])

#   18.4 Índices booleanos

# boolean = [True, True, True, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False]

# print(data.loc[ : , boolean])

# 19. Salve um arquivo .csv com somente as colunas do item 10.

# report = data[data['floors'] == 2]

# path_report = 'C:/Users/emerson eduardo/Desktop/Engenharia Civil/Cursos/Python do zero ao DS/Curso-Python-do-zero-ao-DS/Exercícios/Projeto de Insights/DataSets/report2.csv'
# report.to_csv(path_report, sep = ',', index = False)




# 20 - Modifique a cor dos pontos no mapa de "pink" para "verde-escuro"


data_mapa = data[['id', 'lat', 'long', 'price']]

import plotly.express as px

mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long', hover_name='id', 
hover_data=['price'] , color_discrete_sequence=['dark green'], zoom=3, height=300) 

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0 })
mapa.show()

mapa.write_html('C:/Users/emerson eduardo/Desktop/Engenharia Civil/Cursos/Python do zero ao DS/Curso-Python-do-zero-ao-DS/Exercícios/Projeto de Insights/DataSets/mapa_house_rocket.html')






import pandas as pd
import numpy as np


path = 'C:/Users/emerson eduardo/Desktop/Engenharia Civil/Cursos/Python do zero ao DS/Curso-Python-do-zero-ao-DS/Exercícios/Projeto de Insights/DataSets/kc_house_data.csv'

data = pd.read_csv(path, encoding='UTF-8')

#print(data.head())


# mostra na tela os tipos de variáveis em cada coluna
#print(data.dtypes)

# função que converte de object (string) --> date
#data['date'] = pd.to_datetime(data['date'])

#print(data.head())

# converter float para inteiro

#data['bedrooms'] = data['bedrooms'].astype(np.int64)

# String --> Data
# data['date'] = pd.to_datetime(data['date'])

# criando novas variáveis 
# data['aniversario'] = pd.to_datetime("1991-07-25")


# print(data.dtypes)

# print(data.head())

# print(data.columns)

# apagando colunas

#data = data.drop('aniversario', axis=1)

# print(data.columns)


# ======================================================================================================


# forma 01: Direto pelo nome das colunas

# print(data[['price', 'id', 'date']])



# ========================================================================================================

# forma 02: Pelos índices das linhas e colunas 

# print(data.iloc[0:10, 0:3])

# =======================================================================================================

# Forma 03: Pelos índices das linhas e nome das colunas

#print(data.loc[0:10, ['price', 'id', 'date']])

# =====================================================================================================

# Forma 04: Índices Booleanos

# cols = [True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False, True]

# print(data.loc[0:10, cols])

# 1- Qual a data do imóvel mais antigo no portfólio?

# data['date'] = pd.to_datetime(data['date'])
# print(data.sort_values('date', ascending=True))

# 2- Quantos imóveis possuem o número máximo de andares?
# print(data[data['floors'] == 3.5 ][['floors', 'id']])

# print(data[data['floors'] == 3.5 ].shape)

# 3- Criar um classificação para os imóveis, separando-os em baixo de acordo com o preço.

data['level'] = 'standard'

data.loc[data['price'] > 540000, 'level'] = 'high_level'
data.loc[data['price'] < 540000, 'level'] = 'low_level'

# print(data.head())

# 4- Gostaria de um relatório ordenado pelo preço

report = data[['id', 'date','price', 'bedrooms', 'sqft_lot', 'level']].sort_values('price', ascending = False)

print(report.head())

report.to_csv('C:/Users/emerson eduardo/Desktop/Engenharia Civil/Cursos/Python do zero ao DS/Curso-Python-do-zero-ao-DS/Exercícios/Projeto de Insights/DataSets/report_aula02.csv', sep=',', index = False)

# 5- Gostaria de um mapa indicando onde as casas estão localizadas geograficamente.

# Plotly - Biblioteca que armazena uma função que desenha mapas
# Scatter MapBox - Função que desenha um mapa

data_mapa = data[['id', 'lat', 'long', 'price']]


# data_mapa --> dados para plotar o mapa
# lat e long --> latidude e longitude
# Hover_ name --> nome que aparece quando o mouse passar por cima da região
# hover_data --> dado que aparece junto com o nome (hover_name)
# color_discrete_sequence --> cor do ponto no mapa

import plotly.express as px

mapa = px.scatter_mapbox(data_mapa, lat='lat', lon='long', hover_name='id', 
hover_data=['price'] , color_discrete_sequence=['fuchsia'], zoom=3, height=300) 

mapa.update_layout(mapbox_style='open-street-map')
mapa.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0 })
mapa.show()

mapa.write_html('C:/Users/emerson eduardo/Desktop/Engenharia Civil/Cursos/Python do zero ao DS/Curso-Python-do-zero-ao-DS/Exercícios/Projeto de Insights/DataSets/mapa_house_rocket.html')
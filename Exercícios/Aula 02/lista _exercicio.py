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
# data.loc[data['condition'] <= 2, 'condition_type']  = 'bad'

#   - Se o valor da coluna "condition" for menor ou igual à 3 ou 4 --> "regular"
# data.loc[(data['condition'] >=3) | (data['condition'] <= 4) , 'condition_type']  = 'regular'

#   - Se o valor da coluna "condition" for maior ou igual à 5 --> "good"
# data.loc[data['condition'] >= 5, 'condition_type']  = 'good'

# print(data.loc[0:50, ['condition', 'condition_type']])


# 4 - Modifique o tipo da coluna "condition" para string

# data['condition'] = data['condition'].astype(str)


# 5 - Delete as colunas: "sqrf_living15" e "sqft_lot15"

# data = data.drop(columns = ['sqft_living15', 'sqft_lot15'])


# 6 - Modifique o tipo da coluna "yr_built" para Date

data['yr_built'] = pd.to_datetime.strptime(data['yr_built'])
print(data.head())

# 7 - Modifique o tipo da coluna "yr_renovated" para date


# 8 - Qual a data mais antiga de construção de um imóvel?

# 9 - Qual a data mais antiga de revovação de um imóvel?

# 10 - Quantos imóveis tem 02 andares?

# 11 - Quantos imóveis está com a condição igual a "regular"?

# 12 - Quantos imóveis estão com a condição igual a "bad" e possuem "vista para a água"?

# 13 - Quantos imóveis estão com a condição igual a "good" e são "new_house"?


# 14 - Qual o valor do imóvel mais caro do tipo "studio"?


# 15 - Quantos imóveis do tipo "apartament" foram reformados em 2015?

# 16 - Qual o maior número de quartos que um imóvel do tipo "house" possui?

# 17 - Quantos imóveis "new_house" foram reformados no ano de 2014?

# 18 - Selecione as colunas: "id", "date", "price", "floors", "zipcode" pelo método:
#   18.1 Direto pelo nome das colunas
#   18.2 Pelos índices
#   18.3 Pelos índices das linhas e o nome das colunas
#   18.4 Índices booleanos


# 19. Salve um arquivo .csv com somente as colunas do item 10.



# 20 - Modifique a cor dos pontos no mapa de "pink" para "verde-escuro"









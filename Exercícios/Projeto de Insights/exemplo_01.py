import pandas as pd


path = 'C:/Users/emerson eduardo/Desktop/Engenharia Civil/Cursos/Python do zero ao DS/Curso-Python-do-zero-ao-DS/Exercícios/Projeto de Insights/DataSets/kc_house_data.csv'

data = pd.read_csv(path)

# mostre na tela as 5 primeiras linhas do conjunto de dados 
#print(data.head())

# mostre o número de colunas e o número de linhas do conjunto de dados
#print(data.shape)

# mostre na tela o nome das colunas do conjunto de dados
#print(data.columns)

# mostre na tela o conjunto de dados ordenados pela coluna price
#print(data.sort_values('price'))

# mostre na tela o conjunto de dados ordenados pela coluna price --> exibir apenas as colunas 'id' e 'price'
print(data[['id', 'price']].sort_values('price'))

# mostre na tela o conjunto de dados ordenados pela coluna price do maior para maior
print(data[['id', 'price']].sort_values('price', ascending=False))

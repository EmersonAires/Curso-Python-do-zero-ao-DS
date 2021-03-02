#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("estou aprendendo")


# # Agrupamento

# In[2]:


import pandas as pd


# In[4]:


path = 'C:/Users/emerson eduardo/Desktop/Engenharia Civil/Cursos/Python do zero ao DS/Curso-Python-do-zero-ao-DS/Exercícios/Projeto de Insights/DataSets/kc_house_data.csv'


# In[5]:


data = pd.read_csv(path)


# In[6]:


data.head()


# In[9]:


# Quantos imóveis existem por número de quartos
print(data[data['bedrooms'] == 0].shape)
print(data[data['bedrooms'] == 1].shape)
print(data[data['bedrooms'] == 2].shape)
print(data[data['bedrooms'] == 3].shape)
print(data[data['bedrooms'] == 4].shape)


# In[13]:


df_grouped = data[['id', 'bedrooms']].groupby('bedrooms')


# In[16]:


for bedrooms, frame in df_grouped:
    print('número de quartos: {}'.format(bedrooms))
    print(frame.head, end='\n\n')


# # Respondendo as perguntas do CEO

# In[12]:


import pandas as pd
pd.set_option('display.float_format' , lambda x: '%.3f' % x)


# In[6]:


path = 'C:/Users/emerson eduardo/Desktop/Engenharia Civil/Cursos/Python do zero ao DS/Curso-Python-do-zero-ao-DS/Exercícios/Projeto de Insights/DataSets/kc_house_data.csv'


# In[7]:


data = pd.read_csv(path)


# In[8]:


# 1. Qual o número de imóveis por ano de construção?
data[['id', 'yr_built']].groupby('yr_built').count()


# In[9]:


# 2. Qual o menor número de quartos por ano de construção de imóveis ?
data[['bedrooms', 'yr_built']].groupby('yr_built').min()


# In[10]:


# 3. Qual o preço de compra mais alto por cada número de quarto?
data[['price', 'bedrooms']].groupby('bedrooms').max()


# In[13]:


# 4. Qual a soma de todos os preços de compra por número de quartos?
data[['price', 'bedrooms']].groupby('bedrooms').sum()


# In[15]:


# 5. Qual a soma de todos os preços de compra por número de quartos e banheiros?
data[['price', 'bedrooms', 'bathrooms']].groupby(['bedrooms', 'bathrooms']).sum()


# In[17]:


# 6. Qual o tamanho médio das salas dos imóveis por ano de construção?
data[['sqft_living', 'yr_built']].groupby('yr_built').mean()


# In[18]:


# 7. Qual o tamanho mediano das salas dos imóveis por ano de construção?
data[['sqft_living', 'yr_built']].groupby('yr_built').median()


# In[19]:


# 8. Qual o desvio-padrão do tamanho das salas dos imóveis por ano de coonstrução?
data[['sqft_living', 'yr_built']].groupby('yr_built').std()


# In[ ]:


# 9. Como é o crescimeento médio de preços de compras dos imóveis, por ano, por dia e pela semana do ano?


# In[32]:


# crescimento médio de preços de compras dos imóveis por ano.
# eixo x: anos
# eixo y: soma dos preços
#Gráfico: Barras

from matplotlib import pyplot as plt

# First graph
data['year'] = pd.to_datetime(data['date']).dt.year
by_year = data[['price', 'year']].groupby('year').sum().reset_index()

plt.figure(figsize=(10, 6))
plt.bar(by_year['year'], by_year['price'])


# In[24]:


data.dtypes


# In[38]:


# Second graph
data['day'] = pd.to_datetime(data['date'])
by_day = data[['price', 'day']].groupby('day').mean().reset_index()

plt.figure(figsize=(20, 12))
plt.plot(by_day['day'], by_day['price'])


# In[36]:


data.head()


# In[40]:


# Third graph
data['year_week'] = pd.to_datetime(data['date']).dt.strftime('%Y-%U')
by_year_week = data[['price', 'year_week']].groupby('year_week').mean().reset_index()

plt.figure(figsize=(20, 12))
plt.plot(by_year_week['year_week'], by_year_week['price'])
plt.xticks(rotation=60);


# In[41]:


from matplotlib import gridspec

fig = plt.figure(figsize=(10, 6))
specs = gridspec.GridSpec(ncols=2, nrows=2, figure=fig)

ax1 = fig.add_subplot(specs[0, :]) # First Row
ax2 =fig.add_subplot(specs[1, 0]) # Second Row - First Column
ax3 =fig.add_subplot(specs[1, 1]) # Second Row - Second Column



# First graph
data['year'] = pd.to_datetime(data['date']).dt.year
by_year = data[['price', 'year']].groupby('year').sum().reset_index()


ax1.bar(by_year['year'], by_year['price'])

# Second graph
data['day'] = pd.to_datetime(data['date'])
by_day = data[['price', 'day']].groupby('day').mean().reset_index()


ax2.plot(by_day['day'], by_day['price'])


# Third graph
data['year_week'] = pd.to_datetime(data['date']).dt.strftime('%Y-%U')
by_year_week = data[['price', 'year_week']].groupby('year_week').mean().reset_index()


ax3.plot(by_year_week['year_week'], by_year_week['price'])
plt.xticks(rotation=60);


# In[43]:


# 10. Eu gostaria de olhar no mapa e conseguir identificar as casas com maior preço.
import plotly.express as px

house = data[['id', 'lat', 'long', 'price']]

fig = px.scatter_mapbox(house,
                       lat = 'lat',
                       lon = 'long',
                       size = 'price',
                       color_continuous_scale=px.colors.cyclical.IceFire,
                       size_max=15,
                       zoom=10)

fig.update_layout(mapbox_style = 'open-street-map')
fig.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





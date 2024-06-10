import streamlit as st
import pandas as pd
import plotly.express as px

# CSV
df = pd.read_csv('algoritmos.csv')

# Título principal
st.title('Análise de Algoritmos')

# Exibir o DataFrame completo
st.write(df)
st.markdown("<hr>", unsafe_allow_html=True)


# Convertendo as colunas de desempenho para tipos numéricos, aparentemente essa porra deu certo n sei como
df['Melhor'] = df['Melhor'].str.replace('.', '').astype(float)
df['Médio'] = df['Médio'].str.replace('.', '').astype(float)
df['Pior'] = df['Pior'].str.replace('.', '').astype(float)

# Obtendo os valores únicos da coluna 'Elementos'
valores_elementos = sorted(df['Elementos'].unique())

# Widget de selecionar o número de elementos
num_elementos = st.selectbox('Selecione o número de elementos:', valores_elementos)

# Filtra o DataFrame com base no número de elementos selecionado
df_filtrado = df[df['Elementos'] == num_elementos]

# Gráfico de Desempenho Melhor
st.title(f'Desempenho Melhor para {num_elementos} elementos')
fig_melhor = px.bar(df_filtrado, x='Nome do algoritmo', y='Melhor',color='Melhor')
fig_melhor.update_layout(xaxis_tickangle=-45, yaxis_title='Microssegundos')
st.plotly_chart(fig_melhor)
st.markdown("<hr>", unsafe_allow_html=True)

# Gráfico de Desempenho Médio
st.title(f'Desempenho Médio para {num_elementos} elementos')
fig_media = px.bar(df_filtrado, x='Nome do algoritmo', y='Médio',color = 'Médio')
fig_media.update_layout(xaxis_tickangle=-45, yaxis_title='Microssegundos')
st.plotly_chart(fig_media)
st.markdown("<hr>", unsafe_allow_html=True)

# Gráfico de Pior Desempenho
st.title(f'Pior Desempenho para {num_elementos} elementos')
fig_pior = px.bar(df_filtrado, x='Nome do algoritmo', y='Pior',color='Pior')
fig_pior.update_layout(xaxis_tickangle=-45, yaxis_title='Microssegundos')
st.plotly_chart(fig_pior)
st.markdown("<hr>", unsafe_allow_html=True)

# Rodapé
st.markdown("""
**INSTITUTO FEDERAL DE SÃO PAULO – IFSP 💚🤍**

**ANÁLISE E DESENVOLVIMENTO DE SISTEMAS - Estrutura de Dados 2**

Caio Dib Laronga  
Domenico Kenjy Rizzo  
Gabriela Santana Camilo  
Isabella Urdiali Miranda  
Pedro Henrique Ramos Lauton
""")

import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar o CSV
df = pd.read_csv('algoritmos.csv')

# Título principal
st.title('Análise de Algoritmos - Estrutura de Dados 2')

# Exibir o DataFrame completo se necessário
# st.write(df)
# st.markdown("<hr>", unsafe_allow_html=True)

# Converter as colunas numéricas de string para float, mantendo a formatação
def converter_para_float(valor):
    try:
        return float(valor.replace(',', '.'))
    except:
        return valor

df['Melhor'] = df['Melhor'].apply(converter_para_float)
df['Médio'] = df['Médio'].apply(converter_para_float)
df['Pior'] = df['Pior'].apply(converter_para_float)

# Obtendo os valores únicos da coluna 'Elementos'
valores_elementos = sorted(df['Elementos'].unique())

# Widget de seleção do número de elementos
num_elementos = st.selectbox('Selecione o número de elementos:', valores_elementos)

# Filtra o DataFrame com base no número de elementos selecionado
df_filtrado = df[df['Elementos'] == num_elementos]

# Gráfico de Desempenho Melhor
st.title(f'Desempenho Melhor para {num_elementos} elementos')
if df_filtrado['Melhor'].max() == 0:
    fig_melhor = px.line(df_filtrado, x='Nome do algoritmo', y='Melhor')
    fig_melhor.update_layout(xaxis_tickangle=-45, yaxis_title='Microssegundos', yaxis_range=[-1,1])  
else:
    fig_melhor = px.bar(df_filtrado, x='Nome do algoritmo', y='Melhor', color='Melhor', color_continuous_scale=["#FFFFFF", "#00FF00"])
    fig_melhor.update_layout(xaxis_tickangle=-45, yaxis_title='Microssegundos')
    fig_melhor.update_traces(hovertemplate='Melhor: %{y:.3f}')  # Formatação do hover

st.plotly_chart(fig_melhor)
st.markdown("<hr>", unsafe_allow_html=True)

# Gráfico de Desempenho Médio
st.title(f'Desempenho Médio para {num_elementos} elementos')
fig_media = px.bar(df_filtrado, x='Nome do algoritmo', y='Médio', color='Médio', color_continuous_scale=["#FFFFFF", "#00FF00"])
fig_media.update_layout(xaxis_tickangle=-45, yaxis_title='Microssegundos')
fig_media.update_traces(hovertemplate='Médio: %{y:.3f}')  # Formatação do hover

st.plotly_chart(fig_media)
st.markdown("<hr>", unsafe_allow_html=True)

# Gráfico de Pior Desempenho
st.title(f'Pior Desempenho para {num_elementos} elementos')
fig_pior = px.bar(df_filtrado, x='Nome do algoritmo', y='Pior', color='Pior', color_continuous_scale=["#FFFFFF", "#00FF00"])
fig_pior.update_layout(xaxis_tickangle=-45, yaxis_title='Microssegundos')
fig_pior.update_traces(hovertemplate='Pior: %{y:.3f}')  # Formatação do hover

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

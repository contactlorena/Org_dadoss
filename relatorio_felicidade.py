import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuração da página
st.set_page_config(page_title="Relatório Mundial da Felicidade 2023", page_icon="🌍", layout="wide")

# Título centralizado
st.title("Relatório Mundial da Felicidade 2023")

# Barra lateral de navegação
st.sidebar.title("Menu")
selecao = st.sidebar.radio("Escolha um tópico", ["Introdução", "Dataset de Felicidade", "Fatores que Influenciam a Felicidade", "Conclusões"])

# Conteúdo conforme a seleção do menu
if selecao == "Introdução":
    st.subheader("Introdução ao Relatório Mundial da Felicidade")
    st.write("""
        O Relatório Mundial da Felicidade 2023 é uma análise das condições de felicidade global, realizada anualmente pelas Nações Unidas. 
        O relatório leva em consideração diversos fatores sociais, econômicos e psicológicos que afetam o bem-estar das populações ao redor do mundo.
        
        O objetivo deste estudo é fornecer uma visão abrangente do estado da felicidade em diferentes países e ajudar os governos a implementar políticas que promovam o bem-estar.
    """)

elif selecao == "Dataset de Felicidade":
    st.subheader("Análise do Dataset de Felicidade")
    st.write("""
        Abaixo você encontrará uma análise detalhada do dataset de Felicidade de 2023, que inclui indicadores como PIB per capita, suporte social, expectativa de vida saudável, entre outros.
    """)

    
    df = pd.read_csv(r'C:\Users\vales\Documents\WHR2023.csv')  

    # Exibir primeiras linhas do dataframe
    st.write("Primeiras linhas do dataset:")
    st.dataframe(df.head())

    # Informações sobre o dataset
    st.write("Informações do dataset:")
    st.text(df.info())

    # Descrição estatística
    st.write("Descrição estatística do dataset:")
    st.text(df.describe())

    # Verificação de dados nulos
    st.write("Quantidade de valores nulos por coluna:")
    st.text(df.isnull().sum())

    # Gráfico: Distribuição do Ladder Score
    st.subheader("Distribuição do Ladder Score")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Ladder score'], kde=True, color='skyblue', bins=20)
    plt.title('Distribuição do Ladder Score (Índice de Felicidade)', fontsize=14)
    plt.xlabel('Ladder Score', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    st.pyplot()

    #Grafico de distribuição do PIB per capta
    st.subheader("Distribuição do PIB per capta")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Logged GDP per capita'], kde=True, color='skyblue', bins=20)
    plt.title('Distribuição do PIB per capita', fontsize=14)
    plt.xlabel('PIB per capita (log)', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    st.pyplot()

    #Grafico de Relação entre PIB per capita e Ladder
    st.subheader("Relação entre PIB per capita e Ladder")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Logged GDP per capita', y='Ladder score', color='green')
    plt.title('Relação entre PIB per capita e Ladder Score', fontsize=14)
    plt.xlabel('Logged GDP per capita', fontsize=12)
    plt.ylabel('Ladder Score', fontsize=12)
    st.pyplot()


    # Gráfico: Relação entre Suporte Social e Ladder Score
    st.subheader("Relação entre Suporte Social e Ladder Score")
    bins = np.linspace(df['Social support'].min(), df['Social support'].max(), 10)
    labels = [f'{round(bins[i], 2)}-{round(bins[i+1], 2)}' for i in range(len(bins)-1)]
    df['Social support bins'] = pd.cut(df['Social support'], bins=bins, labels=labels, include_lowest=True)

    df_grouped = df.groupby('Social support bins', observed=False)['Ladder score'].mean()

    plt.figure(figsize=(12, 6))
    df_grouped.plot(kind='bar', color='orange')

    plt.title('Relação entre Suporte Social e Ladder Score (Agrupado por Faixas)', fontsize=14)
    plt.xlabel('Faixas de Social Support', fontsize=12)
    plt.ylabel('Média do Ladder Score', fontsize=12)
    plt.xticks(rotation=45)

    plt.tight_layout()
    st.pyplot()

    #Grafico de Distribuição do Suporte Social
    st.subheader("Distribuição do Suporte Social")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Social support'], kde=True, color='green', bins=20)
    plt.title('Distribuição do Suporte Social', fontsize=14)
    plt.xlabel('Suporte Social', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    st.pyplot()


    # Gráfico: Relação entre Expectativa de Vida Saudável e Ladder Score
    st.subheader("Relação entre Expectativa de Vida Saudável e Ladder Score")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Healthy life expectancy', y='Ladder score', color='blue')
    plt.title('Relação entre Expectativa de Vida Saudável e Ladder Score', fontsize=14)
    plt.xlabel('Healthy Life Expectancy', fontsize=12)
    plt.ylabel('Ladder Score', fontsize=12)
    st.pyplot()

    #Grafico de Distribuição da Expectativa de Vida Saudável
    st.subheader("Distribuição da Expectativa de Vida Saudável")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Healthy life expectancy'], kde=True, color='orange', bins=20)
    plt.title('Distribuição da Expectativa de Vida Saudável', fontsize=14)
    plt.xlabel('Expectativa de Vida Saudável', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    st.pyplot()

    #Grafico de Distribuição da Percepção de Corrupção
    st.subheader("Distribuição da Percepção de Corrupção")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Perceptions of corruption'], kde=True, color='brown', bins=20)
    plt.title('Distribuição das Percepções de Corrupção', fontsize=14)
    plt.xlabel('Percepções de Corrupção', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    st.pyplot()

    #Grafico de Relação entre Liberdade de Fazer Escolhas e Ladder Score
    st.subheader("Relação entre Liberdade de Fazer Escolhas e Ladder Score")
    plt.figure(figsize=(10, 6))
    sns.regplot(x='Freedom to make life choices', y='Ladder score', data=df, scatter_kws={'color':'red'}, line_kws={'color':'blue'})
    plt.title('Relação Suavizada entre Liberdade de Fazer Escolhas e Ladder Score', fontsize=14)
    plt.xlabel('Freedom to make life choices', fontsize=12)
    plt.ylabel('Ladder Score', fontsize=12)
    st.pyplot()

    #Grafico de Distribuição da Liberdade de Fazer Escolhas
    st.subheader("Distribuição da Liberdade de Fazer Escolhas")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Freedom to make life choices'], kde=True, color='purple', bins=20)
    plt.title('Distribuição da Liberdade de Fazer Escolhas', fontsize=14)
    plt.xlabel('Liberdade de Fazer Escolhas', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    st.pyplot()

    #Grafico de Relação entre Generosidade e Ladder Score
    st.subheader("Relação entre Generosidade e Ladder Score")
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='Generosity', y='Ladder score', cmap='Purples', binwidth=0.1, cbar=True)
    plt.title('Distribuição entre Generosidade e Ladder Score', fontsize=14)
    plt.xlabel('Generosity', fontsize=12)
    plt.ylabel('Ladder Score', fontsize=12)
    st.pyplot()

    #Grafico de Relação entre Percepções de Corrupção e Ladder Score
    st.subheader("Relação entre Percepções de Corrupção e Ladder Score")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Perceptions of corruption', y='Ladder score', color='brown')
    plt.title('Relação entre Percepções de Corrupção e Ladder Score', fontsize=14)
    plt.xlabel('Perceptions of corruption', fontsize=12)
    plt.ylabel('Ladder Score', fontsize=12)
    st.pyplot()

elif selecao == "Fatores que Influenciam a Felicidade":
    st.subheader("Fatores que Influenciam a Felicidade")
    st.write("""
        Diversos fatores contribuem para a felicidade de um país e seus cidadãos. Alguns dos principais fatores são:
        
        - **PIB per capita**: Renda mais alta está correlacionada com maior felicidade.
        - **Suporte social**: A presença de uma rede de apoio influencia diretamente o bem-estar.
        - **Expectativa de vida saudável**: Maior longevidade e saúde são componentes essenciais para a felicidade.
        - **Liberdade para tomar decisões**: A capacidade de escolher seu próprio caminho é um fator importante.
        - **Generosidade e falta de corrupção**: Sociedades mais generosas e com menor corrupção tendem a ser mais felizes.
    """)

elif selecao == "Conclusões":
    st.subheader("Conclusões do Relatório")
    st.write("""
        O Relatório Mundial da Felicidade 2023 mostra que os países mais felizes geralmente possuem uma boa combinação de estabilidade social, confiança nas pessoas e nas instituições, e um sistema de bem-estar eficiente. Esses fatores ajudam a criar uma vida melhor para as pessoas. Porém, o relatório também aponta que existe uma diferença grande de felicidade entre os países. Regiões que enfrentam crises econômicas ou sociais acabam tendo índices de felicidade bem mais baixos.

A felicidade global está muito ligada a ter oportunidades de vida, confiança no governo e apoio das pessoas ao nosso redor. Além disso, a pandemia de COVID-19 mexeu bastante com a forma como as pessoas enxergam a felicidade, mostrando que a saúde mental e o apoio social são mais importantes do que nunca. Isso reforça que, além de investir na economia, é essencial cuidar das pessoas e garantir uma vida digna para todos.
    """)

# Rodapé
st.markdown("---")
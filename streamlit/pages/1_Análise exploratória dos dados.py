from nltk.corpus import stopwords
import nltk
import os
import io
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

import seaborn as sns  # visualization tool
import matplotlib
import matplotlib.pyplot as plt
import missingno as msno
import streamlit as st

from sklearn.impute import SimpleImputer
import plotly.express as px

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.compose import make_column_transformer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

nltk.download('stopwords')
nltk.download('punkt')

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Food Recipes Dataset Exploratory Data Analysis')

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "Exploração dos dados",
        "Limpeza dos dados",
        "Seleção de colunas",
        "Tratamento de atributos categóricos",
        "Escalonamento de valores",
        "Visualização e Análise"
    ]
)
with tab1:
    st.header('1. Exploração dos dados')
    st.write('''
    O datase contêm 8009 linhas e 16 colunas, o dataset reune diversas informações relacionados a receita
    ''')
    df = pd.read_csv("data/data.csv", ",")
    st.dataframe(df.head())
    st.subheader('1.1. Análises do tipo das variáveis')
    st.text(df.columns)
    st.write('''
    1. recipe_title: Variável categórica nominal, informa os títulos das receitas. 
    2. URL: Variável categórica nominal, informa o link de no qual foi obtido as informações da receita
    3. record_health: Coluna cujo a interpretação é confusa, pois só possui um único valor categórico. 
    4. vote_count: Variável numérica discreta, contabiliza a quantidade de votos de uma receita. 
    5. rating: Variável numérica contínua, informa a avaliação da receita pelo público. 
    6. description: Variável categórica nominal, se trata de uma breve descrição da receita. 
    7. cuisine: Variável categórica ordinal, informa a cozinha regional da receita. 
    8. course: Variável categórica ordinal, informa o tipo do prato. 
    9. diet: Variável categórica ordinal, informa qual dieta engloba a receita. 
    10. prep_time: Variável numérica contínua, informa o tempo de preparação da receita. 
    11. cook_time: Variável numérica contínua, informa o tempo de cozimento da receita.
    12. ingredients: Variável categórica nominal, informa os ingredientes presentes na receita, mas não informa quantidade. 
    13. instructions: Variável categórica nominal, armazena a instrução de preparo da receita. 
    14. author: Variável categórica nominal, armazena o nome do autor. 
    15. tags: Variável categórica ordinal, armazena as tags da receita. 
    16. category: Variável categórica ordinal, armazena a categoria da receita. 
    ''')

    st.subheader('1.2. Visualização dos dados')
    col1, col2 = st.columns(2)
    with col1:
        st.text((df.isna().sum()))
    with col2:
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)
    sns.set_style('dark')
    sns.set_theme(color_codes=True)

    st.line_chart((df.isna().sum()))

    col1, col2 = st.columns(2)
    with col1:
        # this column must be dropped
        graph = sns.countplot(x=df['record_health'])
        st.text(graph)
        st.pyplot()
    with col2:
        h = sns.histplot(x='diet', data=df, bins=20)
        plt.xticks(rotation=90)
        plt.tight_layout()
        st.text(h)
        st.pyplot()
with tab2:
    st.header('2. Limpeza dos dados')
    st.subheader("2.1. Visualização dos dados")
    matrix = msno.matrix(df)
    st.text(matrix)
    st.pyplot()

    st.dataframe(df.head(3))

    cols_with_missing = [col for col in df.columns if df[col].isnull().any()]
    st.subheader("2.2. Exclusão de linhas e colunas")
    st.write("Excluir receitas duplicatas e linhas com valores nulos nas colunas de ingredientes, instruções, título de receita e dieta.")
    df = df.dropna(
        subset=['ingredients', 'instructions', 'recipe_title', 'diet'])
    df = df.drop(['url', 'record_health'], axis=1)
    st.text(df.columns)
    st.dataframe(df.head(3))

    st.subheader("2.3. Tratamento do tipo das variáveis")
    st.write('''
    - Alterar o tipo das variáveis nas colunas de tempo de preparação e tempo de cozimento;
    - Transformar strings nas colunas de ingredientes e tags para listas com várias strings;
    - Formatação dos dados da coluna de instrução;
    ''')

    df['ingredients'] = df['ingredients'].apply(lambda x: x.split('|'))
    df['instructions'] = df['instructions'].apply(lambda x: x.replace('|', ''))
    df['tags'] = df['tags'].apply(
        lambda x: x.split('|') if type(x) != float else x)
    df['prep_time'] = df['prep_time'].apply(lambda x: int(
        x.replace('M', '')) if type(x) != float else x)
    df['cook_time'] = df['cook_time'].apply(lambda x: int(
        x.replace('M', '')) if type(x) != float else x)

    st.dataframe(
        df[['ingredients', 'instructions', 'tags', 'prep_time', 'cook_time']])
    st.subheader("2.4. Tratamento de valores ausentes")

    df['cook_time'].fillna(df['cook_time'].mean(), inplace=True)
    df['prep_time'].fillna(df['prep_time'].mean(), inplace=True)

    st.line_chart((df.isna().sum()))

with tab3:
    st.header('3. Seleção de colunas')
    st.write("""A seleção de dados para o treinamento do nosso modelo é uma etapa crucial no desenvolvimento do modelo de Machine Learning.
    
    Dessa forma, as colunas selecionadas para treinamento e validação de modelo serão: 
    1. vote_count: Variável numérica discreta, contabiliza a quantidade de votos de uma receita.
    2. rating: Variável numérica contínua, informa a avaliação da receita pelo público. 
    3. description: Variável categórica nominal, se trata de uma breve descrição da receita. 
    4. cuisine: Variável categórica nominal, informa a cozinha regional da receita. 
    5. course: Variável categórica nominal, informa o tipo do prato. 
    6. diet: Variável categórica nominal, informa qual dieta engloba a receita. 
    7. prep_time: Variável numérica contínua, informa o tempo de preparação da receita. 
    8. cook_time: Variável numérica contínua, informa o tempo de cozimento da receita.
    9. ingredients: Variável categórica nominal, informa os ingredientes presentes na receita, mas não informa quantidade. 
    10. instructions: Variável categórica nominal, armazena a instrução de preparo da receita. 
    12. category: Variável categórica nominal, armazena a categoria da receita. """)

    x = df.iloc[:, [1, 2, 3, 4, 5, 6, 7, 8, 13]]
    st.dataframe(x.head(3))

with tab4:
    st.header('4. Tratamento de atributos categóricos')
    st.write(
        """O modelo de Machine Learning somente trabalha com valores numéricos e não com strings. Dessa forma, será utilizado o módulo [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) disponibilizado pela biblioteca [Sklearn](https://scikit-learn.org/stable/).""")
    st.write("""As colunas que terão seus atributos categóricos tratados são: """)
    st.write("""
    1. cuisine
    2. description
    3. course
    4. diet
    5. category
    """)
    st.write("O tratamendo da coluna 'description' será através do módulo TF-IDF Vectorizar da biblioteca Sklearn a fim de converter-la num formato numérico. O termo TF significa frequência do termo, enquanto IDF significa frequência de documento inversa. Dessa forma, o valor do TF-IDF aumenta de forma proporcional a frequência que aquele termo aparece em um determinado número de textos.")
    vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words=stopwords.words(
        'portuguese'), min_df=5, max_df=0.95)

    onehotencoder = ColumnTransformer(transformers=[('', OneHotEncoder(
    ), ['cuisine', 'course', 'diet', 'category'])], remainder='passthrough')
    x_new = onehotencoder.fit_transform(
        x[['cuisine', 'course', 'diet', 'category']]).toarray()
    st.dataframe(x_new[1:6, :])

    x_description = x['description'].values.astype('U')
    vectorizer = TfidfVectorizer(sublinear_tf=True, stop_words=stopwords.words(
        'portuguese'), min_df=5, max_df=0.95)
    x_description = vectorizer.fit_transform(x_description)
    x_description = x_description.toarray()


with tab5:
    st.header('5. Escalonamento de valores')
    st.write(
        """A fim de normalizar os valores numéricos existentes, será aplicado uma função de normalização disponibilizado pela biblioteca [Sklearn](https://scikit-learn.org/stable/) chamada **Standard Scaler**.""")

    x_new = scaler.fit_transform(x_new)
    st.dataframe(x_new[0:5, :])

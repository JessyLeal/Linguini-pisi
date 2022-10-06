import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

import seaborn as sns  # visualization tool
import matplotlib
import matplotlib.pyplot as plt
import missingno as msno
import streamlit as st

from sklearn.impute import SimpleImputer
import plotly.express as px

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Clustering Model')

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Seleção de ingredientes para o cluster",
        "Matriz de correlação de ingredientes",
        "Método do Cotovelo",
        "Método da Silhueta"
    ]
)

with tab1:
    st.header('1. Selecionando ingredientes para a clusterização')
    col1, col2 = st.columns(2)
    with col1:
        df_ingr = pd.read_csv('data\ingredients2.csv')
        st.text(df_ingr.iloc[:, 0:])

    with col2:
        st.line_chart(data=df_ingr.iloc[:, 1:])
with tab2:
    st.header('2. Análise da matriz de correlação dos ingredientes')

    corr_ingr = pd.read_csv("data\corr_ingr.csv").iloc[:, 1:]

    matrix = np.triu(corr_ingr)
    f, ax = plt.subplots(figsize=(25, 14))
    h = sns.heatmap(corr_ingr, cmap="flare", mask=matrix,
                    linewidths=.2, annot=True)
    st.text(h)
    st.pyplot()

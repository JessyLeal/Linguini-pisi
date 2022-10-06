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

with tab3:
    st.header("3. Método do Colovelo")
    distortions = [2.85965842801772, 2.749594309651305, 2.708398609670136, 2.668235931460964, 2.6244524151268402, 2.6035607619026813, 2.575307367320609, 2.555666580882066, 2.536270044522046, 2.5126697866737477, 2.4927905385014766, 2.4894405655798333, 2.462116390057049, 2.460891111038134, 2.455198532597521, 2.4378996398711066, 2.4409383258936943, 2.4197401187610934, 2.4160916915049966, 2.4096465193318464]

    inertias = [64331.28217890172, 60454.766096270076, 58758.2910447342, 57235.51021661238, 55807.16593600383, 54671.82297837343, 53659.03261114535, 52892.17437593758, 52231.90349021995, 51726.617813395635, 51086.22760545593, 50747.15691914297, 50224.85331455058, 49830.86961951273, 49713.681682624316, 49327.245053800216, 49096.88514314346, 48872.937054915616, 48480.441873601114, 48340.28443255428]

    sns.set(style="darkgrid") 


    col1, col2 = st.columns(2)
    with col1:
        f, ax = plt.subplots(figsize=(5, 4.25))
        p = sns.lineplot(y = inertias, x = range(1, 21));
        plt.title('Método do Cotovelo usando Inércia')
        p.set_xlabel("k", fontsize = 12);
        p.set_ylabel("Inertia", fontsize = 12);

        st.pyplot()
        
    with col2:
        f, ax = plt.subplots(figsize=(5, 4))
        p = sns.lineplot(y = distortions, x = range(1, 21));
        plt.title('Método do Cotovelo usando distorção')
        p.set_xlabel("k", fontsize = 12);
        p.set_ylabel("Distorção", fontsize = 12);

        st.pyplot()

with tab4: 
    st.header("4. Método da Silhueta")

    st.code("""
    For no of clusters = 2  The average silhouette_score is : 0.0946921700155199
    For no of clusters = 3  The average silhouette_score is : 0.05428667840264565
    For no of clusters = 4  The average silhouette_score is : 0.07509431883083256
    For no of clusters = 5  The average silhouette_score is : 0.044191703617342086
    For no of clusters = 6  The average silhouette_score is : 0.048531114287358866
    For no of clusters = 7  The average silhouette_score is : 0.04980574097266969
    For no of clusters = 8  The average silhouette_score is : 0.052647760970409935
    For no of clusters = 9  The average silhouette_score is : 0.0544814181778927
    For no of clusters = 10  The average silhouette_score is : 0.03217131104319553
    For no of clusters = 11  The average silhouette_score is : 0.033002965302722516
    For no of clusters = 12  The average silhouette_score is : 0.045060532967220346
    For no of clusters = 13  The average silhouette_score is : 0.033570599671632034
    For no of clusters = 14  The average silhouette_score is : 0.035908689729619546
    For no of clusters = 15  The average silhouette_score is : 0.021948798134996297
    For no of clusters = 16  The average silhouette_score is : 0.020590503683421683
    For no of clusters = 17  The average silhouette_score is : 0.030523749654333302
    For no of clusters = 18  The average silhouette_score is : 0.021231046764328507
    For no of clusters = 19  The average silhouette_score is : 0.02372268639866818
    For no of clusters = 20  The average silhouette_score is : 0.022521662512775213
    """)
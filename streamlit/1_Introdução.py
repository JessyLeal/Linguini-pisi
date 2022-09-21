import streamlit as st

st.title("Introdução ao dataset Food Recipes")
st.image('streamlit\src\image.jpg')
st.header("Conteúdo")
st.write("""
O dataset possui mais de 8000 receitas com uma ampla variedade de cozinhas globais distintas, entretanto com o foco na cozinha indiana. Dessa forma, a maior parte das receitas são indianas. Além disso, é possível encontrar informações tal como dieta, tempo de preparação, tempo de cozimento, tipo de prato, tipo de cozinha, descrição, avaliação, e entre outros. 

O dataset tem a usabilidade igual a 8.82, o que indica que grande parte dos dados do dataset estão presentes,  16 colunas e o tamanho de 19.35 MB. 
""")
st.header("Aplicativo Linguini")
st.write("""
O desenvolvimento do projeto Linguini resulta na criação de uma aplicação no qual a premissa se dá na necessidade dos usuários, em sua maioria vegetarianos, de encontrar receitas de pratos acessíveis e diversos concernentes com as preferências individuais de cada utilizador.

O aplicativo é desenvolvido em dart com o framework Flutter, 
""")
st.subheader("Time de desenvolvimento")
col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.image("streamlit\src\dan.jpg", width=125)
    st.caption('Danielly Egito')
with col2:
    st.image("streamlit\src\jorge.jpg", width=125)
    st.caption('Jorge Lucas')
with col3:
    st.image("streamlit\src\pvictao.jpg", width=125)
    st.caption('Vyctor Costa')
with col4:
    st.image("streamlit\src\debs.jpg", width=125)
    st.caption('Débora Silva')
with col5:
    st.image("streamlit\src\lip.jpg", width=125)
    st.caption('Fellipe Domingues')
with col6:
    st.image("streamlit\src\jess.jpeg", width=125)
    st.caption("""Jéssica Leal""")

st.header("Referência")
st.write("As receitas foram extraídas através do site [Archanas Kitchen](https://www.archanaskitchen.com), uma das plataformas de receitas mais acessadas na Índia,  e o dataset pode ser baixado através do link [Kaggle Food Recipes](https://www.kaggle.com/datasets/sarthak71/food-recipes).")

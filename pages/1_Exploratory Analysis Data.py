from packages import *

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
    df = pd.read_csv("data/food_recipes.csv", ",")
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
        graph = sns.countplot(x = df['record_health']); #this column must be dropped
        st.text(graph)
        st.pyplot();
    with col2:
        h = sns.histplot(x = 'diet',data = df, bins = 20);
        plt.xticks(rotation=90);
        plt.tight_layout()
        st.text(h)
        st.pyplot()
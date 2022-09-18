import os
import psycopg2
import pandas as pd
import time
from dotenv import load_dotenv

#! Execute o comando 'pip install -r requirements.txt' antes de rodar esse script.

load_dotenv()
DATABASE_URL = os.environ['DATABASE_URL']
reset_table = False #! Variavel de controle para deletar a tabela e criar uma nova caso seja True.
insert_data = False #! Variavel de controle para inserir as informações  caso seja True.
insert_ingredients = False #! Variavel de controle para inserir todos os ingredientes caso seja True.
path = os.path.abspath('./food_recipes_translated.csv.zip') 
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

#* Script para Criar as tables
if reset_table:
  cur.execute("DROP TABLE IF EXISTS public.data;")
  cur.execute("DROP TABLE IF EXISTS public.ingredients;")
  cur.execute("DROP TABLE IF EXISTS public.user;")

cur.execute("""CREATE TABLE IF NOT EXISTS public.data (
  id SERIAL PRIMARY KEY,
  recipe_title TEXT,
  vote_count INTEGER,
  rating REAL,
  description TEXT,
  cuisine TEXT,
  course TEXT,
  diet TEXT,
  prep_time REAL,
  cook_time REAL,
  ingredients TEXT,
  instructions TEXT,
  author TEXT,
  tags TEXT,
  category TEXT
);""")
cur.execute("""CREATE TABLE IF NOT EXISTS public.ingredients (
  id SERIAL PRIMARY KEY,
  ingredient TEXT
);""")
cur.execute("""CREATE TABLE IF NOT EXISTS public.user (
  id SERIAL PRIMARY KEY,
  username TEXT,
  password TEXT,
  email TEXT
);""")
#*----------------------------------------------------------------

#* Script para inserir as informações do dataset na tabela do BD.
#* Tempo de execução em média: 814 segundos.
df = pd.read_csv(path)
columns = list(df.columns);
columns.remove('ingredients')
columns.remove('tags')
columns.remove('Unnamed: 0.1')
columns.remove('Unnamed: 0')

a = time.time()
if insert_data:
  for i in range(len(df)):
    row = df.iloc[i]
    string_ingredients = row['ingredients'].replace('[', '').replace(']', '').replace("'", '').replace(', ', ' | ')
    string_tags = row['tags'].replace('[', '').replace(']', '').replace("'", '').replace(', ', ' | ')

    ar = [row[columns[0]].replace("'", "''"), row[columns[1]], row[columns[2]], row[columns[3]].replace("'", "''"), row[columns[4]].replace("'", "''"), row[columns[5]].replace("'", "''"), row[columns[6]].replace("'", "''"), row[columns[7]], row[columns[8]], row[columns[9]].replace("'", "''"), row[columns[10]].replace("'", "''"), row[columns[10]].replace("'", "''")]

    cur.execute(f"INSERT INTO public.data VALUES (DEFAULT, '{ar[0]}', {ar[1]}, {ar[2]}, '{ar[3]}', '{ar[4]}', '{ar[5]}', '{ar[6]}', {ar[7]}, {ar[8]}, '{string_ingredients}', '{ar[9]}', '{ar[10]}', '{string_tags}', '{ar[11]}');")
#*----------------------------------------------------------------

#* Script para inserir os ingredientes.
#* Tempo de execução em média: 711 segundos.
if insert_ingredients:
  array_ingredients = [];
  for i in df['ingredients']:
    string = i.replace('[', '').replace(']', '').replace("'", '')
    ar = string.split(',')
    for j in ar:
      if not j in array_ingredients:
        array_ingredients.append(j)
  for ingredients in array_ingredients:
    ingredients = ingredients.strip()
    cur.execute(f"INSERT INTO public.ingredients VALUES (DEFAULT, '{ingredients}')")
#*----------------------------------------------------------------

conn.commit()
cur.close()
conn.close()
b = time.time()
print(f'Tempo levado: {abs(a-b)}')
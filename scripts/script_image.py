import os
import psycopg2
import time
from dotenv import load_dotenv
from google_images_search import GoogleImagesSearch

load_dotenv()
DATABASE_URL = os.environ['DATABASE_URL']
API_KEY = os.environ['API_KEY']
PROJECT_CX = os.environ['PROJECT_CX']

gis = GoogleImagesSearch(API_KEY, PROJECT_CX)

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()

cur.execute("SELECT id, recipe_title FROM public.data ORDER BY id ASC;")
arr = cur.fetchall();
for index, obj in enumerate(arr):
  a = time.time()
  _search_params = {
    'q': obj[1],
    'num': 1,
    'fileType': 'jpg|gif|png',
  }
  try:
    gis.search(search_params=_search_params)
    try:
      image = gis.results()[0].url
      cur.execute(f"UPDATE public.data SET image='{image}' WHERE id={obj[0]}")
      conn.commit()
      b = time.time()
      print(f'tempo: {abs(a-b)}')
      print(f'percentage: {index/len(arr)*100}%')
      print(f'id: {obj[0]}')
    except:
      b = time.time()
      print(f'tempo: {abs(a-b)}')
      print(f'percentage: {index/len(arr)*100}%')
      print(f'id: {obj[0]}')
      continue
  except:
    print(F'API_KEY: {API_KEY}')
    cur.close()
    conn.close()
    break

cur.close()
conn.close()

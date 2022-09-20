import os, io
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import seaborn as sns
import nltk
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

df = pd.read_csv("data\data-clean.csv")

df = df.drop(['Unnamed: 0.1'], axis=1)
df.rename(columns={'Unnamed: 0': 'id'}, inplace = True)

documents = df['description'].values.astype('U')
nltk.download('stopwords')
vectorizer = TfidfVectorizer(sublinear_tf=True,stop_words=stopwords.words('portuguese'), min_df = 5, max_df=0.95)
features = vectorizer.fit_transform(documents)
X = features.toarray()

k = 10
model = KMeans(n_clusters = k, init ='k-means++', max_iter = 100, n_init=1)
model.fit(X)  

pca = PCA(n_components=2, random_state=42)
pca_vecs = pca.fit_transform(X)
x0 = pca_vecs[:, 0]
x1 = pca_vecs[:, 1]

clusters = model.labels_
df['cluster'] = clusters
df['x0'] = x0
df['x1'] = x1
from packages import *
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

df = pd.read_csv("data\data_clean.csv")

df = df.drop(['Unnamed: 0.1'], axis=1)
df.rename(columns={'Unnamed: 0': 'id'}, inplace = True)

documents = df['description'].values.astype('U')

vectorizer = TfidfVectorizer(sublinear_tf=True,stop_words=stopwords.words('portuguese'), min_df = 5, max_df=0.95)
features = vectorizer.fit_transform(documents)
X = features.toarray()

k = 10
model = KMeans(n_clusters = k, init ='k-means++', max_iter = 100, n_init=1)
model.fit(X)  

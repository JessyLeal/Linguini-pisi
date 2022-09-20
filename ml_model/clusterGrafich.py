from main import *

print('Cluster centroids: \n')
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()

for i in range(k):
    print('Cluster %d: ' % i)
    for j in order_centroids[i, :35]:
        print('%s' % terms[j], end=' ')
    print()
    print('-----------------')

# Cluster graphic

plt.figure(figsize=(12, 7))
plt.title("Cluster Graphic", fontdict={"fontsize": 16})
plt.xlabel("X0", fontdict={"fontsize": 14})
plt.ylabel("X1", fontdict={"fontsize": 14})
sns.scatterplot(data=df, x='x0', y='x1', hue='cluster', palette="viridis")

plt.show()

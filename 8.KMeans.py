import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris=load_iris()
x=iris.data

def kmeans(x,k):
    centroids=x[np.random.choice(x.shape[0],k,replace=False)]
    
    for _ in range(100):
        distances=np.linalg.norm(x[:,None]-centroids,axis=2)
        labels=np.argmin(distances,axis=1)
        centroids=np.array([x[labels==i].mean(axis=0) for i in range(k)])
    return centroids,labels

k=3

centroids,labels=kmeans(x,k)

colors=['r','g','b']

for i in range(k):
    plt.scatter(x[labels==i,0],x[labels==i,1],c=colors[i],label=f'Cluster {i+1}')

plt.scatter(centroids[:,0],centroids[:,1],marker='x',c='black',label='Centroids')

plt.title("K means Clustering")
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
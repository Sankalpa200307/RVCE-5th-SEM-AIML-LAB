import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

iris=datasets.load_iris()
x=iris.data[:,:2]
y=(iris.target!=0)*1

sc=StandardScaler()
x=sc.fit_transform(x)
print(x[:5])

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=42)

class Logistic:
    def __init__(self):
        self.weigths=None
    def sigmoid(self,z):
        return 1.0/(1.0+np.exp(-z))
    def gradient(self,x,h,y):
        return np.dot(x.T,(h-y))/y.shape[0]
    
    def fit(self,x,y,num_iterations=200,learning_rate=0.01):
        self.weights=np.zeros(x.shape[1])
        for i in range(num_iterations):
            z=np.dot(x,self.weights)
            h=self.sigmoid(z)
            grad=self.gradient(x,h,y)
            self.weights=self.weights-learning_rate*grad
    def predict(self,x):
        z=np.dot(x,self.weights)
        return (self.sigmoid(z)>0.5)*1
    
lr=Logistic()

lr.fit(x_train,y_train)

y_pred=lr.predict(x_test)

print("The accuracy is ",np.mean(y_pred==y_test))

import matplotlib.pyplot as plt
plt.scatter(x_train[:,0],x_train[:,1],c=y_train)

plt.title("Logistic Regression")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal width")








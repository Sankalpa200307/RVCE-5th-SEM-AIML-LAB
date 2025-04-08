from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np
from collections import Counter as c
from sklearn.metrics import classification_report, confusion_matrix

iris = load_iris()
X, y, class_names = iris.data, iris.target, iris.target_names
k = 3

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=9)

pred = []
for i in X_test:
    distances = [np.linalg.norm(i - j) for j in X_train]
    topK = np.argsort(distances)[:k]
    nearestK = [y_train[i] for i in topK]
    most_common = c(nearestK).most_common(1)
    pred.append(most_common[0][0])
y_pred = np.array(pred)


print('Accuracy:', np.mean(y_pred == y_test))
print('Predictions:', class_names[y_pred])
print("\nConfusion Matrix:", confusion_matrix(y_test, y_pred))
print("\nClassification Report:", classification_report(y_test, y_pred))

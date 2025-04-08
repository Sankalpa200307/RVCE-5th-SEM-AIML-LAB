import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

iris = load_iris()
X, y, class_names = iris.data, iris.target, iris.target_names

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

pred = []
classes = np.unique(y_train)
mean = np.array([X_train[y_train == c].mean(axis=0) for c in classes])
var = np.array([X_train[y_train == c].var(axis=0) for c in classes])
priors = np.array([X_train[y_train == c].shape[0] / len(y_train) for c in classes])
for x_test in X_test:
    posteriors = []
    for idx, prior in enumerate(priors):
        m, v = mean[idx], var[idx]
        numerator = np.exp(- (x_test - m)**2 / (2 * v))
        denominator = np.sqrt(2 * np.pi * v)
        pdf = numerator / denominator
        posteriors.append(np.log(prior) + np.sum(np.log(pdf)))
    pred.append(classes[np.argmax(posteriors)])
y_pred = np.array(pred)

print('Accuracy:', np.mean(y_pred == y_test))
print("Predictions:", class_names[y_pred])
print("\nConfusion Matrix:", confusion_matrix(y_test, y_pred))
print("\nClassification Report:", classification_report(y_test, y_pred, target_names=class_names))

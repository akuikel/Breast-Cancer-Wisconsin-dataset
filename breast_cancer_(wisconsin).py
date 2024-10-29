# -*- coding: utf-8 -*-
"""Breast Cancer (Wisconsin).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10zqCLZ6jhK3jOnEfv_2Kfv6yuz3a7RBB

Loading the dataset
"""

from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
x = data.data
y = data.target
print(x.shape, y.shape)

print(df.isnull().sum())

"""Splitting the dataset into training set and testing set"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

"""  Training and evaluating three classifiers"""

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

logistic_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('logistic_regression', LogisticRegression())
])

svm_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC())
])

decision_tree_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('decision_tree', DecisionTreeClassifier())
])

logistic_pipeline.fit(x_train, y_train)
svm_pipeline.fit(x_train, y_train)
decision_tree_pipeline.fit(x_train, y_train)

"""Finding out the accuracy"""

logistic_pred = logistic_pipeline.predict(x_test)
svm_pred = svm_pipeline.predict(x_test)
decision_tree_pred = decision_tree_pipeline.predict(x_test)

print("Logistic Regression Accuracy:", accuracy_score(y_test, logistic_pred))
print("SVM Accuracy:", accuracy_score(y_test, svm_pred))
print("Decision Tree Accuracy:", accuracy_score(y_test, decision_tree_pred))

"""Visualizing the decision tree"""

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(20,10))
plot_tree(decision_tree_pipeline.named_steps['decision_tree'], feature_names=data.feature_names, class_names=data.target_names, filled=True)
plt.title("Decision Tree Visualization")
plt.savefig("decision_tree_visualization.png")  # Saves the image
plt.show()
import pandas as pd
import seaborn as sns
from bs4 import BeautifulSoup
import requests
import psycopg2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import  accuracy_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error



# Uzduotis
# X = np.random.randn(200, 2)
# y = (X[:, 0]+X[:, 1] > 0).astype(int)
# X_train, X_test = X[:150], X[150:]
# y_train, y_test = y[:150], y[150:]
# svm_classifier = SVC(kernel = 'linear', C = 1)
# svm_classifier.fit(X_train, y_train)
# y_pred = svm_classifier.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f'accuracy {accuracy:.2f}')  #2f yra 2 skai2iai po kablelio :)
# xx,yy=np.meshgrid(np.linspace(X[:, 0].min() -1, X[:, 0].max() +1, 100),
#                               np.linspace(X[:, 0].min() -1, X[:, 0].max() +1, 100))
# Z = svm_classifier.decision_function(np.c_[xx.ravel(), yy.ravel()])
# Z = Z.reshape(xx.shape)
# plt.contourf(xx, yy, Z, levels = [-1, 0, 1], alpha = 0.6, colors = ['red', 'blue'])
# plt.scatter(X[:, 0], X[:, 1], c = y, cmap = plt.cm.brg, edgecolors ='k')
# plt.xlabel('feature1')
# plt.ylabel('feature2')
# plt.title('Sprendimų ribos vizualizacija')
# plt.show()

# uzduotis
# np.random.seed(0)
# X = np.random.rand(100, 1)*10
# y = 3*X+np.random.randn(100,1)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
# regresor = LinearRegression()
# regresor.fit(X_train, y_train)
# forcast = regresor.predict(X_test)
# Vid_kv_nuokrypis = mean_squared_error(y_test, forcast)
# print(Vid_kv_nuokrypis)
# plt.scatter(X_test, y_test, color = 'blue', label = 'actual')
# plt.plot(X_test, forcast, color = 'red', label = 'predicted')
# plt.xlabel('X')
# plt.ylabel('y')
# plt.title('Tiesinė regresija (actual vs predicted)')
# plt.legend()
# plt.show()














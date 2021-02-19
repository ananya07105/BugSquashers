# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_irkU0gEa6raZ2TqA8a4nS3eQePzdmUq
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
basic = pd.read_csv('/content/location_Avail.csv')
basic.head()

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline

plt.scatter(basic['SOIL'],basic['STATE'])

le = preprocessing.LabelEncoder()
X1 = basic[["SOIL","Cotton"]]
y1 = basic["STATE"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(X1, y1,test_size=0.3)

len(X_train)

len(X_test)

len(y_train)

len(y_test)

X_train

X_test

y_train

y_test

from sklearn.linear_model import LinearRegression
clf = LinearRegression()
clf.fit(X_train, y_train)

X_test

clf.predict(X_test)

y_test


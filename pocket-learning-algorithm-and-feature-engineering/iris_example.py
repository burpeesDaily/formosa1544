# Copyright © 2017, 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""An example of supervised learning uses the Iris data set.
https://archive.ics.uci.edu/ml/datasets/Iris
Attribute Information:
0. sepal length in cm 
1. sepal width in cm 
2. petal length in cm 
3. petal width in cm 
4. class: 
-- Iris Setosa 
-- Iris Versicolour 
-- Iris Virginica
"""

import urllib.request

# matplotlib is a python 2D plotting library which produces publication
# quality. Figures in a variety of hardcopy formats and interactive
# environments across platforms.
# http://matplotlib.org/2.0.0/index.html
import matplotlib.pyplot as plt

# NumPy is the fundamental package for scientific computing with
# Python. http://www.numpy.org/
import numpy as np

# pandas is an open source library providing high-performance, 
# easy-to-use data structures and data analysis tools.
# http://pandas.pydata.org/
import pandas as pd

# Seaborn is a Python data visualization library based on matplotlib.
# It provides a high-level interface for drawing attractive and
# informative statistical graphics.
# http://seaborn.pydata.org/index.html
import seaborn as sns

sns.set() # set the default seaborn theme, scaling, and color palette.

import perceptron_classifier

# Download Iris Data Set from 
# http://archive.ics.uci.edu/ml/datasets/Iris
URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
urllib.request.urlretrieve(URL, "iris.data")
# use pandas" read_csv function to read iris.data into a python array.
# Note: the iris.data is headerless, so header is None.
IRIS_DATA = pd.read_csv("iris.data", header=None)

# Plot the versicolor and virginica.
VERSICOLOR = IRIS_DATA.iloc[50:100, [0, 2]].values
VIRGINICA = IRIS_DATA.iloc[100:150, [0, 2]].values

plt.scatter(VERSICOLOR[:, 0], VERSICOLOR[:, 1],
            color="blue", marker="x", label="versicolor")
plt.scatter(VIRGINICA[:, 0], VIRGINICA[:, 1],
            color="green", marker="v", label="virginica")

plt.xlabel("sepal length")
plt.ylabel("petal length")
plt.legend(loc="upper left")
plt.show()

# Use Perceptron Learning Algorithm onto the versicolor and virginica
# of the Iris Data Set.
VERSICOLOR_LABEL = IRIS_DATA.iloc[50:100, 4].values
VIRGINICA_LABEL = IRIS_DATA.iloc[100:150, 4].values
LABELS = np.append(VERSICOLOR_LABEL, VIRGINICA_LABEL)
SAMPLES = np.append(VERSICOLOR, VIRGINICA, axis=0)

perceptron_classifier = perceptron_classifier.PerceptronClassifier(
    number_of_attributes=2, class_labels=('Iris-versicolor', 'Iris-virginica'))

perceptron_classifier.train(SAMPLES, LABELS, 100)
plt.plot(perceptron_classifier.misclassify_record, color="purple")

# Plot the error rate and show it never converges.
plt.xlabel("number of iteration")
plt.ylabel("number of misclassification")
plt.legend(loc="lower right")
plt.show()
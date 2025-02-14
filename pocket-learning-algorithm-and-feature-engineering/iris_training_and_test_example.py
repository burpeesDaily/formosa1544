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

# pandas is an open source library providing high-performance,
# easy-to-use data structures and data analysis tools. http://pandas.pydata.org/
import pandas as pd

# scikit-learn is a python machine learning library. train_test_split
# function splits a data set to a train and a test subsets.
# http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
from sklearn import model_selection

import perceptron_classifier

# Download Iris Data Set from
# http://archive.ics.uci.edu/ml/datasets/Iris
URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
urllib.request.urlretrieve(URL, "iris.data")
# use pandas" read_csv function to read iris.data into a python array.
# Note: the iris.data is headerless, so header is None.
IRIS_DATA = pd.read_csv("iris.data", header=None)

# Try only versicolor and virginica
LABELS = IRIS_DATA.iloc[50:150, 4].values
DATA = IRIS_DATA.iloc[50:150, [0, 2]].values

# Use scikit-learn's train_test_split function to separate the
# Iris Data Set to a training subset (75% of the data) and
# a test subst (25% of the data)
DATA_TRAIN, DATA_TEST, LABELS_TRAIN, LABELS_TEST = model_selection.train_test_split(
    DATA, LABELS, test_size=0.25, random_state=1000
)

perceptron_classifier = perceptron_classifier.PerceptronClassifier(
    number_of_attributes=2, class_labels=("Iris-versicolor", "Iris-virginica")
)

perceptron_classifier.train(DATA_TRAIN, LABELS_TRAIN, 100)
result = perceptron_classifier.classify(DATA_TEST)

misclassify = 0
for predict, answer in zip(result, LABELS_TEST):
    if predict != answer:
        misclassify += 1

print("Accuracy rate: %2.2f" % (100 * (len(result) - misclassify) / len(result)) + "%")

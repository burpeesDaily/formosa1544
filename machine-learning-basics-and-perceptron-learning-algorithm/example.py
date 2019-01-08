import urllib.request

import numpy as np
import pandas as pd

import perceptron_classifier # Perceptron classifier

# Download Iris Data Set from http://archive.ics.uci.edu/ml/datasets/Iris
URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
urllib.request.urlretrieve(URL, "iris.data")
# Use pandas.read_csv module to load iris data set
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
IRIS_DATA = pd.read_csv("iris.data", header=None)

# Prepare the training data and test data
# The original Iris Data Set has 150 samples and 50 samples for each
# class. This example takes first 40 samples of each class as training
# data, and the other 10 samples of each class as testing data.
# So, this example uses the testing data to verify the trained
# Perceptron learning model.
# 0 ~ 39: setosa training set
# 40 ~ 49: setosa testing set
# 50 ~ 89 versicolor training set
# 90 ~ 99: versicolor testing set
# 100 ~ 139: virginica training set
# 140 ~ 149: virginica testing set
# Use pandas iloc to select samples by position and return an
# one-dimension array
# http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc
SETOSA_LABEL = IRIS_DATA.iloc[0:40, 4].values
VERSICOLOR_LABEL = IRIS_DATA.iloc[50:90, 4].values
VIRGINICA_LABEL = IRIS_DATA.iloc[100:140, 4].values

SETOSA_VERSICOLOR_TRAINING_LABEL = np.append(SETOSA_LABEL, VERSICOLOR_LABEL)
SETOSA_VIRGINICA_TRAINING_LABEL = np.append(SETOSA_LABEL, VIRGINICA_LABEL)
VERSICOLOR_VIRGINICA_TRAINING_LABEL = np.append(VERSICOLOR_LABEL,
                                                VIRGINICA_LABEL)

# In this example, it uses only Sepal width and Petal width to train.
SETOSA_DATA = IRIS_DATA.iloc[0:40, [1, 3]].values
VERSICOLOR_DATA = IRIS_DATA.iloc[50:90, [1, 3]].values
VIRGINICA_DATA = IRIS_DATA.iloc[100:140, [1, 3]].values

# Use one-vs-one strategy to train three classes data set, so we need
# three binary classifiers: 
# setosa-versicolor, setosa-viginica, and versicolor-viginica
SETOSA_VERSICOLOR_TRAINING_DATA = np.append(
    SETOSA_DATA, VERSICOLOR_DATA, axis=0)

SETOSA_VIRGINICA_TRAINING_DATA = np.append(
    SETOSA_DATA, VIRGINICA_DATA, axis=0)

VERSICOLOR_VIRGINICA_TRAINING_DATA = np.append(
    VERSICOLOR_DATA, VIRGINICA_DATA, axis=0)

# Prepare test data set. Use only Sepal width and Petal width as well.
SETOSA_TEST = IRIS_DATA.iloc[40:50, [1, 3]].values
VERSICOLOR_TEST = IRIS_DATA.iloc[90:100, [1, 3]].values
VIRGINICA_TEST = IRIS_DATA.iloc[140:150, [1, 3]].values
TEST = np.append(SETOSA_TEST, VERSICOLOR_TEST, axis=0)
TEST = np.append(TEST, VIRGINICA_TEST, axis=0)

# Prepare the target of test data to verify the prediction
SETOSA_VERIFY = IRIS_DATA.iloc[40:50, 4].values
VERSICOLOR_VERIFY = IRIS_DATA.iloc[90:100, 4].values
VIRGINICA_VERIFY = IRIS_DATA.iloc[140:150, 4].values
VERIFY = np.append(SETOSA_VERIFY, VERSICOLOR_VERIFY)
VERIFY = np.append(VERIFY, VIRGINICA_VERIFY)

# Define a setosa-versicolor Perceptron() with 2 attributes
perceptron_setosa_versicolor = perceptron_classifier.PerceptronClassifier(
    number_of_attributes=2, class_labels=("Iris-setosa", "Iris-versicolor"))

# Train the model
perceptron_setosa_versicolor.train(
    SETOSA_VERSICOLOR_TRAINING_DATA, SETOSA_VERSICOLOR_TRAINING_LABEL)

# Define a setosa-virginica Perceptron() with 2 attributes
perceptron_setosa_virginica = perceptron_classifier.PerceptronClassifier(
    number_of_attributes=2, class_labels=("Iris-setosa", "Iris-virginica"))

# Train the model
perceptron_setosa_virginica.train(
    SETOSA_VIRGINICA_TRAINING_DATA, SETOSA_VIRGINICA_TRAINING_LABEL)

# Define a versicolor-virginica Perceptron() with 2 attributes
perceptron_versicolor_virginica = perceptron_classifier.PerceptronClassifier(
    number_of_attributes=2, class_labels=("Iris-versicolor", "Iris-virginica"))

# Train the model
perceptron_versicolor_virginica.train(VERSICOLOR_VIRGINICA_TRAINING_DATA,
                                      VERSICOLOR_VIRGINICA_TRAINING_LABEL)

# Run three binary classifiers
predict_target_1 = perceptron_setosa_versicolor.classify(TEST)
predict_target_2 = perceptron_setosa_virginica.classify(TEST)
predict_target_3 = perceptron_versicolor_virginica.classify(TEST)

overall_predict_result = []
for item in zip(predict_target_1, predict_target_2, predict_target_3):
    unique, counts = np.unique(item, return_counts=True)
    temp_result = (zip(unique, counts))
    # Sort by values and return the class that has majority votes
    overall_predict_result.append(
        sorted(temp_result, reverse=True, key=lambda tup: tup[1])[0][0])
    # The result should look like:
    # [("Iris-setosa", 2), ("Iris-versicolor", 1)]
    # [("Iris-setosa", 2), ("Iris-versicolor", 1)]
    # [("Iris-setosa", 2), ("Iris-versicolor", 1)]
    # [("Iris-setosa", 2), ("Iris-versicolor", 1)]
    # [("Iris-setosa", 2), ("Iris-versicolor", 1)]
    # [("Iris-setosa", 2), ("Iris-versicolor", 1)]
    # [("Iris-setosa", 2), ("Iris-versicolor", 1)]
    # [("Iris-setosa", 2), ("Iris-versicolor", 1)]
    # [("Iris-setosa", 2), ("Iris-versicolor", 1)]
    # [("Iris-setosa", 2), ("Iris-versicolor", 1)]
    # [("Iris-versicolor", 2), ("Iris-virginica", 1)]
    # [("Iris-versicolor", 2), ("Iris-virginica", 1)]
    # [("Iris-versicolor", 2), ("Iris-virginica", 1)]
    # [("Iris-versicolor", 2), ("Iris-virginica", 1)]
    # [("Iris-versicolor", 2), ("Iris-virginica", 1)]
    # [("Iris-versicolor", 2), ("Iris-virginica", 1)]
    # [("Iris-versicolor", 2), ("Iris-virginica", 1)]
    # [("Iris-versicolor", 2), ("Iris-virginica", 1)]
    # [("Iris-versicolor", 2), ("Iris-virginica", 1)]
    # [("Iris-versicolor", 2), ("Iris-virginica", 1)]
    # [("Iris-virginica", 2), ("Iris-versicolor", 1)]
    # [("Iris-virginica", 2), ("Iris-versicolor", 1)]
    # [("Iris-virginica", 2), ("Iris-versicolor", 1)]
    # [("Iris-virginica", 2), ("Iris-versicolor", 1)]
    # [("Iris-virginica", 2), ("Iris-versicolor", 1)]
    # [("Iris-virginica", 2), ("Iris-versicolor", 1)]
    # [("Iris-virginica", 2), ("Iris-versicolor", 1)]
    # [("Iris-virginica", 2), ("Iris-versicolor", 1)]
    # [("Iris-virginica", 2), ("Iris-versicolor", 1)]
    # [("Iris-virginica", 2), ("Iris-versicolor", 1)]

# Verify the results
misclassified = 0
for predict, verify in zip(overall_predict_result, VERIFY):
    if predict != verify:
        misclassified += 1
print("The number of misclassified: " + str(misclassified))
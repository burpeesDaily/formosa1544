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
# quality. Figures in a variety of formats and interactive
# environments across platforms.
# http://matplotlib.org/2.0.0/index.html
import matplotlib.pyplot as plt

# pandas is an open source library providing high-performance,
# easy-to-use data structures and data analysis tools.
# http://pandas.pydata.org/
import pandas as pd

# Seaborn is a Python data visualization library based on matplotlib.
# It provides a high-level interface for drawing attractive and
# informative statistical graphics.
# http://seaborn.pydata.org/index.html
import seaborn as sns

sns.set_theme()  # set the default seaborn theme, scaling, and color palette.

# Download Iris Data Set from
# http://archive.ics.uci.edu/ml/datasets/Iris
URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
urllib.request.urlretrieve(URL, "iris.data")
# use pandas read_csv function to read iris.data into a python array.
# Note: the iris.data is headerless, so header is None.
IRIS_DATA = pd.read_csv("iris.data", header=None)

SETOSA = IRIS_DATA.iloc[0:50, [0, 2]].values
VERSICOLOR = IRIS_DATA.iloc[50:100, [0, 2]].values
VIRGINICA = IRIS_DATA.iloc[100:150, [0, 2]].values

plt.scatter(SETOSA[:, 0], SETOSA[:, 1],
            color="red", marker="o", label="setosa")
plt.scatter(VERSICOLOR[:, 0], VERSICOLOR[:, 1],
            color="blue", marker="x", label="versicolor")
plt.scatter(VIRGINICA[:, 0], VIRGINICA[:, 1],
            color="green", marker="v", label="virginica")

plt.xlabel("sepal length")
plt.ylabel("petal length")
plt.legend(loc="upper left")
plt.show()

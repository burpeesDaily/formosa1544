# Copyright © 2017, 2019 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""An example of unsurprised learning uses the Iris data set.
https://archive.ics.uci.edu/ml/datasets/Iris
Attribute Information:
1. sepal length in cm 
2. sepal width in cm 
3. petal length in cm 
4. petal width in cm 
5. class: 
-- Iris Setosa 
-- Iris Versicolour 
-- Iris Virginica
"""

import urllib.request

# pandas is an open source library providing high-performance, 
# easy-to-use data structures and data analysis tools.
# http://pandas.pydata.org/
import pandas

# matplotlib is a python 2D plotting library which produces publication
# quality. Figures in a variety of hardcopy formats and interactive
# environments across platforms.
# http://matplotlib.org/2.0.0/index.html
import matplotlib.pyplot as plt

# Seaborn is a Python data visualization library based on matplotlib.
# It provides a high-level interface for drawing attractive and
# informative statistical graphics.
# http://seaborn.pydata.org/index.html
import seaborn as sns

sns.set() # set the default seaborn theme, scaling, and color palette.

# Download Iris Data Set from http://archive.ics.uci.edu/ml/datasets/Iris
URL = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
urllib.request.urlretrieve(URL, 'iris.data')
# use pandas' read_csv function to read iris.data into a python array.
# Note: the iris.data is headerless, so header is None.
iris_data = pandas.read_csv('iris.data', header=None)

unlabeled_data = iris_data.iloc[:, [0, 2]].values

plt.scatter(unlabeled_data[:, 0], unlabeled_data[:, 1],
            color='green', marker='o')

plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.legend(loc='upper left')
plt.show()

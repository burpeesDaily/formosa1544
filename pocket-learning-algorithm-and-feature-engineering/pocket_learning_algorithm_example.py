import collections

import numpy as np
import pandas as pd
import seaborn as sns

from typing import Any
from urllib import request

from sklearn import impute
from sklearn import model_selection
from sklearn import preprocessing

import pocket_classifier


sns.set_theme()  # set the default seaborn theme, scaling, and color palette.


def imputer_by_most_frequent(missing_values: Any, data: list) -> list:
    """Input missing value by frequency, i.e., the value appeared
    most often.

    Parameters
    ----------
    missing_values: Any
        The missing value can be np.nan, "?", or whatever character
        which indicates missing value.
    data: list
        The list of the data.

    Returns
    -------
    List of numerical data
        The list of the data based on the most frequent approach.
    """
    most = collections.Counter(data).most_common(1)[0][0]
    complete_list = []
    for item in data:
        if item is missing_values:
            item = most
        complete_list.append(item)
    return complete_list


def one_hot_encoder(data: list) -> list:
    """Transfer categorical data to numerical data based on one hot
    encoding approach.

    Parameters
    ----------
    data: list of data. Any numerical type.
        One dimension list.

    Returns
    -------
    List of int
        The list of the encoded data based on one hot encoding approach.
    """
    LABEL_ENCODER = preprocessing.LabelEncoder()
    numerical_data = LABEL_ENCODER.fit_transform(data)
    two_d_array = [[item] for item in numerical_data]

    encoder = preprocessing.OneHotEncoder()
    encoder.fit(two_d_array)
    return encoder.transform(two_d_array).toarray()


if __name__ == "__main__":
    # Download Japanese Credit Data Set from
    # http://archive.ics.uci.edu/ml/datasets/Japanese+Credit+Screening
    URL = "http://archive.ics.uci.edu/ml/machine-learning-databases/credit-screening/crx.data"
    request.urlretrieve(URL, "crx.data")
    # Use pandas.read_csv module to load adult data set
    # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
    crx_data = pd.read_csv("crx.data", header=None)
    crx_data.replace("?", np.nan, inplace=True)

    # Transfer the category data to numerical data and input
    # missing data:
    # A1: b, a. (missing)
    # A2: continuous. (missing) mean
    # A3: continuous.
    # A4: u, y, l, t. (missing) frequency
    # A5: g, p, gg. (missing) frequency
    # A6: c, d, cc, i, j, k, m, r, q, w, x, e, aa, ff. (missing) frequency
    # A7: v, h, bb, j, n, z, dd, ff, o. (missing) frequency
    # A8: continuous.
    # A9: t, f.
    # A10: t, f.
    # A11: continuous.
    # A12: t, f.
    # A13: g, p, s.
    # A14: continuous. (missing) mean
    # A15: continuous.
    # A16: +,- (class label)

    A1_no_missing = imputer_by_most_frequent(np.nan, crx_data.iloc[:, 0].values)

    A1_encoded = one_hot_encoder(A1_no_missing)

    imputer = impute.SimpleImputer(missing_values=np.nan, strategy="mean")

    A2_two_d = np.array([[item] for item in crx_data.iloc[:, 1].values])
    A2_no_missing = imputer.fit_transform(A2_two_d)

    A3 = crx_data.iloc[:, 2].values

    A4_no_missing = imputer_by_most_frequent(np.nan, crx_data.iloc[:, 3].values)
    A4_encoded = one_hot_encoder(A4_no_missing)

    A5_no_missing = imputer_by_most_frequent(np.nan, crx_data.iloc[:, 4].values)
    A5_encoded = one_hot_encoder(A5_no_missing)

    A6_no_missing = imputer_by_most_frequent(np.nan, crx_data.iloc[:, 5].values)
    A6_encoded = one_hot_encoder(A6_no_missing)

    A7_no_missing = imputer_by_most_frequent(np.nan, crx_data.iloc[:, 6].values)
    A7_encoded = one_hot_encoder(A7_no_missing)

    A8 = crx_data.iloc[:, 7].values

    A9_encoded = one_hot_encoder(crx_data.iloc[:, 8].values)

    A10_encoded = one_hot_encoder(crx_data.iloc[:, 9].values)

    A11 = crx_data.iloc[:, 10].values

    A12_encoded = one_hot_encoder(crx_data.iloc[:, 11].values)

    A13_encoded = one_hot_encoder(crx_data.iloc[:, 12].values)

    A14_two_d = np.array([[item] for item in crx_data.iloc[:, 13].values])
    A14_no_missing = imputer.fit_transform(A14_two_d)

    A15 = crx_data.iloc[:, 14].values

    # Aggregate all the encoded data together to a two-dimension set
    data = list()
    label = list()
    for index in range(690):
        temp = np.append(A1_encoded[index], A2_no_missing[index])
        temp = np.append(temp, A3[index])
        temp = np.append(temp, A4_encoded[index])
        temp = np.append(temp, A5_encoded[index])
        temp = np.append(temp, A6_encoded[index])
        temp = np.append(temp, A7_encoded[index])
        temp = np.append(temp, A8[index])
        temp = np.append(temp, A9_encoded[index])
        temp = np.append(temp, A10_encoded[index])
        temp = np.append(temp, A11[index])
        temp = np.append(temp, A12_encoded[index])
        temp = np.append(temp, A14_no_missing[index])
        temp = np.append(temp, A15[index])
        data.append(temp.tolist())
        label.append(crx_data[15][index])

    # Use scikit-learn"s MinMaxScaler to scale the training data set.
    # http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html
    min_max_scaler = preprocessing.MinMaxScaler()
    data_minmax = min_max_scaler.fit_transform(data)

    features = len(data[0])

    # Use scikit-learn"s train_test_split function to separate
    # the Iris Data Set to a training subset (75% of the data)
    # and a test subst (25% of the data).
    DATA_TRAIN, DATA_TEST, LABELS_TRAIN, LABELS_TEST = model_selection.train_test_split(
        data_minmax, label, test_size=0.25, random_state=1000
    )

    classifier = pocket_classifier.PocketClassifier(features, ("+", "-"))
    classifier.train(DATA_TRAIN, LABELS_TRAIN, 100)

    result = classifier.classify(DATA_TEST)

    misclassify = 0
    for predict, answer in zip(result, LABELS_TEST):
        if predict != answer:
            misclassify += 1
    print(
        "Accuracy rate: %2.2f" % (100 * (len(result) - misclassify) / len(result)) + "%"
    )

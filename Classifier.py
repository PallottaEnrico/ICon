import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def importdata(dataset):
    balance_data = pd.read_csv(dataset, sep=',', header=None)
    return balance_data


def set_training(balance_data, test):
    X = balance_data.values[:, 1:9]
    Y = balance_data.values[:, 9]
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.000001, random_state=0)

    X_test = test

    return X, Y, X_train, X_test, y_train, y_test


def train_using_entropy(X_train, y_train):
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(
        criterion="entropy", random_state=100,
        max_depth=3, min_samples_leaf=5)

    # Performing training
    clf_entropy.fit(X_train, y_train)
    return clf_entropy


def prediction(X_test, clf_object):
    y_pred = clf_object.predict(X_test)
    return y_pred

def classify(test, dataset):
    data = importdata(dataset)
    X, Y, X_train, X_test, y_train, y_test = set_training(data, test)
    clf_entropy = train_using_entropy(X_train, y_train)
    y_pred = prediction(X_test, clf_entropy)
    return y_pred

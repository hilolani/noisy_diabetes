import numpy as np
import pandas as pds
from pandas import Series,DataFrame
import csv
import random
from sklearn.datasets import load_diabetes
from sklearn.utils import Bunch

def add_gaussian_noise_np(X, mean=0.0, sd=0.1):
    X = np.array(X)
    noise = np.random.normal(loc=mean, scale=sd, size=X.shape)
    noisy = X + noise
    col_mins = X.min(axis=0)
    col_maxs = X.max(axis=0)
    return np.clip(noisy, col_mins, col_maxs)

def add_uniform_noise_np(X, low=-0.01, high=0.01):
    X = np.array(X)
    noise = np.random.uniform(low=low, high=high, size=X.shape)
    noisy = X + noise
    return noisy

def load_noisy_diabetes(return_X_y=False, as_frame=False, scaled=True):
    diabetes = load_diabetes(return_X_y=False, as_frame=as_frame, scaled=scaled)

    with open('/content/drive/My Drive/Colab Notebooks/noisy_diabetes_data.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
    f.close()
    del(l[0])
    X_noisy = [list(map(lambda x:float(x), i)) for i in l]
    y = diabetes.target.copy()

    if return_X_y:
        return X_noisy, y

    return Bunch(
        data=X_noisy,
        target=y,
        feature_names=["age", "sex", "bmi", "map", "tc", "ldl", "hdl", "tch", "ltg", "glu"],
        frame=pds.DataFrame(X_noisy, columns=["age", "sex", "bmi", "map", "tc", "ldl", "hdl", "tch", "ltg", "glu"]) if as_frame else None,
        DESCR="Noisy version of the diabetes dataset",
        data_filename=None,
        target_filename=None,
    )

def load_total_noisy_diabetes(return_X_y=False, as_frame=False, scaled=True):
    diabetes = load_diabetes(return_X_y=False, as_frame=as_frame, scaled=scaled)

    with open('/content/drive/My Drive/Colab Notebooks/total_noisy_diabetes_data.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
    f.close()
    del(l[0])
    X_noisy = [
        list(map(int, row[:2])) + list(map(float, row[2:]))
        for row in l
    ]

    with open('/content/drive/My Drive/Colab Notebooks/total_noisy_diabetes_target.csv') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
    f.close()
    del(l[0])
    y_noisy = [list(map(lambda x:float(x), i)) for i in l]

    if return_X_y:
        return X_noisy, y_noisy

    return Bunch(
        data=X_noisy,
        target=y_noisy,
        feature_names=["participants", "sessions","age", "sex", "bmi", "map", "tc", "ldl", "hdl", "tch", "ltg", "glu"],
        frame=pds.DataFrame(X_noisy, columns=["participants", "sessions","age", "sex", "bmi", "map", "tc", "ldl", "hdl", "tch", "ltg", "glu"]) if as_frame else None,
        DESCR="Total (augmented) version of the noisy diabetes dataset",
        data_filename=None,
        target_filename=None,
    )


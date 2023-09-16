#!/usr/bin/python3

import os
import sys
import platform
import numpy
import pandas
import scipy

print(platform.platform())
print("Python", sys.version)
print("NumPy", numpy.__version__)
print("SciPy", scipy.__version__)


def train():
    MODEL_DIR = os.environ.get("MODEL_DIR")
    MODEL_FILE_LDA = os.environ.get("MODEL_FILE_LDA")
    MODEL_FILE_NN = os.environ.get("MODEL_FILE_NN")
    MODEL_PATH_LDA = os.path.join(MODEL_DIR, MODEL_FILE_LDA)
    MODEL_PATH_NN = os.path.join(MODEL_DIR, MODEL_FILE_NN)

    # Load, read and normalize training data
    training = "./src/train.csv"
    data_train = pandas.read_csv(training)

    y_train = data_train["# Letter"].values


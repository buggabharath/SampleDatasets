#Sample Project on Bostan
# Feature name and Shape

import mglearn
from  sklearn.datasets import load_boston

bostan = load_boston()
print("Data Shape: {}".format(bostan.data.shape))

X,y = mglearn.datasets.load_extended_boston()
print("X.Shape: {}".format(X.shape))

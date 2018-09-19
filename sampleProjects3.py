#Sample Project 3
#using sklearn datasets beast Cancer
import numpy as np
from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
print("Cancer.Keys(): \n{} ".format(cancer.keys()))
print("Shape of Cancer data: {}".format(cancer.data.shape))

print("Sample counts per class: \n{}".format(
    {n: v for n,v in zip(cancer.target_names, np.bincount(cancer.target))}))
print("Feature Names:\n{}".format(cancer.feature_names))

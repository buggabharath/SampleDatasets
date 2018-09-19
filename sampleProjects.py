# Dataset on Forge

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
#generate dataset
X,y = mglearn.datasets.make_forge()
#plot datasets

mglearn.discrete_scatter(X[:, 0], X[:, 1], y)
plt.legend(['Class 0', 'Class 1'], loc=4)
plt.xlabel('First feature')
plt.ylabel('Second Class')
print('X.Shape: {}'.format(X.shape))



import numpy as np
import pandas as pd

x=pd.read_csv('Dataset\\x.csv')
y=pd.read_csv('Dataset\\y.csv',header=None)

print(x.shape)
print(y.shape)


#convert a pandas dataframe into a numpy array

X=x.values
Y=y.values
print(X.shape)
print(Y.shape)
print(X[0][0]+2)            #for testing purposes only
from sklearn  import svm
from loader_v2 import *
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV
import os
import sys







filename = 'finalized_model.sav'

print("loading data ...")

X_train,Y_train,X_test,Y_test=lo_data2()
path="C:\\Users\\vegon\\Desktop\\BROCA\\BROCA\\svm_br"
os.chdir(path)
print(os.getcwd())

scaler = preprocessing.StandardScaler().fit(X_train)
scaled_train=scaler.transform(X_train)
scaled_test=scaler.transform(X_test)

loaded_model = joblib.load(filename)
result = loaded_model.score(scaled_test, Y_test)
print(result)

def prd(p):
    scaled_in=scaler.transform(p)

    print(str(loaded_model.predict(scaled_in)[0]))
    #sys.stdout.write("\r"+)
    #sys.stdout.flush()

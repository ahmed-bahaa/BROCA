from sklearn  import svm
#from loader import *
from loader_v2 import *
from sklearn import preprocessing
from sklearn.metrics import accuracy_score

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV

def selector (selec,data,clas):
    clas_m=list(clas)
    selec=selec-1
    test_set=data[(0+(selec*100)):(100+(100*selec))]
    clas_test=clas_m[(0+(selec*100)):(100+(100*selec))]
    train_set=data[:(0+(selec*100))]
    train_set=train_set.append(data[(100+(100*selec)):])
    #clas_train=clas[:(0+(selec*100))]
    #clas_train.append(clas[(100+(100*selec)):])
    #clas_train=filter(None,clas_train)
    del clas_m[(0+(selec*100)):(100+(100*selec))]
    clas_train = clas_m
    #print(len(clas_train))
    #print(len(clas_test))
    clas_train=np.array(clas_train).ravel()
    clas_test=np.array(clas_test).ravel()
    return (train_set,clas_train,test_set,clas_test)


def main():

        print("loading data ...")

        X_train,Y_train,X_test,Y_test=lo_data2()        #lo_data2(): to use loader_v2   ,,, and lo_data(): to use loader

        print("SVM received data successfully")

        print(X_train.shape)
        print(Y_train.shape)

        scaler = preprocessing.StandardScaler().fit(X_train)
        scaled_train=scaler.transform(X_train)
        scaled_test=scaler.transform(X_test)



        C_range = np.logspace(-2, 10, 13)
        gamma_range = np.logspace(-9, 3, 13)
        param_grid = dict(gamma=gamma_range, C=C_range)
        cv = StratifiedShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
        grid = GridSearchCV(SVC(), param_grid=param_grid, cv=cv , n_jobs=-2)
        grid.fit(scaled_train,Y_train)
        print("The best parameters are %s with a score of %0.2f"
        % (grid.best_params_, grid.best_score_))

        '''

        clf = svm.SVC(kernel='rbf',decision_function_shape='ovo'  ,gamma=.01 , C=1000000)
        #clf = svm.SVC(kernel='rbf',decision_function_shape='ovo' ,gamma=0.01 , C=1000)
        clf.fit(scaled_train,Y_train)
        print(clf)
        pr=clf.predict(scaled_test)
        print(clf.predict(scaled_test))
        print(Y_test)
        print("accuracy: ",accuracy_score(Y_test,pr))
        '''

        print("=================================================================")




if __name__ == "__main__":
    main()

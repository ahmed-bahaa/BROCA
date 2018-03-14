import numpy as np
import os ,glob , csv
import pandas as pd
global persons, gestures,train_data,test_data,clas_train,clas_test
'''
this script use modified data from data handler v2
this program just load and seperate it into train set and test set
'''

persons=3
train_data=pd.DataFrame()
test_data=pd.DataFrame()
clas_train=[]
clas_test=[]
def lo_data():
    global persons,gestures,clas_train,clas_test,train_data,test_data
    for person in range(1,persons+1):
            path="C:\\Users\\vegon\\Desktop\\BROCA\\BROCA\\svm_br\\acquisitions\\static\\P"+str(person)
            extension = 'csv'
            os.chdir(path)
            result = [i for i in glob.glob('*.{}'.format(extension))]
            print("person: ",person)
            count=0
            for name in result:
                        df = pd.read_csv(name , index_col=0)

                        df= df.loc[['R.Thumb.TTP','R.Index.TTP','R.Middle.TTP','R.Ring.TTP','R.Pinky.TTP','L.Thumb.TTP',
                        'L.Index.TTP','L.Middle.TTP','L.Ring.TTP','L.Pinky.TTP']]
                        df = df.transpose()
                        #df = df.drop(df.columns[[0]], axis=1)
                        #print(df.shape[0])
                        nam=name.split('_')[0]

                        total=df.shape[0]
                        count=count+total
                        no_train=int (0.7*total) +1
                        no_test=total-no_train

                        for i in range (no_train) :
                            clas_train.append(nam)
                        for i in range (no_test) :
                            clas_test.append(nam)

                        train_data=train_data.append(df[:no_train])
                        test_data=test_data.append(df[no_train:])
                        #print(no_train)
                        #print(clas_test)
                        #print(clas_train)
                        #print(train_data.shape[0])
                        #print(test_data.shape[0])
                        #print("=====================================")
            print(train_data.shape)
            print(test_data.shape)
            print(count)
            print (len(clas_train))
            print (len(clas_test))
            print("=====================================")
    clas_train=np.array(clas_train).ravel()
    clas_test=np.array(clas_test).ravel()

    print("loading complete successfully")
    #return (train_data,clas_train,test_data,clas_test)





#a,b,c,d=lo_data(10)

#lo_data()

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
def lo_data2():
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
                        'L.Index.TTP','L.Middle.TTP','L.Ring.TTP','L.Pinky.TTP',
                        'R.Thumb.TNA', 'R.Index.TNA', 'R.Middle.TNA', 'R.Ring.TNA', 'R.Pinky.TNA', 'L.Thumb.TNA',
                        'L.Index.TNA', 'L.Middle.TNA', 'L.Ring.TNA', 'L.Pinky.TNA',
                        'R.Thumb_Index.ang', 'R.Index_Middle.ang', 'R.Middle_Ring.ang', 'R.Ring_Pinky.ang',
                        'L.Thumb_Index.ang', 'L.Index_Middle.ang', 'L.Middle_Ring.ang', 'L.Ring_Pinky.ang']]
                        df = df.transpose()
                        #df = df.drop(df.columns[[0]], axis=1)
                        #print(df.shape[0])
                        nam=name.split('_')[0]
                        nam2=name.split('_')[1]
                        nam2=int (nam2.split('.')[0])
                        #print(nam2)


                        #test set
                        if (nam2 >= 8):
                            #print("test")
                            test_data=test_data.append(df[:])
                            n=df.shape[0]
                            for i in range (n) :
                                clas_test.append(nam)
                        if( (person==3) & (nam=="b") & (nam2==4)  ):

                            #print("run")
                            test_data=test_data.append(df[:])
                            n=df.shape[0]
                            for i in range (n) :
                                clas_test.append(nam)
                            continue


                        #train set
                        if (nam2 < 8):
                            #print("train")
                            train_data=train_data.append(df[:])
                            n=df.shape[0]
                            for i in range (n) :
                                clas_train.append(nam)







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
    return (train_data,clas_train,test_data,clas_test)





#a,b,c,d=lo_data(10)

#lo_data()

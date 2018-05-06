import numpy as np
import os ,glob , csv
import pandas as pd
global persons, gestures,train_data,test_data,clas_train,clas_test,train_3D,test_3D,q,Q
'''
this script use modified data from data handler v2
this program just load and seperate it into train set and test set
'''

persons=8
train_data=pd.DataFrame()
test_data=pd.DataFrame()
train_3D=np.array(())
test_3D=np.array(())
clas_train=[]
clas_test=[]
q=0
Q=0
org_path= os.getcwd()
req_path=org_path+"\\dataset\\modified\\"

os.chdir(req_path)
with open('parameters.csv', "rt") as f:
    reader = list(csv.reader(f))[0]
    no_gestures  = int(reader[0])
    no_sequences = int(reader[1])
    no_features  = int(reader[2])
    no_dynfiles= int(reader[3])
os.chdir(org_path)

def lo_data2():
    global persons,gestures,clas_train,clas_test,train_data,test_data,train_3D,test_3D,q,Q
    type=['static','dynamic']

    for typ in type:

        if (typ=="static"):

            for person in range(1,persons+1):
                    path=req_path+typ+"\\P"+str(person)
                    extension = 'csv'
                    if not os.path.exists(path):
                                #continue
                                os.makedirs(path)
                                os.chdir(path)
                    else:
                            os.chdir(path)
                    result = [i for i in glob.glob('*.{}'.format(extension))]
                    print("person: ",person)
                    count=0
                    for name in result:
                                df = pd.read_csv(name , index_col=0)

                                df= df.loc[[ 'L.pitch', 'L.roll','L.sphere_radius' ,'R_speed','L_speed',
                                 'L.yaw', 'L.Arm direction_x', 'L.Arm direction_y','L.Arm direction_z', 'R.hand.palm_position_x',
                                 'R.hand.palm_position_y', 'R.hand.palm_position_z', 'R.pitch', 'R.roll', 'R.yaw',
                                 'R.Arm direction_x', 'R.Arm direction_y','R.Arm direction_z','R.Thumb.TTP','R.Index.TTP',
                                'R.Middle.TTP','R.Ring.TTP','R.Pinky.TTP','L.Thumb.TTP','L.Index.TTP',
                                'L.Middle.TTP','L.Ring.TTP','L.Pinky.TTP','R.Thumb.TNA', 'R.Index.TNA',
                                 'R.Middle.TNA', 'R.Ring.TNA', 'R.Pinky.TNA', 'L.Thumb.TNA','L.Index.TNA',
                                 'L.Middle.TNA', 'L.Ring.TNA', 'L.Pinky.TNA','R.Thumb_Index.ang', 'R.Index_Middle.ang',
                                 'R.Middle_Ring.ang', 'R.Ring_Pinky.ang','L.Thumb_Index.ang', 'L.Index_Middle.ang', 'L.Middle_Ring.ang',
                                'L.Ring_Pinky.ang'

                                ,'R.Thumb.TTP_sacled','R.Index.TTP_sacled','R.Middle.TTP_sacled','R.Ring.TTP_sacled','R.Pinky.TTP_sacled',
                                'L.Thumb.TTP_sacled','L.Index.TTP_sacled','L.Middle.TTP_sacled','L.Ring.TTP_sacled','L.Pinky.TTP_sacled'
                                ,"L.hand direction_x","L.hand direction_y","L.hand direction_z","R.hand direction_x","R.hand direction_y",
                                "R.hand direction_z",'R.Thumb.THA', 'R.Index.THA', 'R.Middle.THA', 'R.Ring.THA',
                                 'R.Pinky.THA', 'L.Thumb.THA','L.Index.THA', 'L.Middle.THA', 'L.Ring.THA',
                                 'L.Pinky.THA','R.sphere_radius',  'palms_dis','Thumb_dis','Index_dis',
                                'Middle_dis','Ring_dis','Pinky_dis'

                                ,

                                 'R.Thumb.transformed_direction_x', 'R.Thumb.transformed_direction_y', 'R.Thumb.transformed_direction_z'
                                , 'R.Index.transformed_direction_x', 'R.Index.transformed_direction_y', 'R.Index.transformed_direction_z'
                                , 'R.Middle.transformed_direction_x', 'R.Middle.transformed_direction_y', 'R.Middle.transformed_direction_z'
                                , 'R.Ring.transformed_direction_x', 'R.Ring.transformed_direction_y', 'R.Ring.transformed_direction_z'
                                , 'R.Pinky.transformed_direction_x', 'R.Pinky.transformed_direction_y', 'R.Pinky.transformed_direction_z'
                                 ,'L.Thumb.transformed_direction_x', 'L.Thumb.transformed_direction_y', 'L.Thumb.transformed_direction_z'
                                 , 'L.Index.transformed_direction_x', 'L.Index.transformed_direction_y', 'L.Index.transformed_direction_z'
                                 , 'L.Middle.transformed_direction_x', 'L.Middle.transformed_direction_y', 'L.Middle.transformed_direction_z'
                                 , 'L.Ring.transformed_direction_x', 'L.Ring.transformed_direction_y', 'L.Ring.transformed_direction_z'
                                 , 'L.Pinky.transformed_direction_x', 'L.Pinky.transformed_direction_y', 'L.Pinky.transformed_direction_z'
                                 , 'R.wrist position_x', 'R.wrist position_y', 'R.wrist position_z'
                                 , 'L.wrist position_x', 'L.wrist position_y', 'L.wrist position_z'
                                ]]
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
                                '''
                                if( (person==3) & (nam=="b") & (nam2==4)  ):
                                    #print("run")
                                    test_data=test_data.append(df[:])
                                    n=df.shape[0]
                                    for i in range (n) :
                                        clas_test.append(nam)
                                    continue
                                '''
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

            nfeatues=train_data.shape[1]
            if nfeatues==0:
                nfeatues=115
            trsize=int((no_dynfiles*.7)+ len(clas_train))
            tesize=int((no_dynfiles*.3)+ len(clas_test))
            train_3D=np.zeros((trsize,no_sequences,nfeatues))
            test_3D=np.zeros((tesize,no_sequences,nfeatues))

            for j in range((len(clas_train))):
                train_3D[q, 0] = train_data.ix[j]
                q = q + 1
            for j in range((len(clas_test))):
                test_3D[Q, 0] = test_data.ix[j]
                Q = Q + 1

        else:
            print("dynamic")
            for person in range(1,persons+1):
                    path=req_path+typ+"\\P"+str(person)
                    extension = 'csv'
                    if not os.path.exists(path):
                                #continue
                                os.makedirs(path)
                                os.chdir(path)
                    else:
                            os.chdir(path)
                    result = [i for i in glob.glob('*.{}'.format(extension))]
                    print("person: ",person)
                    count=0
                    for name in result:
                                df = pd.read_csv(name , index_col=0)

                                df= df.loc[[ 'L.pitch', 'L.roll','L.sphere_radius' ,'R_speed','L_speed',
                                 'L.yaw', 'L.Arm direction_x', 'L.Arm direction_y','L.Arm direction_z', 'R.hand.palm_position_x',
                                 'R.hand.palm_position_y', 'R.hand.palm_position_z', 'R.pitch', 'R.roll', 'R.yaw',
                                 'R.Arm direction_x', 'R.Arm direction_y','R.Arm direction_z','R.Thumb.TTP','R.Index.TTP',
                                'R.Middle.TTP','R.Ring.TTP','R.Pinky.TTP','L.Thumb.TTP','L.Index.TTP',
                                'L.Middle.TTP','L.Ring.TTP','L.Pinky.TTP','R.Thumb.TNA', 'R.Index.TNA',
                                 'R.Middle.TNA', 'R.Ring.TNA', 'R.Pinky.TNA', 'L.Thumb.TNA','L.Index.TNA',
                                 'L.Middle.TNA', 'L.Ring.TNA', 'L.Pinky.TNA','R.Thumb_Index.ang', 'R.Index_Middle.ang',
                                 'R.Middle_Ring.ang', 'R.Ring_Pinky.ang','L.Thumb_Index.ang', 'L.Index_Middle.ang', 'L.Middle_Ring.ang',
                                'L.Ring_Pinky.ang'

                                ,'R.Thumb.TTP_sacled','R.Index.TTP_sacled','R.Middle.TTP_sacled','R.Ring.TTP_sacled','R.Pinky.TTP_sacled',
                                'L.Thumb.TTP_sacled','L.Index.TTP_sacled','L.Middle.TTP_sacled','L.Ring.TTP_sacled','L.Pinky.TTP_sacled'
                                ,"L.hand direction_x","L.hand direction_y","L.hand direction_z","R.hand direction_x","R.hand direction_y",
                                "R.hand direction_z",'R.Thumb.THA', 'R.Index.THA', 'R.Middle.THA', 'R.Ring.THA',
                                 'R.Pinky.THA', 'L.Thumb.THA','L.Index.THA', 'L.Middle.THA', 'L.Ring.THA',
                                 'L.Pinky.THA','R.sphere_radius',  'palms_dis','Thumb_dis','Index_dis',
                                'Middle_dis','Ring_dis','Pinky_dis'

                                ,

                                 'R.Thumb.transformed_direction_x', 'R.Thumb.transformed_direction_y', 'R.Thumb.transformed_direction_z'
                                , 'R.Index.transformed_direction_x', 'R.Index.transformed_direction_y', 'R.Index.transformed_direction_z'
                                , 'R.Middle.transformed_direction_x', 'R.Middle.transformed_direction_y', 'R.Middle.transformed_direction_z'
                                , 'R.Ring.transformed_direction_x', 'R.Ring.transformed_direction_y', 'R.Ring.transformed_direction_z'
                                , 'R.Pinky.transformed_direction_x', 'R.Pinky.transformed_direction_y', 'R.Pinky.transformed_direction_z'
                                 ,'L.Thumb.transformed_direction_x', 'L.Thumb.transformed_direction_y', 'L.Thumb.transformed_direction_z'
                                 , 'L.Index.transformed_direction_x', 'L.Index.transformed_direction_y', 'L.Index.transformed_direction_z'
                                 , 'L.Middle.transformed_direction_x', 'L.Middle.transformed_direction_y', 'L.Middle.transformed_direction_z'
                                 , 'L.Ring.transformed_direction_x', 'L.Ring.transformed_direction_y', 'L.Ring.transformed_direction_z'
                                 , 'L.Pinky.transformed_direction_x', 'L.Pinky.transformed_direction_y', 'L.Pinky.transformed_direction_z'
                                 , 'R.wrist position_x', 'R.wrist position_y', 'R.wrist position_z'
                                 , 'L.wrist position_x', 'L.wrist position_y', 'L.wrist position_z'
                                ]]
                                df = df.transpose()
                                l = list(set(np.where(pd.isnull(df))[0]))
                                df=df.drop(df.index[l], axis=0)
                                #df = df.drop(df.columns[[0]], axis=1)
                                #print(df.shape[0])
                                nam=name.split('_')[0]
                                nam2=name.split('_')[1]
                                nam2=int (nam2.split('.')[0])
                                #print(nam2)

                                #train set
                                if (nam2 < 8):
                                    #print("train")
                                    clas_train.append(nam)
                                    #train_data=train_data.append(df[:])
                                    n=df.shape[0]
                                    for j in range(n):
                                        train_3D[q, j] = df.ix[j]
                                    q = q + 1


                                #test set
                                if (nam2 >= 8):
                                    #print("test")
                                    clas_test.append(nam)
                                    #test_data=test_data.append(df[:])
                                    n=df.shape[0]
                                    for j in range(n):
                                        test_3D[Q, j] = df.ix[j]
                                    Q = Q + 1






    #print(clas_train)
    clas_train=np.array(clas_train).ravel()
    clas_test=np.array(clas_test).ravel()
    no_features=train_3D.shape[2]
    print(train_3D[50])
    print("loading complete successfully")
    os.chdir(org_path)
    return (train_3D,clas_train,test_3D,clas_test,no_features,no_sequences)




'''
a,b,c,d=lo_data2()
print(a.shape)
print(b.shape)
print(c.shape)
print(d.shape)
#lo_data()
'''


import numpy as np
import os
import glob
import csv
import pandas as pd
global L
L=5

no_persons=8
type=['static','dynamic']
no_gestures=0
no_sequences=0
no_features=0
no_dynamic_files=0
org_path = os.getcwd()

for typ in type:

    if (typ=="static"):
        for person in range(1,no_persons+1):
            print("person:",person)

            req_path = org_path + "\\dataset\\original\\"+typ+"\\p"+str(person)+"\\"
            extension = 'csv'
            os.chdir(req_path)
            result = [i for i in glob.glob('*.{}'.format(extension))]
            y=pd.DataFrame()
            for name in result:

                df = pd.read_csv(name)
                df = df.drop(df.columns[[0,1,4,5,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,216
                                         ,217,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247]], axis=1)
                # print(df[0:9].shape[0])
                print(df.shape)
                #print(df)
                z = list(set(np.where(pd.isnull(df))[0]))  # list of indecies for empty rows
                df = df.drop(df.index[z]).reset_index(drop=True)
                #print('after',df.shape)
                leng = df.shape[0]
                i = leng / L
                r = leng - (L * i)
                if (r>0):
                    iter=i+1
                else:
                    iter=i
                s = pd.DataFrame()
                #print(name[0])
                print("file name:"+name)

                for x in range(0, iter, 1):

                    no_gestures=no_gestures+1

                    if (x == i):
                        if(r==1):
                            s[x] = df.ix[(x * L)]
                        else:
                            d = df[(x * L):((x * L) + r )] #d = df[(x * L):((x * L) + r - 1)]
                            s[x] = np.mean(d, axis=0)
                    else:

                        d = df[(x * L):((x * L) + L )] #d = df[(x * L):((x * L) + L - 1)]
                        s[x] = np.mean(d, axis=0)

                #print (s.shape[1])


                req_path = org_path + "\\dataset\\modified\\"+typ+"\\p"+str(person)
                if not os.path.exists(req_path):
                    os.makedirs(req_path)

                os.chdir(req_path)
                if(np.isinf(s).sum().sum()>0):
                    print("heeeeeeeeeeeeeeeeeeeeere")
                #s.to_csv('p'+str(person)+'\\'+name, sep=',', index=True, header=True)
                s.to_csv(name, sep=',', index=True, header=True)

                req_path = org_path + "\\dataset\\modified\\"+typ+"\\classification\\p"+str(person)

                if not os.path.exists(req_path):
                    os.makedirs(req_path)
                os.chdir(req_path)
                n=s.shape[1]
                cls=name.split('_')[0]

                cls=cls.split('.')[0]

                print("class name:"+cls)

                with open("y"+str(person)+".csv", "ab") as fp:
                    wr = csv.writer(fp, dialect='excel')
                    for z in range (n):
                        wr.writerow([cls])
                req_path = org_path + "\\dataset\\orginial\\"+typ+"\\p"+str(person)
                os.chdir(req_path)

    #dynamic gesture handling
    else:
        #L=10
        print no_gestures
        print("dynamic gestures:")
        for person in range(1,no_persons+1):
            print("person:",person)

            req_path = org_path + "\\dataset\\original\\"+typ+"\\p"+str(person)
            extension = 'csv'
            os.chdir(req_path)
            result = [i for i in glob.glob('*.{}'.format(extension))]
            y=pd.DataFrame()
            for name in result:
                print name
                no_dynamic_files+=1
                df = pd.read_csv(name)
                df = df.drop(df.columns[[0,1,4,5,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,216
                                         ,217,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247]], axis=1)

                no_gestures=no_gestures+1

                # print(df[0:9].shape[0])
                #print(df.shape)
                #print(df)

                l=list(set(np.where(pd.isnull(df))[0]))    #list of indecies for empty rows
                #print l
                l=sorted(l)
                #print l
                Len = len(list(set(np.where(pd.isnull(df))[0])))+1
                #print Len

                z=df
                s = pd.DataFrame()
                ind=0
                for k in range(Len):  # 0 1 2 3
                    if (k == 0):
                        g = df[:l[0]]
                        #print g.shape
                        #print g.ix[0]
                    elif (k == (Len - 1)):
                        g = df[l[k - 1] + 1:].reset_index(drop=True)
                        #print g.shape
                        #print g.ix[0]
                    else:
                        g = df[l[k - 1] + 1:l[k]].reset_index(drop=True)
                        #print g.shape
                        #print g.ix[0]


                    leng = g.shape[0]
                    i = leng / L
                    r = leng - (L * i)

                    if (r>0):
                        iter=i+1
                    else:
                        iter=i


                    for x in range(0, iter, 1):

                        if (x == i):
                            if(r==1):
                                s[ind] = g.ix[(x * L)]
                                ind=ind+1
                            else:
                                d = g[(x * L):((x * L) + r )] #d = g[(x * L):((x * L) + r - 1)]
                                s[ind] = d.mean(axis=None, skipna=None, level=None, numeric_only=None)
                                ind = ind + 1
                        else:

                            d = g[(x * L):((x * L) + L )]   #d = g[(x * L):((x * L) + L - 1)]
                            s[ind] = d.mean(axis=None, skipna=None, level=None, numeric_only=None)
                            ind = ind + 1
                    #print k
                    if(k==(Len-1)):
                        pass
                    else:
                        s[ind]=z.ix[l[k]]
                        ind=ind+1


                #print (s.shape[1])



                req_path = org_path + "\\dataset\\modified\\"+typ+"\\p"+str(person)

                if not os.path.exists(req_path):
                    os.makedirs(req_path)

                os.chdir(req_path)

                if ( (s.shape[1]-Len+1) > no_sequences):
                    no_sequences= (s.shape[1]-Len+1)
                    #print name
                    no_features=s.shape[0]
                if(np.isinf(s).sum().sum()>0):
                    print ("============================================================================================")
                    print("heeeeeeeeeeeeeeeeeeeeereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
                    print person
                    print name
                    print (np.isinf(s).sum().sum())
                    print ("============================================================================================")
                s.to_csv(name, sep=',', index=True, header=True)
                req_path = org_path + "\\dataset\\modified\\"+typ+"\\classification\\p"+str(person)

                if not os.path.exists(req_path):
                    os.makedirs(req_path)
                os.chdir(req_path)
                cls=name.split('_')[0]
                cls=cls.split('.')[0]
                #print("class name:"+cls)
                with open("y"+str(person)+".csv", "ab") as fp:
                    wr = csv.writer(fp, dialect='excel')
                    wr.writerow([cls])

                req_path = org_path + "\\dataset\\original\\"+typ+"\\p"+str(person)
                os.chdir(req_path)



print ("number of samples: ",no_gestures)
print ("maximum number of sequences: ",no_sequences)
print ("number of features: ",no_features)
print ("number of dynamic features: ",no_dynamic_files)

parameters=([no_gestures,no_sequences,no_features,no_dynamic_files])
req_path = org_path + "\\dataset\\modified\\"
os.chdir(req_path)

with open("parameters" + ".csv", "w") as fp:
    wr = csv.writer(fp, dialect='excel')
    wr.writerow(parameters)
os.chdir(org_path)


'''

#we have to add if condition in case of static perform upper part but incase we are in dynami getures we should write it one per fire

#print (s)
#print (s.shape)

#Y.to_csv('modified\\y.csv', sep=',', index=False, header=False)


path = 'C:\\Users\\vegon\\Desktop\\data_handler_v2\\dataset\\orginial\\dynamic\\p1'
extension = 'csv'
os.chdir(path)
df = pd.read_csv("7.csv")
print list(set(np.where(pd.isnull(df))[0]))
'''

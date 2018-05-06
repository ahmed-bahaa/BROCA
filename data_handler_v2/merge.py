
import numpy as np
import os
import glob
import csv
import pandas as pd



global q
no_persons=5
type=['static','dynamic']
no_gestures=0
no_sequences=0
no_features=0
q=0
# for x
org_path = os.getcwd()
req_path = org_path + "\\dataset\\modified\\"

os.chdir(req_path)
with open('parameters.csv', "rt") as f:
    reader = list(csv.reader(f))[0]
    no_gestures  = int(reader[0])
    no_sequences = int(reader[1])
    no_features  = int(reader[2])
    print ('parameters:',no_gestures,no_sequences,no_features)

data=np.zeros((no_gestures,no_sequences,no_features))

print('collecting input data...')

for typ in type:

    if (typ=="static"):
        for person in range(1,no_persons+1):
            print("person:",person)
            req_path = org_path + "\\dataset\\modified\\"+typ+"\\p"+str(person)
            extension = 'csv'
            os.chdir(req_path)
            result = [i for i in glob.glob('*.{}'.format(extension))]
            for name in result:

                df = pd.read_csv(name)
                df = df.drop(df.columns[[0]], axis=1)

                df = df.transpose()
                n = df.shape[0]
                #print df.shape
                for j in range(n):

                    data[q, 0] = df.ix[j]
                    q = q + 1


    else:

        for person in range(1,no_persons+1):
            print("person:",person)
            req_path = org_path + "\\dataset\\modified\\"+typ+"\\p"+str(person)
            extension = 'csv'
            os.chdir(req_path)
            result = [i for i in glob.glob('*.{}'.format(extension))]
            for name in result:


                df = pd.read_csv(name)
                df = df.drop(df.columns[[0]], axis=1)

                df = df.transpose()
                n = df.shape[0]
                print (n)
                l = list(set(np.where(pd.isnull(df))[0]))
                print ("empty rows indices:",list(set(np.where(pd.isnull(df))[0])))
                print (df.shape)
                df=df.drop(df.index[l], axis=0)
                n = df.shape[0]
                print (df.shape)
                for j in range(n):

                    data[q, j] = df.ix[j]
                q = q + 1





#for y

print('collecting output data...')

output = pd.DataFrame([])


for typ in type:

    print (typ)

    for person in range(1,no_persons+1):

            print("person:",person)
            req_path = org_path + "\\dataset\\modified\\"+typ+"\\classification\\p"+str(person)
            extension = 'csv'
            os.chdir(req_path)
            result = [i for i in glob.glob('*.{}'.format(extension))]
            for name in result:

                df = pd.read_csv(name, header=None)
                output = output.append(df)


print('input data shape is:',data.shape)
print('output data shape is:',output.shape)
os.chdir(org_path)



#path = 'C:\\Users\\vegon\\Desktop\\new\\dataset\\modified\\'
#os.chdir(path)
#np.savetxt("output.csv", output, delimiter=",")
#np.savetxt("data.csv", data, delimiter=",")            raise ab error

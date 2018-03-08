
import numpy as np
import os
import glob
import csv
import pandas as pd
import pickle
#import pathlib
from keras.utils import to_categorical
import keras.backend as K

global q

def load_dataset(n):
        no_persons=n
        type=['static','dynamic']
        no_gestures=0
        no_sequences=0
        no_features=0
        q=0
        # for x

        path = 'C:\\Users\\vegon\\Desktop\\lap\\dataset\\modified\\'
        os.chdir(path)
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
                    path = 'C:\\Users\\vegon\\Desktop\\lap\\dataset\\modified\\'+typ+'\\p'+str(person)
                    extension = 'csv'
                    os.chdir(path)
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
                    path = 'C:\\Users\\vegon\\Desktop\\lap\\dataset\\modified\\'+typ+'\\p'+str(person)
                    extension = 'csv'
                    os.chdir(path)
                    result = [i for i in glob.glob('*.{}'.format(extension))]
                    for name in result:


                        df = pd.read_csv(name)
                        df = df.drop(df.columns[[0]], axis=1)

                        df = df.transpose()
                        n = df.shape[0]
                        #print (n)
                        l = list(set(np.where(pd.isnull(df))[0]))
                        #print ("empty rows indices:",list(set(np.where(pd.isnull(df))[0])))
                        #print (df.shape)
                        df=df.drop(df.index[l], axis=0)
                        n = df.shape[0]
                        #print (df.shape)
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
                    path = 'C:\\Users\\vegon\\Desktop\\lap\\dataset\\modified\\'+typ+'\\classification\\p'+str(person)
                    extension = 'csv'
                    os.chdir(path)
                    result = [i for i in glob.glob('*.{}'.format(extension))]
                    for name in result:

                        df = pd.read_csv(name, header=None)
                        output = output.append(df)


        print('input data shape is:',data.shape)
        print('output data shape is:',output.shape)
        return(data,output.values,no_features,no_gestures,no_sequences)


def load_dict():
        path = 'C:\\Users\\vegon\\Desktop\\lap'
        os.chdir(path)
        index_vocab_dict = np.load('dataset\\modified\\index_vocab_dict.npy').item()
        vocab_index_dict = np.load('dataset\\modified\\vocab_index_dict.npy').item()
        return (index_vocab_dict,vocab_index_dict)





'''
def load_dict():
    abspath = pathlib.Path('dataset\\modified\\index_vocab_dict.pkl').absolute()
    with open(str(abspath), 'rb') as f1:
        index_vocab_dict = pickle.load(f1)

    with open('dataset\\modified\\vocab_index_dict.pkl', 'rb') as f2:
        vocab_index_dict = pickle.load(f2)
        return (index_vocab_dict,vocab_index_dict)
'''


def preprocess_data(dataset, vocab_index_dict , Ty):

    Y = dataset

    #Y = [string_to_int(str(t), Ty, vocab_index_dict) for t in Y]
    Y=[vocab_index_dict[str(t[0])]  for t in Y ]

    Yoh = np.array(list(map(lambda x: to_categorical(x, num_classes=len(vocab_index_dict)), Y)))

    return  Yoh


'''
#we will need this if we have sentences not just words

def string_to_int(string, length, vocab):
    """
    Converts all strings in the vocabulary into a list of integers representing the positions of the
    input string's characters in the "vocab"

    Arguments:
    string -- input string, e.g. 'Wed 10 Jul 2007', 'a'
    length -- the number of time steps you'd like, determines if the output will be padded or cut
    vocab -- vocabulary, dictionary used to index every character of your "string"

    Returns:
    rep -- list of integers (or '<unk>') (size = length) representing the position of the string's character in the vocabulary
    """

    #make lower to standardize
    string = string.lower()
    string = string.replace(',','')

    if len(string) > length:
        string = string[:length]

    rep = list(map(lambda x: vocab.get(x, '<unk>'), string))

    if len(string) < length:
        rep += [vocab['<pad>']] * (length - len(string))

    #print (rep)
    return rep
'''

def int_to_string(ints, inv_vocab):
    """
    Output a machine readable list of characters based on a list of indexes in the machine's vocabulary

    Arguments:
    ints -- list of integers representing indexes in the machine's vocabulary
    inv_vocab -- dictionary mapping machine readable indexes to machine readable characters

    Returns:
    l -- list of characters corresponding to the indexes of ints thanks to the inv_vocab mapping
    """

    l = [inv_vocab[i] for i in ints]
    return l




#path = 'C:\\Users\\vegon\\Desktop\\new\\dataset\\modified\\'
#os.chdir(path)
#np.savetxt("output.csv", output, delimiter=",")
#np.savetxt("data.csv", data, delimiter=",")            raise ab error

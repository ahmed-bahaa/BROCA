import csv
import pickle
import  numpy as np

mydict={0:'i',1:'love',2:'you',3:'family',4:'b',5:'r',6:'o',7:'c',8:'a'}
np.save('dataset\\modified\\index_vocab_dict.npy',mydict)
print("index to word dict done ")

mydict2={'i':0,'love':1,'you':2,'family':3,'b':4,'r':5,'o':6,'c':7,'a':8}
np.save('dataset\\modified\\vocab_index_dict.npy',mydict2)
print("word to index dict done ")








'''
mydict={0:'i',1:'love',2:'you',3:'family',4:'b',5:'r',6:'o',7:'c',8:'a'}
with open('dataset\\modified\\index_vocab_dict.pkl', 'wb') as f:
    pickle.dump(mydict, f,pickle.HIGHEST_PROTOCOL)
    print("index to word dict done ")


mydict2={'i':0,'love':1,'you':2,'family':3,'b':4,'r':5,'o':6,'c':7,'a':8}
with open('dataset\\modified\\vocab_index_dict.pkl', 'wb') as f:
    pickle.dump(mydict2, f,pickle.HIGHEST_PROTOCOL)
    print("word to index dict done ")

'''



'''
import csv

mydict={0:'i',1:'love',2:'you',3:'family',4:'b',5:'r',6:'o',7:'c',8:'a'}
with open('dataset\\modified\\index_vocab_dict.csv', 'ab') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
       writer.writerow([key, value])
    print("index to word dict done ")


mydict={'i':0,'love':1,'you':2,'family':3,'b':4,'r':5,'o':6,'c':7,'a':8}
with open('dataset\\modified\\vocab_index_dict.csv', 'ab') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
       writer.writerow([key, value])
    print("word to index dict done ")

'''


'''
    def save_obj(obj, name ):
    with open('obj/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def load_obj(name ):
    with open('obj/' + name + '.pkl', 'rb') as f:
        return pickle.load(f)
'''

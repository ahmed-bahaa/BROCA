# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import pickle
import  numpy as np



mydict={0:'<unk>',
        1:'<pad>',
        2:'أُريد',
        3:'شهادة',
        4:'ميلاد',
        5:'وفاة',
        6:'صفراء',
        7:'بِطاقه',
        8:'عمل',
        9:'توكيل',
        10:'السلام_عليكم',
        11:'كيف_الحال',
        12:'الحمد_لله',
        13:'جيد',
        14:'تنفس',
        15:'مفيش',
        16:'مكتوم',
        17:'رؤية',
        18:'الضغط',
        19:'قرض'
        }

np.save('dataset\\modified\\index_vocab_dict.npy',mydict)
print("index to word dict done ")


mydict2={'<unk>':0,
         '<pad>':1,
         'أُريد':2,
         'شهادة':3,
         'ميلاد':4,
         'وفاة':5,
         'صفراء':6,
         'بِطاقه':7,
         'عمل':8,
         'توكيل':9,
         'السلام_عليكم':10
         'كيف_الحال':11
         'الحمد_لله':12,
         'جيد':13,
         'تنفس':14,
         'مفيش':15,
         'مكتوم':16,
         'رؤية':17,
         'الضغط':18,
         'قرض':19
                           }

np.save('dataset\\modified\\vocab_index_dict.npy',mydict2)
print("word to index dict done ")

map_dict={        'G1':'أًريد شهادة ميلاد'
                , 'G2':'أًريد شهادة وفاة صفراء'
                , 'G3':'أُريد بِطاقه'
                , 'G4':'أُريد عمل توكيل'
                , 'G5':'السلام_عليكم'
                , 'G6':'كيف_الحال'
                , 'G7':'الحمد_لله جيد'
                , 'G8':'تنفس مفيش مكتوم'
                , 'G9':'أُريد رؤية الضغط'
                , 'G10':'أُريد قرض'
        }

"""
map_dict={        'G1':'aorid shahdt melad'
                , 'G2':'aorid shahdt wafaa safra'
                , 'G3':'aorid btaka'
                , 'G4':'aorid 3aml tawkeel'
                , 'G5':'slamo_3lko'
        }
"""
np.save('dataset\\modified\\map_dict.npy',map_dict)
print("gestures mapping dict done ")

"""
notes:
make <unk> :0
     <pad> :1
to be fixed in codes after any addition in dictionary

mydict2: will be like this:
G1:1
G2:2
.....

mydict2:
1:Family or 3a'ela
2:.....
"""






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

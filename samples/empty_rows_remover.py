import numpy as np
import os
import glob
import csv
import pandas as pd
global L
L=5




df = pd.read_csv('a_10.csv')
df = df.drop(df.columns[[1,2,6,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36
                                         ,218,234,235,236,237,238,239,240,241,241,242,243,244,245,246,247,248]], axis=1)
# print(df[0:9].shape[0])
#print(df.shape)
#print(df)
l=list(set(np.where(pd.isnull(df))[0]))      #list of indecies for empty rows
df=df.drop(df.index[l])

df.to_csv("a.csv", sep=',', index=True, header=True)
#print(name[0])

print ("hello git")

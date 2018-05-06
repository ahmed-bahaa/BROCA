# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from keras.layers import Bidirectional, Concatenate, Permute, Dot, Input, LSTM, Multiply
from keras.layers import RepeatVector, Dense, Activation, Lambda ,Flatten
from keras.optimizers import Adam
from keras.utils import to_categorical
from keras.models import load_model, Model
import keras.backend as K
import numpy as np
from keras.models import Sequential
import random
from tqdm import tqdm
from loader_v2 import *
from br_util import *
from numpy import argmax
from keras.layers.normalization import BatchNormalization
from gtts import gTTS
import time
import os
np.random.seed(12345)
no_pers=8                                         #no of persons to collect
#X_train,Y_train,X_test,Y_test,f,s=lo_data2()
in_v_dic,v_in_dic,map_dict=load_dict()
with open('dataset\\modified\\parameters.csv', "rt") as f:
    reader = list(csv.reader(f))[0]
    no_gestures  = int(reader[0])
    s = int(reader[1])
    f  = 109
    no_dynfiles= int(reader[3])
"""
X        :   input frames as 3 dimension
Y        :   1D list of output labels
f        :   number of features per frame             (mostly 426 features)
g        :   number of input gestures                 (length of the training dataset)
s        :   maximum number of sequences per gesture  (also it will be no. inputs for RNN)
in_v_dic :   index to vocab dictionary
v_in_dic :   vocab to index dictionary
"""

print("index to vocab")
print(in_v_dic)
print("vocab to index")
print(v_in_dic)

Tx=s
Ty=4
#Yoh_train=preprocess_data(Y_train,v_in_dic,map_dict,Ty)
#Yoh_test=preprocess_data(Y_test,v_in_dic,map_dict,Ty)




# Defined shared layers as global variables
repeator = RepeatVector(Tx)
concatenator = Concatenate(axis=-1)
densor = Dense(1, activation = "relu")
activator = Activation(softmax, name='attention_weights') # We are using a custom softmax(axis = 1) loaded in this notebook
dotor = Dot(axes = 1)



def one_step_attention(a, s_prev):
    """
    Performs one step of attention: Outputs a context vector computed as a dot product of the attention weights
    "alphas" and the hidden states "a" of the Bi-LSTM.

    Arguments:
    a -- hidden state output of the Bi-LSTM, numpy-array of shape (m, Tx, 2*n_a)
    s_prev -- previous hidden state of the (post-attention) LSTM, numpy-array of shape (m, n_s)

    Returns:
    context -- context vector, input of the next (post-attetion) LSTM cell
    """

    ### START CODE HERE ###
    # Use repeator to repeat s_prev to be of shape (m, Tx, n_s) so that you can concatenate it with all hidden states "a" ( 1 line)
    s_prev = repeator(s_prev)
    # Use concatenator to concatenate a and s_prev on the last axis ( 1 line)
    concat = concatenator([s_prev,a])
    # Use densor to propagate concat through a small fully-connected neural network to compute the "energies" variable e. (1 lines)

    e = densor(concat)

    e= BatchNormalization()(e)
    # Use activator and e to compute the attention weights "alphas" ( 1 line)
    alphas = activator(e)
    # Use dotor together with "alphas" and "a" to compute the context vector to be given to the next (post-attention) LSTM-cell ( 1 line)
    context = dotor([alphas,a])
    ### END CODE HERE ###

    return context


# You will be able to check the expected output of `one_step_attention()` after you've coded the `model()` function.

# **Exercise**: Implement `model()` as explained in figure 2 and the text above. Again, we have defined global layers that will share weights to be used in `model()`.

# In[8]:

n_a = 64
n_s = 128
post_activation_LSTM_cell = LSTM(n_s, return_state = True)
output_layer = Dense(len(v_in_dic), activation=softmax)


# Now you can use these layers $T_y$ times in a `for` loop to generate the outputs, and their parameters will not be reinitialized. You will have to carry out the following steps:
#
# 1. Propagate the input into a [Bidirectional](https://keras.io/layers/wrappers/#bidirectional) [LSTM](https://keras.io/layers/recurrent/#lstm)
# 2. Iterate for $t = 0, \dots, T_y-1$:
#     1. Call `one_step_attention()` on $[\alpha^{<t,1>},\alpha^{<t,2>}, ..., \alpha^{<t,T_x>}]$ and $s^{<t-1>}$ to get the context vector $context^{<t>}$.
#     2. Give $context^{<t>}$ to the post-attention LSTM cell. Remember pass in the previous hidden-state $s^{\langle t-1\rangle}$ and cell-states $c^{\langle t-1\rangle}$ of this LSTM using `initial_state= [previous hidden state, previous cell state]`. Get back the new hidden state $s^{<t>}$ and the new cell state $c^{<t>}$.
#     3. Apply a softmax layer to $s^{<t>}$, get the output.
#     4. Save the output by adding it to the list of outputs.
#
# 3. Create your Keras model instance, it should have three inputs ("inputs", $s^{<0>}$ and $c^{<0>}$) and output the list of "outputs".

# In[9]:

# GRADED FUNCTION: model

def model(Tx, Ty, n_a, n_s, human_vocab_size, machine_vocab_size):
    """
    Arguments:
    Tx -- length of the input sequence
    Ty -- length of the output sequence
    n_a -- hidden state size of the Bi-LSTM
    n_s -- hidden state size of the post-attention LSTM
    human_vocab_size -- size of the python dictionary "human_vocab"
    machine_vocab_size -- size of the python dictionary "machine_vocab"

    Returns:
    model -- Keras model instance
    """

    # Define the inputs of your model with a shape (Tx,)
    # Define s0 and c0, initial hidden state for the decoder LSTM of shape (n_s,)
    X = Input(shape=(Tx, human_vocab_size))
    s0 = Input(shape=(n_s,), name='s0')
    c0 = Input(shape=(n_s,), name='c0')
    out0 = Input(shape=(machine_vocab_size,), name='O0')

    s = s0
    c = c0
    out = out0
    # Initialize empty list of outputs
    outputs = []

    ### START CODE HERE ###

    # Step 1: Define your pre-attention Bi-LSTM. Remember to use return_sequences=True. ( 1 line)
    #a = Bidirectional(LSTM(n_a,return_sequences=True)([X,s0]))

    a = Bidirectional(LSTM(n_a, return_sequences=True))(X)

    # Step 2: Iterate for Ty steps
    for t in range(Ty):

        # Step 2.A: Perform one step of the attention mechanism to get back the context vector at step t ( 1 line)
        context = one_step_attention(a, s)

        # Step 2.B: Apply the post-attention LSTM cell to the "context" vector.
        # Don't forget to pass: initial_state = [hidden state, cell state] ( 1 line)
        context_out=concatenator([context,out])
        s, _, c = post_activation_LSTM_cell(initial_state = [s, c] , inputs=context_out)

        # Step 2.C: Apply Dense layer to the hidden state output of the post-attention LSTM ( 1 line)

        out = output_layer(s)

        # Step 2.D: Append "out" to the "outputs" list (1 line)
        outputs.append(out)

    # Step 3: Create model instance taking three inputs and returning the list of outputs. (1 line)

    model = Model(inputs=[X,s0,c0,out0],outputs=outputs)

    ### END CODE HERE ###

    return model



model = model(Tx, Ty, n_a, n_s, f, len(v_in_dic))


model.summary()

model.load_weights('models\\model_10.h5',by_name=True)
### START CODE HERE ### (2 lines)
opt = Adam(lr=0.005, beta_1=0.9, beta_2=0.999, decay=0.01)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
### END CODE HERE ###




#outputs = list(Yoh_train.swapaxes(0,1))
#model.fit([X, s0, c0], Yoh, epochs=50, batch_size=100)




#print(model.evaluate([X_train,s0,c0,out], outputs, verbose=0))


def predict_fun(z):
        #print(model.evaluate([X,s0,c0], Yoh, verbose=0))
        #print(z)
        m=z.shape[0]
        z=np.array(z).astype('float32')
        s0 = np.zeros((m, n_s)).astype('float32')
        c0 = np.zeros((m, n_s)).astype('float32')
        out = np.zeros((m, len(v_in_dic))).astype('float32')
        prediction = model.predict([z,s0,c0,out])
        #print(prediction)
        prediction = np.argmax(prediction, axis = -1)
        #print(prediction)
        ou = [in_v_dic[int(i)] for i in prediction]
        print("")
        print( ' '.join(ou).replace('<pad>','').replace('_',' '))
        word=(' '.join(ou).replace('<pad>','').replace('_',' '))
        print("")
        mytext = word
        language = 'ar'

        myobj = gTTS(text=mytext, lang=language, slow=False)

        myobj.save("high.mp3")
        path=os.getcwd()
        path=path+"\\high.mp3"
        os.system(path)

        time.sleep(3)
        os.remove("high.mp3")

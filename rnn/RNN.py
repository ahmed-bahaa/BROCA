from keras.layers import Bidirectional, Concatenate, Permute, Dot, Input, LSTM, Multiply
from keras.layers import RepeatVector, Dense, Activation, Lambda ,Flatten
from keras.optimizers import Adam
from keras.utils import to_categorical
from keras.models import load_model, Model
import keras.backend as K
import numpy as np
from keras.models import Sequential
import random
from nmt_utils import *
import matplotlib.pyplot as plt
from keras.models import model_from_json
from br_util import *
from numpy import argmax
#get_ipython().magic('matplotlib inline')
np.random.seed(12345)
no_pers=3                                       #no of persons to collect

X,Y,f,g,s=load_dataset(no_pers)
in_v_dic,v_in_dic=load_dict()

"""
X        :   input frames as 3 dimension
Y        :   1D list of output labels
f        :   number of features per frame             (mostly 426 features)
g        :   number of input gestures                 (length of the training dataset)
s        :   maximum number of sequences per gesture  (also it will be no. inputs for RNN)
in_v_dic :   index to vocab dictionary
v_in_dic :   vocab to index dictionary
"""
print (Y[0])

print("index to vocab")
print(in_v_dic)

print("vocab to index")
print(v_in_dic)
m=g
Tx=s
Ty=1
Yoh=preprocess_data(Y,v_in_dic,Ty)
print(Yoh.shape)
'''
print(Y[1])
print(Yoh[1])
print(Y[200])
print(Yoh[200])
print(Y[500])
print(Yoh[500])
print(Y[1500])
print(Yoh[1500])

print(argmax(Yoh[1]))                # from one hot vector to integer
'''

print("X.shape:", X.shape)
print("Y.shape:", Y.shape)
print("Yoh.shape:", Yoh.shape)


'''
index = 0
print("Source date:", dataset[index][0])
print("Target date:", dataset[index][1])
print()
print("Source after preprocessing (indices):", X[index])
print("Target after preprocessing (indices):", Y[index])
print()
print("Source after preprocessing (one-hot):", Xoh[index])
print("Target after preprocessing (one-hot):", Yoh[index])
'''


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
    # Use activator and e to compute the attention weights "alphas" ( 1 line)
    alphas = activator(e)
    # Use dotor together with "alphas" and "a" to compute the context vector to be given to the next (post-attention) LSTM-cell ( 1 line)
    context = dotor([alphas,a])
    ### END CODE HERE ###

    return context


# You will be able to check the expected output of `one_step_attention()` after you've coded the `model()` function.

# **Exercise**: Implement `model()` as explained in figure 2 and the text above. Again, we have defined global layers that will share weights to be used in `model()`.

# In[8]:

n_a = 512
n_s = 1024
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
    s = s0
    c = c0

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
        s, _, c = post_activation_LSTM_cell(initial_state = [s, c] , inputs=context)

        # Step 2.C: Apply Dense layer to the hidden state output of the post-attention LSTM ( 1 line)

        out = output_layer(s)

        # Step 2.D: Append "out" to the "outputs" list (1 line)
        outputs.append(out)

    # Step 3: Create model instance taking three inputs and returning the list of outputs. (1 line)

    model = Model(inputs=[X,s0,c0],outputs=outputs)

    ### END CODE HERE ###

    return model


# Run the following cell to create your model.

# In[10]:

model = model(Tx, Ty, n_a, n_s, f, len(v_in_dic))


# Let's get a summary of the model to check if it matches the expected output.

# In[11]:

model.summary()


### START CODE HERE ### (2 lines)
opt = Adam(lr=0.005, beta_1=0.9, beta_2=0.999, decay=0.01)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])
### END CODE HERE ###


# The last step is to define all your inputs and outputs to fit the model:
# - You already have X of shape $(m = 10000, T_x = 30)$ containing the training examples.
# - You need to create `s0` and `c0` to initialize your `post_activation_LSTM_cell` with 0s.
# - Given the `model()` you coded, you need the "outputs" to be a list of 11 elements of shape (m, T_y). So that: `outputs[i][0], ..., outputs[i][Ty]` represent the true labels (characters) corresponding to the $i^{th}$ training example (`X[i]`). More generally, `outputs[i][j]` is the true label of the $j^{th}$ character in the $i^{th}$ training example.

# In[ ]:

s0 = np.zeros((m, n_s))
c0 = np.zeros((m, n_s))
#outputs = list(Yoh.swapaxes(0,1))
#print(outputs.shape)


# Let's now fit the model and run it for one epoch.

# In[ ]:

model.fit([X, s0, c0], Yoh, epochs=100, batch_size=50)
#model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

#from keras.models import load_model
model.save('models\\model_9.h5')
model.save_weights('models\\model_w_9.h5')
model_json = model.to_json()
with open("models\\model_j_9.json", "w") as json_file:
    json_file.write(model_json)
np.save("models\\\model_w_9_np",model.get_weights())
#print(model.get_weights())
'''
model = load_model('my_model.h5')
model.load_weights('my_model_weights.h5')
model.load_weights('my_model_weights.h5', by_name=True)
'''



'''
EXAMPLES = ['3 May 1979', '5 April 09', '21th of August 2016', 'Tue 10 Jul 2007', 'Saturday May 9 2018', 'March 3 2001', 'March 3rd 2001', '1 March 2001']
for example in EXAMPLES:

    source = string_to_int(example, Tx, human_vocab)
    source = np.array(list(map(lambda x: to_categorical(x, num_classes=len(human_vocab)), source))).swapaxes(0,1)
    prediction = model.predict([source, s0, c0])
    prediction = np.argmax(prediction, axis = -1)
    output = [inv_machine_vocab[int(i)] for i in prediction]

    print("source:", example)
    print("output:", ''.join(output))


# You can also change these examples to test with your own examples. The next part will give you a better sense on what the attention mechanism is doing--i.e., what part of the input the network is paying attention to when generating a particular output character.
'''


model.summary()


#z=X[1000].reshape(1,s,f)
z=X[1000:1060,:,:]
prediction = model.predict([z,s0,c0])

#print(prediction)

print(Y[1000:1060])
#print(X[1])
prediction = np.argmax(prediction, axis = -1)
ou = [in_v_dic[int(i)] for i in prediction]
print(ou)

z=X[400:450,:,:]
prediction = model.predict([z,s0,c0])

print(Y[400:450])
#print(X[1])
prediction = np.argmax(prediction, axis = -1)
ou = [in_v_dic[int(i)] for i in prediction]
print(ou)


z=X[1890:1905,:,:]
prediction = model.predict([z,s0,c0])

print(Y[1890:1905])
#print(X[1])
prediction = np.argmax(prediction, axis = -1)
ou = [in_v_dic[int(i)] for i in prediction]
print(ou)

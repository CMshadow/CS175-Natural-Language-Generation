# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 15:14:54 2018

@author: Daniel Maher
"""

""" Recurrent Neural Network for Language Generation """

import ngram_sentence as ns
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Embedding, SimpleRNN, LSTM
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
speeches = ns.generate_local_rawtext(["obama_speeches.txt"])

# translate text into int tokens
vocab_size = 20000 + 1
tokenizer = Tokenizer(num_words=vocab_size-1, filters="\n\t")
tokenizer.fit_on_texts([speeches])
encoded_text = tokenizer.texts_to_sequences([speeches])[0]

print ("Text: " + speeches[69:300])
print ("Encodings: " + str(encoded_text[:100]))

sequences = list()
for i in range(1, len(encoded_text)):
    sequence = encoded_text[i-1:i+1]
    sequences.append(sequence)
print ("total sequences: %d" % len(sequences))

sequences = np.array(sequences)
X_train, y_train = sequences[:,0], sequences[:,1]
y_train = to_categorical(y_train, num_classes=vocab_size)

print (X_train)
print (y_train)

h1_size = 100
h_RNN_size = 500

model = Sequential()
model.add(Embedding(vocab_size, h1_size, input_length = 1))
model.add(LSTM(h_RNN_size))
model.add(Dense(vocab_size, activation="softmax"))

model.summary()

adam = keras.optimizers.Adam(lr=0.005)
model.compile(optimizer=adam, loss = 'categorical_crossentropy', metrics = ['accuracy'])

from keras.models import load_model
#train_log = model.fit(X_train, y_train, epochs=10, batch_size=64)
model = load_model('speeches_rnn.h5')

def generate_seq(model, tokenizer, seed_text, n_words, temperature=1.):
    in_text, result = seed_text, seed_text
    
    # generate a fixed number of words
    for _ in range(n_words):
        encoded = tokenizer.texts_to_sequences([in_text])[0]
        encoded = np.array(encoded)
        
        # get the probabilities of each vocabulary word
        word_probs = model.predict(encoded, verbose=0)[0]
    
        # add a temperature to create more sampling variation
        word_probs = np.log(word_probs) / temperature
        word_probs = np.exp(word_probs) / np.sum(np.exp(word_probs))
        yhat = np.random.choice(range(word_probs.shape[0]), p=word_probs)
    
        # map predicted word index to word
        out_word = ""
        for word, index in tokenizer.word_index.items():
            if index == yhat:
                out_word = word
                break
    
        # append to input
        in_text, result = out_word, result + " " + out_word

    return result

text = generate_seq(model, tokenizer, seed_text='america', n_words=150, temperature=1.)
print (text)


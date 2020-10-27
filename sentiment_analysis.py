import json
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

#######################
vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
training_size = 20000
#######################



with open("TensorFlow_tut/Resources/Sarcasm.json" , "r") as file:
    dataset = json.load(file)

headlines = []
urls = []
labels = []

for data in dataset:
    headlines.append(data["headline"])
    urls.append(data["article_link"])
    labels.append(data["is_sarcastic"])

print(len(headlines))
#data_split
training_sentences = headlines[:training_size]
training_labels = labels[:training_size]

test_sentences = headlines[training_size:]
test_labels = labels[training_size:]

#sent to vector

tokenizer = Tokenizer(num_words = vocab_size, oov_token= "<OOV>")
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index

training_sequences = tokenizer.texts_to_sequences(training_sentences)
training_padded = pad_sequences(training_sequences,padding = "post", maxlen = max_length,truncating=trunc_type)
test_sequences = tokenizer.texts_to_sequences(test_sentences)
test_padded = pad_sequences(test_sequences,padding = "post", maxlen = max_length,truncating=trunc_type)

import numpy as np
training_padded = np.array(training_padded)
training_labels = np.array(training_labels)
test_padded = np.array(test_padded)
test_labels = np.array(test_labels)
print(training_padded.shape)

# print(training_padded[:2])

# print(type(training_padded))

######################
# model

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim , input_length = max_length), #calculating vector word by word
    tf.keras.layers.GlobalAveragePooling1D(),  #averaging sum of all the vector 
    tf.keras.layers.Dense(24, activation = "relu"),
    tf.keras.layers.Dense(1, activation = "sigmoid")
])

model.compile(loss = "binary_crossentropy", optimizer = "adam", metrics = ["accuracy"])

num_epochs =30
history = model.fit(training_padded , training_labels , epochs = num_epochs  , validation_data = (test_padded,test_labels), verbose = 2)

import matplotlib.pyplot as plt


def plot_graphs(history, string):
  plt.plot(history.history[string])
  plt.plot(history.history['val_'+string])
  plt.xlabel("Epochs")
  plt.ylabel(string)
  plt.legend([string, 'val_'+string])
  plt.show()
  
plot_graphs(history, "accuracy")
plot_graphs(history, "loss")

sentence = ["granny starting to fear spiders in the garden might be real", "game of thrones season finale showing this sunday night"]
sequences = tokenizer.texts_to_sequences(sentence)
padded = pad_sequences(sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)
print(model.predict(padded))
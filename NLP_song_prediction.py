import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers  import Embedding , LSTM , Bidirectional , Dense
from tensorflow.keras.optimizers import Adam
import numpy as np





data = open("TensorFlow_tut/Resources/irish-lyrics-eof.txt").read()
#make word corpus
corpus = data.lower().split("\n")

tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
word_index = tokenizer.word_index
# print(len(word_index))
total_words = len(word_index)+1
print(total_words)
#input sequence
input_sequence = []
for line in corpus:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1 , len(token_list)):
        n_gram_sequence = token_list[:i+1]
        input_sequence.append(n_gram_sequence)

# print(input_sequence[0:5])
#padding
max_sequence_len = max([len(i) for i in input_sequence])
input_sequence = np.array(pad_sequences(input_sequence , padding = "pre", maxlen = max_sequence_len))
# print(input_sequence[0:5])

#preparing Xs and Ys
Xs , labels = input_sequence[:, :-1] , input_sequence[:,-1]

labels = tf.keras.utils.to_categorical(labels , num_classes = total_words)
# print(tokenizer.word_index['lanigan'])
# print(Xs[1791])
# print(labels[1791])


#model
tensorboard = tf.keras.callbacks.TensorBoard(log_dir="TensorFlow_tut/logs/NLP_song_1", histogram_freq=1)
model = Sequential()
model.add(Embedding(total_words , 100 , input_length = max_sequence_len -1 ))
model.add(Bidirectional(LSTM(150)))
model.add(Dense(total_words, activation = "softmax"))

adam = Adam(lr = 0.01)
model.compile(loss = "categorical_crossentropy", optimizer = adam , metrics = ["accuracy"])
earlystop = tf.keras.callbacks.EarlyStopping(monitor='loss', min_delta=0, patience=5, verbose=0, mode='auto')
history = model.fit(Xs , labels , epochs = 100 , verbose = 1, callbacks=[earlystop , tensorboard])
print(model.summary())


import matplotlib.pyplot as plt


def plot_graphs(history, string):
  plt.plot(history.history[string])
  plt.xlabel("Epochs")
  plt.ylabel(string)
  plt.show()

plot_graphs(history, 'accuracy')
#poem generation

model.save("TensorFlow_tut/Resources/saved_models/NLP-1")

seed_text = "I've got a bad feeling about this"
next_words = 100
  
for _ in range(next_words):
	token_list = tokenizer.texts_to_sequences([seed_text])[0]
	token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
	predicted = model.predict_classes(token_list, verbose=0)
	output_word = ""
	for word, index in tokenizer.word_index.items():
		if index == predicted:
			output_word = word
			break
	seed_text += " " + output_word
print(seed_text)

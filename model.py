import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from tensorflow.python import keras
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Flatten, Conv2D, Dropout

from keras import optimizers

img_rows, img_cols = 28, 28
num_classes = 10

#preprocessing img data
def data_prep(raw):
	out_y = keras.utils.to_categorical(raw.label, num_classes)

	num_images = raw.shape[0]
	x_as_array = raw.values[:,1:]
	x_shaped_array = x_as_array.reshape(num_images, img_rows, img_cols, 1)
	out_x = x_shaped_array/255

	return out_x, out_y

raw_data = pd.read_csv('train.csv')

x, y = data_prep(raw_data)

#sequential model with 4 layers
model = Sequential()
model.add(Conv2D(20, kernel_size=(3,3), activation='relu', input_shape=(img_rows, img_cols, 1)))
model.add(Dropout(0.5))
model.add(Conv2D(20, kernel_size=(3,3), activation='relu'))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy, optimizer='adam', metrics=['accuracy'])

model.fit(x, y, batch_size=128, epochs=2, validation_split=0.2)
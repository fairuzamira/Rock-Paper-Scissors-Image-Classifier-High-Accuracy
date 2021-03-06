# -*- coding: utf-8 -*-
"""Rock-Paper-Scissors-Image Classifier-With-Accuracy-99%

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sgfIT-Shkjl8lOZLxGGLt3qAiFFeAR8s
"""

import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras import layers
from keras.layers import GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam

!wget --no-check-certificate \
  https://dicodingacademy.blob.core.windows.net/picodiploma/ml_pemula_academy/rockpaperscissors.zip \
  -O /tmp/rockpaperscissors.zip

import zipfile,os
local_zip = '/tmp/rockpaperscissors.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp')
zip_ref.close()

base_dir = '/tmp/rockpaperscissors'
train_dir = os.path.join(base_dir, 'rps-cv-images')
validation_dir = os.path.join(base_dir, 'rps-cv-images')

os.listdir('/tmp/rockpaperscissors/rps-cv-images')

train_rock_dir = os.path.join(train_dir, 'rock')
train_paper_dir = os.path.join(train_dir, 'paper')
train_scissors_dir = os.path.join(train_dir, 'scissors')
validation_rock_dir = os.path.join(validation_dir, 'rock')
validation_paper_dir = os.path.join(validation_dir, 'paper')
validation_scissors_dir = os.path.join(validation_dir, 'scissors')

print('There are :', len(train_rock_dir), 'images of rock inside the folder.')
print('There are :', len(train_paper_dir), 'images of paper inside the folder.')
print('There are :', len(train_scissors_dir), 'images of scissors inside the folder.')

train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=30,
        horizontal_flip=True,
        shear_range = 0.2,
        zoom_range = 0.2,
        validation_split = 0.2,
        fill_mode = 'nearest')

train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(100, 100),
        batch_size=32,
        color_mode = 'rgb',
        shuffle=True,
        subset = 'training',
        class_mode = 'categorical')

validation_generator = train_datagen.flow_from_directory(
        validation_dir,
        target_size=(100, 100),
        batch_size=32,        
        color_mode = 'rgb',
        shuffle=False,
        subset = 'validation',
        class_mode = 'categorical')

class_base = keras.applications.VGG16(
    include_top=False, 
    weights='imagenet',
    input_shape=(100, 100, 3)
)
class_base.trainable = False

final_model = tf.keras.models.Sequential([
    class_base,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(3, activation='softmax')
])

final_model.summary()

final_model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

model_fit = final_model.fit_generator(
    train_generator,  
    validation_data  = validation_generator,
    epochs = 5, 
    verbose = 1
)

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
from google.colab import files
from keras.preprocessing import image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# %matplotlib inline

uploaded = files.upload()

for itr in uploaded.keys():
 
  path = itr
  picture = image.load_img(path, target_size=(130,120))
  imgplot = plt.imshow(picture)
  x = image.img_to_array(picture)
  x = np.expand_dims(x, axis=0)

  images = np.vstack([x])
  classes = final_model.predict(images, batch_size=7)
  define_class = int(classes.argmax(axis=-1))
  print("This image belongs to:", define_class)
  if (define_class==0):
    print("Paper Class")
  elif (define_class==1):
    print("Rock Class")
  elif (define_class==2):
    print("Scissors Class")
    
  print(itr)

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
from google.colab import files
from keras.preprocessing import image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# %matplotlib inline

uploaded = files.upload()

for itr in uploaded.keys():
 
  path = itr
  picture = image.load_img(path, target_size=(130,120))
  imgplot = plt.imshow(picture)
  x = image.img_to_array(picture)
  x = np.expand_dims(x, axis=0)

  images = np.vstack([x])
  classes = final_model.predict(images, batch_size=7)
  define_class = int(classes.argmax(axis=-1))
  print("This image belongs to:", define_class)
  if (define_class==0):
    print("Paper Class")
  elif (define_class==1):
    print("Rock Class")
  elif (define_class==2):
    print("Scissors Class")
    
  print(itr)

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
from google.colab import files
from keras.preprocessing import image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# %matplotlib inline

uploaded = files.upload()

for itr in uploaded.keys():
 
  path = itr
  picture = image.load_img(path, target_size=(130,120))
  imgplot = plt.imshow(picture)
  x = image.img_to_array(picture)
  x = np.expand_dims(x, axis=0)

  images = np.vstack([x])
  classes = final_model.predict(images, batch_size=7)
  define_class = int(classes.argmax(axis=-1))
  print("This image belongs to:", define_class)
  if (define_class==0):
    print("Paper Class")
  elif (define_class==1):
    print("Rock Class")
  elif (define_class==2):
    print("Scissors Class")
    
  print(itr)
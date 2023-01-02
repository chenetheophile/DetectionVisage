# %%
import numpy as np
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Dense,Flatten,Dropout
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
#from keras.layers.normalization import BatchNormalization
from tensorflow.keras.layers import BatchNormalization
from keras_preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import joblib

# %%
#train_dir="../input/face_recognition_dataset/Original_Images/Original_Images/"
#train_dir="/home/meatisdelicious/DetectionVisage/DetectionVisage/FaceDetectionV4/input/face_recognition_dataset/Original_Images/Original_Images/"
#Unmodified Dataset
#train_dir="input/face_recognition_dataset/Original_Images/Original_Images"
#Modified Dataset
train_dir="input/face_recognition_dataset/Original_Images_more/"

# Quand on a une classification à faire.
generator = ImageDataGenerator()
#seed : melange tjr de la meme manière le dataset à partir du meme argument
dataset = tf.keras.utils.image_dataset_from_directory(train_dir,image_size=(224, 224),batch_size=32, shuffle=True, seed=123)
dataset_size = len(dataset)
train_test_split=0.8
train_ds=dataset.take(int(train_test_split*dataset_size))
test_ds=dataset.skip(int(train_test_split*dataset_size))

classes = dataset.class_names


# %%
model = Sequential()
model.add(Conv2D(32, kernel_size = (3,3), activation='relu', input_shape=(224,224,3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(96, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(32, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(len(classes),activation='softmax'))

# %%
model.compile(
    loss = 'sparse_categorical_crossentropy',
    optimizer = 'adam',
    metrics=['binary_accuracy', 'categorical_accuracy'])
    #metrics = ["accuracy"])
model.summary()

# %%
#history = model.fit(train_ds,epochs= 30, batch_size=32)
history = model.fit(train_ds,epochs= 15, batch_size=32, validation_data=test_ds)

# %%
# Saving Model
filename = 'final_model1.hdf5'
joblib.dump(history, filename)

# %%
# load the model from disk
model_saved = joblib.load(filename)

# %%
plt.plot(model_saved.history['categorical_accuracy'])
plt.plot(model_saved.history['loss'])
plt.xlabel('Time')
plt.legend(['categorical_accuracy', 'loss'])
plt.show()

# %%
from sklearn.metrics import accuracy_score

def predict_image(image_path):
    img = image.load_img(image_path, target_size=(224,224,3))
    #plt.imshow(img)
    #plt.show()
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    
    pred = model.predict(images, batch_size=32)
    print(pred)

    # Prediction accuracy
    #--> le pb que j'arrive pas à resoudre est ici
    print("Score:",(np.argmax(pred)),"%")
    model.evaluate(test_ds)

    print("Actual result: "+(image_path.split("/")[-1]).split("_")[0])
    print("Predicted result: "+classes[np.argmax(pred)])

predict_image("/home/meatisdelicious/DetectionVisage/DetectionVisage/FaceDetectionV4/input/face_recognition_dataset/Original_Images/Original_Images/Brad Pitt/Brad Pitt_95.jpg")



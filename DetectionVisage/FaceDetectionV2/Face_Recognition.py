# Importing libraries
import tensorflow as tf
import numpy as np
import os

#root=os.path.dirname(os.path.realpath(__file__))
#img_path=root+"../DetectionVisage/img.jpg"

# Loading data and normalizing it
# We'll normalize the images as well as the keypoints. The shape of our input image will be
# ( 96 , 96 , 1 ) and the expected output will have a shape of ( 1 , 1 , 30 ).
# The output is from a Conv2D layer rather than the Dense layer.
x_train = np.load("Face_Images/x_train.npy") / 255
y_train = np.load("Face_Images/y_train.npy") / 96
x_test = np.load("Face_Images/x_test.npy") / 255
y_test = np.load("Face_Images/y_test.npy") / 96

y_train = np.reshape(y_train, (-1, 1, 1, 30))
y_test = np.reshape(y_test, (-1, 1, 1, 30))

model_layers = [
    tf.keras.layers.SeparableConv2D(128, input_shape=(96, 96, 1), kernel_size=(5, 5), strides=1),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.SeparableConv2D(128, kernel_size=(5, 5), strides=1),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),

    tf.keras.layers.SeparableConv2D(128, kernel_size=(5, 5), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(128, kernel_size=(5, 5), strides=1, activation='relu'),

    tf.keras.layers.SeparableConv2D(128, kernel_size=(5, 5), strides=1),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.SeparableConv2D(128, kernel_size=(5, 5), strides=1),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),

    tf.keras.layers.SeparableConv2D(128, kernel_size=(5, 5), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(128, kernel_size=(5, 5), strides=1, activation='relu'),

    tf.keras.layers.SeparableConv2D(128, kernel_size=(5, 5), strides=1),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.SeparableConv2D(128, kernel_size=(5, 5), strides=1),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),

    tf.keras.layers.SeparableConv2D(64, kernel_size=(5, 5), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(64, kernel_size=(5, 5), strides=1, activation='relu'),

    tf.keras.layers.SeparableConv2D(64, kernel_size=(5, 5), strides=1),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),
    tf.keras.layers.SeparableConv2D(64, kernel_size=(5, 5), strides=1),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Activation('relu'),

    tf.keras.layers.SeparableConv2D(64, kernel_size=(3, 3), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(64, kernel_size=(3, 3), strides=1, activation='relu'),

    tf.keras.layers.SeparableConv2D(64, kernel_size=(3, 3), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(64, kernel_size=(3, 3), strides=1, activation='relu'),

    tf.keras.layers.SeparableConv2D(64, kernel_size=(3, 3), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(64, kernel_size=(3, 3), strides=1, activation='relu'),

    tf.keras.layers.SeparableConv2D(32, kernel_size=(3, 3), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(32, kernel_size=(3, 3), strides=1, activation='relu'),

    tf.keras.layers.SeparableConv2D(32, kernel_size=(3, 3), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(32, kernel_size=(3, 3), strides=1, activation='relu'),

    tf.keras.layers.SeparableConv2D(32, kernel_size=(3, 3), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(32, kernel_size=(3, 3), strides=1, activation='relu'),

    tf.keras.layers.SeparableConv2D(32, kernel_size=(3, 3), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(32, kernel_size=(3, 3), strides=1, activation='relu'),

    tf.keras.layers.SeparableConv2D(32, kernel_size=(3, 3), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(32, kernel_size=(3, 3), strides=1, activation='relu'),

    tf.keras.layers.SeparableConv2D(32, kernel_size=(3, 3), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(32, kernel_size=(2, 2), strides=1, activation='relu'),

    tf.keras.layers.SeparableConv2D(30, kernel_size=(2, 2), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(30, kernel_size=(2, 2), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(30, kernel_size=(2, 2), strides=1, activation='relu'),
    tf.keras.layers.SeparableConv2D(30, kernel_size=(2, 2), strides=1, activation='sigmoid'),
]
model = tf.keras.Sequential(model_layers)
model.compile(loss=tf.keras.losses.mean_squared_error, optimizer=tf.keras.optimizers.Adam(lr=0.0001), metrics=['accuracy'])
model.summary()

# basic parameters for training :
#model.fit( x_train , y_train , epochs=30 , batch_size=50 , validation_data=( x_test , y_test ) )
# Training the model test
model.fit(x_train, y_train, epochs=6, batch_size=50, validation_data=(x_test, y_test))

# Generating keypoints for images
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(50, 50))
for i in range(1, 6):
    sample_image = np.reshape(x_test[i] * 255, (96, 96)).astype(np.uint8)
    pred = model.predict(x_test[i: i + 1]) * 96
    pred = pred.astype(np.int32)
    pred = np.reshape(pred[0, 0, 0], (15, 2))
    fig.add_subplot(1, 10, i)
    plt.imshow(sample_image.T, cmap='gray')
    plt.scatter(pred[:, 0], pred[:, 1], c='yellow')
plt.show()
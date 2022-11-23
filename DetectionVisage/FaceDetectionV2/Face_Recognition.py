# Deep Learning CNN model to recognize face
####### IMAGE PRE-PROCESSING for TRAINING and TESTING data #######
import os

# Specifying the folder where images are present

#TrainingImagePath='/Face_Images/Final_Training_Images'
root=os.path.dirname(os.path.realpath(__file__))
TrainingImagePath=root+'/Face_Images/Final_Training_Images/'

# importing packages :
import tensorflow as tf
import numpy as np

# Loading the data
import os

import tensorflow as tf
tf.keras.utils.get_file(origin="https://github.com/shubham0204/Dataset_Archives/blob/master/face_landmarks_cleaned.zip?raw=true",fname='train.csv',untar=False, extract=False)


# Normalising the images as keypoints

x_train = np.load("face_landmarks_cleaned/x_train.npy") / 255
y_train = np.load("face_landmarks_cleaned/y_train.npy") / 96
x_test = np.load("face_landmarks_cleaned/x_test.npy") / 255
y_test = np.load("face_landmarks_cleaned/y_test.npy") / 96

y_train = np.reshape(y_train,( -1 , 1 , 1 , 30 ))
y_test = np.reshape(y_test,( -1 , 1 , 1 , 30 ))
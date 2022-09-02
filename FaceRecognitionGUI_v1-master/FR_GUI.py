from keras.models import Sequential
from tensorflow.keras.layers import Conv2D, ZeroPadding2D, Activation, Input, concatenate
from keras.models import Model
from tensorflow.keras.layers import BatchNormalization
from keras.layers.pooling import MaxPooling2D, AveragePooling2D
from keras.layers.merge import Concatenate
from keras.layers.core import Lambda, Flatten, Dense
from keras.initializers import glorot_uniform
from tensorflow.keras.layers import Layer
from keras import backend as K
K.set_image_data_format('channels_first')
import cv2   #opencv
import os
import sys
import numpy as np
from numpy import genfromtxt
import pandas as pd
import tensorflow as tf
from fr_utils import *
from inception_blocks_v2 import *
from PIL import Image


np.set_printoptions(threshold=sys.maxsize)

FRmodel = faceRecoModel(input_shape=(3, 96, 96))
print("Total Params:", FRmodel.count_params())


def triplet_loss(y_true, y_pred, alpha = 0.2):
    """
    Implementation of the triplet loss as defined by formula
    
    Arguments:
    y_true -- true labels, required when you define a loss in Keras, you don't need it in this function.
    y_pred -- python list containing three objects:
            anchor -- the encodings for the anchor images, of shape (None, 128)
            positive -- the encodings for the positive images, of shape (None, 128)
            negative -- the encodings for the negative images, of shape (None, 128)
    
    Returns:
    loss -- real number, value of the loss
    """
    
    anchor, positive, negative = y_pred[0], y_pred[1], y_pred[2]
    pos_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, positive)), axis = -1)
    neg_dist = tf.reduce_sum(tf.square(tf.subtract(anchor, negative)), axis = -1)
    basic_loss = tf.add(tf.subtract(pos_dist, neg_dist), alpha)
    loss = tf.reduce_sum(tf.maximum(basic_loss, 0))
    return loss

#  Example
y_true = (None, None, None)
y_pred = (tf.random.normal([3,128], mean=6, stddev=0.1, seed=1),
        tf.random.normal([3, 128], mean=1, stddev=1, seed = 1),
        tf.random.normal([3, 128], mean=3, stddev=4, seed = 1))
loss = triplet_loss(y_true, y_pred)
print("[Debug] loss = " + str(loss.eval()))

print("Compliling Face Recognition Model ~")
FRmodel.compile(optimizer = 'adam', loss = triplet_loss, metrics = ['accuracy'])
load_weights_from_FaceNet(FRmodel)
print("Model Compiled.")

#Create a temp database
database = {}
database["Neha"] = img_to_encoding(r'C:\Users\cvpr\Documents\Bishal\FaceRecognitionGUI_v1-master\images\crop\neha1.jpg', FRmodel)
database["Kalu"] = img_to_encoding(r'C:\Users\cvpr\Documents\Bishal\FaceRecognitionGUI_v1-master\images\crop\kalu1.jpg', FRmodel)
database["Suds"] = img_to_encoding(r'C:\Users\cvpr\Documents\Bishal\FaceRecognitionGUI_v1-master\images\crop\suds1.jpg', FRmodel)


def who_is_it(image_path, database, model):
    """
    Implements face recognition by finding who is the person on the image_path image.
    
    Arguments:
    image_path -- path to an image
    database -- database containing image encodings along with the name of the person on the image
    model -- your Inception model instance in Keras
    
    Returns:
    min_dist -- the minimum distance between image_path encoding and the encodings from the database
    identity -- string, the name prediction for the person on image_path
    """

    encoding = img_to_encoding(image_path, model)
    min_dist = 100
    for (name, db_enc) in database.items():
        dist = np.linalg.norm(encoding - db_enc)
        if dist < min_dist:
            min_dist = dist
            identity = name

    if min_dist > 0.65:
        return("Not in the database.")
    else:
        return("It's " + str(identity)) #+ ", the distance is " + str(min_dist))

print(who_is_it(r'C:\Users\cvpr\Documents\Bishal\FaceRecognitionGUI_v1-master\images\crop\neha2.jpg', database, FRmodel))
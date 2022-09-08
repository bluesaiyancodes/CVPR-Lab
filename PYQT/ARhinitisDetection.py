from ast import main
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

    

# predicting images
def predictARhinitis(imgPath=r'C:/Users/cvpr/Documents/Bishal/Allergic Rhinitis/Dataset/non_rotate/dataset2/1/19_1_00002_right.tif'):
    model = load_model(r'C:\Users\cvpr\Documents\Bishal\Allergic Rhinitis\ARhinitisModel')
    model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
    (img_width, img_height) = (224, 224)
    img = image.load_img(imgPath, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    classes = model.predict(images/255, batch_size=10)
  #  print(np.argmax(classes, axis=1)[0])
  #  print(classes)
    return  np.argmax(classes, axis=1)[0]

if __name__ == '__main__':
    predictARhinitis()

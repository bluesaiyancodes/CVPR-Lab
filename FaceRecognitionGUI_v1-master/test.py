import os
import cv2

dir = r'C:\Users\cvpr\Documents\Bishal\FaceRecognitionGUI_v1-master'
print(os.listdir(dir))


path = r'C:\Users\cvpr\Documents\Bishal\FaceRecognitionGUI_v1-master\images\crop'
print(os.listdir(path))
img1 = cv2.imread(path)
print(img1)
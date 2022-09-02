import sys
import os
from tkinter.tix import Select
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ARhinitisDetection import predictARhinitis


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        QWidget.__init__(self, *args, **kwargs)

        #Set Window
        self.setGeometry(500,500,640,480)
        self.setWindowTitle("Allergic Rhinitis Detection")
      
        # Adding Label and button
        self.imgLabel = QLabel("Select an Image", self)
        self.btnChoose = QPushButton("Choose", self)
        self.btnChoose.clicked.connect(self.btnChooseAction)
        self.btnAsses = QPushButton("Asses Image", self)
        self.btnAsses.clicked.connect(self.btnAssesAction)



        self.layout = QGridLayout(self)
        self.groupbox = QGroupBox("AR Detection", checkable=False)
        self.layout.addWidget(self.groupbox)

        '''  
        self.hLayout = QHBoxLayout(self)
        self.hLayout.setContentsMargins(0,0,0,0)
        self.hLayout.addWidget(self.btnChoose)
        self.hLayout.addWidget(self.btnAsses)
        '''
    
        self.layout.addWidget(self.imgLabel, 0,0, Qt.AlignCenter)
        self.layout.addWidget(self.btnChoose,1,0, Qt.AlignRight)
        self.layout.addWidget(self.btnAsses, 2,0, Qt.AlignRight)


        #Setting Layout
        self.show()
        sys.exit(app.exec_())
    
    def btnChooseAction(self):
        print("Choose Button clicked")
        self.imgPath = self.open_file()
        self.imgLabel.setText(self.imgPath)
        #load image
        self.load_image(self.imgPath) 
        


    def btnAssesAction(self):
        print("Asses Button Clicked")
        print(self.imgPath)
        result = predictARhinitis(self.imgPath)
        print(result)
        if (result==0):
            self.imgLabel.setText("Allergic Rhinitis Prediciton - NEGATIVE")
        elif (result==1):
            self.imgLabel.setText("Allergic Rhinitis Prediciton - POSITIVE [MAST1]")
        elif (result==2):
            self.imgLabel.setText("Allergic Rhinitis Prediciton - POSITIVE [MAST2]")
        else:
            self.imgLabel.setText("Processing Error. Debug ASAP.")





    def open_file(self):
        path = QFileDialog.getOpenFileName(self, "Pick an Image", os.getenv('HOME'), "Images (*.png *.jpeg *.jpg *.bmp *.tif)")
        if path != ("", ""):
            print(path[0])
        return path[0]
    
    def load_image(self, imgPath):
        image = QImage()
        image.load(imgPath)
        # Set the pixmap using the QImage instance
        self.imgLabel.setPixmap(QPixmap.fromImage(image).scaled(224, 224, Qt.KeepAspectRatioByExpanding))
        # self.adjustSize() Auto adjusts the size of window based on the image size

        # Window Manipulation call
        self.postImgLoadWindow()

    def postImgLoadWindow(self):
        # Window Manipulation after the image is loaded
        # self.imgLabel.hide()
        return


if __name__ == '__main__':
   app = QApplication(sys.argv)
   win = Window()
   sys.exit(app.exec_())

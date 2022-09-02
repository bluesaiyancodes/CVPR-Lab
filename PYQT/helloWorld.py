import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Window(QWidget):
   def __init__(self, *args, **kwargs):
      QWidget.__init__(self, *args, **kwargs)

      #Set Window
      self.setGeometry(500,500,320,200)
      self.setWindowTitle("PyQt5 Example")
      
      # Adding Label and button
      self.label = QLabel("PyQT Testing", self)
      self.button = QPushButton("Test", self)
      self.btn_count = 0
      self.button.clicked.connect(self.button_clicked)


      layout = QGridLayout(self)
      groupbox = QGroupBox("Hello World!", checkable=False)
      layout.addWidget(groupbox)

      layout.addWidget(self.label, 0,0,1,0, Qt.AlignCenter)
      layout.addWidget(self.button,1,0, Qt.AlignRight)


      #Setting Layout

      
      self.show()
      sys.exit(app.exec_())

   def button_clicked(self):
      print("Button clicked")
      self.btn_count+=1
      self.label.setText("Button Clicked "+str(self.btn_count)+" times.")


def window():
   app = QApplication(sys.argv)
   widget = QWidget()

   label = QLabel(widget)
   label.setText("PyQT testing")
   label.move(50,50)

   
   button1 = QPushButton(widget)
   button1.setText("Button1")
   button1.move(64,32)
   button1.clicked.connect(button_clicked)

   widget.setGeometry(500,500,320,200)
   widget.setWindowTitle("PyQt5 Button Click Example")
   widget.show()
   sys.exit(app.exec_())


def button_clicked():
   print("Button 1 clicked")
  
   
if __name__ == '__main__':
   #window()
   app = QApplication(sys.argv)
   win = Window()
   sys.exit(app.exec_())

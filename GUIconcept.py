import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout)
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout Managers")
        self.setGeometry(100,100,300,300)
        self.setWindowIcon(QIcon("img.jpg"))
        self.initUI()

    def initUI(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)

        l1=QLabel("1",self)
        l2=QLabel("2",self)
        l3=QLabel("3",self)
        l4=QLabel("4",self)
        l5=QLabel("5",self)

        l1.setStyleSheet("Background-color:red;")
        l2.setStyleSheet("Background-color:green;")
        l3.setStyleSheet("Background-color:yellow;")
        l4.setStyleSheet("Background-color:blue;")
        l5.setStyleSheet("Background-color:orange;")

        hbox=QHBoxLayout()    #vbox -> to print vertically
        hbox.addWidget(l1) 
        hbox.addWidget(l2)
        hbox.addWidget(l3)
        hbox.addWidget(l4)
        hbox.addWidget(l5)

        central_widget.setLayout(hbox)


        '''
    #IMAGES
        label=QLabel(self)
        label.setGeometry(0,0,400,100)
        pixmap=QPixmap("imp.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry((self.width()-label.width())//2,
                          (self.height()-label.height())//2,
                          label.width(),
                          label.height())

    #LABELS
        label=QLabel("Hello",self)
        label.setFont(QFont("Arial",20))
        label.setGeometry(0,0,400,100)
        label.setStyleSheet("color:yellow;"
                            "background-color:red;"
                            "font-weight:bold;"
                            "font-style-italic;"
                            "text-decoration-underline;")
        #label.setAlignment(Qt.AlignTop)    #to align vertically top
        #label.setAlignment(Qt.AlignBottom)   #to align vertically bottom
        #label.setAlignment(Qt.AlignVCenter)  #vertically center
        #label.setAlignment(Qt.AlignRight)         #horizontally right
        #label.setAlignment(Qt.AlignHCenter)
        #label.setAlignment(Qt.AlignLeft)
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        label.setAlignment(Qt.AlignCenter)     #WE CAN ALSO USE->label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        '''
        

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())       #execute method

if __name__=="__main__":
    main()
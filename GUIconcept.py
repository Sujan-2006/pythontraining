import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QCheckBox
from PyQt5.QtGui import QPixmap, QIcon, QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check Box")
        self.setGeometry(600, 150, 500, 200)
        self.checkbox = QCheckBox("Do you like Cars?", self)
        self.checkbox.setGeometry(10, 30, 400, 60)
        self.checkbox.setStyleSheet("font-size: 30px; font-family: Arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("I like cars")
        else:
            print("I don't like Cars")

'''
#BUTTONS
    def initUI(self):
        
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        self.label.setGeometry(150,300,150,100)
        self.label.setStyleSheet("font-size:50 px;")

    def on_click(self):
        print("You pressed me!")
        self.label.setText("Konnochiwa!")
        #self.button.setText("Clicked")
        #self.button.setDisabled(True)
       
        #LAYOUT MANAGER

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

        grid=QGridLayout()    #vbox -> to print vertically
        grid.addWidget(l1,3,0) 
        grid.addWidget(l2,1,0)
        grid.addWidget(l3,1,1)
        grid.addWidget(l4,0,1)
        grid.addWidget(l5,2,2)

        central_widget.setLayout(grid)

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
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anime wa kakkoii!!")
        self.setGeometry(100,100,400,400)
        self.setWindowIcon(QIcon("img"))


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





def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())       #execute method

if __name__=="__main__":
    main()
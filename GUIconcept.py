import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Anime wa kakkoii!!")
        self.setGeometry(100,100,400,400)
        self.setWindowIcon(QIcon("img"))
def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())       #execute method

if __name__=="__main__":
    main()
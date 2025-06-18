import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt
from PyQt5.QtGui import QFont,QFontDatabase  #if ant font file downloaded for thr digital clock

class DC(QWidget):

    def __init__(self):
        super().__init__()
        self.l=QLabel(self)
        self.t=QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("DIGITAL CLOCK")
        self.setGeometry(500,300,400,200)

        vbox=QVBoxLayout()
        vbox.addWidget(self.l)
        self.setLayout(vbox)

        self.l.setAlignment(Qt.AlignCenter)
        self.l.setStyleSheet("font-size: 150px;"
                             "font-familt: Arial;"
                             "color: red;")
        self.setStyleSheet("background-color:black;")

        #fontid=QFontDatabase.addApplicationFont("file name of the font")
        #fontfamily=QFontDatabase.applicationFontFamilies(fontid)[0]
        #myfont=QFont(fontfamily,150)
        #self.l.setFont(myfont)

        self.t.timeout.connect(self.update_time)
        self.t.start(1000)
        self.update_time()

    def update_time(self):
        current_time=QTime.currentTime().toString("hh:mm:ss AP")
        self.l.setText(current_time)


if __name__=="__main__":
    app=QApplication(sys.argv)
    clock=DC()
    clock.show()
    sys.exit(app.exec_())
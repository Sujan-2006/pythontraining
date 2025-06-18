import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout,QHBoxLayout,QPushButton
from PyQt5.QtCore import QTimer,QTime,Qt

class SW(QWidget):

    def __init__(self):
        super().__init__()
        self.l=QLabel("00:00:00:00",self)  
        self.t=QTime(0,0,0,0)
        self.start_b=QPushButton("start",self)
        self.stop_b=QPushButton("stop",self)
        self.reset_b=QPushButton("reset",self)
        self.tt=QTimer(self)
        
        self.initUI()

    def initUI(self):
        self.setWindowTitle("STOP WATCH")
        self.setGeometry(500,300,400,200)
        vbox=QVBoxLayout()
        vbox.addWidget(self.l)
        vbox.addWidget(self.start_b)
        vbox.addWidget(self.stop_b)
        vbox.addWidget(self.reset_b)

        self.setLayout(vbox)
        self.l.setAlignment(Qt.AlignCenter)

        hbox=QHBoxLayout()
        hbox.addWidget(self.start_b)
        hbox.addWidget(self.stop_b)
        hbox.addWidget(self.reset_b)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
                           QPushButton,QLabel{
                           padding:10px;
                           font-weight:bold;
                           font-family:calibri;
                           }
                           QPushButton{
                           font-size=50px;
                           }
                           QLabel{
                           font-size:150px;
                           background-color: red;
                           border-radius:30px;
                           }
                           """)
        self.start_b.clicked.connect(self.start)
        self.stop_b.clicked.connect(self.stop)
        self.reset_b.clicked.connect(self.reset)
        self.tt.timeout.connect(self.update_display)

    def start(self):
        self.tt.start(10)

    def stop(self):
        self.tt.stop()

    def reset(self):
        self.tt.stop()
        self.t=QTime(0,0,0,0)
        self.l.setText(self.format_time(self.t))

    def format_time(self,t):
        hrs=t.hour()
        min=t.minute()
        sec=t.second()
        ms=t.msec()//10
        return f"{hrs:02}:{min:02}:{sec:02}:{ms:02}"

    def update_display(self):
        self.t=self.t.addMSecs(10)
        self.l.setText(self.format_time(self.t))

if __name__=="__main__":
    app=QApplication(sys.argv)
    sw=SW()
    sw.show()
    sys.exit(app.exec_())

import sys
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget, QVBoxLayout
from random import randint

class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("새창"+str(randint(1,100)))
        self.resize(250, 100)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w1 = None
        self.btn1 = QPushButton("create_new_window")
        self.btn1.clicked.connect(self.create_new_window)

        self.w2 = NewWindow()
        self.btn2 = QPushButton("show_existing_window")
        self.btn2.clicked.connect(self.show_existing_window)

        layout = QVBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
    
    def create_new_window(self):
        if self.w1 is None:
            self.w1 = NewWindow()
            self.w1.show()
        else:
            self.w1.close()
            self.w1 = None
    
    def show_existing_window(self):
        if self.w2.isVisible()==False:
            self.w2.show()
        elif self.w2.isVisible()==True:
            self.w2.close()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
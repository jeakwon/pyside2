# https://jeakwon.github.io/pyside2/pyside2-windows/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from random import randint

class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("새창"+str(randint(1,100)))
        self.resize(250, 100)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.btn1 = QPushButton("create_without_reference")
        self.btn1.clicked.connect(self.create_without_reference)
        self.btn2 = QPushButton("create_with_reference")
        self.btn2.clicked.connect(self.create_with_reference)

        layout = QVBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.btn2)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
    
    def create_without_reference(self):
        w = NewWindow()
        w.show()

    def create_with_reference(self):
        self.w = NewWindow()
        self.w.show()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
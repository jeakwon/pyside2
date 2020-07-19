# https://jeakwon.github.io/pyside2/pyside2-windows/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QCheckBox, QWidget
from random import randint

class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("새창"+str(randint(1,100)))
        self.resize(250, 100)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = NewWindow()

        self.chkbx1 = QCheckBox("show_and_close")
        self.chkbx1.clicked.connect(self.show_and_close)

        self.chkbx2 = QCheckBox("show_and_hide")
        self.chkbx2.clicked.connect(self.show_and_hide)

        self.chkbx3 = QCheckBox("set_visible")
        self.chkbx3.clicked.connect(self.set_visible)

        layout = QVBoxLayout()
        layout.addWidget(self.chkbx1)
        layout.addWidget(self.chkbx2)
        layout.addWidget(self.chkbx3)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
    
    def show_and_close(self):
        if self.w.isVisible():
            self.w.close()
        else:
            self.w.show()
        
    def show_and_hide(self):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
    
    def set_visible(self):
        if self.w.isVisible():
            self.w.setVisible(False)
        else:
            self.w.setVisible(True)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
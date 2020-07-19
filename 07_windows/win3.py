import sys
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QCheckBox, QWidget
from PySide2.QtCore import Qt
from random import randint

class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("새창"+str(randint(1,100)))
        self.resize(250, 100)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chkbx1 = QCheckBox("show_window_without_signal")
        self.chkbx1.clicked.connect(self.show_window_without_signal)
        self.chkbx2 = QCheckBox("show_window_with_signal")
        self.chkbx2.clicked.connect(self.show_window_with_signal)

        layout = QVBoxLayout()
        layout.addWidget(self.chkbx1)
        layout.addWidget(self.chkbx2)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.w = NewWindow()
    
    def show_window_without_signal(self):
        if self.w.isVisible()==False:
            self.w.show()
        elif self.w.isVisible()==True:
            self.w.close()
    
    def show_window_with_signal(self, checked):
        if checked:
            self.w.show()
        else:
            self.w.close()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
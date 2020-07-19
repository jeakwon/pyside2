import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QCheckBox, QWidget
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
        self.w1 = NewWindow()
        self.chkbx1 = QCheckBox("without_delete_on_close")
        self.chkbx1.clicked.connect(self.without_delete_on_close)

        self.w2 = NewWindow()
        self.chkbx2 = QCheckBox("with_delete_on_close")
        self.chkbx2.clicked.connect(self.with_delete_on_close)

        layout = QVBoxLayout()
        layout.addWidget(self.chkbx1)
        layout.addWidget(self.chkbx2)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
    
    def without_delete_on_close(self, checked):
        if checked:
            self.w1.show()
        else:
            self.w1.close()
    
    def with_delete_on_close(self, checked):
        self.w2.setAttribute(Qt.WA_DeleteOnClose)
        if checked:
            self.w2.show()
        else:
            self.w2.close()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
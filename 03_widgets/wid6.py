# https://jeakwon.github.io/pyside2/pyside2-widgets/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QListWidget()
        
        widget.addItems(["a", "b", "c"])
        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        
        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i.text())

    def text_changed(self, s):
        print(s)
        
app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
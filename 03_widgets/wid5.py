# https://jeakwon.github.io/pyside2/pyside2-widgets/

import sys
from PySide2.QtWidgets import QApplication, QComboBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QComboBox()

        widget.addItems(["First", "Second", "Third"])
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, data):
        print('index_changed', data)

    def text_changed(self, data):
        print('item_changed', data)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
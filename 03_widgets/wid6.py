# https://jeakwon.github.io/pyside2/pyside2-widgets/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QListWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QListWidget()
        
        widget.addItems(["First", "Second", "Third"])
        widget.currentItemChanged.connect(self.item_changed)
        widget.currentTextChanged.connect(self.text_changed)
        
        self.setCentralWidget(widget)

    def item_changed(self, data):
        print('item_changed', data.text())

    def text_changed(self, data):
        print('text_changed', data)
        
app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
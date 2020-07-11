# https://jeakwon.github.io/pyside2/pyside2-layouts/

from PySide2.QtGui import QColor, QPalette
from PySide2.QtWidgets import QWidget

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QTabWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QTabWidget()
        widget.setTabPosition(QTabWidget.North)
        
        for label in ["red", "green", "blue", "yellow"]:
            widget.addTab(Color(label), label)
            
        widget.setMovable(True)
        widget.setTabsClosable(True)
        widget.tabCloseRequested.connect(widget.removeTab)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
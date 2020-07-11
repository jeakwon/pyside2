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
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QTabWidget, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setMovable(True)
        tabs.setTabPosition(QTabWidget.North)
        
        for n, color in enumerate(["red", "green", "blue", "yellow"]):
            tabs.addTab(Color(color), color)
            
        self.setCentralWidget(tabs)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
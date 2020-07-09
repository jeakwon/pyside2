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
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        layout = QGridLayout()
        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("blue"), 0, 1)
        layout.addWidget(Color("yellow"), 1, 1)
        layout.addWidget(Color("black"), 2, 2)
        layout.addWidget(Color("white"), 100, 0)
        layout.addWidget(Color("grey"), 100, 100)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
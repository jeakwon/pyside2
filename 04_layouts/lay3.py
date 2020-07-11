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
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        l1 = QVBoxLayout()
        l1.addWidget(Color("red"))
        l1.addWidget(Color("green"))
        l1.addWidget(Color("blue"))
        l1.addWidget(Color("yellow"))
        layout.addLayout(l1)

        l2 = QVBoxLayout()
        l2.addWidget(Color("black"))
        l2.addWidget(Color("white"))
        layout.addLayout(l2)

        l3 = QVBoxLayout()
        l3.addWidget(Color("grey"))
        layout.addLayout(l3)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
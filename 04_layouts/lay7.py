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
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStackedLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        layout = QVBoxLayout()
        layout_top = QHBoxLayout()
        layout_bot = QStackedLayout()

        layout.addLayout(layout_top)
        layout.addLayout(layout_bot)

        for i, label in enumerate(["red", "green", "blue", "yellow"]):
            button = QPushButton(label)
            widget = Color(label)
            # def func(x=i):
            #     return layout_bot.setCurrentIndex(x)
            # button.pressed.connect(func)
            button.pressed.connect(lambda x=i: layout_bot.setCurrentIndex(x))

            layout_top.addWidget(button)
            layout_bot.addWidget(widget)

        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
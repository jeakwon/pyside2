# https://jeakwon.github.io/pyside2/pyside2-widgets/

import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("커피퐁당")
        self.setFixedSize(300, 100)

        label = QLabel("Cafe Fondant")

        font = label.font()
        font.setPointSize(20)
        font.setFamily("Century Gothic")
        font.setItalic(True)
        font.setUnderline(True)

        label.setFont(font)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(label)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
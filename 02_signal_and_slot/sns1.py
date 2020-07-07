# https://jeakwon.github.io/pyside2/pyside2-signal-and-slot/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Push")
        btn.clicked.connect(self.btn_clicked)

        self.setCentralWidget(btn)

    def btn_clicked(self):
        print("Clicked")

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
# https://jeakwon.github.io/pyside2/pyside2-signal-and-slot/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Push")
        btn.clicked.connect(self.btn_clicked)
        btn.clicked.connect(self.btn_toggled) # added from sns1.py
        btn.setCheckable(True) # added from sns1.py
        self.setCentralWidget(btn)

    def btn_clicked(self):
        print("Clicked")

    def btn_toggled(self, checked): # added from sns1.py
        self.btn_checked = checked # added from sns1.py
        print(self.btn_checked)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
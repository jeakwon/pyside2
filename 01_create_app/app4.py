# https://jeakwon.github.io/pyside2/pyside2-create-app/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("앱")

        btn = QPushButton("클릭")

        self.setCentralWidget(btn)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
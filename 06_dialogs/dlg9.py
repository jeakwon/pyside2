# https://jeakwon.github.io/pyside2/pyside2-dialogs/

import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, 
QPushButton, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("Push")
        btn.clicked.connect(self.with_parent)
        self.setCentralWidget(btn)
    
    def with_parent(self):
        dialog = QMessageBox(self)
        dialog.deleteLater()
        dialog.exec_()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
print('\n'.join(repr(w) for w in app.allWidgets()))
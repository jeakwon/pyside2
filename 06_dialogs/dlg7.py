# https://jeakwon.github.io/pyside2/pyside2-dialogs/

import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, 
QPushButton, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("Push")
        btn.clicked.connect(self.with_parent)
        # btn.clicked.connect(self.without_parent)
        self.setCentralWidget(btn)
    
    # memory leak but safe modality
    def with_parent(self):
        dialog = QMessageBox(self) 
        dialog.exec_()
    
    # No memory leak but unsafe modality
    def without_parent(self):
        dialog = QMessageBox() 
        dialog.exec_()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
print('\n'.join(repr(w) for w in app.allWidgets()))
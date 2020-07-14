# https://jeakwon.github.io/pyside2/pyside2-dialogs/

import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, 
QPushButton, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("Push")
        btn.clicked.connect(self.on_click)
        self.setCentralWidget(btn)
    
    # No memory leak, proper modal on premade QMessagebox
    def on_click(self):
        QMessageBox.question(self, "title", "question")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()
    print('\n'.join(repr(w) for w in app.allWidgets()))
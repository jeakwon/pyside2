# https://jeakwon.github.io/pyside2/pyside2-dialogs/

import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, 
QPushButton, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("Dialog")
        btn.clicked.connect(self.on_click)
        self.setCentralWidget(btn)
    
    def on_click(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Question")
        dialog.setText("Do you have any question?")
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.setIcon(QMessageBox.Question)
        ret = dialog.exec_()
        print("ret:", ret)
        if ret == QMessageBox.Yes:
            print("Yes")
        elif ret == QMessageBox.No:
            print("No")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
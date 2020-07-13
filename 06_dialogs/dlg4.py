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
        button = dialog.exec_()
        if button == QMessageBox.Yes:
            print("Yes", button)
        elif button == QMessageBox.No:
            print("No", button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
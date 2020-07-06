import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton("Push")
        self.btn.released.connect(self.btn_released)
        self.btn.setCheckable(True)
        self.setCentralWidget(self.btn)

    def btn_released(self):
        print(self.btn.isChecked())
        

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
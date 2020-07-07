import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Push")
        btn.released.connect(self.btn_released) # changed from sns4.py
        btn.released.connect(self.btn_toggled) # changed from sns4.py
        btn.setCheckable(True)
        self.setCentralWidget(btn)

    def btn_released(self): # changed from sns4.py
        print("Released") # changed from sns4.py

    def btn_toggled(self, checked):  # should invoke TypeError
        self.btn_checked = checked
        print(self.btn_checked)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
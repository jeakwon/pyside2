# https://jeakwon.github.io/pyside2/pyside2-widgets/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        checkbox = QCheckBox("체크박스")
        checkbox.stateChanged.connect(self.state_changed)

        self.setCentralWidget(checkbox)
        
    def state_changed(self, state):
        print(state, state == Qt.Checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

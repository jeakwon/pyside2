# https://jeakwon.github.io/pyside2/pyside2-widgets/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QCheckBox
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        checkbox = QCheckBox("3옵션 체크박스")
        checkbox.stateChanged.connect(self.state_changed)
        checkbox.setTristate(True)
        checkbox.setCheckState(Qt.PartiallyChecked)

        self.setCentralWidget(checkbox)
        
    def state_changed(self, state):
        if state == Qt.Checked:
            print(state, "Checked")
        elif state == Qt.Unchecked:
            print(state, "Unchecked")
        elif state == Qt.PartiallyChecked:
            print(state, "PartiallyChecked")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

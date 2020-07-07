# https://jeakwon.github.io/pyside2/pyside2-create-app/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
win = QMainWindow()
win.show()
sys.exit(app.exec_())
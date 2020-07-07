import sys
from PySide2.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
win = QMainWindow()
win.show()
sys.exit(app.exec_())
import sys
from PySide2.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
win = QWidget()
win.show()
sys.exit(app.exec_())
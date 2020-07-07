# https://jeakwon.github.io/pyside2/pyside2-create-app/

import sys
from PySide2.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
win = QWidget()
win.show()
sys.exit(app.exec_())
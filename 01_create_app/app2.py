# https://jeakwon.github.io/pyside2/pyside2-create-app/

import sys
from PySide2.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)
win = QPushButton("클릭")
win.show()
sys.exit(app.exec_())
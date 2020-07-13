# https://jeakwon.github.io/pyside2/pyside2-dialogs/

import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, 
QPushButton, QMessageBox, QVBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for type_ in ['about','critical','information','question','warning']:
            btn = QPushButton(type_)
            btn.pressed.connect(
                lambda x=type_: getattr(QMessageBox, x)(self, x, x+"_message"))
            layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
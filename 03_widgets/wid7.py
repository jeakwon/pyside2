# https://jeakwon.github.io/pyside2/pyside2-widgets/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QLineEdit()

        widget.setPlaceholderText("place_holder_text")
        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)
        
        self.setCentralWidget(widget)

    def return_pressed(self):
        self.centralWidget().setText("return_pressed")
        print("[return_pressed]")

    def selection_changed(self):
        data = self.centralWidget().selectedText()
        print("[selection_changed]", data)
        
    def text_changed(self, data):
        print("[text_changed]", data)

    def text_edited(self, data):
        print("[text_edited]", data)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
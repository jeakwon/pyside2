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
        self.centralWidget().setText("BOOM!")
        print("[return_pressed]")

    def selection_changed(self):
        s = self.centralWidget().selectedText()
        print("[selection_changed]", s)
        
    def text_changed(self, s):
        print("[text_changed]", s)

    def text_edited(self, s):
        print("[text_edited]", s)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
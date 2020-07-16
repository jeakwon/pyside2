import sys
from PySide2.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QWidget,
)

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)
    
    def show_new_window(self, checked):
        w = AnotherWindow()
        w.show()
        # self.w = AnotherWindow()
        # self.w.show()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
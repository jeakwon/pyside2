import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("마우스를 가지고 놀아보세요")
        self.setCentralWidget(self.label)

        # Mouse tracking method requires all widget enabled
        # self.setMouseTracking(True) 
        # self.label.setMouseTracking(True) 

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")
    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")
    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("마우스를 가지고 놀아보세요")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mousePressEvent LEFT")
        elif e.button() == Qt.MiddleButton:
            self.label.setText("mousePressEvent MIDDLE")
        elif e.button() == Qt.RightButton:
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")
        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")
        elif e.button() == Qt.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")
        elif e.button() == Qt.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")
        elif e.button() == Qt.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
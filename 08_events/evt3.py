import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QMenu, QAction
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec_(e.globalPos())


app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
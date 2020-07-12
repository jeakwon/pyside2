import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QToolBar, QAction, QStatusBar
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        toolbar = QToolBar("툴바")
        self.addToolBar(toolbar)
        
        action_text = QAction("텍스트", self)
        toolbar.addAction(action_text)
        
        action_icon = QAction(QIcon("icon.png"), "아이콘", self)
        toolbar.addAction(action_icon)
        toolbar.setIconSize(QSize(16, 16))

        statusbar = QStatusBar(self)
        self.setStatusBar(statusbar)
        action_text.setStatusTip("액션_텍스트")
        action_icon.setStatusTip("액션_아이콘")

        action_icon.triggered.connect(self.on_click)
        action_icon.setCheckable(True)

    def on_click(self, s):
        print("클릭", s)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())




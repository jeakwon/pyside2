# https://jeakwon.github.io/pyside2/pyside2-toolbars-and-menus/

import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QStatusBar
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        
        menubar = self.menuBar()
        menu = menubar.addMenu("&Menu") # "&"" allows short cut access "alt+M"

        action_text = QAction("텍스트", self)
        menu.addAction(action_text)

        action_text.setCheckable(True)

        menu.addSeparator()
        submenu = menu.addMenu("submenu")

        action_icon = QAction(QIcon("icon.png"), "아이콘", self)
        submenu.addAction(action_icon)
        
        action_icon.triggered.connect(self.on_click)
        action_icon.setCheckable(True)
        
        self.setStatusBar(QStatusBar(self))
        action_text.setStatusTip("액션_텍스트")
        action_icon.setStatusTip("액션_아이콘")

    def on_click(self, s):
        print("클릭", s)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
# https://jeakwon.github.io/pyside2/pyside2-toolbars-and-menus/
# icon source: https://feathericons.com/

import sys
from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QToolBar, QAction, QStatusBar
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        
        file_icons = {
            "file" : "icons/file.svg",
            "folder" : "icons/folder.svg",
            "save" : "icons/save.svg",
            "search" : "icons/search.svg",
        }
        contact_icons = {
            "facebook" : "icons/facebook.svg",
            "instagram" : "icons/instagram.svg",
            "twitter" : "icons/twitter.svg",
            "mail" : "icons/mail.svg",
            "phone" : "icons/phone.svg",
        }

        file_actions    = [QAction(QIcon(src), label, self) for label, src in file_icons.items()]
        contact_actions = [QAction(QIcon(src), label, self) for label, src in contact_icons.items()]
        
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addActions(file_actions)

        contact_menu = menubar.addMenu("Contact")
        contact_menu.addActions(contact_actions)
        
        file_toolbar = QToolBar("File")
        file_toolbar.addActions(file_actions)
        self.addToolBar(file_toolbar)

        contact_toolbar = QToolBar("Contact")
        contact_toolbar.addActions(contact_actions)
        self.addToolBar(contact_toolbar)

        self.insertToolBarBreak(contact_toolbar)
        
        # self.addToolBar(Qt.RightToolBarArea, file_toolbar)
        # self.addToolBar(Qt.RightToolBarArea, contact_toolbar)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
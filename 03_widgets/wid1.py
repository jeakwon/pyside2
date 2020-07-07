# https://jeakwon.github.io/pyside2/pyside2-widgets/

import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        widgets = [
            # QAbstractScrollArea,
            # QAbstractSlider,
            # QAbstractSpinBox,
            # QCalendarWidget,
            QCheckBox,
            # QColorDialog,
            # QColumnView,
            QComboBox,
            # QCommandLinkButton,
            QDateEdit,
            QDateTimeEdit,
            # QDesktopWidget,
            QDial,
            # QDialog,
            # QDialogButtonBox,
            # QDockWidget,
            QDoubleSpinBox,
            # QErrorMessage,
            # QFileDialog,
            # QFocusFrame,
            QFontComboBox,
            # QFontDialog,
            # QFrame,
            # QGraphicsView,
            # QGroupBox,
            # QInputDialog,
            # QKeySequenceEdit,
            QLCDNumber,
            QLabel,
            QLineEdit,
            # QListView,
            # QListWidget,
            # QMainWindow,
            # QMdiArea,
            # QMdiSubWindow,
            # QMenu,
            # QMenuBar,
            # QMessageBox,
            # QOpenGLWidget,
            # QPlainTextEdit,
            QProgressBar,
            # QProgressDialog,
            QPushButton,
            QRadioButton,
            # QScrollArea,
            # QScrollBar,
            QSlider,
            QSpinBox,
            # QSplashScreen,
            # QSplitter,
            # QStackedWidget,
            # QStatusBar,
            # QTabBar,
            # QTabWidget,
            # QTableView,
            # QTableWidget,
            # QTextBrowser,
            # QTextEdit,
            QTimeEdit,
            # QToolBar,
            # QToolBox,
            # QToolButton,
            # QTreeView,
            # QTreeWidget,
            # QUndoView,
            # QWidget,
            # QWizard,
            # QWizardPage,
        ]

        for w in widgets:
            layout.addWidget(w())
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()

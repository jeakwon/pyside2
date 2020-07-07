---
date: 2020-07-08 01:00:00 -0000
categories: pyside2
tags:
  - python
  - gui
  - qt
toc: true
header:
  overlay_color: "#333"
---
PySide2의 위젯에 대하여 알아보자
[소스코드](https://github.com/jeakwon/pyside2/tree/master/3_widgets){: .btn .btn--primary}

# Widgets
[전편](https://jeakwon.github.io/pyside2/pyside2-signal-and-slot/)에서는 시그널&슬롯의 개념에 대하여 
`QPushButton`위젯을 통해서 알아보았다. Qt에는 `QPushButton`이외에도 다양한 위젯들이 존재한다. 위젯이란
**창 안에 존재하는 사용자가 상호작용할 수 있는 UI 컴포넌트**이다. Qt에서는 많은 종류의 위젯이 존재하고
사용자가 새롭게 만들 수도 있다.

## 1. 위젯의 종류
### 소스코드
**wid1.py**
```python
import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        widgets = [
            QCalendarWidget,
            QCheckBox,
            QColorDialog,
            QComboBox,
            QCommandLinkButton,
            QDateEdit,
            QDateTimeEdit,
            QDial,
            QDoubleSpinBox,
            QFileDialog,
            QFontComboBox,
            QFontDialog,
            QLCDNumber,
            QLabel,
            QLineEdit,
            QProgressBar,
            QPushButton,
            QRadioButton,
            QSlider,
            QSpinBox,
            QTimeEdit,
            QToolButton,
            # QAbstractScrollArea,
            # QAbstractSlider,
            # QAbstractSpinBox,
            # QColumnView,
            # QDesktopWidget,
            # QDialog,
            # QDialogButtonBox,
            # QDockWidget,
            # QErrorMessage,
            # QFocusFrame,
            # QFrame,
            # QGraphicsView,
            # QGroupBox,
            # QInputDialog,
            # QKeySequenceEdit,
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
            # QProgressDialog,
            # QScrollArea,
            # QScrollBar,
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
            # QToolBar,
            # QToolBox,
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
        
        scroll = QScrollArea()
        scroll.setWidget(widget)

        self.setCentralWidget(scroll)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
```

### 결과
![](https://github.com/jeakwon/pyside2/blob/master/03_widgets/wid1.png){: .align-center}

### 설명
```python
```

# 참고
* This post was written based on Martin Fitzpatrick's Create GUI Applications with QT & Python - PySide2 [Official Link](www.learnpyqt.com){: .btn .btn--inverse}

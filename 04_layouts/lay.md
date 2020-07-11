---
date: 2020-07-10 01:36:00 -0000
categories: pyside2
tags:
  - python
  - gui
  - qt
toc: true
header:
  overlay_color: "#333"
---
PySide2의 레이아웃에 대하여 알아보자
[소스코드](https://github.com/jeakwon/pyside2/tree/master/04_layouts){: .btn .btn--primary}

# 1. 레이아웃이란
**Layout 종류**  

@ `QHBoxLayout`: 일자형 가로 박스 레이아웃  
@ `QVBoxLayout`: 일자형 세로 박스 레이아웃  
@ `QGridLayout`: (x, y) 그리드 인덱스를 이용한 레이아웃  
@ `QStackedLayout`: z축으로 여러개가 겹쳐질 수 있는 레이아웃  
@ `QTabWidget`: 
.{: .notice--info}

# 2. QVBoxLayout 
vertically arranged widgets
**lay1.py**
```python
from PySide2.QtGui import QColor, QPalette
from PySide2.QtWidgets import QWidget

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```


# 3. QHBoxLayout 
horizontally arranged widgets
**lay2.py**
```python
from PySide2.QtGui import QColor, QPalette
from PySide2.QtWidgets import QWidget

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```

# 4. Nesting layouts
**lay3.py**
```python
from PySide2.QtGui import QColor, QPalette
from PySide2.QtWidgets import QWidget

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        l1 = QVBoxLayout()
        l1.addWidget(Color("red"))
        l1.addWidget(Color("green"))
        l1.addWidget(Color("blue"))
        l1.addWidget(Color("yellow"))

        l2 = QVBoxLayout()
        l2.addWidget(Color("black"))
        l2.addWidget(Color("white"))

        l3 = QVBoxLayout()
        l3.addWidget(Color("grey"))

        layout = QHBoxLayout()
        layout.addLayout(l1)
        layout.addLayout(l2)
        layout.addLayout(l3)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```


# 5. QGridLayout
widgets arranged in a grid

# 6. QStackedLayout
multiple widgets in the same space

# 7. QTabWidget
multiple widgets in the same space


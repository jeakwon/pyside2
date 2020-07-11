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

# 레이아웃이란?
**Layout 종류**  
@ `QHBoxLayout`: 일자형 가로 박스 레이아웃  
@ `QVBoxLayout`: 일자형 세로 박스 레이아웃  
@ `QGridLayout`: (x, y) 그리드 인덱스를 이용한 레이아웃  
@ `QStackedLayout`: z축으로 여러개가 겹쳐질 수 있는 레이아웃  
@ `QTabWidget`: 레이아웃은 아니지만 `QStackedLayout`처럼 중첩이 가능한 위젯.
.{: .notice--info}

# 1. QVBoxLayout 
vertically arranged widgets
## 소스코드
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
## 결과
![](https://raw.githubusercontent.com/jeakwon/pyside2/master/04_layouts/lay1.png){: .align-center}

# 2. QHBoxLayout 
horizontally arranged widgets
## 소스코드
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
## 결과
![](https://raw.githubusercontent.com/jeakwon/pyside2/master/04_layouts/lay2.png){: .align-center}

# 3. 레이아웃 중첩
## 소스코드
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

        layout = QHBoxLayout()

        l1 = QVBoxLayout()
        l1.addWidget(Color("red"))
        l1.addWidget(Color("green"))
        l1.addWidget(Color("blue"))
        l1.addWidget(Color("yellow"))
        layout.addLayout(l1)

        l2 = QVBoxLayout()
        l2.addWidget(Color("black"))
        l2.addWidget(Color("white"))
        layout.addLayout(l2)

        l3 = QVBoxLayout()
        l3.addWidget(Color("grey"))
        layout.addLayout(l3)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```
## 결과
![](https://raw.githubusercontent.com/jeakwon/pyside2/master/04_layouts/lay3.gif){: .align-center}


# 4. QGridLayout
widgets arranged in a grid
## 소스코드
**lay4.py**
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
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        layout = QGridLayout()
        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("blue"), 0, 1)
        layout.addWidget(Color("yellow"), 1, 1)
        layout.addWidget(Color("black"), 2, 2)
        layout.addWidget(Color("white"), 100, 0)
        layout.addWidget(Color("grey"), 100, 100)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
```
## 결과
![](https://raw.githubusercontent.com/jeakwon/pyside2/master/04_layouts/lay4.gif){: .align-center}

# 5. QStackedLayout - 
multiple widgets in the same space
## 소스코드
**lay5.py**
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
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        layout = QStackedLayout()
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))

        layout.setCurrentIndex(0)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
```
## 결과
![](https://raw.githubusercontent.com/jeakwon/pyside2/master/04_layouts/lay5.gif){: .align-center}

# 6. QStackedLayout - 응용
multiple widgets in the same space
## 소스코드
**lay6.py**
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
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStackedLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        layout = QVBoxLayout()
        layout_top = QHBoxLayout()
        layout_bot = QStackedLayout()

        layout.addLayout(layout_top)
        layout.addLayout(layout_bot)

        for i, label in enumerate(["red", "green", "blue", "yellow"]):
            button = QPushButton(label)
            widget = Color(label)

            # def func(x=i):
            #     return layout_bot.setCurrentIndex(x)
            # button.pressed.connect(func)

            button.pressed.connect(lambda x=i: layout_bot.setCurrentIndex(x))

            layout_top.addWidget(button)
            layout_bot.addWidget(widget)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
```
## 결과
![](https://raw.githubusercontent.com/jeakwon/pyside2/master/04_layouts/lay6.gif){: .align-center}

# 7. QTabWidget
## 소스코드
**lay7.py**
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
from PySide2.QtWidgets import QApplication, QMainWindow, QTabWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QTabWidget()
        widget.setTabPosition(QTabWidget.North)
        
        for label in ["red", "green", "blue", "yellow"]:
            widget.addTab(Color(label), label)
            
        widget.setMovable(True)
        widget.setTabsClosable(True)
        widget.tabCloseRequested.connect(widget.removeTab)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
```
## 결과
![](https://raw.githubusercontent.com/jeakwon/pyside2/master/04_layouts/lay7.gif){: .align-center}

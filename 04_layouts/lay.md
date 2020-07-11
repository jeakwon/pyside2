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
[전편](https://jeakwon.github.io/pyside2/pyside2-widgets/)에서는 위젯의 종류를 알아보았다.
레이아웃은 여러개의 위젯을 하나의 창에 담고 어디에 위치할지를 조율해주는 역할을 한다. Qt에서는
총 네가지 종류의 레이아웃이 존재한다. 가로(x축), 세로(y축), 바둑판식(x&y축) 그리고 중첩식(z축) 
레이아웃. 레이아웃은 아니지만 여러 위젯을 담는데 유용한 탭 위젯도 같이 알아보자.

**Layout 종류**  
@ `QVBoxLayout`: 일자형 세로 박스 레이아웃  
@ `QHBoxLayout`: 일자형 가로 박스 레이아웃  
@ `QGridLayout`: (x, y) 그리드 인덱스를 이용한 레이아웃  
@ `QStackedLayout`: z축으로 여러개가 겹쳐질 수 있는 레이아웃  
@ `QTabWidget`: 조작이 쉬운 `QStackedLayout`처럼 중첩이 가능한 내장 위젯.
.{: .notice--info}

# 1. QVBoxLayout 
`QVBoxLayout`을 이용하면 세로로 위젯을 추가할 수 있다. 위에서 아래로 추가되는 형식이다. 
플레이스홀더로 색깔 위젯을 이용하여 레이아웃의 형태를 알아보자.

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

## 설명
### 1. 플레이스홀더 위젯
여기서 플레이스홀더 위젯은 기능은 없지만 단순히 그 위치를 잡을 목적으로 생성한(색깔만 입힌) 위젯을 지칭한다.
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
```
먼저 `class Color(QWidget):`로 `QWidget`을 상속받아 새로운 커스텀 위젯을 만든다. 그리고 새로운 위젯의 색깔을 
지정해 주기 위해 `def __init__(self, color):`로 `color`인수를 전달한다. `self.setAutoFillBackground(True)`
로 배경색깔을 채울 수 있게 한다. 다음은 색깔을 지정해 줘야 하는데, 색을 지정하려면 위젯의 `palette`에 접근하여
`palette.setColor(QPalette.Window, QColor(color))`로 색을 `palette`에 전달하고, `self.setPalette(palette)`
로 `palette`를 지정해준다. 그러면 `Color(color)`형태로 인수를 전달하여 레아이웃에 사용 할 위젯을 생성한다.

### 2. 레이아웃에 위젯 추가하기
```python
        layout = QVBoxLayout()
        layout.addWidget(Color("red"))
```
`layout = QVBoxLayout()`로 레이아웃을 등록한다. `.addWidget`으로 위젯을 추가한다.

### 3. 메인윈도우에 레이아웃 등록
```python
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
```
레이아웃을 메인윈도우에 등록하기 위해 `QWidget`을 이용하여 레이아웃을 등록한 뒤 그 위젯을 `.setCentralWidget`을 
해준다. 어떤 위젯을 구성하더라도 2번의 메인 `layout` 구성만 바꾸어 메인윈도우에 등록하면 된다.

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

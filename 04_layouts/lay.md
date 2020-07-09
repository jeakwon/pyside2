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
.{: .notice--info}

# 2. QVBoxLayout 
vertically arranged widgets
```python
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QPushButton("A"))
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

# 4. Nesting layouts

# 5. QGridLayout 
widgets arranged in a grid

# 6. QStackedLayout 
multiple widgets in the same space


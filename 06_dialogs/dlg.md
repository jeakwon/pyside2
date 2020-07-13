---
date: 2020-07-14 01:00:00 -0000
categories: pyside2
tags:
  - python
  - gui
  - qt
toc: true
header:
  overlay_color: "#333"
---
PySide2의 다이얼로그 (대화상자)에 대해서 알아보자
[소스코드](https://github.com/jeakwon/pyside2/tree/master/06_dialogs){: .btn .btn--primary}

# 대화상자(Dialog)란?
대화상자는 유용한 GUI요소로써 어플리케이션이 유저와 커뮤니케이션하는 수단이다.
파일 열기, 저장, 설정 등과 같은 기능에 일반적으로 사용된다. 작은 [모달][1] 윈도우 형태로
사용자에게 프로그램 구동에 원하는 커뮤니케이션을 유도하는데 이용된다. Qt는 널리 사용되는 범용성 대화상자를 많이 제공하고, 좀더 사용자 친화적인 플랫폼 맞춤형태로 제공된다.

[1]: (Modal) 사용자 입력을 독점하는, 자식 윈도에서 부모 윈도로 돌아가기 전에 사용자의 상호동작을 요구하는 창.

# 1. QDialog - 기본구성
## 소스코드
**dlg1.py**
```python
import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, 
QPushButton, QDialog, QLabel, QVBoxLayout, QDialogButtonBox)
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("Dialog")
        btn.clicked.connect(self.on_click)
        self.setCentralWidget(btn)
    
    def on_click(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dialog")
        
        layout = QVBoxLayout()
        dialog.setLayout(layout)

        label = QLabel("Message")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        btns = QDialogButtonBox.Ok|QDialogButtonBox.Cancel
        btnbox = QDialogButtonBox(btns)
        layout.addWidget(btnbox)

        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
```

## 결과
![](https://raw.githubusercontent.com/jeakwon/pyside2/master/06_dialogs/dlg1.gif){: .align-center}

## 설명
- 먼저 `QDialog` Widget을 생성하면 깡통 대화상자가 등장한다. 이 때 메인윈도우를 등지고 있는데, 대화상자가 생성되면 부모 위젯과는 소통이 불가능해지는 모달 상태가 된다. 메인윈도우에 타이틀을 붙여준 것 처럼 `setWindowTitle`을 통해 타이틀을 부여해 줄 수 있다.
- QApplication처럼 `.exec_()`를 사용하여 새로운 이벤트루프로 진입하고 창을 띄운다.
- 대화상자역시 여러개의 위젯을 담으려면 `.setLayout`으로 layout을 등록하고, 추가하고 싶은 위젯을 (여기선 `QLabel`, `QDialogButtonBox`) 담아주면 된다.
- `QDialogButtonBox`에 담을 수 있는 버튼의 종류는 여러가지가 이미 만들어져 있다.파이프(`|`)로 구분해주면 원하는 버튼을 여러개 담을 수 있다.
- `QDialogButtonBox.Ok`와 `QDialogButtonBox.Cancel`를 박스에 추가해 주어, Ok버튼과 Cancel버튼을 추가하였으나 아직은 사용자와의 커뮤니케이션이 불가능한 상태.(다음으로)

**Buttons for QDialogButtonBox**  
아래는 사용가능한 버튼의 종류와 버튼이 정의하는 역할  
@ `QDialogButtonBox.Ok` AcceptRole
@ `QDialogButtonBox.Open` AcceptRole
@ `QDialogButtonBox.Save` AcceptRole
@ `QDialogButtonBox.Cancel` RejectRole
@ `QDialogButtonBox.Close` RejectRole
@ `QDialogButtonBox.Discard` DestructiveRole
@ `QDialogButtonBox.Apply` ApplyRole
@ `QDialogButtonBox.Reset` ResetRole
@ `QDialogButtonBox.RestoreDefaults` ResetRole
@ `QDialogButtonBox.Help` HelpRole
@ `QDialogButtonBox.SaveAll` AcceptRole
@ `QDialogButtonBox.Yes` YesRole
@ `QDialogButtonBox.YesToAll` YesRole
@ `QDialogButtonBox.No` NoRole
@ `QDialogButtonBox.NoToAll` NoRole
@ `QDialogButtonBox.Abort` RejectRole
@ `QDialogButtonBox.Retry` AcceptRole
@ `QDialogButtonBox.Ignore` AcceptRole
@ `QDialogButtonBox.NoButton` Invalid Button
{: .notice--info}

# 2. QDialog - 커스터마이징
`QDialog`의 서브클래스로 `Dialog`라는 커스텀 대화상자를 만들어 본다.
## 소스코드
**dlg2.py**
```python
import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, 
QPushButton, QDialog, QLabel, QVBoxLayout, QDialogButtonBox)
from PySide2.QtCore import Qt

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog")
        
        layout = QVBoxLayout()

        label = QLabel("Message")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        btns = QDialogButtonBox.Ok|QDialogButtonBox.Cancel
        btnbox = QDialogButtonBox(btns)
        layout.addWidget(btnbox)
        
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("Dialog")
        btn.clicked.connect(self.on_click)
        self.setCentralWidget(btn)
    
    def on_click(self):
        dialog = Dialog()
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
```

## 결과
![](https://raw.githubusercontent.com/jeakwon/pyside2/master/06_dialogs/dlg2.gif){: .align-center}

## 설명
- 최종적으로 모습은 **dlg1.py**와 똑같지만 `QDialog`를 상속받은 독립적인 `Dialog`서브클래스를 생성하여 반복적인 사용이 가능한 형태가 되었다.
- `QLabel`위젯을 만들어서 `Qt.AlignCenter`를 통해 텍스트를 중앙에 위치 시키고, 레이아웃에 추가해준다.

# 3. QDialog - 시그널 & 슬롯
## 소스코드
**dlg3.py**
```python
import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, 
QPushButton, QDialog, QLabel, QVBoxLayout, QDialogButtonBox)
from PySide2.QtCore import Qt

class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog")
        
        layout = QVBoxLayout()

        label = QLabel("Message")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
        btns = QDialogButtonBox.Ok|QDialogButtonBox.Cancel
        btnbox = QDialogButtonBox(btns)
        btnbox.accepted.connect(self.accept)
        btnbox.rejected.connect(self.reject)
        layout.addWidget(btnbox)
        
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("Dialog")
        btn.clicked.connect(self.on_click)
        self.setCentralWidget(btn)
    
    def on_click(self):
        dialog = Dialog()
        print("Ok" if dialog.exec_() else "Cancel")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
```

## 결과
![](https://raw.githubusercontent.com/jeakwon/pyside2/master/06_dialogs/dlg3.gif){: .align-center}

## 설명
- **dlg1.py**와 **dlg2.py**에서는 사용자가 대화상자의 버튼을 눌러도 아무 일도 일어 나지 않았다. 


# 4. QMessageBox - 구성하기
## 소스코드
**dlg4.py**
```python
import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, 
QPushButton, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("Dialog")
        btn.clicked.connect(self.on_click)
        self.setCentralWidget(btn)
    
    def on_click(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Question")
        dialog.setText("Do you have any question?")
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        dialog.setIcon(QMessageBox.Question)
        ret = dialog.exec_()
        print("ret:", ret)
        if ret == QMessageBox.Yes:
            print("Yes")
        elif ret == QMessageBox.No:
            print("No")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
```

## 결과
![](https://raw.githubusercontent.com/jeakwon/pyside2/master/06_dialogs/dlg4.gif){: .align-center}

## 설명

# 5. QMessageBox - 내장위젯
## 소스코드
**dlg5.py**
```python
import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, 
QPushButton, QMessageBox)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        btn = QPushButton("Dialog")
        btn.clicked.connect(self.on_click)
        self.setCentralWidget(btn)
    
    def on_click(self):
        ret = QMessageBox.question(
            self, "Question", "Do you have any question?")
        print(ret)
        if ret == QMessageBox.Yes:
            print("Yes")
        elif ret == QMessageBox.No:
            print("No")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
```

## 결과
![](https://raw.githubusercontent.com/jeakwon/pyside2/master/06_dialogs/dlg5.gif){: .align-center}

## 설명

# 6. QMessageBox - 여러가지타입들
**Premade QMessageBox**  
@ 기본: `QMessageBox.about(parent, title, text)`: (아이콘: 없음)  
@ 오류: `QMessageBox.critical(parent, title, text)`: (아이콘: X)  
@ 정보: `QMessageBox.information(parent, title, text)`: (아이콘: i)  
@ 질의: `QMessageBox.question(parent, title, text)`: (아이콘: ?)  
@ 경고: `QMessageBox.warning(parent, title, text)`: (아이콘: !)  
{: .notice--primary}

## 소스코드
**dlg6.py**
```python
import sys
from PySide2.QtWidgets import (QApplication, QMainWindow, 
QPushButton, QMessageBox, QVBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        for type_ in ['about','critical','information','question','warning']:
            btn = QPushButton(type_)
            btn.pressed.connect(
                lambda x=type_: getattr(QMessageBox, x)(self, x, x+"_message"))
            layout.addWidget(btn)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
```

## 결과
![](https://raw.githubusercontent.com/jeakwon/pyside2/master/06_dialogs/dlg6.gif){: .align-center}

## 설명
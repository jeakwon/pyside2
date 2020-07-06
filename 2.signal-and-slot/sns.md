# Singal and Slot - QPushButton
## 1. 시그널 함수 연결
### 소스코드
**sns1.py**
```python
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Push")
        btn.clicked.connect(self.btn_clicked)

        self.setCentralWidget(btn)

    def btn_clicked(self):
        print("Clicked")

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
```

### 결과 (클릭 세번)
```
Clicked
Clicked
Clicked
```

### 설명
```python
class MainWindow(QMainWindow):
    def __init__(self):
        #...
        btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        print("Clicked")
```
`btn.clicked`는 시그널이고 `btn_clicked` 우리가 정의 해준 슬롯이다. 이를 `.connect` 메소드를 통해 시그널과 슬롯을 연결하여
생성해준 `QPushButton`이 클릭 시그널을 발생할 때 마다 우리가 만들어준 슬롯이 작동하게 된다.


## 2. 데이터 수신
### 소스코드
**sns2.py**
```python
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Push")
        btn.clicked.connect(self.btn_clicked)

        self.setCentralWidget(btn)

    def btn_clicked(self, checked): # changed from sns1.py
        print("Clicked", checked) # changed from sns1.py

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
```

### 결과 (클릭 세번)
```
Clicked False
Clicked False
Clicked False
```

### 설명
```python
class MainWindow(QMainWindow):
    #...

    def btn_clicked(self, checked): # changed from sns1.py
        print("Clicked", checked) # changed from sns1.py
```
`btn_clicked(self, checked)`는 시그널이 전송한 데이터가 접근할 argument로 `checked`를 추가해 준 것이다. 꼭 `checked`로 할 필요는 없다.  

결과를 보면, 수신된 데이터 `checked`가 `False`상태인데, 위젯과의 상호작용을 통해 위젯의`checked` status가 변하게 할 수 있다. 이것을 데이터 저장이라고 표현해 보겠다.

## 3. 위젯의 상태 변환
### 소스코드
**sns3.py**
```python
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Push")
        btn.clicked.connect(self.btn_clicked)
        btn.setCheckable(True) # added from sns2.py
        self.setCentralWidget(btn)

    def btn_clicked(self, checked):
        print("Clicked", checked)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
```

### 결과 (클릭 세번)
```
Clicked True
Clicked False
Clicked True
```

### 설명
```python
class MainWindow(QMainWindow):
    def __init__(self):
        #...
        btn.setCheckable(True) # added from sns2.py
```

`.setCheckable(True)`는 `btn`의 `checked` 상태를 변화시킬 수 있게 해준다. 디폴트값으로 False로 되어있다. 

## 4. 데이터 저장
### 소스코드
**sns4.py**
```python
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Push")
        btn.clicked.connect(self.btn_clicked)
        btn.clicked.connect(self.btn_toggled) # added from sns1.py
        btn.setCheckable(True) # added from sns1.py
        self.setCentralWidget(btn)

    def btn_clicked(self):
        print("Clicked")

    def btn_toggled(self, checked): # added from sns1.py
        self.btn_checked = checked # added from sns1.py
        print(self.btn_checked)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
```

### 결과 (클릭 세번)
```
Clicked
True
Clicked
False
Clicked
True
```

### 설명
```python
class MainWindow(QMainWindow):
        #...
    def btn_toggled(self, checked): # added from sns1.py
        self.btn_checked = checked # added from sns1.py
```

`self.btn_checked = checked`를 통해서 MainWindow 객체에 수신된 데이터를 저장할 수 있다. 이를 통해서 사용자가 원하는 방식으로 
수신된 데이터를 후처리 할 수도 있다.

## 5. 버튼 릴리즈는 데이터 수신이 불가
### 소스코드
**sns5.py**
```python
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Push")
        btn.released.connect(self.btn_released) # changed from sns4.py
        btn.released.connect(self.btn_toggled) # changed from sns4.py
        btn.setCheckable(True)
        self.setCentralWidget(btn)

    def btn_released(self): # changed from sns4.py
        print("Released") # changed from sns4.py

    def btn_toggled(self, checked):  # should invoke TypeError
        self.btn_checked = checked
        print(self.btn_checked)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
```

### 결과 (클릭 한번)
```
Released
TypeError: btn_toggled() missing 1 required positional argument: 'checked'
```

### 설명
```python
class MainWindow(QMainWindow):
    def __init__(self):
        # ...
        btn.released.connect(self.btn_released) # changed from sns4.py
        btn.released.connect(self.btn_toggled) # changed from sns4.py

    def btn_released(self): # changed from sns4.py
        print("Released") # changed from sns4.py

    def btn_toggled(self, checked):  # should invoke TypeError
        self.btn_checked = checked
        print(self.btn_checked)
```

`btn.released.connect`

## 6. 객체 싱태 접근을 통한 우회
### 소스코드
**sns6.py**
```python
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton("Push")
        self.btn.released.connect(self.btn_released)
        self.btn.setCheckable(True)
        self.setCentralWidget(self.btn)

    def btn_released(self):
        print(self.btn.isChecked())
        

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
```

### 결과 (클릭 세번)
```
True
False
True
```
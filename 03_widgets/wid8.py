# https://jeakwon.github.io/pyside2/pyside2-widgets/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QSpinBox() # QDoubleSpinBox()
        
        widget.setRange(-10,10)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(1) # 0.1
        widget.valueChanged.connect(self.value_changed)
        widget.valueChanged[str].connect(self.value_changed_str)
        
        self.setCentralWidget(widget)
    
    def value_changed(self, data):
        print("[value_changed]", data)
    
    def value_changed_str(self, data):
        print("[value_changed_str]", data)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()
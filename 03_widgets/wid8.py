# https://jeakwon.github.io/pyside2/pyside2-widgets/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QSpinBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QSpinBox()
        # widget = QDoubleSpinBox()
        
        widget.setMinimum(-10)
        widget.setMaximum(3)
        # widget.setRange(-10,3)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3) # 0.5 for QDoubleSpinBox
        widget.valueChanged.connect(self.value_changed)
        widget.valueChanged[str].connect(self.value_changed_str)
        
        self.setCentralWidget(widget)
    
    def value_changed(self, data):
        print(data)
    
    def value_changed_str(self, data):
        print(data)

app = QApplication(sys.argv)
win = MainWindow()
win.show()
app.exec_()

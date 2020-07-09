# https://jeakwon.github.io/pyside2/pyside2-widgets/

import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QDial

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        widget = QDial()
        widget.setRange(-10, 10)
        widget.setSingleStep(0.1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)
        
        self.setCentralWidget(widget)
        
    def value_changed(self, data):
        print("[value_changed]", data)

    def slider_position(self, data):
        print("[slider_position]", data)

    def slider_pressed(self):
        print("[slider_pressed]")

    def slider_released(self):
        print("[slider_released]")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
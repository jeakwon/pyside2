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
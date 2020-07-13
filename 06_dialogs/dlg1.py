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
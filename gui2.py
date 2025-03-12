from PyQt6 import QtWidgets as Qt

class MainWindow(Qt.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('BotoPalet')
        self.setGeometry(100, 100, 647, 573)
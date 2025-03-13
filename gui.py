from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer, QTime
from gui_designer import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Ładujemy interfejs z Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Ustawienie i uruchomienie timera
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        # Ustawienie początkowego czasu
        self.start_time = QTime(0, 0, 0)

        # Podłączanie przycisków do funkcji
        self.ui.start.clicked.connect(self.start_timer)
        self.ui.stop.clicked.connect(self.stop_timer)

    def start_timer(self):
        """ Uruchamia timer od momentu kliknięcia START """
        self.start_time = QTime(0, 0, 0)
        self.timer.start(1000)  # Odświeżanie co 1 sekundę

    def stop_timer(self):
        """ Zatrzymuje timer po kliknięciu STOP """
        self.timer.stop()

    def update_timer(self):
        """ Aktualizuje label_timer o upływający czas """
        self.start_time = self.start_time.addSecs(1)
        self.ui.label_timer.setText(self.start_time.toString("hh:mm:ss"))
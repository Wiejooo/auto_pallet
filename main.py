from gui import MainWindow
from PyQt6.QtWidgets import QApplication



if __name__ == "__main__":
    app = QApplication([]) # Główna pętla
    window = MainWindow() # Tworzy główne okno
    window.show() # Pokazuje główne okno
    app.exec() # Czeka na zdarzenie użytkownika
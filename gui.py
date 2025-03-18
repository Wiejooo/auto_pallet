import functions
import json
import os
from PyQt6 import QtWidgets
from PyQt6.QtCore import QTimer, QTime
from gui_designer import Ui_MainWindow
from tests import func_tests


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
        self.ui.start.clicked.connect(self.start_cyclicality)
        self.ui.start.clicked.connect(self.start_cleaning)
        self.ui.stop.clicked.connect(self.stop_cyclicality)

        # Zakupione palety
        self.scroll_layout = QtWidgets.QVBoxLayout()
        self.scroll_widget = QtWidgets.QWidget()
        self.scroll_widget.setLayout(self.scroll_layout)
        self.ui.scrollArea.setWidget(self.scroll_widget)
        self.label_pallets = QtWidgets.QLabel()
        self.label_pallets.setWordWrap(True)
        self.scroll_layout.addWidget(self.label_pallets)
        
        

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

    def show_newest_pallets(self):
        """Wyświetl najnowsze palety"""
        pallets = functions.find_newest_pallet()
        pallets_text = "\n".join(pallets)
        self.ui.newest_list.setText(pallets_text)

    def key_words(self):
        """Wpisane słowa w textarea"""
        words = self.ui.textEdit.toPlainText()
        words = words.split(' ')
        return words
    
    def buy_pallet(self):
        """Zakup palety i zwrócenie danych"""
        if self.key_words() != ['']:
            find = functions.check_offerts(self.key_words())
            
            # Formatowanie danych do stringa
            result_lines = []
            for pallet_name, data in find.items():
                title = f'{pallet_name} - {data["price"]} brutto'
                items_str = ", ".join(f"{item}: {quantity}" for item, quantity in data["items"].items())
                result_lines.append(f"{title}\n{items_str}")
            find_str = "\n\n".join(result_lines)
            self.label_pallets.setText(str(find))

            json_path = 'both_pallets.json'
            if result_lines != []:
                # Sprawdzenie, czy plik istnieje i czy nie jest pusty
                if os.path.exists(json_path) and os.stat(json_path).st_size > 0:
                    with open(json_path, 'r', encoding='utf-8') as file:
                        both_pallets = json.load(file)
                else:
                    both_pallets = {}
            
                # Dodanie nowego wpisu do JSON
                both_pallets[str(len(both_pallets) + 1)] = find_str
                # Zapis zaktualizowanych danych do pliku JSON
                with open(json_path, 'w', encoding='utf-8') as file:
                    json.dump(both_pallets, file, indent=4, ensure_ascii=False)
                # Tworzenie stringa do wyświetlenia
                to_show = "\n\n".join(both_pallets.values())
                # Aktualizacja labela w GUI
                self.label_pallets.setText(to_show)

    def buy_pallet_TEST(self):
        """Kupowanie palet i zwrócenie danych TEST"""
        find = func_tests.check_offerts_TEST(['zmywarka', 'Etui', 'foremka', 'Puszek', 'Monitor'])
        result_lines = []
        for pallet_name, data in find.items():
            title = f'{pallet_name} - {data["price"]} brutto'
            items_str = ", ".join(f"{item}: {quantity}" for item, quantity in data["items"].items())
            result_lines.append(f"{title}\n{items_str}")
        find_str = "\n\n".join(result_lines)
        json_path = 'both_pallets.json'
        if result_lines != []:
            # Sprawdzenie, czy plik istnieje i czy nie jest pusty
            if os.path.exists(json_path) and os.stat(json_path).st_size > 0:
                with open(json_path, 'r', encoding='utf-8') as file:
                    both_pallets = json.load(file)
            else:
                both_pallets = {}
            # Dodanie nowego wpisu do JSON
            both_pallets[str(len(both_pallets) + 1)] = find_str
            # Zapis zaktualizowanych danych do pliku JSON
            with open(json_path, 'w', encoding='utf-8') as file:
                json.dump(both_pallets, file, indent=4, ensure_ascii=False)
            # Tworzenie stringa do wyświetlenia
            to_show = "\n\n".join(both_pallets.values())
            # Aktualizacja labela w GUI
            self.label_pallets.setText(to_show)

    def start_cyclicality(self):
        """Cykliczność programu"""
        self.start_timer()
        self.key_words()
        self.timer_loop = QTimer(self)
        # self.timer_loop.timeout.connect(self.show_newest_pallets) # <- wyłączona funkcja najnowszych palet
        self.timer_loop.timeout.connect(self.buy_pallet)
        self.timer_loop.start(3500)

    def start_cleaning(self):
        # Wyczyszczenie both_pallets.json
        with open('both_pallets.json', 'w', encoding='utf-8') as file:
            json.dump({}, file, indent=4, ensure_ascii=False)
        # Wyczyszczenie okno Kupione palety
        self.label_pallets.setText('')

    def stop_cyclicality(self):
        """Zatrzymanie cykliczności"""
        if hasattr(self, 'timer_loop'):
            self.stop_timer()
            self.timer_loop.stop()

    

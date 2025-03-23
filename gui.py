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
        self.json_name = f'{functions.save_date()}-operation.json'

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
        self.ui.start.clicked.connect(self.make_json_file)
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
    
    def make_json_file(self):
        # Stworzenie nowego JSON'a
        data = {
            "creation_date": self.json_name,
            "data": {}
        }
        with open(f'operation_history/{self.json_name}', 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            file.flush()
    
    def buy_pallet(self):
        """Zakup palety i zwrócenie danych"""
        if self.key_words() != ['']:
            # Wypełnienie pliku json
            functions.fill_file(self.key_words(), self.json_name)

            # Kupienie palet
            # WIP

            # Zaznaczenie palety jako kupionej
            # WIP

            # Wyświetlenie zawartości pliku json
            json_path = os.path.join(os.path.dirname(__file__), "operation_history", self.json_name)
            with open(json_path, 'r', encoding='utf-8') as file:
                json_file = json.load(file)
            # Formatowanie danych do stringa
            result_lines = []
            for pallet_name, data in json_file['data'].items():
                title = f'{pallet_name} - {data["price"]} brutto'
                items_str = ", ".join(f"{item}: {quantity}" for item, quantity in data["items"].items())
                result_lines.append(f"{title}\n{items_str}")
            find_str = "\n\n".join(result_lines)
            # Aktualizacja labela w GUI
            self.label_pallets.setText(find_str)

    def buy_pallet_TEST(self):
        """Kupowanie palet TEST"""
        func_tests.check_offerts_TEST(['zmywarka', 'Etui', 'foremka', 'Puszek', 'Monitor'], self.json_name)

        with open(f'tests/operation_history_TEST/{self.json_name}', 'r', encoding='utf-8') as file:
            json_file = json.load(file)
        result_lines = []
        for key, data in json_file['data'].items():
            title = f'{key} - {data["price"]} brutto'
            items_str = ", ".join(f"{item}: {quantity}" for item, quantity in data["items"].items())
            result_lines.append(f"{title}\n{items_str}")
        find_str = "\n\n".join(result_lines)
        # Aktualizacja labela w GUI
        self.label_pallets.setText(find_str)
        

    def start_cyclicality(self):
        """Cykliczność programu"""
        self.start_timer()
        self.key_words()
        self.timer_loop = QTimer(self)
        # self.timer_loop.timeout.connect(self.show_newest_pallets)
        self.timer_loop.timeout.connect(self.buy_pallet)
        self.timer_loop.timeout.connect(self.summary)
        self.timer_loop.start(3500)

    def start_cleaning(self):
        # Wyczyszczenie okna Kupione palety
        self.label_pallets.setText('')
        # Wyczyszczenie okna Najnowsze palety
        self.ui.newest_list.setText('')

    def stop_cyclicality(self):
        """Zatrzymanie cykliczności"""
        if hasattr(self, 'timer_loop'):
            self.stop_timer()
            self.timer_loop.stop()

    def summary(self):
        # Wczytanie pliku
        with open(f'operation_history/{self.json_name}', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        summary_cost = 0
        summary_items = {}
        for key, palet in data["data"].items():
            summary_cost += palet['price']
            for item_key, quantity in palet['items'].items(): 
                if item_key in summary_items:
                     summary_items[item_key] += quantity
                else:
                     summary_items[item_key] = quantity
        
        summary_items_text = ''
        for key, value in summary_items.items():
             summary_items_text = summary_items_text + f'{key}: {value}\n\n'

        show = f'Wydano w sumie: {summary_cost} brutto\n\n{summary_items_text}'
        self.ui.summary_list.setText(show)

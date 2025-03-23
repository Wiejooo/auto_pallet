import json
import os
import datetime

"""Funkcje do sprawdzania programu przed startem"""

def save_date():
    """Zwraca datę do zapisu"""
    string_date = str(datetime.datetime.now())[:-10]
    string_date = string_date.replace(':', '-')
    string_date = string_date.replace(' ', '_')
    return string_date

def check_offerts_TEST(words, file_json):
    """Sprawdza oferty"""

    # Wczytanie pliku json
    with open(f'tests/operation_history_TEST/{file_json}', 'r', encoding='utf-8') as file:
        json_file = json.load(file)
    # Wyczyszczenie pliku json
    json_file['data'] = {}


    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_folder_path = os.path.join(base_dir, 'json_TEST')
    for pallet in os.listdir(full_folder_path):
        json_path = os.path.join(base_dir, 'json_TEST', pallet)
        with open(json_path, 'r', encoding='utf-8') as file:        
            products = json.load(file)['data']

        # Sprawdzenine słów w produktach
        word_set = set(word.lower() for word in words)
        find_words = {}
        for product in products:
            for word in word_set:
                if word in product['name'].lower():
                    find_words[word] = find_words.get(word, 0) + int(product['quantity'])

        productCode = str(pallet[:-5])
        # ID palet do kupienia
        if find_words != {}:
            json_file["data"][productCode] = {
                'price': '100',
                "items": find_words,
                "both": False
            }
    
    # Zapisanie danych
    with open(f'tests/operation_history_TEST/{file_json}', 'w', encoding='utf-8') as file:
        json.dump(json_file, file, indent=4, ensure_ascii=False)
        

# print(check_offerts_TEST(['zmywarka', 'Etui', 'foremka', 'Puszek', 'Monitor']))
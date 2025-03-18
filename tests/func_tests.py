import json
import os

"""Funkcje do sprawdzania programu przed startem"""

def check_offerts_TEST(words):
    """Sprawdza oferty"""
    pallets_to_buy = {}

    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_folder_path = os.path.join(base_dir, 'json')
    for pallet in os.listdir(full_folder_path):
        json_path = os.path.join(base_dir, 'json', pallet)
        with open(json_path, 'r', encoding='utf-8') as file:        
            products = json.load(file)['data']

        # Sprawdzenine słów w produktach
        word_set = set(word.lower() for word in words)
        find_words = {}
        for product in products:
            for word in word_set:
                if word in product['name'].lower():
                    find_words[word] = find_words.get(word, 0) + int(product['quantity'])

        # ID palet do kupienia
        if find_words != {}:
            pallets_to_buy[pallet[:-5]] = {
                'price': '123',
                "items": find_words,
            }
    return pallets_to_buy

# print(check_offerts_TEST(['zmywarka', 'Etui', 'foremka', 'Puszek', 'Monitor']))
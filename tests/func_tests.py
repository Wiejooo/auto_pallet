import json
import os

"""Funkcje do sprawdzania programu przed startem"""

def check_offerts_TEST(words):
    """Sprawdza oferty"""
    test_pallets = [
        {'id': '63228', 'code': 'F111', 'priceGross':'111'},
        {'id': '63230', 'code': 'F222', 'priceGross':'222'},
        {'id': '63237', 'code': 'F333', 'priceGross':'333'},
    ]
    pallets_to_buy = {}

    for pallet in test_pallets:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, 'json', f'{pallet["id"]}.json')
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
            pallets_to_buy[pallet['code']] = {
                'price': pallet['priceGross'],
                "items": find_words,
            }
    return pallets_to_buy

print(check_offerts_TEST(['zmywarka', 'Etui', 'foremka', 'Puszek']) )
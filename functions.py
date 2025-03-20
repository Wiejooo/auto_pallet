import requests
import json
import os
import time
import datetime

def save_date():
    """Zwraca datę do zapisu"""
    string_date = str(datetime.datetime.now())[:-10]
    string_date = string_date.replace(':', '-')
    string_date = string_date.replace(' ', '_')
    return string_date

def measure_time(func):
    """Odmierza czas funkcji"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Wczytanie danych logowania
login_json_path = os.path.join(os.path.dirname(__file__), "..", "login_miglo.json")
with open(login_json_path, 'r', encoding="utf-8") as file:
    json_login_data = json.load(file)

def find_token():
    """Oddaje token"""
    login_url = 'https://sa.miglo.pl/api/account/login'
    login_data = {
        'Email': json_login_data['login'],
        'Password': json_login_data['password']
    }
    response = requests.post(login_url, json=login_data)
    if response.status_code == 200:
        token = response.json().get('data').get('token')
        return token
    else:
        return "Błąd przy logowaniu"


product_id = 62530
def add_to_card():
    URL = 'https://sklepapi.miglo.pl/api/Cart/AddItem'
    request = {
        "OfferId": product_id,
        "Quantity": 1,
        "ComapnyId": None
    }
    token = find_token()
    headers = {
        "Content-Type":"application/json; charset=utf-8",
        "Accept":"*/*",
        "Authorization":f"Bearer {token}",
        }
    response = requests.post(URL, json=request, headers=headers)
    if response.status_code == 200:
        return f'Status dodania do koszyka: {response.text}'
    else:
        return 'Błąd przy dodawaniu do koszyka'
    

def find_newest_pallet():
    '''Znajduje najnowsze palety'''
    URL = 'https://sklepapi.miglo.pl/api/product/List'
    token = find_token()
    headers = {
        "Content-Type":"application/json; charset=utf-8",
        "Accept":"*/*",
        "Authorization":f"Bearer {token}",
        }
    request = {
        "CategoryId": None,
        "Category": None,
        "ItemsOnPage": 5,
        "Page": 1,
        "CustomerId": None,
        "OnlyPromotions": False,
        "SearchText": None,
        "RandomList": False,
        "ValueMin": None,
        "ValueMax": None,
        "WeightMin": None,
        "WeightMax": None,
        "AveragePriceMin": None,
        "AveragePriceMax": None,
        "QtyOnPalletMin": None,
        "QtyOnPalletMax": None
    }
    response = requests.post(URL, json=request, headers=headers)
    pallets = response.json()
    pallets = pallets['data']['products'][0:4]
    cut_data_pallets = []
    for pallet in pallets:
        cut_data_pallets.append(f'{pallet["productCode"]} - {pallet["priceGross"]} brutto\n')
    if response.status_code == 200:
        return cut_data_pallets
    else:
        return 'Błąd przy sprawdzaniu najnowszych palet'

# @measure_time
def make_operation(words):
    """Tworzy plik JSON do zakupów jednej operacji"""
    current_time = save_date()
    pallets_to_buy = {
        "creation_date" : current_time,
        "data": {}
    }
    URL = 'https://sklepapi.miglo.pl/api/product/List'
    token = find_token()
    headers = {
        "Content-Type":"application/json; charset=utf-8",
        "Accept":"*/*",
        "Authorization":f"Bearer {token}",
        "Accept-Language": "pl"
        }
    request = {
        "CategoryId": None,
        "Category": None,
        "ItemsOnPage": 5,
        "Page": 1,
        "CustomerId": None,
        "OnlyPromotions": False,
        "SearchText": None,
        "RandomList": False,
        "ValueMin": None,
        "ValueMax": None,
        "WeightMin": None,
        "WeightMax": None,
        "AveragePriceMin": None,
        "AveragePriceMax": None,
        "QtyOnPalletMin": None,
        "QtyOnPalletMax": None
    }
    # Znalezienie ID ofert
    with requests.Session() as session:
        response = session.post(URL, json=request, headers=headers).json()
    for pallet in response['data']['products']:
        pallet_id = pallet['id']

        # Znalezienie produktów oferty
        URL = f'https://sklepapi.miglo.pl/api/product/Specification/{pallet_id}'
        products = session.get(URL, headers=headers).json()['data']
    
        # Sprawdzenine słów w produktach
        word_set = set(word.lower() for word in words)
        find_words = {}
        for product in products:
            for word in word_set:
                if word in product['name'].lower():
                    find_words[word] = find_words.get(word, 0) + int(product['quantity'])

        # ID palet do kupienia
        if find_words != {}:
            pallets_to_buy["data"][pallet['productCode']] = {
                'price': pallet['priceGross'],
                "items": find_words,
            }

        # Stworzenie nowego JSON'a
        json_name = f'{current_time}-operation.json'
        with open(f'tests/operation_history_TEST/{json_name}', 'w', encoding='utf-8') as file:
            json.dump(pallets_to_buy, file, indent=4, ensure_ascii=False)
    return json_name


    
def summary():
    # Wczytanie pliku
    json_path = 'both_pallets.json'
    summary = 'Zakupiono za: 1000\n'
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # Sumowanie ceny
    summary_cost = ''
    for item in data.items():

    
        return
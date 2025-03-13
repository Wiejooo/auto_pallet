import requests
import json
import os

with open('test.json', 'r', encoding='utf-8') as file:
    pallets = json.load(file)

# print(pallets['data']['products'][0:5])

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
        "ItemsOnPage": 21,
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
    response.json() # TODO Zmień response na json i wyciągnij z niego informacje
    pallets = response['data']['products'][0]
    if response.status_code == 200:
        return f'Najnowsze palety: {pallets}'
    else:
        return 'Błąd przy sprawdzaniu najnowszych palet'
    
print(find_newest_pallet())



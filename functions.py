import requests
import json
import os

product_id = 62530
login_json_path = os.path.join(os.path.dirname(__file__), "..", "login_miglo.json")
with open(login_json_path, 'r', encoding="utf-8") as file:
    login_data = json.load(file)

def find_token():
    """Oddaje token"""
    login_url = 'https://sa.miglo.pl/api/account/login'
    login_data = {
        'Email': login_data['login'],
        'Password': login_data['password']
    }
    response = requests.post(login_url, json=login_data)
    if response.status_code == 200:
        token = response.json().get('data').get('token')
        return token
    else:
        return "Błąd przy logowaniu"


def add_to_card():
    login_url = 'https://sklepapi.miglo.pl/api/Cart/AddItem'
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
    response = requests.post(login_url, json=request, headers=headers)
    if response.status_code == 200:
        print(f'kod: {response.status_code}')
        print(f'treść: {response.json()}')
        return f'Status dodania do koszyka: {response.text}'
    else:
        print(f'kod: {response.status_code}')
        print(f'treść: {response.text}')
        return 'Błąd przy dodawaniu do koszyka'
    

# print(add_to_card())

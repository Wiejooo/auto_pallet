find = {'F12473':
    {
     'price': 4749.18,
     'items':
        {
         'statyw': 1,
         'teatr': 1,
         'dupa': 1,
        }
    }
}

result_lines = []
for pallet_name, data in find.items():
    title = f'{pallet_name} - {data["price"]}'
    items_str = ", ".join(f"{item}: {quantity}" for item, quantity in data["items"].items())
    result_lines.append(f"{title}\n{items_str}")


print(result_lines)
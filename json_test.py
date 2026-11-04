import json
my_data ={'name': 'Артас', 'hp': 100, 'gold': 50}
with open('json_save.py', 'w', encoding='utf-8') as f:
    json.dump(my_data,f, ensure_ascii=False, indent=4)
with open('json_save.py', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)
print(loaded_data['name'])
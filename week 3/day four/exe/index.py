import json

with open('/path/to/your/json/file.json', 'r') as file:
    family = json.load(file)

janes_children = family['Jane']['children']
for child in janes_children:
    print(f"Child name: {child['name']}")
    print(f"Child age: {child['age']}")
    print(f"Child favorite color: {child.get('favorite_color', 'N/A')}")
    print()


for child in janes_children:
    child['favorite_color'] = 'blue'  # Replace 'blue'

with open('/path/to/your/json/file.json', 'w') as file:
    json.dump(family, file, indent=4)
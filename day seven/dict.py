from email.headerregistry import Address


animals = ['cat', 'dog', 'fish', 'bird']

animals_dict = {'animalone': 'cat', 'animaltwo': 'dog', 'animalthree': 'fish', 'animalfour': 'bird'}

rick = {
    'first_name': 'Rick',
    'last_name': 'Sanchez',
    'Address': '1234 Main St',
    'city': 'Seattle',
}

morty = {
    'first_name': 'Morty',
    'last_name': 'Smith',
    'Address': '5678 Main St',
    'city': 'Seattle',
}


list = [{1,2} , {3,4} , {5,6}]

ricks_full_name = rick['first_name'] + ' ' + rick['last_name']

print(rick('first_name')) + ' ' + rick('last_name')

print(ricks_full_name)


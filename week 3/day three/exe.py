import os

base_dir = '.'
week_structure = {
    'week1': {
        'day1': ['lesson', 'homework'],
        'day2': [],
        'day3': []
    },
    'week2': {},
    'week3': {},
    'week4': {},
    'week5': {}
}

def create_directories(base, structure):
    for key, value in structure.items():
        if isinstance(value, dict):
            create_directories(os.path.join(base, key), value)
        else:
            for subfolder in value:
                os.makedirs(os.path.join(base, key, subfolder), exist_ok=True)

create_directories(base_dir, week_structure)
print("Directories created successfully!")

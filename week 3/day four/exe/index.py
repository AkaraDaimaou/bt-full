import json


# Read the contents of the file
with open('file.json', 'r') as file:
    data = json.load(file)

# Perform operations on the data
# ...

# Write the updated data back to the file
with open('file.json', 'w') as file:
    json.dump(data, file)
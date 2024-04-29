# kebab-case
# snake_case
# camelCase
# PascalCase

# Primitive types
test_string = "slkdfjklsdjflksd"
test_integer = 55
test_float = 0.39320489234
test_boolean = False
test_no_value = None

print(test_integer)
print(test_string)
print(test_float)
print(test_boolean)
print(test_no_value)

# Complex types
test_list = ['unstringounimporte', 'dsfgfdgdf','unstringounimporte', 'dsfgfdgdf','unstringounimporte', 'dsfgfdgdf','unstringounimporte', 'dsfgfdgdf']
# test_tuple = ['unstringounimporte', 'dsfgfdgdf']

print(test_list)
test_list[1]= "hello"
print(test_list)
# Add "good morning" to test_list
test_list.append("good morning")
# Print the new values
print(test_list)

print(test_list[1], test_list[2])
print(test_list[1:3])

# Create a list with values 1 - 20
test_numbers_list = [i for i in range(1, 51)] # list comprehension
print(test_numbers_list)

# Print odd numbers
count = 0
while count < 20:
    print(test_numbers_list[count])
    count += 2

# 0-based index

print(test_numbers_list[0:-1:2])
print(test_numbers_list[0:-1:2])
print(test_numbers_list[0:-1:2])
print(test_numbers_list[0:-1:2])
print(test_numbers_list[0:-1:2])
print(test_numbers_list[0:-1:2])


# Write a function that prints "MRU PYTHON 147 FULL TIME" 5x
def nomdelafonction(number=0):
    for _ in range(5):
        print(f"MRU PYTHON {number} FULL TIME")

nomdelafonction()
nomdelafonction(147)
nomdelafonction(150)
nomdelafonction(300)
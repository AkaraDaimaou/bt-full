import random

def display_message():
    print("I am learning Python programming in this course.")

display_message()



def favorite_book(title):
    print("One of my favorite books is", title)

favorite_book("harry potter and the chamber of secrets")




def describe_city(city, country="Unknown"):
    print(city, "is in", country)

describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")
describe_city("Tokyo")
describe_city("London", "United Kingdom")
describe_city("New York", "United States")



def compare_numbers(number):
    generated_number = random.randint(1, 100)
    if number == generated_number:
        print("Success! The generated number is also", number)
    else:
        print("Fail! The generated number is", generated_number, "and the input number is", number)

compare_numbers(46)



def make_shirt(size='large', message='I love Python'):
    print("The size of the shirt is", size, "and the text is", message)

make_shirt()
make_shirt('medium','good vibes only')
make_shirt('small', 'Hello World!')
# Exercise 1: Hello World
print("Hello world\n" * 4)

# Exercise 2: Some Math
result = (99 ** 3) * 8
print(result)

# Exercise 3: What Is The Output?
print(5 < 3)  # False
print(3 == 3)  # True
print(3 == "3")  # False
print("3" > 3)  # Error: '>' not supported between instances of 'str' and 'int'
print("Hello" == "hello")  # False

# Exercise 4: Your Computer Brand
computer_brand = "Your computer brand"
print(f"I have a {computer_brand} computer")

# Exercise 5: Your Information
name = "Your name"
age = 0  # Your age
shoe_size = 0  # Your shoe size
info = f"My name is {name}, I am {age} years old, and my shoe size is {shoe_size}"
print(info)

# Exercise 6: A & B
a = 0  # Your number
b = 0  # Your number
if a > b:
    print("Hello World")

# Exercise 7: Odd Or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Exercise 8: What's Your Name?
user_name = input("What's your name? ")
if user_name == "Your name":
    print("Hey, we have the same name!")

# Exercise 9: Tall Enough To Ride A Roller Coaster
height = int(input("Enter your height in centimeters: "))
if height > 145:
    print("You are tall enough to ride!")
else:
    print("You need to grow some more to ride.")
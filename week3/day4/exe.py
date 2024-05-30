count = {}
words = []

with open('', 'r') as file:
    lines = file.readlines()

for index, line in enumerate(lines):
    print(line)
    
    if index == 4:
        print(line)
    
    print(line[:5])
    
    words.extend(line.split())

count['Darth'] = words.count('Darth')
count['Luke'] = words.count('Luke')
count['Lea'] = words.count('Lea')
print(count)

with open('../filetext.txt', 'a') as file:
    file.write('YourFirstName\n')

with open('', 'r+') as file:
    content = file.read()
    content = content.replace('Luke', 'Luke Skywalker')
    file.seek(0)
    file.write(content)
    file.truncate()

# Reading files
with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)

# Read line by line
with open('sample.txt', 'r') as file:
    for line in file:
        print(line.strip())
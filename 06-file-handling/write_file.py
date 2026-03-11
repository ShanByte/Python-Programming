with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new file.\n")

# Append to file
with open('output.txt', 'a') as file:
    file.write("Appending new line.\n")

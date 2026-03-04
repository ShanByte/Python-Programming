squares = []
for x in range(10):
    squares.append(x * x)

even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x * x)

square_dict = {}
for x in range(5):
    square_dict[x] = x * x

print("Squares:", squares)
print("Even squares:", even_squares)
print("Square dict:", square_dict)

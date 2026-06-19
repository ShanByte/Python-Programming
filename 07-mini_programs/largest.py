n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    numbers.append(int(input()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element:", largest)

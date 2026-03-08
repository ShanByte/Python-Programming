def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"Factorial of 5: {factorial(5)}")
print(f"Fibonacci 7: {fibonacci(7)}")

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def main():
    print("Factorial Calculator")
    number = int(input("Enter a number: "))
    
    if number < 0:
        print("Factorial not defined for negative numbers!")
    else:
        result = factorial_iterative(number)
        print(f"\n{number}! = {result}")

if __name__ == "__main__":
    main()
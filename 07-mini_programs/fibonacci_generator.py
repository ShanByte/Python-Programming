def fibonacci(n):
    sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    
    return sequence

def main():
    print("🔢 Fibonacci Sequence Generator")
    n = int(input("How many terms? "))
    
    fib_sequence = fibonacci(n)
    print(f"\n First {n} Fibonacci numbers:")
    print(fib_sequence)

if __name__ == "__main__":
    main()
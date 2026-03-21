def generate_table(number, range_end=10):
    print(f"\nMultiplication Table for {number}")
    print("=" * 25)
    
    for i in range(1, range_end + 1):
        result = number * i
        print(f"{number} × {i:2d} = {result:3d}")

def main():
    print("Multiplication Table Generator")
    number = int(input("Enter a number: "))
    range_end = int(input("Up to which number? (default 10): ") or 10)
    
    generate_table(number, range_end)

if __name__ == "__main__":
    main()
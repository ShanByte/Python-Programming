def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def binary_to_decimal(binary):
    return int(binary, 2)

def main():
    print("Binary ↔ Decimal Converter")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    
    choice = input("\nChoose option: ")
    
    if choice == '1':
        decimal = int(input("Enter decimal number: "))
        binary = decimal_to_binary(decimal)
        print(f"\n{decimal} in binary: {binary}")
    
    elif choice == '2':
        binary = input("Enter binary number: ")
        try:
            decimal = binary_to_decimal(binary)
            print(f"\n{binary} in decimal: {decimal}")
        except ValueError:
            print("Invalid binary number!")

if __name__ == "__main__":
    main()
def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number

def main():
    print("Armstrong Number Checker")
    number = int(input("Enter a number: "))
    
    if is_armstrong(number):
        print(f"{number} is an Armstrong number!")
    else:
        print(f"{number} is not an Armstrong number!")
    
    # Show some examples
    print("\nArmstrong numbers up to 1000:")
    armstrong_nums = [n for n in range(1, 1001) if is_armstrong(n)]
    print(armstrong_nums)

if __name__ == "__main__":
    main()
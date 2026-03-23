def check_even_odd(number):
    return "Even" if number % 2 == 0 else "Odd"

def main():
    print("Even/Odd Checker")
    number = int(input("Enter a number: "))
    
    result = check_even_odd(number)
    print(f"\n{number} is {result}!")

if __name__ == "__main__":
    main()
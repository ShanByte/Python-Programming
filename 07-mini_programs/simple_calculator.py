def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /, %, **")
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter second number: "))
        
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        elif operator == '%':
            result = num1 % num2
        elif operator == '**':
            result = num1 ** num2
        else:
            result = "Invalid operator"
        
        print(f"\nResult: {num1} {operator} {num2} = {result}")
    
    except ValueError:
        print("Invalid input!")

if __name__ == "__main__":
    calculator()
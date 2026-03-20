def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def main():
    print("Simple Interest Calculator")
    
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest (%): "))
    time = float(input("Enter time period (years): "))
    
    interest = calculate_simple_interest(principal, rate, time)
    total = principal + interest
    
    print(f"\nResults:")
    print(f"Principal: ${principal:.2f}")
    print(f"Interest: ${interest:.2f}")
    print(f"Total Amount: ${total:.2f}")

if __name__ == "__main__":
    main()
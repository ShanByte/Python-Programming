def calculate_emi(principal, rate, time_months):
    # Monthly interest rate
    r = rate / (12 * 100)
    
    # EMI formula
    emi = (principal * r * (1 + r)**time_months) / ((1 + r)**time_months - 1)
    
    return emi

def main():
    print("Loan EMI Calculator")
    
    principal = float(input("Enter loan amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = float(input("Enter loan tenure (years): "))
    
    time_months = int(years * 12)
    emi = calculate_emi(principal, rate, time_months)
    total_payment = emi * time_months
    total_interest = total_payment - principal
    
    print(f"\nLoan Details:")
    print(f"Monthly EMI: ${emi:.2f}")
    print(f"Total Payment: ${total_payment:.2f}")
    print(f"Total Interest: ${total_interest:.2f}")

if __name__ == "__main__":
    main()
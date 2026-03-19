def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        return None
    
    # Convert to USD first, then to target currency
    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]
    return converted

def main():
    # Exchange rates relative to USD
    rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.73,
        'INR': 83.12,
        'JPY': 110.0
    }
    
    print("Currency Converter")
    print(f"Available currencies: {', '.join(rates.keys())}")
    
    amount = float(input("\nEnter amount: "))
    from_curr = input("From currency: ").upper()
    to_curr = input("To currency: ").upper()
    
    result = convert_currency(amount, from_curr, to_curr, rates)
    
    if result:
        print(f"\n{amount} {from_curr} = {result:.2f} {to_curr}")
    else:
        print("Invalid currency!")

if __name__ == "__main__":
    main()
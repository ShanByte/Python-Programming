def number_to_words(n):
    ones = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 
             'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    
    if n == 0:
        return 'Zero'
    
    if n < 10:
        return ones[n]
    elif n < 20:
        return teens[n - 10]
    elif n < 100:
        return tens[n // 10] + (' ' + ones[n % 10] if n % 10 != 0 else '')
    elif n < 1000:
        return ones[n // 100] + ' Hundred' + (' ' + number_to_words(n % 100) if n % 100 != 0 else '')
    
    return str(n)

def main():
    print("Number to Words Converter")
    number = int(input("Enter a number (0-999): "))
    
    if 0 <= number <= 999:
        words = number_to_words(number)
        print(f"\n{number} in words: {words}")
    else:
        print("Please enter a number between 0 and 999!")

if __name__ == "__main__":
    main()
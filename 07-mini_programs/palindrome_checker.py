def is_palindrome(text):
    cleaned = ''.join(text.split()).lower()
    return cleaned == cleaned[::-1]

def main():
    print("Palindrome Checker")
    text = input("Enter a word or phrase: ")
    
    if is_palindrome(text):
        print(f"'{text}' is a palindrome!")
    else:
        print(f"'{text}' is not a palindrome!")

if __name__ == "__main__":
    main()
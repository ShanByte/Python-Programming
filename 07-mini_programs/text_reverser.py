def reverse_text(text):
    return text[::-1]

def reverse_words(text):
    words = text.split()
    return ' '.join(reversed(words))

def main():
    print("Text Reverser")
    print("1. Reverse entire text")
    print("2. Reverse word order")
    
    choice = input("\nChoose option: ")
    text = input("Enter text: ")
    
    if choice == '1':
        result = reverse_text(text)
        print(f"\nReversed: {result}")
    elif choice == '2':
        result = reverse_words(text)
        print(f"\nReversed words: {result}")

if __name__ == "__main__":
    main()
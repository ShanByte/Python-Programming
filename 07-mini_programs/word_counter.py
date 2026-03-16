def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text, include_spaces=True):
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))

def main():
    print("Word and Character Counter")
    text = input("Enter your text: ")
    
    words = count_words(text)
    chars_with_spaces = count_characters(text, True)
    chars_without_spaces = count_characters(text, False)
    
    print(f"\n Statistics:")
    print(f"Words: {words}")
    print(f"Characters (with spaces): {chars_with_spaces}")
    print(f"Characters (without spaces): {chars_without_spaces}")

if __name__ == "__main__":
    main()
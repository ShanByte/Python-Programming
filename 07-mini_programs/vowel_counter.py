def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in text if char in vowels)
    return count

def main():
    print("Vowel Counter")
    text = input("Enter a text: ")
    
    vowel_count = count_vowels(text)
    consonant_count = sum(1 for char in text if char.isalpha()) - vowel_count
    
    print(f"\nResults:")
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")

if __name__ == "__main__":
    main()
def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

def main():
    print("Anagram Checker")
    str1 = input("Enter first word/phrase: ")
    str2 = input("Enter second word/phrase: ")
    
    if are_anagrams(str1, str2):
        print(f"'{str1}' and '{str2}' are anagrams!")
    else:
        print(f"'{str1}' and '{str2}' are not anagrams!")

if __name__ == "__main__":
    main()
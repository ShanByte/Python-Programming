import random
import string

def generate_password(length=12, use_special=True):
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter password length (8-32): "))
    special = input("Include special characters? (y/n): ").lower() == 'y'
    
    if 8 <= length <= 32:
        password = generate_password(length, special)
        print(f"\nGenerated Password: {password}")
    else:
        print("Length must be between 8 and 32!")

if __name__ == "__main__":
    main()
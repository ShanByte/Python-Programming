import random

def get_random_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "It is during our darkest moments that we must focus to see the light. - Aristotle",
        "The only impossible journey is the one you never begin. - Tony Robbins",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "Success is not final, failure is not fatal. - Winston Churchill",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Code is like humor. When you have to explain it, it's bad. - Cory House"
    ]
    
    return random.choice(quotes)

def main():
    print("Random Quote Generator\n")
    
    while True:
        print(f"{get_random_quote()}\n")
        
        again = input("Get another quote? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
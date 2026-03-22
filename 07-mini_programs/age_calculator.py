from datetime import datetime

def calculate_age(birth_year, birth_month, birth_day):
    today = datetime.today()
    birth_date = datetime(birth_year, birth_month, birth_day)
    
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

def main():
    print("Age Calculator")
    
    year = int(input("Enter birth year: "))
    month = int(input("Enter birth month (1-12): "))
    day = int(input("Enter birth day: "))
    
    age = calculate_age(year, month, day)
    print(f"\nYou are {age} years old!")

if __name__ == "__main__":
    main()
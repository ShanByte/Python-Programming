def calculate_bmi(weight, height):
    """Weight in kg, height in meters"""
    return weight / (height ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("BMI Calculator")
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))
    
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    
    print(f"\n Your BMI: {bmi:.2f}")
    print(f"Category: {category}")

if __name__ == "__main__":
    main()
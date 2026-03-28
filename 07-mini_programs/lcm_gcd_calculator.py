import math

def find_gcd(a, b):
    return math.gcd(a, b)

def find_lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def main():
    print("LCM & GCD Calculator")
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    gcd = find_gcd(num1, num2)
    lcm = find_lcm(num1, num2)
    
    print(f"\nResults:")
    print(f"GCD of {num1} and {num2}: {gcd}")
    print(f"LCM of {num1} and {num2}: {lcm}")

if __name__ == "__main__":
    main()
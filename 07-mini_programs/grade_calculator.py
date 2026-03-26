def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

def main():
    print("Grade Calculator")
    
    subjects = int(input("How many subjects? "))
    total_marks = 0
    
    for i in range(1, subjects + 1):
        marks = float(input(f"Enter marks for subject {i}: "))
        total_marks += marks
    
    percentage = (total_marks / (subjects * 100)) * 100
    grade = calculate_grade(percentage)
    
    print(f"\nResults:")
    print(f"Total Marks: {total_marks}/{subjects * 100}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
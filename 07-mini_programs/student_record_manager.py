def add_student(students):
    name = input("Enter student name: ")
    marks = []

    for i in range(3):
        mark = int(input(f"Enter mark {i+1}: "))
        marks.append(mark)

    students[name] = marks
    print(f"{name} added successfully!\n")


def calculate_average(marks):
    return sum(marks) / len(marks)


def display_students(students):
    if not students:
        print("No student records found.\n")
        return

    for name, marks in students.items():
        avg = calculate_average(marks)
        print(f"Name: {name}")
        print(f"Marks: {marks}")
        print(f"Average: {avg:.2f}")

        if avg >= 75:
            print("Grade: A")
        elif avg >= 50:
            print("Grade: B")
        else:
            print("Grade: C")
        print()


def find_topper(students):
    topper = ""
    highest = 0

    for name, marks in students.items():
        avg = calculate_average(marks)
        if avg > highest:
            highest = avg
            topper = name

    if topper:
        print(f"Topper: {topper} with average {highest:.2f}\n")


students = {}

while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Topper")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        display_students(students)
    elif choice == "3":
        find_topper(students)
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")

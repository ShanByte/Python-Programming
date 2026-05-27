salary = float(input("Enter the salary: "))
gender = input("Enter the gender (M,F): ").upper()
if gender == "M":
  bonus = salary * 0.05
elif gender == "F":
  bonus = salary * 0.10
else:
  bonus = 0
  print("Invalid Gender")

if salary < 10000:
  bonus += salary * 0.02

print("Bonus: ", bonus)
print("Salary: ", salary)
print("Total salary: ", salary + bonus)

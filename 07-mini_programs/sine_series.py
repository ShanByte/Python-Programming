import math
terms = int(input("Enter the number of terms: "))
degree = float(input("Enter the degree of angle: "))
x = math.radians(degree)
sum = 0


for i in range (terms):
  power = (2*i)+1

  current_term = (x**power)/math.factorial(power)

  if i % 2 == 0 :
    sum = sum + current_term
  else:
    sum = sum - current_term

  print("The sine series is: ", sum)

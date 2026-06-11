year = int(input("Entee a year: "))
if(year%400 ==0) or (year%4 == 0 and year %10 != 0 ):
  print("Leap Year")
else:
  print("Not Leap Year")

print("Leap years from 1900 to 2101 are : ")
for i in range(1900,2102):
  if(i % 400 == 0) or (i % 4 ==0 and i %100 !=0):
    print(i)

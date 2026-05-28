exam1 = float(input("Enter the marks of exam1: "))
exam2 = float(input("Enter the marks of exam2: "))

sports = float(input("Enter the marks of sports: "))

activity1 = float(input("Enter the marks of activity1: "))
activity2 = float(input("Enter the marks of activity2: "))
activity3 = float(input("Enter the marks of activity3: "))


avg_exam = (exam1 + exam2)/2
avg_act = (activity1 + activity2 + activity3)/3

result = ((avg_exam*0.50) + (sports * 0.20) + (avg_act*0.30))

print ("Result: ",result , "%")
